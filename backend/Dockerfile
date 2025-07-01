FROM python:latest
RUN python -m venv  /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
RUN rm -rf /app/*
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
# Uncomment the following lines if you want to copy static files and source code
# RUN mkdir -p /app/static_folder
# COPY ./static_html app/static_folder
COPY ./src .
CMD [ "python", "-m", "http.server"]