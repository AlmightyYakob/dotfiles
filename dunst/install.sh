TARGET_DIR="$HOME/.config/dunst"
SRC_DIR="$DOTFILES/dunst"


if [ ! -d $TARGET_DIR ]; then
    sudo mkdir $TARGET_DIR
fi

sudo ln -s $SRC_DIR/dunstrc $TARGET_DIR/dunstrc
