#!/usr/bin/env python
import boto3
import random
import os
BUCKET=os.environ.get('AWS_S3_BUCKET')
if (BUCKET != None):
    s3 = boto3.client('s3')
    with open("maze.txt", "rb") as f:
        s3.upload_fileobj(f, BUCKET, "maze"+str(random.randrange(100000))+".txt")
else:
    print("AWS_S3_BUCKET was not set so not uploading file")