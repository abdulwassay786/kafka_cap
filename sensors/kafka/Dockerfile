FROM python:3.8
COPY . /app
WORKDIR /app

CMD ["python", "./app.py"]

CMD bash -c "/wait-for-it.sh --timeout=0 broker:9092 -- python solution.py"
