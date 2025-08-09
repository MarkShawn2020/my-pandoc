#!/usr/bin/env python3
"""
QR Code generator for pandoc-enhanced
Generates QR code from URL and saves as image
"""

import os
import sys
import hashlib
from pathlib import Path

try:
    import qrcode
    from PIL import Image
except ImportError:
    print("❌ 需要安装 qrcode 和 pillow 库")
    print("   请运行: pip install qrcode[pil]")
    sys.exit(1)

def generate_qrcode(url, output_dir, size=200):
    """
    生成 QR 码图片
    
    Args:
        url: 要编码的 URL
        output_dir: 输出目录
        size: QR 码尺寸（像素）
    
    Returns:
        生成的 QR 码文件路径
    """
    # 使用 URL 的 hash 作为文件名
    url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
    output_file = Path(output_dir) / f"qrcode_{url_hash}.png"
    
    # 创建输出目录
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # 生成 QR 码
    qr = qrcode.QRCode(
        version=1,  # QR 码版本（1-40）
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    # 创建图片
    img = qr.make_image(fill_color="black", back_color="white")
    
    # 调整大小
    img = img.resize((size, size), Image.Resampling.LANCZOS)
    
    # 保存图片
    img.save(str(output_file))
    
    return str(output_file)

def main():
    if len(sys.argv) < 3:
        print("用法: generate_qrcode.py <url> <output_dir> [size]")
        sys.exit(1)
    
    url = sys.argv[1]
    output_dir = sys.argv[2]
    size = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    
    print(f"🔗 生成 QR 码: {url}")
    
    try:
        qrcode_path = generate_qrcode(url, output_dir, size)
        print(f"✅ QR 码已保存: {qrcode_path}")
        # 输出路径供脚本读取
        print(f"QRCODE_PATH:{qrcode_path}")
    except Exception as e:
        print(f"❌ 生成 QR 码失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()