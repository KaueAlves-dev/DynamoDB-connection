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
        return item

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
  def update_item(self, item_keys: dict, item_values: dict):
    try:
      # Montando dinamicamente a UpdateExpression
      update_expression = []
      expression_attr_values = {}
      expression_attr_names = {}

      for i, (campo, valor) in enumerate(item_values.items()):
          value_placeholder = f":val{i}" # substui o valor a ser atribuido
          name_placeholder = f"#field{i}" # substitui o nome da coluna

          update_expression.append(f"{name_placeholder} = {value_placeholder}")
          expression_attr_values[value_placeholder] = valor
          expression_attr_names[name_placeholder] = campo

      update_expression_str = "SET " + ", ".join(update_expression)

      response = self.table.update_item(
          Key=item_keys,  
          UpdateExpression=update_expression_str,
          ExpressionAttributeValues=expression_attr_values,
          ExpressionAttributeNames=expression_attr_names,
          ConditionExpression="attribute_exists(userId)",
          ReturnValues="ALL_NEW"  
      )

      status_code = response["ResponseMetadata"]["HTTPStatusCode"]

      if status_code < 300:
        return response["Attributes"]
      
      return False

    except Exception as e:
      logger.info(f"Não foi possivel encontrar o item {e}")
      return False 