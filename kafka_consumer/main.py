from fastapi import FastAPI, BackgroundTask
from aiokafka import AIOKafkaConsumer
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

app = FastAPI()

topics = os.getenv('TOPICS', ['my-topic']).split(',')


kafka_consumer_settings = {
    'booststrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
}

consumer.subscribe(topics)

async def consume_message():
    consumer = AIOKafkaConsumer(topics[0], loop=asyncio.get_event_loop(), **kafka_consumer_settings)
    await consumer.start()
    
    try:
        async for message in consumer:
            print(f"Received message: {message.value.decode('utf-8')}")
    finally:
        await consumer.stop()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(consume_message())

@app.post("/send-message/{topic}")
async def send_kafka_message(topic: str, message: str, background_tasks: BackgroundTasks):
    # Here, you can also send the message to Kafka using a producer, as shown in the previous answer
    background_tasks.add_task(send_message, topic, message)
    return {"message": "Message sent to Kafka"}

def send_message(topic, message):
    # Implement your Kafka message sending logic here
    pass