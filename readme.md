# 项目说明
用本地的deepseek r1+本地知识库实现基于行业领域专业认知的QA问答

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
## 进入虚拟空间
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
