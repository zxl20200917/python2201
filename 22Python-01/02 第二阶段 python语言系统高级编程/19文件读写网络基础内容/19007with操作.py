"""
    with操作
"""

with open('file','r') as f:
    # data = f.read()
    for line in f:
        print(line)
