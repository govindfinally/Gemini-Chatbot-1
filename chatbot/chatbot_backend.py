from dotenv import load_dotenv

from google import genai
import os


load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file.")
client = genai.Client(api_key=api_key)


def generate_summary_and_keywords(prompt_text: str):
    """
    Given an input prompt, this function generates a summary and extracts keywords
    using the Gemini models via the Vertex AI SDK client.

    Args:
        prompt_text: The text you want to process.

    Returns:
        A tuple containing (summary_text, keywords_text).
    """
    try:
    
        print("Generating summary...")
        summary_prompt = f"Summarize this text: {prompt_text}"
        summary_response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=summary_prompt
        )
        summary_text = summary_response.text
        print("...summary generated.")

        # Step 2: Extract keywords from the summary
        print("Extracting keywords...")
        keywords_prompt = f"Extract the most important keywords from the following text:\n\n{summary_text}"
        keywords_response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=keywords_prompt
        )
        keywords_text = keywords_response.text
        print("...keywords extracted.")

        # Step 3: Save results to a file (appends to the file)
        with open("D:\gemni chatbot 1\maintainance_result.txt", "a", encoding="utf-8") as f:
            f.write(f"--- Entry ---\n")
            f.write("Summary:\n")
            f.write(summary_text + "\n\n")
            f.write("Keywords:\n")
            f.write(keywords_text + "\n\n")
        
        print("Results saved to maintenance_results.txt")
        return summary_text, keywords_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

# Example of how to run this function
if __name__ == '__main__':
    # You can get this text from a file, a database, or user input
    example_prompt = """
    The sun is a star at the center of the Solar System. It is a nearly perfect ball of hot plasma,
    heated to incandescence by nuclear fusion reactions in its core. The Sun radiates this energy mainly
    as light, ultraviolet, and infrared radiation, and is the most important source of energy for life on Earth.
    Its diameter is about 1.39 million kilometers, or 109 times that of Earth.
    """
    generate_summary_and_keywords(example_prompt)

