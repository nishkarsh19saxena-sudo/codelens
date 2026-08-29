import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)


def review_code(code: str):

    prompt = f"""
You are an expert competitive programming code reviewer.

Analyze this code:

{code}

Give your answer in this exact format:

EXPLANATION:
Explain what the code is doing.

ISSUES:
List bugs or logical errors. If there are no bugs, say "No major bugs found."

TIME:
Give the time complexity and explain why.

SPACE:
Give the space complexity and explain why.

OPTIMAL:
Say whether the approach is optimal. If not, explain a better approach.

OPTIMIZED_CODE:
Give the improved code. If the original approach is already optimal, give the original code.
"""

    print("Sending request to Hugging Face...")

    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-Coder-32B-Instruct",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=1000,
    )

    result = response.choices[0].message.content

    print("HF RESPONSE:")
    print(result)

    return result