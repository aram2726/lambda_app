
resource "aws_lambda_function" "announcements" {
  function_name = "announcements"
  handler = "src/api"
  role = ""
  runtime = "python3.8"
}
