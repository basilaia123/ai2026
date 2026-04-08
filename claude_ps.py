"""
Claude Code Monitor
====================
Tails Claude Code's JSONL transcript in real-time.
Shows all tool calls (Bash, Read, Write, Edit, Grep, Glob) with outputs.
Auto-switches to new sessions. Logs to file.

Run: python claude_ps_demo.py
Stop: Ctrl+C
"""
import json
import glob
import time
import os
from datetime import datetime

PROJ_DIR = os.path.expanduser(
    "~/.claude/projects/C--Users-GBASILAIA-claude-ai2026"
)
LOG_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "claude_monitor.log"
)

TOOL_COLORS = {
    "Bash":  ("$", "96"),
    "Read":  ("R", "94"),
    "Write": ("W", "95"),
    "Edit":  ("E", "95"),
    "Grep":  ("?", "93"),
    "Glob":  ("G", "93"),
    "Task":  ("T", "92"),
}

def find_latest_jsonl():
    files = glob.glob(os.path.join(PROJ_DIR, "*.jsonl"))
    if not files:
        return None
    return max(files, key=os.path.getmtime)

def parse_line(line):
    """Parse JSONL line. Returns list of events."""
    try:
        obj = json.loads(line)
    except json.JSONDecodeError:
        return None

    obj_type = obj.get("type")
    timestamp = obj.get("timestamp", "")
    events = []

    # Assistant message with tool_use(s)
    if obj_type == "assistant":
        for block in obj.get("message", {}).get("content", []):
            if block.get("type") == "tool_use":
                tool_name = block.get("name", "")
                if tool_name not in TOOL_COLORS:
                    continue
                inp = block.get("input", {})
                tool_id = block.get("id", "")

                if tool_name == "Bash":
                    detail = inp.get("command", "")
                    desc = inp.get("description", "")
                elif tool_name == "Read":
                    detail = inp.get("file_path", "")
                    desc = ""
                elif tool_name == "Write":
                    detail = inp.get("file_path", "")
                    desc = ""
                elif tool_name == "Edit":
                    fp = inp.get("file_path", "")
                    old = inp.get("old_string", "")[:50]
                    detail = f"{fp}  [{old}...]"
                    desc = ""
                elif tool_name == "Grep":
                    pattern = inp.get("pattern", "")
                    path = inp.get("path", "")
                    detail = f'"{pattern}" in {path}' if path else f'"{pattern}"'
                    desc = ""
                elif tool_name == "Glob":
                    detail = inp.get("pattern", "")
                    desc = ""
                elif tool_name == "Task":
                    detail = inp.get("description", "")
                    desc = inp.get("subagent_type", "")
                else:
                    detail = str(inp)[:100]
                    desc = ""

                events.append({
                    "kind": "cmd",
                    "tool_name": tool_name,
                    "detail": detail,
                    "desc": desc,
                    "tool_id": tool_id,
                    "timestamp": timestamp,
                })

    # Tool result (user type message)
    if obj_type == "user":
        for block in obj.get("message", {}).get("content", []):
            if isinstance(block, dict) and block.get("type") == "tool_result":
                tool_id = block.get("tool_use_id", "")
                is_error = block.get("is_error", False)

                # message.content[0].content is always a string for all tools
                content = block.get("content", "")
                if isinstance(content, list):
                    texts = []
                    for item in content:
                        if isinstance(item, dict) and item.get("type") == "text":
                            texts.append(item.get("text", ""))
                    content = "\n".join(texts)
                output = content.strip() if content else ""

                events.append({
                    "kind": "result",
                    "output": output,
                    "is_error": is_error,
                    "tool_id": tool_id,
                    "timestamp": timestamp,
                })
                break  # one result per message

    return events if events else None

def fmt_time(iso_ts):
    try:
        dt = datetime.fromisoformat(iso_ts.replace("Z", "+00:00"))
        return dt.strftime("%H:%M:%S")
    except Exception:
        return datetime.now().strftime("%H:%M:%S")

def log_to_file(logf, text):
    logf.write(text + "\n")
    logf.flush()

