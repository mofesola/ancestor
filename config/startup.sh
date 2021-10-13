
cd /home/pi/ancestor
sudo /etc/init.d/alsa-utils stop
sudo /etc/init.d/alsa-utils start
su - pi && nohup /usr/bin/python3 /home/pi/ancestor/main.py &
