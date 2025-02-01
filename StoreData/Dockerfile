FROM python:3.9

RUN apt-get update && \
    apt-get install -y docker.io docker-compose && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY store_data.py /app/store_data.py

RUN chmod +x /app/store_data.py

CMD ["python", "/app/store_data.py"]

# For running:

# docker build -t store_data-container .
# docker run --rm -v /var/run/docker.sock:/var/run/docker.sock store_data-container