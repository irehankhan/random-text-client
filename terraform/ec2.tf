resource "aws_instance" "FRONTEND-SERVER" {
    ami = "ami-0fc5d935ebf8bc3bc"
    instance_type = "t2.micro"
    key_name = aws_key_pair.ssh_key1.key_name

     security_groups = [aws_security_group.random_text_sg1.name]

    count=1

    tags = {
        Name = "Client Instance"

    }
}

resource "aws_security_group" "random_text_sg1" {
  name        = "random_text_sg1"
  description = "Allow inbound traffic on port 5010, 12345, and 22 from all IPs"

  # VPC ID where the security group will be created
  vpc_id = "vpc-003893cb3140f5d73"

  # Inbound rules to allow traffic on ports 5010, 12345, and 22 from all IPs
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
# Server Port
  ingress {
    from_port   = 12345
    to_port     = 12345
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
# For SSH Access
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
    ingress {
    from_port   = 3020
    to_port     = 3020
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
    ingress {
    from_port   = 3000
    to_port     = 3000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
    ingress {
    from_port   = 9100
    to_port     = 9100
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
      ingress {
    from_port   = 9090
    to_port     = 9090
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
      ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
# Outbound rule to allow all traffic to all IPS
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}