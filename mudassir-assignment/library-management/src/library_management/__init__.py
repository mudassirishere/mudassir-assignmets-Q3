import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv(find_dotenv())

def main() -> None:
    # Initialize OpenAI client
    client = OpenAI(api_key=os.getenv("GEMINI_API_KEY"))
    
    # ------------------ Book Database ------------------
    BOOK_DB = {
        "pride and prejudice": {"title": "Pride and Prejudice", "copies": 3},
        "clean code": {"title": "Clean Code", "copies": 2},
        "deep learning": {"title": "Deep Learning", "copies": 1},
        "introduction to algorithms": {"title": "Introduction to Algorithms", "copies": 0},
    }


    # ------------------ Guardrail ------------------
    def library_guardrail(user_input):
        keywords = ["book", "library", "availability", "borrow", "return", "timing", "hours", "opening", "closing"]
        if not any(k in user_input.lower() for k in keywords):
            raise ValueError("Sorry, I only answer library-related questions.")
        return user_input

    # ------------------ Tools ------------------
    def search_book_tool(query):
        q = query.lower().strip()
        matches = []
        for key, info in BOOK_DB.items():
            if q in key:
                matches.append({"title": info["title"], "copies": info["copies"]})
        return {"matches": matches}

    def check_availability_tool(query, user):
        if not user.get("member_id"):
            return {"error": "Only registered members can check availability."}
        q = query.lower().strip()
        if q in BOOK_DB:
            return {"title": BOOK_DB[q]["title"], "copies": BOOK_DB[q]["copies"]}
        return {"error": "Book not found."}

    def library_timings_tool():
        return {"timings": "Mon-Fri 9AM-7PM, Sat 10AM-4PM, Sun Closed"}

    # ------------------ Library Assistant Function ------------------
    def run_library_assistant(messages, user_context):
        # Check guardrail first
        user_message = messages[-1]["content"]
        try:
            library_guardrail(user_message)
        except ValueError as e:
            return str(e)
        
        # Prepare system message with user context
        user_name = user_context.get("name", "User")
        system_message = f"You are a polite library assistant for {user_name}. Only answer library-related questions."
        
        # Add system message to the beginning
        full_messages = [{"role": "system", "content": system_message}] + messages
        
        try:
            response = client.chat.completions.create(
                model="gemini-3.5-flash",
                messages=full_messages,
                temperature=0
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

    # ------------------ Example Usage ------------------
    alice = {"name": "Alice", "member_id": "M-1"}
    bob = {"name": "Bob"}  # not registered

    res1 = run_library_assistant(
        [{"role": "user", "content": "Find Clean Code and tell me if copies are available"}],
        alice
    )
    print("Alice:", res1)

    res2 = run_library_assistant(
        [{"role": "user", "content": "How many copies of Introduction to Algorithms?"}],
        bob
    )
    print("Bob:", res2)

    res3 = run_library_assistant(
        [{"role": "user", "content": "What is the weather today?"}],
        alice
    )
    print("Weather query:", res3)


if __name__ == "__main__":
    main()
