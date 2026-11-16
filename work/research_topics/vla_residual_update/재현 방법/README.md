# VLA 업데이트 후 residual 적응 — 환경과 재개 방법

Updated: 2026-11-05 KST. **P0 실행 코드·image recipe 초안 작성 / 제어·중단 장치 9개 검사 통과 / native image·IO 미검증**.

연구 질문과 내부 비실험 완료 범위는 [내용](../내용/README.md#nonexperimental-completion), 환경 관측·미구현 필드는 [RESUME_PLAN.json](./RESUME_PLAN.json)이 관리한다. 전체 학습 계약은 [공통 source 원장](../../../sources/vla_rl_gap_review_2026-11-03.json)의 `r2_review.comparison_contract` 하나에 둔다. 이 문서를 runnable image나 검증된 재현 결과로 읽지 않는다.

**11/06 호환성 검토:** [GAP-INTEGRATED-N2](../../../update/INTEGRATED_GAP_REVIEW_2026-11-05.md#integrated-n2)에서 RL4VLA와 대조했다. 이 packet은 LIBERO·8×7 chunk·20 Hz 전용이며 RL4VLA의 ManiSkill·single action·5 Hz에 그대로 사용할 수 없다. 비용/provenance 기록 원칙만 재사용한다. 기존 코드·RESUME_PLAN·source contract hash와 11/05 runtime 기록은 보존했으며 이번에는 native 실행이나 Docker 재측정을 하지 않았다.

## 현재 컴퓨터에서 확인한 범위

| 항목 | 2026-11-05 실제 읽기 전용 재확인 |
|---|---|
| Host | Darwin / arm64, 물리 RAM 17,179,869,184 bytes (16 GiB) |
| Docker context·endpoint | `desktop-linux`, 사용자 로컬 Unix socket. DOCKER_HOST/DOCKER_CONTEXT override 없음 |
| Daemon | Docker Desktop 28.3.3, Linux aarch64, 10 CPUs |
| Docker memory | 8,218,034,176 bytes, 약 7.65 GiB |
| Runtimes | runc / io.containerd.runc.v2. NVIDIA runtime 미표시 |
| 판정 | 이 계획의 Linux x86-64 NVIDIA CUDA 조건 미충족. Native P0 실행 안 함 |
| 실제 실행 | 기존 로컬 image에서 제어·중단 장치 단위 검사 9개 통과. 임시 CPU container 2개(코드 수정 후 재검사 포함)는 `--rm`으로 종료 후 제거 |
| 하지 않은 실행 | GPU allocation container, 신규 image pull/build, dependency 설치, inference/training, weights·sim assets·PDF 다운로드 모두 0 |

사용자의 비-NVIDIA 컴퓨터 설명과 현재 host/daemon 관측을 함께 판단했다. Runtime 목록만으로 모든 플랫폼의 GPU 존재를 판정한 것은 아니다. [Docker 공식 문서](https://docs.docker.com/desktop/features/gpu/)상 Desktop의 Linux container `--gpus` passthrough는 Windows WSL2 경로이며, 다른 플랫폼의 Model Runner GPU 지원은 이 CUDA simulator/model 경로와 다르다. ARM emulation이나 host MPS로 우회하지 않는다. 기존 image는 보존했고 새 image/volume은 만들지 않았다. 과거 exit 125를 이번 결과로 복제하지 않는다. 현재 `resume.py check`는 정상적으로 **exit 3 / RESOURCE_UNMET**에서 멈췄다.

<a id="checkpoints"></a>

## 공개 source와 checkpoint

같은 저자의 **SimpleVLA-RL LIBERO-10(논문/README의 LIBERO-Long) SFT→RL 후보 쌍**을 찾았다. 공식 OpenVLA-OFT continuous-head checkpoint와 임의로 섞지 않는다. 저자 model card는 one-trajectory-per-task SFT 뒤 RL이라고 설명하지만 **B의 parent를 A의 특정 SHA로 연결하는 학습 manifest는 없다.** B config의 옛 경로에 `traj10`도 남아 있어 exact-parent는 미확인이다. 따라서 최초 비교는 공개 SFT/RL 쌍의 *교체*이며 정확한 한 run의 causal training lineage를 주장하지 않는다.

| 항목 | A | B / 확인 결과 |
|---|---|---|
| 공개 model | [Openvla-oft-SFT-libero10-traj1](https://huggingface.co/Haozhan72/Openvla-oft-SFT-libero10-traj1) | [openvla-oft-libero10-traj1-rl](https://huggingface.co/Haozhan72/openvla-oft-libero10-traj1-rl) |
| 고정 revision | `679a2cc1504b905e6cd954a46c80a9408a8ba3e0` | `d44ac12c3431fc1d2a4579d2e768bbeba60054d4` |
| Config / weight index | `OpenVLAForActionPrediction`, 982 parameter keys, bfloat16 표기, 4 shards | 같은 architecture·982 key 집합; float32 표기, 7 shards. Shape/value·실제 load 호환성은 미검증 |
| Index의 tensor bytes | 15,082,474,368 | 30,164,948,736. 다운로드/VRAM 실측 수치가 아님 |
| Normalizer | `libero_10_no_noops`, q01/q99·gripper mask | 파일 bytes 동일, SHA-256 `dbe516987e8124416af39c32d3f39ce2137ccb4e282adc590bb4bcede09fb5e1` |
| Processor/tokenizer | 공개 blob identity 대조 | processor·tokenizer·preprocessor·model code 파일 identity 동일. 실제 registry code loader와 HF remote code는 구분 필요 |
| 입력/행동 후보 계약 | 저자 LIBERO script 기준 단일 224 RGB + language, VLA proprio off | Discrete action decoding, 8×7 chunk, 원 gripper normalize/invert 유지. 두 모델에 동일 decoding 설정 적용 |

[고정 공식 repository](https://github.com/PRIME-RL/SimpleVLA-RL/tree/7c51662df27b586f9e8a1ab35fcf849f2b8852f9)의 `examples/run_openvla_oft_rl_libero.sh`, `rob_rollout.py`, OFT `constants.py`/`modeling_prismatic.py`를 대조했다. **`ROBOT_PLATFORM=LIBERO`를 명시해야 한다.** 이 commit의 constants 자동 감지는 `libero` 인자도 ALOHA로 분기하므로 파일 이름만 믿으면 25×14로 잘못 설정될 수 있다. 원 script는 환경변수를 올바르게 설정한다. 저자 training script의 temperature 1.6은 평가 권고값으로 자동 채택하지 않는다. 동일 결정적 decode를 최초 IO 비교에 쓰고 원 stochastic 평가와는 분리한다.

이 검토에서 weights·PDF는 다운로드하지 않았다. Normalizer hash는 받은 작은 metadata bytes에 대한 실제 hash이고, model shard hash는 HF가 광고한 LFS metadata이며 로컬 검증값이 아니다. CUDA/graphics·image build·실제 step rate·VRAM·checkpoint 로딩은 미검증. 공개 residual checkpoint는 확보하지 못했으므로 **즉시 B+residual-A를 실행할 수 있는 상태가 아니다.** 새 A 학습은 피할 수 있지만 A용 residual 학습은 필요하다.

## 환경 설정 — 출처가 확인된 값과 아직 정해야 하는 값

| 구성 | 재개 목표/현재 경계 |
|---|---|
| 실행 위치 | 사용자가 선택한 NVIDIA 컴퓨터의 **로컬 Docker**. Linux x86-64를 첫 target으로 사용. 다른 지원 플랫폼은 별도 검증 |
| Host infrastructure | Docker Engine, NVIDIA driver, NVIDIA Container Toolkit이 이미 구성되어 있어야 함. 이번에는 host 설치·설정 변경 없음 |
| Python/PyTorch/CUDA 후보 | Python 3.10, torch 2.4.0 + cu124는 pinned [SETUP.md](https://github.com/PRIME-RL/SimpleVLA-RL/blob/7c51662df27b586f9e8a1ab35fcf849f2b8852f9/SETUP.md)의 값. 완성된 dependency lock은 아님 |
| Driver | CUDA 12.4 GA 기준 Linux driver **550.54.14 이상을 재개 목표**로 삼되 GPU 세대·설치 driver 지원을 확인. CUDA 12.x minor compatibility의 525.60.13 조건과 구분하며 특정 model 실행 보증이 아님 |
| 의존성 초안 | [requirements.txt](./requirements.txt): torchvision 0.19.0, transformers 4.40.1, tokenizers 0.19.1, timm 0.9.10, TF CPU 2.15.1, robosuite 1.4.0, MuJoCo 2.3.7 등. 모델 버전은 pinned source 요구를 따르며 나머지는 검증 전 조합. 전체 closure·wheel hash·OS package lock은 미확정 |
| Image recipe | [Dockerfile](./Dockerfile): 공식 CUDA 12.4.0 Ubuntu 22.04 amd64 manifest digest 고정. Registry metadata만 확인했고 image pull/build는 미실행. Python 3.10·CUDA 12.4·import·pip check를 build에서 검사하도록 작성 |
| P0 attention | A/B 모두 `eager`, BF16, `do_sample=false`. Flash Attention/분산 veRL stack을 설치하지 않는 최소 IO 경로. 원 저자 attention backend와 수치 동등성·성능 재현은 주장하지 않음 |
| GPU memory | BF16 base 한 개의 tensor storage만 약 14.05 GiB; activation/KV·A vision/projector·렌더링·allocator는 별도. 24 GiB에서 된다는 보장 없음. 48 GiB급은 여유를 둔 계획 예시일 뿐 측정된 최소 사양/구매 권고 아님 |
| Host RAM·disk | 계획 여유값 RAM 64 GiB·free disk 100 GiB. A/B 공개 tensor 합만 약 42.14 GiB이며 image/cache/temporary loading이 추가됨. 실제 peak와 disk 사용량은 P0에서 기록 |
| Precision/load | A/B 모두 BF16 inference 후보, B FP32 shard의 cast·동등 경로 검증 필요. Quantization/offload로 자동 변경하지 않음. A/B 전체 모델을 동시에 상주시킬 필요는 없음; 순차 load 후 B 단계에는 A vision+projector만 유지하는 구현은 미검증 |
| Rendering | `MUJOCO_GL=egl`, `PYOPENGL_PLATFORM=egl`, `NVIDIA_DRIVER_CAPABILITIES=compute,utility,graphics`; container에서 실제 offscreen frame 확인 |
| 모델 구분 | `ROBOT_PLATFORM=LIBERO`, VLA proprio off, `use_film=false`, 동일 224 RGB processor·deterministic discrete decoder·8×7 actions |
| 통계/행동 | Normalizer key `libero_10_no_noops`; metadata의 action 7·proprio 8차원 확인. Actual state 순서·q01/q99 적용·zero-range 처리 검증 필요 |
| 원격 logging | `WANDB_MODE=disabled`; API key 필요 없음. 공식 분산 RL script를 P0 launcher로 사용하지 않음 |

[CUDA 12.4 공식 release notes](https://docs.nvidia.com/cuda/archive/12.4.0/cuda-toolkit-release-notes/index.html)의 toolkit driver와 minor compatibility를 대조했다. 원 README의 driver 470.161.03·CUDA 12.4 병기는 그대로 호환 보증으로 채택하지 않는다. [NVIDIA Toolkit 안내](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)는 필요한 host 기반 환경의 근거이며 지금 설치를 수행했다는 뜻이 아니다.

**SETUP의 재현성 빈칸:** v0.2.x veRL branch, OpenVLA-OFT/LIBERO의 unpinned clone, 후속 `pip install torch torchvision`, unpinned flash-attn이 있다. 이 지시를 그대로 실행하면 앞서 정한 torch까지 바뀔 수 있다. 전체 PPO/분산 training stack을 무조건 설치하지 않고 P0의 loader·model·LIBERO 경로에 필요한 의존성만 분리한다. 별도 upstream OpenVLA-OFT code가 필요하면 commit을 추가로 고정하며, 그 continuous-head 모델로 현재 discrete checkpoint를 대체하지 않는다.

## 파일·volume 배치와 아직 없는 산출물

Host에는 이 저장소의 문서·재개 코드·작은 실행 결과만 둔다. 외부 source checkout·package·weights·LIBERO assets/init states는 Docker image 또는 named volume 안에서만 준비한다.

| 위치 | 역할 |
|---|---|
| Repository read-only mount `/workspace` | 이 저장소의 계약·재개 코드. `.dockerignore`는 build context를 recipe·직접 의존성 목록·native 코드로 제한 |
| Named volume `vrl_update_cache` → `/cache` | pinned model snapshots·HF cache; `HF_HOME=/cache/huggingface` |
| Image layer `/opt/vrl/LIBERO` | pinned LIBERO source·assets·init states. 별도 assets/build volume은 사용하지 않도록 단순화 |
| Image layer `/opt/vrl` | pinned SimpleVLA source·standalone model package·Python 환경·실제 빌드 시 생성되는 package freeze |
| 지정 결과 mount `/results` | runtime manifest·IO trace·작은 요약. weights·assets·학습 replay 전체를 Git에 넣지 않음 |

지금 volume을 생성하지 않았다. 실제 resolved dependency lock·완성 image ID·weight file sha256·init-state hashes·P0 trace는 **null/미생성**이다. Base image digest와 완성 image ID를 구분한다. `prepare`는 container 안에서 받은 파일을 hash하고 init-state 수·중복을 기록한다. P0에는 ID 0만 필요하며, 50개 미만/중복이면 후속 학습 split을 자격 미충족으로 표시한다. P0 통과가 후속 split 승인도 대신하지 않는다.

<a id="resume"></a>

## NVIDIA 컴퓨터에서 이어갈 순서

1. 이 폴더의 코드·recipe·명세와 공통 source 원장이 포함된 revision을 전달한다. **이번에 commit/push하지 않았으므로 현재 원격 clone에 포함되어 있다고 보장하지 않는다.**
2. `check`가 local Unix endpoint·Linux amd64 daemon·host NVIDIA metadata를 확인한다. Docker/BuildKit endpoint override는 거부하며 비호환이면 다운로드 전에 exit 3으로 끝난다. Host 적격 판정은 CUDA/EGL 통과가 아니다.
3. `build`가 같은 검사를 재실행한 뒤 pinned base에서 `nvidia-smi` 할당 확인 → local Docker image build·pip check·model import를 시도한다. 실패 로그를 먼저 수정하며 자동 재시도하지 않는다. [Docker의 default builder](https://docs.docker.com/build/builders/)를 사용하며 custom remote builder로 전환하지 않는다.
4. `prepare`는 container에서 CUDA/BF16·source SHA를 검사하고 A/B snapshots·실제 파일 hashes·LIBERO init/asset metadata를 준비한다. 약 42.14 GiB의 weight tensor와 image/cache 여유 공간이 필요하다. 실제 dependency freeze와 image ID가 이때 결과에 남는다.
5. `p0`는 네트워크를 끈 container에서 payload hashes 재검사 → EGL/동일 reset·A/B 각 한 query·zero-residual·frozen A encoder·최대 한 chunk 실행을 시도한다. **2 query·2 reset·16 policy steps + 20 warmup = 최대 36 env step 호출**만 허용한다. Encoder 상한 4회에는 두 base query의 vision forward도 포함한다. Simulator 생성 내부 초기화와 명시적 control-step 호출은 구분한다. Full task rollout·residual 학습은 없다.

저장소 루트에서 **각 단계가 exit 0인 경우에만** 다음 명령으로 진행한다. Host Python은 표준 라이브러리로 Docker를 호출할 뿐 payload를 실행하지 않는다.

```bash
VRL_REPRO='work/research_topics/vla_residual_update/재현 방법'
python3 "$VRL_REPRO/resume.py" check
python3 "$VRL_REPRO/resume.py" build --results "$VRL_REPRO/results/target-001"
python3 "$VRL_REPRO/resume.py" prepare --results "$VRL_REPRO/results/target-001"
python3 "$VRL_REPRO/resume.py" p0 --results "$VRL_REPRO/results/target-001"
```

`--gpu 0`이 기본이며 하나의 GPU만 사용한다. 실패하면 해당 `*-host.json`, `.log`, native가 시작된 경우 `.json`을 읽는다. `STOPPED_NO_RETRY`는 실패이고 `HOST_ELIGIBLE_CONTAINER_GPU_UNVERIFIED`/`PAYLOAD_PREPARED_NATIVE_IO_UNVERIFIED`도 P0 통과가 아니다. `P0_IO_PASSED_NOT_POLICY_EVIDENCE`만 IO 검증 통과이며 성능 결과가 아니다. 결과 덮어쓰기와 source/recipe가 바뀐 stale image를 거부한다. 수정 후 의도적 재시도에는 새 결과 directory를 사용한다. 자동 학습·sweep으로 연결하지 않는다.

### P0 adapter가 만족해야 할 구체 명세

- Official pinned code의 모델 class/processor/weights를 명시적으로 연결한다. HF remote code를 묵시적으로 실행하지 않고 사용하는 source를 기록한다.
- 두 reset은 init ID 0·environment seed 0·동일 controller/queue/history로 시작한다. Warmup command는 환경 좌표 `[0,0,0,0,0,0,-1]`이며 gripper 변환을 재적용하지 않는다.
- A/B마다 warmup 10 step 뒤 observation을 읽고 base query 1회로 8×7 chunk를 받는다. 같은 저장 chunk에 zero-residual 합성을 적용하여 원 command와 비교하며 검증용 추가 model query를 만들지 않는다.
- Original adapter가 공개 API에서 unnormalized action만 반환한다면 normalized token decode 값과 action 변환 중간값을 함께 노출하는 wrapper를 구현한다. CLI만 바꿔 normalized residual이 적용되었다고 간주하지 않는다.
- 같은 RGB에서 frozen A vision+projector의 shape·finite 값·dtype·패치 평균, proprio 8차원과 `2d+24` 입력을 확인한다. Feature call 최대 4회; real history/state 순서를 기록한다.
- 정합성 검사 실패 시 env step 전에 멈춘다. 통과 시 각 base의 chunk를 최대 8 step 실행하며 native success/terminal이면 조기 종료한다. Full task success를 요구하거나 전이 성능으로 보고하지 않는다.
- 결과에는 source/container/config/file hashes, reset fingerprint, decode shape, normalization/gripper/clip 비교, actual queries/steps, errors·peak memory를 기록한다. 허용 오차는 dtype와 변환별로 실행 전에 정하고 post-hoc 완화하지 않는다.

### 구현·검증 상태

| 항목 | 지금 상태 | 재개 후 필요한 일 |
|---|---|---|
| 문헌·연구 계약·public A/B revisions | 준비 완료 | 직접 collision의 새 version이 있을 때만 갱신 |
| Local resource check | 현재 비호환 확인 | 다른 컴퓨터에서 재확인 |
| Package lock·image/Dockerfile | 직접 의존성 pin·recipe 초안 작성, build 미검증 | 전체 dependency closure·import/CUDA/EGL·실제 image ID 확보 |
| Native model/encoder/action adapter | [native_p0.py](./native_p0.py) 작성, native 미검증 | 실제 load·전처리·action/state 정합성 및 남은 오류 수정 |
| Assets/init states·weight checksums | Container acquisition/hash 코드 작성, payload 미확보 | 실제 hash·count·중복과 source payload 검증 |
| P0 launcher/trace | [resume.py](./resume.py) 작성, host check 실제 exit 3; native trace 없음 | 호환 컴퓨터에서 상한 내 native IO 검증 |
| 제어·중단 장치 검사 | [test_packet.py](./test_packet.py) 9개 Docker CPU 통과 | 원격/비호환 차단·stale image·계약 drift·상한 검사. CUDA/모델/수치 action 변환 검사 아님 |
| A residual checkpoint·B 적응 trainer | 없음 | P0 이후 별도 P1/P2, 현재 자동 실행 대상 아님 |
| 전이 효과·논문 기여 | 미입증 | 연구 비교와 독립 후속 결과 필요 |

P0 실패는 환경/interface 문제로 기록한다. P1의 sparse RL bootstrap 실패와 P2의 전이 결과를 섞지 않는다. 재현에 필요한 구현이 남아 있다는 사실을 숨기지 않으며, **내부 비실험 검토 완료**와 **실행 준비 완료**를 별도 상태로 유지한다.

2026-11-05 구현 검토에서 pinned 모델의 local-relative import를 분리해 veRL/Ray training stack을 제외했다. 영상 helper는 고정 source에서 함수 정의만 읽어 원 JPEG round-trip·180도 회전·crop을 사용한다. HF remote code는 실행하지 않는다. Native decoder를 한 번 호출하면서 normalized intermediate를 캡처해 같은 chunk의 zero-residual 경로를 비교한다. Float64 action 변환 허용 오차는 `atol=1e-7, rtol=0`으로 고정했으며 BF16 모델 간 수치 동등성을 뜻하지 않는다. Reset wrapper의 무제한 randomization retry를 사용하지 않고 한 번 실패하면 중단한다. 이들은 **작성한 코드의 동작 의도**이며 해당 모델·simulator에서 실행 확인한 사실은 아니다.

