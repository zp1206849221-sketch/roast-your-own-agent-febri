import os

LINE = "My agent loops: break my code, say 'You're absolutely right, my mistake,' break it worse — each apology longer than the last, until the sorry has subheadings and the code won't compile."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
