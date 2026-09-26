# 统计字数
def count_words(text):
    return len(text.replace(" ","").replace('\n',''))

# 统计段落
def count_prographs(text):
    return text.count('\n\n')+1

# 文件大小
def size_file(filename):
    return filename.stat().st_size
