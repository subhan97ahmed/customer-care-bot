# Customer Care Bot 🤖
The Customer Care Bot is a cutting-edge customer support solution designed to revolutionize the way e-commerce websites interact with and assist their customers. Powered by OpenAI's advanced GPT-3.5 language model, this intelligent bot offers a seamless and personalized customer service experience.

## Key Features:

1. **Conversational Expertise:** The Customer Care Bot engages customers in dynamic, natural conversations, making them feel heard and understood. It replicates the warmth and effectiveness of human customer support.

2. **Efficient Query Resolution:** With its deep understanding of natural language, the bot efficiently addresses customer queries, providing precise and timely responses. Customers no longer need to wait for support staff to get answers.

3. **Product Recommendations:** Leveraging its knowledge of products and customer preferences, the bot can recommend relevant products, enhancing upselling and cross-selling opportunities.

4. **Info Extraction:** The bot excels at extracting critical information such as order IDs and product preferences from conversations. This feature streamline processes like order tracking and customization.

5. **Context Management:** Throughout the conversation, the bot maintains context, enabling it to provide consistent and personalized assistance. Customers can switch topics or revisit previous questions seamlessly.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

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

## Contributing
Contributions to the Customer Care Bot project are welcome! If you'd like to contribute, please follow these guidelines:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them with clear, descriptive messages.
- Push your branch to your forked repository.
- Submit a pull request to the main repository, describing the changes you've made.
