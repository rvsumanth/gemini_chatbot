import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


# Load variables from .env into the system environment
load_dotenv()

# Access variables safely (returns None if not found)
apikey = os.getenv("API_KEY")

client =  genai.Client(api_key= apikey)

# chat session also gives your bot memory of earlier messages
chat = client.chats.create(
    model="gemini-3.6-flash",  # double-check this model name in AI Studio
    config=types.GenerateContentConfig(
        system_instruction="Answer concisely.",
        max_output_tokens=500,
        # Less thinking = faster first word.
        # Use thinking_budget=0 on 2.5-era models;
        # newer models may use thinking_level="low" instead.
        thinking_config=types.ThinkingConfig(thinking_budget=0),
    ),
)

while True:
    question = input("You: ")
    if question.lower() == "exit":
        break

    print("Gemini: ", end="", flush=True)
    for chunk in chat.send_message_stream(question):
        print(chunk.text or "", end="", flush=True)
    print()




