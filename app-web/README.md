# Web Application

This is web application of wyly.

## Requirement

- fvm 2.3~

## Setup development environment

1. Install flutter by fvm: `fvm install`
2. Ensure that web is installed: `fvm flutter devices`
   - If "Chrome (web) • chrome • web-javascript" is showed, that OK

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
