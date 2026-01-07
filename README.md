# LangChain Assistant

![Test](https://github.com/gvill0576/langchain-assistant/actions/workflows/test.yml/badge.svg)
![Lint](https://github.com/gvill0576/langchain-assistant/actions/workflows/lint.yml/badge.svg)

A multilingual AI assistant built with LangChain and AWS Bedrock.

## Features

- ✨ Multilingual chatbot (responds in any language)
- 📝 Text summarization (brief or detailed)
- 🧪 Automated testing with pytest
- 🚀 CI/CD with GitHub Actions
- 🏗️ Clean, modular code structure

## Setup

1. Clone the repository:
```bash
   git clone https://github.com/gvill0576/langchain-assistant.git
   cd langchain-assistant
```

2. Create virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Configure AWS credentials in .env:
```bash
   AWS_PROFILE=default
```

5. Run the chatbot:
```bash
   python main.py
```

## Testing

Run tests locally:
```bash
pytest tests/ -v
```

Run linting:
```bash
flake8 src/ tests/ --max-line-length=100
```

## Project Structure
```
langchain-assistant/
├── .github/
│   └── workflows/
│       ├── lint.yml      # Linting automation
│       └── test.yml      # Test automation (Python 3.10, 3.11)
├── src/
│   ├── __init__.py
│   ├── client.py         # AWS Bedrock client setup
│   ├── prompts.py        # Prompt templates
│   └── chains.py         # LCEL chains
├── tests/
│   ├── __init__.py
│   └── test_prompts.py   # Unit tests
├── .env                  # AWS configuration (not committed)
├── .gitignore
├── requirements.txt
├── README.md
└── main.py              # Entry point
```

## Technologies

- **LangChain** - AI application framework
- **AWS Bedrock** - Foundation model access
- **pytest** - Testing framework
- **GitHub Actions** - CI/CD automation
- **flake8** - Code quality/linting

## Author

George Villanueva ([@gvill0576](https://github.com/gvill0576))
