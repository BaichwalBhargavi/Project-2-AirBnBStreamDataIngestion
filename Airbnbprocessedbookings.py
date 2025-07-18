import json
import boto3
import pandas as pd
import io

s3 = boto3.client('s3')

bucket_name = 'airbnb-booking-records'
file_name = 'airbnbbookings.csv'

def lambda_handler(event, context):
    try:
        # Convert incoming event (assumed to be a list of records) to DataFrame
        new_df = pd.DataFrame(event)
        print(new_df)

        # Try reading existing file from S3
        try:
            response = s3.get_object(Bucket=bucket_name, Key=file_name)
            existing_df = pd.read_csv(response['Body'])

            # Combine existing and new data
            combined_df = pd.concat([existing_df, new_df], ignore_index=True)

        except Exception as e:
            # If file doesn't exist or can't be read, just use new data
            print(f"File not found or unreadable, starting fresh. Details: {e}")
            combined_df = new_df

        # Write combined DataFrame to CSV in memory
        csv_buffer = io.StringIO()
        combined_df.to_csv(csv_buffer, index=False, encoding ='utf-8')

        # Upload the updated file back to S3
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=csv_buffer.getvalue(),
            ContentType='text/csv'
        )

        return {
            'statusCode': 200,
            'body': f'Appended data to s3://{bucket_name}/{file_name}'
        }

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
