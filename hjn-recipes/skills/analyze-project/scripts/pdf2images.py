"""PDF 转图片 - 使用 PyMuPDF 将 PDF 每页转为 JPEG 图片"""

import sys
import os
import argparse

try:
    import fitz  # PyMuPDF
except ImportError:
    print("缺少 PyMuPDF 库，请运行: pip install PyMuPDF")
    sys.exit(1)


def pdf_to_images(pdf_path, output_dir=None, dpi=150, start=None, end=None):
    if not os.path.isfile(pdf_path):
        print(f"错误: 文件不存在 - {pdf_path}")
        sys.exit(1)

    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(pdf_path))

    doc = fitz.open(pdf_path)
    total = doc.page_count
    start_idx = (start - 1) if start else 0
    end_idx = end if end else total

    if start_idx < 0 or end_idx > total or start_idx >= end_idx:
        print(f"页码范围无效，有效范围: 1-{total}")
        doc.close()
        sys.exit(1)

    zoom = dpi / 72
    matrix = fitz.Matrix(zoom, zoom)
    output_files = []

    for i in range(start_idx, end_idx):
        page = doc[i]
        pix = page.get_pixmap(matrix=matrix)
        output_path = os.path.join(output_dir, f"page_{i + 1}.jpg")
        pix.save(output_path)
        output_files.append(output_path)
        print(output_path)

    doc.close()
    print(f"\n共转换 {len(output_files)} 页，保存到: {output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF 转图片")
    parser.add_argument("file", help="PDF 文件路径")
    parser.add_argument("-o", "--output", default=None, help="输出目录")
    parser.add_argument("-d", "--dpi", type=int, default=150, help="分辨率（默认150）")
    parser.add_argument("-s", "--start", type=int, default=None, help="起始页码（从1开始）")
    parser.add_argument("-e", "--end", type=int, default=None, help="结束页码")
    args = parser.parse_args()

    pdf_to_images(args.file, args.output, args.dpi, args.start, args.end)
