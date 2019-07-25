#!/bin/sh
if test "$(which code)"; then
	if [ "$(uname -s)" = "Darwin" ]; then
		VSCODE_HOME="$HOME/Library/Application Support/Code"
	else
		VSCODE_HOME="$HOME/.config/Code"
	fi
	mkdir -p "$VSCODE_HOME/User"

	ln -sf "$DOTFILES/vscode/settings.json" "$VSCODE_HOME/User/settings.json"
	ln -sf "$DOTFILES/vscode/keybindings.json" "$VSCODE_HOME/User/keybindings.json"
	ln -sf "$DOTFILES/vscode/snippets" "$VSCODE_HOME/User/snippets"

	# from `code --list-extensions`
	modules="
2gua.rainbow-brackets
blanu.vscode-styled-jsx
dbaeumer.vscode-eslint
dsznajder.es7-react-js-snippets
Equinusocio.vsc-material-theme
formulahendry.auto-close-tag
ms-python.python
PKief.material-icon-theme
robertohuertasm.vscode-icons
teabyii.ayu
vangware.dark-plus-material
"
	for module in $modules; do
		code --install-extension "$module" || true
	done
fi
