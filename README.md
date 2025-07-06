# Formula PNG Generator

This project provides a Python script to generate high-quality PNG images of various mathematical and biological formulas using LaTeX rendering via `matplotlib`. Each formula is saved as a transparent PNG, allowing for easy integration into presentations, documents, or web pages.

## Features

* Outputs images with a transparent background.
* Customizable font family, font size, and text color for the formulas.
* Generates PNG images for a collection of well-known mathematical and biological formulas.

## Setup and Dependencies

To run this project locally, you need Python and a few libraries, along with a LaTeX distribution for rendering.

1.  **Python:** Ensure you have Python 3.x installed.

2.  **Virtual Environment (Recommended):**
    It's recommended to use a virtual environment to manage project dependencies.

    * Navigate to your project directory in your terminal.

    * Create a virtual environment:

        ```
        python -m venv venv
        ```

    * Activate the virtual environment:

        * **Windows (Command Prompt):**

            ```
            venv\Scripts\activate
            ```

        * **Windows (PowerShell):**

            ```
            .\venv\Scripts\Activate.ps1
            ```

        * **macOS/Linux:**

            ```
            source venv/bin/activate
            ```

    Your terminal prompt should now show `(venv)` indicating the environment is active.

3.  **Install Python Libraries:**
    With your virtual environment activated, install `matplotlib`:

    ```
    pip install matplotlib
    ```

4.  **LaTeX Distribution:**
    `matplotlib` uses a LaTeX backend to render the mathematical formulas. You need a LaTeX distribution installed on your system.

    * **Windows:** [MiKTeX](https://miktex.org/download) or [TeX Live](https://www.tug.org/texlive/acquire-netinstall.html)

    * **macOS:** [MacTeX](https://www.tug.org/mactex/) (includes TeX Live)

    * **Linux:** [TeX Live](https://www.tug.org/texlive/acquire-netinstall.html) (often available via package managers, e.g., `sudo apt-get install texlive-full` on Debian/Ubuntu)

    After installing LaTeX, it's a good idea to restart your terminal or IDE (like VS Code) to ensure the system's `PATH` variable is updated correctly. You can verify the installation by running `pdflatex --version` in your terminal.

## How to Run

After setting up the dependencies:

1.  **Activate your virtual environment** (if you haven't already).

2.  **Navigate to your project's root directory** in the terminal.

3.  **Run the main script:**

    ```
    python generate_formulas.py
    ```

The script will create a directory named `png` in your project root (if it doesn't exist) and save all the generated formula images inside it.

## Customization

You can customize the appearance of the generated formulas by modifying the `formula_to_png` function calls in `generate_formulas.py`:

* **`font_family`**: Change the font. Options include `"Computer Modern"`, `"Latin Modern"`, or `"Palatino"`.

* **`fontsize`**: Adjust the size of the text.

* **`color`**: Set the text color using named colors (e.g., `'red'`, `'blue'`), hexadecimal strings (e.g., `'#FF4500'`), or RGB/RGBA tuples (e.g., `(0.1, 0.3, 0.7)`).

For example, to change the math formulas to red:

```
# In generate_formulas.py, within the math formulas loop:

formula_to_png(latex_formula, filename, font_family="Latin Modern", fontsize=20, color="red")
```
