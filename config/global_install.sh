ROOT="/home/pi/ancestor"

sudo apt update
sudo apt install -y python3-pip libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg libcairo2-dev python3-gst-1.0 supervisor
cp $ROOT/config/supervisord.conf /etc/supervisor/supervisord
pip3 install --user supervisor
pip3 install -r requirements.txt
pip install pygobject
