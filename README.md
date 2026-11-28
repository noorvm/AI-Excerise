# 🤖 Gemini Python Tutor CLI  
# day2.py File

A simple and interactive **command-line Python Programming Tutor** built using **Python** and the **Google GenAI SDK (`google-genai`)**.

This application allows users to ask Python programming questions in the terminal, receive clear beginner-friendly explanations with simple examples, maintain multi-turn conversation memory, view chat history, and reset sessions anytime.

The application uses Gemini's **Chat API** (`client.chats.create()`) along with a custom **System Instruction** so the AI stays focused as an experienced Python tutor throughout the conversation.

---

## 📌 Project Overview

The Gemini Python Tutor CLI is a terminal-based AI learning assistant powered by the `gemini-3.6-flash` model.

Users can:

* Ask Python programming questions directly in the terminal
* Receive beginner-friendly explanations with simple examples
* Ask follow-up questions with automatic conversation memory
* View the full conversation history (`history`)
* Clear memory and start a new conversation (`reset`)
* View all available CLI commands (`help`)
* Exit the chatbot cleanly (`exit`)
* Load API keys securely from a `.env` file

The application runs directly in the command line and does not require a frontend or database.

---


###  🎨 Terminal Interface

```text
gemini Python tutor Ready
Type exite to stop.

YOU : What is a Python list?
Tutor:
A list in Python is an ordered collection of items...

YOU : Show me how to loop through it
Tutor:
You can use a for loop to go through each item...

YOU : history
--------Your Previous Questions----------
1.You:What is a Python list?
2.Gemini:A list in Python is an ordered collection...

YOU : reset
New chat loaded

YOU : exit
Chat ended . GOOD BYE !
```

---

## ▶️ How to Run the Project

### 1. Prerequisites

* Python 3.9 or higher
* A Gemini API key from [Google AI Studio](https://aistudio.google.com/)

### 2. Install Dependencies

```bash
pip install google-genai python-dotenv
```

### 3. Configure Environment Variables

Create a `.env` file in the project folder and add your API key:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

### 4. Run the Script

```bash
python day2.py
```

---

## 📥 Clone the Repository

```bash
git clone [https://github.com/noorvm/AI-Excerise.git](https://github.com/noorvm/AI-Excerise.git)
```

Then enter the project directory:

```bash
cd AI-Excerise
```

Install the dependencies, add your `.env` file, and run `python day2.py`.

---

## 🔐 Environment Variables & Security

* Your `GEMINI_API_KEY` is loaded from `.env` using `python-dotenv` and is never hardcoded in `day2.py`.
* Always ensure `.env` is listed in `.gitignore` before pushing commits to GitHub.

---

## 🧪 Concepts Practiced

This project demonstrates practical usage of several Python and Generative AI concepts:

* Google GenAI SDK (`google-genai`)
* Stateful multi-turn chat (`client.chats.create()`)
* System instructions (`types.GenerateContentConfig`)
* Reading conversation history (`chat.get_history()`)
* Environment variable management (`python-dotenv`, `os.getenv`)
* Interactive CLI loops (`while True`, `continue`, `break`)
* String normalization (`.strip()`, `.lower()`)
* List comprehensions and `enumerate()`
* Exception handling (`try` / `except errors.APIError`)
* Resource cleanup (`client.close()`)

---

## 🔮 Possible Future Improvements

The project can be extended with:

* Exponential backoff retry logic for `503 UNAVAILABLE` server errors
* Automatic fallback to alternative Gemini models
* Streaming responses token-by-token in the terminal
* Saving conversation history to a `.txt` or `.json` file
* Markdown syntax highlighting in the terminal using `rich`
* Switching tutor personas (e.g., Python, SQL, FastAPI, DSA)

---

## 👨‍💻 Author

**Noor Mohammed**

GitHub: [@noorvm](https://github.com/noorvm)

---

## 📄 License

This project is created for learning and demonstration purposes.