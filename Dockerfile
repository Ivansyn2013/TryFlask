FROM python:3.10.10-alpine
WORKDIR /app

COPY req.txt requirement.txt
RUN pip install requirement.txt