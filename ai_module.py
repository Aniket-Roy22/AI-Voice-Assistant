import requests
import json
import os

def aiResponse(prompt: str) -> str:
    api_key = os.getenv("deepseek-client-key")
    response = requests.post(
	url="https://openrouter.ai/api/v1/chat/completions",
	headers={
		"Authorization": "Bearer " + api_key,
	},
	data=json.dumps({
		"messages": [
		{
			"role": "user",
			"content": prompt
		}
		]
	})
	)

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]