FROM python:3.9-slim AS line-bot

WORKDIR /app/run

COPY requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt
RUN pip install gunicorn

COPY *py /app

EXPOSE 5000

CMD ["gunicorn", "--pythonpath", "/app", "-w", "1", "-b", "0.0.0.0:5000", "line_bot:app"]


FROM python:3.9-slim as discord-bot

WORKDIR /app/run

COPY requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY *py /app

CMD ["python", "/app/discord_bot.py"]