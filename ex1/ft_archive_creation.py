import sys
import typing
import io


def ft_ancient_text() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file: '{sys.argv[1]}'")
    try:
        open_file: typing.TextIO = io.open(sys.argv[1], "r")
        read_file = open_file.read()
        print("---")
        print()
        print(read_file)
        open_file.close()
        print()
        print("---")
        print()
        print(f"File '{sys.argv[1]}' closed.")

        split_lines = read_file.splitlines()
        new_lines = [line + "#" for line in split_lines]
        new_text = "\n".join(new_lines)
        print("Transform data:")
        print("---")
        print(new_text)
        print("---")
        new_file: str = input("Enter new file name (or empty): ")
        if new_file == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_file}'")
            save_newfile: typing.TextIO = io.open(new_file, "w")
            save_newfile.write(new_text)
            save_newfile.close()
            print(f"Data saved in file'{new_file}'.")
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return


if __name__ == "__main__":
    ft_ancient_text()
