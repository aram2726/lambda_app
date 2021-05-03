
resource "aws_dynamodb_table" "announcements" {
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key = "uuid"
  name = "announcements"
  attribute {
    name = "uuid"
    type = "N"
  }
}
