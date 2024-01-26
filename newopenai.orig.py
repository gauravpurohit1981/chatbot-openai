import openai
import json
import os

# Set your OpenAI API key using an environment variable
openai.api_key = ''

if openai.api_key is None:
    raise ValueError("OpenAI API key not set. Please set the OPENAI_API_KEY environment variable.")

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def main():
    # Set up the system message
    system_message = {'role': 'system', 'content': 'You are a helpful assistant.'}

    # Specify the path to your data file
    data_file_path = 'data.json'

    # Load questions and answers from the data file
    data = load_data(data_file_path)
    questions = [entry['question'] for entry in data]
    answers = [entry['answer'] for entry in data]

    # Display system message
    print(system_message['content'])

    while True:
        # Get user input
        user_input = input("You: ")

        # Check if the user input is a question
        if user_input.lower() == "exit":
            # Exit the loop if the user enters "exit"
            print("Goodbye!")
            break

        # Check if the user input is in the dataset
        if user_input in questions:
            # Find the corresponding answer
            index = questions.index(user_input)
            assistant_response = answers[index]
            print(f"Assistant: {assistant_response}\n")
        else:
            # Generate a response using OpenAI GPT-3.5-turbo
            conversation = [system_message, {'role': 'user', 'content': user_input}]
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=conversation,
                temperature=0.7,
                max_tokens=150
            )
            print(f"Assistant: {response['choices'][0]['message']['content'].strip()}\n")

if __name__ == "__main__":
    main()