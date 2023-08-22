from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel
import os

load_dotenv()

app = FastAPI()

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = int(os.getenv('REDIS_PORT'))
REDIS_DB = int(os.getenv('REDIS_DB', 0))

CORS_ALLOW_ORIGINS = os.getenv('CORS_ALLOW_ORIGINS', '*').split(',')

app.add_middleware(
    CORSMiddleware,
    allow_origins=[CORS_ALLOW_ORIGINS],
    allow_methods=['*'],
    allow_headers=['*']
)

# redis = get_redis_connection(
#     host="redis-11844.c135.eu-central-1-1.ec2.cloud.redislabs.com",
#     port=11844,
#     password="pRdcpRkKPFn6UnEFskrDGxrmFbf5T9ER",
#     decode_responses=True
# )

redis = get_redis_connection(
    host=REDIS_HOST,
    port=REDIS_PORT, 
    db=REDIS_DB, 
    decode_responses=True
)


class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis


@app.get('/products')
def all():
    return [format(pk) for pk in Product.all_pks()]


def format(pk: str):
    product = Product.get(pk)

    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    }


@app.post('/products')
def create(product: Product):
    return product.save()


@app.get('/products/{pk}')
def get(pk: str):
    return Product.get(pk)


@app.delete('/products/{pk}')
def delete(pk: str):
    return Product.delete(pk)
