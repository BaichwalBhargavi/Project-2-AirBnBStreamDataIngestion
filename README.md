# Project-2-AirBnBStreamDataIngestion
# Airbnb Booking AWS Project

This project demonstrates an end-to-end data pipeline using AWS services to simulate and process Airbnb booking data. It uses SQS, Lambda, EventBridge, and S3 to ingest, filter, enrich, and store booking information.

---

## 🛠️ Architecture Overview

1. **Data Generation**  
   A Lambda function generates random Airbnb booking data and publishes it to an SQS queue (`airbnb-booking-queue`).

2. **Dead Letter Queue (DLQ)**  
   Failed messages (after 3 attempts) from the SQS are moved to `airbnb-booking-dlq`.

3. **EventBridge Integration**  
   An EventBridge rule listens to messages from the SQS and triggers an enrichment Lambda function (`Airbnbbooking`). 

4. **Enrichment Lambda**  
   Filters bookings that are **greater than 2 days** and passes them to the next processing stage (`ProcessFilteredBookings`).

5. **Data Storage Lambda**  
   Converts enriched booking data to CSV using **Pandas** and stores the file in an **S3 bucket** (`Airbnbprocessedbookings`).


## 🧪 Testing & Deployment

- Lambda functions and dependencies are zipped and uploaded to S3.
- AWS CodeBuild is used for continuous integration and deployment.
- Buildspec file (`buildspec.yml`) contains Lambda and S3 configuration.
- Git workflow uses feature branches (`lambda-test`) and merge commits to trigger build and deployment.

<img width="1222" height="562" alt="image" src="https://github.com/user-attachments/assets/3ba90d7c-362e-4f81-9e7a-ec53c2898a8d" />


