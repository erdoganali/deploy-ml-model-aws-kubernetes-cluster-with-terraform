provider "kubernetes" {
  host                   = module.eks.cluster_endpoint
  cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)

  exec {
    api_version = "client.authentication.k8s.io/v1beta1"
    command     = "aws"
    # This requires the awscli to be installed locally where Terraform is executed
    args = ["eks", "get-token", "--cluster-name", module.eks.cluster_name]
  }
}

 

resource "kubernetes_namespace" "test" {
  metadata {
    name = "ml-service"
  }
}
resource "kubernetes_deployment" "test" {
  metadata {
    name      = "ml-service"
    namespace = kubernetes_namespace.test.metadata.0.name
  }
  spec {
    replicas = 2
    selector {
      match_labels = {
        app = "mlops-app-1"
      }
    }
    template {
      metadata {
        labels = {
          app = "mlops-app-1"
        }
      }
      spec {
        container {
          image = "491452431274.dkr.ecr.eu-west-1.amazonaws.com/mlops:1.2"
          name  = "mlops-app-1"
          port {
            container_port = 8000
          }
          env {
              name  = "RDS_HOST"
              value = aws_db_instance.example.address
          }
          env {
              name  = "RDS_DB_NAME"
              value = aws_db_instance.example.db_name
          }
          env {
              name  = "RDS_USERNAME"
              value = aws_db_instance.example.username
          }
          env {
              name  = "RDS_PASSWORD"
              value = aws_db_instance.example.password
          }
          env {
              name  = "RDS_PORT"
              value = "3306"
          }
          env {
              name  = "AWS_ACCESS_KEY_ID"
              value = "AKIAXE3GY7OVHF3JP24Z"
          }
          env {
              name  = "AWS_SECRET_ACCESS_KEY"
              value = "LsGzLqCZgccLwZobCV2i0Zr9ZWoX05fw+ECfyjoG"
          }
          env {
              name  = "S3_BUCKET"
              value = aws_s3_bucket.mlops_bucket.bucket
          }
          env {
              name  = "S3_KEY"
              value = "${aws_s3_object.mlops_object.key}"
          } 

        }
      }
    }
  }
}
resource "kubernetes_service" "test" {
  metadata {
    name      = "ml-service"
    namespace = kubernetes_namespace.test.metadata.0.name
  }
  spec {
    selector = {
      app = kubernetes_deployment.test.spec.0.template.0.metadata.0.labels.app
    }
    type = "LoadBalancer"
    port {
      port        = 80
      target_port = 8000
    }
  }
}