import pytest
from src.nodes import (
    research_node, analysis_node, summary_node,
    cost_research_node, expand_research_node,
    decide_after_research
)

def test_research_node_callable():
    """Test that research node is a callable function"""
    assert callable(research_node)

def test_analysis_node_callable():
    """Test that analysis node is a callable function"""
    assert callable(analysis_node)

def test_summary_node_callable():
    """Test that summary node is a callable function"""
    assert callable(summary_node)

def test_cost_research_node_callable():
    """Test that cost research node is a callable function"""
    assert callable(cost_research_node)

def test_expand_research_node_callable():
    """Test that expand research node is a callable function"""
    assert callable(expand_research_node)

def test_decide_after_research_detects_cost():
    """Test decision function identifies cost keywords"""
    state = {"research_results": "This solution is expensive and costly"}
    result = decide_after_research(state)
    assert result == "cost_research"

def test_decide_after_research_detects_short_content():
    """Test decision function identifies brief content"""
    state = {"research_results": "Brief content"}
    result = decide_after_research(state)
    assert result == "expand_research"

def test_decide_after_research_accepts_sufficient_content():
    """Test decision function accepts sufficient content"""
    # Create content over 300 characters
    long_content = "A" * 400
    state = {"research_results": long_content}
    result = decide_after_research(state)
    assert result == "analysis"
