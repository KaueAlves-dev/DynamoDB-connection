from dto.dto import UserDTO
from integration.db_integration import DynamoDB

class UserService():


  def __init__(self):
    self.dynamo = DynamoDB()


  def insert_item(self, user_dto: UserDTO):
    item = user_dto.to_dict()
    response = self.dynamo.insert_item(item)

    return response
  
  def get_item(self, user_dto: UserDTO):
    item = user_dto.to_dict()
    response = self.dynamo.get_item(item)


    return response
  
    