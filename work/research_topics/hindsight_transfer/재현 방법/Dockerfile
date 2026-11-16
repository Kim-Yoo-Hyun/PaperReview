FROM rlinf/rlinf@sha256:b5563d95f681478555c4af63ca988b19d1a113306dbdee15a79fff47d320b5cb
ARG PACKET_SHA
LABEL org.paperregistry.owner="paperregistry.hindsight-p0"
LABEL org.paperregistry.hindsight.packet-sha=$PACKET_SHA
ENV HINDSIGHT_IMAGE_SHA=$PACKET_SHA
ENV PATH="/opt/venv/openvla-oft/bin:${PATH}"
ENV PYTHONPATH="/opt/hindsight/rlinf:/opt/hindsight/oft:/opt/hindsight/libero:/opt/hindsight/transformers/src"
ENV PYTHONDONTWRITEBYTECODE=1 MUJOCO_GL=egl PYOPENGL_PLATFORM=egl
ENV HF_HOME=/cache/huggingface LIBERO_CONFIG_PATH=/tmp/hindsight-libero
ENV TOKENIZERS_PARALLELISM=false CUBLAS_WORKSPACE_CONFIG=:4096:8
WORKDIR /opt/hindsight/packet
COPY plan.json probe.py resume.py ./
# Sources and all dependencies stay inside Docker. No mutable pip/apt resolution.
RUN /opt/venv/openvla-oft/bin/python probe.py source-build
ENTRYPOINT []
CMD ["/opt/venv/openvla-oft/bin/python", "probe.py", "p0"]
