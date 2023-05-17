#local to connect with dynamodb sample data insert  using python code.
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

        'name': 'venkat',
        'age':22,
        'college': 'sdhr',
        'location':'hyd',
        'mobileNo':1234567890,

        'name': 'avinash',
        'age':27,
        'college': 'sv',
        'location':'chennai'
        ,
        'name': 'shiva',
        'age':23,
        'college': 'rgm',
        'location':'nadyal',
   }
   
)