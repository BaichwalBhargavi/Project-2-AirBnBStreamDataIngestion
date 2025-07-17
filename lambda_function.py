import uuid
import random
import datetime
import json

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
        "bookingId": str(uuid.uuid4()),
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
    booking = generate_random_booking()
    
    return {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" },
        "body": json.dumps(booking)
    }
