import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


def analyze_paper(text):
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("BASE_URL")

    if not api_key:
        raise RuntimeError("NEED OPENAI_API_KEY")

    client = OpenAI(
        api_key=api_key,
        base_url=base_url or None,
    )

    paper_text = text[:12000]

    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {
                "role": "system",
                "content": (
                    "你是一个专业的学术论文阅读助手。"
                    "你的任务是根据用户提供的论文内容，进行结构化分析，并输出清晰、专业的中文报告。"
                    "请务必提取核心论点、研究方法、主要发现和局限性。"
                ),
            },
            {
                "role": "user",
                "content": (
                    f"请仔细阅读以下论文内容，并按要求进行分析：\n"
                    "1. 提取论文的核心观点与主要结论。\n"
                    "2. 总结论文使用的研究方法与数据来源。\n"
                    "3. 分析论文的主要创新点与局限性。\n"
                    "4. 给出你的综合评价与启发。\n\n"
                    f"论文内容如下：\n{paper_text}"
                ),
            },
        ],
    )

    return response.choices[0].message.content
