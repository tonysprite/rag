from huggingface_hub import snapshot_download

# 指定模型名称
model_name = "sentence-transformers/all-MiniLM-L6-v2"
# 指定下载到哪个本地目录
local_dir = "./models/all-MiniLM-L6-v2_local"

# 下载模型的所有文件到指定目录
snapshot_download(repo_id=model_name, local_dir=local_dir)

print(f"模型已下载到：{local_dir}")