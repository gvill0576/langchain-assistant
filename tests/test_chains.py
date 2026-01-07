"""Tests for chain functionality."""

import pytest
from src.chains import build_simple_chain, build_research_chain
from src.chains import generate_and_evaluate, research_pipeline


def test_simple_chain_exists():
    """Test that build_simple_chain function exists."""
    assert callable(build_simple_chain)


def test_research_chain_exists():
    """Test that build_research_chain function exists."""
    assert callable(build_research_chain)


def test_generate_and_evaluate_exists():
    """Test that generate_and_evaluate wrapper exists."""
    assert callable(generate_and_evaluate)


def test_research_pipeline_exists():
    """Test that research_pipeline wrapper exists."""
    assert callable(research_pipeline)


def test_simple_chain_requires_llm():
    """Test that simple chain expects an LLM parameter."""
    import inspect
    sig = inspect.signature(build_simple_chain)
    assert 'llm' in sig.parameters


def test_research_chain_requires_llm():
    """Test that research chain expects an LLM parameter."""
    import inspect
    sig = inspect.signature(build_research_chain)
    assert 'llm' in sig.parameters