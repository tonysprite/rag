from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# 加载文档 - 选择一种加载器，这里以 txt 文档为例
loader = DirectoryLoader("docs/", glob="*.txt", loader_cls=TextLoader)
# loader = DirectoryLoader("docs/", glob="*.pdf", loader_cls=PyPDFLoader)
documents = loader.load()

# 分割文本
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(documents)

# 加载嵌入模型
embeddings = HuggingFaceEmbeddings(model_name="./models/all-MiniLM-L6-v2_local")

# 生成向量库
vector_store = FAISS.from_documents(chunks, embeddings)
vector_store.save_local("vector_store")  # 保存到本地

print(f"成功处理 {len(chunks)} 个文档块，向量库已保存到 'vector_store' 目录")