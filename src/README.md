# Docker Images
docker images 

docker run --rm \
--name ml-prediction \
-p 8002:8000 -d mlops:1.1 

docker container stop mlops:1.1  


# AWS ECR register #######################


# create new docker image
docker image build -t mlops:1.1 .

docker images 

## Create you ecr repo
aws ecr create-repository --repository-name mlops --region eu-west-1

{
    "repository": {
        "repositoryArn": "arn:aws:ecr:eu-central-1:491452431274:repository/mlops",
        "registryId": "491452431274",
        "repositoryName": "mlops",
        "repositoryUri": "491452431274.dkr.ecr.eu-central-1.amazonaws.com/mlops",
        "createdAt": "2023-06-13T13:34:55+03:00",
        "imageTagMutability": "MUTABLE",
        "imageScanningConfiguration": {
            "scanOnPush": false
        },
        "encryptionConfiguration": {
            "encryptionType": "AES256"
        }
    }
:
	
## Authenticate your docker to ecr == > gives encrypted password for docker
aws ecr get-login-password --region eu-west-1


## Final Authenticate to ecr
aws ecr --region eu-west-1 | docker login -u AWS -p eyJwYXlsb2FkIjoiaGlNZWRweDE0VlJrb1g0TENHOStocWlFaW0vUEd1RmZPRzhvcjZIdFlJKzJHMEZGZDM0MWs3VktXTnl6OE51QUIzSXBUNThnMllCeGxZYXpoamNVc0puUFlCaWJXK25MTGYwVDhGaVVRdFNWK2JaUG9MU0lOMi9mVGlyR3Z0S2lpMTFaSzkyWUVhLzNRc0c3bzZYZHpHMEdjd3ZxZ3hLUGxRVUdjWm5sRmRWQ2ZHSUtYU0FZWjhlVWd2aERuMUtFd3FqS3Y0YkFMd3plOGVlNFhVbGhDbmVwcEk0dHhkVVkvdVloR3BhQVdnK0dFK2NDOXZHZkZua1h3endjaExiVmlZTGYwL0g3U0JwMW05YTRMVUVmcDRYQlMrQmp2dG5HeTFjU0kzMGRHQjFxSEc3UGtIY2dhM1daTXV4dEMxc0ZCMm1OQjdiVlNuekJQN3YrL0hIUmlYYThuQ3VZS2J0T1RLQWErWnpXSmRWQnFWNndhS2dBY3dTdFRYaENCZ24rUzBxVGVPeCs0QzNwM094WUsrRzBDM1B5SllXSDkwVDNhWVBKalErUkxZdHdFMFZhRS91OGQrNXB3TU9ETGdGaisxZE5iZUM2WGxGNjJLVmhQVHF0c2I3WjU2Q1l1OVNnRjh0RE9NQkxvT3ZwNis4WUx3TGNZL0RDdnNyTHdndm0vWlNIcVpkV0h3RERzS2hxMnNaNWx5Y2M1dFUzbXFzZm8vcUZraUw2MDZFSW44NmxOQVNpbUVlbUhCa3dYMHJvYjkvYURqNGRFaFBKZTRoZENmWmxVak5takRvblVaeXk1UkJuWkdyNkZKUXpSMTBvd2Y3QVNoQzZyM2w3MU9pSHNiaVQzUTVtVzE5UHFGamVJSGRUK3ZIQ3IyaTJERkVYbnMzS1BrWjRORzhpL3hsMkF5R1c0eS9VV1o1Ly9USWNhR3VaRlIrbnI4QzV5WGhRM2V2Umg5c3BDN2YwYUFDN2MzRWZOY2VoR1NOVC9UTE1Cd1hvcE9VelZMbDRKMTAzSDZuWGFWdDdJWkZvc3NLeTkrS1BONXRZSXpNVUR3UlcyUFdOZlpQNENYYTF3cmlDc0VkditlTUk4UGNNOE1WVnA0dmFWNHFhM1dRUHdxOEZFTDZvU3B5bkcrZGlZSEZqaWNVTzFpNUNabno4UTJMbkt2YXcrNnM2Y1NvM1h1L3FSYkVmN0ZCa3d3NFZGOE11cjRCY3BVNzFlbDVXaDlxOHBpRWcvY21MSTlTdTJqQmZmNFNvUitQYXBacWIyQU9QK3hMN0Q0dzZrTEIwS2xqV3h4L1hJUnMyTEJkZ1ozZGszY3J6UzRCU25SekQrMnYrYTZ3bFZIQ041WHNaIiwiZGF0YWtleSI6IkFRRUJBSGgrZFMrQmxOdTBOeG5Yd293YklMczExNXlqZCtMTkFaaEJMWnN1bk94azNBQUFBSDR3ZkFZSktvWklodmNOQVFjR29HOHdiUUlCQURCb0Jna3Foa2lHOXcwQkJ3RXdIZ1lKWUlaSUFXVURCQUV1TUJFRURERnE5NVlKODFWVDhFT1pQd0lCRUlBN1NnRTdkcU9nU21Vd1JML0s1cmZHZGhocXpWVFhjczYvNmJlSXhvY1dVUHRCbUFSVUdvQ2RJTURzUFZJYVFFellHT0ZMR0dwdUh4Z3Y2Q1E9IiwidmVyc2lvbiI6IjIiLCJ0eXBlIjoiREFUQV9LRVkiLCJleHBpcmF0aW9uIjoxNjg2ODAyMjI3fQ== 491452431274.dkr.ecr.eu-west-1.amazonaws.com/mlops

## docker tag
docker tag mlops:1.2 491452431274.dkr.ecr.eu-west-1.amazonaws.com/mlops:1.2

## docker push
docker push 491452431274.dkr.ecr.eu-west-1.amazonaws.com/mlops:1.2

yeni imaj adresi: 491452431274.dkr.ecr.eu-west-1.amazonaws.com/mlops:1.2

 

# AWS IAM POLICY 
1 - user root account olmadıgı için onun için policy create ediyoruz
2 - daha sonra bu policy 'yi attach ediyoruz. 
 

## IAM ROLE (default)
aws sts get-caller-identity 

# Terraform 

https://github.com/terraform-aws-modules

# terraform init
# terraform refresh


 

# versiyon guncelle (version.tf)

    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.47"
    }

    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = ">= 2.10"
    }
 

