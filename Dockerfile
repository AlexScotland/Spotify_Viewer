FROM python:3.8.11 as prereqs
WORKDIR /spotify-web
COPY app/bin .

RUN apt-get update -y
# Copy over the proxy config
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
FROM prereqs as final
# Copy over the SSL cert and key
CMD python spotify_web/manage.py runserver 0.0.0.0:8000
# CMD tail -f /dev/null