import os

hf_token = os.getenv("HF_TOKEN")
if not hf_token:
    raise ValueError("HF_TOKEN is not set.")

from smolagents import CodeAgent, InferenceClientModel, DuckDuckGoSearchTool

model = InferenceClientModel()

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model
)

result = agent.run("Find two recent open-source coding-agent libraries and summarize them briefly.")

print(result)