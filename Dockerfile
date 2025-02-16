FROM python:3.13

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--debug", "--host=0.0.0.0", "--port=5000"]

# docker build -t tg_bot .
# docker run tg_bot
# docker images
# docker ps