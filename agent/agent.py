import requests
from agent.prompt import SYSTEM_PROMPT

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:7b"

def ask_agent(user_input: str) -> str:
    full_prompt = SYSTEM_PROMPT + "\n\nErreur technique:\n" + user_input

    payload = {
        "model": MODEL,
        "prompt": full_prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=60)

    if response.status_code != 200:
        return f"[ERREUR OLLAMA API]\n{response.text}"

    data = response.json()
    return data.get("response", "").strip()
