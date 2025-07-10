#!/bin/bash

# Pandoc Enhanced 安装脚本

set -e

echo "🚀 安装 Pandoc Enhanced..."

# 获取脚本所在目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# 创建软链接到 /usr/local/bin
INSTALL_DIR="/usr/local/bin"
LINK_NAME="pandoc-enhanced"

echo "📦 创建软链接..."

# 检查是否有权限
if [ ! -w "$INSTALL_DIR" ]; then
    echo "⚠️  需要 sudo 权限来创建软链接到 $INSTALL_DIR"
    sudo ln -sf "$SCRIPT_DIR/pandoc-enhanced" "$INSTALL_DIR/$LINK_NAME"
else
    ln -sf "$SCRIPT_DIR/pandoc-enhanced" "$INSTALL_DIR/$LINK_NAME"
fi

echo "🔧 检查依赖..."

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 未找到 python3，请先安装 Python 3"
    exit 1
else
    echo "✅ Python 3 已安装"
fi

# 检查 PyYAML
if ! python3 -c "import yaml" 2>/dev/null; then
    echo "⚠️  未找到 PyYAML，正在安装..."
    pip3 install PyYAML
fi

# 检查 pandoc
if ! command -v pandoc &> /dev/null; then
    echo "⚠️  未找到 pandoc，请安装:"
    echo "   brew install pandoc"
    echo "   或访问: https://pandoc.org/installing.html"
else
    echo "✅ Pandoc 已安装"
fi

# 检查 xelatex
if ! command -v xelatex &> /dev/null; then
    echo "⚠️  未找到 xelatex，请安装 LaTeX:"
    echo "   brew install --cask mactex"
    echo "   或访问: https://www.tug.org/mactex/"
else
    echo "✅ XeLaTeX 已安装"
fi

# 检查 eisvogel 模板
TEMPLATE_FOUND=false
for dir in ~/.pandoc ~/.local/share/pandoc /usr/local/share/pandoc /usr/share/pandoc; do
    if [ -f "$dir/templates/eisvogel.latex" ] || [ -f "$dir/templates/eisvogel.tex" ]; then
        TEMPLATE_FOUND=true
        break
    fi
done

if [ "$TEMPLATE_FOUND" = false ]; then
    echo "⚠️  未找到 eisvogel 模板，正在安装..."
    mkdir -p ~/.pandoc/templates
    curl -s -o ~/.pandoc/templates/eisvogel.latex https://raw.githubusercontent.com/Wandmalfarbe/pandoc-latex-template/master/eisvogel.tex
    if [ $? -eq 0 ]; then
        echo "✅ Eisvogel 模板安装成功"
    else
        echo "❌ Eisvogel 模板安装失败，请手动安装"
    fi
else
    echo "✅ Eisvogel 模板已安装"
fi

# 创建默认配置
echo "⚙️  创建默认配置..."
python3 "$SCRIPT_DIR/config_manager.py" init "$HOME" > /dev/null 2>&1

echo "✅ 安装完成！"
echo ""
echo "📖 使用方法:"
echo "   pandoc-enhanced <file>                    # 基本转换"
echo "   pandoc-enhanced test.md -f docx           # 转换为 Word"
echo "   pandoc-enhanced test.md --theme blue      # 使用蓝色主题"
echo "   pandoc-enhanced test.md --no-emoji        # 禁用 emoji"
echo "   pandoc-enhanced --help                    # 查看完整帮助"
echo ""
echo "🔧 配置管理:"
echo "   pandoc-enhanced --version                 # 查看版本"
echo "   python3 ~/.local/bin/pandoc-enhanced/config_manager.py show"
echo ""
echo "🎉 现在你可以在任何路径直接使用 pandoc-enhanced 命令了！"