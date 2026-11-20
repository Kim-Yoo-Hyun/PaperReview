FROM python:3.12-slim-bookworm@sha256:935c3c5b12357a7e10caa9c1e6ca5692344d97cf229832ef584be2cec9fc03df

ENV PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1
RUN python -m pip install --no-cache-dir --only-binary=:all: \
        mujoco==3.3.7 numpy==2.2.6 absl-py==2.3.1 etils==1.13.0 glfw==2.10.0 \
        PyOpenGL==3.1.10 fsspec==2025.10.0 importlib-resources==6.5.2 \
        typing-extensions==4.15.0 zipp==3.23.0 \
    && python -m pip check
WORKDIR /pilot
COPY insertion.xml simulate.py wrist_observation.py relative_motion.py active_probe.py reference_transfer.py servo_response.py scan_range.py Dockerfile ./
ENTRYPOINT ["python", "scan_range.py"]
