import os
from dotenv import load_dotenv
from google import genai
from google.genai import types, errors

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEmini API key is not found !")

client = genai.Client(api_key = api_key)

def start_new_chat():
    return client.chats.create(
        model = "gemini-3.6-flash",
        config= types.GenerateContentConfig(
            system_instruction = (
                "You are an experienced Python programming tutor."
                "Explain concepts clearly using simple, beginner-friendly examples."
            )
        ),
    ) 

chat = start_new_chat()
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
    
    if question.lower().strip() == "reset":
        print("New chat loaded")
        chat=start_new_chat()
        continue

    if question.lower().strip() == "history":
        user_message = [m for m in chat.get_history() if m.role == "user"]
        if not user_message:
            print("\n----------No Historry----------\n")
        else:
            print("\n--------Your Previous Questions----------")
            for i, message in enumerate(user_message, start=1):
                text ="".join(part.text for part in message.parts if part.text)
                print(f"{i}:{text}")
                print("--------------------\n")
                continue 
    else:
        try:
            response = chat.send_message(question)
            print(f"Tutor:\n{response.text}\n")

        except errors.APIError as error:
            print("Gemini API error: ",error)

        except Exception as error:
            print("Something error :",error)

client.close()