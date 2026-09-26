import re
import jieba
from collections import Counter
# 判断是中文文献还是英文文献
def language(text):

    chinese = 0
    english = 0

    for ch in text:

        if '\u4e00' <= ch <= '\u9fff':
            chinese += 1

        elif ch.isalpha():
            english += 1

    if chinese > english:
        return "zh"

    return "en"

# 获取文章中出现最频繁的10个关键词
def get_keywords(language_type,text):
    if language_type == "zh":
        tokens = jieba.lcut(text)
        tokens = [
            word.strip()for word in tokens if len(word.strip()) > 1]
        counter = Counter(tokens)
        return [word for word, count in counter.most_common(10)]
    else :
        tokens = re.findall(r"[A-Za-z]+", text.lower())
        counter=Counter(tokens)                   #返回字典
        return [word for word,count in counter.most_common(10)]
