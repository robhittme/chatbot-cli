import os
import questionary
import openai
from dotenv import load_dotenv

def chat(p):
    prompt = p 
    model = os.getenv(MODEL) 
    temperature = 0.5
    max_tokens = 4007

# Call the API to generate text
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
      )

    return response.choices[0].text

if __name__ == "__main__":
    try: 
        while True:
            prompt = questionary.text(">> ").ask()
            if prompt == "exit":
                os._exit(0)
            print(chat(prompt))
    except KeyboardInterrupt:
         print("bye!")
