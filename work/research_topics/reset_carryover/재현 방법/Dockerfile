FROM python:3.12-slim-bookworm@sha256:935c3c5b12357a7e10caa9c1e6ca5692344d97cf229832ef584be2cec9fc03df

ENV PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1
RUN python -m pip install --no-cache-dir --only-binary=:all: \
        mujoco==3.3.7 numpy==2.2.6 absl-py==2.3.1 etils==1.13.0 glfw==2.10.0 \
        PyOpenGL==3.1.10 fsspec==2025.10.0 importlib-resources==6.5.2 \
        typing-extensions==4.15.0 zipp==3.23.0 \
    && python -m pip check

WORKDIR /pilot
ADD --checksum=sha256:411d0acbc8aa4d331da4309021ca7a5fe5c59d6c22e66408101492e99c723679 https://raw.githubusercontent.com/ARISE-Initiative/robosuite/a071383d53568ab798eb315c0e95357911be922d/robosuite/models/assets/objects/door_lock.xml /pilot/door_lock.xml
COPY drawer.xml simulate.py door_probe.py Dockerfile ./
ENTRYPOINT ["python", "simulate.py"]
