import json
import boto3
import cv2
import numpy as np
from face_encoder import encode_face

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get bucket name and image key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    try:
        # Download image from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        image_content = response['Body'].read()

        # Convert image content to numpy array
        nparr = np.frombuffer(image_content, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Encode face
        face_vector = encode_face(img)

        # Here you might want to save the face_vector to a database or return it

        return {
            'statusCode': 200,
            'body': json.dumps('Face encoded successfully')
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error encoding face')
        }