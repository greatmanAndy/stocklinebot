# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.10

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN apt-get update && \
    apt-get install -y unixodbc-dev && \
    rm -rf /var/lib/apt/lists/*

# install ta-lib
RUN curl -O https://nchc.dl.sourceforge.net/project/ta-lib/ta-lib/0.4.0/ta-lib-0.4.0-src.tar.gz && \
    tar xvf ta-lib-0.4.0-src.tar.gz && \
    cd ta-lib && \
    ./configure --prefix=/usr && \
    make && \
    make install && \
    cd .. && \
    rm -rf ta-lib-0.4.0-src.tar.gz ta-lib

RUN pip install --no-cache-dir -r requirements.txt && \
    pip uninstall -y numpy && \
    pip install -U TA-Lib && \
    pip install -U numpy


EXPOSE 5000

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec python app.py
