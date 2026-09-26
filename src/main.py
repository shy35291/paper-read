from pathlib import Path
import reader
import statistics
import keywords
import writer

path=Path('../papers')
report={}
for filename in path.glob('*.txt'):
    text=reader.readtext(filename)
    words=statistics.count_words(text)              #单词数

    prographs=statistics.count_prographs(text)      # 段落数

    filesize=statistics.size_file(filename)         # 计算文件大小,以字节为单位

    language_type=keywords.language(text)           #判断文献语言类型

    top10=keywords.get_keywords(language_type,text) #获取关键词
    # 保存结果
    report[filename.stem]={"words":words,
                           "prographs":prographs,
                           "filesize":filesize,
                           "top10":top10}
writer.write(report)

