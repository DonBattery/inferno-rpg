#!/usr/bin/env bash

# this cript looks up the public DNS address of the Inferno RPG server on AWS
# and creates an Ansible Inventory with it.

set -Eeou pipefail

INSTANCE_NAME="inferno-rpg-server"

INSTANCE_PUBLIC_DNS=$(aws ec2 describe-instances \
  --filter "Name=tag:Name,Values=${INSTANCE_NAME}" \
  --query 'Reservations[].Instances[?State.Name==`running`].[PublicDnsName]' \
  --output json | jq -r '.[][] | select(length > 0) | .[0]')

echo "[${INSTANCE_NAME}]"
echo "${INSTANCE_PUBLIC_DNS} ansible_user=ubuntu"
