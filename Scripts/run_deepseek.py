import requests

API_URL = "http://localhost:1234/v1/chat/completions"
MODEL = "DeepSeek-R1-Distill-Qwen-7B-GGUF"

def chat(prompt):
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(API_URL, json=data).json()
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    prompt = "Explain quantum computing simply."
    answer = chat(prompt)
    print(f"DeepSeek-R1 says:\n{answer}")
