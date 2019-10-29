FROM python:3.6-alpine

RUN adduser -D webstickers

WORKDIR /home/webstickers

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN venv/bin/pip3 install Pillow
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY webstickers.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP webstickers.py

RUN chown -R webstickers:webstickers ./
USER webstickers

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
