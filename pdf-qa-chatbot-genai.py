import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from openai import OpenAI
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# upload files
st.header("Chatbot project")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload your documents here", type="pdf")

# extract text
if file is not None:
    pdf_reader = PdfReader(file)
    text=""
    for page in pdf_reader.pages:
        text += page.extract_text()
        #st.write(text)
# break into chunks

    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len

    )
    chunks = text_splitter.split_text(text)
    #st.write(chunks)
    #generating embeddings

    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    #creatiing vector storage

    vector_store = FAISS.from_texts(chunks, embeddings)

    #get user questions
    user_question = st.text_input("Type Your question here")


    if user_question:
        # 1) similarity search to get relevant chunks
        match = vector_store.similarity_search(user_question, k=4)
        context = "\n\n".join(doc.page_content for doc in match)

        # 2) build prompt
        prompt = f"""
    You are a helpful assistant that answers questions based only on the document context.

    Context:
    {context}

    Question: {user_question}

    If the answer is not in the context, say you don't know based on this document.

    Answer:
    """

        # 3) call OpenAI directly
        client = OpenAI(api_key=OPENAI_API_KEY)

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # or "gpt-4o"
            messages=[
                {"role": "system", "content": "You are a helpful PDF QA assistant."},
                {"role": "user", "content": prompt},
            ],
        )

        answer = response.choices[0].message.content
        st.write(answer)


