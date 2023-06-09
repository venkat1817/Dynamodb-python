#create ec2 instance comnnect to ssh connection.
#create i am role dynamodb to ec2 instance.
# sudo yum update -y
# sudo yum install -y python3
# whereis python 
# sudo yum install python3-pip
# whereis pip
# sudo pip3 install flask
# pip install boto3
# sudo yum install gunicorn3
# mkdir flaskapplication
# cd flaskapplication/
# vi app.py
# python3 app.py
# cd ..
# mkdir template
# cd template/
# vi table.html
#thise two folders in same directory
# [ec2-user@ip-172-31-47-198 flaskapplication]$ ls -ltr
# total 4
# -rwxr-xr-x. 1 ec2-user ec2-user 771 May  3 11:16 app.py
# drwxr-xr-x. 2 ec2-user ec2-user  24 May  3 11:21 templates

  #app.py


#python3 app.py run

#output give me ip address in browser
# ex:-http://18.119.12.40:8001/ 

from flask import Flask, render_template
import boto3

app = Flask(__name__, template_folder='template')
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

@app.route('/')
def index():
    response = dynamodb.scan(TableName='dynamodb-1')
    items = response['Items']
    data = []
    for item in items:
        data.append({
            'name': item['name'],
            'age': item['age'],
            'college': item['college'],
            'location': item['location']
        })
    data.append({
        'name': 'venkat',
        'age': '22',
        'college': 'Sv University',
        'location': 'tirupati'
    })

    data.append({
        'name': 'sathish',
        'age': '20',
        'college': 'CV raman jr College',
        'location': 'anantapur'
    })
    return render_template('table.html', data=data)
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=8001, debug=True)



import boto3
dynamodb = boto3.client('dynamodb', region_name='us-east-1')
table_name = 'dynamodb-1'
item = {
    'id': {'N': '1'},
    'name': {'S': 'John'},  
    'age': {'N': '30'},  
}
response = dynamodb.put_item(TableName=table_name, Item=item)
if response['ResponseMetadata']['HTTPStatusCode'] == 200:
    print('Item inserted successfully.')
else:
    print('Error inserting item:', response)
