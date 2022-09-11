import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(    # Create a table
    AttributeDefinitions=[
        {
            'AttributeName': 'Country',
            'AttributeType': 'S',
        },
        {
            'AttributeName': 'Number',
            'AttributeType': 'N',
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'Country',
            'KeyType': 'HASH',
        },
        {
            'AttributeName': 'Number',
            'KeyType': 'RANGE',
        },
    ],
    
    
    
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Countries_To_Visit')    # Insert table name where to write the list


with table.batch_writer() as batch:             # Add items to the table            
    batch.put_item(Item={"Country": "Sweden", "Number": 1})
    batch.put_item(Item={"Country": "France", "Number": 2})
    batch.put_item(Item={"Country": "Spain", "Number": 3})
    batch.put_item(Item={"Country": "Greece", "Number": 4})
    batch.put_item(Item={"Country": "Italy", "Number": 5})
    batch.put_item(Item={"Country": "Denmark", "Number": 6})
    batch.put_item(Item={"Country": "Singapore", "Number": 7})
    batch.put_item(Item={"Country": "Switzerland", "Number": 8})
    batch.put_item(Item={"Country": "Costa Rica", "Number": 9})
    batch.put_item(Item={"Country": "Thailand", "Number": 10})
    
print(batch)


dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Countries_To_Visit')

response = table.scan()
response['Items']

print(response)