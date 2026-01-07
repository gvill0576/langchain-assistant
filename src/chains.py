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

"""Sequential chains for multi-step AI workflows."""

from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SimpleSequentialChain, SequentialChain
from langchain.prompts import PromptTemplate
from src.client import create_client, create_llm


def build_simple_chain(llm):
    """
    Build a two-step chain: generate ideas, then evaluate them.
    
    Step 1: AI generates 3 ideas for a topic
    Step 2: AI picks the best idea and explains why
    """
    # Step 1: Generate ideas
    idea_prompt = PromptTemplate(
        input_variables=["topic"],
        template="Generate 3 creative ideas for: {topic}. List them numbered 1-3."
    )
    idea_chain = LLMChain(llm=llm, prompt=idea_prompt)
    
    # Step 2: Evaluate ideas
    eval_prompt = PromptTemplate(
        input_variables=["ideas"],
        template="Evaluate these ideas and pick the best one. Explain why:\n\n{ideas}"
    )
    eval_chain = LLMChain(llm=llm, prompt=eval_prompt)
    
    # Connect the two steps
    return SimpleSequentialChain(
        chains=[idea_chain, eval_chain],
        verbose=True  # Shows what's happening at each step
    )


def build_research_chain(llm):
    """
    Build a three-step research pipeline with named outputs.
    
    Step 1: Research the topic (get 3 key facts)
    Step 2: Create a 3-point outline
    Step 3: Write a 2-paragraph summary
    """
    # Step 1: Research
    research_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate(
            input_variables=["topic"],
            template="Research {topic} and provide 3 key facts."
        ),
        output_key="research"  # Name this output so we can access it later
    )
    
    # Step 2: Create outline using the research
    outline_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate(
            input_variables=["topic", "research"],
            template="Create a 3-point outline about {topic} using:\n{research}"
        ),
        output_key="outline"  # Name this output
    )
    
    # Step 3: Write summary using the outline
    summary_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate(
            input_variables=["topic", "outline"],
            template="Write a 2-paragraph summary about {topic} using:\n{outline}"
        ),
        output_key="summary"  # Name this output
    )
    
    # Connect all three steps
    return SequentialChain(
        chains=[research_chain, outline_chain, summary_chain],
        input_variables=["topic"],
        output_variables=["research", "outline", "summary"],
        verbose=True
    )


def generate_and_evaluate(topic):
    """
    Convenience function to run the simple chain.
    
    Args:
        topic: The topic to generate ideas for (e.g., "mobile apps")
    
    Returns:
        The AI's evaluation of which idea is best
    """
    client = create_client()
    llm = create_llm(client)
    chain = build_simple_chain(llm)
    return chain.run(topic)


def research_pipeline(topic):
    """
    Convenience function to run the research pipeline.
    
    Args:
        topic: The topic to research (e.g., "renewable energy")
    
    Returns:
        Dictionary with keys: research, outline, summary
    """
    client = create_client()
    llm = create_llm(client)
    chain = build_research_chain(llm)
    return chain({"topic": topic})