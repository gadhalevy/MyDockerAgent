FROM python:latest
WORKDIR /app
RUN rm -rf /app/*
# RUN mkdir -p /app/static_folder
# COPY ./static_html app/static_folder
# COPY ./src .
CMD [ "python", "-m", "http.server"]