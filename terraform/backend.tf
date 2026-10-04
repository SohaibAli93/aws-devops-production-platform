terraform {
  backend "s3" {
    bucket       = "sohaib-devops-tfstate-751501312399"
    key          = "dev/terraform.tfstate"
    region       = "us-west-2"
    encrypt      = true
    use_lockfile = true
  }
}