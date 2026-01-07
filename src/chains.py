from langchain_core.output_parsers import StrOutputParser
from src.prompts import get_prompt_by_name
from src.client import create_client, create_llm


def build_chain(prompt_name="assistant"):
    """Build and return an LCEL chain."""
    prompt = get_prompt_by_name(prompt_name)
    client = create_client()
    llm = create_llm(client)

    # LCEL: prompt -> model -> output parser
    chain = prompt | llm | StrOutputParser()
    return chain


def chat(language, message):
    """Send a message and get a response."""
    chain = build_chain("assistant")
    response = chain.invoke({
        "language": language,
        "message": message
    })
    return response


def summarize(text, length="brief"):
    """Summarize text."""
    chain = build_chain("summarizer")
    response = chain.invoke({
        "text": text,
        "length": length
    })
    return response
