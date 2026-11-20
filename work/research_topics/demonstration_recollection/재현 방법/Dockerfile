FROM python:3.12-slim-bookworm@sha256:935c3c5b12357a7e10caa9c1e6ca5692344d97cf229832ef584be2cec9fc03df
ENV PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1
RUN python -m pip install --no-cache-dir --only-binary=:all: numpy==2.2.6 h5py==3.13.0 pyarrow==18.1.0 && python -m pip check
COPY audit_samples.py /audit_samples.py
ENTRYPOINT ["python", "/audit_samples.py"]
