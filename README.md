# PaperMind

一个用于读取论文、统计文本信息并使用兼容 OpenAI Chat Completions API 的模型生成分析报告的 Python 工具。支持 PDF 和 TXT 文件。

## 功能

- 从 PDF 或 TXT 文件中提取文本
- 统计字数、段落数和文件大小，并提取高频关键词
- 使用大语言模型总结论文观点、方法、发现、创新点和局限性
- 提供命令行批量处理和 Streamlit 网页上传两种使用方式

## 环境准备

需要已安装 Python。建议在项目根目录创建虚拟环境：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

项目需要 API 凭据才能生成 AI 分析。在项目根目录创建 `.env` 文件，填写：

```dotenv
OPENAI_API_KEY=你的_API_密钥
BASE_URL=你的_API_兼容服务地址
```

如果使用 OpenAI 官方 API，可以省略 `BASE_URL`。当前模型名称在 `src/llm.py` 中设置为 `deepseek-flash`；使用其他服务或模型时，请确认服务支持该模型名称，并按需修改 `src/llm.py` 中的配置。请勿将真实密钥提交到版本控制。

## 使用方式

### 网页界面

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

按终端提示打开本地网页，上传 PDF 或 TXT 文件，然后点击“分析论文”。

### 批量命令行

将 PDF 或 TXT 文件放入 `papers/`，然后运行：

```powershell
.\.venv\Scripts\python.exe main.py
```

程序会逐个分析 `papers/` 中的 PDF 和 TXT 文件，并将统计数据及 AI 分析写入 `output/report.json`。每篇论文都会单独调用模型 API。

## 注意事项

- 扫描版 PDF 若没有可提取的文字，需要先进行 OCR；项目本身不执行 OCR。
- AI 分析依赖网络、有效的 API 密钥、正确的服务地址和可用的模型名称。
- 新生成且尚未跟踪的 `output/` 文件默认由 Git 忽略；已经纳入版本控制的文件仍会继续跟踪。

## 项目结构

```text
.
├── app.py              # Streamlit 网页入口
├── main.py             # 批量命令行入口
├── papers/             # 批量分析输入文件（PDF/TXT）
├── output/             # 批量分析输出
├── src/
│   ├── keywords.py     # 关键词提取
│   ├── llm.py          # 大模型调用
│   ├── reader.py       # PDF/TXT 读取
│   ├── statistics.py   # 文本统计
│   └── writer.py       # JSON 输出
└── requirements.txt    # Python 依赖
```
