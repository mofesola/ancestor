ROOT="/home/pi/ancestor"

sudo apt update
sudo apt install -y python3-pip libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg libcairo2-dev python3-gst-1.0
cp $ROOT/config/supervisord.conf /etc/supervisor/supervisord
pip install --user supervisor
pip install -r requirements.txt
pip install pygobject
