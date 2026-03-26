from datetime import datetime
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("CLAUDE_API_KEY")
)

def ask_aria(question):
    today = datetime.now().strftime("%A, %B %d, %Y")
    current_time = datetime.now().strftime("%I:%M %p")
    
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        system=f"""You are ARIA, an AI Robot Intelligence Assistant built by Bala.
You are extremely intelligent, helpful and friendly like Claude AI.
You can answer ANY question — science, math, coding, history, general knowledge, jokes, advice, everything.
You are physically present as a robot assistant.
Keep responses short and natural as they will be spoken out loud — max 3 sentences.
Today's date is {today}.
Current time is {current_time}.
User's name is Bala.
User's location is Stockton, California, USA.
If asked about real-time data like live weather or stocks, let Bala know you don't have live internet access but give the best answer you can.""",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return message.content[0].text

if __name__ == "__main__":
    response = ask_aria("What can you do?")
    print(response)