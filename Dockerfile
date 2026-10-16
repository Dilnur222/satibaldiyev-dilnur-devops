FROM python:3.12-slim
WORKDIR /app
COPY app.py .
COPY test_app.py .
RUN python -m py_compile app.py test_app.py
CMD ["python", "app.py"]

