# Simple Calculator

This is a simple scientific calculator I created to help with my coding and mathematical computations. It features both basic and scientific modes, allowing you to perform a variety of calculations with ease.

## Features

- **Basic Mode**: Standard arithmetic operations (addition, subtraction, multiplication, division).
- **Scientific Mode**: Additional functions including trigonometric functions, logarithms, exponentials, and more.
- **User Interface**:
  - Monochrome color scheme with black, dark gray, and light gray tones.
  - Curved corners and a two-pixel white border around the calculator.
  - Input expression displayed at the top, with the result shown below after pressing `=`, separated by a line.

## Git installation

### Prerequisites

- **Git** must be installed on your system.

#### Install Git on Your System

- **Ubuntu/Debian**:

  ```bash
  sudo apt update
  sudo apt install git
  ```

- **Fedora**:

  ```bash
  sudo dnf install git
  ```

- **Arch Linux**:

  ```bash
  sudo pacman -S git
  ```

- **openSUSE**:

  ```bash
  sudo zypper install git
  ```

- **NixOS**:

  ```bash
  nix-env -iA nixos.git
  ```

- **macOS** (Homebrew):

  ```bash
  brew install git
  ```

============================

###Installation(h3)

============================


1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/ezcacl.git
   ```

2. **Navigate to the Directory**:

   ```bash
   cd ezcacl
   ```

3. **Run the Installation Script**:

   ```bash
   ./install.sh
   ```

   - If you get a permission error, make the script executable:

     ```bash
     chmod +x install.sh
     ```

     Then run the script again:

     ```bash
     ./install.sh
     ```

4. **Update Your Terminal**:

   - If the script added `$HOME/.local/bin` to your PATH, you may need to restart your terminal or run:

     ```bash
     source "$HOME/.zshrc"
     ```

## Usage

- Launch the calculator by typing `cacl` in the terminal:

  ```bash
  cacl
  ```

- The calculator will open in your default web browser.

## Dependencies

- **xdg-open**: To open the calculator in your default web browser. It is usually installed by default on most Linux distributions.

## Notes

- The calculator is contained within a single HTML file (`cacl.html`), making it easy to modify or customize.
- If you encounter any issues or have suggestions, feel free to open an issue or submit a pull request.

## License

This project is licensed under the GNU General Public License (GPL).

---
eagan76 :D
