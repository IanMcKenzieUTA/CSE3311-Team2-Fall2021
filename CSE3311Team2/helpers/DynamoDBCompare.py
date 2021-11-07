import os
import boto3
from ast import literal_eval
from werkzeug.datastructures import FileStorage
from UserLogin.UserInfo import UserInfo
from boto3.dynamodb.conditions import Key, Attr
#from Utils import Util
#from Utils import Util
S3_BUCKET                 = "pix2appcontainer"

#S3_LOCATION               = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)
S3_REGION = "us-west-2"

SECRET_KEY                = os.urandom(32)
DEBUG                     = True
PORT                      = 5000


TABLE_NAME = "UICompareResult"
def createTable():
    dynamodb = boto3.resource(
            'dynamodb',
            region_name=S3_REGION
            )
    

    table = dynamodb.create_table(
            TableName=TABLE_NAME,
            KeySchema=  
                            [
                            {
                                    'AttributeName': 'taskid',
                                    'KeyType': 'HASH'
                            }
                            ],
            AttributeDefinitions=
                            [
                            {
                                    'AttributeName': 'taskid',
                                    'AttributeType': 'S'
                            },
                            ],
        ProvisionedThroughput=
                            {
                                    'ReadCapacityUnits': 5,
                                    'WriteCapacityUnits': 5
                            }
                            )

# Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName='users')





def creteNewItemForEval(taskID, userID, targetID):
    dynamodb = boto3.resource(
        'dynamodb',
        region_name=S3_REGION
    )

    table = dynamodb.Table(TABLE_NAME)
    table.put_item(
        Item={
            'taskid': taskID,
            'username': userID,
            'target': targetID,
            'drawings': "[]",
            'counts': 0,
            'ranks': "[]",
            'feedback': 'NA',
            'ft': -1,
            'ts': "[]",
            'topRelevance': "",
            'paid': 1,
        }
    )

def creteNewItem(taskID, userID, targetID):
    dynamodb = boto3.resource(
            'dynamodb',
            region_name=S3_REGION
            )
    
            
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(
            Item={
                    'taskid': taskID,                    
                    'username': userID,
                    'target': targetID,
                    'drawings': "[]",
                    'counts': 0,
                    'ranks': "[]",
                    'feedback':'NA',
                    'ft':-1,
                    'ts': "[]",
                    'topRelevance': "",
                    'paid': 0,
                    }
                )

def getItem(taskID):
    dynamodb = boto3.resource(
            'dynamodb',
            region_name=S3_REGION
            )
    table = dynamodb.Table(TABLE_NAME)
    response = table.get_item(
    Key={
        'taskid': taskID
    }
    )
    item = response['Item']
    return item




def setSuccess_old(taskID, success):
    rval = 'No'
    if success:
        rval = 'Yes'
        
    dynamodb = boto3.resource(
            'dynamodb',
            region_name=S3_REGION
            )
    table = dynamodb.Table(TABLE_NAME)
    # table.update_item(
    # Key={
    #     'taskid': taskID
    # },
    # UpdateExpression='SET result = :val1',
    # ExpressionAttributeValues={
    #     ':val1': rval
    # }
    # )
    table.update_item(
        Key={
            'taskid': taskID
            },
        UpdateExpression='SET #ts = :val1',
        ExpressionAttributeValues={
            ":val1": rval
            },
        ExpressionAttributeNames={
            "#ts": "result"
            }
        )
     
    
def setSuccess(taskID, success, curtime):
    rval = 'No'
    if success:
        rval = 'Yes'
        
    dynamodb = boto3.resource(
            'dynamodb',
            region_name=S3_REGION
            )
    table = dynamodb.Table(TABLE_NAME)
    table.update_item(
    Key={
        'taskid': taskID
    },
    UpdateExpression='SET feedback = :val1, ft = :val2',
    ExpressionAttributeValues={
        ':val1': rval,
        ':val2': curtime
        
    }
    )

def setRelevance(taskID, relevanceObj):

        dynamodb = boto3.resource(
            'dynamodb',
            region_name=S3_REGION
        )
        table = dynamodb.Table(TABLE_NAME)
        table.update_item(
            Key={
                'taskid': taskID
            },
            UpdateExpression='SET topRelevance = :val1',
            ExpressionAttributeValues={
                ':val1': str(relevanceObj)

            }
        )

    
def setItem(taskID, rank, curtime, strokes):

    prevItem = getItem(taskID)

    curCount =  prevItem['counts'] + 1
    curRank =  literal_eval(prevItem['ranks'])

    curTS = literal_eval(prevItem['ts'])

    curRank.append(rank)
    curTS.append(curtime)
    
    dynamodb = boto3.resource(
            'dynamodb',
            region_name=S3_REGION
            )
    table = dynamodb.Table(TABLE_NAME)
    table.update_item(
    Key={
        'taskid': taskID
    },
    UpdateExpression='SET counts = :val1, ranks = :val2, ts = :val3, drawings = :val4',
    ExpressionAttributeValues={
        ':val1': curCount,
        ':val2': str(curRank),
        ':val3': str(curTS),
        ':val4': str(strokes)
        
    }
    )    
    
def getItems():
    dynamodb = boto3.resource(
            'dynamodb',
            region_name=S3_REGION
            )
    table = dynamodb.Table(TABLE_NAME)
    response = table.scan()
    items = response['Items']
    
    for item in items:
        print(item)
    return 

def delAllItems():
    dynamodb = boto3.resource(
            'dynamodb',
            region_name=S3_REGION
            )
    table = dynamodb.Table(TABLE_NAME)
    response = table.scan()
    items = response['Items']
    
    for item in items:
        response = table.delete_item(
            Key={
                'taskid': item['taskid']
            }

        )
    return 


if __name__ == "__main__":
    getItems()
    # setItem('d7eeb8a868fc1e781e2a8dc2',1,2)
    # print(getItem('d7eeb8a868fc1e781e2a8dc2'))
    # setSuccess('ddd95ddd9a0604ba44d257ed', True)
    # setSuccess('c67d0449d4761824a6960513', True, 22)
    # print(getItem('26972102043e4c39b904e279'))