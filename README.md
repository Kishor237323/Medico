Medical RAG Chatbot
This project is a Medical Chatbot using Retrieval-Augmented Generation (RAG) to provide accurate and context-aware responses to medical queries. It processes medical documents, retrieves relevant information, and generates well-structured responses using a LLM-powered pipeline.

Features
✅ Medical Document Ingestion – Loads and processes PDFs
✅ Text Chunking & Embeddings – Uses Sentence-Transformers for efficient vectorization
✅ Vector Storage & Retrieval – Powered by ChromaDB
✅ LLM-based Response Generation – Utilizes Llama for AI-driven medical insights
✅ Real-time Interaction – Users can input queries and receive instant, relevant answers

Tech Stack
LangChain – Manages the pipeline and integrates different components
Llama (LLM) – Generates human-like responses
Sentence-Transformers – Converts text into embeddings
ChromaDB – Stores and retrieves relevant information
Installation
To set up the project, follow these steps:

1. Install Dependencies
bash
Copy
Edit
pip install langchain sentence_transformers chromadb llama-cpp-python langchain_community pypdf
2. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-repo/medical-rag-chatbot.git  
cd medical-rag-chatbot
3. Load Medical Data
Place your medical PDFs in the appropriate directory (e.g., /data).

4. Run the Chatbot
bash
Copy
Edit
python medical_rag_chatbot.py
How It Works
Loads medical documents (e.g., HealthyHeart.pdf)
Chunks and processes text for embedding
Stores embeddings in ChromaDB
Retrieves relevant information based on user queries
Generates AI-powered responses using Llama
Usage
Run the chatbot and enter your medical queries. Type "exit" to stop.

bash
Copy
Edit
Input query: What are the risk factors for heart disease?
Answer: Heart disease risk factors include high blood pressure, smoking, diabetes, obesity, and lack of physical activity.
Future Improvements
🔹 Expand to support multiple medical datasets
🔹 Improve response accuracy with fine-tuned LLM models
🔹 Enhance UI/UX with a web-based or chatbot interface

Contributing
Pull requests are welcome! Feel free to fork the repo and suggest improvements.
