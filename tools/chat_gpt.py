import gradio as gr
from tools.common.llm.gpt import generate_chat_response, model_to_use


chat_interface = gr.ChatInterface(fn=generate_chat_response, multimodal=True)
chat_interface.chatbot.height="600px"
chat_interface.chatbot.label=model_to_use