#Thise code is deploy to ec2 server thise python code connect to the dynamodb server insert the sample data.
#sudo yum install -y python3
#sudo yum install python3-pip
#pip install boto3
#vi insert_data.py
import boto3

region_name = 'us-east-1'

dynamodb = boto3.resource('dynamodb', region_name=region_name)
dynamodbTable = dynamodb.Table('dynamodb-data')

items = [
    {
        'name': 'sathish',
        'age': 22,
        'college': 'Sv University',
        'location': 'tirupati'
    },
    {
        'name': 'pavan',
        'age': 22,
        'college': 'sdhr',
        'location': 'tirupathi'
    },
    {
        'name': 'venkat',
        'age': 22,
        'college': 'sdhr',
        'location': 'hyd',
        'mobileNo': 1234567890
    },
    {
        'name': 'avinash',
        'age': 27,
        'college': 'sv',
        'location': 'chennai'
    },
    {
        'name': 'shiva',
        'age': 23,
        'college': 'rgm',
        'location': 'nadyal'
    }
]

for item in items:
    dynamodbTable.put_item(Item=item)

#python3 insert_data.py
#aws configure 
#a.key
#s.key

