# Draft native recipe. No successful build/native qualification on the ARM64 host.
FROM nvidia/cuda@sha256:cff3a0d82d2c2b47bab252d67fa9b34a20ef4c50781d98501b5c7367ea9afd10
ARG PACKET_SHA
LABEL org.paperregistry.owner=paperregistry.langret-p0
LABEL org.paperregistry.langret.packet-sha=$PACKET_SHA
ENV DEBIAN_FRONTEND=noninteractive PYTHONDONTWRITEBYTECODE=1 \
    NVIDIA_DRIVER_CAPABILITIES=compute,utility,graphics ROBOT_PLATFORM=LIBERO \
    MUJOCO_GL=egl PYOPENGL_PLATFORM=egl EGL_DEVICE_ID=0 \
    HF_HOME=/cache/hf HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
    TOKENIZERS_PARALLELISM=false WANDB_MODE=disabled \
    LIBERO_CONFIG_PATH=/opt/langret/libero-config \
    PYTHONPATH=/opt/langret/packages:/opt/langret/VLA-CF \
    NUMBA_CACHE_DIR=/tmp/numba XDG_CACHE_HOME=/tmp/cache
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-dev build-essential git git-lfs ca-certificates \
    libegl1 libgl1 libgles2 libglvnd0 libglib2.0-0 libsm6 libxext6 libxrender1 libglfw3 \
    && rm -rf /var/lib/apt/lists/*
RUN python3 -c 'import sys; assert sys.version_info[:2] == (3, 10)'
COPY langret_requirements.txt /opt/langret/requirements.txt
RUN python3 -m pip install --no-cache-dir pip==24.0 setuptools==69.5.1 wheel==0.43.0 \
    && python3 -m pip install --no-cache-dir torch==2.4.0 torchvision==0.19.0 --index-url https://download.pytorch.org/whl/cu124 \
    && python3 -m pip install --no-cache-dir -r /opt/langret/requirements.txt
COPY langret_probe.py plan.json /opt/langret/packet/
# Source and simulator assets are installed only in Docker. No veRL training loop is imported.
RUN python3 /opt/langret/packet/langret_probe.py install-sources \
    && python3 -m pip install --no-cache-dir --no-deps /opt/langret/transformers \
    && python3 -m pip install --no-cache-dir --no-deps -e /opt/langret/VLA-CF \
    && python3 /opt/langret/packet/langret_probe.py configure \
    && python3 -m pip check \
    && python3 -c 'import torch, transformers, peft, libero.libero.envs; from langret_hf.modeling_prismatic import OpenVLAForActionPrediction; assert torch.version.cuda == "12.4"' \
    && python3 -m pip freeze --all > /opt/langret/resolved-packages.txt \
    && dpkg-query -W > /opt/langret/resolved-system-packages.txt
WORKDIR /opt/langret/packet

