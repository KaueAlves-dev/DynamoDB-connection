data "aws_iam_policy_document" "dynamodb_data_policy" {
  statement {
    effect = "Allow"

    actions = [
      "dynamodb:PutItem",
      "dynamodb:UpdateItem",
      "dynamodb:GetItem",
      "dynamodb:Query",
      "dynamodb:DeleteItem"
    ]

    resources = ["arn:aws:dynamodb:us-east-1:787860407830:table/feedback_db"]
  }

}

data "aws_iam_policy_document" "cloudw_data_policy" {
  statement {
    effect = "Allow"

    actions = [
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents"
    ]

    resources = ["arn:aws:logs:us-east-1:787860407830:log-group:/aws/lambda/lambda_db_integration:*"]
  }

}


data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"

    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }

}


resource "aws_iam_role" "lambda_role" {
  name               = "lambda_db_role"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json

}


resource "aws_iam_policy" "dynamo_policy" {
  name   = "dynamo_policy"
  policy = data.aws_iam_policy_document.dynamodb_data_policy.json

}


resource "aws_iam_role_policy_attachment" "dynamo_policy_att" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = aws_iam_policy.dynamo_policy.arn
}

resource "aws_iam_policy" "cloudw_policy" {
  name   = "cloudw_policy"
  policy = data.aws_iam_policy_document.cloudw_data_policy.json
}

resource "aws_iam_role_policy_attachment" "cloudw_policy_att" {
  role = aws_iam_role.lambda_role.name
  policy_arn = aws_iam_policy.cloudw_policy.arn
}
