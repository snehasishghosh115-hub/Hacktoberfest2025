import sys
from typing import Dict, List


def build_font(char: str = "#") -> Dict[str, List[str]]:
  s = " "  
  C = char  

  def row(pattern: str) -> str:
    return pattern.replace("X", C).replace("_", s)

  return {
    "A": [
      row("_XXX_"),
      row("X___X"),
      row("XXXXX"),
      row("X___X"),
      row("X___X"),
    ],
    "D": [
      row("XXXX_"),
      row("X___X"),
      row("X___X"),
      row("X___X"),
      row("XXXX_"),
    ],
    "H": [
      row("X___X"),
      row("X___X"),
      row("XXXXX"),
      row("X___X"),
      row("X___X"),
    ],
    "I": [
      row("XXXXX"),
      row("__X__"),
      row("__X__"),
      row("__X__"),
      row("XXXXX"),
    ],
    "L": [
      row("X____"),
      row("X____"),
      row("X____"),
      row("X____"),
      row("XXXXX"),
    ],
    "P": [
      row("XXXX_"),
      row("X___X"),
      row("XXXX_"),
      row("X____"),
      row("X____"),
    ],
    "W": [
      row("X___X"),
      row("X___X"),
      row("X_X_X"),
      row("XX_XX"),
      row("X___X"),
    ],
    "Y": [
      row("X___X"),
      row("_X_X_"),
      row("__X__"),
      row("__X__"),
      row("__X__"),
    ],
    " ": [
      row("_____"),
      row("_____"),
      row("_____"),
      row("_____"),
      row("_____"),
    ],
  }


def render_text(text: str, char: str = "#", letter_spacing: int = 1) -> str:
  text = text.upper()
  font = build_font(char)
  missing = sorted({ch for ch in text if ch not in font})
  if missing:
    unsupported = ", ".join(missing)
    raise ValueError(f"Unsupported characters for this font: {unsupported}")

  lines: List[str] = [""] * 5
  gap = " " * letter_spacing
  for ch in text:
    glyph = font[ch]
    lines = [existing + (gap if existing else "") + row for existing, row in zip(lines, glyph)]
  return "\n".join(lines)


def main(argv: List[str]) -> None:
  phrase = "HAPPY DIWALI" if len(argv) == 0 else " ".join(argv)
  print(render_text(phrase, char="#", letter_spacing=1))


if __name__ == "__main__":
  try:
    main(sys.argv[1:])
  except Exception as e:
    print(f"Error: {e}")
