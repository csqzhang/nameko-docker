FROM python:3-onbuild
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["nameko", "run", "--config", "conf.yml", "helloworld"]