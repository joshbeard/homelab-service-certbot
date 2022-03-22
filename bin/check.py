#!/usr/bin/env python
# Lets Encrypt certbot script to request/renew certs for my home network.
# I'm using AWS Route53 for DNS and this uses the certbot route53 module for
# verification.
#
# These variables should be defined in the environment:
#  - DOMAINS: list of domains to retrieve certs for. This is a semi-colon
#            delimited list of certificate *sets* separated by spaces. Whatever
#            domains are separated by spaces will be a part of the same cert.
#            Each set separated by semi-colons is a unique certificate.
#        Example DOMAINS="home.jbeard.dev *.home.jbeard.dev;jbeard.dev *.jbeard.dev"
#
#  - EMAIL: e-mail address for Lets Encrypt
#        Example: EMAIL="ssl@jbeard.dev"
#
import os
import shlex
import subprocess

domains = os.environ.get('DOMAINS')
email   = os.environ.get('EMAIL')

domain_sets = domains.split(';')

def run_command(domain_set):
    command = [
      'certbot',
      'certonly',
      '-n',
      '--dns-route53',
      '--agree-tos',
      '--expand',
      '-m', email
    ]

    for d in domain_set.split(' '):
        command = command + ['-d', d]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(result.stdout)

for domain_set in domain_sets:
    print(f"== Checking domains {domain_set}")
    run_command(domain_set)


