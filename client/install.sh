# copy the lines to the tmux config
cat ./conf/.tmux.conf >> ~/.tmux.conf
mkdir -p ~/.unicorntmuxpi/
cp ./conf/set_unicorn.sh ~/.unicorntmuxpi/
# tmux config might not pick up the focus event setting on
# the tmux config file, so run the hook command on shell startup
cmd="tmux set-hook window-pane-changed 'run-shell \"~/.unicorntmuxpi/set_unicorn.sh #{pane_id}\"'"
if [ -e ~/.bashrc ]
then
echo $cmd >> ~/.bashrc
fi

if [ -e ~/.zshrc ]
then
echo $cmd >> ~/.zshrc
fi

echo "Installation done!"
