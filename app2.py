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
            "Return the response in the following format:\n\n"
            "'$schema': 'https://git.drupalcode.org/project/drupal/-/raw/HEAD/core/assets/schemas/v1/metadata.schema.json'\n\n"
            "name: Space Social Button\n\n"
            "status: stable\n\n"
            "group: Atoms\n\n"
            "props:\n"
            "  type: object\n"
            "  properties:\n"
            "    text:\n"
            "      type: string\n"
            "      title: Social button text\n"
            "      description: Text\n"
            "      examples:\n"
            "        - 'Sign in with Google.'\n\n"
            "    text_colors: \n"
            "      type: string\n"
            "      title: Text Color\n"
            "      description: Text Color\n"
            "      enum:\n"
            "        - white\n"
            "        - black\n"
            "        - heading\n"
            "        - body\n"
            "        - primaryLight\n"
            "        - primaryMedium\n"
            "        - primaryDark\n"
            "        - danger\n"
            "        - warning\n"
            "        - success\n"
            "        - neutralLight\n"
            "        - neutralMedium\n"
            "      default:\n"
            "        - black\n"
            "      examples:\n"
            "        - 'black'\n\n"
            "    social_button_link:\n"
            "      type: string\n"
            "      title: Social button link\n"
            "      description: Social button link\n"
            "      examples:\n"
            "        - 'https://google.com'\n\n"
            "    background_color:\n"
            "      type: string\n"
            "      title: Background color\n"
            "      description: Background color.\n"
            "      enum:\n"
            "        - transparent\n"
            "        - success\n"
            "        - danger\n"
            "        - white\n"
            "        - black\n"
            "        - neutralLight\n"
            "        - neutralMedium\n"
            "        - neutralDark\n"
            "        - neutralExtraDark\n"
            "        - primaryExtraLight\n"
            "        - primaryLight\n"
            "        - primaryMedium\n"
            "        - primaryDark\n"
            "        - primaryExtraDark\n"
            "        - facebookBlue\n"
            "      default: \n"
            "        - transparent\n"
            "      examples:\n"
            "        - 'transparent'\n\n"
            "slots:\n"
            "  content:\n"
            "    type: string\n"
            "    title: Icon\n"
            "    description: Content slot.\n"
            "    examples: \n"
            "      - 'Icon'"
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