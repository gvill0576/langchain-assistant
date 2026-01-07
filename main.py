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

"""Main script to test all components."""

from src.chains import generate_and_evaluate, research_pipeline
from src.memory import chat_with_memory, clear_session
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


def test_memory():
    """Test conversation memory."""
    print("\n" + "=" * 50)
    print("TESTING MEMORY")
    print("=" * 50)
    
    # Clear any old memory for this test
    clear_session("demo")
    
    print("\n--- Conversation with Memory ---")
    
    # Message 1: Tell the bot your name
    response1 = chat_with_memory("Hi, my name is George and I'm learning AI", "demo")
    print(f"User: Hi, my name is George and I'm learning AI")
    print(f"Bot: {response1}")
    
    # Message 2: Tell the bot about your work
    response2 = chat_with_memory("I'm working on a chatbot project", "demo")
    print(f"\nUser: I'm working on a chatbot project")
    print(f"Bot: {response2}")
    
    # Message 3: Test if bot remembers
    response3 = chat_with_memory("What's my name and what am I working on?", "demo")
    print(f"\nUser: What's my name and what am I working on?")
    print(f"Bot: {response3}")
    
    print("\n--- Testing Separate Sessions ---")
    
    # Alice's session
    clear_session("alice")
    alice_response = chat_with_memory("I'm Alice and I love Python", "alice")
    print(f"\nAlice: I'm Alice and I love Python")
    print(f"Bot to Alice: {alice_response}")
    
    # Bob's session
    clear_session("bob")
    bob_response = chat_with_memory("I'm Bob and I love JavaScript", "bob")
    print(f"\nBob: I'm Bob and I love JavaScript")
    print(f"Bot to Bob: {bob_response}")
    
    # Check Alice's memory
    alice_check = chat_with_memory("What do I love?", "alice")
    print(f"\nAlice: What do I love?")
    print(f"Bot to Alice: {alice_check}")  # Should say "Python"
    
    # Check Bob's memory
    bob_check = chat_with_memory("What do I love?", "bob")
    print(f"\nBob: What do I love?")
    print(f"Bot to Bob: {bob_check}")  # Should say "JavaScript"


if __name__ == "__main__":
    test_memory()  # Test memory first
    # test_chains()  # Uncomment to test chains too