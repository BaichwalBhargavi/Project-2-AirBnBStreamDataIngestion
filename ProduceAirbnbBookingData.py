 
import random
import datetime
import json
import boto3

sqs_client = boto3.client('sqs')
sqs_queue_url = 'https://sqs.eu-north-1.amazonaws.com/178070228754/airbnb-booking-queue'

# Sample data for random choices
cities = ["New York, USA", "Paris, France", "Tokyo, Japan", "Sydney, Australia", "Berlin, Germany"]
user_ids = [f"user_{i}" for i in range(1, 101)]
property_ids = [f"property_{i}" for i in range(1, 51)]

def generate_random_booking():
    start_date = datetime.date.today() + datetime.timedelta(days=random.randint(0, 10))
    duration = random.randint(1, 7)
    end_date = start_date + datetime.timedelta(days=duration)
    price = random.randint(50, 500) * duration

    booking = {
        "bookingId": random.randint(1000, 9999),
        "userId": random.choice(user_ids),
        "propertyId": random.choice(property_ids),
        "location": random.choice(cities),
        "startDate": start_date.isoformat(),
        "endDate": end_date.isoformat(),
        "price": f"{price} USD"
    }
    return booking

# AWS Lambda handler
def lambda_handler(event, context):
    for i in range(100):
        booking = generate_random_booking()
        sqs_client.send_message(
           QueueUrl=sqs_queue_url,
          MessageBody=json.dumps(booking)
        )

    
    return {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" },
        "body": json.dumps(booking)
    }
