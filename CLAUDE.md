# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**pandoc-enhanced** is a Bash wrapper around Pandoc that adds native Chinese/CJK support, theming, QR code generation, business card embedding, and the Eisvogel LaTeX template for professional PDF generation.

## Common Commands

```bash
# Install (creates symlink to /usr/local/bin/pandoc-enhanced)
npm install
# or
./install.sh

# Test
npm test

# Uninstall
npm uninstall
# or
sudo rm /usr/local/bin/pandoc-enhanced

# Basic usage
./pandoc-enhanced input.md -o output.pdf

# With enhancements
./pandoc-enhanced input.md -o output.pdf \
  --theme blue \
  --qrcode-url "https://github.com/user" \
  --card-image data/card.jpg \
  --toc

# Debug mode (shows full pandoc command and keeps temp files)
./pandoc-enhanced input.md --debug
```

## Architecture

### Main Entry Point: `pandoc-enhanced`

The 381-line Bash script orchestrates the entire conversion pipeline:

1. **Argument Parsing**: Separates enhanced features from native pandoc options
   - Enhanced: `--theme`, `--qrcode-url`, `--card-image`, `--emoji`, `--cjk-fonts`, `--eisvogel`, `--debug`
   - Pass-through: `--toc`, `-o`, `-f`, `-t`, etc.

2. **Output Detection**: Checks if output is PDF (by extension or `-t pdf`)

3. **Metadata Extraction**: Parses YAML front matter for title/author/date
   - Special handling: `source` field → displayed as `author`
   - Date moved to author position when card image is present

4. **PDF Enhancement Pipeline** (only for PDF output):
   - Apply Eisvogel template (`--template eisvogel`)
   - Set PDF engine to XeLaTeX (`--pdf-engine=xelatex`)
   - Apply CJK fonts: Songti SC (main), PingFang SC (sans), Menlo (mono)
   - Apply theme color to titlepage (default: `#CC785C`)
   - Generate QR code if `--qrcode-url` provided
   - Generate business card footer if `--card-image` provided
   - Generate emoji header if `--emoji` enabled (disabled by default)

5. **Execution**: `exec pandoc` with all combined arguments

### Python Helper Scripts

All helpers output their result path to stdout in format `NAME_PATH:path/to/file` for the Bash script to capture.

#### `generate_qrcode.py` (135 lines)
- **Input**: URL, output directory, size, background color, foreground color
- **Output**: PNG file with hash-based naming (`qrcode_<hash>.png`)
- **Features**: Transparent background support, custom hex colors, error correction level L
- **Dependencies**: `qrcode`, `Pillow`

#### `generate_card_header.py` (44 lines)
- **Input**: Card image path, output file path
- **Output**: LaTeX header using `eso-pic` package
- **Positioning**: Absolute positioning with 2.5cm left margin, width = `\paperwidth - 5cm`
- **Purpose**: Adds business card image to titlepage footer, aligned with title content

#### `generate_emoji_header.py` (60 lines)
- **Input**: Markdown file, output header file
- **Output**: LaTeX header with `\newunicodechar` mappings for Apple Color Emoji font
- **Status**: **Disabled by default** due to LaTeX compilation issues
- **Regex**: Matches 9 Unicode emoji ranges (U+1F600-U+1F64F, etc.)

#### `config_manager.py` (137 lines)
- **Purpose**: Manage global (`~/.config/pandoc-enhanced/config.yaml`) and project-level (`.pandoc-enhanced.yaml`) configuration
- **Status**: Initialized but not fully integrated into main script
- **Default theme**: Purple

### Eisvogel Template Integration

Git submodule from `enhuiz/eisvogel`. The wrapper configures it via pandoc metadata:

