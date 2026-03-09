def summarize_text(file_path):
    """Read a file and return (lines, words, characters)."""
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    lines = text.splitlines()
    words = text.split()
    return len(lines), len(words), len(text)


def find_and_replace(text, target, replacement):
    """Replace all occurrences of target with replacement and return (result, count)."""
    count = text.count(target)
    return text.replace(target, replacement), count


def main():
    input_path = "input.txt"
    output_path = "output.txt"

    lines, words, chars = summarize_text(input_path)
    print(f"Lines: {lines}")
    print(f"Words: {words}")
    print(f"Characters: {chars}")

    target = input("Enter text to find: ")
    replacement = input("Enter replacement text: ")

    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    updated, replaced_count = find_and_replace(content, target, replacement)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"Replaced {replaced_count} occurrences. See {output_path}.")


if __name__ == "__main__":
    main()
