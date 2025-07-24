from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_ollama import OllamaLLM
from flask import Flask, request, jsonify
from roles import ROLE_LIST

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


# 创建 Flask 应用
app = Flask(__name__)
@app.route('/roles', methods=['GET'])
def get_roles():
    return jsonify({"roles": ROLE_LIST})


@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({"error": "Missing 'query' field in request"}), 400

    user_query = data['query']
    context = data.get('context', '')
    role = data.get('role', '')  # 获取 role 参数，若不存在则为空字符串

    # 拼接 query 内容
    if role:
        prefixed_query = f"你是一个专业的{role}，请根据以下已知信息回答用户问题。已知信息：{context}。问题：{user_query}。请用简洁、专业的语言作答："
    else:
        prefixed_query = user_query

    # 打印一下拼接后的 query
    print(f"Prefixed query: {prefixed_query}")
    response = qa_chain.invoke({"query": prefixed_query})
    
    return jsonify({
        "answer": response["result"],
        "source": response['source_documents'][0].metadata['source']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)