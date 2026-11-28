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
i = 0

try:
    while True:
        question = input("YOU : ")

        if not question.strip():
            print("Please enter a question")
            continue

        elif question.lower().strip() == "exit":
            print("Chat ended . GOOD BYE !")
            break

        elif question.lower().strip() == "clear":
            os.system("cls" if os.name == "nt" else "clear")
            continue
        
        elif question.lower().strip() == "reset":
            print("New chat loaded")
            i = 0
            chat=start_new_chat()
            continue
        elif question.lower().strip() == "help":
            print("Available Commands:\n \n1.history\t - Show conversation\n2.reset\t - Start new conversation\n3.exit\t - Close chatbot\n4.help\t - Show commands\n"
                "5.clear\t - Clear terminal screen\n"
                "6.help\t - Show commands\n"
                "-----------------------------------------------------------------------------\n"
            )
            continue

        elif question.lower().strip() == "history":
            user_message = chat.get_history() 
            if not user_message:
                print("\n----------No Historry----------\n")
            else:
                print("\n--------Your Previous Questions----------")
                for i, message in enumerate(user_message, start=1):
                    role = "You" if message.role == "user" else "Gemini"
                    text ="".join(part.text for part in message.parts if part.text)
                    print(f"{i}.{role}:{text} \n")
                    print("--------------------\n")
            continue
        else:
            try:
                response = chat.send_message(question)
                i=i+1
                print(f"Tutor:\n{response.text}\n")
                print(f"count of Chat exchange: {i}")

            except errors.APIError as error:
                print("Gemini API error: ",error)

            except Exception as error:
                print("Something error :",error)
finally:
    client.close()