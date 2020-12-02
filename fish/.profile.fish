# Path stuff
set PATH "$HOME/.local/bin:$PATH"

# Virtualenv
set -x WORKON_HOME $HOME/.virtualenvs
set -x PROJECT_HOME $HOME/kitware
bass source $HOME/.local/bin/virtualenvwrapper.sh

# Misc
headsetcontrol -s 80
