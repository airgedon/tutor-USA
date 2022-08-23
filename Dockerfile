FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /home/devops/tutor-USA

COPY . .

RUN python -m pip install --upgrade pip setuptools wheel

RUN pip install -r req.txt