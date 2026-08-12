from pathlib import Path

from detector import detect_encoding
from encoder_decoder import (
    encode_base64,
    decode_base64,
    encode_hex,
    decode_hex,
)


def print_banner():
    print("=" * 55)
    print("       BASE64 / HEX ENCODER & DECODER")
    print("=" * 55)


def encode_menu():
    print("\n[1] Base64")
    print("[2] Hex")

    choice = input("Choose encoding: ").strip()
    text = input("Enter text: ")

    try:
        if choice == "1":
            result = encode_base64(text)
            print(f"\nEncoded Base64:\n{result}")

        elif choice == "2":
            result = encode_hex(text)
            print(f"\nEncoded Hex:\n{result}")

        else:
            print("Invalid choice.")

    except Exception as error:
        print(f"Error: {error}")


def decode_menu():
    print("\n[1] Base64")
    print("[2] Hex")

    choice = input("Choose decoding type: ").strip()
    text = input("Enter encoded text: ").strip()

    try:
        if choice == "1":
            result = decode_base64(text)
            print(f"\nDecoded text:\n{result}")

        elif choice == "2":
            result = decode_hex(text)
            print(f"\nDecoded text:\n{result}")

        else:
            print("Invalid choice.")

    except ValueError as error:
        print(f"Error: {error}")


def detect_menu():
    text = input("\nEnter text to analyze: ")

    encoding = detect_encoding(text)

    print(f"\nDetected type: {encoding}")

    if encoding == "BASE64":
        try:
            print(f"Decoded: {decode_base64(text.strip())}")
        except ValueError:
            pass

    elif encoding == "HEX":
        try:
            print(f"Decoded: {decode_hex(text.strip())}")
        except ValueError:
            pass


def file_menu():
    file_path = input("\nEnter TXT file path: ").strip()

    path = Path(file_path)

    if not path.exists():
        print("File not found.")
        return

    if not path.is_file():
        print("The specified path is not a file.")
        return

    try:
        text = path.read_text(encoding="utf-8")

        encoding = detect_encoding(text)

        print(f"\nFile: {path.name}")
        print(f"Detected type: {encoding}")

        if encoding == "BASE64":
            result = decode_base64(text.strip())

        elif encoding == "HEX":
            result = decode_hex(text.strip())

        else:
            result = text

        print("\nResult:")
        print("-" * 55)
        print(result)
        print("-" * 55)

        save = input("\nSave result to file? (y/n): ").strip().lower()

        if save == "y":
            output_path = input("Output file path: ").strip()
            Path(output_path).write_text(result, encoding="utf-8")
            print(f"Saved to: {output_path}")

    except UnicodeDecodeError:
        print("Unable to read the file as UTF-8 text.")

    except ValueError as error:
        print(f"Decoding error: {error}")

    except OSError as error:
        print(f"File error: {error}")


def main():
    while True:
        print_banner()

        print("\n[1] Encode text")
        print("[2] Decode text")
        print("[3] Auto detect")
        print("[4] Analyze TXT file")
        print("[5] Exit")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            encode_menu()

        elif choice == "2":
            decode_menu()

        elif choice == "3":
            detect_menu()

        elif choice == "4":
            file_menu()

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
