from smolagents import tool

@tool
def normalize_whitespace(text: str) -> str:
    """
    Normalize repeated whitespace in a text string.

    Args:
        text: The input text whose whitespace should be cleaned.
    """
    return " ".join(text.split())

from smolagents import CodeAgent, InferenceClientModel

model = InferenceClientModel()

agent = CodeAgent(
    tools=[normalize_whitespace],
    model=model
)

result = agent.run(
    "Clean the spacing in this sentence and tell me how many words it has: "
    "'This   is    a   badly   spaced   sentence.'"
)

print(result)