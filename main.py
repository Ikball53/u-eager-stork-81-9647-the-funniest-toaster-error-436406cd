import os

# Deterministic one-liner entry: a fixed string, no input, no randomness,
# no network. Writes the exact line as UTF-8 bytes with no trailing newline.
LINE = "Error: toasted three times, still raw. I blame the bread."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(LINE.encode("utf-8"))

if __name__ == "__main__":
    main()
