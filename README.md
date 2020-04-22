[![Build Status](https://dev.azure.com/ali0995/demoProject/_apis/build/status/maati55.countries_app?branchName=master)](https://dev.azure.com/ali0995/demoProject/_build/latest?definitionId=1&branchName=master)

# Countries Service App

## to use this project?

### Setup

1. Clone this repo

1. Download [Docker](https://docs.docker.com/docker-for-mac/install/) (if necessary)

### Build and Run the App

#### Build the Containers

Build the images:

```sh
$ docker-compose build
```

Run the containers:

```sh
$ docker-compose up -d
```

Call the API:
```sh
curl -i -H "Accept: application/json" "http://0.0.0.0:8080/v1/countries?target=source"
curl -i -H "Accept: application/json" "http://0.0.0.0:8080/v1/countries?target=destinations"
```

#### UnitTest
For unit test (you might need to install requests module "pip install requests")
```sh
python tests/unit_test.py
```
#### Healthcheck
Can be used to check the Rest API Healthcheck
http://0.0.0.0:8080/healthcheck

### Task #3
#### Security:
- Secure endpoints using TLS/HTTPS - Keys can be impport from docker compose file
- Access Control - by defining role to the user/group to
- Using API Keys - it also reduce the impact of DOS attacks - it can be include to the request header
- Always input validation
- Defining HTTP return codes
- Using temporary security credentials by Vault

#### Monitoring:
- CloudWatch:
  -- Sending ECS container logs to CloudWatch
  -- Using CloudWatch to collect and processing raw which it can be use for metrics
- Amazon ECS supports container health checks
