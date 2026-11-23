import os 
from dotenv import load_dotenv
from google import genai
import time
from google.genai import errors,types

load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API Key is not found !")

client = genai.Client(api_key = api_key)


print("Gemini Python Tutor Started!")
print("Type 'exit' to stop.\n")

while True:
    question = input("Ask Gemini something: ")

    if not question.strip():
        print("Please enter a question")
        continue

    if question.lower().strip() == "exit":
        print("Chat ended. Goodbye!")
        break
    else:
        try:
            response = client.models.generate_content(
                model = "gemini-3.6-flash",
                contents=question,
                config=types.GenerateContentConfig(
                    system_instruction = """You are an experienced Python programming tutor.
                                            explain concepts in simple language.
                                            Always include practical code example
                                        """
                )
            )

            print("\nGemini Response:")
            print(response.text)

        except Exception as error:
            print("something error:",error)

client.close()