import os

hf_token = os.getenv("HF_TOKEN")
if not hf_token:
    raise ValueError("HF_TOKEN is not set.")

from smolagents import CodeAgent, InferenceClientModel

# Use a hosted model via Hugging Face Inference
model = InferenceClientModel()

# Create a minimal agent with no external tools
agent = CodeAgent(tools=[], model=model)

# Give the agent a task
result = agent.run("Calculate the sum of numbers from 1 to 10.")

print(result)