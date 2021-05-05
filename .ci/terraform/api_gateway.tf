resource "aws_api_gateway_rest_api" "announcement_api" {
  body = jsonencode({
    openapi = "3.0.1"
    info = {
      title   = "announcement_api"
      version = "1.0"
    }
    paths = {
      "/list-announcements" = {
        get = {
          x-amazon-apigateway-integration = {
            httpMethod           = "GET"
            payloadFormatVersion = "1.0"
            type                 = "HTTP_PROXY"
            uri                  = "https://ip-ranges.amazonaws.com/ip-ranges.json"
          }
        }
      },
      "/create-announcement" = {
        post = {
          x-amazon-apigateway-integration = {
            httpMethod           = "POST"
            payloadFormatVersion = "1.0"
            type                 = "HTTP_PROXY"
            uri                  = "https://ip-ranges.amazonaws.com/ip-ranges.json"
          }
        }
      }
    }
  })
  name = "announcement_api"
}


resource "aws_api_gateway_resource" "announcement_api" {
  parent_id   = aws_api_gateway_rest_api.announcement_api.root_resource_id
  path_part   = "announcement_api"
  rest_api_id = aws_api_gateway_rest_api.announcement_api.id
}

resource "aws_api_gateway_method" "announcement_api" {
  authorization = "NONE"
  http_method   = "GET"
  resource_id   = aws_api_gateway_resource.announcement_api.id
  rest_api_id   = aws_api_gateway_rest_api.announcement_api.id
}


resource "aws_iam_role" "api_gateway" {
 name = "announcement_api"
 path = "/"

 assume_role_policy = <<EOF
  {
     "Version": "2012-10-17",
      "Statement": [
         {
           "Sid": "",
           "Effect": "Allow",
           "Principal": {
           "Service": "apigateway.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
     ]
  }
  EOF
}