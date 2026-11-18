# Unbuilt preparation recipe. All installation happens inside local Docker.
FROM rlinf/rlinf@sha256:e3952705e6d38d9b5cb6235aaf2661d5e4112ede95fdf61a69c46beb7d14cf3c
ARG PACKET_SHA
LABEL org.paperregistry.owner="relation-p0" org.paperregistry.packet=$PACKET_SHA
ENV PYTHONDONTWRITEBYTECODE=1 HF_HOME=/cache/huggingface \
    OPENPI_DATA_HOME=/cache/openpi JAX_PLATFORMS=cpu \
    XLA_PYTHON_CLIENT_PREALLOCATE=false TOKENIZERS_PARALLELISM=false \
    WANDB_MODE=disabled NVIDIA_DRIVER_CAPABILITIES=compute,utility,graphics \
    UV_DEFAULT_INDEX=https://pypi.org/simple/ HF_ENDPOINT=https://huggingface.co
SHELL ["/bin/bash", "-euo", "pipefail", "-c"]
RUN git init /opt/relation-src/openpi && \
    git -C /opt/relation-src/openpi remote add origin https://github.com/Physical-Intelligence/openpi.git && \
    GIT_LFS_SKIP_SMUDGE=1 git -C /opt/relation-src/openpi fetch --depth=1 origin 215abfb217dbac7d5f1273282331b9b1866c0479 && \
    git -C /opt/relation-src/openpi checkout --detach FETCH_HEAD && \
    git init /opt/relation-src/robotwin && \
    git -C /opt/relation-src/robotwin remote add origin https://github.com/RoboTwin-Platform/RoboTwin.git && \
    GIT_LFS_SKIP_SMUDGE=1 git -C /opt/relation-src/robotwin fetch --depth=1 origin dca9ec682688821c42944eacd7f5dd9bfb15396f && \
    git -C /opt/relation-src/robotwin checkout --detach FETCH_HEAD
# Keep the image's RoboTwin environment; build upstream OpenPI in another venv.
WORKDIR /opt/relation-src/openpi
RUN UV_PROJECT_ENVIRONMENT=/opt/relation-openpi GIT_LFS_SKIP_SMUDGE=1 \
    uv sync --frozen --no-dev --python 3.11 && \
    /opt/relation-openpi/bin/python -c 'import pathlib,shutil,transformers; shutil.copytree("src/openpi/models_pytorch/transformers_replace", pathlib.Path(transformers.__file__).parent, dirs_exist_ok=True)' && \
    uv pip check --python /opt/relation-openpi/bin/python && \
    test -x /opt/venv/openpi/bin/python
WORKDIR /opt/relation
COPY PLAN.json resume.py probe.py actor.py test_contract.py ./
RUN /opt/relation-openpi/bin/python -m py_compile probe.py actor.py test_contract.py && \
    /opt/relation-openpi/bin/python probe.py build-check && \
    /opt/venv/openpi/bin/python probe.py sim-import-check && \
    uv pip freeze --python /opt/relation-openpi/bin/python > actor-packages.txt && \
    uv pip freeze --python /opt/venv/openpi/bin/python > simulator-packages.txt && \
    dpkg-query -W > system-packages.txt
ENTRYPOINT []
CMD ["/opt/relation-openpi/bin/python", "/opt/relation/probe.py", "environment"]
