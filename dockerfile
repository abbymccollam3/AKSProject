FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV DD_AGENT_HOST=datadog-agent
ENV DD_TRACE_ENABLED=true
ENV DD_SERVICE=flask-demo
ENV DD_ENV=dev
CMD ["python", "app.py"]