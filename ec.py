import base64
import requests
from google import genai
from google.genai import types

# Initialize Gemini client with your API key
client = genai.Client(api_key="YOUR_GOOGLE_API_KEY")

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as f:
        image_bytes = f.read()
    return base64.b64encode(image_bytes).decode('utf-8')

def decode_base64_to_image(base64_str, output_path):
    image_bytes = base64.b64decode(base64_str)
    with open(output_path, "wb") as f:
        f.write(image_bytes)

def generate_content_with_image(image_path, prompt_text):
    # Read image bytes
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    # Create image part for Gemini API
    image_part = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

    # Prepare prompt contents: image + text prompt
    contents = [
        image_part,
        prompt_text
    ]

    # Call Gemini generate_content API
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=contents
    )

    return response.text

if __name__ == "__main__":
    input_image_path = "input.jpg"  # Path to your input image
    output_image_path = "output.jpg"  # Path to save any decoded image if needed
    prompt = "Describe this image."

    # Generate text content describing the image
    result_text = generate_content_with_image(input_image_path, prompt)
    print("Response from Gemini API:")
    print(result_text)

    # If the response contains base64 image data you want to decode, do it like this:
    # (Example: suppose you get base64 image string in `base64_image_str`)
    # decode_base64_to_image(base64_image_str, output_image_path)
