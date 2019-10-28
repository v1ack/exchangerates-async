#!/bin/bash

docker-compose -p school-ci -f docker-compose.tests.yml rm -fsv
docker-compose -p school-ci -f docker-compose.tests.yml build --pull
docker-compose -p school-ci -f docker-compose.tests.yml up --remove-orphans --exit-code-from=tests tests
docker-compose -p school-ci -f docker-compose.tests.yml rm -fsv
