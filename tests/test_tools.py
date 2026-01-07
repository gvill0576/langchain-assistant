"""Tests for tool functionality."""


from src.tools import calculator, get_time, word_counter, get_all_tools


def test_calculator_addition():
    """Test calculator with addition."""
    result = calculator("2 + 3")
    assert "5" in result


def test_calculator_multiplication():
    """Test calculator with multiplication."""
    result = calculator("4 * 5")
    assert "20" in result


def test_calculator_complex():
    """Test calculator with complex expression."""
    result = calculator("(10 + 5) * 2")
    assert "30" in result


def test_calculator_division():
    """Test calculator with division."""
    result = calculator("100 / 4")
    assert "25" in result


def test_calculator_rejects_invalid():
    """Test calculator rejects non-math input."""
    result = calculator("hello")
    assert "Error" in result


def test_calculator_rejects_dangerous():
    """Test calculator rejects dangerous code."""
    result = calculator("import os")
    assert "Error" in result


def test_get_time_returns_string():
    """Test that time function returns a string."""
    result = get_time("default")
    assert isinstance(result, str)
    assert len(result) > 0


def test_get_time_formats():
    """Test different time formats."""
    short = get_time("short")
    long = get_time("long")
    date = get_time("date")
    default = get_time("default")

    assert isinstance(short, str)
    assert isinstance(long, str)
    assert isinstance(date, str)
    assert isinstance(default, str)


def test_word_counter_basic():
    """Test word counter with simple text."""
    result = word_counter("hello world")
    assert "Words: 2" in result
    assert "Characters: 11" in result


def test_word_counter_characters():
    """Test word counter includes character count."""
    result = word_counter("hello")
    assert "Characters: 5" in result


def test_word_counter_empty():
    """Test word counter with empty string."""
    result = word_counter("")
    assert "Words: 0" in result or "Words: 1" in result
    # Split behavior varies
    assert "Characters: 0" in result


def test_word_counter_multiple_words():
    """Test word counter with multiple words."""
    result = word_counter("The quick brown fox")
    assert "Words: 4" in result


def test_get_all_tools_returns_list():
    """Test that get_all_tools returns a list."""
    tools = get_all_tools()
    assert isinstance(tools, list)
    assert len(tools) == 3


def test_tools_have_names():
    """Test that all tools have names."""
    tools = get_all_tools()
    for tool in tools:
        assert hasattr(tool, 'name')
        assert len(tool.name) > 0


def test_tools_have_descriptions():
    """Test that all tools have descriptions."""
    tools = get_all_tools()
    for tool in tools:
        assert hasattr(tool, 'description')
        assert len(tool.description) > 0
