
resource "aws_dynamodb_table" "announcements" {
  hash_key = "uuid"
  name = "announcements"
  attribute {
    name = "uuid"
    type = "N"
  }
}
