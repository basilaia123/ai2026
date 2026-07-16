"""Parse day1/day2 slide HTML into structured JSON.

The HTML is malformed: slide-8 is missing its closing </div>, so 39 subsequent
slide divs are technically nested inside it. We treat each <div class="slide" id="slide-N">
as a top-level slide regardless of DOM nesting. For slide content, we only take
direct children that are NOT themselves .slide divs.
"""
import json
import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag


def text_of(node) -> str:
    if node is None:
        return ""
    parts = []
    for desc in node.descendants:
        if isinstance(desc, NavigableString):
            parts.append(str(desc))
    s = " ".join(parts)
    return re.sub(r"\s+", " ", s).strip()


def block_to_dict(el: Tag):
    """Convert a single block element (direct child of slide-content) into a typed dict.
    Skips nested .slide divs — those are siblings, not children.
    """
    name = el.name
    cls = el.get("class") or []

    # Skip nested slide divs entirely
    if name == "div" and "slide" in cls:
        return None

    if name == "h3":
        return {"type": "h3", "text": text_of(el)}
    if name == "h4":
        return {"type": "h4", "text": text_of(el)}
    if name == "p":
        return {"type": "p", "text": text_of(el)}
    if name == "pre":
        code_text = el.get_text("\n")
        return {"type": "code", "text": code_text.rstrip()}
    if name == "ul":
        items = [text_of(li) for li in el.find_all("li", recursive=False)]
        return {"type": "list", "ordered": False, "items": items}
    if name == "ol":
        items = [text_of(li) for li in el.find_all("li", recursive=False)]
        return {"type": "list", "ordered": True, "items": items}
    if name == "table":
        rows = []
        for tr in el.find_all("tr"):
            cells = [text_of(c) for c in tr.find_all(["td", "th"])]
            rows.append(cells)
        return {"type": "table", "rows": rows}
    if name == "div":
        # Layout containers: highlight-box, warning-box, key-points, prompt-box, cards-grid, two-column, card-item
        # Recurse into children to capture sub-blocks
        sub_blocks = []
        # First, check for bare text content (text directly inside the div, not wrapped in tags)
        bare_text_parts = []
        for child in el.children:
            if isinstance(child, Tag):
                if child.name == "div" and "slide" in (child.get("class") or []):
                    continue
                sub = block_to_dict(child)
                if sub is not None:
                    sub_blocks.append(sub)
            elif isinstance(child, NavigableString):
                txt = str(child).strip()
                if txt:
                    bare_text_parts.append(txt)
        # If we found bare text (e.g. prompt-box with naked prompt), append as a code/p block
        if bare_text_parts:
            combined = " ".join(bare_text_parts)
            # If this is a prompt-box, mark as code (mono); otherwise as paragraph
            if "prompt" in (el.get("class") or [""])[0] if el.get("class") else False:
                sub_blocks.append({"type": "code", "text": combined})
            else:
                sub_blocks.append({"type": "p", "text": combined})

        layout = " ".join(cls) if cls else "div"
        # If single paragraph, hoist it up
        if len(sub_blocks) == 1 and sub_blocks[0]["type"] in ("p", "list", "h4"):
            return sub_blocks[0]
        if not sub_blocks:
            return {"type": "box", "class": layout, "text": text_of(el)}
        return {"type": "box", "class": layout, "blocks": sub_blocks}
    # fallback
    return {"type": name, "text": text_of(el)}


def parse_slide(slide_el: Tag):
    num_el = slide_el.find("div", class_="slide-num")
    number = None
    if num_el:
        m = re.match(r"\s*(\d+)", num_el.get_text())
        if m:
            number = int(m.group(1))
    h2 = slide_el.find("h2", recursive=False)
    title = text_of(h2) if h2 else ""

    blocks = []
    container = slide_el.find("div", class_="slide-content")
    if container is None:
        container = slide_el

    for child in container.children:
        if not isinstance(child, Tag):
            continue
        if child.name == "div" and "slide-num" in (child.get("class") or []):
            continue
        if child.name == "h2":
            continue
        d = block_to_dict(child)
        if d is not None:
            blocks.append(d)

    return {"number": number, "title": title, "blocks": blocks}


def infer_kind(slide):
    title = (slide.get("title") or "")
    title_l = title.lower()
    blocks = slide.get("blocks", [])
    has_list = any(b.get("type") == "list" for b in blocks)
    has_code = any(b.get("type") == "code" for b in blocks)
    has_table = any(b.get("type") == "table" for b in blocks)
    has_h4 = any(b.get("type") == "h4" for b in blocks)
    info = {
        "has_list": has_list,
        "has_code": has_code,
        "has_table": has_table,
        "block_count": len(blocks),
    }
    kind = "content"
    if not title:
        kind = "blank"
    elif any(k in title_l for k in ["მისალმება", "welcome", "შესავალი"]):
        kind = "cover"
    elif "agenda" in title_l or "განრიგი" in title_l or "გეგმა" in title_l:
        kind = "agenda"
    elif "?" in title or title.endswith("?"):
        kind = "question"
    elif any(k in title_l for k in ["შეჯამება", "summary", "დასკვნა", "wrap"]):
        kind = "summary"
    elif any(k in title_l for k in ["პრაქტიკა", "exercise", "ამოცანა", "დავალება"]):
        kind = "exercise"
    elif has_table:
        kind = "table"
    elif has_code:
        kind = "code"
    elif has_list and len(blocks) == 1:
        kind = "list"
    slide["kind"] = kind
    slide["info"] = info
    return slide


def main():
    src = Path(sys.argv[1])
    out = Path(sys.argv[2])
    raw = src.read_text(encoding="utf-8")
    soup = BeautifulSoup(raw, "html.parser")

    slides = []
    seen_ids = set()
    for slide_el in soup.find_all("div", class_="slide"):
        sid = slide_el.get("id") or ""
        if sid in seen_ids:
            continue
        seen_ids.add(sid)
        slides.append(parse_slide(slide_el))

    # Sort by number
    slides.sort(key=lambda s: (s.get("number") or 0, s.get("title") or ""))
    for i, s in enumerate(slides, 1):
        s["index"] = i
        infer_kind(s)

    out.write_text(json.dumps(slides, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{src.name}: extracted {len(slides)} slides -> {out}")


if __name__ == "__main__":
    main()