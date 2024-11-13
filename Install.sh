#!/bin/zsh

# Installation script for the Scientific Calculator

# Variables
INSTALL_DIR="$HOME/.local/share/ezcacl"
EXECUTABLE_DIR="$HOME/.local/bin"
EXECUTABLE="$EXECUTABLE_DIR/cacl"

# Function to create necessary directories
create_directories() {
    mkdir -p "$INSTALL_DIR"
    mkdir -p "$EXECUTABLE_DIR"
}

# Function to copy the calculator file
copy_calculator() {
    cp "cacl.html" "$INSTALL_DIR/cacl.html"
}

# Function to create executable script
create_executable() {
    cat > "$EXECUTABLE" <<EOL
#!/bin/sh
xdg-open "$INSTALL_DIR/cacl.html"
EOL
    chmod +x "$EXECUTABLE"
}

# Function to update PATH if necessary
update_path() {
    if [[ ":$PATH:" != *":$EXECUTABLE_DIR:"* ]]; then
        echo 'export PATH="$PATH:$HOME/.local/bin"' >> "$HOME/.zshrc"
        export PATH="$PATH:$HOME/.local/bin"
        echo "Added $EXECUTABLE_DIR to PATH in .zshrc"
    fi
}

# Main installation function
install_calculator() {
    create_directories
    copy_calculator
    create_executable
    update_path
    echo "Installation complete."
    echo "You can launch the calculator by typing 'cacl' in the terminal."
}

# Run the installation
install_calculator
