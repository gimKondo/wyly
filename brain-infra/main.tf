terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
    }
  }
  required_version = "= 0.14.3"
}

provider "google" {
  project     = var.project_name
  region      = "asia-northeast1"
}

terraform {
  backend "gcs" {
    bucket  = "wyly-brain-tfstate-dev"
  }
}

resource "google_cloud_run_service" "default" {
  name     = "wyly-brain"
  location = var.region
  template {
    spec {
      containers {
        image = "gcr.io/wyly-brain-dev/api:latest"
      }
    }
    metadata {
      labels = {
        project  = "wyly"
      }
    }
  }
  traffic {
    percent         = 100
    latest_revision = true
  }
}
