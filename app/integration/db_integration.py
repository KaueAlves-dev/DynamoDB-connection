import boto3
import os
import uuid
from aws_lambda_powertools.logging import Logger


logger = Logger()
TABLE_NAME = os.environ["DYNAMO_NAME"]

class DynamoDB:

  def __init__(self):
    self.resource = boto3.resource("dynamodb")
    self.table = self.resource.Table(TABLE_NAME)

  def get_item(self, item: dict):
    try:
      response = self.table.get_item(Key=item)

      return response.get("Item", False)

    except Exception as e:
      logger.info(f"Não foi possivel encontrar o item {e}")
      return False

  def insert_item(self, item: dict):
    logger.info("Iniciando inserção no banco de dados")
    try:
      response = self.table.put_item(Item=item)
      status_code = response["ResponseMetadata"]["HTTPStatusCode"]

      if status_code < 300:
        return True

      return False

    except Exception as e:
      logger.info(f"Não foi possivel encontrar o item {e}")
      return False  
    
  def delete_item(self, item: dict):
    
    try:
      response = self.table.delete_item(Key=item)
      status_code = response["ResponseMetadata"]["HTTPStatusCode"]

      if status_code < 300:
        return True
      
      return False

    except Exception as e:
      logger.info(f"Não foi possivel encontrar o item {e}")
      return False 
    
#hardcore
  def update_item():
    pass