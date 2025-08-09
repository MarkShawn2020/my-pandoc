# Pandoc Enhanced

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandoc 2.0+](https://img.shields.io/badge/pandoc-2.0+-green.svg)](https://pandoc.org/)
[![Based on Eisvogel](https://img.shields.io/badge/based%20on-Eisvogel-orange.svg)](https://github.com/Wandmalfarbe/pandoc-latex-template)

`pandoc` 命令的增强包装器，提供中文文档处理的智能预设、专业主题和高级功能，同时保持与所有原生 pandoc 选项的完全兼容性。

[English](README.md) | **中文**

## 什么是 Pandoc Enhanced？

**Pandoc Enhanced** 不是 pandoc 的替代品，而是一个智能包装器：
- **扩展** pandoc，提供针对中文/CJK 文档优化的预配置设置
- **简化** 复杂的 pandoc 命令，提供合理的默认值
- **保持** 与所有原生 pandoc 选项的完全兼容性  
- **基于** 优美的 [Eisvogel LaTeX 模板](https://github.com/Wandmalfarbe/pandoc-latex-template)构建

可以把它看作是自带电池的 `pandoc`，用于专业文档生成。

## 核心特性

- **完全兼容 Pandoc**：可直接传递任何 pandoc 选项 - 未识别的选项会转发给 pandoc
- **CJK 开箱即用**：预配置的中文、日文和韩文字体设置
- **Eisvogel 模板**：使用流行的 Eisvogel LaTeX 模板生成精美的 PDF
- **智能默认值**：为常见文档类型提供合理的预设
- **主题系统**：6 种专业的 PDF 生成颜色主题
- **QR 码集成**：从 URL 生成可自定义样式的 QR 码
- **Emoji 支持**：自动检测和渲染 emoji
- **分层配置**：全局 → 项目 → 命令行参数的优先级

## 安装

```bash
# 克隆仓库
git clone https://github.com/MarkShawn2020/my-pandoc.git
cd my-pandoc

# 安装（创建到 /usr/local/bin 的符号链接）
./install.sh
```

## 使用方法

### 基本用法（增强预设）

```bash
# 使用智能默认值转换（通过 Eisvogel 模板生成 PDF）
pandoc-enhanced document.md

# 使用预配置格式
pandoc-enhanced document.md -f docx    # 支持 CJK 的 Word
pandoc-enhanced document.md -f html    # 正确编码的 HTML
pandoc-enhanced document.md -f epub    # 带元数据的 EPUB

# 应用主题和样式
pandoc-enhanced document.md --theme blue --title "我的文档"
```

### 高级用法（使用原生 Pandoc 选项）

```bash
# 混合使用增强功能和原生 pandoc 选项
pandoc-enhanced document.md \
  --theme blue \                    # 增强：颜色主题
  --qrcode-url "https://example.com" \  # 增强：QR 码
  --number-sections \                # 原生 pandoc 选项
  --toc-depth=3 \                   # 原生 pandoc 选项
  --metadata-file=meta.yaml         # 原生 pandoc 选项

# 所有未识别的选项都会传递给 pandoc
pandoc-enhanced document.md \
  --highlight-style=pygments \      # 传递给 pandoc
  --pdf-engine-opt="-shell-escape"  # 传递给 pandoc
```

## 增强功能

### 预配置模板

该工具使用 **Eisvogel** 作为默认的 LaTeX 模板，提供：
- 专业的排版
- 精美的标题页
- 可自定义的颜色主题
- 完善的 CJK 支持

### 主题系统

| 主题 | 颜色 | 适用场景 |
|------|------|----------|
| `blue` | #1E88E5 | 商务文档 |
| `red` | #E53935 | 演示文稿 |
| `green` | #43A047 | 报告 |
| `purple` | #5D1EB1 | 创意内容 |
| `orange` | #FB8C00 | 营销材料 |
| `teal` | #00ACC1 | 技术文档 |

### QR 码生成

```bash
# 生成透明背景的 QR 码
pandoc-enhanced document.md --qrcode-url "https://github.com"

# 生成与主题匹配背景的 QR 码
pandoc-enhanced document.md --qrcode-url "https://github.com" --qrcode-bg theme

# 自定义颜色的 QR 码
pandoc-enhanced document.md --qrcode-url "URL" --qrcode-bg "#FF0000" --qrcode-fg "#FFFFFF"
```

### 配置系统

全局配置（`~/.config/pandoc-enhanced/config.yaml`）：
```yaml
document:
  author: 你的名字
  language: zh-CN

pdf:
  template: eisvogel
  theme: blue
  toc: true
```

项目配置（`.pandoc-enhanced.yaml`）：
```yaml
document:
  title: 项目文档
  subtitle: v1.0

pdf:
  theme: green
```

## 命令参考

```bash
pandoc-enhanced <输入文件> [选项] [-- pandoc选项]

增强选项：
  -f, --format 格式        输出格式 (pdf|docx|html|epub|pptx)
  -o, --output 目录        输出目录
  -t, --title 标题         文档标题
  -s, --subtitle 副标题    文档副标题
  -a, --author 作者        文档作者
  
  --template 模板          模板名称 (eisvogel|default)
  --theme 颜色             PDF 主题颜色
  --toc/--no-toc          启用/禁用目录
  --emoji/--no-emoji      启用/禁用 emoji 支持
  --lang 语言             文档语言 (zh-CN|en-US|ja-JP)
  
  --qrcode-url URL        从 URL 生成 QR 码
  --qrcode-bg 颜色        QR 码背景 (transparent|theme|#十六进制)
  --qrcode-fg 颜色        QR 码前景色
  
  --debug                 启用调试模式
  -h, --help             显示帮助

所有其他选项都会直接传递给 pandoc。
```

## 与原生 Pandoc 的对比

| 任务 | 原生 Pandoc | Pandoc Enhanced |
|------|-------------|-----------------|
| 基本转换 | `pandoc input.md -o output.pdf` | `pandoc-enhanced input.md` |
| 中文 PDF | `pandoc input.md -o output.pdf --pdf-engine=xelatex -V CJKmainfont="Songti SC" -V mainfont="Songti SC"` | `pandoc-enhanced input.md` |
| Eisvogel 模板 | `pandoc input.md -o output.pdf --template eisvogel --pdf-engine=xelatex` | `pandoc-enhanced input.md` |
| 带主题 | `pandoc input.md -o output.pdf --template eisvogel -V titlepage=true -V titlepage-color="1E88E5"` | `pandoc-enhanced input.md --theme blue` |
| 完整示例 | 100+ 字符的选项 | `pandoc-enhanced input.md --theme blue` |

## 依赖项

### 必需
- **Pandoc** 2.0+ - 通用文档转换器
- **Python** 3.8+ - 用于辅助脚本
- **XeLaTeX** - 用于支持 CJK 的 PDF 生成
- **Eisvogel 模板** - 自动安装

### 可选
- **qrcode[pil]** - 用于 QR 码生成
- **CJK 字体** - Songti SC、Noto Sans CJK SC 等

## 故障排除

### 模板未找到
```bash
# 安装程序应该会处理这个问题，但如果需要：
mkdir -p ~/.pandoc/templates
curl -o ~/.pandoc/templates/eisvogel.latex \
  https://raw.githubusercontent.com/Wandmalfarbe/pandoc-latex-template/master/eisvogel.tex
```

### 调试模式
```bash
# 查看正在执行的实际 pandoc 命令
pandoc-enhanced document.md --debug
```

## 示例

### 生成带 QR 码的技术报告
```bash
pandoc-enhanced report.md \
  --title "技术报告" \
  --subtitle "2024年度总结" \
  --author "张三" \
  --theme blue \
  --qrcode-url "https://company.com/report"
```

### 混合使用原生 pandoc 选项
```bash
pandoc-enhanced paper.md \
  --theme green \                  # 增强功能
  --qrcode-url "https://doi.org" \ # 增强功能
  --number-sections \              # pandoc 选项
  --bibliography=refs.bib \        # pandoc 选项
  --csl=ieee.csl                   # pandoc 选项
```

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 致谢

- [Pandoc](https://pandoc.org/) - 优秀的通用文档转换器
- [Eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template) - 我们所基于的精美 LaTeX 模板
- [Noto Fonts](https://www.google.com/get/noto/) - 全面的字体支持