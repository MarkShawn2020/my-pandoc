#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
import os

def generate_emoji_header(markdown_file, output_file):
    """读取markdown文件，提取所有emoji，生成LaTeX头文件"""
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配所有emoji字符的正则表达式
    emoji_pattern = re.compile(
        r'[\U0001F600-\U0001F64F]|'  # 情绪符号
        r'[\U0001F300-\U0001F5FF]|'  # 杂项符号
        r'[\U0001F680-\U0001F6FF]|'  # 交通符号
        r'[\U0001F700-\U0001F77F]|'  # 几何符号
        r'[\U0001F780-\U0001F7FF]|'  # 几何符号扩展
        r'[\U0001F800-\U0001F8FF]|'  # 补充箭头
        r'[\U00002600-\U000026FF]|'   # 杂项符号
        r'[\U00002700-\U000027BF]|'   # 装饰符号
        r'[\U0001F900-\U0001F9FF]|'  # 补充符号
        r'[\U0001FA00-\U0001FA6F]|'  # 扩展符号
        r'[\U0001FA70-\U0001FAFF]'   # 符号和象形文字扩展
    )
    
    # 找到所有emoji
    emojis = set(emoji_pattern.findall(content))
    
    # 生成LaTeX头文件
    latex_header = r'''\usepackage{fontspec}
\usepackage{newunicodechar}
\newfontfamily\emojifont{Noto Emoji}

% 自动生成的 emoji 字符映射
'''
    
    for emoji in sorted(emojis):
        latex_header += f'\\newunicodechar{{{emoji}}}{{{{\\emojifont {emoji}}}}}\n'
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(latex_header)
    
    return len(emojis)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 generate_emoji_header.py <markdown_file> <output_file>")
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not os.path.exists(markdown_file):
        print(f"Error: File {markdown_file} not found")
        sys.exit(1)
    
    emoji_count = generate_emoji_header(markdown_file, output_file)
    print(f"已生成 {output_file}，包含 {emoji_count} 个 emoji 字符映射")