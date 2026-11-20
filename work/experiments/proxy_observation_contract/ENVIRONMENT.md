# 관측 검증 환경

- 확인: 2026-10-25 KST. **환경 조사·설정 문서화 완료, native 실행 미완료.** 현재 상태는 `WAITING_RESOURCE`, 전체 N3는 `PARTIAL`이다.
- 목적: 수정한 VideoUnmask의 고정 장면 1개×색 permutation 3개를 실제 simulator에서 확인한다. VLA inference·학습·72 episode 수집은 이번 환경 구성 범위가 아니다.
- [구조화한 설정·source hash·확인 상태](./ENVIRONMENT_PROFILE.json) · [동결 계약](./PROTOCOL.json) · [기존 patch](./results/verified/source_repair.patch) · [현재 TODO](../../../TODO.md).
- 아래 명령은 **적합한 로컬 Linux 컴퓨터에서 재개할 때의 예시이며 이번에 실행하지 않았다.** Native image/launcher는 아직 만들어 검증하지 않았다. 이번에는 host 설정·package·Docker image를 변경하지 않았다.

## 1. 현재 컴퓨터와 필요한 실행 경로

현재 읽기 전용 확인값은 macOS 27.0.1/arm64, Docker `desktop-linux`/Linux aarch64, Engine 28.3.3, 10 CPU, Docker 메모리 8,218,034,176 bytes다. 앞선 [실제 GPU 할당 probe](./results/verified/runtime_check.json)는 exit 125로 실패했다. 이번에는 같은 실패 probe를 반복하지 않았고 Docker 설정 변화도 확인되지 않았다.

