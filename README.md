
# EncodeIMAGE

Encode an image to Base64 using Python

---

## Overview

EncodeIMAGE is a simple Python utility to encode images into Base64 strings. This is useful for embedding images directly into text-based formats such as JSON, HTML, or sending images via APIs that accept Base64 encoded data.

---

## Features

- Encode any image file to a Base64 string.
- Simple, minimal Python script.
- Supports common image formats (JPEG, PNG, etc.).
- Easy to integrate into other projects.

---

## Requirements

- Python 3.x

---

## Installation

Clone the repository:

```
git clone https://github.com/Julianhornero/EncodeIMAGE.git
cd EncodeIMAGE
```

No external dependencies are required.

---

## Usage

Run the script `ec.py` with the path to your image file:

```
python ec.py path/to/your/image.jpg
```

Example:

```
python ec.py sample.jpg
```

The script will output the Base64 encoded string of the image to the console.

---

## Example Code Snippet

Here is an example of how the encoding is done in `ec.py`:

```
import base64
import sys

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

if __name__ == "__main__":
    if len(sys.argv) ")
        sys.exit(1)

    image_path = sys.argv[1]
    base64_str = encode_image_to_base64(image_path)
    print(base64_str)
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

