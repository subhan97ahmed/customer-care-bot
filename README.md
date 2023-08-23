# Customer Care Bot


## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Introduction
Welcome to the Customer Care Bot! This README provides an overview of the approach, methods, decisions, assumptions, and instructions for setting up and running the project.

## Approach and Methods

The Chatbot is designed to act as a customer support agent for an e-commerce site. It leverages the OpenAI language model for conversational interactions. The key functionalities include answering customer queries, providing product recommendations, and extracting order IDs and product preferences.

## Decisions Taken

1. **Language Model:** OpenAI's GPT-3.5 is used for generating responses and maintaining conversations.
2. **Memory Management:** A ConversationBufferMemory is employed to store and manage chat history.
3. **Info Extraction:** An InfoExtraction module is created to extract order IDs and product preferences from conversations.

## Assumptions

1. Users will interact with the bot in a conversational manner.
2. The bot will maintain context within a session but will not store information across sessions(only locally for now).
3. Users are interested in receiving accurate and helpful responses.

## Prerequisites


- Python 3.10+
- OpenAI API key
- `venv` module (install with `pip install virtualenv` if needed)

## Installation

Instructions on how to install and set up the project.

```bash
git clone https://github.com/subhan97ahmed/customer-care-bot.git
cd customer-care-bot
```


<details>
<summary>Create and Activate Virtual Environment</summary>
<!--All you need is a blank line-->

1. **Navigate to Project Directory:**
    
   ```bash
    cd /path/to/your/project
   ```

2. **Create Virtual Environment:**
    
   For macOS and Linux:

   ```bash
   pip install virtualenv
   python3 -m venv env
   ```

   For Windows:
   ```bash
   pip install virtualenv
   python -m venv env
   ```

3. **Activate Virtual Environment:**

   For macOS and Linux:

   ```bash
   source env/bin/activate
   ```

   For Windows:

   ```bash
   .\env\Scripts\activate
   ```
</details>


```bash
pip install -r requirements.txt
```

## Usage
open main.py and add openai api key
```python
import os
os.environ["OPENAI_API_KEY"] = "your-api-key"
```

```bash
# Run the application
cd bot
python main.py
```

### API Usage
```bash
# Run the application
cd bot
uvicorn api_endpoint:app --reload
```
open browser and go to http://127.0.0.1:8000/docs
