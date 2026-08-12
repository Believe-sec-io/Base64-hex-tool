## Features / Hex Encoder Decoder

A simple Python command-line tool for detecting, encoding, and decoding Base64 and Hexadecimal text.

The tool can also analyze ".txt" files and automatically detect whether their content appears to be Base64, Hex, or plain text.Featureses

- Encode text to Base64
- Decode Base64
- Encode text to hexadecimal
- Decode hexadecimal
- Automatically detect Base64 or Hex
- Identify plain text
- Analyze ".txt" files
- Save decoded results to a file
- UTF-8 support
- Works on Windows and Linux
- No external Python dependencies

Project Structure

base64-hex-tool/
│
├── main.py
├── detector.py
├── encoder_decoder.py
├── requirements.txt
└── README.md

Requirements

- Python 3.8 or newer
- No external packages required

Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/base64-hex-tool.git
cd base64-hex-tool

Run the program:

python main.py

On some Linux systems:

python3 main.py

Usage

The main menu provides four operations:

[1] Encode text
[2] Decode text
[3] Auto detect
[4] Analyze TXT file
[5] Exit

Encode Base64

Example:

Input:
Hello World

Output:
SGVsbG8gV29ybGQ=

Decode Base64

Input:
SGVsbG8gV29ybGQ=

Output:
Hello World

Encode Hex

Input:
Hello World

Output:
48656c6c6f20576f726c64

Decode Hex

Input:
48656c6c6f20576f726c64

Output:
Hello World

Automatic Detection

The detector analyzes the input and attempts to classify it as:

BASE64
HEX
PLAIN_TEXT
UNKNOWN

For example:

SGVsbG8gV29ybGQ=

is detected as:

BASE64

While:

48656c6c6f20576f726c64

is detected as:

HEX

TXT File Analysis

The tool can read a ".txt" file:

[4] Analyze TXT file

Enter the path:

Enter TXT file path: encoded.txt

The program analyzes the content and attempts to decode it when Base64 or Hex is detected.

The decoded result can then be saved to another file.

Security Note

Base64 and hexadecimal encoding are not encryption.

They do not provide confidentiality or password protection.

For example:

SecretPassword

can become:

U2VjcmV0UGFzc3dvcmQ=

but anyone can decode it.

This project is intended for:

- Cybersecurity learning
- CTF practice
- Log analysis
- Data inspection
- Encoding/decoding experiments
- Security research

Do not treat Base64 or Hex as a secure method for storing passwords, secrets, or sensitive information.

Future Improvements

Possible future features:

- [ ] Colored terminal interface
- [ ] Batch processing
- [ ] Recursive directory scanning
- [ ] Better Base64 detection
- [ ] Binary file support
- [ ] JSON output
- [ ] Command-line arguments
- [ ] Detection confidence score
- [ ] Automatic output file generation
- [ ] Unit tests

License

This project is released under the MIT License.
