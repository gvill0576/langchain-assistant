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

"""Main script to test all components."""

from src.chains import generate_and_evaluate, research_pipeline
from src.tools import calculator, get_time, word_counter


def test_chains():
    """Test the sequential chains."""
    print("=" * 50)
    print("TESTING CHAINS")
    print("=" * 50)
    
    print("\n--- Simple Chain: Idea Generation ---")
    try:
        result = generate_and_evaluate("mobile app ideas for students")
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n--- Research Pipeline ---")
    try:
        result = research_pipeline("renewable energy")
        print(f"\nResearch: {result['research'][:200]}...")
        print(f"\nOutline: {result['outline'][:200]}...")
        print(f"\nSummary: {result['summary'][:200]}...")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_chains()