variable "aws_region" {
  description = "AWS region used for the DevOps platform"
  type        = string
  default     = "us-west-2"
}

variable "project_name" {
  description = "Name of the DevOps platform"
  type        = string
  default     = "aws-devops-production-platform"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
}