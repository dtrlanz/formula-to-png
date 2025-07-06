# generate_formulas.py
import os
from formula_converter import formula_to_png
from math_formulas import math_formulas
from biology_formulas import biology_formulas

def generate_all_formula_pngs():
    """
    Generates PNG images for all defined mathematical and biological formulas.
    Images are saved in a 'png' directory.
    """
    output_dir = "png"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    print("\n--- Generating Math Formulas ---")
    for name, latex_formula in math_formulas.items():
        filename = os.path.join(output_dir, f"{name}.png")
        formula_to_png(latex_formula, filename, font_family="Latin Modern", fontsize=20)

    print("\n--- Generating Biology Formulas ---")
    for name, latex_formula in biology_formulas.items():
        filename = os.path.join(output_dir, f"{name}.png")
        formula_to_png(latex_formula, filename, font_family="Latin Modern", fontsize=18)

    print("\nAll formula PNGs generated successfully!")

if __name__ == "__main__":
    generate_all_formula_pngs()