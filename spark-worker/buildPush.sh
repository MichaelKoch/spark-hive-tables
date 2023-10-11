#/bin/bash
image=ghcr.io/michaelkoch/spark-worker
docker build . -t $image
docker push $image
