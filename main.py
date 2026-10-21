
from pathlib import Path
from src import reader, statistics, keywords, writer
from src.llm import analyze_paper

BASE_DIR = Path(__file__).resolve().parent
PAPERS_DIR = BASE_DIR / "papers"

report = {}

# 同时读取 TXT 和 PDF 文件
for filename in sorted(PAPERS_DIR.iterdir()):

    if not filename.is_file():
        continue

    suffix = filename.suffix.lower()

    if suffix == ".txt":
        text = reader.read_text(filename)
    elif suffix == ".pdf":
        text = reader.read_pdf(filename)
    else:
        continue

    # AI 论文分析
    result = analyze_paper(text)

    # 原有统计流程
    words = statistics.count_words(text)
    paragraphs = statistics.count_prographs(text)
    filesize = statistics.size_file(filename)

    language_type = keywords.language(text)
    top10 = keywords.get_keywords(language_type, text)

    # 将每篇论文的 AI 分析与统计结果一起保存
    report[filename.stem] = {
        "words": words,
        "paragraphs": paragraphs,
        "filesize": filesize,
        "top10": top10,
        "analysis": result,
    }

    print(f"已处理：{filename.name}")

# 保存全部论文的分析结果
writer.write(report)

print(f"分析完成，共处理 {len(report)} 个文件。")
