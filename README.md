# certbot service

A script and Docker deployment for running a script for [certbot](https://certbot.eff.org/)
registrations and renewals.

## Usage

The [`bin/check.py`](bin/check.py) is a rudimentary script that wraps the
`certbot` command with a defined list of domains to request certificates for.
This is configured to use the [route53](https://certbot-dns-route53.readthedocs.io/en/stable/index.html) plugin for registrations.

### Configuration

AWS credentials should be passed as environment variables with permission to
maintain the verification records in route53.

In addition to the standard AWS credential environment variables, these
should be defined for configuring the script:

* __`DOMAINS`__

    List of domains to retrieve certs for. This is a semi-colon
    delimited list of certificate *sets* separated by spaces.  Whatever
    domains are separated by spaces will be a part of the same cert.  Each
    set separated by semi-colons is a unique certificate.

    _Example:_ `DOMAINS="home.jbeard.dev *.home.jbeard.dev;jbeard.dev *.jbeard.dev"`

* __`EMAIL`__

    E-mail address for Lets Encrypt

    _Example:_ `EMAIL="ssl@jbeard.dev"`

## Deployment

This is deployed to Docker Swarm using the
[`deploy/docker-compose.yml`](deploy/docker-compose.yml) file. The deployment
runs `crond` on the container with the [`deploy/crontab`](deploy/crontab)
to periodically run the [`bin/check.py`](bin/check.py) script.
