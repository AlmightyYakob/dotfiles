TARGET_DIR="$HOME/.config/polybar"
SRC_DIR="$DOTFILES/polybar"


if [ ! -d $TARGET_DIR ]; then
    sudo mkdir $TARGET_DIR
fi

sudo ln -s $SRC_DIR/config $TARGET_DIR/config
