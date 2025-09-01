resource "aws_apigatewayv2_integration" "lambda_db_integration" {
  api_id = "3tq8naalth"
  integration_type = "AWS_PROXY"
  integration_uri = aws_lambda_function.lambda_db_integration.invoke_arn
  payload_format_version = "2.0"
  
}

resource "aws_apigatewayv2_route" "route_get_all" {
  api_id = "3tq8naalth"
  route_key = "GET /dynamo"

  target = "integrations/${aws_apigatewayv2_integration.lambda_db_integration.id}"  
}

resource "aws_apigatewayv2_route" "route_get_id" {
  api_id = "3tq8naalth"
  route_key = "GET /dynamo/{id}"

  target = "integrations/${aws_apigatewayv2_integration.lambda_db_integration.id}"  
}

resource "aws_apigatewayv2_route" "route_get_sentiment" {
  api_id = "3tq8naalth"
  route_key = "GET /dynamo/{sentiment}"

  target = "integrations/${aws_apigatewayv2_integration.lambda_db_integration.id}"  
}

resource "aws_apigatewayv2_route" "route_post" {
  api_id = "3tq8naalth"
  route_key = "POST /dynamo"

  target = "integrations/${aws_apigatewayv2_integration.lambda_db_integration.id}"  
}

resource "aws_apigatewayv2_route" "route_put" {
  api_id = "3tq8naalth"
  route_key = "PUT /dynamo"

  target = "integrations/${aws_apigatewayv2_integration.lambda_db_integration.id}"  
}

resource "aws_apigatewayv2_route" "route_del" {
  api_id = "3tq8naalth"
  route_key = "DELETE /dynamo"

  target = "integrations/${aws_apigatewayv2_integration.lambda_db_integration.id}"  
}




