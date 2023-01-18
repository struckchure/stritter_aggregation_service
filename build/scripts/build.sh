#!/usr/bin/env bash

set -e

docker build . -f build/python/Dockerfile -t struckchure/stritter_aggregation_service:$@
docker build . -f build/python/Dockerfile -t struckchure/stritter_aggregation_service:latest

docker build . -f build/python/Dockerfile -t ghcr.io/struckchure/stritter_aggregation_service:$@
docker build . -f build/python/Dockerfile -t ghcr.io/struckchure/stritter_aggregation_service:latest
