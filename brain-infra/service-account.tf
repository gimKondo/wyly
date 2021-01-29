resource "google_service_account" "cloud-run-service-account" {
  account_id   = "cloud-run-service-account"
  display_name = "A service account for app on Cloud Run"
}

resource "google_project_iam_member" "cloud-run-agent-iam" {
  role   = "roles/run.serviceAgent"
  member = "serviceAccount:${google_service_account.cloud-run-service-account.email}"
}
