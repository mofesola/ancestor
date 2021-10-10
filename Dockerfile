FROM python:3

RUN apt-get update
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y

WORKDIR /usr/src
COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
