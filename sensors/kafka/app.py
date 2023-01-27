from flask import Flask, request
from kafka import KafkaProducer
import json

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='kafka:9092')

@app.route('http://0.0.0.0:3000/moisturemate', methods=['POST'])
def post_data():
    data = request.get_json()
    producer.send('events', json.dumps(data).encode('utf-8'))
    return 'Data sent to kafka topic'

if __name__ == '__main__':
    app.run(debug=True)
