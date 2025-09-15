# country_info_toolkit.py

import os
from dotenv import load_dotenv
from openai import OpenAI

# ------------------ Load Environment ------------------
load_dotenv()
# In .env add: OPENAI_API_KEY=your_api_key_here

# ------------------ Configure OpenAI API ------------------
client = OpenAI(api_key=os.getenv("GEMINI_API_KEY"))

# ------------------ Tools ------------------

def capital_tool(country: str) -> str:
    """Return the capital city of a country."""
    capitals = {
        "pakistan": "Islamabad",
        "india": "New Delhi",
        "france": "Paris",
        "germany": "Berlin",
        "usa": "Washington, D.C.",
    }
    return capitals.get(country.lower(), "Capital not found")

def language_tool(country: str) -> str:
    """Return the official language of a country."""
    languages = {
        "pakistan": "Urdu (and English widely used)",
        "india": "Hindi (and English widely used)",
        "france": "French",
        "germany": "German",
        "usa": "English",
    }
    return languages.get(country.lower(), "Language not found")

def population_tool(country: str) -> str:
    """Return the approximate population of a country."""
    populations = {
        "pakistan": "241 million (2025 est.)",
        "india": "1.43 billion (2025 est.)",
        "france": "65 million (2025 est.)",
        "germany": "83 million (2025 est.)",
        "usa": "336 million (2025 est.)",
    }
    return populations.get(country.lower(), "Population data not found")

# ------------------ Orchestrator Agent ------------------
def get_country_info(country: str) -> str:
    """Get complete country information using all three tools."""
    # Call all three tools
    capital = capital_tool(country)
    language = language_tool(country)
    population = population_tool(country)
    
    # Use OpenAI to format the response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an orchestrator agent. Format country information into a nice, readable response. Make it informative and well-formatted."
            },
            {
                "role": "user",
                "content": f"""
                I have gathered this information for {country}:
                - Capital: {capital}
                - Language: {language}
                - Population: {population}
                
                Format this into a nice, readable response like:
                "Country: {country}
                 Capital: {capital}
                 Language: {language}
                 Population: {population}"
                """
            }
        ]
    )
    return response.choices[0].message.content

# ------------------ Runner ------------------
if __name__ == "__main__":
    country_name = "Pakistan"
    result = get_country_info(country_name)

    print("------ Country Info ------")
    print(result)
