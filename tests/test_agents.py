import pytest
from src.agents import (
    create_agent_tools,
    create_research_agent,
    run_agent,
    get_all_tools
)


def test_create_agent_tools_callable():
    """Test that tool creation function exists"""
    assert callable(create_agent_tools)


def test_create_research_agent_callable():
    """Test that agent creation function exists"""
    assert callable(create_research_agent)


def test_run_agent_callable():
    """Test that run_agent function exists"""
    assert callable(run_agent)


def test_get_all_tools_returns_list():
    """Test that get_all_tools returns a list"""
    tools = get_all_tools()
    assert isinstance(tools, list)


def test_agent_has_four_tools():
    """Test that agent has exactly 4 tools"""
    tools = get_all_tools()
    assert len(tools) == 4


def test_all_tools_have_names():
    """Test that all tools have name attributes"""
    tools = get_all_tools()
    for tool in tools:
        assert hasattr(tool, 'name')
        assert isinstance(tool.name, str)


def test_all_tools_have_descriptions():
    """Test that all tools have description attributes"""
    tools = get_all_tools()
    for tool in tools:
        assert hasattr(tool, 'description')
        assert isinstance(tool.description, str)


def test_tool_names_are_correct():
    """Test that tools have expected names"""
    tools = get_all_tools()
    tool_names = [tool.name for tool in tools]
    expected_names = ["Research", "Analyze", "Summarize", "FactCheck"]
    assert set(tool_names) == set(expected_names)
