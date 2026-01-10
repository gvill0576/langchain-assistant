import pytest
from src.workflows import (
    create_linear_workflow,
    create_conditional_workflow,
    run_research_workflow
)


def test_create_linear_workflow():
    """Test that linear workflow can be created"""
    workflow = create_linear_workflow()
    assert workflow is not None


def test_create_conditional_workflow():
    """Test that conditional workflow can be created"""
    workflow = create_conditional_workflow()
    assert workflow is not None


def test_run_research_workflow_exists():
    """Test that run function exists and is callable"""
    assert callable(run_research_workflow)


def test_linear_workflow_compiles_without_error():
    """Test that linear workflow compiles successfully"""
    try:
        workflow = create_linear_workflow()
        assert workflow is not None
    except Exception as e:
        pytest.fail(f"Linear workflow compilation failed: {e}")


def test_conditional_workflow_compiles_without_error():
    """Test that conditional workflow compiles successfully"""
    try:
        workflow = create_conditional_workflow()
        assert workflow is not None
    except Exception as e:
        pytest.fail(f"Conditional workflow compilation failed: {e}")
