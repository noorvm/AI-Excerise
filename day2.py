import os 
from dotenv import load_dotenv
from google import genai
import time
from google.genai import errors

load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API Key is not found !")

client = genai.Client(api_key = api_key)

question = input("aski Gemini something: ")

max_retries = 3

for attempt in range(max_retries):
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=question
        )

        print("\nGemini Response:")
        print(response.text)
        break
    except errors.ServerError as error:
        if error.code == 503 and attempt < max_retries-1:
            wait_time = 2**(attempt+1)

            print(f"gemini is busy . retry in {wait_time} second...")

            time.sleep(wait_time)
        else:
            print("gemini server error :",error)
    except Exception as error:
        print("Unexcepeted error: ",error)
        break

client.close()