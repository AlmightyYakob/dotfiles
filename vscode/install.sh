#!/bin/sh
MODULES_FILE="./modules.txt"

if test "$(which code)"; then
	if [ "$(uname -s)" = "Darwin" ]; then
		VSCODE_HOME="$HOME/Library/Application Support/Code"
	else
		VSCODE_HOME="$HOME/.config/Code"
	fi
    USER_SETTINGS="$VSCODE_HOME/User"
	mkdir -p $USER_SETTINGS

	ln -sf "$DOTFILES/vscode/settings.json" "$USER_SETTINGS/settings.json"
	ln -sf "$DOTFILES/vscode/keybindings.json" "$USER_SETTINGS/keybindings.json"


    while IFS= read -r module
    do
		code --install-extension "$module" || true
    done < $MODULES_FILE
fi
