FROM python:3.10.10-alpine
WORKDIR /app

COPY req.txt requirement.txt
RUN pip install -r requirement.txt
COPY blog ./blog
COPY .env ./.env
COPY wsgi.py ./wsgi.py
EXPOSE 5001
CMD ["python", "wsgi.py"]