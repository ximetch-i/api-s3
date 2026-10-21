import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    region = event['body'].get('region', 'us-east-1')

    # Proceso
    s3 = boto3.client('s3', region_name=region)

    if region == 'us-east-1':
        # us-east-1 NO acepta LocationConstraint
        s3.create_bucket(Bucket=nombre_bucket)
    else:
        s3.create_bucket(
            Bucket=nombre_bucket,
            CreateBucketConfiguration={'LocationConstraint': region}
        )

    # Salida
    return {
        'statusCode': 200,
        'mensaje': f'Bucket {nombre_bucket} creado correctamente',
        'bucket': nombre_bucket,
        'region': region
    }
