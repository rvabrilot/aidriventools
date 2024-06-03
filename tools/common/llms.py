from tools.common.llm.llama import generate_llama_summary
from tools.common.llm.gpt import generate_gpt_summary

def summarize_text(model, text, language):
    """
    Summarizes the given text using the specified model.

    Args:
        model (str): The name of the model to use for summarization. Valid options are "gpt-4o" and "llama3".
        text (str): The input text to be summarized.
        language (str): The language of the input text. Defaults to "English".

    Returns:
        str: The summarized text generated by the specified model.

    Raises:
        ValueError: If the specified model is not "gpt-4o" or "llama3".
    """
    if model == "gpt-4o":
        return generate_gpt_summary(text, language)
    elif model == "llama3":
        return generate_llama_summary(text, language)