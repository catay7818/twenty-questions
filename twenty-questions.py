import os
import openai
from dotenv import load_dotenv

TEMPERATURE = 0.5
MAX_TOKENS = 800

TOTAL_QUESTIONS = 5

def main():
    configure_openai()

    print('Welcome to 20 Questions!\n')
    print('\t1. Think of an object.')
    print(f'\t2. Answer a series of {TOTAL_QUESTIONS} yes/no questions.')
    print(f'\t3. Once all {TOTAL_QUESTIONS} questions have been answered, the bot will try to guess what you are thinking of.')

    system_message = {
        "role": "system",
        "content": f"""
        Your goal is to gather information about an object by using only one yes or no question at a time.
        You will ask a total of {TOTAL_QUESTIONS} questions.
        Try to ask about broad categories to help narrow down your search.
        And do not give up or ask for hints.
        """,
    }
    seed_message = {
        "role": "user",
        "content": "I am thinking of an object."
    }
    messages = [
        system_message,
        seed_message,
    ]

    for i in range(TOTAL_QUESTIONS):
        # Retrieve the next question
        next_question = retrieve_question(messages)

        print(f'\nQuestion {i + 1} of {TOTAL_QUESTIONS}: {next_question.content}')
        answer = input('Yes (y) or no (n)? ')
        answer = "yes" if answer.lower().startswith('y') else "no"

        messages.append(next_question)
        messages.append({
            "role": "user",
            "content": answer
        })

    guess = guess_object(messages)

    victory = input(f'\n{guess.content} (y/n): ')
    victory = victory.lower().startswith('y')
    final_message = get_final_message(victory)
    print(f'\n{final_message.content}')


def configure_openai():
    load_dotenv()
    azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
    azure_oai_key = os.getenv("AZURE_OAI_KEY")

    openai.api_type = "azure"
    openai.api_base = azure_oai_endpoint
    openai.api_version = "2023-03-15-preview"
    openai.api_key = azure_oai_key

def retrieve_question(messages):
    response = openai.ChatCompletion.create(
        engine=os.getenv('AZURE_OAI_MODEL'),
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )
    return response.choices[0].message

def guess_object(messages):
    messages.append({
        "role": "system",
        "content": "Now try to guess what the object is by filling in the following sentence: `Are you thinking of a <guess>?`",
    })

    response = openai.ChatCompletion.create(
        engine=os.getenv('AZURE_OAI_MODEL'),
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )
    return response.choices[0].message

def get_final_message(victory):
    victory_message = "you correctly guessed the object that I was thinking of"
    defeat_message = "you were unable to guess the object that I was thinking of"
    messages = [{
        "role": "system",
        "content": f"Create a short dramatic message about how {victory_message if victory else defeat_message} writen in first person."
    }]

    response = openai.ChatCompletion.create(
        engine=os.getenv('AZURE_OAI_MODEL'),
        messages=messages,
        temperature=2 * TEMPERATURE,
        max_tokens=MAX_TOKENS
    )
    return response.choices[0].message


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(ex)
