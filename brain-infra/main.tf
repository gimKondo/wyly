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

resource "google_cloud_run_service" "api_server" {
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
  lifecycle {
    ignore_changes = [
      "template[0].spec[0].containers",
    ]
  }
}

resource "google_cloud_run_service_iam_member" "allUsers" {
  service  = google_cloud_run_service.api_server.name
  location = google_cloud_run_service.api_server.location
  role     = "roles/run.invoker"
  member   = "allUsers"
}

output "url" {
  value = google_cloud_run_service.api_server.status[0].url
}
