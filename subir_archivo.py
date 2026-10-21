import base64
import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    directorio = event['body']['directorio']
    nombre_archivo = event['body']['archivo']
    contenido_base64 = event['body']['contenido']

    # Normalizar directorio (debe terminar en "/")
    if directorio and not directorio.endswith('/'):
        directorio += '/'

    key = f'{directorio}{nombre_archivo}'

    # Proceso
    archivo_bytes = base64.b64decode(contenido_base64)
    s3 = boto3.client('s3')
    s3.put_object(Bucket=nombre_bucket, Key=key, Body=archivo_bytes)

    # Salida
    return {
        'statusCode': 200,
        'mensaje': f'Archivo {nombre_archivo} subido correctamente',
        'bucket': nombre_bucket,
        'key': key
    }
