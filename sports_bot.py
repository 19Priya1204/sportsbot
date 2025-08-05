# -*- coding: utf-8 -*-
from openai import OpenAI

# Connect to Groq API
client = OpenAI(
    api_key="",  # Replace with your actual Groq API key
    base_url="https://api.groq.com/openai/v1"
)

print("Sports Bot is ready! Ask me about sports or type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bot: See you later, champ!")
        break

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a friendly sports expert. Help users understand cricket, football, basketball, "
                    "Olympics, and general sports trivia. Explain clearly and avoid unrelated topics."
                )
            },
            {"role": "user", "content": user_input}
        ]
    )

    print("Bot:", response.choices[0].message.content)