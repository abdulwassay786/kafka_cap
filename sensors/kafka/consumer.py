from kafka import KafkaConsumer
import boto3
import json

consumer = KafkaConsumer('event', bootstrap_servers='kafka:9092')
s3 = boto3.client('s3')

for message in consumer:
    data = json.loads(message.value.decode('utf-8'))
    s3.upload_file(data, 's3_bucket', 'file_name.json')
