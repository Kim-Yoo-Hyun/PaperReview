FROM python:3.11-slim@sha256:e88e9763f943ec1834f992a4b51e0f24500486803e8bc534e5767af9ea65f6ce
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 OPENBLAS_NUM_THREADS=1
COPY requirements.txt /opt/requirements.txt
RUN python -m pip install --no-cache-dir --only-binary=:all: --require-hashes -r /opt/requirements.txt
COPY replay_c3.py test_replay.py /opt/replay/
WORKDIR /opt/replay
ENTRYPOINT ["python", "/opt/replay/replay_c3.py"]
