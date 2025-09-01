resource "aws_cloudwatch_log_group" "cloudw_log" {
  name              = "/aws/lambda/lambda_db_integration"
  retention_in_days = 1  # opcoes: 1, 3, 7, 30, 90, etx
}