# -*- coding: utf-8 -*-
"""
Created on Wed May  8 01:11:29 2019

@author: soumi
"""

import os
import boto3
from werkzeug.datastructures import FileStorage
from UserLogin.UserInfo import UserInfo
from ast import literal_eval
from boto3.dynamodb.conditions import Key, Attr
#from Utils import Util
#from Utils import Util
S3_BUCKET                 = "pix2appcontainer"
S3_KEY                    = "AKIAJVY6625NN4MICGOA"
S3_SECRET                 = "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"
#S3_LOCATION               = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)
S3_REGION = "us-west-2"

SECRET_KEY                = os.urandom(32)
DEBUG                     = True
PORT                      = 5000


TABLE_NAME = "pix2appFullUITurkuser"
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
                                    'AttributeName': 'turkToken',
                                    'KeyType': 'HASH'
                            }
                            ],
            AttributeDefinitions=
                            [
                            {
                                    'AttributeName': 'turkToken',
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

#    print(table.item_count)

def creteNewItem(turkInfo):
    dynamodb = boto3.resource(
            'dynamodb',
            region_name=S3_REGION
            )

            
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(
            Item={
                    'turkToken': turkInfo.turkToken,
                    'drawingCount': turkInfo.drawingsCount,
                    'drawings': str(turkInfo.drawings),
                    'successCount': turkInfo.successCount,
                    'successDrawing': str(turkInfo.successDrawing),
                    'Approved':turkInfo.approve
                    }
                )

def getItem(turkToken):
    dynamodb = boto3.resource(
            'dynamodb',
            region_name=S3_REGION

            )
    table = dynamodb.Table(TABLE_NAME)
    response = table.get_item(
    Key={
        'turkToken': turkToken
    }
    )
    item = response['Item']
    return item


def updateItem(turkToken, attribute, newValue):
    if attribute == 'drawings':
        newValue = str(newValue)
    dynamodb = boto3.resource(
            'dynamodb',
            region_name=S3_REGION
            )
    table = dynamodb.Table(TABLE_NAME)
    table.update_item(
    Key={
        'turkToken': turkToken
    },
    UpdateExpression='SET '+ attribute +'= :val1',
    ExpressionAttributeValues={
        ':val1': newValue
    }
    )
    
#def deleteItem(userID):
#
#    dynamodb = boto3.resource(
#            'dynamodb',
#            region_name=S3_REGION,
#            aws_access_key_id=S3_KEY,
#            aws_secret_access_key=S3_SECRET
#            )
#    table = dynamodb.Table(TABLE_NAME)
#    try:
#        response = table.delete_item(
#                Key={
#                        'username': userID
#                    })
#    except:
#        print("Hey")


def getUserList():
    userItems =getItems()
    usersList = {}
    for item in userItems:
#        print(item)
        dictItem = {}
        dictItem['drawingCount'] =  int(item['drawingCount'])
        dictItem['drawings'] =  literal_eval(item['drawings'])
        dictItem['successCount'] =  int(item['successCount'])
        dictItem['successDrawing'] =  literal_eval(item['successDrawing'])     
        dictItem['Approved'] =  int(item['Approved']) == 1     
        usersList[item['turkToken']] = dictItem
    return usersList


def getItems():
    dynamodb = boto3.resource(
            'dynamodb',
            region_name=S3_REGION
            )
    table = dynamodb.Table(TABLE_NAME)
    response = table.scan(
            FilterExpression=Attr('drawingCount').gt(-1)
            )
    items = response['Items']
    return items

    userItems =getItems()
    usersList = {}
    for item in userItems:
        dictItem = {}
        dictItem['turkToken'] =  item['turkToken']
        dictItem['drawingCount'] =  int(item['drawingCount'])
        dictItem['drawings'] =  literal_eval(item['drawings'])
        dictItem['successCount'] =  int(item['successCount'])
        dictItem['successDrawing'] =  literal_eval(item['successDrawing'])    
        dictItem['Approved'] =  literal_eval(item['Approved'])     
        usersList[item['turkToken']] = dictItem
    return usersList


#createTable()
#def transferUserInfo():
#    file = open("UserInfo.txt", "r") 
#    userInfos = literal_eval(file.read())
#    for userInfo in userInfos:
##        print(userInfos[userInfo])
#        userprofile = UserInfo(userInfo,userInfos[userInfo]['emailID'], userInfos[userInfo]['passWord'], userInfos[userInfo]['turkID'],userInfos[userInfo]['drawings'],int(userInfos[userInfo]['drawingCount']),int(userInfos[userInfo]['successCount']))
#        creteNewItem(userprofile)
#


#def updateUserInfo():
#    userInfos = getUserList()
#    for userInfo in userInfos:
#        deleteItem(userInfo)
#        newInfo =UserInfo(userInfo,userInfos[userInfo]['emailID'], userInfos[userInfo]['passWord'], userInfos[userInfo]['turkID'],userInfos[userInfo]['drawings'],int(userInfos[userInfo]['drawingCount']),int(userInfos[userInfo]['successCount']),[],0)
#        creteNewItem(newInfo)
        
        
#updateUserInfo()
#createTable()    
#updateItem() 
#A =getItem('soumik')
#print(A)
#updateItem('soumik', 'drawingsCount',41 )
#A = getUserList()
#print(A)
#A['soumik']
#        
#print(A['soumik'])
#updateItem('soumik', 'drawingsCount',41 )
#
#A = getUserList()
#print(A['cppgcc'])
#for elm in A:
##    updateItem(elm, 'SuccessDrawing', str('[]'))
##    updateItem(elm, 'consent', 0)
#    print(elm)
#A['soumik']
#        
#print(A['soumik'])
#creteNewItem()
#transferUserInfo()