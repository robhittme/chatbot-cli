import os
import time 
import questionary
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

def chat(p):
    data = {
        "prompt": p, 
        "max_tokens": 2048,
        "model": os.environ["MODEL"],
        "n": 1,
        "stop": None,
        "temperature": 0.7,
        "stream": True
    }

    # Stream in response data
    response_iterator = openai.Completion.create(**data)
    print("=" * 50)
    print("OPENAI CHATGPT RESPONSE:")
    for response in response_iterator:
        # Call the API to generate text
        if response['choices'][0]['text']:
            print(response['choices'][0]['text'], end=" ")
    print("\n" + ("=" * 50))
    return

if __name__ == "__main__":
    try: 
        while True:
            prompt = questionary.text(">> ").ask()
            if prompt == "exit":
                os._exit(0)
            chat(prompt)
    except KeyboardInterrupt:
        print("bye!")