- `titlepage=true`: Enable custom titlepage
- `titlepage-color`: Background color (RGB hex without `#`)
- `titlepage-rule-height`: Divider line height (default: 2)
- `titlepage-rule-color`: Divider color (default: `FFFFFF`)
- `titlepage-text-color`: Text color (default: `FFFFFF`)
- `titlepage-logo`: Path to logo/QR code image
- `logo-width`: Logo width (for QR code: `6cm`)
- `graphics=true`: Enable graphics support

**Important**: Eisvogel uses 2.5cm margins on all sides, which is why business card positioning uses `\hspace{2.5cm}` and `width=\paperwidth-5cm`.

## Development Workflows

### Adding a New Theme Color

1. Edit `get_theme_color()` function in `pandoc-enhanced`
2. Add case statement: `colorname) echo "HEXCODE" ;;`
3. Update help text in `show_enhanced_help()`

### Modifying Titlepage Layout

The titlepage is controlled by Eisvogel template variables. To change:

1. Edit default metadata in `pandoc-enhanced` around line 228-232
2. Common variables: `titlepage-rule-height`, `titlepage-rule-color`, `titlepage-text-color`, `titlepage-color`
3. For business card positioning, edit `generate_card_header.py` LaTeX code

### Testing Changes

```bash
# Use debug mode to see the actual pandoc command
./pandoc-enhanced test.md --debug

# Check temporary files (they're preserved in debug mode)
ls -la /var/folders/.../tmp.*/

# Test specific feature
./pandoc-enhanced examples/GPT-5\ 发布会（中文完整版，2万字）.md \
  --theme blue \
  --qrcode-url "https://github.com" \
  --debug
```

## Key Technical Details

### YAML Front Matter Processing

The script extracts metadata using `sed`:
```bash
sed -n '/^---$/,/^---$/p' "$INPUT_FILE" | grep -E '^source:'
```

This allows mapping custom fields (like `source`) to standard pandoc fields (like `author`).

### Argument Flow

```
User Input → pandoc-enhanced → Parse → Detect PDF
                                      ↓
                            Generate QR/Card/Emoji
                                      ↓
                            Build pandoc args array
                                      ↓
                            exec pandoc [all_args]
```

**Critical**: Arguments must maintain order:
1. Input files
2. Output file (`-o`)
3. Metadata (`-M`)
4. Variables (`-V`)
5. Headers (`-H`)
6. Format options (`-f`, `-t`)

### Temporary File Cleanup

- Cleanup happens via `trap cleanup EXIT`
- In debug mode, temp directory is preserved and path is printed
- Temp files: QR codes, LaTeX headers, emoji mappings

### TOC Handling

The script normalizes `--toc` and `--no-toc` to `--toc=true` and `--toc=false` for consistency, as pandoc accepts both forms.

## Important Constraints

1. **Emoji disabled by default**: Set `EMOJI=false` due to LaTeX compilation issues with certain emoji ranges
2. **XeLaTeX required**: Must use XeLaTeX (not pdflatex) for CJK font support
3. **Eisvogel titlepage**: Custom titlepage layout is controlled by template, not easily customizable without modifying template
4. **Business card alignment**: Uses absolute positioning because Eisvogel doesn't provide a footer slot in titlepage
5. **CJK fonts hardcoded**: Currently uses macOS system fonts (Songti SC, PingFang SC, Menlo)

## File Locations

- Main script: `./pandoc-enhanced`
- Eisvogel template: `./eisvogel/eisvogel.tex` (submodule)
- Python helpers: Root directory (`generate_*.py`)
- User config: `~/.config/pandoc-enhanced/config.yaml`
- Project config: `./.pandoc-enhanced.yaml`
- Installed template: `~/.pandoc/templates/eisvogel.latex`
- Symlink: `/usr/local/bin/pandoc-enhanced`

## Dependencies

**Required**:
- Bash 3.2+
- Pandoc 2.0+
- XeLaTeX (TeX Live)
- Python 3.8+
- PyYAML
- qrcode (Python package)
- Pillow (Python package)

**Optional**:
- Git (for submodule management)
