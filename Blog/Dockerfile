FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY change_post.py .

ENV WP_URL="http://wordpress/wp-json/wp/v2"
ENV USERNAME="wordpress"
ENV PASSWORD="wordpress"

CMD ["python", "update_post.py"]