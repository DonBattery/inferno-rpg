# Dockerfile

# Ez a file tartalmaz instrukciókat arra hogyan építsük fel a program Docker konténerét

FROM python:3.10

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD [ "python3", "bot.py"]
