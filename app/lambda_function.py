from routes.index import router
from aws_lambda_powertools.event_handler import APIGatewayHttpResolver
from aws_lambda_powertools.logging import Logger


app = APIGatewayHttpResolver()
app.include_router(router)
logger = Logger()

def lambda_handler(event, context):
  return app.resolve(event, context)