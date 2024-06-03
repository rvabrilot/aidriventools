import gradio as gr
from tools.chat_gpt import chat_interface
from tools.chat_llama3_local import chat_interface_local
from tools.sql import sql_iface
from tools.yt import yt_iface

tabs = [chat_interface, chat_interface_local, sql_iface, yt_iface]
tabs_labels = ["ChatGPT", "Llama3", "SQL Tools", "Youtube tools"]
interface = gr.TabbedInterface(
    tabs, 
    tabs_labels, 
    theme=gr.themes.Glass()
)

if __name__ == "__main__":
    interface.launch(server_name="0.0.0.0", server_port=7865)