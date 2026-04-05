"""PDF 读取脚本 - 读取 PDF 文件内容并输出文本"""

import sys
import argparse

try:
    import fitz  # PyMuPDF
except ImportError:
    print("缺少 PyMuPDF 库，请运行: pip install PyMuPDF")
    sys.exit(1)


def read_pdf(file_path, start_page=None, end_page=None):
    """读取 PDF 文件并返回文本内容"""
    doc = fitz.open(file_path)
    total_pages = doc.page_count
    print(f"文件: {file_path}")
    print(f"总页数: {total_pages}")
    print("=" * 60)

    start = (start_page - 1) if start_page else 0
    end = end_page if end_page else total_pages

    if start < 0 or end > total_pages or start >= end:
        print(f"页码范围无效，有效范围: 1-{total_pages}")
        doc.close()
        return

    for i in range(start, end):
        page = doc[i]
        text = page.get_text()
        print(f"\n--- 第 {i + 1} 页 ---\n")
        print(text)

    doc.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="读取 PDF 文件内容")
    parser.add_argument("file", help="PDF 文件路径")
    parser.add_argument("-s", "--start", type=int, default=None, help="起始页码（从1开始）")
    parser.add_argument("-e", "--end", type=int, default=None, help="结束页码")
    args = parser.parse_args()

    read_pdf(args.file, args.start, args.end)
