import gradio as gr
from tools.common.llm.llama import generate_chat_response, model_to_use

chat_interface_local = gr.ChatInterface(fn=generate_chat_response, multimodal=True)
chat_interface_local.chatbot.height="600px"
chat_interface_local.chatbot.label=model_to_use