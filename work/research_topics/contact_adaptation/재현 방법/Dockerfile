FROM python:3.12.12-slim-bookworm@sha256:2986c55feb36e6cae00fa1fefb454283e4b33f35e75ff8bdd123b134130be301
ARG PACKET_FINGERPRINT
LABEL paper.task="contact-p0" paper.contact.packet="${PACKET_FINGERPRINT}"
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 PIP_NO_CACHE_DIR=1
RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates libgomp1 && rm -rf /var/lib/apt/lists/*
RUN git init /opt/contactbench && cd /opt/contactbench && \
    git remote add origin https://github.com/Michaelwyx/contactbench-sim.git && \
    git fetch --depth=1 origin ccd864501275112e369a71c91880adf2da28b536 && git checkout --detach FETCH_HEAD && \
    test "$(git rev-parse HEAD)" = ccd864501275112e369a71c91880adf2da28b536
# Upstream pins four physics packages. Full transitive closure is captured at
# build time, not claimed prevalidated. No VLA, Torch or checkpoint installation.
RUN mkdir -p /opt/build && python -m pip install --report /opt/build/pip-install.json /opt/contactbench/packages/force-bench && \
    python -m pip check && python -m pip freeze --all > /opt/build/pip-freeze.txt && \
    dpkg-query -W > /opt/build/dpkg.txt
ENV TB_ASSETS_ROOT=/opt/contactbench/assets TB_OUT_ROOT=/results/upstream \
    NEWTON_CACHE_PATH=/cache/newton WARP_CACHE_PATH=/cache/warp \
    MPLCONFIGDIR=/cache/matplotlib TMPDIR=/cache/tmp \
    TB_STABILIZER=0 TB_GELSIGHT=0 TB_MULTIVIEW=0 TB_LOOK=studio \
    CONTACT_P0_DOCKER=1 NVIDIA_DRIVER_CAPABILITIES=compute,utility
WORKDIR /packet
ENTRYPOINT ["python", "-B", "/packet/probe.py"]
