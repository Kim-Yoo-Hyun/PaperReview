# Candidate recipe: build/import/CUDA/EGL/native qualification remains pending.
# Official nvidia/cuda:12.4.0-runtime-ubuntu22.04 linux/amd64 manifest, checked 2026-11-05.
FROM nvidia/cuda@sha256:2d205a50fefc321aca51a1d3aa46fb9a633dd2509a10e28c8bd34a6cb2027619
ARG VRL_PACKET_SHA
ARG VRL_SOURCE_SHA=7c51662df27b586f9e8a1ab35fcf849f2b8852f9
ARG LIBERO_SOURCE_SHA=8f1084e3132a39270c3a13ebe37270a43ece2a01
LABEL org.paperregistry.vrl.packet-sha=$VRL_PACKET_SHA
ENV DEBIAN_FRONTEND=noninteractive ROBOT_PLATFORM=LIBERO MUJOCO_GL=egl \
    PYOPENGL_PLATFORM=egl NVIDIA_DRIVER_CAPABILITIES=compute,utility,graphics \
    WANDB_MODE=disabled HF_HOME=/cache/huggingface LIBERO_CONFIG_PATH=/tmp/libero \
    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/opt/vrl/packages:/opt/vrl/LIBERO
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-dev git ca-certificates build-essential \
    libegl1 libgl1 libgles2 libglvnd0 libglib2.0-0 libsm6 libxext6 libxrender1 \
    && rm -rf /var/lib/apt/lists/*
RUN python3 -c 'import sys; assert sys.version_info[:2] == (3, 10)'
COPY requirements.txt /opt/vrl/requirements.txt
RUN python3 -m pip install --no-cache-dir pip==24.0 setuptools==69.5.1 wheel==0.43.0 \
    && python3 -m pip install --no-cache-dir torch==2.4.0 torchvision==0.19.0 --index-url https://download.pytorch.org/whl/cu124 \
    && python3 -m pip install --no-cache-dir -r /opt/vrl/requirements.txt \
    && python3 -m pip check
# Checkouts and all dependencies remain inside the image; no host payload installation.
RUN git init /opt/vrl/SimpleVLA-RL \
    && git -C /opt/vrl/SimpleVLA-RL remote add origin https://github.com/PRIME-RL/SimpleVLA-RL.git \
    && git -C /opt/vrl/SimpleVLA-RL fetch --depth=1 origin "$VRL_SOURCE_SHA" \
    && git -C /opt/vrl/SimpleVLA-RL checkout --detach FETCH_HEAD \
    && test "$(git -C /opt/vrl/SimpleVLA-RL rev-parse HEAD)" = "$VRL_SOURCE_SHA" \
    && git init /opt/vrl/LIBERO \
    && git -C /opt/vrl/LIBERO remote add origin https://github.com/Lifelong-Robot-Learning/LIBERO.git \
    && git -C /opt/vrl/LIBERO fetch --depth=1 origin "$LIBERO_SOURCE_SHA" \
    && git -C /opt/vrl/LIBERO checkout --detach FETCH_HEAD \
    && test "$(git -C /opt/vrl/LIBERO rev-parse HEAD)" = "$LIBERO_SOURCE_SHA"
# Standalone local-relative imports avoid importing the distributed veRL training stack.
RUN mkdir -p /opt/vrl/packages \
    && cp -r /opt/vrl/SimpleVLA-RL/verl/utils/vla_utils/openvla_oft /opt/vrl/packages/openvla_oft
COPY native_p0.py /opt/vrl/native_p0.py
RUN python3 -m py_compile /opt/vrl/native_p0.py \
    && python3 -c 'import torch, tensorflow; from openvla_oft.modeling_prismatic import OpenVLAForActionPrediction; from openvla_oft.processing_prismatic import PrismaticProcessor; assert torch.version.cuda == "12.4"' \
    && python3 -m pip freeze --all > /opt/vrl/resolved-packages.txt \
    && dpkg-query -W > /opt/vrl/resolved-system-packages.txt
WORKDIR /workspace
