
###############################
# IAM assumable role for admin
############################### 

module "iam_assumable_role_admin" {
  source = "terraform-aws-modules/iam/aws//modules/iam-assumable-role"

  allow_self_assume_role = true

  trusted_role_arns = [
    "arn:aws:iam::491452431274:root",
    "arn:aws:iam::491452431274:user/vbo-mlops", 
  ]

  trusted_role_services = [
    "codedeploy.amazonaws.com"
  ]

  create_role             = true
  create_instance_profile = true

  role_name         = "admin"
  role_requires_mfa = false

  attach_admin_policy = true

  tags = {
    Role = "Admin"
  }
}