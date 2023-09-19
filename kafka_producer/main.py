from fastapi import FastAPI
from confluent_kafka import Producer
from dotenv import load_dotenv
load_dotenv()


producer = Producer({'bootstrap.servers': 'localhost:9092'})

def send_message(topic, message):
    producer.produce(topic, message.encode('utf-8'))
    producer.flush()

app = FastAPI()
async def send_kafka_message(topic: str, message: str):
    send_message(topic, message)
    return {"message" "Message sent to Kafka!"}