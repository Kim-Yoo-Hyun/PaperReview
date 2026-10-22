FROM python:3.12-slim-bookworm@sha256:34386ef0cb081344d7ec1c103ba398e6e9f64e9ab3a1509accc92a4e24a07258
ENV DEBIAN_FRONTEND=noninteractive \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    MUJOCO_GL=osmesa \
    PYOPENGL_PLATFORM=osmesa \
    HF_HOME=/artifacts/hf \
    PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y --no-install-recommends \
    libosmesa6 libgl1 libglib2.0-0 ffmpeg git build-essential ca-certificates \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir --index-url https://download.pytorch.org/whl/cpu \
    torch==2.11.0+cpu torchvision==0.26.0+cpu
RUN pip install --no-cache-dir cmake==3.31.10
ENV PATH="/usr/local/lib/python3.12/site-packages/cmake/data/bin:${PATH}"
RUN pip install --no-cache-dir hf-egl-probe==1.0.2 egl-probe==1.0.2
RUN pip install --no-cache-dir mujoco==3.3.2 \
    'hf-libero @ https://github.com/huggingface/LIBERO/archive/8561c60eea2fb93096146f240194649df73d8b1e.tar.gz' \
    'lerobot[smolvla,libero] @ https://github.com/huggingface/lerobot/archive/7e241bd630a3719a56157a497ce5d08f244784f1.tar.gz'
WORKDIR /probe
CMD ["python", "/probe/native_probe.py"]
