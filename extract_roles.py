import os

# 目标文件夹
DOCS_DIR = './docs'

roles = []
for filename in os.listdir(DOCS_DIR):
    if filename.endswith('.txt'):
        file_path = os.path.join(DOCS_DIR, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            if first_line.startswith('role:'):
                role = first_line[len('role:'):].strip()
                roles.append(role)

# 写入 roles.py
with open('./roles.py', 'w', encoding='utf-8') as f:
    f.write('# 自动生成的角色列表\n')
    f.write('ROLE_LIST = ' + repr(roles) + '\n')
