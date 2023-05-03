import boto3
from flask import Flask, jsonify

app = Flask(__name__)
# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

# Retrieve data from DynamoDB table
table = dynamodb.Table('dynamodb-1')
response = table.scan()

# Define API endpoint for retrieving data
@app.route('/data', methods=['GET'])
def get_data():
    data = response['Items']
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)