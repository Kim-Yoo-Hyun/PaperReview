FROM python:3.11.14-slim-bookworm@sha256:65a93d69fa75478d554f4ad27c85c1e69fa184956261b4301ebaf6dbb0a3543d
LABEL org.openai.task="gap-codec1-20261103"
ENV PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 TOKENIZERS_PARALLELISM=false
COPY requirements.lock /requirements.lock
RUN pip install --no-cache-dir -r /requirements.lock \
    && pip freeze > /python-packages.txt
WORKDIR /app
ENTRYPOINT ["python", "-B", "/app/probe.py"]
