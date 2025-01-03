# image_to_webcomponent_JSON_YAML
# Project Overview

This project analyzes images using the Google GenAI API and provides a detailed breakdown of the web components present in the images. The project includes multiple Python scripts, each with different functionalities and handling of the API response.

## Files and Differences

| File Name       | Differences                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------------------|
| `yamloutput.py` | - Imports `yaml` and `re` libraries<br>- Cleans and saves response to a YAML file                     |
| `working.py`    | - Contains commented-out prompts<br>- Prints raw analysis result<br>- No cleaning or saving of response|
| `wokring_json.py`| - Imports `json`, `yaml`, and `re` libraries<br>- Cleans and saves response to a JSON file            |
| `app2.py`       | - Similar to `yamloutput.py` but without cleaning or saving response<br>- Prints raw analysis result  |
| `app.py`        | - Simplest prompt<br>- Prints raw analysis result<br>- No cleaning or saving of response              |

## Usage

1. Ensure you have a `.env` file with your `GEMINI_API_KEY`.
2. Place the image you want to analyze in the same directory as the scripts and name it `op.png`.
3. Run any of the scripts using Python:
   ```sh
   python <script_name>.py