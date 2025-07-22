from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_ollama import OllamaLLM
from flask import Flask, request, jsonify

# 加载向量库
embeddings = HuggingFaceEmbeddings(model_name="./models/all-MiniLM-L6-v2_local")
vector_store = FAISS.load_local(
    "vector_store", 
    embeddings,
    allow_dangerous_deserialization=True
    )

# 初始化本地 LLM（需先安装 Ollama）
llm = OllamaLLM(model="deepseek-R1:1.5B")  # 或 "mistral"、"gemma" 用ollma list看本地都有啥模型

# 构建 RAG 链
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=True
)

# 循环运行到提问环节
while True:
    print("请输入问题（输入 'exit' 退出）：")
    query = input()
    if query.lower() == 'exit':
        break
    response = qa_chain.invoke({"query": query})
    print("答案：", response["result"])
    print("来源：", response['source_documents'][0].metadata['source'])