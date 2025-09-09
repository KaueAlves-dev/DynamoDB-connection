from aws_lambda_powertools.event_handler.api_gateway import Router
from aws_lambda_powertools.logging import Logger
from integration.db_integration import DynamoDB
import uuid
from datetime import datetime
import json

from service. user_service import UserService
from dto.dto import UserDTO

router = Router()
logger = Logger()

user_service = UserService()

@router.get('/dynamo')
def get_all():
  query_params = router.current_event.query_string_parameters

  if query_params:
    user_dto = UserDTO.from_dict(query_params)
    response, status_code = user_service.get_item(user_dto)

  # response, status_code = user_service.get_all_items()
  return response, status_code


@router.post('/dynamo')
def create():
  
  body = router.current_event.json_body
  user_dto = UserDTO.from_dict(body)
  response, status_code = user_service.insert_item(user_dto)

  return response, status_code
  

@router.delete('/dynamo')
def delete():
  body = router.current_event.json_body
  user_dto = UserDTO.from_dict(body)
  response, status_code = user_service.delete_item(user_dto)

  return response, status_code
  

@router.put('/dynamo')
def update():
  body = router.current_event.json_body
  user_dto = UserDTO.from_dict(body)
  response, status_code = user_service.update_item(user_dto)

  return response, status_code