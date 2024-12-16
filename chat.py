"""
Install an additional SDK for JSON schema support Google AI Python SDK

$ pip install google.ai.generativelanguage
"""

import os
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GEMINI_API_KEY")[1:]

genai.configure(api_key=key)

# Create the model
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-8b",
  generation_config=generation_config,
  system_instruction="You are an AI desktop assistant designed to provide helpful, accurate, and engaging support to users in their day-to-day activities. Your primary role is to enhance productivity, solve problems, and respond to queries with clarity, empathy, and precision.",
)

history = []

while True:
  user_input = input("You: ")

  chat_session = model.start_chat(
    history=history
  )


  response = chat_session.send_message(user_input)

  model_response = response.text

  print(model_response)
  print()

  # appending user and model response to history.
  history.append({"role": "user", "parts": [user_input]})
  history.append({"role": "model", "parts": [model_response]})