import pytest
from src.state import ResearchState, create_initial_state, get_state_summary


def test_create_initial_state():
    """Test that initial state is created correctly"""
    state = create_initial_state("test query")

    assert state["query"] == "test query"
    assert state["research_results"] == ""
    assert state["analysis"] == ""
    assert state["summary"] == ""
    assert state["quality_score"] == 0
    assert state["iteration_count"] == 0
    assert state["step_count"] == 0
    assert state["error"] is None


def test_initial_state_has_all_fields():
    """Test that all required fields exist in initial state"""
    state = create_initial_state("test")

    required_fields = [
        "query", "research_results", "analysis", "summary",
        "quality_score", "iteration_count", "step_count", "error"
    ]

    for field in required_fields:
        assert field in state, f"Missing required field: {field}"


def test_get_state_summary():
    """Test state summary generation"""
    state = create_initial_state("test query")
    state["step_count"] = 3
    state["quality_score"] = 2

    summary = get_state_summary(state)

    assert summary["query"] == "test query"
    assert summary["steps"] == 3
    assert summary["quality"] == 2
    assert summary["has_error"] is False


def test_state_summary_detects_errors():
    """Test that state summary detects errors"""
    state = create_initial_state("test")
    state["error"] = "Something went wrong"

    summary = get_state_summary(state)
    assert summary["has_error"] is True
