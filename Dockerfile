FROM python:3.11-slim
WORKDIR $HOME/app
COPY requirements.txt $HOME/app
RUN mkdir /app/cache && chmod 777 /app/cache
RUN pip install -r requirements.txt
COPY . $HOME/app
EXPOSE 22001
CMD ["python", "-m", "apis.data_proxy_api"]