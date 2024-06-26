from tools.common.yt import *
from tools.common.llms import summarize_text
from tools.common.storage import store_transcriber
import gradio as gr

mp4_intf = gr.Interface(
        fn = download_mp4s_from_yt,
        inputs=[gr.TextArea(lines=10, label="youtube urls"), gr.Text(value="d:\\video\\landing", label="Carpeta:") ],
        outputs=gr.TextArea(lines=10)
    )

mp3_intf = gr.Interface(
        fn = download_mp3s_from_yt,
        inputs=[gr.TextArea(lines=10, label="youtube urls"), gr.Text(value="d:\\music\\landing", label="Carpeta:") ],
        outputs=gr.TextArea(lines=10)
    )

with gr.Blocks() as transcribe_intf:
    with gr.Row():
        with gr.Column():
            urls = gr.TextArea(lines=1, label="youtube url")
            landing = gr.Text(value="d:\\music\\landing", label="Carpeta:")
            transcribe_btn = gr.Button("Transcribe")
            transcription = gr.TextArea(lines=10, label="Transcription")
        with gr.Column():
            model_drop = gr.Dropdown(["llama3", "gpt-4o" ], value="llama3", label="Model")
            language_drop = gr.Dropdown(["Spanish", "English", "French", "Japanese"], value="Spanish", label="Language")
            summary_btn = gr.Button("Summary")
            summary = gr.TextArea(lines=20, label="Summary")
            store_btn = gr.Button("Store")
            store_info = gr.TextArea(lines=1, label="Store Info")
        

    transcribe_btn.click(fn=transcribe_mp3, inputs=[urls, landing], outputs=[transcription, summary, store_info])
    summary_btn.click(fn=summarize_text, inputs=[model_drop, transcription, language_drop], outputs=[summary, store_info])
    store_btn.click(fn=store_transcriber, inputs=[urls, landing, transcription, summary], outputs=store_info)

yt_iface = gr.TabbedInterface([mp4_intf, mp3_intf, transcribe_intf], ["Mp4 downloader", "Mp3 downloader", "Transcriber"])