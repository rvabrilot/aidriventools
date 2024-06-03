# AIDrivenTools

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## Introduction

A Gradio based web application implementing various useful tools driven by AI in different shapes

## Features

- Remote chatbot, currently using Openai GPT-4o (you need a valid API Key for this)
- Local chatbot, currently using Llama3 on [ollama](https://github.com/ollama/ollama/) (no API Key needed)
- SQL code tools:
    - Eliminate subqueries converting the code to use Common Table Expressions
    - Make the Sql Code looking pretty (enhancing readibility and maintenability)
- Youtube tools:
    - Mp4 video downloader
    - Mp3 audio downloader
    - audio transcriber and summary, useful to know better what is the video actually about BEFORE seeing it and helping save time on youtuber's bussiness

## Installation

### Prerequisites

Everything is in python using gradio for web ui along with other heavy duty libraries like torch, sql-glot, openai whisper, etc.

### Steps

1. Clone the repository:
    ```powershell
    git clone https://github.com/rvabrilot/aidriventools.git
    ```
2. Navigate to the project directory:
    ```powershell
    cd aidriventools
    ```
3. Create and activate a python dev environment, Windows instrucctions example:
    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```
4. Install dependencies:
    ```powershell
    pip install -r requirements.txt
    ```
5. Set you Openai API key using the keyring on another project or folder, don´t write it directly in the code unless you make sure knobody else will see that code
    ```python
    import keyring
    keyring.set_password("VSCode", "openai_api_key", "sk-THIS_IS_FAKE_API_KEY_DONT_USE_IT_AND_REPLACE_IT_WITH_A_REAL_ONE")
    ```

## Usage

Provide instructions and examples on how to use your project.

```powershell
python app.py
```

navigate to http://localhost:7865

## Contributing

If you have a new feature in mind or in code, please let me know by a Pull Request or email me.
If you just want to steal other's people code, remember this "Alone you will be faster, Together we'll get further"
