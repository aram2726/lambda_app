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

resource "aws_api_gateway_integration" "announcement_api" {
  http_method = aws_api_gateway_method.announcement_api.http_method
  resource_id = aws_api_gateway_resource.announcement_api.id
  rest_api_id = aws_api_gateway_rest_api.announcement_api.id
  type        = "MOCK"
}

resource "aws_api_gateway_deployment" "announcement_api" {
  rest_api_id = aws_api_gateway_rest_api.announcement_api.id

  triggers = {
    # NOTE: The configuration below will satisfy ordering considerations,
    #       but not pick up all future REST API changes. More advanced patterns
    #       are possible, such as using the filesha1() function against the
    #       Terraform configuration file(s) or removing the .id references to
    #       calculate a hash against whole resources. Be aware that using whole
    #       resources will show a difference after the initial implementation.
    #       It will stabilize to only change when resources change afterwards.
    redeployment = sha1(jsonencode([
      aws_api_gateway_resource.announcement_api.id,
      aws_api_gateway_method.announcement_api.id,
      aws_api_gateway_integration.announcement_api.id,
    ]))
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_api_gateway_stage" "announcement_api" {
  deployment_id = aws_api_gateway_deployment.announcement_api.id
  rest_api_id   = aws_api_gateway_rest_api.announcement_api.id
  stage_name    = "announcement_api"
}
