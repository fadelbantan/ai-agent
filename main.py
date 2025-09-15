"""
main.py

This script demonstrates how to use the Gemini API to generate content using the gemini-2.0-flash-001 model.
It loads the API key from environment variables, sends a prompt, and prints the response along with token usage statistics.
"""

import os, sys, argparse
from google import genai
from google.genai import types
from dotenv import load_dotenv

def main():
    """
    Loads the Gemini API key, sends a prompt to the Gemini model, and prints the response and token usage.
    """
    load_dotenv()  # Load environment variables from .env file

    api_key = os.environ.get("GEMINI_API_KEY")  # Retrieve Gemini API key
    client = genai.Client(api_key=api_key)  # Initialize Gemini client

    parser = argparse.ArgumentParser(
        description="Optional verbose output: user prompt and token counts."
    )
    parser.add_argument("prompt", help="Prompt to senx to Gemini model.")
    parser.add_argument("-v", "--verbose", action='store_true', help='Enable verbose output.')

    args = parser.parse_args()
    user_prompt = args.prompt

    if not args.prompt:
        print("Please input a prompt like this:")
        print("uv run main.py 'Insert Prompt Here!'")
        print("Example: uv run main.py 'What is the meaning of life?'")
        exit(1)


    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, user_prompt, args.verbose)

def generate_content(client, messages, user_prompt, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    if verbose:
        print("User prompt:", user_prompt)  # Print model response
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)  # Print prompt token count
        print("Response tokens:", response.usage_metadata.candidates_token_count)  # Print response token count
    print(response.text)

if __name__ == "__main__":
    main()
