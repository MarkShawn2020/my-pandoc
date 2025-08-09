# Pandoc Enhanced

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandoc 2.0+](https://img.shields.io/badge/pandoc-2.0+-green.svg)](https://pandoc.org/)

Professional document converter with native Chinese support, enhanced themes, and advanced features.

**English** | [中文](README-zh.md)

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

## Contributing

Issues and Pull Requests are welcome!

## Author

- **MarkShawn2020** - [GitHub](https://github.com/MarkShawn2020)

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Pandoc](https://pandoc.org/) - Universal document converter
- [Eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template) - Beautiful LaTeX template
- [Noto Fonts](https://www.google.com/get/noto/) - Beautiful and free fonts for all languages