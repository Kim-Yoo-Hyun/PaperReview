# 시각 피드백 활용 진단 — Docker 최소 입출력 검증

- Updated: 2026-11-06 KST
- [연구 내용](../내용/README.md) · [고정 실행 설정·검증 상태](./RESUME_PLAN.json) · [launcher](./resume.py) · [native adapter](./probe.py)
- **GAP-FEEDBACK-P0-PREP 준비 범위 완료 / native 실행 미확인.** 아래 recipe는 현재 Mac에서 build하지 않았다. 다른 컴퓨터의 실제 clone·실행도 미확인이다.

## 현재 확인된 것

| 구분 | 2026-11-06 결과 |
|---|---|
| Local Docker | Unix socket의 Docker Desktop 동작, host Darwin ARM64·16 GiB, daemon Linux aarch64·약 7.65 GiB, NVIDIA runtime 없음 |
| Launcher | `check`가 호스트/architecture 조건에서 exit 3. Native build/pull/download·GPU 할당 요청 전에 중단. [원시 결과](./results/2026-11-06-local/local_check.json) |
| 제어 검사 | 기존 ARM64 Docker CPU image에서 **9개 통과**. Budget·평가 cache·파일 무결성·경로·remote/stale-image 차단 검사. [첫 실패와 수정 후 결과](./results/2026-11-06-control-tests/tests.json) |
| 미실행 | Native image build, 전체 dependency 해결, weights/assets 확보, CUDA/Vulkan/rendering, 모델 추론·시뮬레이션·상태 분기 복원 |

제어 검사는 실제 PyTorch/ManiSkill 인터페이스의 동작을 증명하지 않는다. 첫 검사에서 얕은 Docker mount 경로에 불필요한 repository-depth 가정이 실패해 제거했다. 시험 container는 `--rm`으로 제거했으며 기존 사용자 image를 보존했다. Host에 실험 패키지·weights·assets를 설치하지 않았다.

## 환경과 고정 입력

