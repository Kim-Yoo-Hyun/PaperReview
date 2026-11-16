FROM ghcr.io/astral-sh/uv:0.8.22-python3.11-bookworm-slim@sha256:e59dc06793821e707e3a90234025c996eb4db2af807fdd7d9dd731d2fc678a96
LABEL paperreview.task="object-set-p0"
ENV DEBIAN_FRONTEND=noninteractive GIT_LFS_SKIP_SMUDGE=1 UV_LINK_MODE=copy \
    PYTHONDONTWRITEBYTECODE=1 MUJOCO_GL=egl PYOPENGL_PLATFORM=egl \
    NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility \
    OPENPI_DATA_HOME=/data/openpi-cache WANDB_MODE=disabled \
    XLA_PYTHON_CLIENT_PREALLOCATE=false
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates git git-lfs build-essential libgl1 libegl1 libglib2.0-0 libglvnd0 libgles2 libxrender1 libgomp1 \
    && rm -rf /var/lib/apt/lists/*
RUN git clone https://github.com/OpenMOSS/VLABench.git /opt/vlabench \
    && git -C /opt/vlabench checkout --detach cf588fe60c0c7282174fe979f5913170cfe69017 \
    && git clone https://github.com/Shiduo-zh/openpi.git /opt/openpi \
    && git -C /opt/openpi checkout --detach 4483d1da6332da44115fe530e4e6fdd89bd57b13 \
    && git clone https://github.com/motion-planning/rrt-algorithms.git /opt/rrt \
    && git -C /opt/rrt checkout --detach 7d3fb972bcc8a83b793d516d5953a42e3068dc09
RUN printf '%s\n' '97352549af74bc031ba9cbc9d91339841fead9163408a393bf15895daf2cdc51  /opt/openpi/uv.lock' | sha256sum -c -
COPY sim-requirements.in /recipe/sim-requirements.in
RUN uv python install 3.11.13 \
    && uv sync --project /opt/openpi --python 3.11.13 --frozen --no-dev \
    && uv venv --python 3.11.13 /opt/sim \
    && uv pip compile --python /opt/sim/bin/python /recipe/sim-requirements.in -o /recipe/sim-resolved.txt \
    && uv pip sync --python /opt/sim/bin/python /recipe/sim-resolved.txt \
    && uv pip install --python /opt/sim/bin/python --no-deps -e /opt/vlabench -e /opt/rrt -e /opt/openpi/packages/openpi-client \
    && uv cache clean
RUN mv /opt/vlabench/VLABench/assets /opt/base-assets \
    && ln -s /data/assets /opt/vlabench/VLABench/assets
COPY Dockerfile resume.sh RESUME_PLAN.json ARTIFACTS.json inside.py native_probe.py packet_checks.py /recipe/
RUN /opt/openpi/.venv/bin/python /recipe/packet_checks.py seal /recipe
WORKDIR /opt/openpi
ENTRYPOINT ["/opt/openpi/.venv/bin/python", "/recipe/inside.py"]
