#!/usr/bin/env python3
# telegram_html_to_txt.py
# Usage: python telegram_html_to_txt.py messages.html messages.txt

import sys
from bs4 import BeautifulSoup


def visible_text(el):
    """Return cleaned visible text, preserving intentional line breaks."""
    text = el.get_text(separator="\n")
    lines = [line.strip() for line in text.splitlines()]
    return "\n".join(line for line in lines if line)


def media_placeholders(msg_el):
    placeholders = []
    # images
    for img in msg_el.find_all("img"):
        src = img.get("src") or img.get("data-src") or ""
        if src:
            placeholders.append(f"[IMAGE: {src.split('/')[-1]}]")
    # links to files
    for a in msg_el.find_all("a", href=True):
        href = a["href"]
        # heuristic: file link often points to 'media' or has file extension
        if any(
            href.lower().endswith(ext)
            for ext in (
                ".jpg",
                ".jpeg",
                ".png",
                ".gif",
                ".mp4",
                ".mkv",
                ".mp3",
                ".ogg",
                ".webm",
                ".pdf",
                ".zip",
            )
        ):
            placeholders.append(f"[FILE: {href.split('/')[-1]}]")
    return " ".join(dict.fromkeys(placeholders))  # unique & preserve order


def extract_messages(soup):
    out = []
    # heuristic: messages are top-level divs with class "message"
    candidates = soup.find_all(
        lambda tag: tag.name == "div" and "message" in (tag.get("class") or [])
    )
    if not candidates:
        # Fallback: look for divs whose id starts with "message"
        candidates = soup.find_all(
            lambda tag: tag.name == "div"
            and str(tag.get("id", "")).startswith("message")
        )
    for m in candidates:
        # find sender
        sender = None
        date = None
        text_el = None

        sender_el = m.find(class_="from_name") or m.find(
            lambda t: t.name in ("span", "div")
            and "from" in " ".join(t.get("class") or [])
        )
        if sender_el:
            sender = sender_el.get_text(strip=True)
        date_el = m.find(class_="date") or m.find(
            lambda t: t.name in ("span", "div")
            and "date" in " ".join(t.get("class") or [])
        )
        if date_el:
            date = date_el.get_text(strip=True)
        # message text
        text_el = m.find(class_="text") or m.find("p") or m.find("div", recursive=True)
        if text_el:
            txt = visible_text(text_el)
        else:
            txt = visible_text(m)

        media = media_placeholders(m)
        out.append(
            {
                "sender": sender or "Unknown",
                "date": date or "",
                "text": txt or "",
                "media": media,
            }
        )
    return out


def main():
    if len(sys.argv) < 3:
        print("Usage: telegram_html_to_txt.py input.html output.txt")
        sys.exit(1)
    infile, outfile = sys.argv[1], sys.argv[2]
    with open(infile, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    msgs = extract_messages(soup)

    with open(outfile, "w", encoding="utf-8") as f:
        for m in msgs:
            header = f"{m['sender']}"
            if m["date"]:
                header += f" — {m['date']}"
            f.write(header + "\n")
            if m["text"]:
                f.write(m["text"].strip() + "\n")
            if m["media"]:
                f.write(m["media"] + "\n")
            f.write("\n")

    print(f"Wrote {len(msgs)} message(s) to {outfile}")


if __name__ == "__main__":
    main()
