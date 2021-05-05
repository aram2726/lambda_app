resource "aws_lambda_function" "announcements" {
  function_name = "announcements_app"
  role = aws_iam_role.LambdaExecutionRole.arn
  handler = "src.api.Main"
  timeout = 30

  # TODO: add role for DynamoDB
  # TODO: add trigger api gateway

  # The filebase64sha256() function is available in Terraform 0.11.12 and later
  # For Terraform 0.11.11 and earlier, use the base64sha256() function and the file() function:
  # source_code_hash = "${base64sha256(file("lambda_function_payload.zip"))}"
  source_code_hash = filebase64sha256("../../src.zip")

  runtime = "python3.8"
}

resource "aws_iam_role" "LambdaExecutionRole" {
 name = "lambda-execution-role"
 path = "/"
 assume_role_policy = <<EOF
  {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "",
         "Effect": "Allow",
         "Principal": {
            "Service": "lambda.amazonaws.com"
         },
         "Action": "sts:AssumeRole"
       }
     ]
  }
EOF
}

resource "aws_iam_role_policy" "dynamodb" {
 name = "dynamo-policy"
 role = aws_iam_role.LambdaExecutionRole.id

 policy = <<EOF
  {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowLambdaFunctionInvocation",
            "Effect": "Allow",
            "Action": [
                "lambda:InvokeFunction"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "APIAccessForDynamoDBStreams",
            "Effect": "Allow",
            "Action": [
                "dynamodb:GetRecords",
                "dynamodb:GetShardIterator",
                "dynamodb:DescribeStream",
                "dynamodb:ListStreams"
            ],
            "Resource": "arn:aws:dynamodb:*"
        }
    ]
  }
  EOF
}

