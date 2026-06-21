import os
from smolagents import CodeAgent, InferenceClientModel

hf_token = os.getenv("HF_TOKEN")
if not hf_token:
    raise ValueError("HF_TOKEN is not set.")

model = InferenceClientModel(
    model_id="meta-llama/Llama-3.3-70B-Instruct",
    token=hf_token
)

agent = CodeAgent(
    tools=[],
    model=model,
    add_base_tools=True
)

result = agent.run("Could you give me the 118th Fibonacci number?")
print(result)