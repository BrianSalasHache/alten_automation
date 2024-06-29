FROM python:3.11-slim-bullseye

RUN apt-get -y update
RUN apt-get install -yqq unzip wget gnupg

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN wget -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/126.0.6474.0/linux64/chromedriver-linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver-linux64/chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99
ENV DRIVER_PATH=/usr/local/bin/chromedriver-linux64/chromedriver
ENV HEADLESS=true

RUN mkdir -p /features

COPY requirements.txt /

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY features /features

CMD ["behave"]