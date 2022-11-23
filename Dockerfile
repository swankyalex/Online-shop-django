FROM python:3.10

RUN apt-get update && apt-get install -y netcat

RUN apt install --no-install-recommends --yes \
    bash \
    g++ \
    libffi-dev \
    make \
    redis-server \
    || exit 1
    
RUN apt clean && rm -rf /var/lib/apt/lists/* && rm -rf /var/cache/apt/archives

WORKDIR /app

COPY ./Pipfile .

COPY ./Pipfile.lock .

RUN pip install pipenv

RUN pipenv install --dev

COPY ./ ./

RUN chmod +x ./scripts/*.sh