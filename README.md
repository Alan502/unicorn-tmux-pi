# unicorn-tmux-pi
A program that assigns unicorn animations to each one of your tmux panes.

## Installation

There are two parts of the installation: installation of the raspberry pi server and the tmux client.

### Raspberry pi

1. Clone the repository into /home/pi.
2. Run the installation script:

/home/pi/unicorn-tmux-pi/raspberrypi/install.sh

This will copy the python server that receives the client's commands into a local directory and install a systemd daemon that starts the server upon startup.

### Tmux client

1. Clone the repository into your home directory.
2. Run the installation script:

~/unicorn-tmux-pi/client/install.sh

This will append the configurations needed to listen for focus events on tmux and the execution of client commands to trigger the raspberry pi animations.

## Help, FAQ & Feature requests

For help and feature requests, file an issue to this repository. I will respond within 2 days.
