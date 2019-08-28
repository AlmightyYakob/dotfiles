SYSTEM_I3_DIR="$HOME/.config/i3"
I3_DIR="$DOTFILES/i3"


if [ ! -d $SYSTEM_I3_DIR ]; then
    sudo mkdir $SYSTEM_I3_DIR
fi

sudo ln -s $I3_DIR/config $SYSTEM_I3_DIR/config
sudo ln -s $I3_DIR/i3blocks.conf $SYSTEM_I3_DIR/i3blocks.conf
sudo ln -s $I3_DIR/scripts $SYSTEM_I3_DIR/scripts
