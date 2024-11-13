import boto3

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# Define table name
table_name = 'PostsTable'

try:
    # Create table with 'Post_ID' as the partition key
    response = dynamodb.create_table(
        TableName=table_name,
        AttributeDefinitions=[
            {
                'AttributeName': 'Post_ID',  # Partition key
                'AttributeType': 'N'         # N = Number
            }
        ],
        KeySchema=[
            {
                'AttributeName': 'Post_ID',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    print(f"Table {table_name} is being created.")
except dynamodb.exceptions.ResourceInUseException:
    print(f"Table {table_name} already exists.")

# List all tables to confirm creation
response = dynamodb.list_tables()
print("DynamoDB Tables:")
for table in response['TableNames']:
    print(table)
