FROM ghcr.io/astral-sh/uv:0.8.22-python3.11-bookworm-slim@sha256:e59dc06793821e707e3a90234025c996eb4db2af807fdd7d9dd731d2fc678a96
LABEL paperreview.task="instruction-revision-p0"
ENV DEBIAN_FRONTEND=noninteractive GIT_LFS_SKIP_SMUDGE=1 \
    UV_LINK_MODE=copy PYTHONDONTWRITEBYTECODE=1 \
    MUJOCO_GL=egl PYOPENGL_PLATFORM=egl \
    NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility \
    JAX_PLATFORMS=cuda XLA_PYTHON_CLIENT_MEM_FRACTION=0.70 \
    OPENPI_DATA_HOME=/data/openpi-cache LIBERO_CONFIG_PATH=/tmp/libero \
    HF_HUB_OFFLINE=1 WANDB_MODE=disabled
RUN apt-get update && apt-get install -y --no-install-recommends \
      ca-certificates git git-lfs build-essential libgl1 libegl1 libglib2.0-0 libglvnd0 libgles2 \
    && rm -rf /var/lib/apt/lists/*
RUN git clone https://github.com/ChenZhenY/ReSteer.git /opt/resteer \
    && git -C /opt/resteer checkout --detach 7329c159319a346b7245a69c128e5d4940c0763b \
    && git -C /opt/resteer submodule update --init third_party/openpi \
    && test "$(git -C /opt/resteer/third_party/openpi rev-parse HEAD)" = 215abfb217dbac7d5f1273282331b9b1866c0479
RUN printf '%s\n' \
      '6aabb7b2d4b51de3d8a4af3d08ad9f792e9d8874e00f244430bc3e1bf37b9ec8  /opt/resteer/uv.lock' \
      '793488b5a55bb87200db90a61fd0af51922b686d94e1da4f4c587ab119b37d74  /opt/resteer/third_party/openpi/uv.lock' \
      | sha256sum -c -
RUN uv python install 3.10.18 3.11.13 \
    && uv sync --project /opt/resteer --python 3.10.18 --frozen --no-dev \
    && uv sync --project /opt/resteer/third_party/openpi --python 3.11.13 --frozen --no-dev \
    && uv cache clean
WORKDIR /opt/resteer
COPY RESUME_PLAN.json ARTIFACTS.json inside.py native_probe.py /recipe/
ENTRYPOINT ["/opt/resteer/third_party/openpi/.venv/bin/python", "/recipe/inside.py"]
