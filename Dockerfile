FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
RUN apt-get update && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl \
    gettext \
    git \
    libpq-dev \
    vim \
    tree
COPY requirements.txt ./
RUN pip install -r requirements.txt
