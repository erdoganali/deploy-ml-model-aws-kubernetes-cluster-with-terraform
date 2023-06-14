import boto3
import os
import tempfile   
import joblib  


S3_BUCKET = os.environ.get("S3_BUCKET")
S3_KEY = os.environ.get("S3_KEY")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

def load_model_from_s3():
    s3_client = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)  
    with tempfile.TemporaryFile() as fp:
        s3_client.download_fileobj(Fileobj=fp, Bucket=S3_BUCKET, Key=S3_KEY)
        fp.seek(0)
        model = joblib.load(fp)

    return model