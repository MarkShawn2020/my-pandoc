# Pandoc Enhanced

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandoc 2.0+](https://img.shields.io/badge/pandoc-2.0+-green.svg)](https://pandoc.org/)

Professional document converter with native Chinese support, enhanced themes, and advanced features.

[中文](#中文) | [English](#english)

## Features

- **Multi-format Export**: PDF, Word, HTML, EPUB, PowerPoint with optimized templates
- **Native CJK Support**: Built-in Chinese/Japanese/Korean fonts configuration
- **Smart Emoji Rendering**: Automatic emoji detection and rendering with Noto Emoji
- **Professional Themes**: 6 built-in color themes for PDF generation
- **QR Code Integration**: Generate QR codes from URLs with customizable styling
- **Flexible Configuration**: Cascading configuration system (global → project → CLI)

## Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/MarkShawn2020/my-pandoc.git
cd my-pandoc

# Install
./install.sh
```

### Basic Usage

```bash
# Convert to PDF (default)
pandoc-enhanced document.md

# Convert to other formats
pandoc-enhanced document.md -f docx    # Word
pandoc-enhanced document.md -f html    # HTML
pandoc-enhanced document.md -f epub    # EPUB

# With custom styling
pandoc-enhanced document.md --theme blue --title "My Document"

# With QR code
pandoc-enhanced document.md --qrcode-url "https://example.com"
```

## Advanced Features

### QR Code Generation

```bash
# QR code with transparent background (default)
pandoc-enhanced document.md --qrcode-url "https://github.com"

# QR code with theme color background
pandoc-enhanced document.md --qrcode-url "https://github.com" --qrcode-bg theme

# Custom QR code colors
pandoc-enhanced document.md --qrcode-url "URL" --qrcode-bg "#FF0000" --qrcode-fg "#FFFFFF"
```

### Theme System

| Theme | Color | Use Case |
|-------|-------|----------|
| `blue` | #1E88E5 | Business documents |
| `red` | #E53935 | Presentations |
| `green` | #43A047 | Reports |
| `purple` | #5D1EB1 | Creative content |
| `orange` | #FB8C00 | Marketing materials |
| `teal` | #00ACC1 | Technical documentation |

### Configuration

Create `~/.config/pandoc-enhanced/config.yaml` for global settings:

```yaml
document:
  author: Your Name
  language: zh-CN

pdf:
  template: eisvogel
  theme: blue
  toc: true
```

Project-specific configuration in `.pandoc-enhanced.yaml`:

```yaml
document:
  title: Project Documentation
  subtitle: v1.0

pdf:
  theme: green
```

## Command Reference

```bash
pandoc-enhanced <input> [options]

Options:
  -f, --format FORMAT      Output format (pdf|docx|html|epub|pptx)
  -o, --output DIR         Output directory
  -t, --title TITLE        Document title
  -s, --subtitle SUBTITLE  Document subtitle
  -a, --author AUTHOR      Document author
  
  --template NAME          Template (eisvogel|default)
  --theme COLOR            Theme color
  --toc/--no-toc          Enable/disable table of contents
  --emoji/--no-emoji      Enable/disable emoji support
  --lang LANG             Document language (zh-CN|en-US|ja-JP)
  
  --qrcode-url URL        Generate QR code from URL
  --qrcode-bg COLOR       QR code background (transparent|theme|#hex)
  --qrcode-fg COLOR       QR code foreground color
  
  --debug                 Enable debug mode
  -h, --help             Show help
```

## Dependencies

### Required
- Python 3.8+
- Pandoc 2.0+
- XeLaTeX (for PDF generation)
- qrcode[pil] (for QR code generation)

### Fonts
- Songti SC (Chinese)
- Noto Sans CJK SC
- Noto Emoji
- Noto Sans Mono CJK SC

Install on macOS:
```bash
brew install --cask mactex
brew install font-songti-sc font-noto-sans-cjk-sc font-noto-emoji
```

Install on Ubuntu/Debian:
```bash
sudo apt-get install texlive-full fonts-noto-cjk fonts-noto-color-emoji
```

## Troubleshooting

### Missing Fonts
```bash
# macOS
brew install font-songti-sc font-noto-sans-cjk-sc

# Linux
sudo apt-get install fonts-noto-cjk
```

### Template Not Found
```bash
# Download eisvogel template
mkdir -p ~/.pandoc/templates
curl -o ~/.pandoc/templates/eisvogel.latex \
  https://raw.githubusercontent.com/Wandmalfarbe/pandoc-latex-template/master/eisvogel.tex
```

### Debug Mode
```bash
pandoc-enhanced document.md --debug
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 中文

专业的文档转换工具，原生支持中文、增强主题和高级功能。

### 核心特性

- **多格式导出**：PDF、Word、HTML、EPUB、PowerPoint，使用优化模板
- **原生中文支持**：内置中日韩字体配置，开箱即用
- **智能 Emoji 渲染**：自动检测并使用 Noto Emoji 渲染
- **专业主题系统**：6 种内置 PDF 主题色
- **QR 码集成**：从 URL 生成 QR 码，支持自定义样式
- **灵活配置系统**：分层配置（全局 → 项目 → 命令行）

### 快速开始

#### 安装

```bash
# 克隆仓库
git clone https://github.com/MarkShawn2020/my-pandoc.git
cd my-pandoc

# 安装
./install.sh
```

#### 基本使用

```bash
# 转换为 PDF（默认）
pandoc-enhanced 文档.md

# 转换为其他格式
pandoc-enhanced 文档.md -f docx    # Word
pandoc-enhanced 文档.md -f html    # HTML
pandoc-enhanced 文档.md -f epub    # 电子书

# 自定义样式
pandoc-enhanced 文档.md --theme blue --title "我的文档"

# 带 QR 码
pandoc-enhanced 文档.md --qrcode-url "https://example.com"
```

### 高级功能

#### QR 码生成

```bash
# 透明背景 QR 码（默认）
pandoc-enhanced 文档.md --qrcode-url "https://github.com"

# 主题色背景 QR 码
pandoc-enhanced 文档.md --qrcode-url "https://github.com" --qrcode-bg theme

# 自定义颜色 QR 码
pandoc-enhanced 文档.md --qrcode-url "URL" --qrcode-bg "#FF0000" --qrcode-fg "#FFFFFF"
```

#### 主题系统

| 主题 | 颜色 | 适用场景 |
|------|------|----------|
| `blue` | #1E88E5 | 商务文档 |
| `red` | #E53935 | 演示文稿 |
| `green` | #43A047 | 报告文档 |
| `purple` | #5D1EB1 | 创意内容 |
| `orange` | #FB8C00 | 营销材料 |
| `teal` | #00ACC1 | 技术文档 |

### 许可证

MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。