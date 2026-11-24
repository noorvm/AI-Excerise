import os
from dotenv import load_dotenv
from google import genai
from google.genai import types, errors

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEmini API key is not found !")

client = genai.Client(api_key = api_key)

chat = client.chats.create(
    model = "gemini-3.6-flash",
    config= types.GenerateContentConfig(
        system_instruction = (
            "You are an experienced Python programming tutor."
            "Explain concepts clearly using simple, beginner-friendly examples."
        )
    ),
) 

print("gemini Python tutor Ready")
print("Type exite to stop.\n")

while True:
    question = input("YOU : ")

    if not question.strip():
        print("Please enter a question")
        continue

    if question.lower().strip() == "exit":
        print("Chat ended . GOOD BYE !")
        break
    else:
        try:
            response = chat.send_message(question)
            print(f"Tutor:\n{response.text}\n")
        except Exception as error:
            print("Something error :",error)
    
client.close()