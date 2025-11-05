#!/usr/bin/env python3
"""
Generate LaTeX header for business card on titlepage footer
"""
import sys
import os

def generate_card_header(card_image_path, output_file):
    """Generate LaTeX header to add business card to titlepage footer"""

    # Get absolute path
    card_image_path = os.path.abspath(card_image_path)

    if not os.path.exists(card_image_path):
        print(f"Error: Card image not found: {card_image_path}", file=sys.stderr)
        sys.exit(1)

    latex_code = r"""\usepackage{eso-pic}
\usepackage{graphicx}
\usepackage{calc}

% Add business card to titlepage footer
% Match title text block width: \textwidth (not the 1.3\textwidth rule)
% Position from left=6cm to align with title content
\AddToShipoutPictureBG*{%
  \AtPageLowerLeft{%
    \raisebox{3cm}{%
      \hspace{6cm}%
      \includegraphics[width=\textwidth]{""" + card_image_path.replace('\\', '/') + r"""}%
    }%
  }%
}
"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(latex_code)

    print(f"CARD_HEADER_PATH:{output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: generate_card_header.py <card_image_path> <output_file>", file=sys.stderr)
        sys.exit(1)

    generate_card_header(sys.argv[1], sys.argv[2])
