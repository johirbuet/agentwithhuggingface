from smolagents import CodeAgent, InferenceClientModel, WebSearchTool

model = InferenceClientModel(
    model_id="Qwen/Qwen3-Next-80B-A3B-Thinking"
)

agent = CodeAgent(
    tools=[WebSearchTool()],
    model=model,
    stream_outputs=True
)

result = agent.run(
    "Find the official documentation page for smolagents and summarize what the library does."
)

print(result)