def main():
    print()
    print("  \033[92m===== Claude Code Monitor =====\033[0m")
    print("  \033[90mAll tools | Auto-session | Timer | Log\033[0m")
    print("  \033[90mCtrl+C to stop\033[0m")
    print()

    logf = open(LOG_FILE, "a", encoding="utf-8")
    logf.write(f"\n{'=' * 50}\n")
    logf.write(f"Session started: {datetime.now()}\n")
    logf.write(f"{'=' * 50}\n\n")

    current_jsonl = None
    f = None
    cmd_counter = 0
    # Track command timestamps by tool_id for duration
    pending = {}  # tool_id -> (cmd_counter, time.time())

    try:
        while True:
            latest = find_latest_jsonl()
            if latest != current_jsonl:
                if f:
                    f.close()
                current_jsonl = latest
                if not current_jsonl:
                    time.sleep(1)
                    continue
                f = open(current_jsonl, "r", encoding="utf-8")
                f.seek(0, 2)
                basename = os.path.basename(current_jsonl)
                print(f"  \033[90mTailing: {basename}\033[0m")
                log_to_file(logf, f"Tailing: {basename}")
                print()

            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue

            events = parse_line(line.strip())
            if not events:
                continue

            for ev in events:
                if ev["kind"] == "cmd":
                    cmd_counter += 1
                    ts = fmt_time(ev["timestamp"])
                    tool_name = ev["tool_name"]
                    detail = ev["detail"]
                    desc = ev["desc"]
                    tool_id = ev["tool_id"]
                    icon, color = TOOL_COLORS.get(tool_name, ("?", "37"))

                    pending[tool_id] = (cmd_counter, time.time())

                    if len(detail) > 300:
                        detail = detail[:300] + " ..."

                    desc_part = f" \033[90m# {desc}\033[0m" if desc else ""
                    print(f"  \033[90m─────\033[0m")
                    print(f"  \033[90m[{ts}]\033[0m \033[92m#{cmd_counter}\033[0m \033[{color}m[{tool_name}]\033[0m{desc_part}")
                    print(f"  \033[{color}m{icon} {detail}\033[0m")

                    desc_log = f" # {desc}" if desc else ""
                    log_to_file(logf, f"[{ts}] #{cmd_counter} [{tool_name}]{desc_log}")
                    log_to_file(logf, f"{icon} {detail}")

                elif ev["kind"] == "result":
                    output = ev["output"]
                    is_error = ev["is_error"]
                    tool_id = ev["tool_id"]

                    # Duration and command reference
                    duration_str = ""
                    duration_log = ""
                    ref_prefix = ""
                    if tool_id in pending:
                        cmd_num, start_t = pending.pop(tool_id)
                        elapsed = time.time() - start_t
                        duration_str = f" \033[90m({elapsed:.1f}s)\033[0m"
                        duration_log = f" ({elapsed:.1f}s)"
                        ref_prefix = f"\033[90m← #{cmd_num} \033[0m"

                    if output:
                        lines = output.split('\n')
                        if len(lines) > 15:
                            display = '\n'.join(lines[:15])
                            display += f'\n  ... ({len(lines)} lines total)'
                        elif len(lines) == 1:
                            display = output
                        else:
                            display = output

                        if len(lines) == 1:
                            # Single line result - compact
                            color_code = "91" if is_error else "93"
                            print(f"  {ref_prefix}\033[{color_code}m→ {display}\033[0m{duration_str}")
                        else:
                            # Multi-line result
                            if ref_prefix:
                                print(f"  {ref_prefix}")
                            color_code = "91" if is_error else "93"
                            print(f"  \033[{color_code}m{display}\033[0m{duration_str}")
                        log_to_file(logf, output[:500] + duration_log)
                    else:
                        print(f"  {ref_prefix}\033[90m→ (no output)\033[0m{duration_str}")
                        log_to_file(logf, f"(no output){duration_log}")
                    print()
                    log_to_file(logf, "")

    except KeyboardInterrupt:
        if f:
            f.close()
        print(f"\n\033[90m  Stopped. Total: {cmd_counter} tool calls\033[0m")
        log_to_file(logf, f"\nStopped. Total: {cmd_counter} tool calls")
        logf.close()
        print(f"  \033[90mLog: {LOG_FILE}\033[0m")

if __name__ == "__main__":
    main()
