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

  def get_item(self, item):
    try:
      response = self.table.get_item(Key=item)

      if response.get("Item", False):
        return response["Item"]
      
      raise

    except Exception as e:
      logger.info(f"Não foi possivel encontrar o item {e}")
      return False

  def insert_item(self, item):
    logger.info("Iniciando inserção no banco de dados")
    try:
      response = self.table.put_item(Item=item)

      status_code = response["ResponseMetadata"]["HTTPStatusCode"]

      if status_code >= 300:
        raise 

      return True

    except Exception as e:
      logger.info(f"Não foi possivel encontrar o item {e}")
      return False  
    
  def update_item():
    pass


  def delete_item(self, item):
    
    try:
      response = self.table.delete_item(Key=item)

    except Exception as e:
      logger.info(f"Não foi possivel encontrar o item {e}")
      raise e  
    
    logger.info(f"Resposta ao deletar item -> {response}")
    return response   

#hardcore
  def update_item():
    pass