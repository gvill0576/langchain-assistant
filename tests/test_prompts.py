import pytest
from src.prompts import get_assistant_prompt, get_summarizer_prompt, get_prompt_by_name

def test_assistant_prompt_formats():
    """Test that assistant prompt formats correctly."""
    prompt = get_assistant_prompt()
    result = prompt.format(language="Spanish", message="Hello")
    assert "Spanish" in result
    assert "Hello" in result

def test_summarizer_prompt_formats():
    """Test that summarizer prompt formats correctly."""
    prompt = get_summarizer_prompt()
    result = prompt.format(length="brief", text="Some text here")
    assert "brief" in result
    assert "Some text here" in result

def test_get_prompt_by_name_assistant():
    """Test getting assistant prompt by name."""
    prompt = get_prompt_by_name("assistant")
    assert "language" in prompt.input_variables

def test_get_prompt_by_name_summarizer():
    """Test getting summarizer prompt by name."""
    prompt = get_prompt_by_name("summarizer")
    assert "length" in prompt.input_variables

def test_get_prompt_by_name_invalid():
    """Test that invalid prompt name raises error."""
    with pytest.raises(ValueError):
        get_prompt_by_name("invalid_prompt")