| 항목 | 선택한 설정 / 근거 |
|---|---|
| Host | 사용자 선택 컴퓨터의 **local Linux x86-64, NVIDIA GPU, Docker Engine + NVIDIA Container Toolkit**. SSH/TCP endpoint·remote builder·Mac/MPS fallback 없음 |
| GPU | Native BF16 가능 GPU. Ampere 이상·VRAM 24 GiB 이상을 준비 권장치로 두지만 peak는 미측정. Launcher는 최소한 BF16 actor tensor 약 15.08 GB보다 free VRAM이 큰지 확인 |
| Driver | 이 packet의 CUDA 12.1 GA 선택 기준 `530.30.02` 이상. CUDA minor compatibility의 일반 최저치와 구분. [공식 release notes](https://docs.nvidia.com/cuda/archive/12.1.0/cuda-toolkit-release-notes/index.html) |
| RAM / disk | Host RAM 32 GiB·여유 disk 80 GiB 준비 권장치, 실측 최소 요건 아님. 부족하면 상한 확장/CPU offload로 우회하지 않고 기술 실패로 기록 |
| Container | Ubuntu 22.04 / Python 3.10 / torch 2.2.0+cu121 / torchvision 0.17.0 / Transformers 4.40.1 / SAPIEN 3.0.0b1 / vendored ManiSkill 3.0.0b20 |
| Recipe | [Dockerfile](./Dockerfile)의 amd64 CUDA image digest와 [직접 의존성 pin](./requirements.txt). Native build 성공 시 image 안에 `resolved-packages.txt`, `resolved-system-packages.txt` 생성. 아직 전체 closure/재빌드 동일성을 확보한 것은 아님 |
| RL4VLA code | [de46e0174e7ac310255a2836718fcefab28b8963](https://github.com/gen-robot/RL4VLA/tree/de46e0174e7ac310255a2836718fcefab28b8963). Git checkout은 Docker build 안에서만 수행 |
| P0 모델 1개 | [gen-robot/openvla-7b-rlvla-rl](https://huggingface.co/gen-robot/openvla-7b-rlvla-rl/tree/93c54b036cc90ee394731fc73788406d7e65f057), revision `93c54b036cc90ee394731fc73788406d7e65f057`, native normalizer `bridge_orig` |
| Robot/task assets | WidowX commit `6a12bb745d964aab9fc897f0999cad53aa29000c`; task carrot/plate/table는 RL4VLA checkout 내부; Bridge dataset revision `b5a8f9ba26355ae73758971189e5cdb68f4dad76` |

CUDA enumeration과 graphics가 모두 필요하다. Docker GPU 접근은 [공식 GPU 설정](https://docs.docker.com/engine/containers/resource_constraints/#gpu)을 따른다. `prepare`에서 CUDA/BF16·NVIDIA Vulkan을 먼저 검사하고 payload를 받으며, rendering은 P0의 실제 RGB 취득으로 별도 확인한다.

파일별 immutable URL·size·hash는 `RESUME_PLAN.json`이 소유한다. HF API의 `sha1`은 **Git blob SHA1**, LFS 파일은 SHA256이다. 원격에 게시된 weight hash 확인은 다운로드한 payload 검증과 다르다. `prepare`가 실제 바이트를 확인하고 model/asset SHA256 목록과 `ready.json`을 생성해야 준비 cache가 성립한다. 기존 손상 파일·부분 다운로드는 자동 덮어쓰거나 재시도하지 않는다.

## 입출력 계약과 종료 상한

1. `PutOnPlateInScene25PositionChangeTo-v1`, seed 0·episode ID 0을 결과 확인 전에 고정했다. 원 task의 `test` object split을 쓰지만 **개발용 한 instance**이며 held-out 평가가 아니다. 로봇은 WidowX, control 5 Hz·physics 500 Hz다.
2. Constructor reset을 포함해 reset 최대 2회. Neutral 명령 5회로 event에 도달한다. 제어 step 4 RGB와 step 5의 물체 이동 후 RGB를 저장한다. 원 `evaluate`가 물체 이동·집기 counter를 바꾸므로 제어 step별 evaluation cache로 중복 호출의 효과를 막는다.
3. 물체 변위·RGB hash 변화·시각 정렬을 확인한다. 같은 post-event 상태에서 stale step-4 / fresh step-5 / repeat-fresh의 **3개 query**를 수행한다. 정책은 RGB·instruction만 받고 hidden pose는 기록·검증용이다.
4. 원 코드의 action-token decoder와 normalizer로 `1×7` controller command를 만든다. Greedy repeated-fresh token이 같고 명령이 finite인지 확인한다. 모델의 누락 actor weight는 실패; 공개 weight에 없는 `value_head.*`만 허용하며 그 critic output은 사용하지 않는다.
5. Fresh 명령 한 번만 실행하여 control step 6에서 끝낸다. Stale 명령 rollout·성공률 비교·학습은 하지 않는다. 실패하거나 반응 차이가 없어도 자동 추가 query·scene·checkpoint 실행은 없다.

전체 상한은 **reset 2 / inference 3 / control step 6 / event 1 / physics step 2,000**이다. Physics는 모든 `ManiSkillScene.step()` 호출을 뜻하며 solver 내부 iteration이나 wall time이 아니다. Reset settling과 event settling을 포함한다. 읽은 코드의 상한 추정은 1,950회다. `_settle(0.5)` 인자를 곧바로 물리 0.5초라고 해석하지 않는다. 비용은 native 호출 전에 차감하고 실패 시에도 남긴다.

기본 RL4VLA evaluation의 temperature 0.6과 FlashAttention 대신 **greedy + eager attention + BF16**를 선택한 진단이다. 원 논문 score의 정확한 재현이 아니다. 저장하는 physical/controller/task snapshot은 query가 상태를 바꾸지 않는지 점검하는 용도다. **RNG·task/evaluator를 포함한 전체 상태 분기 복원은 아직 없으며**, 네 조건의 성공률 비교 전에 별도로 구현·교정해야 한다.

<a id="resume"></a>

## 다른 컴퓨터에서 재개

이 파일들이 포함된 저장소 revision을 전달/clone한 뒤 **저장소 루트**에서 실행한다. 아래 host Python은 표준 라이브러리로 Docker를 제어하고 시스템 정보를 읽을 뿐 모델이나 simulator를 import하지 않는다. 각 명령은 새 결과 폴더를 요구한다. 이미 있으면 suffix를 바꾸고 기존 증거를 보존한다. `check`가 exit 3이면 그 컴퓨터에서 뒤 명령을 진행하지 않는다.

```bash
python3 'work/research_topics/visual_feedback/재현 방법/resume.py' check --gpu 0 --results 'work/research_topics/visual_feedback/재현 방법/results/nvidia-check-01'
python3 'work/research_topics/visual_feedback/재현 방법/resume.py' build --gpu 0 --results 'work/research_topics/visual_feedback/재현 방법/results/nvidia-build-01'
python3 'work/research_topics/visual_feedback/재현 방법/resume.py' prepare --gpu 0 --results 'work/research_topics/visual_feedback/재현 방법/results/nvidia-prepare-01'
python3 'work/research_topics/visual_feedback/재현 방법/resume.py' p0 --gpu 0 --results 'work/research_topics/visual_feedback/재현 방법/results/nvidia-p0-01'
```

각 단계 성공 후 다음 단계로 진행한다. Endpoint/builder override 환경변수가 있으면 launcher가 중단한다. 확인한 local context로만 build/run하며 image의 packet hash label이 현재 code·설정과 다르면 재사용을 거부한다. 의존성은 build 내부, weights·Bridge assets는 `prepare` container 내부에서만 받는다. 다음 위치를 사용한다.

| 위치 | 저장물 |
|---|---|
| Image `/opt/feedback/RL4VLA`, `/opt/feedback/widowx` | 고정 source·task/robot assets |
| Docker named volume `paper-feedback-p0-<packet hash prefix>` → `/cache` | 모델, Bridge assets, 검증 `ready.json`; 패키지/weights를 host 폴더에 설치하지 않음 |
| `/cache/model/<checkpoint revision>` | 선택한 RL weight shards·processor/tokenizer/config |
| `/cache/assets/data/tasks/bridge_v2_real2sim_dataset` | Bridge scene; robot 경로는 image 내부 WidowX로 연결 |
| 지정 results 폴더 → `/results` | local check·명령·exit·log·RGB·상태/행동/비용 결과만 |

`p0`는 network none/HF offline이다. `prepare`만 실행 시 network가 있으며 build도 의존성 확보에 network를 사용한다. 실행 container는 고유 이름과 `--rm`으로 정리한다. 재사용 cache/image는 소유 label과 packet hash를 확인한 뒤 관리하며 광범위한 `docker prune`은 하지 않는다.

성공 표시 `IO_QUALIFIED_NOT_RESEARCH_EFFECT`는 이 작은 IO 연결만 뜻한다. 실패는 `FAILED_NO_RESEARCH_CONCLUSION` 및 부분 비용·오류를 남긴다. 준비 성공 `PAYLOAD_PREPARED_NATIVE_UNVERIFIED`도 native IO 통과가 아니다. Launcher는 실제 image ID·digest·architecture를 `image.json`에, container는 build에서 해결된 package/system 목록을 결과 폴더에 기록하도록 작성했다. Native build가 없으므로 이 기록들은 아직 생성되지 않았다.

<a id="preparation-history"></a>

## 준비 이력과 남은 작업

2026-11-06에 official code/metadata와 CUDA/Docker 문서를 대조해 pin·asset 경로·loader·budget을 작성했다. 9개 Docker CPU 검사 결과와 local resource rejection은 위 원시 JSON에 보존했다. 신규 모델 image·payload를 만들지 않았다. 동일한 Mac 자원 실패나 metadata 조사만 반복할 이유는 없다.

최종 registry generator compile·재생성, repository audit, `git diff --check`를 통과했다. 전체 1,110편·5,550개 표준 노트 유지, audit 오류/경고 0이다. 시작 시점 대비 active/history 읽기 tracker와 기존 staged diff·VRL 동결 계약은 byte 동일하며 기존 파일 삭제는 없다. 신규 결과 JSON의 첫 실패·수정 후 통과를 한 파일에 합쳐 보존했다. 이번 test container 잔여물은 없고 기존 image 하나는 유지했다.

다음 **GAP-FEEDBACK-P0**는 `WAITING_RESOURCE_AND_IMPLEMENTATION`이다. 호환 NVIDIA 컴퓨터에서 recipe build/전체 dependency closure → CUDA/Vulkan·payload hash → native IO를 확인한다. Source로 예상한 reset/physics 상한·processor·controller 동작도 그때 실제 교정한다. 전체 상태 복원·clean/changed×fresh/stale 분기·SFT/warmup 비교는 P0 뒤의 별도 범위이며 미구현이다. GPU 확보만으로 연구 효과나 학습 비교를 완료 처리하지 않는다.
