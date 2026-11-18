FROM pytorch/pytorch:2.5.1-cuda12.4-cudnn9-runtime@sha256:c8268a92a69bd500f8be0e665b2630ee006dadaf7bfbc24249141b15ff622755
LABEL paperreview.topic="pose-active-p0"
ENV DEBIAN_FRONTEND=noninteractive PIP_DISABLE_PIP_VERSION_CHECK=1 \
    MUJOCO_GL=egl PYOPENGL_PLATFORM=egl NVIDIA_DRIVER_CAPABILITIES=compute,utility,graphics \
    HF_HOME=/cache/hf TORCH_HOME=/cache/torch MPLCONFIGDIR=/cache/mpl \
    PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 POSE_ACTIVE_CONTAINER=1
RUN apt-get update && apt-get install -y --no-install-recommends \
    git ca-certificates libegl1 libgl1 libgles2 libglib2.0-0 libglvnd0 \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /opt/pose/requirements.txt
RUN python -m pip install --no-cache-dir -r /opt/pose/requirements.txt \
    && git clone https://github.com/ARISE-Initiative/robosuite.git /opt/robosuite \
    && git -C /opt/robosuite checkout --detach 5ce6643f3092639d08f7b0f90ed1c6a84f50552c \
    && python -m pip install --no-cache-dir --no-deps /opt/robosuite \
    && python -m pip check \
    && python -m pip freeze > /opt/pose/packages.txt \
    && dpkg-query -W > /opt/pose/system-packages.txt
WORKDIR /opt/pose
COPY PLAN.json probe.py checks.py ./
RUN python -m py_compile probe.py checks.py
ENTRYPOINT []
CMD ["python", "/opt/pose/probe.py", "environment", "--output", "/out"]
