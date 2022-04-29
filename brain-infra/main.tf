terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
    }
  }
  required_version = "= 0.14.3"
}

provider "google" {
  project = var.project_name
  region  = "asia-northeast1"
}

terraform {
  backend "gcs" {}
}

resource "google_cloud_run_service" "api_server" {
  name     = "wyly-brain"
  location = var.region
  template {
    spec {
      containers {
        image = "gcr.io/wyly-brain-dev/api:latest"
      }
      service_account_name = google_service_account.cloud-run-service-account.email
    }
    metadata {
      labels = {
        project = "wyly"
      }
    }
  }
  traffic {
    percent         = 100
    latest_revision = true
  }
  lifecycle {
    ignore_changes = [
      template[0].spec[0].containers,
    ]
  }
  autogenerate_revision_name = true
}

resource "google_cloud_run_service_iam_member" "allUsers" {
  service  = google_cloud_run_service.api_server.name
  location = google_cloud_run_service.api_server.location
  role     = "roles/run.invoker"
  member   = "allUsers"
}

resource "google_storage_bucket" "image-bucket" {
  name     = "wyly-brain-image-${terraform.workspace}"
  location = var.region
}

resource "google_storage_bucket_access_control" "publish-rule" {
  bucket = google_storage_bucket.image-bucket.name
  role   = "READER"
  entity = "allUsers"
}

output "url" {
  value = google_cloud_run_service.api_server.status[0].url
}
