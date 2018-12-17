# copy the server to your home directory
mkdir -p /home/pi/.unicorntmuxpi/
cp server /home/pi/.unicorntmuxpi/
# copy the systemd definition to the systemd directoy
cp unicorntmuxpi.service /lib/systemd/system/unicorntmuxpi.service
# adjusts permissions
chmod 644 /lib/systemd/system/unicorntmuxpi.service
# reload and enable
systemctl daemon-reload
systemctl enable unicorntmuxpi.service

echo 'Installation is done! Reboot your raspberry pi for changes to take effect'