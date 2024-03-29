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
  - enable Cloud Vision API
- GCP project setting for deployment(on CI)
  - enable Cloud Build API
  - enable Identity and Access Management (IAM) API
  - enable Cloud Resource Manager API
- Access authorization to GCS bucket "wyly-brain-tfstate-dev"
- set up Service account on GCP
  1. create Service account
     - required "owner" role
  2. download credential JSON
  3. set environment variable
     - `export GOOGLE_APPLICATION_CREDENTIALS=[path to credential JSON]`
     - Attention
       - On CI(GitHub Actions), secret is set JSON value
         - dev: GCP_SA_KEY_TERRAFORM_BRAIN_DEV
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

0. Before execute this, you should set credential JSON like following
   - `export GOOGLE_APPLICATION_CREDENTIALS=[path to credential JSON]`
1. At first, initialize terraform
   - `terraform init -backend-config "bucket=wyly-brain-tfstate-[Deploy target name]"`
   - Deploy target name: dev/prod
2. Create or select workspace
   - 1st time: `terraform workspace new [Deploy target name]`
   - 2nd time or later: `terraform workspace select [Deploy target name]`
3. Dry-run
   - `terraform plan`
4. Deploy
   - `terraform apply`
