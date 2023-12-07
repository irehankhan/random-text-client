resource "aws_key_pair" "ssh_key1" {
  key_name = "ssh_key1"
  public_key = file("/Users/irehankhan/.ssh/id_rsa.pub")
}