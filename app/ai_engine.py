import ollama
from app.prompt import build_prompt

def generate_response(name, location, user_message):

    prompt = build_prompt(name, location, user_message)

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
