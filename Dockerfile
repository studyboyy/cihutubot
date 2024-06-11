FROM python:3.10
RUN git clone -b main https://github.com/studyboyy/cihutubot.git /home/Kazuuserbot/ \
    && chmod 777 /home/Kazuuserbot \
    && mkdir /home/Kazuuserbot/bin/

COPY ./sample_config.env ./config.env* /home/Kazuuserbot/

WORKDIR /home/Kazuuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
