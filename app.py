
import streamlit as st

from src.reader import read_pdf, read_text
from src.llm import analyze_paper


st.title("PaperMind - AI 论文助手")
st.write("上传论文 PDF 或 TXT 文件，自动提取正文并生成分析报告。")

uploaded_file = st.file_uploader(
    "选择一篇论文",
    type=["pdf", "txt"],
)

if uploaded_file is not None:
    if st.button("分析论文"):
        with st.spinner("正在读取和分析论文..."):
            try:
                # 根据文件类型调用对应的读取函数
                suffix = uploaded_file.name.rsplit(".", 1)[-1].lower()

                if suffix == "pdf":
                    # 将上传文件保存为临时 PDF 文件
                    import tempfile
                    from pathlib import Path

                    with tempfile.NamedTemporaryFile(
                        suffix=".pdf",
                        delete=False,
                    ) as temp_file:
                        temp_file.write(uploaded_file.getvalue())
                        temp_path = Path(temp_file.name)

                    try:
                        text = read_pdf(temp_path)
                    finally:
                        temp_path.unlink(missing_ok=True)

                elif suffix == "txt":
                    # 将上传的 TXT 内容解码后交给现有读取函数
                    import tempfile

                    with tempfile.NamedTemporaryFile(
                        mode="wb",
                        suffix=".txt",
                        delete=False,
                    ) as temp_file:
                        temp_file.write(uploaded_file.getvalue())
                        temp_path = Path(temp_file.name)

                    try:
                        text = read_text(temp_path)
                    finally:
                        temp_path.unlink(missing_ok=True)

                else:
                    st.error("不支持的文件格式。")
                    st.stop()

                # 检查是否成功提取正文
                if not text.strip():
                    st.warning("未提取到文字，PDF 可能需要 OCR 处理。")
                else:
                    # 调用大模型分析论文
                    result = analyze_paper(text)

                    st.success("文件读取完成！")
                    st.subheader("论文分析结果")
                    st.markdown(result)

            except Exception as e:
                st.error(f"处理失败：{e}")
