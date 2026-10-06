"""RSS headlines. Network calls are mocked."""

import requests

from sources.news import fetch_news, format_headlines


FEED_A = b"""<?xml version="1.0"?>
<rss version="2.0"><channel>
<item><title>One</title><link>https://example.com/1</link></item>
<item><title>Duplicate</title><link>https://example.com/1</link></item>
<item><title></title><link>https://example.com/blank</link></item>
<item><title>No link</title></item>
<item><title>Two</title><link>https://example.com/2</link></item>
</channel></rss>
"""

FEED_B = b"""<?xml version="1.0"?>
<rss version="2.0"><channel>
<item><title>Three</title><link>https://example.com/3</link></item>
<item><title>One again</title><link>https://example.com/1</link></item>
</channel></rss>
"""


class Response:
    def __init__(self, content: bytes, status_code: int = 200) -> None:
        self.content = content
        self.status_code = status_code


def test_dedup_and_skip_entries_without_a_title_or_link(monkeypatch):
    def get(url, timeout, headers):
        assert timeout == 10
        assert headers["User-Agent"] == "morning-briefing/1.0"
        return Response(FEED_A if url.endswith("/a") else FEED_B)

    monkeypatch.setattr("sources.news.requests.get", get)
    items = fetch_news(
        [{"name": "BBC World", "url": "https://feeds.example/a"}, {"name": "Hacker News", "url": "https://feeds.example/b"}],
        per_feed=5,
    )
    assert [(item["title"], item["source"]) for item in items] == [
        ("One", "BBC World"),
        ("Two", "BBC World"),
        ("Three", "Hacker News"),
    ]


def test_one_feed_error_keeps_the_others(monkeypatch):
    def get(url, timeout, headers):
        if url.endswith("/bad"):
            raise requests.ConnectionError("down")
        return Response(FEED_B)

    monkeypatch.setattr("sources.news.requests.get", get)
    items = fetch_news(
        [{"name": "Broken", "url": "https://feeds.example/bad"}, {"name": "TechCrunch", "url": "https://feeds.example/b"}],
        per_feed=5,
    )
    assert [item["title"] for item in items] == ["Three", "One again"]


def test_every_feed_failing_returns_an_empty_list(monkeypatch):
    def get(url, timeout, headers):
        raise requests.Timeout("slow")

    monkeypatch.setattr("sources.news.requests.get", get)
    assert fetch_news([{"name": "BBC World", "url": "https://feeds.example/a"}], per_feed=5) == []


def test_headlines_keep_five_links_and_the_source_name():
    items = [
        {"title": f"Story {index}", "link": f"https://example.com/{index}", "source": "BBC World"}
        for index in range(1, 8)
    ]
    text = format_headlines(items, 5)
    assert text.startswith("📰 სიახლეები")
    assert "Story 5 (BBC World)" in text
    assert "https://example.com/5" in text
    assert "Story 6" not in text
    assert format_headlines([], 5) == "სიახლეები: მიუწვდომელია"
