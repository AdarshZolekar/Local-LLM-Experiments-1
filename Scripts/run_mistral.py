import requests

API_URL = "http://localhost:1234/v1/chat/completions"
MODEL = "Mistral-7B-Instruct-v0.2-GGUF"

def chat(prompt):
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(API_URL, json=data).json()
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    prompt = "Write a short story about a robot learning Python."
    answer = chat(prompt)
    print(f"Mistral says:\n{answer}")
