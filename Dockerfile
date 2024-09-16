FROM python:3.12.6-bookworm as build

RUN apt-get update && apt-get install -y \
    postgresql \
    python3-dev \
    libffi-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip --no-cache-dir

WORKDIR /opt/project

COPY ./entrypoint.sh /

COPY ./requirements.txt /tmp/requirements.txt
COPY ./Makefile /opt/project/

RUN pip install --upgrade --no-cache-dir -r /tmp/requirements.txt


CMD ["/entrypoint.sh"]
