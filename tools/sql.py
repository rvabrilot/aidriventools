from tools.common.sql import *
import gradio as gr


sqli_esf = gr.Interface(
    fn=eliminate_subqueries_from,
    inputs=gr.Code(lines=30, label="SQL query", language="sql"),
    outputs=gr.Code(lines=30, label="Modified SQL query.", language="sql"),    
)
sqli_pret = gr.Interface(
    fn=pretify_sql,
    inputs=gr.Code(lines=30, label="SQL query.", language="sql"),
    outputs=gr.Code(lines=30, label="Modified SQL query.", language="sql"),    
)

sql_iface = gr.TabbedInterface([sqli_esf, sqli_pret], ["Eliminate Subqueries", "Prettify SQL"])