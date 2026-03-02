from flask import Flask, request
import os
import requests
from google import genai

app = Flask(__name__)

# Initialize Gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route('/', methods=['POST'])
def groupme_webhook():
    data = request.get_json()
    text = data.get('text', '')
    if text.startswith('^') and data.get('sender_type') != 'bot':
        user_message = text[1:].strip()

        response = client.models.generate_content(model="gemini-2.5-flash-lite", contents=user_message)

        bot_response = response.text

        post_data = {
            "bot_id": os.getenv("GROUPME_BOT_ID"),
            "text": bot_response
        }
        requests.post("https://api.groupme.com/v3/bots/post", json=post_data)

    return "OK", 200
