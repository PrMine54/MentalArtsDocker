FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY update_post.py .

ENV WP_URL="http://wordpress/wp-json/wp/v2"
ENV USERNAME="wordpress"
ENV PASSWORD="wordpress"

CMD ["python", "update_post.py"]

#For running:

#docker build -t wordpress-updater .

#docker run -e WP_URL="http://wordpress/wp-json/wp/v2" -e USERNAME="wordpress" -e PASSWORD="wordpress" wordpress-updater