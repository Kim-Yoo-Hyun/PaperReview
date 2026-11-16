# Draft native recipe; not built or qualified on the current ARM64 Mac.
# nvidia/cuda:12.1.0-runtime-ubuntu22.04, linux/amd64 manifest checked 2026-11-06.
FROM nvidia/cuda@sha256:a7d949f17fcdfcd56763aa66a7b91c17775a0e1e9d268421b53be3ae2d0e55af
ARG PACKET_SHA
LABEL org.paperregistry.unified.packet-sha=$PACKET_SHA
LABEL org.paperregistry.owner=paperregistry.unified-p0
ENV DEBIAN_FRONTEND=noninteractive PYTHONDONTWRITEBYTECODE=1 \
    NVIDIA_DRIVER_CAPABILITIES=compute,utility,graphics \
    MS_ASSET_DIR=/cache/assets HF_HOME=/cache/huggingface \
    HF_HUB_OFFLINE=1 TOKENIZERS_PARALLELISM=false WANDB_MODE=disabled \
    PYTHONPATH=/opt/unified/packages XDG_RUNTIME_DIR=/tmp
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-dev build-essential git git-lfs ca-certificates \
    libegl1 libgl1 libgles2 libglvnd0 libglib2.0-0 libsm6 libxext6 libxrender1 \
    libvulkan1 vulkan-tools libx11-6 libglfw3 \
    && rm -rf /var/lib/apt/lists/*
RUN python3 -c 'import sys; assert sys.version_info[:2] == (3, 10)'
COPY requirements.txt /opt/unified/requirements.txt
RUN python3 -m pip install --no-cache-dir pip==24.0 setuptools==69.5.1 wheel==0.43.0 \
    && python3 -m pip install --no-cache-dir torch==2.2.0 torchvision==0.17.0 --index-url https://download.pytorch.org/whl/cu121 \
    && python3 -m pip install --no-cache-dir -r /opt/unified/requirements.txt
RUN git lfs install --system \
    && git init /opt/unified/RL4VLA \
    && git -C /opt/unified/RL4VLA remote add origin https://github.com/gen-robot/RL4VLA.git \
    && git -C /opt/unified/RL4VLA fetch --depth=1 origin de46e0174e7ac310255a2836718fcefab28b8963 \
    && git -C /opt/unified/RL4VLA checkout --detach FETCH_HEAD \
    && test "$(git -C /opt/unified/RL4VLA rev-parse HEAD)" = de46e0174e7ac310255a2836718fcefab28b8963 \
    && git init /opt/unified/widowx \
    && git -C /opt/unified/widowx remote add origin https://github.com/haosulab/ManiSkill-WidowX250S.git \
    && git -C /opt/unified/widowx fetch --depth=1 origin 6a12bb745d964aab9fc897f0999cad53aa29000c \
    && git -C /opt/unified/widowx checkout --detach FETCH_HEAD \
    && test "$(git -C /opt/unified/widowx rev-parse HEAD)" = 6a12bb745d964aab9fc897f0999cad53aa29000c
# Standalone HF/PEFT probe: no upstream trainer/RLDS/TensorFlow/data pipeline imported.
RUN python3 -m pip install --no-cache-dir -e /opt/unified/RL4VLA/ManiSkill -e /opt/unified/RL4VLA/SimplerEnv \
    && python3 -m pip check \
    && mkdir -p /opt/unified/packages/unified_hf \
    && cp /opt/unified/RL4VLA/openvla/prismatic/extern/hf/configuration_prismatic.py /opt/unified/packages/unified_hf/ \
    && cp /opt/unified/RL4VLA/openvla/prismatic/extern/hf/modeling_prismatic.py /opt/unified/packages/unified_hf/ \
    && cp /opt/unified/RL4VLA/openvla/prismatic/extern/hf/processing_prismatic.py /opt/unified/packages/unified_hf/ \
    && touch /opt/unified/packages/unified_hf/__init__.py
COPY probe.py plan.json /opt/unified/packet/
RUN python3 /opt/unified/packet/probe.py verify-source \
    && python3 /opt/unified/packet/probe.py build-wheel
RUN python3 -m py_compile /opt/unified/packet/probe.py \
    && python3 -c 'from unified_hf.modeling_prismatic import OpenVLAForActionPredictionWithValueHead; from simpler_env.env.simpler_wrapper import SimlerWrapper; import peft, flash_attn, torch; assert torch.version.cuda == "12.1"' \
    && python3 -m pip check > /opt/unified/pip-check.txt \
    && python3 -m pip freeze --all > /opt/unified/resolved-packages.txt \
    && dpkg-query -W > /opt/unified/resolved-system-packages.txt
WORKDIR /opt/unified/packet
