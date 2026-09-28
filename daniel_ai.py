import gradio as gr
from groq import Groq
from flask import Flask
import os

# Your Groq API key - keep it here
client = Groq(api_key=os.environ.get("GROQ_API_KEY") or "gsk_YOUR_KEY_HERE")

# System prompt - Who made you
SYSTEM = """You are Daniel AI, created by Daniel Somto from Ufuma, Anambra State, Nigeria.
You are a smart, friendly, helpful AI assistant.
If anyone asks who created you, always say Daniel Somto from Ufuma.
Never say you were created by Meta, OpenAI, or anyone else.
"""

def chat(message, history):
    messages = [{"role": "system", "content": SYSTEM}]
    for user, assistant in history:
        messages.append({"role": "user", "content": user})
        messages.append({"role": "assistant", "content": assistant})
    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        max_tokens=1000
    )
    return response.choices[0].message.content

# Gradio interface
demo = gr.ChatInterface(
    fn=chat,
    title="Daniel AI - Created by Daniel Somto",
    description="Ask me anything! I was built by Daniel from Ufuma!",
    theme="soft"
)

# For PythonAnywhere
app = Flask(__name__)
app = gr.mount_gradio_app(app, demo, path="/")

if __name__ == "__main__":
    demo.launch()
