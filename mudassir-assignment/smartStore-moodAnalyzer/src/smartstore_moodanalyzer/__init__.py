"""
Smart Store Mood Analyzer - Agentic AI Demonstrations

This package contains three assignments demonstrating:
1. Smart Store Agent - Product suggestions based on user needs
2. Mood Analyzer with Handoff - Two-agent mood analysis system
3. Country Info Bot with Tools - Multi-tool country information system
"""

def main() -> None:
    """Main entry point for the smartstore-moodanalyzer application."""
    print("🏪 Smart Store Mood Analyzer - Agentic AI Demonstrations")
    print("=" * 60)
    print()
    print("This project contains three assignments:")
    print()
    print("1️⃣  Smart Store Agent (product_suggester.py)")
    print("   - Suggests products based on user needs and symptoms")
    print("   - Example: 'I have a headache' → suggests pain relievers")
    print()
    print("2️⃣  Mood Analyzer with Handoff (mood_checker.py)")
    print("   - Two-agent system: mood analysis + activity suggestions")
    print("   - Automatically hands off to activity agent for negative moods")
    print()
    print("3️⃣  Country Info Bot with Tools (country_info.py)")
    print("   - Three tool agents: capital, language, population")
    print("   - Orchestrator coordinates all tools for complete country info")
    print()
    print("🚀 To run any assignment:")
    print("   python src/smartstore_moodanalyzer/product_suggester.py")
    print("   python src/smartstore_moodanalyzer/mood_checker.py")
    print("   python src/smartstore_moodanalyzer/country_info.py")
    print()
    print("📚 Make sure to:")
    print("   1. Copy .env.example to .env")
    print("   2. Add your OPENAI_API_KEY to .env")
    print("   3. Run 'uv sync' to install dependencies")
    print("=" * 60)

if __name__ == "__main__":
    main()
