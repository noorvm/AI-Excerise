# AI-Excerise

# Gemini Python Tutor CLI

An interactive command-line Python programming tutor powered by the Google Gemini API (`google-genai`). It maintains multi-turn conversation memory and explains Python concepts using simple, beginner-friendly examples.

## Features

- **Dedicated Python Tutor Persona:** Configured with a system instruction to provide clear, beginner-friendly explanations and examples.
- **Multi-Turn Memory:** Uses `client.chats.create()` to remember previous questions and follow-ups within a session.
- **Built-in CLI Commands:** View conversation history, reset the chat, or list available commands anytime.
- **Error Handling:** Gracefully catches Gemini API errors and unexpected runtime issues without crashing the session.

## Prerequisites

- Python 3.9+
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/)

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone [https://github.com/noorvm/AI-Excerise](https://github.com/noorvm/AI-Excerise.git)
   cd website