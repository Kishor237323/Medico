# -*- coding: utf-8 -*-
"""Medical RAG chatbot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fyB209UGgIAdZ1KM32ckB787O0XhzeM7
"""

from google.colab import drive
drive.mount('/content/drive')

!pip install langchain sentence_transformers chromadb llama-cpp-python langchain_community pypdf

from langchain_community.document_loaders import PyPDFDirectoryLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter

RecursiveCharacterTextSplitter

from langchain_community.embeddings import sentence_transformer

sentence_transformer

from langchain.vectorstores import Chroma

Chroma

from langchain.llms import LlamaCpp

LlamaCpp

from langchain.chains import RetrievalQA,LLMChain

RetrievalQA,LLMChain

#import the document
loader=PyPDFDirectoryLoader("/content/drive/MyDrive/Biomistral/data")
docs=loader.load()

len(docs)

docs[6]

#chunking
text_splitter=RecursiveCharacterTextSplitter(chunk_size=300,chunk_overlap=50)
chunks=text_splitter.split_documents(docs)

len(chunks)

chunks[550]

#Embeddings Creations
import os
os.environ['HUGGINGFACEHUB_API_TOKEN']="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"

embeddings=sentence_transformer.SentenceTransformerEmbeddings(model_name="NeuML/pubmedbert-base-embeddings")
embeddings

#vector store creation
vectorstore=Chroma.from_documents(chunks,embeddings)

query="who is at risk of heart disease ?"
search_results=vectorstore.similarity_search(query)

search_results

retriever=vectorstore.as_retriever(search_kwargs={"k":5})

retriever.get_relevant_documents(query)

"""LLM Model Loading"""

llm=LlamaCpp(
    model_path="/content/drive/MyDrive/Biomistral/BioMistral-7B.Q4_K_M.gguf",
    temperature=0.2,
    max_tokens=2048,
    top_p=1

)

template="""
<|context|>
You are an Medical Assistant that follows the instructions and generate the accurate response based on the query and the context provided.
Please be truthful and give direct answers.
</s>
</user/>
{query}
</s>
<lassistant/>
"""

from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate

prompt=ChatPromptTemplate.from_template(template)

rag_chain = (
    {"context": retriever, "query": RunnablePassthrough()}
    | prompt
    |llm
    | StrOutputParser()
)

response=rag_chain.invoke(query)

response

import sys
while True:
    user_input = input(f"Input query: ")
    if user_input == 'exit':
        print("Exiting...")
        sys.exit()
    if user_input=="":
        continue
    result = rag_chain.invoke(user_input)
    print("Answer: ", result)

