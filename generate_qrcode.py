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

def hex_to_rgb(hex_color):
    """
    将十六进制颜色转换为 RGB 元组
    
    Args:
        hex_color: 十六进制颜色字符串（如 "FFFFFF" 或 "#FFFFFF"）
    
    Returns:
        RGB 元组 (r, g, b)
    """
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def generate_qrcode(url, output_dir, size=200, bg_color=None, fg_color="000000"):
    """
    生成 QR 码图片
    
    Args:
        url: 要编码的 URL
        output_dir: 输出目录
        size: QR 码尺寸（像素）
        bg_color: 背景色（None 或 "transparent" 表示透明，十六进制字符串表示颜色）
        fg_color: 前景色（十六进制字符串）
    
    Returns:
        生成的 QR 码文件路径
    """
    # 使用 URL 的 hash 作为文件名
    url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
    output_file = Path(output_dir) / f"qrcode_{url_hash}.png"
    
    # 创建输出目录
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # 生成 QR 码（无边框）
    qr = qrcode.QRCode(
        version=1,  # QR 码版本（1-40）
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=0,  # 无边框
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    # 处理颜色
    if bg_color and bg_color.lower() != "transparent":
        # 使用指定的背景色
        bg_rgb = hex_to_rgb(bg_color)
        fg_rgb = hex_to_rgb(fg_color)
        img = qr.make_image(fill_color=fg_rgb, back_color=bg_rgb)
        # 转换为 RGBA 以保持一致性
        img = img.convert("RGBA")
    else:
        # 透明背景模式 - 黑色前景，白色背景，然后将白色转为透明
        img = qr.make_image(fill_color="black", back_color="white")
        # 转换为 RGBA 模式
        img = img.convert("RGBA")
        
        # 创建新的图像数据，将白色背景替换为透明
        pixdata = img.load()
        width, height = img.size
        for y in range(height):
            for x in range(width):
                # 获取当前像素
                r, g, b, a = pixdata[x, y]
                # 如果是白色（背景），设置为透明
                if r > 200 and g > 200 and b > 200:
                    pixdata[x, y] = (255, 255, 255, 0)
                # 否则保持原色（黑色前景）
                else:
                    # 可以选择使用自定义前景色
                    if fg_color != "000000":
                        fg_rgb = hex_to_rgb(fg_color)
                        pixdata[x, y] = (fg_rgb[0], fg_rgb[1], fg_rgb[2], 255)
    
    # 调整大小
    img = img.resize((size, size), Image.Resampling.LANCZOS)
    
    # 保存图片
    img.save(str(output_file), "PNG")
    
    return str(output_file)

def main():
    if len(sys.argv) < 3:
        print("用法: generate_qrcode.py <url> <output_dir> [size] [bg_color] [fg_color]")
        print("  bg_color: 背景色，'transparent' 或十六进制颜色（如 'B55F3F'）")
        print("  fg_color: 前景色，十六进制颜色（默认 '000000'）")
        sys.exit(1)
    
    url = sys.argv[1]
    output_dir = sys.argv[2]
    size = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    bg_color = sys.argv[4] if len(sys.argv) > 4 else None
    fg_color = sys.argv[5] if len(sys.argv) > 5 else "000000"
    
    # 处理背景色参数
    if bg_color and bg_color.lower() == "transparent":
        bg_color = None
        print(f"🔗 生成透明背景 QR 码: {url}")
    elif bg_color:
        print(f"🔗 生成 QR 码: {url} (背景色: #{bg_color})")
    else:
        print(f"🔗 生成 QR 码: {url}")
    
    try:
        qrcode_path = generate_qrcode(url, output_dir, size, bg_color, fg_color)
        print(f"✅ QR 码已保存: {qrcode_path}")
        # 输出路径供脚本读取
        print(f"QRCODE_PATH:{qrcode_path}")
    except Exception as e:
        print(f"❌ 生成 QR 码失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()