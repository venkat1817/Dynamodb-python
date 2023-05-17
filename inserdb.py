#local to connect dynamodb connection data insert.
import boto3
dynamodb= boto3.resource('dynamodb')
dynamodbTable=dynamodb.Table('orders')
dynamodbTable.put_item (

   Item= {
        'name': 'sathish',
        'age':22,
        'college': 'Sv University',
        'location':'tirupati',
        'name': 'pavan',
        'age':22,
        'college': 'sdhr',
        'location':'tirupathi',
        'name': 'avinash',

        'name': 'venkat',
        'age':22,
        'college': 'sdhr',
        'location':'hyd',
        'mobileNo':1234567890,

        'name': 'avinash',
        'age':22,
        'college': 'sv',
        'location':'chennai',
   }
)