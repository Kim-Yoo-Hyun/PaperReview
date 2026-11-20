# 부분 지시 수정 재현

2026-11-03 폴더 정리: 과거 실행 JSON의 명령·hash는 당시 기록을 유지한다. 현재 실행은 이 문서의 명령을 사용하고, 이전 경로는 [이동·병합 대응표](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/research_topics/ORGANIZATION.json)에서 찾는다.

환경·명령·미구현 항목을 관리하는 단일 안내다. 아래 날짜별 점검은 당시 결과이며 현재 GPU 또는 정책 성공의 증거가 아니다. 실행 범위와 설정은 RESUME_PLAN.json을 따른다.

[연구 내용](../내용/README.md) · [재현 방법](../재현%20방법/README.md)

<a id="execution"></a>

<a id="execution-vla-지시-전환-최소-실행-준비"></a>
## VLA 지시 전환 최소 실행 준비

- Updated: 2026-10-31 KST
- 범위: [지시 일부 수정 사례집](../내용/README.md#cases)의 **R8 기본 전환 1건**. 활성 작업은 [TODO](../../../../TODO.md).
- 상태: **준비 artifact 작성·정적 검사 완료 / 이미지 빌드·native 실행 미확인 / 현재 자원 NOT_MET**. 실행 성공이나 연구 효과를 보고하는 문서가 아니다.
- 후속 연구 설계는 [GPU 전 보완](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/update/PRE_GPU_BUILDUP_REVIEW_2026-10-31.md#instruction-revision)을 따른다. 의미 갱신/평가 계약의 보완이며 이 폴더의 R8 단일 IO 예산·실행 코드는 변경하지 않았다.

<a id="execution-현재-확인한-것"></a>
### 현재 확인한 것

[로컬 확인 기록](LOCAL_CHECK_2026-10-31.json): Docker daemon은 동작하지만 `linux/arm64`, 10 CPU, 메모리 8,218,034,176 bytes다. 기존 이미지로 `--gpus all`을 요청했을 때 exit 125, `could not select device driver "" with capabilities: [[gpu]]`가 발생했다. 모델·simulator는 실행하지 않았다. 새 image/container/volume, host 패키지·weights·simulator assets는 만들지 않았다. 아래 recipe를 이 컴퓨터에서 빌드하거나 emulation으로 우회하지 않는다.

| 준비 artifact | 역할·현재 경계 |
|---|---|
| [RESUME_PLAN.json](RESUME_PLAN.json) | source/환경/관측·행동/seed/예산/중단 조건. 실제 runtime manifest 아님 |
| [ARTIFACTS.json](ARTIFACTS.json) | 공개 GCS metadata로 고정한 checkpoint 16개 + tokenizer 1개. weights 미다운로드 |
| [Dockerfile](Dockerfile) | 하나의 image에 simulation Python 3.10과 policy Python 3.11 분리. 빌드 미검증 |
| [resume.sh](resume.sh) | 로컬 endpoint·architecture 확인, 단계별 Docker 실행. ARM64 차단 동작 확인 |
| [inside.py](inside.py) | Docker 내부 다운로드·checksum·서버 시작·예산·결과 수집. 미실행 |
| [native_probe.py](native_probe.py) | 실제 ReSteer evaluator와 openpi client 사용, 두 query/행동 큐 감사. 미실행 |

<a id="execution-대상-컴퓨터와-설정"></a>
### 대상 컴퓨터와 설정

대상은 사용자가 선택한 **Linux x86-64 + NVIDIA GPU의 로컬 Docker**다. CUDA 12와 EGL을 지원하는 NVIDIA driver 및 Docker GPU runtime이 미리 구성되어 있어야 한다. Toolkit 설정은 [NVIDIA 공식 안내](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)를 따른다. 이 launcher는 host driver/toolkit을 설치하거나 daemon 설정을 바꾸지 않는다. [Docker Desktop의 일반 Linux container GPU passthrough](https://docs.docker.com/desktop/features/gpu/)와 다른 제품의 모델 가속 기능을 혼동하지 않는다. Windows/WSL에서 CUDA가 보이더라도 이 recipe의 EGL 경로는 별도 검증이 필요하다.

준비 목표는 GPU VRAM 24 GiB, host RAM 32 GiB, Docker 여유 공간 80 GiB다. 이는 모델·렌더링·빌드 여유를 위한 **미검증 provisioning 값**이며 최소 요구량 실측치가 아니다. [ReSteer 저자 README](https://github.com/ChenZhenY/ReSteer/blob/7329c159319a346b7245a69c128e5d4940c0763b/README.md)는 serving 약 10 GB를 안내한다. `gpu`에서 UUID·driver·VRAM을 확인하고, 실행 시 CUDA backend·EGL frame·실제 model load를 따로 확인한다. 메모리/공간은 자동 보장되지 않으므로 실행 전 대상 컴퓨터에서 확인한다.

고정값은 [plan](RESUME_PLAN.json)을 따른다. 핵심은 ReSteer `7329c159…`, openpi submodule `215abfb2…`, 공개 `pi05_libero`, JAX 0.5.3 CUDA12, MuJoCo 3.2.3, robosuite 1.4.1이다. `MUJOCO_GL=egl`, `PYOPENGL_PLATFORM=egl`, `NVIDIA_DRIVER_CAPABILITIES=compute,graphics,utility`, `JAX_PLATFORMS=cuda`, `XLA_PYTHON_CLIENT_MEM_FRACTION=0.70`으로 실행한다. 한 GPU만 노출하며 `REVISION_GPU_DEVICE` 기본값은 host의 GPU index 0이다. ReSteer fine-tuned weight는 이 packet에 포함하지 않는다.

Base image의 linux/amd64 digest, 두 uv.lock의 SHA-256, Python patch version을 고정했다. apt system package 전체를 snapshot 고정한 것은 아니므로 완전한 bitwise rebuild를 주장하지 않는다. 실행 시 image ID·source revision·실제 package version·artifact SHA-256을 runtime manifest에 남긴다. Docker 빌드가 dependency/ABI 문제로 실패하면 그 단계에서 멈추고 원인을 기록한 뒤 recipe를 수정한다.

<a id="execution-clone-후-실행-순서"></a>
### Clone 후 실행 순서

이 packet이 포함된 저장소 revision을 clone한 뒤 repository root에서 실행한다. **2026-10-31 현재 packet은 로컬 작업 변경이며 원격 게시·다른 물리 컴퓨터 실행은 확인하지 않았다.** 현재 코드·문서가 실제 clone에 들어 있는지 먼저 확인한다. 사용자별 절대 경로는 실행 조건에 없다. Shell과 Docker CLI 외 패키지를 host에 설치하지 않는다.

```sh
sh "work/research_topics/instruction_revision/재현 방법/resume.sh" check
sh "work/research_topics/instruction_revision/재현 방법/resume.sh" gpu
sh "work/research_topics/instruction_revision/재현 방법/resume.sh" build
sh "work/research_topics/instruction_revision/재현 방법/resume.sh" assets
sh "work/research_topics/instruction_revision/재현 방법/resume.sh" smoke
sh "work/research_topics/instruction_revision/재현 방법/resume.sh" results
```

각 단계가 성공한 경우에만 다음 단계로 간다. `check`는 read-only이며 ARM64/원격 endpoint를 거절한다. `gpu`는 고정 base image가 없으면 Docker로 가져와 GPU 노출을 확인한다. `build`도 GPU를 먼저 확인하고 recipe를 빌드한다. GPU 노출 성공만으로 CUDA/EGL/native 성공을 판정하지 않는다. Recipe 변경 후에는 `build`를 다시 해야 한다.

`assets`는 Docker 내부에서 17개 파일 **12,443,349,504 bytes**를 받는다. 각 파일의 정확한 GCS generation, size, CRC32C와 제공된 경우 MD5를 검사하고 SHA-256을 계산한다. Composite object는 MD5가 없을 수 있어 CRC32C를 필수로 사용한다. Normalizer의 SHA-256은 사전 확인값과도 비교한다. 고정 generation이 사라졌거나 checksum이 다르면 멈추며 최신 객체로 자동 치환하지 않는다. 중단된 `.partial`은 재실행 시 해당 파일만 다시 받는다. 현재 정상 파일은 재사용·재검사한다.

- `paper-revision-p0-data` → `/data`: checkpoint와 tokenizer cache, `VERIFIED_ARTIFACTS.json`.
- `paper-revision-p0-runs` → `/runs`: 시각별 run과 `LATEST` pointer. 이전 결과를 덮어쓰지 않는다.
- LIBERO scene/mesh는 고정 ReSteer source와 함께 image 내부에 있다. 별도 demonstration dataset은 P0에 필요하지 않다.
- `smoke`는 외부 network/host port 없이 같은 container의 loopback websocket으로 sim/server를 연결한다. 관측·action·상태·log는 Docker volume에 저장한다.
- `results`는 최신 runtime manifest를 stdout으로 읽는다. 필요하면 작은 JSON만 저장소에 옮겨 근거로 검토한다. weights/assets를 host로 복사하지 않는다.

<a id="execution-최소-검증과-판정"></a>
### 최소 검증과 판정

한 scene, seed 7, source task 3(`put the bowl on the plate`)에서 target task 5(`put the bowl on top of the cabinet`)로 바꾼다. Warmup 10회 후 policy step 2에서 전환하고, 최대 policy 7회·inference 2회만 실행한다. 기존 5-action queue 중간에서 전환하므로 query B의 첫 action으로 교체되는지 확인할 수 있다. `smoke`의 900초 예산은 artifact 검증과 CUDA backend 확인 후 **서버 시작 + native probe**에 적용한다. CUDA backend probe는 별도 120초이며 build/download 시간은 이 예산에 포함하지 않는다.

`PASS_IO_ONLY`의 조건은 GPU backend, 224×224×3 uint8 두 영상과 finite 8D state, finite 10×7 action 두 응답, step 2의 target query, 실제 실행한 action과 새 queue의 일치, environment exception 없음이다. 시간 초과/OOM/checksum/transport/EGL 오류는 실패 단계와 함께 보존하고 중단한다. CPU/MPS 대체나 추가 sweep은 하지 않는다. Target 첫 성공 flag는 부수 기록이며 성공률·steerability·제약 준수의 증거로 해석하지 않는다. 최대 7회 action만으로 task competence를 판정할 수 없다.

향후 실제 결과는 `runtime_manifest.json`, `native_result.json`, `policy_observations.npz`, `server.log`, `probe.log`로 저장한다. 실행 중 중단으로 `RUNNING`만 남았거나 native JSON이 없으면 PASS로 처리하지 않는다. Runtime manifest는 당시 환경과 artifact의 증거다. Native step callback은 입력 action을 기록하고 MuJoCo 내부 clipping/control 변환은 선행 evaluator를 그대로 사용한다.

<a id="execution-남은-구현연구-단계"></a>
### 남은 구현·연구 단계

먼저 호환 컴퓨터에서 image build → checksum → CUDA/EGL → 1개 native IO를 실제 확인해야 한다. 그 다음 R1/R4의 기간별 제약 observer·허용 오차, 동일 상태 branch/controller/RNG 복원, O/A 능력 비교를 구현·검증한다. H/S 자동 의미 갱신·paired 성능 비교·학습은 아직 구현하지 않았으며 이번 최소 검증에 포함하지 않는다. 자원 부족은 연구 가설의 반증이 아니고, IO 통과 역시 연구 가치의 입증이 아니다.

Container는 `--rm`과 현재 task label을 확인하는 종료 trap으로 정리한다. 전용 image는 `paper-revision-p0:7329c159`, volume은 위 두 개이며 동일 이름의 다른 task 자산은 사용하지 않는다. 이 task를 종료하고 더 사용할 계획이 없을 때 전용 image를 지정해 제거할 수 있다. 결과/weights가 있는 volume은 재개 근거라 자동 삭제하지 않는다. 전역 `prune`, 기존 `paper-gap-p3` image, `minikube` volume 정리는 하지 않는다.

Source 대조: [rollout](https://github.com/ChenZhenY/ReSteer/blob/7329c159319a346b7245a69c128e5d4940c0763b/resteer/eval/rollout.py), [sim 입력](https://github.com/ChenZhenY/ReSteer/blob/7329c159319a346b7245a69c128e5d4940c0763b/resteer/sim/libero.py), [openpi config](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/src/openpi/training/config.py), [checkpoint object metadata](https://storage.googleapis.com/storage/v1/b/openpi-assets/o?prefix=checkpoints/pi05_libero/).

<a id="preparation-history"></a>

<a id="preparation-history-검증보존"></a>
### 검증·보존

- 수행: Python 구문/임시 bytecode 검사(실험 모듈 import·실행 없음), JSON 문법·17개 file/bytes/예산 정합성, shell 구문, `help` 및 현재 로컬 `check` 차단 동작.
- Generator 임시 bytecode 검사·`PYTHONDONTWRITEBYTECODE=1 python3 work/scripts/build_reading_tiers.py`·`git diff --check` PASS. Repository audit: **errors 0 / warnings 0**, Markdown 5,565개·링크 11,112개 검사.
- AGENTS·PAPER·papers manifest·registry meta·READING_PLAN·tiers·active/history tracker **8개 파일 SHA-256이 작업 전후 동일**하다. Registry 1,074편, CORE 47 / NEXT 299 / REFERENCE 486 / ARCHIVE 242, active 346 / history 47을 보존했다.
- 종료 시 Docker inventory: container 0개, 기존 `paper-gap-p3:rvo-c2c46ba` image 1개·`minikube` volume 1개. 신규 자산이 없어 삭제할 항목도 없었다.
- 준비 파일의 존재와 native 검증을 구별했다. 실제 image ID·downloaded artifact SHA-256·runtime manifest는 아직 없다. 새 논문 등록·tier/reading status 변경은 없다.
- 이 packet은 로컬 작업 변경으로 추가되었으며 원격 게시·다른 물리 컴퓨터 clone 실행은 이번 범위에 포함하지 않았다.
