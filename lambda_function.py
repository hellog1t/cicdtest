import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    html = "<html><body><h1>Updated via CI/CD!</h1></body></html>"

    s3.put_object(
        Bucket="my-devops-test-99",
        Key="index.html",
        Body=html,
        ContentType="text/html"
    )

    return {"status": "success"}
