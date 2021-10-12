ROOT="/home/pi/ancestor"

sudo apt update
sudo apt install -y python3-pip libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg libcairo2-dev python3-gst-1.0 supervisor
sudo apt --no-install-recommends install -y jackd2
cp $ROOT/config/supervisord.conf /etc/supervisor/supervisord.conf
pip3 install -r requirements.txt
