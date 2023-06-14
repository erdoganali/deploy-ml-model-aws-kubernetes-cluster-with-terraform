 resource "aws_db_subnet_group" "rds_subnet_group" {
  name        = "rds-subnet-group"
  subnet_ids  = [module.vpc.private_subnets[0], module.vpc.private_subnets[1]]
  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}

resource "aws_security_group" "example" {
  name_prefix = "example"
  description = "Example security group"

  vpc_id = module.vpc.vpc_id

  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks     = ["0.0.0.0/0"]
  }

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}

resource "aws_db_instance" "example" {
  allocated_storage    = 10
  storage_type         = "gp2"
  db_name              = "mlops"
  identifier           = "mlops"
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = "db.t2.micro"
  username             = "mlops_user"
  password             = "Ankara06"
  port                 = 3306
  parameter_group_name = "default.mysql5.7"
  db_subnet_group_name = aws_db_subnet_group.rds_subnet_group.name
  vpc_security_group_ids = [aws_security_group.example.id]
  tags = {
    Terraform   = "true"
    Environment = "dev"
    Name = "mlops-db-instance"
  }

  skip_final_snapshot = true
  publicly_accessible =  true
}