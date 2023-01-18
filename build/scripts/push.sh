#!/usr/bin/env bash

set -e

docker push struckchure/stritter_aggregation_service:$@
docker push struckchure/stritter_aggregation_service:latest

docker push ghcr.io/struckchure/stritter_aggregation_service:$@
docker push ghcr.io/struckchure/stritter_aggregation_service:latest
