# cloud-run-service-account
resource "google_service_account" "cloud-run-service-account" {
  account_id   = "cloud-run-service-account"
  display_name = "A service account for app on Cloud Run"
}

resource "google_project_iam_member" "cloud-run-agent-iam" {
  project = var.project_name
  role    = "roles/run.serviceAgent"
  member  = "serviceAccount:${google_service_account.cloud-run-service-account.email}"
}

# local-app-service-account
resource "google_service_account" "local-app-service-account" {
  account_id   = "local-app-service-account"
  display_name = "A service account for app on local"
}
resource "google_project_iam_member" "viewer-for-local-app-iam" {
  project = var.project_name
  role    = "roles/viewer"
  member  = "serviceAccount:${google_service_account.local-app-service-account.email}"
}
