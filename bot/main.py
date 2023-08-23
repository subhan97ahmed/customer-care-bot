import os
import utils
from langchain.schema import messages_to_dict
from InfoExtraction import InfoExtraction
from langchain import PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferWindowMemory, ConversationBufferMemory, ChatMessageHistory
from langchain.llms import OpenAI
from db import ChromaDBHandler

os.environ["OPENAI_API_KEY"] = "sk-"


class Chatbot:
    def __init__(self, use_local_history=False):
        self.db_handler = ChromaDBHandler()
        self.db = self.db_handler.load_db()
        self.use_local_history = use_local_history
        self.template = """
        ### Instruction: You're a customer support agent for an e-commerce site that is talking to a customer. Use only information provided by the human in chat history and the following information
        {context}
        to answer in a helpful manner to the question.
        Keep your replies short, informative and compassionate.
        Remember User information from the following
        {chat_history}
        ### Input: {question}
        ### Response:
        """.strip()
        if self.use_local_history:
            self.memory = ConversationBufferMemory(
                memory_key="chat_history",
                human_prefix="### Input",
                ai_prefix="### Response",
                output_key="answer",
                return_messages=True,
                chat_memory=ChatMessageHistory(messages=utils.load_json("../data/history.json"))
            )
        else:
            self.memory = ConversationBufferMemory(
                memory_key="chat_history",
                human_prefix="### Input",
                ai_prefix="### Response",
                output_key="answer",
                return_messages=True,
            )
        self.prompt = PromptTemplate(
            input_variables=['context', 'question', 'chat_history'], template=self.template
        )

        self.conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=OpenAI(temperature=0.5),
            chain_type="stuff",
            retriever=self.db.as_retriever(),
            memory=self.memory,
            combine_docs_chain_kwargs={"prompt": self.prompt},
            return_source_documents=True,
            verbose=False,
            rephrase_question=False
        )

        self.extractor = InfoExtraction()

    def handle_input(self, input_text):
        response = self.conversation_chain(input_text)
        print("Bot: " + response['answer'])
        # print(self.conversation_chain.memory)

    def run(self):
        while True:
            user_input = input("User: ")
            self.handle_input(user_input)

            if user_input.strip().lower() == "bye":
                break


if __name__ == "__main__":
    chatbot = Chatbot(use_local_history=True)
    chatbot.run()
    messages = chatbot.memory.chat_memory.messages
    history = ChatMessageHistory(messages=messages)

    # Extracted data
    extracted_data = chatbot.extractor.extract_order_info(str(messages_to_dict(messages)))
    utils.save_as_json("user_likes", extracted_data)
    utils.save_as_json("history", messages_to_dict(history.messages))
