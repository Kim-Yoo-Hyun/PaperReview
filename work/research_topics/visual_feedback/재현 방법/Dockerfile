# Draft native recipe; not built or qualified on the current ARM64 Mac.
# nvidia/cuda:12.1.0-runtime-ubuntu22.04, linux/amd64 manifest checked 2026-11-06.
FROM nvidia/cuda@sha256:a7d949f17fcdfcd56763aa66a7b91c17775a0e1e9d268421b53be3ae2d0e55af
ARG PACKET_SHA
LABEL org.paperregistry.feedback.packet-sha=$PACKET_SHA
ENV DEBIAN_FRONTEND=noninteractive PYTHONDONTWRITEBYTECODE=1 \
    NVIDIA_DRIVER_CAPABILITIES=compute,utility,graphics \
    MS_ASSET_DIR=/cache/assets HF_HOME=/cache/huggingface \
    HF_HUB_OFFLINE=1 TOKENIZERS_PARALLELISM=false WANDB_MODE=disabled \
    PYTHONPATH=/opt/feedback/packages XDG_RUNTIME_DIR=/tmp
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-dev build-essential git git-lfs ca-certificates \
    libegl1 libgl1 libgles2 libglvnd0 libglib2.0-0 libsm6 libxext6 libxrender1 \
    libvulkan1 vulkan-tools libx11-6 libglfw3 \
    && rm -rf /var/lib/apt/lists/*
RUN python3 -c 'import sys; assert sys.version_info[:2] == (3, 10)'
COPY requirements.txt /opt/feedback/requirements.txt
RUN python3 -m pip install --no-cache-dir pip==24.0 setuptools==69.5.1 wheel==0.43.0 \
    && python3 -m pip install --no-cache-dir torch==2.2.0 torchvision==0.17.0 --index-url https://download.pytorch.org/whl/cu121 \
    && python3 -m pip install --no-cache-dir -r /opt/feedback/requirements.txt
RUN git lfs install --system \
    && git init /opt/feedback/RL4VLA \
    && git -C /opt/feedback/RL4VLA remote add origin https://github.com/gen-robot/RL4VLA.git \
    && git -C /opt/feedback/RL4VLA fetch --depth=1 origin de46e0174e7ac310255a2836718fcefab28b8963 \
    && git -C /opt/feedback/RL4VLA checkout --detach FETCH_HEAD \
    && test "$(git -C /opt/feedback/RL4VLA rev-parse HEAD)" = de46e0174e7ac310255a2836718fcefab28b8963 \
    && git init /opt/feedback/widowx \
    && git -C /opt/feedback/widowx remote add origin https://github.com/haosulab/ManiSkill-WidowX250S.git \
    && git -C /opt/feedback/widowx fetch --depth=1 origin 6a12bb745d964aab9fc897f0999cad53aa29000c \
    && git -C /opt/feedback/widowx checkout --detach FETCH_HEAD \
    && test "$(git -C /opt/feedback/widowx rev-parse HEAD)" = 6a12bb745d964aab9fc897f0999cad53aa29000c
# Install the vendored simulator. Inference does not require the full OpenVLA training/data stack.
RUN python3 -m pip install --no-cache-dir -e /opt/feedback/RL4VLA/ManiSkill -e /opt/feedback/RL4VLA/SimplerEnv \
    && python3 -m pip check \
    && mkdir -p /opt/feedback/packages/feedback_hf \
    && cp /opt/feedback/RL4VLA/openvla/prismatic/extern/hf/configuration_prismatic.py /opt/feedback/packages/feedback_hf/ \
    && cp /opt/feedback/RL4VLA/openvla/prismatic/extern/hf/modeling_prismatic.py /opt/feedback/packages/feedback_hf/ \
    && cp /opt/feedback/RL4VLA/openvla/prismatic/extern/hf/processing_prismatic.py /opt/feedback/packages/feedback_hf/ \
    && touch /opt/feedback/packages/feedback_hf/__init__.py
COPY probe.py RESUME_PLAN.json /opt/feedback/packet/
RUN python3 -m py_compile /opt/feedback/packet/probe.py \
    && python3 -c 'from feedback_hf.modeling_prismatic import OpenVLAForActionPredictionWithValueHead; from simpler_env.env.simpler_wrapper import SimlerWrapper; import torch; assert torch.version.cuda == "12.1"' \
    && python3 -m pip freeze --all > /opt/feedback/resolved-packages.txt \
    && dpkg-query -W > /opt/feedback/resolved-system-packages.txt
WORKDIR /opt/feedback/packet
