FROM python:3.11.14-slim-bookworm@sha256:65a93d69fa75478d554f4ad27c85c1e69fa184956261b4301ebaf6dbb0a3543d AS builder
ARG RVO_REV=c2c46ba8d59556aa10faf03479293236efea154d
RUN apt-get update && apt-get install -y --no-install-recommends build-essential cmake curl ca-certificates && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir Cython==0.29.37 setuptools==75.8.0 wheel==0.45.1
RUN curl -fsSL --retry 3 https://codeload.github.com/sybrenstuvel/Python-RVO2/tar.gz/${RVO_REV} -o /tmp/rvo.tar.gz \
    && mkdir /rvo /wheels /provenance \
    && sha256sum /tmp/rvo.tar.gz > /provenance/rvo_archive.sha256 \
    && tar -xzf /tmp/rvo.tar.gz --strip-components=1 -C /rvo \
    && cd /rvo && pip wheel --no-deps --no-build-isolation . -w /wheels \
    && cp LICENSE /provenance/RVO_LICENSE \
    && pip freeze > /provenance/build_python_packages.txt \
    && dpkg-query -W > /provenance/build_debian_packages.txt \
    && printf '%s\n' "${RVO_REV}" > /provenance/rvo_revision.txt

FROM python:3.11.14-slim-bookworm@sha256:65a93d69fa75478d554f4ad27c85c1e69fa184956261b4301ebaf6dbb0a3543d
LABEL org.openai.task="gap-p3-reactive-nav-contract"
RUN apt-get update && apt-get install -y --no-install-recommends libgomp1 && rm -rf /var/lib/apt/lists/*
COPY --from=builder /wheels /wheels
COPY --from=builder /provenance /opt/provenance
RUN pip install --no-cache-dir --no-index /wheels/*.whl && rm -rf /wheels \
    && pip freeze > /opt/provenance/runtime_python_packages.txt \
    && dpkg-query -W > /opt/provenance/runtime_debian_packages.txt
ENV PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
WORKDIR /app
CMD ["python", "-B", "check_contract.py", "--output", "/output"]
