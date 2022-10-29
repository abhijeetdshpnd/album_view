import boto3
import os
from botocore.client import Config

x = os.environ.get('access_key_id')

y = os.environ.get('secret_access_key')


def show_image(bucket):
    s3_client = boto3.client('s3',
                             aws_access_key_id=x,
                             aws_secret_access_key=y,
                             config=Config(signature_version='s3v4'))

    public_urls = []
    for item in s3_client.list_objects(Bucket=bucket)['Contents']:

        presigned_url = s3_client.generate_presigned_url('get_object',
                                                         Params={
                                                             'Bucket': bucket,
                                                             'Key': item['Key']
                                                         },
                                                         ExpiresIn=100)
        metadata = s3_client.head_object(Bucket=bucket, Key=item['Key'])
        print(metadata)
        if '.' in item['Key']:
            public_urls.append(presigned_url)

    # print("[INFO] : The contents inside show_image = ", public_urls)
    return public_urls
