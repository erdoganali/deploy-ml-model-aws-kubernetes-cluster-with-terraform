resource "aws_s3_bucket" "mlops_bucket" {
  bucket = "mlops-churn-model-bucket" 
  force_destroy = true
  
  tags = {
    Terraform   = "true"
    Environment = "dev"
		Name = "mlops-bucket"
  }
}
resource "aws_s3_object" "mlops_object" {
  bucket = aws_s3_bucket.mlops_bucket.id
  key    = "pipeline_churn_random_forest.pkl"
  source = "../src/saved_model/pipeline_churn_random_forest.pkl"
}  
resource "aws_s3_bucket_acl" "mlops_bucket_acl" {
  bucket = aws_s3_bucket.mlops_bucket.id

  # Set the bucket ACL to "private"
  acl = "private"
}
