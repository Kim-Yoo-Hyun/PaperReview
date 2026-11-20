# 단일 VLA 강화학습 재현

- Updated: 2026-11-12 KST / 기존 실행 확인: **11/07 GAP-UNIFIED-P0-R1**, 새 문헌/정적 검토: **LANGRET-N1/N2**
- [질문·판정](../내용/README.md#n1-review) · [단일 source·pin·설계 원장](../내용/sources.json)
- **실행 코드·직접 의존성 pin·Docker recipe 작성, CPU 제어 검사 15개 통과, native 실행은 0회.** 실제 image build·CUDA/graphics·model/goal adapter 교정은 미검증이다. 과학적 효과·목표 feasibility를 확인한 상태가 아니다.
- **N2 비실험 검토 완료:** [연구 설계·예산·통계·판단 기준](../내용/README.md#nonexperimental-completion)을 보완했다. 기존 P0 코드·compile 대상 설정·fingerprint는 유지했다. 아래 미래 단계는 P0 통과 후 별도 구현/계약이 필요하며 자동 실행되지 않는다.

**11/12 추가:** [LANGRET의 N1 source 심사](#langret-source-review)와 [N2 모델·측정 경로](#langret-n2-interface)는 새 보존 분석을 위한 정적 검토다. 현재 Docker recipe·RL4VLA/ManiSkill P0가 LIBERO-CF도 지원한다는 뜻이 아니며, 기존 실행 파일·pin·상한은 변경하지 않았다. 새 실험 환경 구성이나 실행은 이번에 하지 않았다.

## 1. 동일 초기화와 학습 대상

N1에서 정한 기준은 [RL4VLA pinned 코드](https://github.com/gen-robot/RL4VLA/tree/de46e0174e7ac310255a2836718fcefab28b8963)와 [공개 warm-up checkpoint](https://huggingface.co/gen-robot/openvla-7b-rlvla-warmup/tree/735fd5d1f4472c4c9f3f998f0e89aa641af5ad03)다. Code commit·metadata SHA256·weight의 원격 LFS SHA256은 `sources.json.n1`에 모았다. Weight hash는 서버 선언값이며 다운로드 후 검증한 값이 아니다.

| 항목 | 고정 설정·경계 |
|---|---|
| 초기 모델 | `gen-robot/openvla-7b-rlvla-warmup`, revision `735fd5d1f4472c4c9f3f998f0e89aa641af5ad03`. 네 shard의 merged model이며 index에 LoRA·value-head key 없음 |
| 초기화 해석 | 병합 warm-up에 **새 rank-32 LoRA + 새 value head**. 원 README의 base OpenVLA + 기존 warm-up LoRA 재개와 parameterization/optimizer가 같다고 주장하지 않음 |
| loader | pinned RL4VLA `OpenVLAForActionPredictionWithValueHead`; `vla_path`는 Docker volume의 고정 snapshot, `vla_load_path`는 빈 값. HF floating auto-map 대신 pinned local class 사용. 예상 value-head missing key 외 mismatch는 중단 |
| normalizer | `config.json.norm_stats.bridge_orig.action`. `warmup.action` 및 `dataset_statistics.json.warmup.action`과 정확히 같음을 JSON 대조. 파일명 때문에 key를 임의 변경하지 않음 |
| processor | pinned Prismatic processor + checkpoint tokenizer 설정. 640×480 RGB uint8 → 두 vision branch의 224×224 resize. Tokenizer binary/weight는 host에 미설치 |
| 행동 | 7 tokens: xyz delta 3, rotation delta 3, gripper 1. 원 bin·q01/q99·mask·gripper threshold 0.5 보존; 임의 gripper 재해석 금지 |
| LoRA | rank 32, alpha 16, dropout 0, gaussian init. Target suffix: `proj,qkv,fc1,fc2,q,kv,fc3,q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj,lm_head`. 실제 matched name·shape·trainable count는 native 확인 필요 |
| value | `vh_mode=a0`: teacher-forcing에서 **첫 action을 예측하는 직전 공백 token** feature. Value branch에만 `hidden_features.detach()` 적용. Action을 이미 본 a6 feature와 섞지 않음 |
| optimizer | AdamW: LoRA lr 1e-4, head lr 3e-3, betas 0.9/0.999, upstream 기본 weight decay 0.01 명시. A/B/C의 초기 LoRA·head·optimizer state·seed 동일 |

Gaussian/zero LoRA 초기화 때문에 첫 backward에서 일부 factor의 gradient는 0일 수 있다. 모든 tensor의 nonzero를 요구하지 않고 policy→공유 표현, value→head, A의 value→공유 표현을 module group별로 확인한다.

## 2. A/B/C와 clipping 통제

원 코드는 policy loss + clipped Huber value loss를 합산한 뒤 **LoRA와 value-head를 함께 norm 10으로 clipping**한다. 별도 optimizer만으로 gradient가 분리되지 않는다. Joint clipping은 B에서도 value-head gradient 크기를 통해 actor update를 바꿀 수 있다.

| 조건 | Value branch | 목적 |
|---|---|---|
| A | `V(h)`, λv=1 | 공동 표현 갱신 |
| B | `V(stopgrad(h))`, λv=1 | 동일 forward/head 학습을 유지하고 shared value gradient만 차단 |
| C | `V(h)`, λv=0.1 | 단순 loss 크기 조정으로 충분한지 확인 |

주 비교는 모두 **LoRA group과 head group을 각각 norm 10으로 clipping**한다. 이 변경은 연구 설계이며 원 논문 그대로의 재현은 아니다. 원 joint clipping의 A0는 호환성 기준·후속 sensitivity다. Clip 이전 gradient와 실제 AdamW parameter delta를 함께 기록한다.

- PPO clip 0.2, Huber delta 10, entropy coefficient 0, γ=0.99, GAE λ=0.95는 원 설정이다. 원 `returns_norm`은 이름과 달리 dtype cast이며 return normalization이 아니다. Advantage는 batch mean/std로 정규화한다.
- C 하나를 이겨도 모든 scale 대안을 배제하지 않는다. 효과가 보이면 dev에서 λ∈{0.01,0.1,1}, train-only return normalization, 필요 시 PPG를 비교한다. Eval 결과로 λ를 고르지 않는다.
- **고정 batch 진단:** 원 instruction·old log-prob·old value·return·advantage를 봉인해 A/B/C에 재사용. 한 update의 직접 효과만 추정한다.
- **On-policy 효과:** arm별 수집 데이터와 critic으로 GAE를 계산. 탐색·데이터 분포의 매개 효과가 포함되므로 고정 batch와 별도 보고한다.
- Instruction을 바꾼 채 원 return을 복제하지 않는다. 잘린 1-step probe의 0 bootstrap을 정상 target으로 사용하지 않는다. 원 wrapper는 `terminated`를 무시하고 `truncated`를 done으로 전달하므로 task horizon 80과 중간 probe cutoff를 구별해야 한다.

## 3. 같은 장면의 두 목표

선택 환경은 `PutOnPlateInScene25MultiCarrot-v1`, WidowX, `obj_set=train`, native `episode_id=0`이다. [환경 코드](https://github.com/gen-robot/RL4VLA/blob/de46e0174e7ac310255a2836718fcefab28b8963/ManiSkill/mani_skill/envs/tasks/digital_twins/bridge_dataset_eval/put_on_in_scene_multi.py#L1689)와 asset metadata에서 아래 후보를 연결했다.

| 역할 | Identity / instruction |
|---|---|
| 원 source index 0 | `001_carrot_simpler` → `put carrot on plate` |
| 다른 visible object index 1 | `002_kitchen shovel_1` → `put kitchen shovel on plate` |
| 공통 receptacle | `001_plate_simpler` |
| 개발 scene | overlay 0, position-config 0, quaternion-config 0, seed 0 |

`MultiCarrot`라는 class명과 달리 서로 다른 물체 종류가 들어 있다. **다른 episode ID로 source/extra를 바꾸면 pose와 초기 높이까지 달라져 동일 장면 쌍이 아니다.** 한 번 settle한 상태에서 goal binding만 바꾸고 같은 RGB를 두 instruction에 넣는 adapter를 `probe.py`에 작성했다. 실제 simulator에서의 동일성은 P0에서 검사한다.

목표 전환 시 `select_carrot_ids`, `source_obj_name`/planner map, 해당 객체 settled quaternion/bbox, grasp counter·episode stats·wrapper reward history를 정합화한다. Pose·velocity·robot/controller state·camera·overlay·RNG는 유지한다. P0는 한 관측을 재사용하는 query까지만 한다. 전체 simulator/controller buffer의 분기 복원은 후속 rollout 전에 별도 검증한다.

**확보한 것은 source-defined 목표 후보이며, 두 목표의 성공 가능성 witness는 아니다.** 두 번째 물체의 reachability·collision·planner 성공과 warm-up의 기본 조작 능력은 미확인이다. 제공 planner entry도 두 목표의 성공 기록이 아니다. Warm-up은 carrot 중심이므로 기존 목표 구분 능력을 가정할 수 없다. 필요하면 “능력 손상” 대신 “목표 구분 습득”으로 질문을 수정한다.

### 평가와 분할

- Native success는 선택 source–plate bbox 위치·높이 및 contact force(코드 threshold 0.03)다. Release·stable placement를 보장하는 정의가 아니므로 “안정적으로 놓기” 성공으로 바꾸어 쓰지 않는다.
- Reward는 grasp 0.1 + 연속 grasp 0.1 + success∧grasp 1.0의 **점수 차분**. 여기서 `info`의 grasp·연속 grasp flag는 episode 내 OR 누적이며 현재 순간 상태와 다르다. 모든 arm에 동일 함수·goal binding·history를 사용한다. Image-only value는 이 이력을 모두 볼 수 없으므로 value 오차를 곧바로 언어 정보 손상으로 해석하지 않는다.
- Goal selection은 두 객체의 `agent.is_grasping`을 읽는 side-effect 없는 observer를 사용한다. 후속 event 집계는 최초 grasp의 목표/오목표/동시/없음을 기록하며 동시 grasp를 나중 단독 grasp로 대체하지 않는다. Native `evaluate()` 재호출은 counter를 바꾸므로 두 목표 평가용으로 반복 호출하지 않는다.
- Primary는 목표 균등 native task success의 A−B 차이 하나로 고정한다. 80-step 내 native success event·마지막 step 성공·최초 correct/wrong/simultaneous/no-grasp·목표별 결과와 pair 양쪽 성공은 [N2 정의](../내용/README.md#nonexperimental-completion)를 따른다. 현재 순간 observer를 시간적 first-event 집계 구현으로 간주하지 않는다.
- Split 초안: 같은 두 object·plate·overlay 0·quat 0에서 pos 0–3 dev, 4–19 train, 20–27 eval 후보. **역할 swap으로 같은 배치가 반복될 수 있으므로 unordered geometry key로 전역 dedup한 실제 manifest를 봉인해야 한다. 아직 미실체화 초안이다.** 중복 후보는 뒤쪽에서 제외하고 사전 순서의 다음 고유 배치로 보충; eval 행동으로 선택하지 않음.
- 같은 scene family의 배치 holdout만 주장한다. Unseen object/embodiment나 pretraining contamination-free가 아니다. 단일/multi-object 대조는 geometry도 달라 언어 특이성을 식별하지 못한다. N2의 목표 배정 H/L factorial은 별도 후속 설계이며 현재 adapter에 구현되지 않았다.

## 4. 최소 probe와 후속

| 단계 | 상한·통과 조건 | 현재 |
|---|---|---|
| P0-I: IO/goal binding | 1 env, constructor 포함 reset≤2, policy query≤2, control step 0, settle 포함 physics≤8,000. 두 instruction 외 RGB·상태 동일, 다른 target binding, loader/normalizer 교정 | 구현 초안 작성·native 미검증 |
| P0-G: gradient routing | P0 관측·action 하나, A/B/C 독립 restore. Teacher-forced forward≤12, backward≤8, optimizer step≤3. A/B 초기 logits/value 동일, B value-only shared grad 0, head·policy 경로 유효. 인공 nondegenerate value target은 **wiring fixture**로만 사용 | 구현 초안 작성·native 미검증 |
| P1: feasibility/competence | 목표별 planner/기본 정책·full-state branch. N2 계획 한도: dev 4 layouts × 2 goals × (planner 1 + base 2 seeds) = 24 episodes, 각각 ≤80 control steps | 미구현. P0 측정 후 query/physics/wall-time 한도와 실행 manifest 추가; 자동 실행 안 함 |
| 고정 transition 진단 | 정상 instruction/reward/timeout으로 수집한 batch에서 한 update. P0 인공 label 재사용 금지 | P1 이후 |
| On-policy pilot | 동일 step·update budget, 독립 train seeds, frozen eval. N2 최초 비용 점검 계획은 A/B/C × 3 seeds × ≤10,000 control steps = ≤90,000 training steps | 미구현·미실행. Eval/tuning 비용은 별도, 수렴 보장/실행 승인 아님. P0/P1 비용 확인 후 별도 계약 |

P0 실패 시 학습을 시작하지 않고 해당 구현만 교정한다. 통과도 연구 가설 입증이 아니다.

## 5. Docker 환경과 clone 재개

**11/07 현재 컴퓨터에서 재확인:** context `desktop-linux`, local Unix socket, daemon 동작, host Darwin/arm64·RAM 16 GiB, daemon **aarch64·약 7.65 GiB**다. `resume.py check`는 **exit 3 / RESOURCE_UNMET**로 중단했다. [이번 명령·실측 결과](./results/2026-11-07-resume-check/local_check.json)를 보존했다. 아키텍처 조건에서 중단했으므로 NVIDIA allocation·native build·weight/asset download는 시도하지 않았다. Docker daemon 고장이 아니라 이 실험이 요구하는 Linux x86-64/NVIDIA 환경과의 불일치다.

11/06 [이전 실측](./results/2026-11-06-preparation/local-check/local_check.json)과 CPU 제어 검사 15개는 당시 기록이다. 그때 사용한 임시 container 2개는 제거했고 새 image는 만들지 않았다. 11/07에는 실행 코드·설계 fingerprint가 같음을 파일 대조로 확인했으므로 같은 CPU 제어 검사를 반복하지 않았다.

| 항목 | 준비 값 / 미확인 |
|---|---|
| OS/GPU | Linux x86-64, NVIDIA CUDA 12.1·BF16·graphics. 저자 README의 80 GB 한 장 또는 40 GB 두 장은 실행 예시이며 **P0 최소 VRAM 측정값 아님** |
| RAM/driver | daemon RAM 32 GiB는 준비를 위한 보수적 하한, driver 530.30.02 이상을 선택. Free VRAM > BF16 weight 약 15.08 GB는 필요 하한일 뿐 activations/optimizer/simulator 실행 보장이 아님 |
| Python/torch | Python 3.10, torch 2.2.0+cu121, torchvision 0.17.0. 현재 P0 recipe는 torchaudio를 설치하지 않음 |
| VLA | transformers 4.40.1, peft 0.11.1, timm 0.9.10, tokenizers 0.19.1, sentencepiece 0.1.99, accelerate 0.30.1. 나머지 직접 pin은 `requirements.txt` |
| attention | flash-attn 2.7.4.post1; upstream cp310/cu12/torch2.2/cxx11abiFALSE wheel |
| simulation | pinned repo ManiSkill/SimplerEnv; sapien 3.0.0.b1, gymnasium 0.29.1, NumPy <2. CUDA physics·Vulkan/default shader smoke 필요 |
| IO | `arm_pd_ee_target_delta_pose_align2_gripper_pd_joint_pos`, physics 500 Hz / control 5 Hz, RGB+segmentation, `3rd_view_camera`; policy에는 RGB+instruction만 전달 |
| assets | repo `ManiSkill/mani_skill/assets/carrot/` meshes/textures + `bridge_v2_real2sim`. Metadata만 확인; payload hash/전체 resource closure 미확인 |
| disk | checkpoint payload 약 15.1 GB 외 source assets·image layers·download cache 여유 공간 필요. 전체 디스크 최소량은 아직 측정하지 않았으며 build/prepare의 실제 사용량을 기록해야 함 |
| storage | Source는 image 내부 `/opt/unified/RL4VLA`·`/opt/unified/widowx`. 작업 소유 volume `paper-unified-p0-<packet SHA 앞 16자>` 하나를 `/cache`에 mount하며 weights는 `/cache/model/<checkpoint revision>`, assets는 `/cache/assets`, archive는 `/cache/downloads`에 저장. 환경변수 `HF_HOME=/cache/huggingface`. 결과만 repo-relative `재현 방법/results/`에 bind. Host dependency/weights/assets 설치 금지 |
| 남은 lock | Base image digest·source commit·accelerate/tyro 등 직접 pin은 이미 고정. 남은 것은 실제 apt/transitive dependency 해석·flash wheel 관측 hash·native build/driver 호환성·다운로드한 payload checksum·memory peak다. P0에 불필요한 dlimp/TF/RLDS는 설치하지 않음 |

<a id="resume"></a>
## 6. Clone 후 실행 명령

Repository root에서 실행한다. `resume.py`는 host stdlib로 Docker 명령·파일 검증만 제어한다. 의존성·model·simulator·autograd는 container 내부에서 실행한다. 결과 경로는 **각 명령마다 새 디렉토리**로 지정한다.

**전달 전제 — 11/07 확인:** 현재 `git ls-files`와 `git ls-tree HEAD` 모두 이 주제의 파일을 포함하지 않는다. 따라서 현재 HEAD만 clone하면 아래 실행 파일이 없다. 이 주제의 `내용/`과 `재현 방법/`을 포함한 revision을 전달하거나 전체 주제 폴더를 함께 전달한 뒤 재개해야 한다. 이번 작업은 commit/push나 다른 컴퓨터의 clone을 수행하지 않았다. 필요한 실행 입력은 `내용/sources.json`, `재현 방법/{resume.py,probe.py,Dockerfile,requirements.txt}`이며 과거 결과 파일은 실행 전제는 아니다. 문서·제어 검사·이력까지 보존하려면 두 폴더를 함께 전달한다.

전달 뒤 아래는 **파일/계약 동일성만** 확인한다. Host에 package를 설치하거나 model을 실행하지 않는다. 불일치하면 현재 원장의 검증 이력과 전달 파일부터 대조한다.

```bash
python3 -B - <<'PY'
import json, runpy
from pathlib import Path
topic = Path('work/research_topics/unified_vla_rl')
launcher = runpy.run_path(str(topic / '재현 방법/resume.py'), run_name='packet_inspection')
source = json.loads((topic / '내용/sources.json').read_text())
expected = source['p0_preparation']['validation']['tested_packet_sha']
actual = launcher['fingerprint']()
assert actual == expected, '실행 파일/계약이 이전 제어 검사 대상과 다름'
print('Packet files match:', actual)
PY
```

```bash
python3 'work/research_topics/unified_vla_rl/재현 방법/resume.py' check --results 'work/research_topics/unified_vla_rl/재현 방법/results/resume-check'
python3 'work/research_topics/unified_vla_rl/재현 방법/resume.py' build --results 'work/research_topics/unified_vla_rl/재현 방법/results/resume-build'
python3 'work/research_topics/unified_vla_rl/재현 방법/resume.py' prepare --results 'work/research_topics/unified_vla_rl/재현 방법/results/resume-prepare' --gpu 0
python3 'work/research_topics/unified_vla_rl/재현 방법/resume.py' p0 --results 'work/research_topics/unified_vla_rl/재현 방법/results/resume-p0' --gpu 0
```

각 명령이 성공한 뒤 다음 명령을 실행한다. 자원 거부 exit 3에서는 build/download/native 실행을 진행하지 않는다. 조건 충족 시 최소 P0까지 실행한다. 원격 endpoint·Docker override는 차단한다. 다른 GPU를 쓸 때는 모든 명령에 같은 `--gpu`를 지정한다.

- **Build:** pinned CUDA image·RL4VLA/WidowX commit, 직접 dependency pin, standalone HF/PEFT·simulator를 설치한다. Source file hash·import·`pip check` 뒤 resolved Python/system package 목록을 image 안에 기록한다. Full training의 TF/RLDS/dlimp/datasets/wandb를 설치하지 않는다. P0에는 불필요하기 때문이다.
- **Prepare:** container CUDA/BF16/Vulkan 검사 후 checkpoint 4 shards·processor/normalizer·bridge assets의 size/hash를 검증한다. Weight·assets는 task 소유 Docker volume에만 저장한다. 준비된 payload와 packet hash가 다르면 중단한다.
- **P0:** network 없이 실제 scene의 두 goal binding·RGB/물리 상태 동일성, action decoding, 4개 gradient 경로 검사, A/B/C의 각 1회 disposable update를 검사한다. Update 후 초기 trainable parameter를 복원하고 학습 weight를 저장하지 않는다. 총 7 teacher forwards·7 backwards·3 paired optimizer updates를 사용하는 구현이며 계약 상한 12/8/3 안에 있다. 한 paired update는 actor/head optimizer 두 번의 step을 포함한다.
- Packet hash가 image label과 다르면 재빌드를 요구한다. Timeout은 build 2h / prepare 1h / P0 20min이며 자동 재시도·학습 확대는 없다. 실행 container는 종료/실패 시 정리하고 사용자 image/volume은 삭제하지 않는다.

**의존성 lock의 한계:** base image digest·source commit·checkpoint hash·직접 package version은 고정했다. OS apt/transitive wheel의 실제 해석과 flash-attn release wheel의 checksum은 첫 native build 전에는 확정되지 않는다. GitHub release API가 digest를 제공하지 않아 build 시 실제 SHA256을 별도 기록한다. 따라서 이 recipe를 완전한 bitwise 재현 lock이라고 부르지 않는다. 첫 성공 image ID·resolved package 목록·wheel hash·payload hash가 실제 runtime 증거다.

<a id="preparation-history"></a>
## 7. 이번 확인과 남은 검증

| 구분 | 결과 |
|---|---|
| 작성 | [Dockerfile](./Dockerfile), [직접 pin](./requirements.txt), [host launcher](./resume.py), [goal/observer/gradient probe](./probe.py), [제어 검사](./test_packet.py) |
| source 원장 | [단일 JSON](../내용/sources.json)의 `n1`은 당시 설계 이력, `p0_preparation`은 현재 준비 상태. Build용 plan은 여기서 임시 생성하며 별도 편집본을 두지 않음 |
| 실제 실행 | 11/07 `resume.py check` 자원 차단, native 실행 0회. 11/06 기존 local ARM Docker의 stdlib 제어 검사 15/15는 [이전 결과](./results/2026-11-06-preparation/control-tests/control_tests.json)이며 이번 재실행 아님. 11/09 raw test log·image/exit metadata를 같은 JSON에 통합 |
| 이번 준비 대조 | 실행 코드 5개와 compile 대상 계약/fingerprint 동일. README의 storage·torchaudio·이미 고정된 dependency 설명을 실제 recipe에 맞춰 수정. 현재 HEAD에 실행 자료 미포함 확인; 전달 후 파일 동일성 확인 명령 추가 |
| 제어 검사 범위 | 0-step/최대 query guard, evaluation cache, 변조 payload·archive·stale image·원격 endpoint 차단, value hook 수명·제거, 코드 parsing. Tensor autograd나 물리 모델의 대용 실험 아님 |
| 미검증 | native dependency closure/build, GPU allocation·BF16/Vulkan, 실제 parameter matching·gradient·입출력 교정, P0 latency/peak VRAM |
| P0 밖의 미구현 | 실제 목표별 feasibility/기본 정책 competence, full-state/controller 분기 복원, 분할 실체화, 정상 transition batch, on-policy 학습과 연구 효과 |

Goal adapter는 reset 상태에만 적용한다. 원 reward의 누적 history와 future wrapper 연결까지 구현한 training adapter가 아니다. Goal observer는 현재 grasp만 읽으며 최초 grasp event 집계는 rollout 단계에서 추가해야 한다. N1의 split 후보를 실제 학습/평가 episode로 materialize하지 않았다.

**기존 native 후속: GAP-UNIFIED-P0.** 호환 local NVIDIA 컴퓨터에서 자원 재확인 → build → prepare → P0. 실패하면 최초 실패 단계와 log를 보존하고 그 부분만 교정한다. P0 성공은 연결 검증이지 연구 효과·출판 가치의 증거가 아니다. 원격 게시·다른 컴퓨터 clone은 아직 확인하지 않았다. 현재 선택된 후속은 [TODO](../../../../TODO.md)의 LANGRET-P0이며 [별도 모델 경로의 준비 결과](#langret-p0-preparation)를 따른다.

<a id="langret-source-review"></a>

## 8. LANGRET-N1 공개 source 심사 — 실행 자료 아님

**2026-11-12:** [VLA-CF revision `8280a500a01f7f7d45efe202cb416ca362aa8c1a`](https://github.com/yuffish/VLA-CF/tree/8280a500a01f7f7d45efe202cb416ca362aa8c1a)의 tree 2,016 entries, 아래 관련 text/config 19개와 OFT의 작은 metadata 2개를 읽었다. 외부 코드를 import·실행하지 않았다. [공통 source 원장](../../../sources/vla_masters_gap_scout_2026-11-12.json)의 `n1_review`가 경로·SHA256·확인 절과 미확인을 소유한다. Revision은 **정적 검토 identity**이며 실행 지원을 확인한 runtime pin이 아니다.

### 두 목표쌍 후보

| 후보·같이 사용할 장면 | A / B 지시 초안 | A / B 성공 predicate | Source에서 확인한 것 |
|---|---|---|---|
| **OBJ-01**, `libero_cf_spatial/01-pick_up_the_cookie_box_and_place_it_on_the_plate.bddl` | `pick up the cookie box and place it on the plate` / `pick up the ramekin and place it on the plate` | `on cookies_1 plate_1` / `on glazed_rim_porcelain_ramekin_1 plate_1` | [BDDL L109–132](https://github.com/yuffish/VLA-CF/blob/8280a500a01f7f7d45efe202cb416ca362aa8c1a/libero/libero/bddl_files/libero_cf_spatial/01-pick_up_the_cookie_box_and_place_it_on_the_plate.bddl#L109)에서 두 물체·plate·서로 다른 초기 region; [condition JSON](https://github.com/yuffish/VLA-CF/blob/8280a500a01f7f7d45efe202cb416ca362aa8c1a/libero/libero/conditions/libero_cf_spatial.json)에서 두 predicate |
| **DEST-05**, `libero_cf_long/05-put_the_yellow_and_white_mug_on_the_left_plate.bddl` | `put the yellow and white mug on the left plate` / `put the yellow and white mug on the right plate` | `on white_yellow_mug_1 plate_1` / `on white_yellow_mug_1 plate_2` | [BDDL L66–87](https://github.com/yuffish/VLA-CF/blob/8280a500a01f7f7d45efe202cb416ca362aa8c1a/libero/libero/bddl_files/libero_cf_long/05-put_the_yellow_and_white_mug_on_the_left_plate.bddl#L66)에서 같은 mug·두 plate·left/right region binding; [condition JSON](https://github.com/yuffish/VLA-CF/blob/8280a500a01f7f7d45efe202cb416ca362aa8c1a/libero/libero/conditions/libero_cf_long.json)에서 두 predicate |

각 pair의 A/B는 **한 BDDL을 공유**하도록 설계한 연구용 대조다. 서로 다른 task ID의 별도 초기 배치를 같은 scene으로 취급하지 않는다. Focused suite는 원 대상 제거가 있어 제외했다. 좌우가 실제 카메라·로봇 기준에서 어떻게 보이는지와 목표의 물리적 도달 가능성은 렌더/실행 전 미확인이다.

연결할 init source는 각각 같은 stem의 `.pruned_init`이다. Tree metadata의 Git blob ID는 OBJ `543deb5f5c1d2ca29426a7b77964c9273f71197d`(44,271 bytes), DEST `0c78a021a8a4be6bd9b7670064fa4437f829a9b7`(41,775 bytes)다. **파일 payload를 받거나 `torch.load`하지 않았으므로 row 수·row hash·값·성공 witness는 없다.** N1 당시 paired runner는 미구현이었다. 아래 P0-PREP에서 같은 row·settle·seed와 state/RGB/일부 controller 필드를 비교하는 코드를 작성했으나 native 동작과 완전한 controller-state 복원은 미검증이다.

### 공개 평가기를 그대로 사용하지 않는 이유와 필요한 연결

1. **Prompt 경로:** [benchmark L45–86](https://github.com/yuffish/VLA-CF/blob/8280a500a01f7f7d45efe202cb416ca362aa8c1a/libero/libero/benchmark/__init__.py#L45)는 파일명에서 language를 만들고, [eval L227–244](https://github.com/yuffish/VLA-CF/blob/8280a500a01f7f7d45efe202cb416ca362aa8c1a/eval/main_cf.py#L227)는 그 하나를 `prompt`로 보낸다. Conditions의 모든 목표가 각각 policy 지시로 실행되는 구조가 아니다. A/B를 명시적으로 바인딩해야 한다.
2. **Goal 경로:** OBJ의 기본 BDDL goal은 bowl-on-plate, DEST는 porcelain mug/left **AND** yellow mug/right다. [eval L132–161](https://github.com/yuffish/VLA-CF/blob/8280a500a01f7f7d45efe202cb416ca362aa8c1a/eval/main_cf.py#L132)은 condition 목록 전체를 OR 종료로 등록한다. [문제 class L135–154](https://github.com/yuffish/VLA-CF/blob/8280a500a01f7f7d45efe202cb416ca362aa8c1a/libero/libero/envs/problems/libero_tabletop_manipulation.py#L135)는 custom 목록이 있으면 기본 conjunction을 대체한다. 따라서 `done`이나 OR 성공은 지정 지시 이행과 다르다.
3. **후속 설계에 쓸 interface:** `evaluate_conditions([A,B,...])`로 다른 목표도 관찰하면서 `set_success_any_conditions([target])`에는 지정 목표 하나만 넣는 경로를 source에서 확인했다. Base reward와 done은 `_check_success()`를 사용한다. 실제 실행에서 지시별 reward/종료가 일치하는지 교정해야 하며 예외를 조용히 삼켜 원 goal로 돌아가는 경우는 유효 결과로 세지 않는다. N1에서는 launcher나 adapter를 작성하지 않았으며 후속 구현 범위는 아래 P0-PREP에 기록한다.
4. **측정 의미:** [`On` predicate](https://github.com/yuffish/VLA-CF/blob/8280a500a01f7f7d45efe202cb416ca362aa8c1a/libero/libero/envs/predicates/base_predicates.py#L62)는 target의 `check_ontop`을 호출한다. [Object check L78–94](https://github.com/yuffish/VLA-CF/blob/8280a500a01f7f7d45efe202cb416ca362aa8c1a/libero/libero/envs/object_states/base_object_states.py#L78)는 상대 높이·접촉·xy 거리 조건이다. Gripper release·장시간 안정적 placement를 보장하지 않는다. 접촉/touch와 goal completion을 분리한다.
5. **오목표와 회복:** 두 목표가 같은 rollout에서 차례로 성립할 수 있다. 다른 목표를 먼저 수행한 것을 진단으로 남기되, 자연 지시에 없는 “다른 물체는 절대 움직이지 말라”를 임의 성공 조건으로 추가하지 않는다. 원 OR 종료와 target-only 종료는 회복 기회도 달라 N2에서 평가 지평·첫 사건/최종 결과를 정해야 한다.

### 지원 모델·normalizer·KL의 경계

| 확인한 공개 경로 | 입출력·metadata 확인 | 남은 경계 |
|---|---|---|
| π₀.₅ `pi05_libero`, `gs://openpi-assets/checkpoints/pi05_libero` | [serve default L78–81](https://github.com/yuffish/VLA-CF/blob/8280a500a01f7f7d45efe202cb416ca362aa8c1a/openpi-cf/scripts/serve_policy.py#L78), [config](https://github.com/yuffish/VLA-CF/blob/8280a500a01f7f7d45efe202cb416ca362aa8c1a/openpi-cf/src/openpi/training/config.py#L764): horizon10, two RGB·8D state·prompt, 7D output, checkpoint assets의 norm stats를 로드 | URI·source 경로만 확인. Weight/normalizer payload identity·실제 출력·두 목표 능력 미확인. Flow action L2·vector-field loss를 exact KL로 해석하지 않음 |
| [OpenVLA-OFT checkpoint](https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-spatial-object-goal-10/tree/638918f3d1c2e43a39a8a20772bdb8b91835e4b7) | HF revision `638918…4b7`, 공개 여부·파일 목록·config/statistics JSON 확인. [Serving config](https://github.com/yuffish/VLA-CF/blob/8280a500a01f7f7d45efe202cb416ca362aa8c1a/openvla-oft-cf/serving/openvla_oft_policy.py#L83): L1 regression, diffusion false, two RGB·8D proprio. `libero_spatial_no_noops`/`libero_10_no_noops` action q01/q99/mask 존재 | Weight·action head·projector 미다운로드/미실행. Normalizer가 없으면 첫 key로 fallback하는 source는 후속 비교에서 허용하지 않을 계획. OFT 기본 회귀 head는 기존 U1 AR token 정책과 다름 |
| 기존 U1 RL4VLA AR/ManiSkill | 위 1–3절의 고정된 기존 계약 | 여기의 LIBERO 두 pair·OFT/flow server와 직접 호환되지 않음. Categorical KL이 필요하면 실제 AR forward/log-prob와 task 지원을 별도 대조 |

공개 CF 보고에서 OFT의 대체 지시 성공이 낮다는 사실도 두 선택 pair의 학습 전 능력을 보장하지 않는다. 평균 benchmark 수치를 개별 scene 성공 witness로 승격하지 않았다. 위 표는 N1에서 살핀 경로이며, N2의 선택은 아래 별도 RL 변형이다.

<a id="langret-n2-interface"></a>

## 9. LANGRET-N2 선택 경로와 다음 구현 범위

**2026-11-12 / N2 완료 당시 설계·정적 검토 범위.** [비교 설계](../내용/README.md#langret-n2)가 연구 질문·분할·baseline·예산의 소유 문서이며, source identity와 확인 범위는 [공통 원장 `n2_review`](../../../sources/vla_masters_gap_scout_2026-11-12.json)에 있다. N2 당시 runtime manifest·Docker image·launcher·native 결과는 없었다. 후속 P0-PREP의 작성/검사 결과는 [10절](#langret-p0-preparation)을 따른다. 아래 경로는 실험 재현을 완료했다는 뜻이 아니다.

### 선택한 구현의 확인 위치

- Repository: [PRIME-RL/SimpleVLA-RL](https://github.com/PRIME-RL/SimpleVLA-RL/tree/7c51662df27b586f9e8a1ab35fcf849f2b8852f9), revision `7c51662df27b586f9e8a1ab35fcf849f2b8852f9`, tree326 entries·truncated=false. RLinf/openvla 본 저장소는 대안 발견/설정 대조에만 사용했고 이 실행 경로와 섞지 않는다.
- Checkpoint: [Haozhan72/Openvla-oft-SFT-libero-spatial-trajall](https://huggingface.co/Haozhan72/Openvla-oft-SFT-libero-spatial-trajall/tree/0a051b39aaebd3fc509fe2aba8bc7e60100e09f5), revision `0a051b39aaebd3fc509fe2aba8bc7e60100e09f5`. Public/ungated·파일 목록과 `config.json`/`dataset_statistics.json`만 확인했다. Weight/tokenizer payload는 받지 않았으며 model card가 없어 세부 SFT membership은 확정하지 않았다.
- Simulator source: N1의 VLA-CF revision·OBJ-01 BDDL/predicate. **SimpleVLA-RL의 표준 LIBERO collector와 CF가 바로 호환된다는 근거는 없다.** Backend 연결·BDDL path·조건 주입·reset/RGB/controller 교정이 필요하다.

| Source 위치 | 확인한 사실·후속 구현 주의 |
|---|---|
| [model L1595–1748](https://github.com/PRIME-RL/SimpleVLA-RL/blob/7c51662df27b586f9e8a1ab35fcf849f2b8852f9/verl/utils/vla_utils/openvla_oft/modeling_prismatic.py#L1595), L1992–2010 | Action placeholder를 zeroing한 forward 뒤 `[-320:-64]`의 256 logits를 temperature로 나눠 categorical sampling. 56 tokens→8×7 actions. 원 L1 head 호출을 KL 대상으로 바꾼 것이 아니라 별도 공개 discrete 경로를 선택 |
| [actor L139–171, L202–233](https://github.com/PRIME-RL/SimpleVLA-RL/blob/7c51662df27b586f9e8a1ab35fcf849f2b8852f9/verl/workers/actor/dp_rob.py#L139) | 같은 vocab slice·token offset·temperature로 log-prob 계산. 실제 sampling/재채점 수치 일치·padding·LoRA wrapper 동작은 미확인. `dp_actor.py`의 일반 언어모델 경로를 로봇 actor 경로로 오인하지 않음 |
| [collector L334–417](https://github.com/PRIME-RL/SimpleVLA-RL/blob/7c51662df27b586f9e8a1ab35fcf849f2b8852f9/verl/workers/rollout/rob_rollout.py#L334), L429–434·L484–488·L933–950 | Standard task prompt/init, settle, 512-step limit, gripper binarize/invert, 실제 finish step. 새 A/B prompt·target success·실행 prefix·물리 step 계수는 별도 연결해야 함 |
| [loader L195–246](https://github.com/PRIME-RL/SimpleVLA-RL/blob/7c51662df27b586f9e8a1ab35fcf849f2b8852f9/verl/workers/fsdp_workers.py#L195) | `dataset_statistics.json`을 읽어 `norm_stats`를 교체하고 LoRA를 붙이는 경로가 있음. Config 내부 norm_stats에는 LIBERO key가 없고 별도 statistics에는 `libero_spatial_no_noops`가 있으므로 전자를 그대로 쓰면 안 됨. Actor·rollout 양쪽 동일 hash/key를 강제할 계획 |
| [constants L27–32, L70–98](https://github.com/PRIME-RL/SimpleVLA-RL/blob/7c51662df27b586f9e8a1ab35fcf849f2b8852f9/verl/utils/vla_utils/openvla_oft/constants.py#L27) | LIBERO chunk8/action7/BOUNDS_Q99. 환경 변수 없는 CLI 추론에 `libero`→ALOHA 분기가 있어, 향후 `ROBOT_PLATFORM=LIBERO`를 명시하고 로드된 상수를 검증해야 함. 이번 실행으로 발견한 오류는 아님 |
| [overwrite script L21–35](https://github.com/PRIME-RL/SimpleVLA-RL/blob/7c51662df27b586f9e8a1ab35fcf849f2b8852f9/examples/overwrite_vla_ckpt_utils.sh#L21) | Checkpoint의 Python 파일을 복사·교체하는 공식 경로. 원 payload를 변경하지 않고 Docker 내부의 분리된 runtime copy에서 revision/hash를 기록할 계획. 스크립트는 실행하지 않음 |
| [ray_trainer L85–118](https://github.com/PRIME-RL/SimpleVLA-RL/blob/7c51662df27b586f9e8a1ab35fcf849f2b8852f9/verl/trainer/ppo/ray_trainer.py#L85), [dp_rob L499–515](https://github.com/PRIME-RL/SimpleVLA-RL/blob/7c51662df27b586f9e8a1ab35fcf849f2b8852f9/verl/workers/actor/dp_rob.py#L499) | Reference log-prob reward penalty와 old/current PPO 추정값은 존재하나 N2의 명시적 forward KL loss와 다름. B3 loss·B4 replay loss·고정 bank 평가기는 미구현. `kl_coef`를 켜는 것만으로 N2 구현 완료라고 하지 않음 |

### N2에서 정한 P0-PREP 범위 — 아래 10절에서 처리

1. **현 로컬 Docker 조건 확인:** endpoint/daemon·OS/architecture·메모리·NVIDIA allocation/CUDA·EGL를 실제 컴퓨터에서 확인한다. N2에서는 환경을 재측정하지 않았으며 과거 Mac 결과를 오늘의 결과로 쓰지 않는다.
2. **재개 자료:** Linux x86-64/NVIDIA용 image digest, Python/PyTorch/transformers/peft/MuJoCo/robosuite/LIBERO 의존성 closure, 위 세 source revision, checkpoint/tokenizer/processor/statistics와 init/asset hash, mount와 저장소 상대 경로를 봉인한다. 아직 version 충돌·최소 VRAM·build/import를 검증하지 않았으므로 구체적인 미검증 package pin을 완료된 환경으로 쓰지 않는다. Source/weights는 Docker 내부에만 설치한다.
3. **단일 IO 검사 구현:** OBJ-01의 dev row 하나, A/B prompt·target를 명시하고 singleton 성공 조건을 등록한다. 초기 target=false, 동일 reset의 state/RGB 확인, 한 chunk sampling과 같은 입력/응답의 재채점, 정상 log-prob와 실행 후 normalizer·gripper mapping을 저장한다. Bool predicate를 강제로 바꾼 fixture와 실제 장면 event를 구분한다. 두 query만으로 placement 능력을 검증했다고 하지 않는다.
4. **상한·실패 처리:** [N2 P0 상한](../내용/README.md#langret-n2)을 코드로 강제한다. Constructor reset·settle·physics도 집계하고 미계수면 중단. 조건이 맞으면 그 최소 IO까지 수행, 자원이 부족하면 portable 준비와 정확한 실패 단계만 남긴다. 큰 학습·능력 pilot을 이어서 자동 실행하지 않는다.

N2 당시 완료 범위는 **문헌/코드 경로 선택·비교 명세**, 실제 실행 확인은 **0**이었다. 후속 준비는 아래 전용 명령을 사용한다. 기존 U1 launcher를 새 경로의 실행 명령으로 재사용하지 않는다.


<a id="langret-p0-preparation"></a>

## 10. LANGRET-P0-PREP — 실행 준비 결과와 재개

**2026-11-12: 준비 자료 작성·Docker 제어 검사 완료, native 검증 대기.** 현재 Mac의 local Docker는 정상이나 `aarch64`, daemon 메모리8,218,034,176 bytes(약7.65GiB)다. 기존 image의 `--gpus all` 할당은 **exit125 / `could not select device driver "" with capabilities: [[gpu]]`**로 실패했다. 새 launcher의 `check`는 **exit3**으로 build/download 전에 중단했다. CUDA/EGL·정책/물리·gradient 실행은 **0회**다. 상세 명령·결과·source/해시는 [공통 원장 `p0_preparation`](../../../sources/vla_masters_gap_scout_2026-11-12.json)에 통합했다.

### 준비 artifact와 환경

| 항목 | 고정 내용·검증 경계 |
|---|---|
| 실행 파일 | [langret_resume.py](./langret_resume.py), [langret_probe.py](./langret_probe.py), [langret.Dockerfile](./langret.Dockerfile), [직접 dependency pin](./langret_requirements.txt), [제어 검사](./test_langret.py). 기존 U1 파일은 변경하지 않음 |
| 단일 설정 원장 | 공통 JSON의 `p0_preparation.runtime_plan`. 별도 편집용 manifest 없음. Launcher가 plan과 실행 파일4개의 SHA256으로 image/cache identity를 만들고 build용 `plan.json`을 임시 생성 |
| 목표 환경 | 로컬 Linux x86-64·NVIDIA Docker, driver **550.54.15 이상을 선택한 목표**, BF16 지원 GPU, daemon RAM≥32GiB·여유 VRAM≥24GiB(48GiB 권장). **측정한 최소치나 충분성 보장이 아님**. Docker storage100GiB 권장, cache volume 여유50GiB 검사 |
| Base·Python·Torch | CUDA12.4.1 runtime/Ubuntu22.04 **amd64 manifest** `sha256:cff3a0d82d2c2b47bab252d67fa9b34a20ef4c50781d98501b5c7367ea9afd10`; Python3.10·torch2.4.0/torchvision0.19.0 cu124 |
| 정책 source | SimpleVLA-RL `7c51662df27b586f9e8a1ab35fcf849f2b8852f9`, 공개 standalone model5파일을 Docker 내부 별도 package에 복사. Full veRL worker/trainer는 P0에서 import하지 않음 |
| 병렬 attention | [수정된 Transformers fork](https://github.com/moojink/transformers-openvla-oft/tree/bc339d9ad707454c0c115970db43c260067c61ab) `bc339d9ad707454c0c115970db43c260067c61ab`, SDPA 사용. 이 revision의 Llama mask/비인과 attention·FP32 logit 출력 source 확인; 실제 sampler/actor 일치는 P0에서 검사 |
| 시뮬레이터·주요 의존성 | VLA-CF `8280a500a01f7f7d45efe202cb416ca362aa8c1a`, MuJoCo3.2.3·robosuite1.4.1·NumPy1.26.4·PEFT0.11.1·timm0.9.10·tokenizers0.19.1·TensorFlow CPU2.15.0. 전체 closure/build/import는 **미검증** |
| Checkpoint·normalizer | 위 Spatial SFT revision `0a051b39aaebd3fc509fe2aba8bc7e60100e09f5`; selected15파일 약15.09GB. Safetensors4개/LFS tokenizer는 공개 SHA256, 작은 파일은 Git blob SHA1·size로 검증. `libero_spatial_no_noops`를 statistics JSON에서 명시적으로 사용하며 임의 key fallback 없음 |
| Assets·init | BDDL·reviewed source SHA256, init Git blob SHA1/size를 고정. Docker build에만 CF assets, Docker volume에만 weights. Prepare에서 실제 asset inventory SHA256·init SHA256을 기록. LFS pointer·누락·변조는 중단; init row 수/row0 해시는 실제 P0 전 미확인 |

설정 근거는 [SimpleVLA-RL 공식 setup](https://github.com/PRIME-RL/SimpleVLA-RL/blob/7c51662df27b586f9e8a1ab35fcf849f2b8852f9/SETUP.md), [CF의 OFT 의존성](https://github.com/yuffish/VLA-CF/blob/8280a500a01f7f7d45efe202cb416ca362aa8c1a/openvla-oft-cf/pyproject.toml), [CUDA12.4.1 driver 표](https://docs.nvidia.com/cuda/archive/12.4.1/cuda-toolkit-release-notes/index.html), [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)다. 충돌하는 원 repository 환경을 그대로 합친 검증 환경이 아니라 **선택한 P0용 recipe 초안**이다. Host driver/toolkit은 새 컴퓨터의 사전 조건이며 이 launcher가 host에 설치하지 않는다. Base digest·직접 pin만으로 apt/transitive wheel의 완전한 lock을 주장하지 않으며 첫 build의 `pip check`·resolved Python/system 목록·image ID를 실제 근거로 남긴다.

### 다른 컴퓨터에서 실행

이 변경 파일이 포함된 revision을 전달/clone한 후 **저장소 루트**에서 아래 순서로 실행한다. 이번 작업에서 commit/push나 다른 물리 컴퓨터 clone은 하지 않았다. Host Python은 stdlib 기반 Docker 제어만 수행한다. 각 명령 성공 후에만 다음 명령을 실행하며, 결과 경로는 **기존에 없는 디렉토리**여야 한다.

```bash
python3 -B 'work/research_topics/unified_vla_rl/재현 방법/langret_resume.py' check --results ../langret-runs/check-01 --gpu 0
python3 -B 'work/research_topics/unified_vla_rl/재현 방법/langret_resume.py' build --results ../langret-runs/build-01 --gpu 0
python3 -B 'work/research_topics/unified_vla_rl/재현 방법/langret_resume.py' prepare --results ../langret-runs/prepare-01 --gpu 0
python3 -B 'work/research_topics/unified_vla_rl/재현 방법/langret_resume.py' p0 --results ../langret-runs/p0-01 --gpu 0
```

- `check`: local Unix endpoint·host/daemon architecture·RAM을 확인하고 호환 host에서 선택 GPU·driver·여유 VRAM을 확인한다. 자원 미충족 **exit3**이면 pull/build/download/native 실행 없이 종료한다. 성공은 host 조건만 충족한 상태다.
- `build`: 선택 GPU UUID의 container 할당을 먼저 확인하고 같은 local Engine에 native image를 만든다. Docker socket/remote builder override는 거부한다. Source·환경·코드는 image 안에, build log/명령은 지정 결과 경로에 남는다.
- `prepare`: image fingerprint와 소유 cache volume을 확인하고 CUDA/BF16 검사 후 payload를 내려받아 검증한다. Cache는 `paper-langret-cache-<fingerprint 앞16자>`, image는 `paper-langret-p0:<같은 값>`이다. Host에는 weights/실험 dependency를 설치하지 않는다. 실제 해석한 package 목록·payload/hash 결과를 결과 폴더에 복사한다.
- `p0`: network 차단·read-only root·선택 GPU1개로 실행한다. Cache는 `/cache`, 실행 산출물만 `/results`, 임시 파일은 `/tmp`에 둔다. `p0_result.json`, 초기 관측 PNG, token/action NPZ, 명령·image identity를 저장한다. 실패는 실제 소비 counter와 원인을 기록하고 중단한다. Host timeout7200초, P0 내부7100초이며 자동 재시도/학습 확대는 없다.
- Fingerprint가 다르면 stale image/cache를 재사용하지 않는다. 종료·실패 시 이번 호출의 고유 이름과 owner label이 일치하는 container만 정리한다. 재사용할 image/cache는 보존하며 사용자 image/volume을 일괄 prune하지 않는다.

### P0의 정확한 범위

OBJ-01 **dev init row0**를 A/B에 사용하며 아직 train/test split이 아니다. A/B별 생성자 reset1회 → 동일 init·seed → settle10회 → query1회/8-action chunk 이하를 수행한다. CF의 무한 reset retry 함수를 호출하지 않고, 생성자 reset과 low-level MuJoCo `mj_step/step1/step2`까지 집계한다. Half-step은 보수적으로 각각1회로 센다. 총 reset≤2·query≤2·actor 재채점≤2·backward≤1·**optimizer0**·control≤36·physics≤10,000·단일 GPU≤2시간이며 초과 동작 **전에** 중단한다.

각 지시의 singleton predicate를 reward/done에 연결하고 A/B predicate를 따로 기록한다. 초기 목표가 이미 참이거나 settle 중 성립하면 중단한다. 두 시작점의 sim state/RGB·일부 controller 필드가 같아야 한다. 이것만으로 전체 숨은 controller/RNG 상태 복원을 입증하지 않는다. Sampler FP32 logits·56 token IDs·원 normalizer로 해독한8×7 action·gripper mapping을 기록하고 같은 입력의 actor log-prob 최대오차≤0.02, 실제 softmax sampling weight와 log-softmax 오차≤1e-5를 **임시 IO 허용치**로 검사한다. LoRA rank32/alpha32/dropout0의 NLL backward1회는 gradient 연결 fixture이며 retention loss나 RL 학습이 아니다.

**P0 통과도 성공적인 placement·지시 구별·보존 효과의 증거가 아니다.** 8-step chunk에서 참인 target event가 관측되지 않을 수 있으므로 false-state wiring과 실제 true-event 교정을 구분한다. Token 확률을 명령/궤적 확률로 확대하지 않는다. 전체 collector·split·B3/B4 loss·학습 및 완전한 상태 분기는 미구현이다.

### 실제 확인과 다음 판단

기존 local image `paper-gap-p3:rvo-c2c46ba`에서 **stdlib 제어 검사22/22 통과**: 원격/override 차단, Mac/메모리 조건, stale image/cache·타 소유 volume 보존, source/payload integrity, 실행 상한/constructor/half-step, 잘못된 OR 성공·reward/done 불일치, 제한된 함수 추출을 검사했다. PyTorch·모델·물리·정책 성능 대용 실험은 없다. 새 image/volume·host package/weights/init/PDF는 만들지 않았고 임시 검사 container는 제거했다.

다음은 **GAP-LANGRET-P0 — WAITING_RESOURCE_AND_IMPLEMENTATION**이다. 호환 local NVIDIA 컴퓨터에서 위 경로를 실제로 build·payload 검증·native 교정해야 한다. 첫 실패를 수정한 뒤 같은 상한으로 재개하며, 자원 부족은 연구 반증이 아니다. P0 뒤에도 P1의 두 목표 기본 능력·분할 실체화와 P2 학습 비교가 남는다. 현재는 좁은 분석 후보를 유지하며 독립 방법 기여나 논문 채택 가능성을 확정하지 않는다.
