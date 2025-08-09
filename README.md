# Pandoc Enhanced

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandoc 2.0+](https://img.shields.io/badge/pandoc-2.0+-green.svg)](https://pandoc.org/)
[![Based on Eisvogel](https://img.shields.io/badge/based%20on-Eisvogel-orange.svg)](https://github.com/Wandmalfarbe/pandoc-latex-template)

An enhanced wrapper for the `pandoc` command, providing intelligent presets for Chinese document processing, professional themes, and advanced features while maintaining full compatibility with all native pandoc options.

**English** | [中文](README-zh.md)

## What is Pandoc Enhanced?

**Pandoc Enhanced** is not a replacement for pandoc, but rather an intelligent wrapper that:
- **Extends** pandoc with pre-configured settings optimized for Chinese/CJK documents
- **Simplifies** complex pandoc commands with sensible defaults
- **Preserves** full compatibility with all native pandoc options
- **Built on** the beautiful [Eisvogel LaTeX template](https://github.com/Wandmalfarbe/pandoc-latex-template)

Think of it as `pandoc` with batteries included for professional document generation.

## Key Features

- **Full Pandoc Compatibility**: Pass any pandoc option directly - unrecognized options are forwarded to pandoc
- **CJK-Ready**: Pre-configured Chinese, Japanese, and Korean font settings
- **Eisvogel Template**: Beautiful PDF output using the popular Eisvogel LaTeX template
- **Smart Defaults**: Sensible presets for common document types
- **Theme System**: 6 professional color themes for PDF generation
- **QR Code Integration**: Generate QR codes from URLs with customizable styling
- **Emoji Support**: Automatic emoji detection and rendering
- **Cascading Configuration**: Global → Project → CLI parameter precedence

## Installation

```bash
# Clone repository
git clone https://github.com/MarkShawn2020/my-pandoc.git
cd my-pandoc

# Install (creates symlink to /usr/local/bin)
./install.sh
```

## Usage

### Basic Usage (Enhanced Presets)

```bash
# Convert with smart defaults (PDF via Eisvogel template)
pandoc-enhanced document.md

# Use pre-configured formats
pandoc-enhanced document.md -f docx    # Word with CJK support
pandoc-enhanced document.md -f html    # HTML with proper encoding
pandoc-enhanced document.md -f epub    # EPUB with metadata

# Apply themes and styling
pandoc-enhanced document.md --theme blue --title "My Document"
```

### Advanced Usage (With Native Pandoc Options)

```bash
# Mix enhanced features with native pandoc options
pandoc-enhanced document.md \
  --theme blue \                    # Enhanced: color theme
  --qrcode-url "https://example.com" \  # Enhanced: QR code
  --number-sections \                # Native pandoc option
  --toc-depth=3 \                   # Native pandoc option
  --metadata-file=meta.yaml         # Native pandoc option

# All unrecognized options are passed to pandoc
pandoc-enhanced document.md \
  --highlight-style=pygments \      # Passed to pandoc
  --pdf-engine-opt="-shell-escape"  # Passed to pandoc
```

## Enhanced Features

### Pre-configured Templates

The tool uses **Eisvogel** as the default LaTeX template, providing:
- Professional typography
- Beautiful title pages
- Customizable color themes
- Proper CJK support

### Theme System

| Theme | Color | Use Case |
|-------|-------|----------|
| `blue` | #1E88E5 | Business documents |
| `red` | #E53935 | Presentations |
| `green` | #43A047 | Reports |
| `purple` | #5D1EB1 | Creative content |
| `orange` | #FB8C00 | Marketing materials |
| `teal` | #00ACC1 | Technical documentation |

### QR Code Generation

```bash
# Generate QR code with transparent background
pandoc-enhanced document.md --qrcode-url "https://github.com"

# QR code with theme-matched background
pandoc-enhanced document.md --qrcode-url "https://github.com" --qrcode-bg theme

# Custom colored QR code
pandoc-enhanced document.md --qrcode-url "URL" --qrcode-bg "#FF0000" --qrcode-fg "#FFFFFF"
```

### Configuration System

Global configuration (`~/.config/pandoc-enhanced/config.yaml`):
```yaml
document:
  author: Your Name
  language: zh-CN

pdf:
  template: eisvogel
  theme: blue
  toc: true
```

Project configuration (`.pandoc-enhanced.yaml`):
```yaml
document:
  title: Project Documentation
  subtitle: v1.0

pdf:
  theme: green
```

## Command Reference

```bash
pandoc-enhanced <input> [options] [-- pandoc-options]

Enhanced Options:
  -f, --format FORMAT      Output format (pdf|docx|html|epub|pptx)
  -o, --output DIR         Output directory
  -t, --title TITLE        Document title
  -s, --subtitle SUBTITLE  Document subtitle
  -a, --author AUTHOR      Document author
  
  --template NAME          Template (eisvogel|default)
  --theme COLOR            Theme color for PDF
  --toc/--no-toc          Enable/disable table of contents
  --emoji/--no-emoji      Enable/disable emoji support
  --lang LANG             Document language (zh-CN|en-US|ja-JP)
  
  --qrcode-url URL        Generate QR code from URL
  --qrcode-bg COLOR       QR code background (transparent|theme|#hex)
  --qrcode-fg COLOR       QR code foreground color
  
  --debug                 Enable debug mode
  -h, --help             Show help

All other options are passed directly to pandoc.
```

## Comparison with Native Pandoc

| Task | Native Pandoc | Pandoc Enhanced |
|------|---------------|-----------------|
| Basic conversion | `pandoc input.md -o output.pdf` | `pandoc-enhanced input.md` |
| Chinese PDF | `pandoc input.md -o output.pdf --pdf-engine=xelatex -V CJKmainfont="Songti SC" -V mainfont="Songti SC"` | `pandoc-enhanced input.md` |
| Eisvogel template | `pandoc input.md -o output.pdf --template eisvogel --pdf-engine=xelatex` | `pandoc-enhanced input.md` |
| With theme | `pandoc input.md -o output.pdf --template eisvogel -V titlepage=true -V titlepage-color="1E88E5"` | `pandoc-enhanced input.md --theme blue` |
| Full example | 100+ characters of options | `pandoc-enhanced input.md --theme blue` |

## Dependencies

### Required
- **Pandoc** 2.0+ - The universal document converter
- **Python** 3.8+ - For helper scripts
- **XeLaTeX** - For PDF generation with CJK support
- **Eisvogel Template** - Automatically installed

### Optional
- **qrcode[pil]** - For QR code generation
- **CJK Fonts** - Songti SC, Noto Sans CJK SC, etc.

## Troubleshooting

### Template Not Found
```bash
# The installer should handle this, but if needed:
mkdir -p ~/.pandoc/templates
curl -o ~/.pandoc/templates/eisvogel.latex \
  https://raw.githubusercontent.com/Wandmalfarbe/pandoc-latex-template/master/eisvogel.tex
```

### Debug Mode
```bash
# See the actual pandoc command being executed
pandoc-enhanced document.md --debug
```

## Contributing

Issues and Pull Requests are welcome!

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Pandoc](https://pandoc.org/) - The amazing universal document converter
- [Eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template) - The beautiful LaTeX template we build upon
- [Noto Fonts](https://www.google.com/get/noto/) - Comprehensive font support