ARG SPARK_IMAGE=gcr.io/spark-operator/spark-py:v3.1.1-hadoop3
#ARG SPARK_IMAGE=ghcr.io/michaelkoch/spark-worker
FROM ${SPARK_IMAGE} AS build

# Switch to user root so we can add additional jars and configuration files.

USER root
RUN /usr/bin/python3 -m pip install --upgrade pip &&\ 
    pip install pyspark==3.1.1

ENTRYPOINT ["/opt/entrypoint.sh"]