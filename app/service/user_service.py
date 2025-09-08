from dto.dto import UserDTO
from integration.db_integration import DynamoDB
from aws_lambda_powertools.logging import Logger

logger = Logger()

class UserService():

  def __init__(self):
    self.dynamo = DynamoDB()


  def insert_item(self, user_dto: UserDTO):
    item = user_dto.to_dict()
    logger.info(f"item to_dict -> {item}")
    response = self.dynamo.insert_item(item)

    if response:
      return {"message": "Sucesso ao inserir item!", "error": False}, 201
    
    return {"message": "Erro ao inserir item!", "error": True}, 500
  
  def get_item(self, user_dto: UserDTO):
    item = user_dto.to_dict()
    logger.info(f"item to_dict -> {item}")
    response = self.dynamo.get_item(item)

    if response:
      return {"Item": response, "error": False}, 200
    
    return {"message": "Erro ao buscar item!", "error": True}, 404
  

  def delete_item(self, user_dto: UserDTO):
    item = user_dto.to_dict()
    logger.info(f"item to_dict -> {item}")
    response = self.dynamo.delete_item(item)

    if response:
      return {"message": "Sucesso ao deletar item!", "error": False}, 200
    
    return {"message": "Erro ao deletar item!", "error": True}, 500
    
  def update_item(self, user_dto: UserDTO):
    pass

  def get_all_items(self):
    pass