
├── docs/                    # 存放知识文档
│   ├── manual.pdf
│   └── policies.txt
├── models/                  # 句向量模型
│   ├── all-MiniLM-L6-v2/    #  Sentence-Transformers的句向量模型 本地模型 无需再下载
├── vector_store/            # FAISS 向量库（自动生成）
├── ingest.py                # 文档处理脚本
└── rag.py                   # RAG 主程序
└── README.md

# 项目说明
用本地的deepseek r1+本地知识库实现QA问答个性化

# 项目依赖说明 
python3.9
ollama

# 安装依赖
## 下载deepseek-R1 模型 LLM 模型
ollama download deepseek-R1:1.5B
## 下载向量模型 sentence-transformers/all-MiniLM-L6-v2
pip install sentence-transformers
python download_model.py
## 创建虚拟环境（推荐）
python -m venv rag-env
source rag-env/bin/activate

## 安装依赖包
pip install -r requirements.txt

# 构建知识库
准备文档
将文档（如 PDF、TXT）放入 docs/ 目录。

文档加载与分割
执行 ingest.py：
python ingest.py

# 提问运行demo
python rag.py

# 重新进入已创建的虚拟空间
## 进入虚拟空间
source rag-env/bin/activate
## 安装依赖包
pip install -r requirements.txt
