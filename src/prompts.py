from langchain_core.prompts import PromptTemplate


def get_assistant_prompt():
    """Return the multilingual assistant prompt template."""
    return PromptTemplate(
        input_variables=["language", "message"],
        template="""You are a helpful assistant. Respond in {language}.

User: {message}
Assistant:"""
    )


def get_summarizer_prompt():
    """Return the text summarizer prompt template."""
    return PromptTemplate(
        input_variables=["length", "text"],
        template="""Summarize the following text. Make the summary {length}.

Text: {text}

Summary:"""
    )


def get_prompt_by_name(name):
    """Return the appropriate prompt template by name."""
    prompts = {
        "assistant": get_assistant_prompt,
        "summarizer": get_summarizer_prompt,
    }
    if name not in prompts:
        raise ValueError(f"Unknown prompt: {name}")
    return prompts[name]()
