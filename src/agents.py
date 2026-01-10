from langchain.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from src.client import create_llm

def get_llm():
    """Get LLM instance for agent"""
    return create_llm()

def create_agent_tools():
    """Create tools that the agent can choose from"""
    llm = get_llm()
    
    def research_tool(topic: str) -> str:
        """Research a topic"""
        print(f"🔍 Tool: Researching '{topic}'")
        try:
            response = llm.invoke(f"Research and provide key information about: {topic}")
            return f"Research Results: {response.content}"
        except Exception as e:
            return f"Research Error: {str(e)}"
    
    def analyze_tool(data: str) -> str:
        """Analyze data"""
        print(f"📊 Tool: Analyzing data")
        try:
            response = llm.invoke(f"Analyze this information and provide insights: {data[:500]}")
            return f"Analysis: {response.content}"
        except Exception as e:
            return f"Analysis Error: {str(e)}"
    
    def summarize_tool(content: str) -> str:
        """Summarize content"""
        print(f"📝 Tool: Summarizing")
        try:
            response = llm.invoke(f"Provide a clear, concise summary of: {content[:500]}")
            return f"Summary: {response.content}"
        except Exception as e:
            return f"Summary Error: {str(e)}"
    
    def fact_check_tool(claim: str) -> str:
        """Fact-check a claim"""
        print(f"✅ Tool: Fact-checking")
        try:
            response = llm.invoke(f"Evaluate the accuracy of this claim and provide evidence: {claim}")
            return f"Fact Check: {response.content}"
        except Exception as e:
            return f"Fact Check Error: {str(e)}"
    
    # Package each function as a Tool
    tools = [
        Tool(
            name="Research",
            description="Research any topic to gather comprehensive information",
            func=research_tool
        ),
        Tool(
            name="Analyze",
            description="Analyze data or information to extract insights and patterns",
            func=analyze_tool
        ),
        Tool(
            name="Summarize",
            description="Create a concise summary of content or information",
            func=summarize_tool
        ),
        Tool(
            name="FactCheck",
            description="Verify the accuracy of claims and provide evidence",
            func=fact_check_tool
        ),
    ]
    
    return tools

def create_research_agent():
    """Create an agent that autonomously selects tools"""
    print("🤖 Building research agent...")
    
    llm = get_llm()
    tools = create_agent_tools()
    
    # Instructions for the agent
    agent_prompt = PromptTemplate.from_template("""You are a research assistant with access to tools.

Available tools: {tool_names}

Tool descriptions:
{tools}

Think step by step about which tools to use to help answer the user's request.

User Request: {input}

{agent_scratchpad}""")
    
    # Create ReAct agent (Reasoning + Acting)
    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=agent_prompt
    )
    
    # Create executor
    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,  # Show the thinking process
        max_iterations=5,  # Don't loop forever
        handle_parsing_errors=True
    )
    
    print("✅ Research agent created")
    return executor

def run_agent(query: str) -> str:
    """Run the research agent on a query"""
    agent = create_research_agent()
    result = agent.invoke({"input": query})
    return result["output"]

def get_all_tools():
    """Get list of all available tools"""
    return create_agent_tools()
