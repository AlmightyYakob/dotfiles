if [ ! -d "$HOME/.config/i3" ]; then
    sudo mkdir $HOME/.config/i3
fi

sudo ln -s $(pwd -P)/config $HOME/.config/i3/config
sudo ln -s $(pwd -P)/i3blocks.conf $HOME/.config/i3/i3blocks.conf
sudo ln -s $(pwd -P)/scripts $HOME/.config/i3/scripts
