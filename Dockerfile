FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 SMARTGATE_DB_PATH=/data/smartgate.db
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt \
    && useradd --system --uid 10001 --create-home appuser \
    && mkdir -p /data && chown 10001:10001 /data
COPY app /app/app
USER appuser
EXPOSE 8003
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8003/health', timeout=2)" || exit 1
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8003"]
