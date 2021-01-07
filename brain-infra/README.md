# Infrastructure for wyly-brain

This projects manages infrastructure for wyly-brain.
The infrastructure is on GCP and managed by Terraform.

## Requirements

- Terraform v0.14.3
- Google Cloud SDK v321.0.0

## Developer tools

- VSCode with some extensions
  - [HashiCorp Terraform](https://marketplace.visualstudio.com/items?itemName=mauve.terraform)
- [TFLint](https://github.com/terraform-linters/tflint)
  - This tool collaborate with VSCode automatically

## Prerequisite

- GCP project setting
  - enable Container Registry API
  - enable Cloud Run API
- Access authorization to GCS bucket "wyly-brain-tfstate-dev"
- Service account
  1. create Service account
     - required "editor" role
  2. download credential JSON
  3. set environment variable
     - `export GOOGLE_APPLICATION_CREDENTIALS=[path to credential JSON]`
- build and push API Docker
  0. (1st time) setup gcloud command for Docker helper
    `gcloud auth configure-docker`
  1. move to API project directory
    `cd ../brain`
  2. build docker
    `docker build -t gcr.io/wyly-brain-dev/api .`
  3. push docker to Container Registry
    `docker push gcr.io/wyly-brain-dev/api:latest`

## Execution

1. At first, initialize terraform
  `terraform init`
2. Dry-run
  `terraform plan`
