# unicorn-tmux-pi
A program that assigns unicorn animations to each one of your tmux panes. It generates a random conway's game of life board with a color palette and generation frequency distict for that specific pane. The program remembers the color pallete and frequency and sets that configuration each time that pane is focused.

## Installation

There are two parts of the installation: installation of the raspberry pi server and the tmux client.

### Raspberry pi

The script assumes that the raspberry pi has a headless configuration and available through raspberrypi.local. If your configuration is different, you might have to adjust the domain where the webserver serves on raspberrypi/server/server.py.

1. Clone the repository into /home/pi.
2. Run the installation script:

/home/pi/unicorn-tmux-pi/raspberrypi/install.sh

This will copy the python server that receives the client's commands into a local directory and install a systemd daemon that starts the server upon startup.

### Tmux client

1. Clone the repository into your home directory.
2. Run the installation script:

~/unicorn-tmux-pi/client/install.sh

This will append the configurations needed to listen for focus events on tmux and the execution of client commands to trigger the raspberry pi animations.

## Demo

View demo on youtube: https://youtu.be/JMdNZsYVP6o

## Help, FAQ & Feature requests

For help and feature requests, file an issue to this repository. I will respond within 2 days.
