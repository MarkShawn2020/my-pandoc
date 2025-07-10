# Pandoc Enhanced

一个功能强大的 pandoc 增强工具，专为中文用户优化，支持多种输出格式、emoji 渲染、自定义主题等。

## 🎯 核心特性

### 📝 多格式转换
- **PDF**: 使用 XeLaTeX + eisvogel 模板生成专业文档
- **Word**: 完美的 .docx 格式输出
- **HTML**: 响应式网页文档
- **EPUB**: 电子书格式
- **PowerPoint**: 演示文稿格式

### 🎨 中文优化
- 完美的中文字体支持
- 自动 CJK 字体配置
- 多语言支持 (中文/英文/日文)

### 😊 Emoji 支持
- 自动检测文档中的 emoji 字符
- 使用 Noto Emoji 字体完美渲染
- 可选择启用/禁用

### 🎨 主题系统
- 内置 6 种精美主题色
- 自定义封面和样式
- 支持用户自定义主题

### ⚙️ 灵活配置
- 全局配置文件
- 项目级配置
- 命令行参数覆盖

## 🚀 快速开始

### 安装

```bash
# 克隆或下载项目到 ~/.local/bin/pandoc-enhanced
cd ~/.local/bin/pandoc-enhanced

# 运行安装脚本
./install.sh
```

### 基本使用

```bash
# 转换 markdown 到 PDF
pandoc-enhanced document.md

# 转换到其他格式
pandoc-enhanced document.md -f docx    # Word 文档
pandoc-enhanced document.md -f html    # HTML 网页
pandoc-enhanced document.md -f epub    # 电子书
```

## 📖 详细用法

### 基本参数

```bash
pandoc-enhanced <文件> [选项]

基本选项:
  -f, --format <格式>     输出格式 (pdf|docx|html|epub|pptx)
  -o, --output <目录>     输出目录 (默认: ~/Documents)
  -t, --title <标题>      文档标题
  -s, --subtitle <副标题> 文档副标题
  -a, --author <作者>     文档作者
```

### 高级选项

```bash
样式选项:
  --template <模板>       指定模板 (eisvogel|default)
  --theme <主题>         PDF 主题色 (blue|red|green|purple|orange|teal)
  --toc / --no-toc       启用/禁用目录生成
  --emoji / --no-emoji   启用/禁用 emoji 支持
  --lang <语言>          文档语言 (zh-CN|en-US|ja-JP)
```

### 实用示例

```bash
# 生成带蓝色主题的技术文档
pandoc-enhanced tech-guide.md --theme blue -t "技术指南" -a "张三"

# 转换英文文档
pandoc-enhanced readme.md --lang en-US --author "John Doe"

# 生成 Word 文档（不含 emoji）
pandoc-enhanced report.md -f docx --no-emoji

# 调试模式查看详细信息
pandoc-enhanced document.md --debug
```

## ⚙️ 配置管理

### 全局配置

编辑 `~/.config/pandoc-enhanced/config.yaml`:

```yaml
output:
  directory: ~/Documents
  format: pdf

document:
  author: 南川
  subtitle: V0.1
  language: zh-CN

pdf:
  template: eisvogel
  theme: purple
  toc: true
  emoji: true
```

### 项目配置

在项目目录创建 `.pandoc-enhanced.yaml`:

```yaml
document:
  title: 我的项目文档
  author: 项目组
  subtitle: V2.0

pdf:
  theme: blue
  toc: true
```

### 配置命令

```bash
# 查看当前配置
python3 ~/.local/bin/pandoc-enhanced/config_manager.py show

# 创建项目配置
python3 ~/.local/bin/pandoc-enhanced/config_manager.py init .
```

## 🎨 主题预览

| 主题 | 色值 | 效果 |
|------|------|------|
| purple | #5D1EB1 | 优雅紫色（默认）|
| blue | #1E88E5 | 商务蓝色 |
| red | #E53935 | 热情红色 |
| green | #43A047 | 自然绿色 |
| orange | #FB8C00 | 活力橙色 |
| teal | #00ACC1 | 现代青色 |

## 📁 项目结构

```
~/.local/bin/pandoc-enhanced/
├── pandoc-enhanced           # 主程序
├── generate_emoji_header.py  # emoji 处理器
├── config_manager.py         # 配置管理器
├── install.sh               # 安装脚本
└── README.md               # 说明文档
```

## 🔧 依赖项

### 必需依赖
- **Python 3**: 脚本运行环境
- **Pandoc**: 文档转换核心
- **XeLaTeX**: PDF 生成引擎
- **PyYAML**: 配置文件解析

### 字体依赖
- **Songti SC**: 中文宋体
- **Noto Sans CJK SC**: 中文无衬线字体
- **Noto Emoji**: Emoji 字体
- **Noto Sans Mono CJK SC**: 中文等宽字体

### 模板依赖
- **Eisvogel**: LaTeX 模板（自动安装）

## 🆚 vs 原生 Pandoc

| 功能 | 原生 Pandoc | Pandoc Enhanced |
|------|-------------|-----------------|
| 中文支持 | 需要手动配置 | ✅ 开箱即用 |
| Emoji 渲染 | ❌ 不支持 | ✅ 自动检测 |
| 主题系统 | ❌ 无 | ✅ 内置 6 种主题 |
| 配置管理 | ❌ 无 | ✅ 分层配置 |
| 参数简化 | ❌ 复杂 | ✅ 简单易用 |
| 多格式 | ✅ 支持 | ✅ 优化支持 |

## 🛠️ 故障排除

### 常见问题

**Q: 字体缺失错误**
```bash
# 安装中文字体
brew install font-songti-sc
brew install font-noto-sans-cjk-sc
```

**Q: Emoji 不显示**
```bash
# 安装 emoji 字体
brew install font-noto-emoji
```

**Q: 模板未找到**
```bash
# 重新安装模板
mkdir -p ~/.pandoc/templates
curl -o ~/.pandoc/templates/eisvogel.latex \
  https://raw.githubusercontent.com/Wandmalfarbe/pandoc-latex-template/master/eisvogel.tex
```

### 调试模式

使用 `--debug` 参数查看详细信息：

```bash
pandoc-enhanced document.md --debug
```

## 🔄 更新

重新运行安装脚本即可更新：

```bash
cd ~/.local/bin/pandoc-enhanced
./install.sh
```

## 🗑️ 卸载

```bash
# 删除软链接
sudo rm /usr/local/bin/pandoc-enhanced

# 删除项目目录
rm -rf ~/.local/bin/pandoc-enhanced

# 删除配置文件（可选）
rm -rf ~/.config/pandoc-enhanced
```

## 📄 License

MIT License

---

**Pandoc Enhanced** - 让文档转换变得简单优雅 ✨