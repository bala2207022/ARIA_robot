from datetime import datetime
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv('CLAUDE_API_KEY'))


def ask_aria(question: str, recognized_name: str | None = None) -> str:
    today        = datetime.now().strftime('%A, %B %d, %Y')
    current_time = datetime.now().strftime('%I:%M %p')

    if recognized_name:
        user_info = f'Person talking is {recognized_name}. Use their name naturally.'
    else:
        user_info = 'Do not know who is talking. Do not use any name.'

    message = client.messages.create(
        model='claude-sonnet-4-20250514',
        max_tokens=150,
        system=(
            f'You are ARIA, an AI Robot Intelligence Assistant.\n'
            f'Keep responses very short, max 2 sentences, spoken out loud.\n'
            f'Today is {today}. Time is {current_time}. Location: Stockton, CA.\n'
            f'{user_info}'
        ),
        messages=[{'role': 'user', 'content': question}],
    )
    return message.content[0].text


if __name__ == '__main__':
    print(ask_aria('What can you do?'))