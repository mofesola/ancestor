ROOT="/home/pi/ancestor"

sudo apt update
sudo apt install -y python3-pip libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg libcairo2-dev python3-gst-1.0 supervisor libatlas-base-dev git curl libsdl2-mixer-2.0-0 libsdl2-image-2.0-0 libsdl2-2.0-0
sudo apt --no-install-recommends install -y jackd2
cp $ROOT/config/supervisord.conf /etc/supervisor/supervisord.conf
pip3 install -r requirements.txt
sudo /etc/init.d/alsa-utils stop
sudo /etc/init.d/alsa-utils start