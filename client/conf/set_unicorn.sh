# get the configuration from tmux options
conf=`tmux show -v "@unicorn_conf_$1"`
# if tmux shows an error getting the configuration
# create a new one
if [ $? -eq 1 ]
then
# set random values for red, green, blue and period
r=`od -An -N1 -i /dev/random`
r=`expr $r % 8`
g=`od -An -N1 -i /dev/random`
r=`expr $g % 8`
b=`od -An -N1 -i /dev/random`
r=`expr $b % 8`
period=`od -An -N1 -i /dev/random`
period=`expr $period % 8`
period=`expr 1 + $period`
conf="$r $g $b $period"
tmux set -q "@unicorn_conf_$1" "$conf"
fi
# send the command raspberry pi
curl -d "gameoflife $conf" raspberrypi.local:61002
# comment the line above and uncomment the line after this comment
# to send commands through ssh_manager instead:
# curl -d "curl -d 'gameoflife $conf' localhost:61002" localhost:61002