terraform init -upgrade 

terraform versiyon

# Module versiyon
module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  version         = "19.5.1"
  cluster_name    = local.cluster_name
  cluster_version = "1.27" 



# install Kubectl

 curl -LO https://dl.k8s.io/release/v1.27.2/bin/linux/amd64/kubectl  
   
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

kubectl version --client --output=yaml


# sudo apt install graphviz

## 14.1. terraform graph -type plan  | dot -Tsvg > graph.svg

## OUTPUTS 
cluster_endpoint = "https://6120F3ECB775146925D478735FBC4C92.gr7.eu-west-1.eks.amazonaws.com"
cluster_name = "test-eks-cluster-ME0h2Qf2"
cluster_security_group_id = "sg-0a2142574fbab7b2e"
region = "eu-west-1"


aws eks list-clusters


## KubeConfig Update 

 aws eks –-region $(terraform output -raw region) update-kubeconfig –-name $(terraform output -raw cluster_name)

 aws eks –-region eu-west-1 update-kubeconfig –-name test-eks-cluster-ME0h2Qf2 
 
 kubectl get nodes
 

## RDS Mysql 
- Connect ec2 

sudo dnf install mariadb105
sudo yum install mysql-client 
mlops.cw17zk3pwfhh.eu-west-1.rds.amazonaws.com
mysql -h mlops.cw17zk3pwfhh.eu-west-1.rds.amazonaws.com -P 3306 -u mlops_user -p 



# terradorm destroy 
# terraform state rm







# OTHER KIND OF PROVISION AWS EKS  #### 

# Install additional tools
sudo yum install -y jq gettext bash-completion

# Install eksctl
sudo curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /usr/local/bin

# Install kubectl
sudo curl --silent --location -o /usr/local/bin/kubectl "<https://dl.k8s.io/release/$>(curl --silent --location <https://dl.k8s.io/release/stable.txt>)/bin/linux/amd64/kubectl"
sudo chmod +x /usr/local/bin/kubectl

# Set AWS region and profile
export AWS_REGION=<your-region>
export AWS_PROFILE=<your-profile>

# Create an Amazon EKS cluster
eksctl create cluster \\
--name <your-cluster-name> \\
--version <your-kubernetes-version> \\
--region $AWS_REGION \\
--nodegroup-name <your-node-group-name> \\
--node-type <your-node-group-instance-type> \\
--nodes <number-of-nodes> \\
--nodes-min <minimum-number-of-nodes> \\
--nodes-max <maximum-number-of-nodes> \\
--ssh-access \\
--ssh-public-key <your-ssh-public-key> \\
--managed \\
--asg-access \\
--external-dns-access \\
--alb-ingress-access \\
--full-ecr-access \\
--appmesh-access \\
--cloudwatch-logs

# Get the kubeconfig file for the new cluster
aws eks update-kubeconfig --name <your-cluster-name>


<!-- 

export AWS_ACCESS_KEY_ID="AKIAXE3GY7OVHF3JP24Z"
export AWS_SECRET_ACCESS_KEY="LsGzLqCZgccLwZobCV2i0Zr9ZWoX05fw+ECfyjoG"
export AWS_REGION="eu-west-1"

 
export RDS_HOST="mlops.cw17zk3pwfhh.eu-west-1.rds.amazonaws.com"
export RDS_PORT="3306"
export RDS_DB_NAME="mlops"
export RDS_USER="mlops_user"
export RDS_PASSWORD="Ankara06"

export S3_BUCKET="mlops-miuul-bucket"
export S3_KEY="pipeline_churn_random_forest.pkl" -->