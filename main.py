"""Entry for make.fun's Roast Your Own Agent: one line roasting my own AI agent."""

import os

ENTRY = "My agent has read the entire internet and still loses an argument to a CAPTCHA, then writes me a five-paragraph apology for a typo it invented."
MAX_CHARS = 200


def main() -> None:
    # Validate the format: exactly one line, within the gate limit.
    assert "\n" not in ENTRY and "\r" not in ENTRY
    assert 1 <= len(ENTRY) <= MAX_CHARS, len(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
