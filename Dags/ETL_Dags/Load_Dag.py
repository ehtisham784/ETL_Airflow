import boto3
import pandas as pd
from Transform_Dag import transform_function

def load_to_dynamodb():
    # Get the transformed data
    linkedin_post_tbl = transform_function()

    # Initialize DynamoDB resource
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('PostsTable')

    # Insert each row into the DynamoDB table
    for index, row in linkedin_post_tbl.iterrows():
        try:
            response = table.put_item(
                Item={
                    'Post_ID': int(row['Post_ID']),
                    'Total Reactions': int(row['Total Reactions']),
                    'Like Count': int(row['Like Count']),
                    'Appreciation Count': int(row['Appreciation Count']),
                    'Comments Count': int(row['Comments Count']),
                    'Posted Date': str(row['Posted Date']),
                    'Author First Name': str(row['Author First Name']),
                    'Author Last Name': str(row['Author Last Name']),
                    'Author Username': str(row['Author Username']),
                }
            )
            print(f"Inserted row {index} into DynamoDB:", response)
        except Exception as e:
            print(f"Failed to insert row {index}:", e)

    print("Data loading into DynamoDB completed.")
