from google import genai
import os
from dotenv import load_dotenv
import base64

def analyze_image_with_genai(image_path: str, api_key: str) -> str:
    """Analyze the image using the Google GenAI API."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    client = genai.Client(api_key=api_key)

    with open(image_path, 'rb') as image_file:
        image_content = base64.b64encode(image_file.read()).decode('utf-8')
        prompt = (
            "Analyze the following image and provide a detailed breakdown of the web components present in it. "
            "For each component, specify the type (e.g., input field, button, dropdown, checkbox), its props (e.g., placeholder, type, id, class), "
            "and its potential functionality. Also, identify the layout structure, such as whether it's a single-column or two-column design, "
            "and highlight any responsiveness features or visual hierarchies that developers should consider."
        )
        response = client.models.generate_content(
            model='gemini-2.0-flash-exp', 
            contents=[prompt, image_content]
        )

    return response.text

def main():
    load_dotenv()  # Load environment variables from .env file
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("API key is required. Set GEMINI_API_KEY in .env file or pass it to the constructor.")

    image_path = "op.png"
    try:
        result = analyze_image_with_genai(image_path, api_key)
        print(result)
    except Exception as e:
        print(f"Analysis failed: {str(e)}")

if __name__ == "__main__":
    main()