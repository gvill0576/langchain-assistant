#!/usr/bin/env python3
"""
Manual testing script for LangGraph workflows and agents.
Run this to see your workflows in action!
"""

from src.state import create_initial_state, get_state_summary
from src.workflows import run_research_workflow
from src.agents import run_agent

def test_linear_workflow():
    """Test the linear workflow"""
    print("=" * 60)
    print("TESTING LINEAR WORKFLOW")
    print("=" * 60)
    
    query = "benefits of solar energy"
    print(f"\nQuery: {query}")
    print("Running workflow...\n")
    
    result = run_research_workflow(query, "linear")
    summary = get_state_summary(result)
    
    print(f"\n✅ Workflow Complete!")
    print(f"Steps executed: {summary['steps']}")
    print(f"Quality score: {summary['quality']}")
    print(f"\nFinal Summary:")
    print(result['summary'][:300] + "...")

def test_conditional_workflow():
    """Test the conditional workflow"""
    print("\n" + "=" * 60)
    print("TESTING CONDITIONAL WORKFLOW")
    print("=" * 60)
    
    # This query should trigger cost research
    query = "solar panel installation costs"
    print(f"\nQuery: {query}")
    print("Expected: Should trigger cost research branch")
    print("Running workflow...\n")
    
    result = run_research_workflow(query, "conditional")
    
    print(f"\n✅ Workflow Complete!")
    print(f"Steps executed: {result['step_count']}")
    print(f"\nFinal Summary:")
    print(result['summary'][:300] + "...")

def test_agent():
    """Test the agent"""
    print("\n" + "=" * 60)
    print("TESTING AGENT")
    print("=" * 60)
    
    query = "Research and summarize renewable energy benefits"
    print(f"\nQuery: {query}")
    print("Expected: Agent should use multiple tools")
    print("Running agent...\n")
    
    result = run_agent(query)
    
    print(f"\n✅ Agent Complete!")
    print(f"\nResult:")
    print(result[:400] + "...")

if __name__ == "__main__":
    print("🚀 LangGraph and Agents - Manual Testing")
    print("=" * 60)
    
    # Run tests
    test_linear_workflow()
    test_conditional_workflow()
    test_agent()
    
    print("\n" + "=" * 60)
    print("✅ All manual tests completed!")
    print("=" * 60)
