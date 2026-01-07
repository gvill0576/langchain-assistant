from src.chains import chat, summarize

def main():
    print("Testing Multilingual Assistant")
    print("=" * 40)
    
    # Test English
    response = chat("English", "What is the capital of France?")
    print(f"English: {response}\n")
    
    # Test Spanish
    response = chat("Spanish", "What is the capital of France?")
    print(f"Spanish: {response}\n")
    
    # Test Summarizer
    text = "LangChain is a framework for developing applications powered by language models. It enables applications that are context-aware and can reason about how to answer based on provided context."
    summary = summarize(text, "brief")
    print(f"Summary: {summary}")

if __name__ == "__main__":
    main()
