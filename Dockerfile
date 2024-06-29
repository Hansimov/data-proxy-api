FROM python:3.11-slim
WORKDIR $HOME/app
COPY requirements.txt $HOME/app
RUN mkdir /.cache && chmod 777 /.cache
RUN pip install -r requirements.txt
COPY . $HOME/app
EXPOSE 22001
CMD ["python", "-m", "apps.data_proxy_app"]