import json
import gradio as gr
import base64
import requests

# Set the model to use
model_to_use = "llama3"

# Open the image file and encode it as a base64 string
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def generate_chat_response(input, chat_history):
    """
    Generates a chat response using the Llama model.

    Args:
        input (dict): A dictionary containing the input text and optional files.
            The input text is expected to be in the 'text' key.
        chat_history (list): A list of previous chat messages. Currently not used.

    Returns:
        str: The generated chat response.

    Raises:
        None

    Description:
        This function generates a chat response using the Llama model. It sends a POST request to the
        Llama API with the provided input text and system prompt. If the request is successful, it
        extracts the generated response from the API response and returns it. If the request fails, it
        returns an error message indicating the status code of the failed request.

        The input dictionary should have the following structure:
        {
            'text': str,
            'files': Optional[List[str]]
        }

        The 'text' key should contain the input text for generating the chat response. The 'files' key is
        optional and can be used to provide additional files (e.g., images) for the chat.

        The chat history is not used in this function and can be left empty.

        The function returns the generated chat response as a string.
    """
    systemPrompt = f"You are a helpful assistant that responds in Markdown."

    url = "http://localhost:11434/api/generate"

    payload = {
        "model": model_to_use,
        "prompt": input['text'], 
        "system": systemPrompt,
        "stream": False
    }

    # Convert the payload to a JSON string
    payload_json = json.dumps(payload)

    # Set the headers to specify JSON content
    headers = {
          "Content-Type": "application/json"
    }

      # Send the POST request
    response = requests.post(url, data=payload_json, headers=headers)
    content = ""
    if response.status_code == 200:
            output = json.loads(response.text)
            context = output['context']
            content = output['response']
    else:
         content = f"Request failed with status code {response.status_code}"

    return content

def generate_llama_summary(input, language="English"):
    """
    Generates a summary of the given input text using the Llama model.

    Args:
        input (str): The text to be summarized.
        language (str, optional): The language of the input text. Defaults to "English".

    Returns:
        str: The generated summary of the input text. If the request fails, it returns an error message
        indicating the status code of the failed request.

    Description:
        This function sends a POST request to the Llama API with the provided input text and system prompt.
        If the request is successful, it extracts the generated response from the API response and returns it.
        The function returns the generated chat response as a string.

        The input dictionary should have the following structure:
        {
            'text': str,
            'files': Optional[List[str]]
        }

        The 'text' key should contain the input text for generating the chat response. The 'files' key is
        optional and can be used to provide additional files (e.g., images) for the chat.

        The chat history is not used in this function and can be left empty.
    """
    systemPrompt = f"You are a helpful assistant that summarizes text and responds in {language}."

    url = "http://localhost:11434/api/generate"

    payload = {
        "model": model_to_use,
        "prompt": "summarize the following text: " + input, 
        "system": systemPrompt,
        "stream": False
    }

    # Convert the payload to a JSON string
    payload_json = json.dumps(payload)

    # Set the headers to specify JSON content
    headers = {
          "Content-Type": "application/json"
    }

      # Send the POST request
    response = requests.post(url, data=payload_json, headers=headers)
    content = ""
    if response.status_code == 200:
            output = json.loads(response.text)
            context = output['context']
            content = output['response']
    else:
         content = f"Request failed with status code {response.status_code}"

    return content