Docker Desktop의 Linux container용 `--gpus` passthrough는 공식 문서상 Windows WSL2 경로다. 따라서 현재 Mac의 Docker 메모리 증설이나 `--platform linux/amd64` 에뮬레이션만으로 NVIDIA CUDA/Vulkan GPU가 생기지 않는다. Docker Model Runner의 다른 플랫폼 가속은 이 simulator의 GPU passthrough와 구분한다. [Docker GPU 문서](https://docs.docker.com/desktop/features/gpu/)

**이번 재개의 기준 환경은 사용자 선택 물리 컴퓨터의 Linux x86_64 + NVIDIA GPU + Docker Engine이다.** ManiSkill은 Linux/NVIDIA에서 simulation과 rendering을 지원하며, Docker 안에서는 GUI 대신 headless 영상 저장을 사용할 수 있다. Windows/WSL에서 CUDA probe가 성공하더라도 같은 RGB 환경이 보장되지는 않는다. ManiSkill 현재 문서는 WSL rendering을 지원 표에서 제외하고 있어 이 경로를 기본값으로 제시하지 않는다. [ManiSkill 설치·지원 표](https://maniskill.readthedocs.io/en/latest/user_guide/getting_started/installation.html), [Docker 안내](https://maniskill.readthedocs.io/en/latest/user_guide/getting_started/docker.html)

| 단계 | 환경 | 검증 상태 |
|---|---|---|
| N3-A 계약 검사 재실행 | 기존 digest 고정 Python 3.11.14 Docker, 2 CPU·512 MiB | ARM64에서 17/17 PASS; [기존 명령](./README.md#다른-컴퓨터에서-재실행) 사용 |
| N3-B native fixture | 아래 CUDA/Vulkan simulator 환경, GPU 1개·env 1개씩 순차 실행 | Image build·renderer·reset·관측 일치 모두 미실행 |
| 향후 VLA 서버·학습 | 별도 policy 환경·checkpoint/normalizer·VRAM qualification | HOLD. N3-B에 모델·학습 데이터 다운로드 불필요 |

## 2. Host와 container의 역할

| 항목 | 기준 설정 | 근거/확인 수준 |
|---|---|---|
| Host OS/architecture | Ubuntu 24.04 LTS x86_64를 구성 기준으로 선택 | Docker 공식 지원 OS. 정확히 이 OS만 가능한 것은 아니며 22.04도 Docker 지원 대상. 우리 native 실행은 아직 없음. [Docker Ubuntu](https://docs.docker.com/engine/install/ubuntu/) |
| GPU | NVIDIA CUDA 및 Vulkan graphics를 사용할 수 있는 GPU 1개 | GPU 이름/UUID·VRAM·Vulkan physical device를 실제 머신에서 기록. CUDA compute 전용 사용 가능 여부만으로 rendering을 판정하지 않음 |
| NVIDIA host driver | 설치한 GPU와 CUDA 12.8에 맞는 지원 driver | CUDA 12.8 GA release의 Linux driver 기준은 570.86.10. RoboMME README 저자 환경은 570.211.01/Vulkan 1.3.275. 이 숫자를 모든 GPU의 유일한 버전으로 강제하지 않음 |
| Docker Engine / NVIDIA Container Toolkit | GPU injection이 구성된 Engine, 실제 설치 버전 기록 | Toolkit은 host driver/library를 container에 노출하는 인프라. `nvidia-ctk` 설정과 driver를 container 내부 설치만으로 대체할 수 없음 |
| RAM/CPU/storage 준비 | Host RAM 32 GiB·free disk 40 GiB를 준비 예산으로 제안; 첫 container 4 CPU·8 GiB·shared memory 1 GiB | **저장소의 임시 운영 예산이며 공식 최소 사양·실측 peak가 아님.** OOM/시간 초과 시 결과와 함께 재설정 |
| VRAM | 최소값 미확정 | N3-B peak VRAM을 먼저 기록한다. VLA 학습용 VRAM을 이 표로 추정하지 않음 |

Driver 값은 [CUDA 12.8 release notes](https://docs.nvidia.com/cuda/archive/12.8.0/cuda-toolkit-release-notes/index.html)와 [고정 RoboMME README의 저자 환경](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/readme.md#L146)에서 확인했다. CUDA 12.x의 제한적인 minor compatibility 하한을 Vulkan·PyTorch·새 GPU까지 통과하는 전체 환경의 최소값으로 쓰지 않는다. [CUDA compatibility의 제한](https://docs.nvidia.com/deploy/cuda-compatibility/minor-version-compatibility.html)

**Host 무설치 정책:** 이 저장소에서는 Python·Torch·SAPIEN·학습 dependency를 host에 설치하지 않는다. Docker/driver/toolkit이 이미 갖춰진 컴퓨터를 사용하면 이 정책을 유지할 수 있다. 이 host 인프라까지 없다면 별도 시스템 준비가 필요하며, 이번 문서화 작업에서 설치하거나 daemon을 재시작하지 않았다. 설치·설정의 공식 근거는 [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)이다. Host CUDA Toolkit 전체나 host conda 환경은 요구하지 않는다.

## 3. N3-B simulator의 source와 package 설정

공식 저자 repository의 **고정 revision**에 있는 [Dockerfile](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/Dockerfile), [pyproject](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/pyproject.toml), [uv.lock](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/uv.lock)을 기준으로 한다. 일반 최신 ManiSkill로 바꾸거나 `pip install --upgrade`로 새 조합을 만들지 않는다.

| 설정 | 고정 source에서 확인한 값 |
|---|---|
| RoboMME benchmark commit | `1babf64480e28320e0f9db7992554616ceefda0e` + N3-A patch |
| Container base tag | `nvidia/cuda:12.8.0-cudnn-runtime-ubuntu24.04` |
| Python / uv | Python `3.11`, uv image tag `0.8.17` |
| 설치 경로 | `/app/.venv`, `PYTHONPATH=/app/src` |
| 설치 방식 | Docker build 안에서 `uv sync --frozen --no-dev --group server --python 3.11`; upstream의 project 설치 전후 단계 보존 |
| ManiSkill | 저자 fork `YinpeiDai/ManiSkill`, commit `07be6fbc66350ddca200abfb0a11b692f078f7fd`, lock version `3.0.0b21` |
| SAPIEN / motion planner | `sapien==3.0.2`, `mplib==0.1.1` |
| Torch / torchvision | `2.9.1` / `0.24.1` |
| NumPy / Gymnasium | `1.26.4` / `0.29.1` |
| h5py / trimesh | `3.15.1` / `4.11.2` |
| CUDA Python dependency / cuDNN | lock에 `nvidia-cuda-runtime-cu12==12.8.90`, `nvidia-cudnn-cu12==9.10.2.21` |
| Container OS library | upstream Dockerfile의 Vulkan/EGL/GL·ffmpeg·build 도구 사용. 특히 `libvulkan1`, `vulkan-tools`, `libegl1`, `libgl1` 확인 |

Lock의 SAPIEN 3.0.2 Linux wheel은 x86_64다. 현재 ARM64 contract image에서 package 이름만 추가해 같은 native 환경이 된다고 보지 않는다. 위 표는 metadata/lock 확인이며 실제 설치 성공 결과가 아니다.

**아직 완전히 고정되지 않은 것:** upstream CUDA/uv image는 digest가 아닌 tag이며 apt package와 Python patch version도 완전한 artifact lock이 아니다. Native build 시 base/uv의 resolved digest, 최종 image ID, 실제 Python/package list, driver/Vulkan 값, N3 patch SHA256를 결과 manifest에 저장해야 한다. 현재 `native_image_digest=null`, `build_verified=false`다. Lock version만으로 binary 호환성을 보증하지 않는다.

## 4. Docker 실행 설정값

| 항목 | N3-B 제안값 | 주의할 구분 |
|---|---|---|
| Platform | `linux/amd64` | 해당 물리 Linux host에서 사용. Mac 에뮬레이션을 GPU 대체로 쓰지 않음 |
| GPU 선택 | `--gpus device=0` 또는 확인된 GPU UUID | 선택한 GPU만 노출하고 runtime 기록에 UUID 저장 |
| Driver capabilities | `NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility,video` | compute/utility만으로 Vulkan graphics가 준비됐다고 볼 수 없음. [NVIDIA capabilities](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/docker-specialized.html#driver-capabilities) |
| Renderer | `SAPIEN_RENDER_DEVICE=cuda` | 저자 Dockerfile 값. 실제 선택 device·RGB 출력을 확인해야 함 |
| XDG runtime | `XDG_RUNTIME_DIR=/tmp/runtime-root` | Container 내부 writable directory, 실행 UID 소유·mode 0700 확인 |
| Threads/resources | `--cpus 4 --memory 8g --shm-size 1g`; `OMP_NUM_THREADS=1` | 첫 qualification의 미검증 운영 제한; 성능 baseline이나 최소 사양 아님 |
| GUI | `gui_render=False`, `render_mode=rgb_array`; `DISPLAY` 설정 불필요 | X11/GUI 대신 RGB array·파일 저장. GUI 성공 여부로 headless를 대체하지 않음 |
| Asset cache | `MS_ASSET_DIR=/assets` | 사용자 선택 로컬 Docker volume 사용. 필요한 asset만 준비하고 version/hash 기록 |
| Registry mount | `/workspace/paper_registry:ro` | `/app`에 registry를 덮어 mount하면 설치된 source/venv를 가릴 수 있음 |
| Output | 새 `/runs` directory/volume | 기존 `results/verified`를 덮어쓰지 않음. 큰 raw 결과·cache는 registry commit에서 제외 |
| Network/ports | Build/asset 준비 때만 다운로드; fixture 실행은 준비 후 network none 가능, 공개 port 없음 | VLA WebSocket 서버를 아직 실행하지 않음 |

Benchmark README에는 `SAPIEN_RENDER_DEVICE=cpu`/`MUJOCO_GL=osmesa` 대안도 적혀 있다. 그러나 이 조합이 현재 Mac Docker의 SAPIEN RGB/physics 계약을 만족한다는 증거는 없다. 단순 환경 변수 변경을 검증된 우회로로 사용하지 않는다. Native launcher, asset 준비 및 fixture 출력 collector는 아직 미구현이다.

## 5. 재개 시 확인 순서와 명령 예시

**선행 작업:** 적합한 local host에서 pinned benchmark source를 Docker build 내부에 확보하고 N3-A patch를 적용한다. `uv.lock`/fork commit을 보존해 native image를 만든 뒤 실제 digest를 기록한다. 현재 있는 `run_contract.sh`는 source/합성 계약 검사 전용이다. `scripts/run_example.py`를 실행했다고 N3-B의 세 paired fixture를 검증한 것으로 기록하지 않는다.

아래 예시는 **향후 만든 native image**에 대한 진단이며, 미구현 native launcher의 실행 명령이 아니다. Shell variable에 실제 immutable image ID/digest를 넣기 전에는 진행하지 않는다.

```sh
# 사용자 선택 Linux GPU 컴퓨터에서만 실행. 값이 없으면 중단한다.
: "${N3_NATIVE_IMAGE:?Set the built native image ID or digest first}"

docker run --rm --gpus device=0 \
  -e NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility,video \
  "$N3_NATIVE_IMAGE" nvidia-smi

docker run --rm --gpus device=0 \
  -e NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility,video \
  "$N3_NATIVE_IMAGE" vulkaninfo --summary

docker run --rm -i --gpus device=0 \
  -e NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility,video \
  "$N3_NATIVE_IMAGE" /app/.venv/bin/python - <<'PY'
import importlib.metadata as md
import torch
for name in ('mani-skill', 'sapien', 'mplib', 'torch', 'torchvision', 'numpy'):
    print(name, md.version(name))
print('torch_cuda_build', torch.version.cuda)
assert torch.cuda.is_available(), 'CUDA unavailable'
print('selected_gpu', torch.cuda.get_device_name(0))
x = torch.ones(1, device='cuda:0')
assert x.sum().item() == 1
PY
```

| Gate | 저장해야 할 실제 증거 | 실패 시 |
|---|---|---|
| E0 Host/container GPU | Host/Engine/Toolkit/driver, GPU UUID/VRAM, image digest, container `nvidia-smi` | Package 대량 설치나 rollout 전 중단 |
| E1 Vulkan + CUDA | `vulkaninfo`의 실제 NVIDIA device, import/version·CUDA operation 결과 | Compute 성공만으로 renderer PASS 처리하지 않음 |
| E2 Native reset/render | Patched VideoUnmask import/reset, 실제 front/wrist RGB shape/dtype, robot state, control/sim rate, peak RAM/VRAM | Native 실패 로그 보존; source/mock로 대체하지 않음 |
| E3 Paired fixture | 고정 seed/scene의 permutation 3개, demo 끝과 첫 policy decision의 시간, RGB/proprio/pose hash와 수치 비교, 목표 연결 | 관측 누설/장면 불일치 시 fixture 수정 또는 기각 |
| E4 다음 연결 | 실제 HDF5 ID join·action offset·feature/model tensor·checkpoint/normalizer 계약 | 별도 후속 작업. N3-B 통과만으로 학습 시작 안 함 |

E2/E3의 collector와 허용 수치 오차·종료 기준은 native 실행 전에 별도로 동결해야 한다. 서로 다른 목표를 가진 구성에서 RGB가 비슷하다는 육안 판단만으로 observation equality를 통과시키지 않는다. 이번에 확정한 fixture 값은 `VideoUnmask`, `easy`, `panda_wristcam`, `pd_joint_pos`, joint-angle action, seed `21000`, 고정 목표 `red`, permutation `[0,1,2]`, `[1,2,0]`, `[2,0,1]`, group `n3-dev-scene-21000-v1`, split `qualification_dev`다. 자세한 [planned 설정](./results/verified/fixture_plan.json)은 실제 수집 episode가 아니다. Actual control/sim frequency·camera config·backend는 source/default를 기록한 뒤 실행 manifest에서 고정하며 임의로 20 Hz 등을 가정하지 않는다.

## 6. 향후 VLA 환경은 별도로 준비

Policy commit은 `ac846a9a4aec841e483b1dc5d620dfe426bde853`다. [저자 policy pyproject](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/pyproject.toml)는 Python `>=3.11,<=3.12`, JAX CUDA12 `0.5.3`, Flax `0.10.2`, Torch `2.7.1`, Transformers `4.53.2`를 선언한다. 이는 위 simulator의 Torch `2.9.1`과 같은 venv에 합칠 목록이 아니다. [저자 README](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/README.md#L50)도 simulator와 policy를 분리하고 WebSocket으로 연결한다.

[Policy Dockerfile](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/Dockerfile#L49)은 uv 환경 외에 micromamba 평가 환경을 만들지만 `micromamba latest`와 평가 requirements의 [ManiSkill `@dev`](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/examples/robomme/requirements.txt)가 포함되어 완전한 고정 환경이 아니다. N3-B에는 이 전체 image가 필요하지 않다. 향후에는 simulator/policy를 별도 Docker image로 고정하고 submodule·fork·package hash를 다시 맞춘다.

그때 필요한 추가값은 checkpoint digest와 학습 provenance, `history_config.txt`의 resolved perceptual 설정, `OPENPI_DATA_HOME`, encoder/normalizer hash, GPU UUID 배정, WebSocket endpoint, 실제 VRAM·JAX allocation 정책이다. 예제 port 8000이나 학습용 memory fraction을 현재 native 설정으로 자동 적용하지 않는다. Inference/training의 VRAM 최소값은 아직 미측정이며, 저자의 큰 학습 예제를 N3-B의 하드웨어 요구로 옮기지 않는다.

## 7. 현재 결론

**환경 문서는 준비됐지만 native 실행 가능성이 검증된 것은 아니다.** 현재 Mac에서는 N3-A 계약 검사를 재실행할 수 있으며 N3-B는 적합한 로컬 Docker 환경을 기다린다. 이번에는 설치·이미지 build·GPU probe 반복·dataset/checkpoint/PDF 다운로드·실험을 수행하지 않았다. 설정 source text는 검토 후 임시 파일을 정리하고 hash만 남긴다. 환경 문서 완료를 연구 GO나 읽기 status 승격으로 사용하지 않는다.
