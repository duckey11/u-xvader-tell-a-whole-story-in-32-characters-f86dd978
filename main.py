"""Tell a Whole Story in 32 Characters.

Writes one Wi-Fi network name (max 32 characters) to /output/entry.txt.

The name: "My ex changed it. Again. Sorry."

The story it implies in 31 characters: the breakup is over, but the ex
still has the router password and keeps changing it. The host is now
apologising to every guest who asks for the Wi-Fi. One character (the ex),
one situation (locked out of your own network), one event that keeps
happening ("Again." as its own deadpan beat), and a punchline ("Sorry.").
"""

import os

ENTRY = "My ex changed it. Again. Sorry."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 32, f"entry must be 1-32 characters, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
