import json
from datetime import datetime
from itertools import count
def lambda_handler(event, context):
    print("Event", event)
    message = json.loads(event[0]['body'])
    print("Message", message)
    start = datetime.strptime(message['startDate'], "%Y-%m-%d")
    end = datetime.strptime(message['endDate'], "%Y-%m-%d")
    print("Start", start)
    print("End", end)
    print("Days", (end - start).days)
    count = 0
    if (end - start).days >=2:
        count +=1
        return message 
    # TODO implement
    print("Count", count)
  

