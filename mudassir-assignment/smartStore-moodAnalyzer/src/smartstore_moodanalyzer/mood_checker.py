# mood_handoff.py

import os
from dotenv import load_dotenv
from openai import OpenAI

# ------------------ Load environment ------------------
load_dotenv()
# Make sure your .env file has OPENAI_API_KEY=your_api_key_here

# ------------------ Configure OpenAI API ------------------
client = OpenAI(api_key=os.getenv("GEMINI_API_KEY"))

# ------------------ Agent 1: Mood Analyzer ------------------
def analyze_mood(user_message: str) -> str:
    """Analyze the mood from user message."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a mood analyzer. Respond ONLY with one word: 'happy', 'sad', 'stressed', 'angry', or 'neutral'."
            },
            {
                "role": "user",
                "content": f"Analyze the mood in this message: '{user_message}'"
            }
        ]
    )
    return response.choices[0].message.content.strip().lower()

# ------------------ Agent 2: Activity Suggester ------------------
def suggest_activity(mood: str) -> str:
    """Suggest activity based on mood."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. If the mood is 'sad' or 'stressed', suggest an uplifting activity like listening to music, going for a walk, or calling a friend. If the mood is anything else, respond with 'No activity needed.'"
            },
            {
                "role": "user",
                "content": f"The detected mood is: '{mood}'"
            }
        ]
    )
    return response.choices[0].message.content

# ------------------ Main Runner ------------------
if __name__ == "__main__":
    # Example user input
    user_message = "I feel really down today and nothing excites me."

    # Step 1: Run mood analyzer
    mood = analyze_mood(user_message)
    print(f"Detected Mood: {mood}")

    # Step 2: Run activity suggester (handoff if sad/stressed)
    activity = suggest_activity(mood)
    print(f"Suggested Activity: {activity}")
