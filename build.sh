!/bin/bash
set -xe

docker build -t dor .

aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 058264363980.dkr.ecr.eu-central-1.amazonaws.com

docker tag dor:latest 058264363980.dkr.ecr.eu-central-1.amazonaws.com/devsecops-task:latest

docker push 058264363980.dkr.ecr.eu-central-1.amazonaws.com/devsecops-task:latest

echo 0;
