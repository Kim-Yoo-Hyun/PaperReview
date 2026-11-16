# 모바일 조작 정책 교체 — 재현 방법

2026-11-03 폴더 정리: 과거 실행 JSON의 명령·hash는 당시 기록을 유지한다. 현재 실행은 이 문서의 명령을 사용하고, 이전 경로는 [이동·병합 대응표](../../ORGANIZATION.json)에서 찾는다.

환경·명령·미구현 항목을 관리하는 단일 안내다. 아래 날짜별 점검은 당시 결과이며 현재 GPU 또는 정책 성공의 증거가 아니다. 실행 범위와 설정은 RESUME_PLAN.json을 따른다.

[연구 내용](../내용/README.md) · [재현 방법](../재현%20방법/README.md)

<a id="execution"></a>

<a id="execution-handoff-p0-다른-컴퓨터에서-이어갈-실행-준비"></a>
## HANDOFF P0 — 다른 컴퓨터에서 이어갈 실행 준비

- Updated: **2026-10-31 KST**. 사용자 지시: 현재 로컬 Docker의 조건이 맞으면 최소 실행 검증, 맞지 않으면 clone 후 재개 준비. [운영 기준](../../../../AGENTS.md#실험-준비-확인로컬-docker-실행-검증--2026-10-28-사용자-지시).
- **현재 결과: WAITING_RESOURCE.** Docker daemon은 동작하지만 현재 Mac ARM64 Docker의 `--gpus all` 할당이 exit 125로 실패했다. 시뮬레이터/정책 검증은 시작하지 않았다. [실제 점검 기록](LOCAL_CHECK_2026-10-28.json).
- 준비한 것은 **로컬 자원 확인 스크립트·재개 설정·구현 인계**다. Native Docker image·정책 transport 수정·handoff adapter는 아직 미구현/미검증이다. 이 폴더가 완성된 실험 launcher라는 뜻은 아니다.

<a id="execution-clone-후-첫-명령"></a>
### Clone 후 첫 명령

저장소를 clone한 사용자 선택 컴퓨터에서 다음을 실행한다. Host Python/pip/package 설치는 필요 없다. Shell은 Docker endpoint·daemon 정보를 확인하고, GPU 명령은 컨테이너 안에서만 실행한다.

```sh
sh "work/research_topics/mobile_policy_transfer/재현 방법/resume.sh" check
```

`check`의 exit 0은 Linux AMD64 daemon까지 확인했다는 뜻이다. GPU/VRAM·Vulkan·모델·상태 분기는 별도다. 현재 native recipe의 대상이 아닌 architecture는 exit 3으로 멈추며, `--platform` emulation·MPS·remote/cloud로 바꾸지 않는다. TCP/SSH Docker endpoint도 거부한다.

호환 컴퓨터에서 NVIDIA 드라이버와 Container Toolkit이 갖춰져 있고 `nvidia-smi`가 들어 있는 **기존 로컬 Linux AMD64 image**가 있을 때 다음으로 GPU 노출을 확인한다. 이 스크립트는 image를 내려받거나 host driver를 설치하지 않는다.

```sh
HANDOFF_GPU_IMAGE='<로컬 image ID 또는 digest>' \
  sh "work/research_topics/mobile_policy_transfer/재현 방법/resume.sh" gpu
```

GPU 이름·UUID·driver·VRAM이 출력돼도 CUDA 연산/RTX rendering 성공은 아직 아니다. 실제 image ID를 기록하고 native image 안에서 CUDA, rendering, 한 scene restore를 순서대로 확인해야 한다. 실패 컨테이너는 task label/name으로만 정리한다. 기존 이미지·volume을 지우는 명령은 제공하지 않는다. [Docker GPU passthrough](https://docs.docker.com/desktop/features/gpu/), [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).

<a id="execution-고정-근거와-환경-차이"></a>
### 고정 근거와 환경 차이

연구 질문·A/B·거리 후보·metric은 [H3 설계](../내용/README.md#design-history)를 따르며 split에는 아래 10/31 보완을 적용한다. [RESUME_PLAN.json](RESUME_PLAN.json)은 재개 설정이며 `native_executable=false`다. 공개 revision·normalizer hash와 미확정 image/weight/seed·물리 상태 항목을 구분했다.

**10/31 비실험 보완이 split 해석에 우선한다.** [데이터·설계 검토](../../../update/PRE_GPU_BUILDUP_REVIEW_2026-10-31.md#mobile-policy-transfer)에서 10개 source episode가 같은 scene instance template임을 확인했다. H3의 2/4/4는 독립 instance holdout으로 사용할 수 없다. 1개 dev IO는 유지하며 후속 2/4/4의 역할을 동일-template 개발/조건 선택/선택 후 기술적 평가로 수정했다. Scene hash 차이는 물리 상태 독립성의 증거가 아니다. 이 검토에서 Docker/GPU probe는 반복하지 않았다.

| 구성 | 확인한 source 설정 | 재개 시 해야 할 일 |
|---|---|---|
| Host/daemon | 목표는 Linux AMD64 Docker + NVIDIA CUDA/RTX graphics. Ubuntu 22.04는 server README의 참고 OS | 실제 GPU·driver·VRAM·RAM·disk 확인. 총 필요 VRAM은 미측정; 작은 server의 요구량을 simulator 포함 총량으로 사용하지 않음 |
| Simulator | Benchmark `d3593788…`: Python **3.10**, PyTorch **2.6.0**, 기본 CUDA wheel **12.4**, OmniGibson **3.7.2**, BDDL **3.7.0**, Isaac Sim **4.5.0** | 고정 source로 전용 Docker image를 구성하고 digest/설치 결과 기록. [setup.sh](https://github.com/nubot-nudt/Behavior-Skill/blob/d3593788bdc7bd3016d307ea9529fdb500c146ba/setup.sh)의 host 설치 명령을 host에서 실행하지 않음 |
| Policy server | Server `7ca6eace…`: `.python-version` **3.11**, `requires-python>=3.11`, torch **2.7.1**, JAX CUDA12 **0.5.3**, flax **0.10.2** | 별도 policy Docker 환경. [pyproject](https://github.com/mafangniu/pi05-behavior-skill/blob/7ca6eace02aaba2d8ce19af600b85dd04a60d720/pyproject.toml)·lock을 기준으로 dependency resolve/import 검증; sim 환경에 강제 설치하지 않음 |
| Transport | 공개 server는 OmniGibson의 websocket/상태 index helper를 import함 | **컨테이너 둘로 나누는 것만으로 해결되지 않음.** Policy 쪽 helper를 simulator runtime 없이 제공할 작은 adapter 또는 저자 지원 조합을 먼저 검증. Python 요구를 무시하거나 다른 torch로 조용히 바꾸지 않음 |
| Checkpoint | A=12-task Skill, B=50-task Skill, 각 normalizer 유지 | Docker volume에 고정 revision으로 수집하고 weight 파일 전체 hash manifest 생성. Native loader 확인 전 완전 다운로드/호환이라고 표시하지 않음 |
| Scene/data | 고정 dataset release의 radio dev `00000010`, skill0/1 config·manifest·scene | 실제 scene/instance grouping 및 source identity 확인. Demo skill1 snapshot은 reference만; handoff는 skill0 실행으로 만든 상태 사용 |

Simulator와 server의 Python/torch 요구가 달라 **단일 environment 설치 recipe를 아직 확정할 수 없다.** Source에 있는 websocket 기반 분리를 출발점으로 사용하되 실제 transport import를 다음 구현 대상으로 남긴다. 이것은 추가로 확인한 구체적인 실행 준비 문제이며 연구 효과의 반증이 아니다. Source URL/hash와 확인 구간은 점검 JSON에 있다. 4.5.0 공식 requirements 페이지는 이번 접근에서 404였으므로 최신 Isaac Sim 요구를 옛 버전의 검증된 최소 사양으로 옮기지 않았다.

<a id="execution-저장-위치설정-계약"></a>
### 저장 위치·설정 계약

아래는 **제안된 container 경로/volume 이름**이다. 현재 생성한 volume은 없다. Repository 문서는 read-only로 mount하고, 패키지·외부 source·weights·assets는 Docker image 또는 named volume에 둔다.

| 저장 대상 | 제안 위치 | 사용 방식 |
|---|---|---|
| 이 repository | `/workspace/paper_registry:ro` | clone 위치와 무관하게 실행 시 mount |
| 두 upstream source | `paper-handoff-source` → `/sources` | Docker 내부 checkout, 두 revision 확인; runtime은 read-only |
| Models/data | `paper-handoff-assets` → `/assets` | 수집 과정만 쓰기, runtime read-only; A/B normalizer 별도 |
| Simulator cache | `paper-handoff-sim-cache` → `/sim-cache` | release 및 image별 cache 구분 |
| 새 run 결과 | `paper-handoff-runs` → `/runs/<새 run ID>` | 원본 trace·manifest 저장; 기존 결과 덮어쓰기 없음 |

두 native container가 통신할 경우 같은 로컬 Docker 내부 network에서 server port **8000**을 사용하고 host에 공개할 필요는 없다. GPU driver capabilities는 `compute,graphics,utility,video`를 후보로 둔다. Simulator와 정책이 동시에 사용하는 GPU memory를 실제로 측정해야 한다. 초기에는 환경 하나·정책 한 개씩 순차 로드하며 A/B branch를 실행한다. 이 방법도 상태 재로드의 동등성 확인이 필요하다. Image digest·GPU UUID·driver·assets version·seed·실제 controller 설정은 native run마다 기록한다.

<a id="execution-조건이-맞는-컴퓨터에서-이어갈-순서"></a>
### 조건이 맞는 컴퓨터에서 이어갈 순서

1. `check → gpu`: 로컬 endpoint·AMD64·GPU 노출 확인. 다음에는 native image의 CUDA kernel·RTX/Vulkan rendering·장면 restore를 실제 확인한다. 하나가 실패하면 그 단계에서 멈춘다.
2. Simulator/policy 환경 분리와 transport import 문제를 해결하고 두 image digest를 고정한다. [H2 queue/복원 경계](../내용/README.md#public-interface-3-구현을-시작하기-전에-알아둘-차이)를 준수한다. 설치·작은 import 확인도 Docker 안에서만 한다.
3. A/B checkpoint와 각 normalizer를 확인하고 **동일한 실제 관측**으로 각각 1회 추론한다. 입력 RGB/proprio shape·유한성, 출력 23 action의 실제 controller slot/단위·queue reset을 확인한다. 임의 관측의 action shape 통과를 정책 competence로 표시하지 않는다.
4. Dev `00000010`의 navigation을 최대 600 tick 실행하고 종료→15 tick 정지 후 상태를 저장한다. BDDL `near`의 조기 종료, 영상 추가 5 step, 시연 snapshot reset이 handoff 상태를 바꾸지 않게 adapter를 구현한다.
5. 저장 상태에서 A/B를 각각 cold-start하며 동일 RGB/proprio·object/robot/contact/grasp/controller state와 RNG 복원 경계를 기록한다. 직렬화하지 못한 상태를 숨기지 말고 비교 제한 또는 미통과로 남긴다. 한 dev의 최대 예산은 **nav 1회 + A/B pickup 각 1회**이며 reference가 필요한 경우 A/B 각 1회만 추가한다. 성공률 비교·110 phase pilot·학습은 P0에 포함하지 않는다.
6. 확인된 단일 scene-template identity와 수정된 역할 배분을 적용하고 실제 state 중복·복원 경계를 확인한다. 동일-template 탐색 범위에서 seed/runtime 명세를 결과 관측 전에 고정한다. 기존 2/4/4를 독립 instance 평가로 자동 사용하지 않는다. P0 결과에 따라 H3 pilot을 별도로 판단한다. 성능이 낮거나 도착 후보가 구별되지 않아도 연구 전체의 반증으로 확대하지 않는다.

**현재 준비의 종료점:** 자원 확인 스크립트·설정 인계는 존재한다. Native image/transport/handoff 구현은 남아 있다. 현재 컴퓨터에서는 GPU 할당 실패가 확인되어 이 지점에서 멈췄다. 다른 컴퓨터에서 clone하려면 이 폴더와 문서 변경이 먼저 Git에 포함돼야 한다. 이번 작업은 commit/push를 수행하지 않았다.

<a id="preparation-history"></a>

<a id="preparation-history-검증"></a>
### 검증

`sh -n` 통과, `help` exit 0, 실제 로컬 `check`의 ARM64 차단 exit 3, TCP endpoint 거부 exit 2를 확인했다. 이는 shell 자원 확인 경로의 검증이며 GPU 성공 경로·VLA/runtime 검증은 아니다.

Reading generator `py_compile`·재생성, `git diff --check`, repository audit, JSON 검사를 통과했다. 오류·경고 **0**, registry **1,072편**, tier **47/297/486/242**, active/history **344/47**, notes **5,360개**를 보존했다. Markdown **5,547개**, 상대 링크 **11,034개** 검사 통과. Generator/queue 변화는 없다.

기존 dirty **664개** 중 이번 수정 **6개** 외 **658개**와 기존 삭제 **10개**를 보존했다. 신규는 재개 폴더 4파일·이 기록 1파일이다. Canonical 7파일 중 요청한 AGENTS만 변경했으며, 추가한 기준·날짜만 역적용한 hash로 이전 AGENTS 내용 보존도 확인했다. PAPER·manifest/meta·tier·active/history CSV 6개는 byte-identical이다.
