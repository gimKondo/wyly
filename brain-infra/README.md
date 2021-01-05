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
- Access authorization to GCS bucket "wyly-brain-tfstate-dev"
- Credential file is on the path written on variables.tf
