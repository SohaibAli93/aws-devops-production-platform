provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project   = "aws-devops-production-platform"
      ManagedBy = "Terraform"
    }
  }
}