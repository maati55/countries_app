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

#### Sanity Check

#### Healthcheck
Can be used to check the Rest API Healthcheck
http://0.0.0.0:8080/healthcheck

### Task #3
#### Security:
1- Secure endpoints using TLS/HTTPS - Keys can be impport from docker compose file
2- Access Control - by defining role to the user/group to
3- Using API Keys - it also reduce the impact of DOS attacks - it can be include to the request header
4- Always input validation
5- Defining HTTP return codes
6- Using temporary security credentials by Vault

#### Monitoring:
- CloudWatch:
  -- Sending ECS container logs to CloudWatch
  -- Using CloudWatch to collect and processing raw which it can be use for metrics
- Amazon ECS supports container health checks
