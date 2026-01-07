# LangChain Assistant

A multilingual AI assistant built with LangChain and AWS Bedrock.

## Setup

1. Create virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate
```

2. Install dependencies:
```bash
   pip install -r requirements.txt
```

3. Configure AWS credentials in .env:
```bash
   AWS_PROFILE=default
```

4. Run the chatbot:
```bash
   python main.py
```

## Testing
```bash
pytest tests/ -v
```
