from db import load_db
from langchain import ConversationChain, LLMChain, PromptTemplate
from langchain.chains import ConversationalRetrievalChain, StuffDocumentsChain
from langchain.memory import ConversationBufferWindowMemory, ConversationBufferMemory
from langchain.memory import ConversationSummaryMemory
from langchain.llms import OpenAI

db = load_db()
template = """
### Instruction: You're a customer support agent for an e-commerce site that is talking to a customer. Use only chat history and the following information
{context}
to answer in a helpful manner to the question.
Keep your replies short, informative and compassionate.
{chat_history}
### Input: {question}
### Response:
""".strip()

prompt = PromptTemplate(
    input_variables=['context', 'question', 'chat_history'], template=template
)
memory = ConversationBufferMemory(
    memory_key="chat_history",
    human_prefix="### Input",
    ai_prefix="### Response",
    output_key="answer",
    return_messages=True,
    # window_size=10
)

conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=db.as_retriever(),
    memory=memory,
    combine_docs_chain_kwargs={"prompt": prompt},
    return_source_documents=True,
    verbose=True
)


def handle_input(input_text):
    response = conversation_chain(input_text)

    print("Bot: " + response['answer'])


while True:
    user_input = input("User: ")

    handle_input(user_input)
