import os
import boto3
from werkzeug.datastructures import FileStorage
#from Utils import Util
#from Utils import Util
S3_BUCKET                 = "fullsketchui"
S3_KEY                    = "AKIAJVY6625NN4MICGOA"
S3_SECRET                 = "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"
#S3_LOCATION               = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)
S3_REGION = "us-west-2"

SECRET_KEY                = os.urandom(32)
DEBUG                     = True
PORT                      = 5000


consideredFiles = ['back','cancel','forward','hamburger','leftarrow','play','plus','search','settings','share']

def upload_file_to_s3(fileName,uploadContent, acl="private"):
    
    fileNameToUpload = uploadContent.elementType+"/"+ fileName
    s3 = boto3.resource(
            's3',
            region_name=S3_REGION,
            aws_access_key_id=S3_KEY,
            aws_secret_access_key=S3_SECRET
            )

#    content_type = 	"text/plain"
    try:
            s3.Object(S3_BUCKET, fileNameToUpload).put(Body=str(uploadContent.content))
 
    except Exception as e:
        # This is a catch all exception, edit this part to fit your needs.
            print("Something Happened: ", e)
            return e
        


def get_all_s3_object_Count():
    s3 = boto3.client(
                "s3",
                aws_access_key_id=S3_KEY,
                aws_secret_access_key=S3_SECRET,
                region_name= S3_REGION
    )
    objects         = s3.list_objects_v2(Bucket=S3_BUCKET)
    contents = objects['Contents']
    
#    for obj in objects:
#        print(obj)
#    
    while objects['IsTruncated']:
#        print(type(objects['IsTruncated']))
#        print(objects['IsTruncated'])
#        print(objects['NextContinuationToken'])
        objects = s3.list_objects_v2(Bucket=S3_BUCKET, ContinuationToken = objects['NextContinuationToken'])
        contents.extend(objects['Contents'])
#        totalObject= len(objects['Contents'])
        
    totalObject= len(contents)
#    dictList = {}
#    for content in contents:
#        fullFileName = content['Key']
#        if fullFileName != 'UserInfo.txt':
#            directory = fullFileName.split('/')
#            fileCount = fullFileName.split('_')
#            if directory[0] in consideredFiles:
#                totalObject = totalObject+1
#            if directory[0] in dictList:
#                dictList[directory[0]] = max(int(fileCount[-1]),dictList[directory[0]])
#            else:
#                dictList[directory[0]] = int(fileCount[-1])
    
    return totalObject

def get_all_s3_objects():
    s3 = boto3.client(
                "s3",
                aws_access_key_id=S3_KEY,
                aws_secret_access_key=S3_SECRET,
                region_name= S3_REGION
    )
    objects         = s3.list_objects_v2(Bucket=S3_BUCKET)
    totalObject= 0
    dictList = {}

    if 'contents' in objects:  
        contents = objects['Contents']
#    for obj in objects:
#        print(obj)
#    
        while objects['IsTruncated']:
#        print(type(objects['IsTruncated']))
#        print(objects['IsTruncated'])
#        print(objects['NextContinuationToken'])
            objects = s3.list_objects_v2(Bucket=S3_BUCKET, ContinuationToken = objects['NextContinuationToken'])
            contents.extend(objects['Contents'])
            totalObject= len(objects['Contents'])
        
 
        for content in contents:
            fullFileName = content['Key']
            directory = fullFileName.split('/')
            fileCount = fullFileName.split('_')
            if directory[0] in consideredFiles:
                totalObject = totalObject+1
            if directory[0] in dictList:
                dictList[directory[0]] = max(int(fileCount[-1]),dictList[directory[0]])
            else:
                dictList[directory[0]] = int(fileCount[-1])
    
    return dictList, totalObject
#
    
