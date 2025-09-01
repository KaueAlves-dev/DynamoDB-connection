resource "aws_lambda_function" "lambda_db_integration" {
  function_name    = "lambda_db_integration"
  role             = aws_iam_role.lambda_role.arn
  runtime          = "python3.9"
  filename         = "../lambda_function.zip"
  source_code_hash = filebase64sha256("../lambda_function.zip")
  environment {
    variables = {
      DYNAMO_NAME = "feedback_db"
    }
  }

}

resource "aws_lambda_permission" "lambda_permission" {
  statement_id  = "AllowAPIGTWInvoke"
  action        = "lambda:invokeFunction"
  function_name = aws_lambda_function.lambda_db_integration.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "arn:aws:execute-api:us-east-1:787860407830:3tq8naalth/$default/*/*"
}
