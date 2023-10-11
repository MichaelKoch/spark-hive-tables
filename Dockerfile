
ARG SPARK_IMAGE=ghcr.io/michaelkoch/spark-worker
FROM ${SPARK_IMAGE} AS build
USER root
COPY /src /app
ENTRYPOINT ["/opt/entrypoint.sh"]