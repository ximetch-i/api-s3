import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    directorio = event['body']['directorio']

    # En S3 un "directorio" es un objeto vacio cuya key termina en "/"
    if not directorio.endswith('/'):
        directorio += '/'

    # Proceso
    s3 = boto3.client('s3')
    s3.put_object(Bucket=nombre_bucket, Key=directorio, Body=b'')

    # Salida
    return {
        'statusCode': 200,
        'mensaje': f'Directorio {directorio} creado en el bucket {nombre_bucket}',
        'bucket': nombre_bucket,
        'directorio': directorio
    }
