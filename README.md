# Pandoc Enhanced

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandoc 2.0+](https://img.shields.io/badge/pandoc-2.0+-green.svg)](https://pandoc.org/)
[![Based on Eisvogel](https://img.shields.io/badge/based%20on-Eisvogel-orange.svg)](https://github.com/Wandmalfarbe/pandoc-latex-template)

一个轻量级的 `pandoc` 包装器，在保持与原生 pandoc 100% 兼容的同时添加增强功能。

[English](README.md) | **中文**

## 什么是 Pandoc Enhanced？

**Pandoc Enhanced** 是一个透明的包装器，它：
- **添加了** QR 码生成、主题系统、Emoji 支持和 CJK 优化
- **保持了** 与原生 pandoc 100% 的兼容性 - 所有 pandoc 选项都按预期工作
- **应用了** 使用 Eisvogel LaTeX 模板的智能默认设置，生成精美的 PDF
- **简化了** 中文/CJK 文档处理，预配置了字体

## 核心特性

### 增强功能（我们的添加）
- 🎨 **主题系统**：6 种专业的 PDF 标题页颜色主题
- 🔗 **QR 码生成**：为 PDF 添加可自定义颜色的 QR 码
- 😀 **Emoji 支持**：自动配置 Emoji 字体
- 🀄 **CJK 优化**：预配置的中文、日文和韩文字体
- 📄 **Eisvogel 模板**：默认生成精美的 PDF 输出
- 🐛 **调试模式**：查看实际执行的 pandoc 命令

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
pandoc-enhanced document.md -o output.pdf --theme blue --qrcode-url "https://github.com"
```

### 仅增强功能

我们的包装器在 pandoc 之上添加了这些选项：

```bash
--theme COLOR           # PDF 主题颜色 (blue|red|green|purple|orange|teal|#hex)
--qrcode-url URL       # 生成 QR 码并添加到 PDF
--qrcode-bg COLOR      # QR 码背景 (transparent|theme|#hex)
--qrcode-fg COLOR      # QR 码前景色
--emoji/--no-emoji     # 启用/禁用 emoji 支持（默认：启用）
--cjk-fonts            # 应用 CJK 字体（默认：PDF 启用）
--eisvogel             # 使用 Eisvogel 模板（默认：PDF 启用）
--debug                # 显示实际运行的 pandoc 命令
```

### 示例

```bash
# 简单的 PDF，自动应用我们的增强功能（Eisvogel + CJK 字体）
pandoc-enhanced document.md -o output.pdf

# 添加主题和 QR 码
pandoc-enhanced document.md -o output.pdf --theme blue --qrcode-url "https://example.com"

# 结合原生 pandoc 选项
pandoc-enhanced document.md -o output.pdf \
  --theme green \                    # 我们的增强
  --qrcode-url "https://github.com" \ # 我们的增强
  --toc \                            # 原生 pandoc
  --number-sections \                # 原生 pandoc
  -M author="张三" \                  # 原生 pandoc
  --bibliography=refs.bib           # 原生 pandoc

# 调试模式查看发生了什么
pandoc-enhanced document.md -o output.pdf --debug
```

## 实际示例

```bash
# 转换带 QR 码和主题的 markdown 文档
./pandoc-enhanced './examples/GPT-5 发布会（英文完整版）.md' \
  -o './examples/GPT-5 发布会（英文完整版）.pdf' \
  --theme blue \
  --qrcode-url https://mp.weixin.qq.com/s/M6rDJ-onGrIJdYepgUu79A \
  --qrcode-bg theme \
  --toc
```

## 主题颜色

| 主题 | 用途 | 十六进制 |
|------|------|----------|
| `blue` | 商务 | #1E88E5 |
| `red` | 演示 | #E53935 |
| `green` | 报告 | #43A047 |
| `purple` | 创意 | #5D1EB1 |
| `orange` | 营销 | #FB8C00 |
| `teal` | 技术 | #00ACC1 |

## 工作原理

1. **解析参数**：将我们的增强选项与原生 pandoc 选项分离
2. **应用增强**：如果输出 PDF，自动：
   - 使用 Eisvogel 模板生成精美输出
   - 为中文/日文/韩文文本配置 CJK 字体
   - 如果需要，生成 QR 码
   - 应用主题颜色
3. **传递给 Pandoc**：所有参数（原生 + 我们的添加）都传递给 pandoc
4. **完全兼容**：Pandoc 正常处理其他所有内容

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