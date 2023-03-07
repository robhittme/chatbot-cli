# Chatbot using OpenAI API
This is a simple chatbot application that uses the OpenAI API to generate responses based on user input. The bot generates text by calling the OpenAI Completion API, using a pre-trained language model.

## Installation
To run this application, you will need to install the following dependencies:

* questionary
* openai
* dotenv

You can install these dependencies by running `pip install -r requirements.txt` in your terminal.

You will also need an OpenAI API key, which you can obtain from the OpenAI website.

## Configuration
Before running the application, you need to create a `.env` file in the root directory of the project and set the `MODEL` and `OPENAI_API_KEY` variable to the name of the OpenAI language model you want to use. For example:

```
OPENAI_API_KEY=your_api_key
MODEL=text-davinci-002
```

You should replace text-davinci-002 with the name of the language model you want to use.

## Usage
To run the chatbot, simply run the chatbot.py file in your terminal by running python chatbot.py.

Once the chatbot is running, you can start chatting with it by typing your message after the prompt >>. To exit the chatbot, type `exit`.



