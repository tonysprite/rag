
├── docs/                    # 存放知识文档
│   ├── manual.pdf
│   └── policies.txt
├── models/                  # 句向量模型
│   ├── all-MiniLM-L6-v2/    #  Sentence-Transformers的句向量模型 本地模型 无需再下载
├── vector_store/            # FAISS 向量库（自动生成）
├── ingest.py                # 文档处理脚本
└── rag.py                   # RAG 主程序
└── README.md