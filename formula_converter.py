import matplotlib.pyplot as plt
import os


def formula_to_png(formula_latex: str, filename: str, font_family: str = "Computer Modern", fontsize: int = 24, color: str = "black"):
    """
    Converts a LaTeX mathematical formula into a PNG image with a transparent background.

    Args:
        formula_latex (str): The LaTeX string of the formula (e.g., r'$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$').
                             Remember to use raw strings (r'...') for LaTeX to handle backslashes correctly.
        filename (str): The desired output filename for the PNG image.
        font_family (str): The font family to use for the formula.
                           Common options for "maths looking" fonts include "Computer Modern" (default),
                           "Latin Modern", or "Palatino". This will influence the LaTeX preamble.
        fontsize (int): The font size for the rendered formula.
    """
    try:
        # Set up LaTeX font configuration based on the requested font_family
        # Store original rcParams to restore them later
        original_rcParams = plt.rcParams.copy()

        if font_family == "Computer Modern":
            plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath, amsfonts, amssymb, cmbright}'
            plt.rcParams['font.family'] = 'serif'
            plt.rcParams['font.serif'] = ['Computer Modern Roman']
        elif font_family == "Latin Modern":
            plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath, amsfonts, amssymb, lmodern}'
            plt.rcParams['font.family'] = 'serif'
            plt.rcParams['font.serif'] = ['Latin Modern Roman']
        elif font_family == "Palatino":
            plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath, amsfonts, amssymb, mathpazo}'
            plt.rcParams['font.family'] = 'serif'
            plt.rcParams['font.serif'] = ['Palatino']
        else:
            # Fallback for other fonts or if no specific LaTeX package is known
            plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath, amsfonts, amssymb}'
            plt.rcParams['font.family'] = 'serif'
            plt.rcParams['font.serif'] = [font_family]

        # Create a figure and axes
        # Adjust figsize dynamically based on formula length for better fit
        # This is a heuristic; more complex formulas might need manual adjustment
        fig_width = max(8, len(formula_latex) * 0.2)
        fig, ax = plt.subplots(figsize=(fig_width, 1.5))

        # Hide the axes (we only want the formula, not a plot)
        ax.axis('off')

        # Add the LaTeX formula as text with the specified color
        ax.text(0.5, 0.5, formula_latex, fontsize=fontsize, ha='center', va='center', usetex=True, color=color)

        # Save the figure with a transparent background
        plt.savefig(filename, bbox_inches='tight', transparent=True, dpi=300)
        plt.close(fig) # Close the figure to free up memory

        # Restore original rcParams to avoid affecting subsequent plots
        plt.rcParams.update(original_rcParams)

        print(f"Formula successfully saved as {filename} with {font_family} font.")

    except Exception as e:
        print(f"An error occurred while processing {filename}: {e}")
        print("Please ensure you have a LaTeX distribution installed if running locally,")
        print("or check the LaTeX syntax of your formula and the availability of the specified font package.")
        # Restore rcParams even on error
        plt.rcParams.update(original_rcParams)

