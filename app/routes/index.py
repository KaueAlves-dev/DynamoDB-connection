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


@router.get('/dynamo')
def get_all():
  pass


@router.get('/dynamo/{id}')
def get_id(id: str):
  pass

@router.get('/dynamo/{sentiment}')
def get_sentiment(sentiment: str):
  pass

@router.post('/dynamo')
def create():
  #db = DynamoDB()
  #new_id = str(uuid.uuid4())
  #hoje = datetime.date()
  #db.insert_item(f"USERID#{new_id}", f"TIME#{hoje}", nome="kaue", idade=20)
  

  #return json.dumps({"teste": "deu certo"}), 201

  body = router.current_event.json_body
  user_dto = UserDTO.from_dict(body)
  user_service = UserService()
  response = user_service.insert_item(user_dto)



@router.put('/dynamo')
def updtae():
  pass

@router.delete('/dynamo')
def delete():
  pass