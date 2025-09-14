"""
main.py

This script demonstrates how to use the Gemini API to generate content using the gemini-2.0-flash-001 model.
It loads the API key from environment variables, sends a prompt, and prints the response along with token usage statistics.
"""

import os
from dotenv import load_dotenv
from google import genai


def main():
    """
    Loads the Gemini API key, sends a prompt to the Gemini model, and prints the response and token usage.
    """
    load_dotenv()  # Load environment variables from .env file

    api_key = os.environ.get("GEMINI_API_KEY")  # Retrieve Gemini API key

    client = genai.Client(api_key=api_key)  # Initialize Gemini client

    # Generate content using Gemini model
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
    )

    print(response.text)  # Print model response
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")  # Print prompt token count
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")  # Print response token count


if __name__ == "__main__":
    main()
