"""Custom tools for AI capabilities."""

from langchain.tools import Tool
from datetime import datetime


def calculator(expression):
    """
    Safely evaluate a math expression.

    Args:
        expression: Math expression like "25 * 4 + 10"

    Returns:
        "Result: X" or "Error: message"
    """
    try:
        allowed = set('0123456789+-*/.()')
        clean = expression.replace(' ', '')

        if not set(clean).issubset(allowed):
            return "Error: Only basic math operations allowed"

        result = eval(clean)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_time(format_type="default"):
    """
    Get current time in various formats.

    Args:
        format_type: "short", "long", "date", or "default"

    Returns:
        Formatted time string
    """
    now = datetime.now()
    formats = {
        "short": now.strftime("%H:%M"),
        "long": now.strftime("%Y-%m-%d %H:%M:%S"),
        "date": now.strftime("%Y-%m-%d"),
        "default": now.strftime("%B %d, %Y at %I:%M %p")
    }
    return formats.get(format_type, formats["default"])


def word_counter(text):
    """
    Count words and characters in text.

    Args:
        text: The text to analyze

    Returns:
        "Words: X, Characters: Y"
    """
    words = len(text.split())
    chars = len(text)
    return f"Words: {words}, Characters: {chars}"


calc_tool = Tool(
    name="Calculator",
    description="Perform basic math. Input: expression like '25 * 4'",
    func=calculator
)

time_tool = Tool(
    name="CurrentTime",
    description=(
        "Get current time. "
        "Input: 'short', 'long', 'date', or 'default'"
    ),
    func=get_time
)

word_tool = Tool(
    name="WordCounter",
    description="Count words and characters. Input: text to analyze",
    func=word_counter
)


def get_all_tools():
    """Return list of all available tools."""
    return [calc_tool, time_tool, word_tool]
