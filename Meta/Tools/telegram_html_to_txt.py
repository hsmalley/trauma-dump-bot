#!/usr/bin/env python3
# telegram_html_to_txt.py
# Usage: python telegram_html_to_txt.py messages.html messages.txt

import sys
from bs4 import BeautifulSoup, NavigableString, Tag

def visible_text(el):
    """Return reasonably cleaned visible text from element, preserving newlines."""
    parts = []
    for node in el.descendants:
        if isinstance(node, NavigableString):
            text = str(node).strip()
            if text:
                parts.append(text)
        elif isinstance(node, Tag) and node.name == 'br':
            parts.append('\n')
    return ' '.join(p for p in (p.replace('\n',' ').strip() for p in parts) if p)

def media_placeholders(msg_el):
    placeholders = []
    # images
    for img in msg_el.find_all('img'):
        src = img.get('src') or img.get('data-src') or ''
        if src:
            placeholders.append(f'[IMAGE: {src.split("/")[-1]}]')
    # links to files
    for a in msg_el.find_all('a', href=True):
        href = a['href']
        # heuristic: file link often points to 'media' or has file extension
        if any(href.lower().endswith(ext) for ext in ('.jpg','.jpeg','.png','.gif','.mp4','.mkv','.mp3','.ogg','.webm','.pdf','.zip')):
            placeholders.append(f'[FILE: {href.split("/")[-1]}]')
    return ' '.join(dict.fromkeys(placeholders))  # unique & preserve order

def extract_messages(soup):
    out = []
    # heuristic: messages are often in divs with class containing 'message'
    candidates = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') and any('message' in c for c in tag.get('class')))
    if not candidates:  # fallback - try common telegram export structure
        candidates = soup.find_all('div', class_='message default clearfix') or soup.find_all('div')
    for m in candidates:
        # find sender
        sender = None
        date = None
        text_el = None

        sender_el = m.find(class_='from_name') or m.find(lambda t: t.name in ('span','div') and 'from' in ' '.join(t.get('class') or []))
        if sender_el:
            sender = sender_el.get_text(strip=True)
        date_el = m.find(class_='date') or m.find(lambda t: t.name in ('span','div') and 'date' in ' '.join(t.get('class') or []))
        if date_el:
            date = date_el.get_text(strip=True)
        # message text
        text_el = m.find(class_='text') or m.find('p') or m.find('div', recursive=True)
        if text_el:
            txt = visible_text(text_el)
        else:
            txt = visible_text(m)

        media = media_placeholders(m)
        out.append({
            'sender': sender or 'Unknown',
            'date': date or '',
            'text': txt or '',
            'media': media
        })
    return out

def main():
    if len(sys.argv) < 3:
        print("Usage: telegram_html_to_txt.py input.html output.txt")
        sys.exit(1)
    infile, outfile = sys.argv[1], sys.argv[2]
    with open(infile, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    msgs = extract_messages(soup)

    with open(outfile, 'w', encoding='utf-8') as f:
        for m in msgs:
            header = f"{m['sender']}"
            if m['date']:
                header += f" — {m['date']}"
            f.write(header + '\n')
            if m['text']:
                f.write(m['text'].strip() + '\n')
            if m['media']:
                f.write(m['media'] + '\n')
            f.write('\n')

    print(f"Wrote {len(msgs)} message(s) to {outfile}")

if __name__ == '__main__':
    main()
