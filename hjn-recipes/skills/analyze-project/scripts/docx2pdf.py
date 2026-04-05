"""
docx 转 pdf 工具

用法: python docx2pdf.py <docx文件路径> [输出pdf路径]
不指定输出路径则在同目录下生成同名 .pdf

需要安装: pip install pywin32
"""

import os
import sys
import win32com.client


def convert(docx_path, pdf_path=None):
    docx_path = os.path.abspath(docx_path)
    if not os.path.isfile(docx_path):
        print(f"错误: 文件不存在 - {docx_path}")
        sys.exit(1)

    if pdf_path is None:
        pdf_path = os.path.splitext(docx_path)[0] + ".pdf"
    pdf_path = os.path.abspath(pdf_path)

    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    try:
        doc = word.Documents.Open(docx_path, False, True)
        doc.SaveAs(pdf_path, FileFormat=17)
        doc.Close(SaveChanges=0)
    finally:
        word.Quit()

    print(pdf_path)
    return pdf_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python docx2pdf.py <docx文件> [输出pdf路径]")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
