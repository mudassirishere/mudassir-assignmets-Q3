# Smart Store Mood Analyzer

A Python project demonstrating Agentic AI concepts with three assignments using the Gemini API.

## 🎯 Assignments

1. **Smart Store Agent** (`product_suggester.py`) - Product suggestions based on user needs
2. **Mood Analyzer with Handoff** (`mood_checker.py`) - Two-agent mood analysis system  
3. **Country Info Bot with Tools** (`country_info.py`) - Multi-tool country information system

## 🚀 Quick Start

1. **Install dependencies**:
   ```bash
   uv sync
   ```

2. **Set up environment**:
   ```bash
   cp .env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

3. **Get OpenAI API key**:
   - Visit [OpenAI Platform](https://platform.openai.com/api-keys)
   - Create a new API key
   - Add it to your `.env` file

4. **Run assignments**:
   ```bash
   python src/smartstore_moodanalyzer/product_suggester.py
   python src/smartstore_moodanalyzer/mood_checker.py
   python src/smartstore_moodanalyzer/country_info.py
   ```

## 📁 Project Structure

```
smartStore-moodAnalyzer/
├── pyproject.toml              # Dependencies
├── .env.example               # Environment template
├── README.md                  # This file
└── src/smartstore_moodanalyzer/
    ├── __init__.py           # Main module
    ├── product_suggester.py  # Assignment 1
    ├── mood_checker.py       # Assignment 2
    └── country_info.py       # Assignment 3
```

## 🎮 Usage Examples

### Assignment 1: Smart Store Agent
```python
# Input: "I have a headache"
# Output: Suggests Paracetamol with explanation
```

### Assignment 2: Mood Analyzer with Handoff
```python
# Input: "I feel really down today"
# Output: Detects "sad" mood → suggests uplifting activities
```

### Assignment 3: Country Info Bot
```python
# Input: "Pakistan"
# Output: Capital, language, population information
```

## 🔧 Dependencies

- `openai>=1.107.2` - OpenAI SDK
- `python-dotenv>=1.1.1` - Environment variables

## 🆘 Troubleshooting

- **Import errors**: Run `uv sync` to install dependencies
- **API key errors**: Make sure `OPENAI_API_KEY` is set in `.env`
- **Model errors**: Ensure your API key has access to OpenAI models

---

**Happy coding! 🚀**