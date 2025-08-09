# Pandoc Enhanced

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandoc 2.0+](https://img.shields.io/badge/pandoc-2.0+-green.svg)](https://pandoc.org/)

专业的文档转换工具，原生支持中文、增强主题和高级功能。

[English](README.md) | **中文**

## 核心特性

- **多格式导出**：PDF、Word、HTML、EPUB、PowerPoint，使用优化模板
- **原生中文支持**：内置中日韩字体配置，开箱即用
- **智能 Emoji 渲染**：自动检测并使用 Noto Emoji 渲染
- **专业主题系统**：6 种内置 PDF 主题色
- **QR 码集成**：从 URL 生成 QR 码，支持自定义样式
- **灵活配置系统**：分层配置（全局 → 项目 → 命令行）

## 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/MarkShawn2020/my-pandoc.git
cd my-pandoc

# 安装
./install.sh
```

### 基本使用

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

## 高级功能

### QR 码生成

```bash
# 透明背景 QR 码（默认）
pandoc-enhanced 文档.md --qrcode-url "https://github.com"

# 主题色背景 QR 码
pandoc-enhanced 文档.md --qrcode-url "https://github.com" --qrcode-bg theme

# 自定义颜色 QR 码
pandoc-enhanced 文档.md --qrcode-url "URL" --qrcode-bg "#FF0000" --qrcode-fg "#FFFFFF"
```

QR 码背景色选项：
- `transparent` - 透明背景（默认）
- `theme` - 使用文档主题色
- `#十六进制` - 自定义颜色

### 主题系统

| 主题 | 颜色 | 适用场景 |
|------|------|----------|
| `blue` | #1E88E5 | 商务文档 |
| `red` | #E53935 | 演示文稿 |
| `green` | #43A047 | 报告文档 |
| `purple` | #5D1EB1 | 创意内容 |
| `orange` | #FB8C00 | 营销材料 |
| `teal` | #00ACC1 | 技术文档 |

### 配置管理

创建全局配置文件 `~/.config/pandoc-enhanced/config.yaml`：

```yaml
document:
  author: 你的名字
  language: zh-CN

pdf:
  template: eisvogel
  theme: blue
  toc: true
```

项目配置文件 `.pandoc-enhanced.yaml`：

```yaml
document:
  title: 项目文档
  subtitle: v1.0

pdf:
  theme: green
```

## 命令参考

```bash
pandoc-enhanced <输入文件> [选项]

选项:
  -f, --format 格式        输出格式 (pdf|docx|html|epub|pptx)
  -o, --output 目录        输出目录
  -t, --title 标题         文档标题
  -s, --subtitle 副标题    文档副标题
  -a, --author 作者        文档作者
  
  --template 模板          模板名称 (eisvogel|default)
  --theme 颜色             主题颜色
  --toc/--no-toc          启用/禁用目录
  --emoji/--no-emoji      启用/禁用 emoji 支持
  --lang 语言             文档语言 (zh-CN|en-US|ja-JP)
  
  --qrcode-url URL        生成 QR 码
  --qrcode-bg 颜色        QR 码背景色 (transparent|theme|#十六进制)
  --qrcode-fg 颜色        QR 码前景色
  
  --debug                 调试模式
  -h, --help             显示帮助
```

## 依赖项

### 必需依赖
- Python 3.8+
- Pandoc 2.0+
- XeLaTeX（PDF 生成）
- qrcode[pil]（QR 码生成）

### 字体依赖
- Songti SC（宋体）
- Noto Sans CJK SC
- Noto Emoji
- Noto Sans Mono CJK SC

macOS 安装：
```bash
brew install --cask mactex
brew install font-songti-sc font-noto-sans-cjk-sc font-noto-emoji
pip install qrcode[pil]
```

Ubuntu/Debian 安装：
```bash
sudo apt-get install texlive-full fonts-noto-cjk fonts-noto-color-emoji
pip install qrcode[pil]
```

## 故障排除

### 字体缺失
```bash
# macOS
brew install font-songti-sc font-noto-sans-cjk-sc

# Linux
sudo apt-get install fonts-noto-cjk
```

### 模板未找到
```bash
# 下载 eisvogel 模板
mkdir -p ~/.pandoc/templates
curl -o ~/.pandoc/templates/eisvogel.latex \
  https://raw.githubusercontent.com/Wandmalfarbe/pandoc-latex-template/master/eisvogel.tex
```

### QR 码库缺失
```bash
pip install qrcode[pil]
```

### 调试模式
```bash
pandoc-enhanced 文档.md --debug
```

## 示例

### 生成技术报告
```bash
pandoc-enhanced report.md \
  --title "技术报告" \
  --subtitle "2024年度总结" \
  --author "张三" \
  --theme blue \
  --qrcode-url "https://company.com/report"
```

### 生成带目录的学术论文
```bash
pandoc-enhanced paper.md \
  --title "研究论文" \
  --author "李四" \
  --template eisvogel \
  --toc \
  --theme green
```

### 批量转换
```bash
for file in *.md; do
  pandoc-enhanced "$file" -o ./output --theme blue
done
```

## 许可证

MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 贡献

欢迎提交 Issue 和 Pull Request！

## 作者

- **MarkShawn2020** - [GitHub](https://github.com/MarkShawn2020)

## 致谢

- [Pandoc](https://pandoc.org/) - 强大的文档转换工具
- [Eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template) - 优秀的 LaTeX 模板
- [Noto Fonts](https://www.google.com/get/noto/) - 开源字体家族