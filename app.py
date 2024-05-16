import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import faiss
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
# from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import bot_template, user_template, css
from langchain_community.vectorstores import qdrant
import qdrant_client
import os
from langchain_groq import ChatGroq
# from langchain_community.llms import huggingface_hub
# from langchain.llms import huggingface_hub

def get_vectorstores():
    client = qdrant_client.QdrantClient(
        os.getenv("QDRANT_HOST"),
        api_key=os.getenv("QDRANT_API_KEY")
    )
    
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    vector_store = qdrant.Qdrant(
        client=client, 
        collection_name=os.getenv("QDRANT_COLLECTION_NAME"), 
        embeddings=embeddings,
    )
    return vector_store

def get_conversation_chain(vectorstore):
    # my_llm = ChatOpenAI(model = "gpt-4")
    my_llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")
    # my_llm = huggingface_hub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=my_llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_UserInput(user_question):
        if st.session_state.conversation:
            response = st.session_state.conversation({'question': user_question})
            st.session_state.chat_history = response.get('chat_history', [])

            with st.spinner('Initializing magical powers...'):
                for i, message in enumerate(st.session_state.chat_history):
                    if i % 2 == 0:
                        st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
                    else:
                        st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.error("Conversation not initialized.")
    
def main():
    try:
        load_dotenv()
        st.set_page_config(page_title="Wizarding World Explorer 🧙‍♂️✨",
                        page_icon=":books:")

        st.write(css, unsafe_allow_html=True)

        # Sidebar
        st.sidebar.title("Wizarding World Explorer 🧙‍♂️✨")
        # About the app
        st.sidebar.subheader("📜 About This App")
        st.sidebar.write("""
        A magical interface to uncover the secrets of wizardry and witchcraft. For those potter-heads who believe in the power of magic.
        """)

        # Tech behind the app
        st.sidebar.subheader("🔮 Under the Hood")
        st.sidebar.write("""
        - **RAG**: Combines the power of retrieval and generation, fetching relevant data and weaving it into coherent responses using LangChain.
        - **LLM**: Harnesses GPT's prowess for understanding and generating human-like text.
        - **Vector DB**: Employs Qdrant to swiftly search through high-dimensional spaces, ensuring knowledge is retrieved at wizard speed.
        """)

        # About the creator
        # st.sidebar.subheader("🧙‍♂️ Created with love by Yash Bharambay")
        st.sidebar.markdown("""
        ---
        #### 🧙‍♂️ Created By
        **Yash Bharambay** 👨‍💻
        
        [![Portfolio](https://img.shields.io/badge/Portfolio-Yash_Bharambay-blue?logo=About.me)](https://yashbharambay.vercel.app)
    """, unsafe_allow_html=True)

        
      
        if "conversation" not in st.session_state:
            with st.spinner('Processing'):
                st.session_state.conversation = None
                vectorstore = get_vectorstores()
                st.session_state.conversation = get_conversation_chain(vectorstore)

                st.success('Conversation Chain Initialized!')
        # # Initialize user input
        # if "text_input" not in st.session_state:
        #     st.session_state.text_input = ""

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        st.header("Wizarding World Explorer 🧙‍♂️✨")
        # Using text_input widget for user input
        user_question = st.chat_input("Ask questions and learn about various aspects of harry potter:",key="user_question_input")
        # st.session_state.text_input = user_question
        if user_question:
            with st.expander("Chat History", expanded=True):
                handle_UserInput(user_question)
    except Exception as error:
        print(f"Error: {error}") 
        # Footer
        # st.markdown("<div style='position: static; left: 0; bottom: 0; width: 100%; text-align: center; padding: 10px;'>Made with 🖥️ by <a href='https://www.linkedin.com/in/yash-bharambay-9873b220a/'>Yash Bharambay</a></div>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
