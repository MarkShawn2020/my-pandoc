# Pandoc Enhanced

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandoc 2.0+](https://img.shields.io/badge/pandoc-2.0+-green.svg)](https://pandoc.org/)
[![Based on Eisvogel](https://img.shields.io/badge/based%20on-Eisvogel-orange.svg)](https://github.com/Wandmalfarbe/pandoc-latex-template)

一个轻量级的 `pandoc` 包装器，在保持与原生 pandoc 100% 兼容的同时添加增强功能。

[English](README.md) | **中文**

## 什么是 Pandoc Enhanced？

**Pandoc Enhanced** 是一个透明的包装器，它：
- **保持了** 与原生 pandoc 100% 的兼容性 - 所有 pandoc 选项都按预期工作
- **应用了** 使用 Eisvogel LaTeX 模板的智能默认设置，生成精美的 PDF
- **简化了** 中文/CJK 文档处理，预配置了字体
- **添加了** QR 码生成、Emoji 支持和 CJK 优化

### 原生 Pandoc 功能（直接传递）
所有 pandoc 选项都按照[官方 pandoc 手册](https://pandoc.org/MANUAL.html)中的说明工作：
- `-o`, `--output`：指定输出文件
- `-t`, `--to`：指定输出格式
- `-f`, `--from`：指定输入格式
- `--toc`：生成目录
- `--number-sections`：章节编号
- `-M`, `--metadata`：设置元数据
- 以及数百个其他选项...

## 安装

```bash
# 克隆仓库
git clone https://github.com/MarkShawn2020/my-pandoc.git
cd my-pandoc

# 安装（创建到 /usr/local/bin 的符号链接）
./install.sh
```

## 使用方法

### 基本使用

```bash
# 标准 pandoc 命令按预期工作
pandoc-enhanced document.md -o output.pdf

# 支持所有原生 pandoc 选项
pandoc-enhanced document.md -o output.pdf --toc --number-sections

# 添加我们的增强功能
pandoc-enhanced document.md -o output.pdf --qrcode-url "https://github.com"
```



## 实际示例

```bash
# 转换带 QR 码的 markdown 文档
./pandoc-enhanced './examples/GPT-5 发布会（英文完整版）.md' \
  -o './examples/GPT-5 发布会（英文完整版）.pdf' \
  --qrcode-url https://mp.weixin.qq.com/s/M6rDJ-onGrIJdYepgUu79A \
  --qrcode-bg transparent \
  --toc
```

## 依赖项

### 必需
- **Pandoc** 2.0+ - 通用文档转换器
- **Python** 3.8+ - 用于 QR 码生成和 Emoji 支持
- **XeLaTeX** - 用于支持 CJK 的 PDF 生成

### 可选
- **qrcode[pil]** - 用于 QR 码生成
- **Eisvogel 模板** - 由我们的安装程序自动安装
- **CJK 字体** - Songti SC、Noto Sans CJK SC 等

## 故障排除

### 查看发生了什么
```bash
# 使用调试模式查看实际的 pandoc 命令
pandoc-enhanced document.md -o output.pdf --debug
```

### 模板未找到
```bash
# 安装程序应该会处理这个问题，但如果需要：
mkdir -p ~/.pandoc/templates
curl -o ~/.pandoc/templates/eisvogel.latex \
  https://raw.githubusercontent.com/Wandmalfarbe/pandoc-latex-template/master/eisvogel.tex
```

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 致谢

- [Pandoc](https://pandoc.org/) - 我们包装的优秀通用文档转换器
- [Eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template) - 精美的 LaTeX 模板
- [Noto Fonts](https://www.google.com/get/noto/) - 全面的字体支持