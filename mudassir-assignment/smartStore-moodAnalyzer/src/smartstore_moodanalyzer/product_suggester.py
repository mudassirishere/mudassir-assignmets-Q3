import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

# ------------------ Load Environment Variables ------------------
load_dotenv()  
# Make sure you have a .env file with:
# OPENAI_API_KEY="your_api_key_here"

# ------------------ Configure OpenAI API ------------------
client = OpenAI(api_key=os.getenv("GEMINI_API_KEY"))

# ------------------ Product Recommendation Function ------------------
def suggest_product(symptom: str) -> str:
    """Suggests a product based on the user's symptom."""
    suggestions = {
        "headache": "Paracetamol – helps relieve pain and reduce fever.",
        "cold": "Antihistamine – helps with runny nose and sneezing.",
        "cough": "Cough syrup – soothes throat and reduces coughing.",
        "fever": "Ibuprofen – reduces fever and inflammation.",
    }
    return suggestions.get(symptom.lower(), "I'm not sure. Please consult a doctor.")

# ------------------ User Context ------------------
class UserContext(BaseModel):
    name: str

# ------------------ Agent Setup ------------------
def run_product_agent(user_message: str) -> str:
    """Run the product recommendation agent."""
    # Get product suggestion
    symptom = user_message.lower()
    if any(word in symptom for word in ["headache", "cold", "cough", "fever"]):
        product = suggest_product(symptom)
        
        # Use OpenAI to generate explanation
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system", 
                    "content": "You are a helpful product recommendation assistant. Explain why the suggested product is useful in simple language."
                },
                {
                    "role": "user", 
                    "content": f"User said: '{user_message}'. I suggested: '{product}'. Explain why this product helps."
                }
            ]
        )
        return response.choices[0].message.content
    else:
        return "I can help with headache, cold, cough, or fever symptoms. Please describe your specific symptom."

# ------------------ Runner ------------------
if __name__ == "__main__":
    result = run_product_agent("I have a headache")
    print(result)
