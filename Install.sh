# Check for Python3 installation
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install Python3."
    exit
fi

# Install required Python packages
python3 -m pip install --user pyinstaller tk

# Create executable with PyInstaller
pyinstaller --onefile --windowed calculator.py

# Move the executable to local bin for easy access
if [ ! -d "$HOME/.local/bin" ]; then
  mkdir -p "$HOME/.local/bin"
fi
mv dist/calculator "$HOME/.local/bin/ezcalc"

# Create desktop shortcut for Linux
echo "[Desktop Entry]
Type=Application
Name=Ezcalc
Exec=$HOME/.local/bin/ezcalc
Icon=utilities-calculator
Terminal=false" > "$HOME/Desktop/Ezcalc.desktop"

# Set permissions and make the shortcut executable
chmod +x "$HOME/Desktop/Ezcalc.desktop"

echo "Installation complete. You can launch Ezcalc from the desktop shortcut or by typing 'ezcalc' in the terminal."
	
