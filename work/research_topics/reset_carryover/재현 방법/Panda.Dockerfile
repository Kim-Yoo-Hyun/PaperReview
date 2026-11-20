# The original MuJoCo 2.0 Linux binary is x86-64. Build with --platform linux/amd64.
FROM python:3.7.17-slim-bullseye@sha256:603879aeff06df23f0d392a19f7ce02aa85e14e6b4d25fd9647b116e0cb93467

ENV MUJOCO_PY_MUJOCO_PATH=/opt/mujoco200 \
    MUJOCO_PY_MJKEY_PATH=/opt/mujoco200/bin/mjkey.txt \
    MUJOCO_PY_FORCE_CPU=1 LD_LIBRARY_PATH=/opt/mujoco200/bin \
    PYTHONPATH=/opt/rlkit PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 \
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMBA_NUM_THREADS=1
RUN echo 'deb [check-valid-until=no] https://snapshot.debian.org/archive/debian/20240301T000000Z/ bullseye main' > /etc/apt/sources.list \
    && apt-get -o Acquire::Retries=2 update && apt-get -o Acquire::Retries=2 install -y --no-install-recommends \
    build-essential curl unzip patchelf libosmesa6-dev libgl1-mesa-dev libglfw3 libglew-dev \
    && rm -rf /var/lib/apt/lists/*

ADD --checksum=sha256:ba8560040f6ca47dbd89e4731bc9e06080a99eba4583cda95cdedca802389153 https://www.roboti.us/download/mujoco200_linux.zip /tmp/engine.zip
RUN unzip -q /tmp/engine.zip -d /opt && mv /opt/mujoco200_linux /opt/mujoco200 && rm /tmp/engine.zip
ADD --checksum=sha256:bffe403bce6978d329239c83e874e0fd412740d149834b8c051689ba4a9adecc https://www.roboti.us/file/mjkey.txt /opt/mujoco200/bin/mjkey.txt
RUN pip install --no-cache-dir \
    'setuptools==59.8.0' 'wheel==0.38.4' 'Cython==0.29.13' 'numpy==1.17.2' \
    'scipy==1.4.1' 'numba==0.49.1' 'llvmlite==0.32.1' 'cffi==1.15.1' \
    'glfw==1.12.0' 'imageio==2.9.0' 'fasteners==0.15' 'gtimer==1.0.0b5' \
    'gym==0.15.7' 'python-dateutil==2.8.1'
RUN pip install --no-cache-dir --no-build-isolation \
    'mujoco-py @ https://files.pythonhosted.org/packages/a2/30/21abd0cf2734bf5f34a7a8967789b12dee55f1e51e9c1c60af1cba549123/mujoco-py-2.0.2.9.tar.gz#sha256=6ae20ca9509203758f5e30a7a4019cb2d581b6d40dc2c2669dbe3229cfdf05e8' \
    'robosuite @ https://files.pythonhosted.org/packages/ec/7b/49a31db8fb7e5465e0961077951d2ae9d26eb97028bb61089e6de1e39807/robosuite-1.0.1-py3-none-any.whl#sha256=92d45d7ad57e6d8a63becc96d14a038e17ab1919c00d771a4bbb6e6fc7aa4810' \
    'torch @ https://download.pytorch.org/whl/cpu/torch-1.4.0%2Bcpu-cp37-cp37m-linux_x86_64.whl#sha256=5960a74eb6b396ee566ff3652bba3d45b0183a17399d0b62484d833ee2b47b82' \
    && python -c "import mujoco_py, robosuite, torch; print(mujoco_py.get_version(), torch.__version__)"
ARG RLKIT_COMMIT=d63dab7008cf4d5b6018db8da97b714718bf8a8a
ARG RLKIT_SHA256=6551f106a47046cea045df8ae5f1734b17d702928fb96070c7c2ff8d8abcee9d
ADD --checksum=sha256:${RLKIT_SHA256} https://codeload.github.com/rail-berkeley/rlkit/tar.gz/${RLKIT_COMMIT} /tmp/rlkit.tar.gz
RUN mkdir /opt/rlkit && tar -xzf /tmp/rlkit.tar.gz --strip-components=1 -C /opt/rlkit && rm /tmp/rlkit.tar.gz
ENV PANDA_RLKIT_COMMIT=${RLKIT_COMMIT}
RUN pip install --no-cache-dir 'h5py==2.10.0' \
    && python -c "from robosuite.wrappers import GymWrapper; from rlkit.torch.sac.policies import MakeDeterministic"

WORKDIR /panda
ARG BENCH=https://raw.githubusercontent.com/ARISE-Initiative/robosuite-benchmark/b229f7442f3590dd0e0cad21dc6ae52f410a34bc/runs
ADD --checksum=sha256:71c775ddb977eaf6a0d686fc3d156df5c4de12a6ba42cb67255d436acc0e0713 ${BENCH}/Door-Panda-OSC-POSE-SEED17/Door_Panda_OSC_POSE_SEED17_2020_09_13_00_26_44_0000--s-0/params.pkl /panda/17/params.pkl
ADD --checksum=sha256:eeb0f57046a17c5af184ad84527e2fa1f5e71d0d3415f7ef1ff64258eea4a053 ${BENCH}/Door-Panda-OSC-POSE-SEED17/Door_Panda_OSC_POSE_SEED17_2020_09_13_00_26_44_0000--s-0/variant.json /panda/17/variant.json
ADD --checksum=sha256:46931b453fab158a9bcee26291ee01b8f6f81ca651301a33785a1514b138d779 ${BENCH}/Door-Panda-OSC-POSE-SEED59/Door_Panda_OSC_POSE_SEED59_2020_09_13_00_26_44_0000--s-0/params.pkl /panda/59/params.pkl
ADD --checksum=sha256:3f511cea79294794b0675fff657965413eeb2c75983a78f39c67e4b91c5b1b1c ${BENCH}/Door-Panda-OSC-POSE-SEED59/Door_Panda_OSC_POSE_SEED59_2020_09_13_00_26_44_0000--s-0/variant.json /panda/59/variant.json
COPY panda_eval.py /panda/panda_eval.py
