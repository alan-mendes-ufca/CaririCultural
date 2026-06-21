import re
import os

wiki_home = '/home/alan/Documentos/Cariri-Cultural/g6.wiki/home'
matrix_path = os.path.join(wiki_home, 'traceability-matrix.md')

with open(matrix_path, 'r') as f:
    content = f.read()

# Replace links like [ID](user-storys#ID) with [ID](home/user-storys#ID)
content = re.sub(r'\]\((business-rules|functional-requirements|user-storys|non-functional-requirements)(#?[^)]*)\)', r'](home/\1\2)', content)

# Also fix the interview links: [interviews/interview-xxx](interviews/interview-xxx) -> [interviews/interview-xxx](home/interviews/interview-xxx)
content = re.sub(r'\]\(interviews/([^#)]+)\)', r'](home/interviews/\1)', content)

# And bpmn/
content = re.sub(r'\]\(bpmn/?\)', r'](home/bpmn)', content)

with open(matrix_path, 'w') as f:
    f.write(content)

print("Added home/ prefix to links")
