# Web Application

This is web application of wyly.

## Requirement

- fvm 2.3~

## Setup development environment

### fvm and flutter

1. Install flutter by fvm: `fvm install`
2. Ensure that web is installed: `fvm flutter devices`
   - If "Chrome (web) • chrome • web-javascript" is showed, that OK

### env

1. Copy "assets/sample.env" to "assets/.env"
2. Set each values
   - values of Firebase is on Firebase console
   - Google Auth value is on [GCP console](https://console.cloud.google.com/apis/credentials)

## Run on local

Type just `make up` , then you can see app on Chrome.  
If you want to shutdown app, just close chrome window.

## Run test & lint

- test: `make test`
- lint: `make lint`

## Attention on maintenance

### update flutter version

1. Change version on `app-web/.fvm/fvm_config.json`
2. Change version on `.github/workflows/app-web-test.yaml`

### Attention on adding new authentication setting

Set allowed origin for each client IDs on GCP console.  
`make up` command use 7357 port, so you have to add <http://localhost:7357> to run at local.  
Refer <https://pub.dev/packages/google_sign_in_web>.
