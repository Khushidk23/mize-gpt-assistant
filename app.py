import os
import gradio as gr
from openai import OpenAI

# Initialize OpenAI client with the new SDK
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

SYSTEM_PROMPT = """
You are an expert assistant in maize warehouse management.
You answer questions related to maize storage, pest control, moisture control, and inventory tracking in a professional and helpful tone.
"""

def maize_warehouse_bot(question):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question}
            ],
            temperature=0.4,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Gradio Interface
iface = gr.Interface(
    fn=maize_warehouse_bot,
    inputs=gr.Textbox(lines=2, placeholder="Ask a maize warehouse question..."),
    outputs="text",
    title="📦 Maize Warehouse GPT Assistant",
    description="Ask about maize storage, pest control, moisture, or inventory tracking."
)

iface.launch()
