import boto3
from decimal import Decimal
import random as rnd

conn = boto3.resource('dynamodb', region_name='us-east-1')

table = conn.create_table(
    TableName='lugod_transactions',
    KeySchema=[
        {'AttributeName': 'transactionId', 'KeyType': 'HASH'},
    ],
    AttributeDefinitions=[
        {'AttributeName': 'transactionId', 'AttributeType': 'S'},
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
table.wait_until_exists()

prods = [
    {'productName':'Wireless Camera', 'productCategory': 'Photography', 'productPrice': Decimal(str(1999.50))},
    {'productName': 'Tripod Stand', 'productCategory': 'Accessories', 'productPrice': Decimal(str(799.25))},
    {'productName': 'Memory Card 128GB', 'productCategory': 'Storage', 'productPrice': Decimal(str(701.00))},
]
for i in range(100):
    products = []
    amt = 0
    for _ in range(rnd.randint(1, len(prods))):
        item = rnd.choice(prods)
        products.append(item)
        amt += item['productPrice']

    table.put_item(
        Item={
            'transactionId': f'TXN-20251102-{(i+1):03}',
            'transactionDate': '2025-11-02',
            'transactionTimestamp': '2025-11-02T10:15:30Z', 
            'transactionAmount': Decimal(str(amt)),
            'transactionTotalQuantity': len(products),
            'products': products
        }
    )
