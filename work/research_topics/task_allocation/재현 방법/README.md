# 과제 배분 후보 — Docker 재개 방법과 검증 경계

- Updated: 2026-11-09 KST
- 실제 완료: N1–N2 문헌/정적 비교 설계와 **GAP-ALLOC-P0-PREP**. 현재 자원 확인·portable 코드 작성·Docker stdlib 제어 검사24개 통과. Native tensor·simulator·정책 추론·gradient·학습·성능 측정은 0회.
- [연구 내용·N2 계약](../내용/README.md) · [URL/revision/파일 hash 원장](../내용/sources.json)
- Checkpoint/normalizer identity, immutable base image·source pin, Docker recipe·sampler/actor-facing sidecar·loss fixture·bounded launcher를 작성했다. **Native image build·의존성 import·payload·tensor/IO/gradient는 미검증**이다. 전체 EnvWorker/collector 전달 경로와 학습 loop는 아직 구현하지 않았다. [실행 명령](#resume) · [실제 확인 기록](#preparation-history).

## 추가 비실험 보완과 P1 인계

[2026-11-09 N2-R1](../내용/README.md#nonexperimental-review)에서 **task 평균 성공률과 같은 초기 상태 group의 outcome 다양성이 다르다**는 반례, p/q 보정의 인과 해석 한계, calibration·단순 baseline·통계 계획을 보완했다. 문헌/수작업 논증이며 이번 보완에서는 Docker·tensor·policy·toy 실험을 실행하지 않았다. 아래 P0 코드·immutable plan·상한·이전 검사24개는 변경하지 않았다.

| P0 이후 P1에서 반영할 내용 | 구현/해석 경계 |
|---|---|
| Task당 train state2개×group2개, 총320rollout calibration 권고 | 이전80rollout 초안을 상태 이질성 진단용으로 보완. 미구현·미승인 실행이며 P0의16 fragments 상한과 무관.80만 진행하면 한 상태 탐색으로 제한 |
| `task/state/policy_version/attempted_group/mixed_group/cost` 기록 | 서로 다른 checkpoint의 이력을 같은 정책의 상태 이질성으로 합치지 않음. 실제 binary complete-group 결과 필요; P0 synthetic returns 재사용 금지 |
| U-distinct 조건부 대조 | 비복원 task subset과 포함 확률0.8의 별도 schema/aggregation 검증 필요. 기존 복원 sampler·p/q loss가 이미 지원한다고 해석하지 않음 |
| U-qweight·optimizer 진단 조건부 대조 | 목표 변경의 원인 주장을 할 때 추가. 같은 모델/optimizer state·global gradient clipping 설정/적용률·gradient 규모를 기록. P0에 optimizer update 없음 |
| Group ESS·paired training-seed 결과·budget slack | 자세한 식과 결과 분기는 내용 문서가 소유. 학습 pilot 시간/메모리·resource cap은 native 측정 후 결정 |

전체 worker/channel 통합 뒤 첫 구현 주 점검을 하며 무기한 trainer 이식을 하지 않는다. 환경이 지원돼도 이 계획만으로320rollout calibration·16-update 학습을 자동 실행하지 않는다. 다음 실행 작업은 기존 **check → build → prepare → bounded p0**다.

## 확인한 source

| Repository | 검토 revision | 읽은 핵심 경로 |
|---|---|---|
| RLinf/RLinf | `5c415fa28bb25074fab68f0d09baa73d1b67c608` | LIBERO config/env/worker, embodied actor, advantage/loss/metric utility, train entrypoint |
| PRIME-RL/SimpleVLA-RL | `7c51662df27b586f9e8a1ab35fcf849f2b8852f9` | `verl/utils/dataset/rob_dataset.py`, `verl/workers/rollout/rob_rollout.py` |
| GuanxingLu/vlarl | `212379e840376e07505cba398c0c587d96a13678` | curriculum wrapper, LIBERO env, PPO entrypoint |
| HieuNT91/VIP | `f7bd18915467f50a0d8565b4f16afaef0741a96f` | `src/vip/allocation/bernoulli_allocation.py` (README/benchmark는 탐색용 fetch) |
| Lifelong-Robot-Learning/LIBERO | `8f1084e3132a39270c3a13ebe37270a43ece2a01` | benchmark task map·task-order/initial-state loader |

이 revision들은 **이번 문헌/코드 검토의 고정 지점**이다. 모두 서로 호환되는 실행 dependency 조합이라는 뜻은 아니다. 특히 RLinf는 11/09 현재 공개 HEAD를 읽었으며 이전 HINDSIGHT/UNIFIED 실행 자료의 revision을 바꾸지 않았다. DRATS는 본문·저자 페이지에서 공식 구현을 식별하지 못했다. 미공개라고 단정하지 않는다.

원장의 N1 `static_source_files`와 N2 `n2.sources`에 각 원본 URL·SHA256·확인한 line/symbol을 남겼다. 이 저장소에는 외부 source 전체를 복제하지 않는다. 다른 컴퓨터에서 원본 내용을 다시 읽어 hash와 비교할 수 있으며 파일 확인은 패키지 설치나 코드 실행이 아니다. 이미 source checkout이 있다면 아래로 지정 내용을 볼 수 있다.

```bash
git -C "$RLINF_SOURCE_DIR" show 5c415fa28bb25074fab68f0d09baa73d1b67c608:examples/embodiment/config/libero_goal_grpo_openvlaoft.yaml
git -C "$RLINF_SOURCE_DIR" show 5c415fa28bb25074fab68f0d09baa73d1b67c608:rlinf/workers/actor/embodied_fsdp_actor_worker.py
```

`RLINF_SOURCE_DIR`는 검토자가 지정하는 source checkout 경로다. 실험용 dependency·모델·asset의 설치/실행은 이후에도 로컬 Docker 내부에서만 수행한다.

## 후보 baseline 설정 — upstream에서 읽은 값

| 항목 | 확인 값 | 연구 비교에서 남은 결정 |
|---|---|---|
| Trainer | RLinf embodied entrypoint, FSDP actor, GRPO | native 환경/모델 호환성 확인 |
| Model | OpenVLA-OFT, BF16, action dim 7, action chunk 8 | 아래 checkpoint 후보 고정; 실제 weight load·hash 대조 미실시 |
| Task suite | LIBERO-Goal | row 0–29/30–39/40–49 계약; payload decode·SFT 노출 미확인 |
| Group size | 8 | 첫 주 비교에서 공통 유지; group 내부 조건과 seed 연결 검증 |
| Horizon | max episode/rollout steps 512 | 의미 변경 없이 유지; 실제 비용 counters와 일치 확인 |
| Reset | train auto-reset=false, fixed/ordered reset=true | task 확률 sampler는 ordered 경로를 대체해야 함; 초기 상태 분포는 공통 |
| Reward/filter | reward coefficient 5, 상대 reward, group mean bounds 0.5–4.5의 filter | 주 비교 filter=false·actor-only; 원 filter는 별도 호환성 검사 |
| Upstream batch | train envs 64, rollout epochs 16, actor global batch 16,384 | 원 실행 예시일 뿐 최소 검증 규모나 우리 학습 예산으로 승인한 값이 아님 |
| Inference | train/eval temperature 1.6, top-k -1, top-p 1.0 | 공통 유지; eval sampling seeds100/101/102, dropout 비활성 |
| Model path | `/path/to/model/Openvla-oft-SFT-libero-goal-traj1/` | upstream placeholder이며 확보·검증된 weight 경로가 아님 |

아래 P0 준비에서 1-GPU·immutable base image·CUDA/source 조합을 고정했다. 실제 설치 package 목록·import 호환성·full-parameter 메모리 적합성은 native build/prepare/P0에서 확인한다. BF16 config나 image metadata만으로 실행 가능하다고 판정하지 않는다. 다른 후보의 cache/image를 자동 재사용하지 않는다.

## 작은 공개 task 구성

현재는 LIBERO-Goal 10개를 배포 평가 범위 후보로 두었다. Code의 task-order index 0에서 아래 네 가지는 초기 static/IO 진단 대상으로 구별 가능하다.

| Task ID 후보 | 공식 task stem | 확인/미확인 |
|---|---|---|
| 0 | `open_the_middle_drawer_of_the_cabinet` | 공개 task map 존재; 실행 competence·길이 미측정 |
| 3 | `open_the_top_drawer_and_put_the_bowl_inside` | 조작과 배치가 결합된 이름; 실제 비용 차이 미측정 |
| 5 | `push_the_plate_to_the_front_of_the_stove` | 공개 task map 존재; native 성공 판정/입력 교정 미실시 |
| 7 | `turn_on_the_stove` | 공개 task map 존재; sparse 성공/실패 빈도 미측정 |

이 네 task를 실제로 길거나 짧다고 분류하지 않았다. ID는 suite와 task-order를 함께 검증해야 한다. 원 초기 상태 파일과 model payload를 아직 내려받지 않았으며, 이번에는 task map과 loader source만 읽었다.

<a id="n2-interface"></a>
## N2에서 고정한 source·입출력 계약

**SFT 시작점:** [Haozhan72/Openvla-oft-SFT-libero-goal-traj1](https://huggingface.co/Haozhan72/Openvla-oft-SFT-libero-goal-traj1), revision `d20e1d447dfd87c0daa121b0739e2a379f7fe334`. RLinf의 pinned 공식 예제와 일치하는 후보다. API에서 public·ungated·MIT metadata, 4개 weight shard의 크기/LFS SHA256을 확인했다. **Weight를 다운로드하거나 실행하지 않았다.** 원장의 `n2.checkpoint`는 원격 게시 metadata이며 실제 payload 검증 결과가 아니다.

`config.json`에는 `libero_goal_no_noops` 통계가 없다. [RLinf loader](https://github.com/RLinf/RLinf/blob/5c415fa28bb25074fab68f0d09baa73d1b67c608/rlinf/models/embodiment/openvla_oft/rlinf/__init__.py#L77)가 별도 `dataset_statistics.json`을 합친 뒤 model을 만든다. 이 파일의 SHA256은 `4580775aabade04d26b3530203b9037809b40dced358bae8230b60e6e1804527`이며 해당 key·7차원 action·q01/q99/mask가 존재한다. 이를 다른 checkpoint의 통계로 대체하지 않는다. 통계의 trajectory 수10·transition 수1,282는 데이터 identity/평가 독립성의 증거가 아니다. Image processor는 224×224 metadata, runtime은 `implement_version=rlinf`, `num_images_in_input=1`, `use_proprio=false`, `center_crop=true`를 유지한다. 실제 이미지 변환·행동 단위·normalizer 적용은 native에서 확인한다.

**LIBERO 초기 상태:** source revision `8f1084e3132a39270c3a13ebe37270a43ece2a01`, suite `libero_goal`, task-order0. GitHub tree에서 10개 `libero/libero/init_files/libero_goal/*.pruned_init`의 path·Git blob SHA·size를 확인했다. Asset 내용은 받지 않았다. [Pinned 공식 설명](https://github.com/RLinf/RLinf/blob/5c415fa28bb25074fab68f0d09baa73d1b67c608/docs/source-en/rst_source/examples/embodied/libero.rst#L237)의 50 trials를 전제로 row 0–29 train / 30–39 dev / 40–49 eval을 설계했다. Docker에서 실제 N=50·serialized-file SHA256·row dtype/shape/hash·cross-split 중복을 확인한 뒤 manifest를 만든다. File Git blob SHA를 row hash로 표시하지 않는다. 실패 시 seed/row를 조용히 바꾸지 않는다. P0는 task0/3·dev row30에서 시작한다.

### Metadata 전달 계약 — 전체 학습 경로와 P0 구현 범위

문자열을 `env_info`에 넣는 것만으로 충분하지 않다. [Trajectory.from_steps/to_batch](https://github.com/RLinf/RLinf/blob/5c415fa28bb25074fab68f0d09baa73d1b67c608/rlinf/data/schema/embodied_types.py#L843)는 정해진 field를 stack/concat하며, [train reshape](https://github.com/RLinf/RLinf/blob/5c415fa28bb25074fab68f0d09baa73d1b67c608/rlinf/utils/nested_dict_process.py#L280)는 `env_info` 이름을 거부한다. 별도 tensor field를 끝까지 연결해야 한다.

| 위치 | 필요한 전달/검사 |
|---|---|
| 중앙 sampler | `run/seed, update, draw_id, suite_id, task_id, init_row, group_id, policy_version, q_version, q_i, p_i`를 draw 전에 생성. q/p 전체 벡터·split/source hash는 단일 run header에 저장 |
| LIBERO reset | `reset_state_id = cumulative_task_offset + init_row`로 변환; hardcoded `task_id×50` 금지. 같은 group8은 같은 task/state, replicate0…7·sampling seed는 구별. 자동 reset과 ordered sampler가 새 배분을 덮어쓰지 않게 함 |
| EnvTransition → EnvPart → TrajectoryStep | `allocation_ids` int64 `[B,K]`, `allocation_probs` float64 `[B,2]`를 추가. q/p는 행동·이미지·언어 입력에 넣지 않음. TrajectoryKey의 step/epoch/rank/stage/chunk와 source offset을 join에 사용 |
| Trajectory.from_steps/split/to_batch | `[E*T,B,K]` / `[E*T,B,2]`로 stack. 모든 trajectory에서 필드 존재·동일 shape 검증. 한 shard의 missing field를 건너뛰어 concat하지 않음 |
| Advantage 전 reshape | `[T,E*B,K]`와 확률에 같은 reshape 적용. 각 contiguous8의 group/task/state/policy/q가 일치하는지 검증한 뒤 GRPO 계산. 이 단계 전에 group을 섞지 않음 |
| Train flatten/shuffle | `[T*E*B,K]`로 바꾸고 **동일 shuffle_id**·rank/minibatch split 적용. q/p를 chunk마다 재추정하지 않음 |
| Embodied actor → loss preprocess | p/q를 detached float32 `[micro_B,1,1]`로 전달; token-level `[micro_B,8,7]`에 broadcast. PPO clipping 이후 loss에 곱하고 native 길이 집계를 한 번 적용. 원 `loss_mask_sum`은 불변 |

처음에는 stage1·동기 rollout·동일 크기 shard를 사용한다. 여러 rank로 확대 시 group8 경계를 보존하고 실제 permutation roundtrip을 별도로 검사한다. Logging의 group/state ID와 actor에 도착한 ID가 같아야 한다. q가 뽑기 전 값인지, backward 때 최신 q로 덮어쓰지 않았는지도 확인한다. **현재 `allocation.py`에 단일 sampler·record 검증·actor-facing Trajectory 확장·weighted loss를 작성했다.** `probe.py`는 이 경로의 tensor reshape/gradient fixture를 포함한다. EnvTransition→EnvPart→TrajectoryStep의 실제 worker/channel 전달, 분산 sampler와 rolling history 갱신은 미구현이다. P0에서 직접 만든 TrajectoryStep이 통과해도 전체 trainer 통합 완료가 아니다.

### 비교군 설정과 계산 기록

연구 설정의 canonical 값·수식·손계산은 [N2 계약](../내용/README.md#n2-contract)이 소유한다. 실행 후보에서는 native GRPO의 H512/C8/d7/G8·temperature1.6·lr2e-5·PPO clip0.2/0.28을 유지하고 **filter=false, rollout_epoch1, global_batch4096, microbatch32, update_epoch1**을 공통으로 사용한다. 기본 `is_lora=false`이므로 8B급 모델의 full-parameter gradient/optimizer 메모리를 요구한다. 24GB 단일 GPU에서 가능하다고 가정하지 않는다. First P0는 optimizer step이 없으며 학습 pilot과 자원 요구가 다르다.

| Cost ledger field | 계측 위치·정의 |
|---|---|
| `control_calls` | 개별 simulator의 실제 step 호출에서 증가. Vector wrapper 호출1회에 N env면 N회. Constructor/reset/정착·terminal 이후·실패 시도 포함 |
| `physics_substeps` | simulator integrator 계층에서 별도 계측. 읽지 못하면 null이며 control calls와 합치지 않음 |
| `valid_actions` | 첫 terminal 포함 mask의 합. 비용이 아니라 유효 학습 구간 진단 |
| `forward_calls`, `forward_batch_slots` | 실제 policy forward에서 call1과 입력 batch 크기를 각각 합산. 완료 env·bootstrap·re-score도 역할별 분리 |
| `backward_chunk_rows`, `backward_action_slots` | 실제 backward에 전달한 chunk row·8×7 action 슬롯. Mask=0도 계산했다면 포함; activation recompute 시간은 학습 시간에 포함 |
| `optimizer_steps` | 성공한 optimizer step마다 증가. Gradient 검사에서는0 |
| `stage_seconds`, `wall_seconds`, `gpu_seconds` | 단조 시계·명시적 CUDA 동기화/이벤트 기준. Worker overlap 시간을 중복 합산하지 않음. GPU-seconds는 할당 GPU 수×구간 wall time, utilization과 다름 |
| `phase` | setup / selector_calibration / train / eval / failed_attempt. 학습 효율에는 train+필요 calibration, 전체 연구비용에는 전부 보고 |

Task별 c는 group에 직접 귀속되는 control-call counter로만 계산한다. Mixed inference batch의 GPU 시간을 task에 임의 배분하지 않는다. Budget cap은 dispatch 전에 여유를 예약하며 중간 중단·초과·optimizer 미완료 batch를 따로 기록한다. 비용 cap 안의 완성 checkpoint와 그 실제 비용을 보고하고 더 비싼 checkpoint를 더 작은 budget으로 내삽하지 않는다.

<a id="next-p0"></a>
## P0 구현 범위와 제한

이번 GAP-ALLOC-P0-PREP는 현재 자원 확인·이동 가능한 실행 자료 작성까지 완료했다. 다음 **GAP-ALLOC-P0는 자원 및 native 구현 검증 대기**다. N2 연구 설계·과학적 판단은 유지한다.

| 파일 | 작성한 기능 | 실제 확인 범위 |
|---|---|---|
| [allocation.py](./allocation.py) | task→uniform train row→group8 sampler, identity/q/p 검증, actor-facing Trajectory sidecar, clipping 뒤 p/q를 곱하는 native reducer adapter | sampler/identity stdlib 검사만 실행; torch adapter·reshape는 미실행 |
| [probe.py](./probe.py) | Docker source/payload 검증, row/split·asset manifest, native tensor fixture와 2-task IO/re-score/gradient | hash·budget 제어만 실행; native third-party import/IO는 미실행 |
| [resume.py](./resume.py) | local-only check/build/prepare/p0, fingerprint·image/volume 소유권·시간 상한·고유 container 정리 | 현재 환경 check exit3와 guard 검사 통과 |
| [Dockerfile](./Dockerfile) | immutable amd64 base에 고정 source 4개를 Docker 안에서 overlay | 원격 manifest/config metadata 대조만; pull/build 미실시 |
| [test_packet.py](./test_packet.py) | 제어·확률/identity·손상 payload·오래된 image·외부 volume 보존·구문 검사 | 기존 ARM64 Docker image에서24개 통과; torch 없음 |

Native P0는 task0/3의 dev row30을 각각 같은 상태로 복원해 group8씩 **짧은 action chunk 하나**를 다룬다. 반복 reset RGB hash가 다르면 group 일치를 가정하지 않고 중단한다. Tensor fixture는 native length/filter 분모·w=1 loss 일치·p/q gradient·epoch/shuffle 정렬을 확인하도록 작성했다. 실제 IO 뒤에는 task별 replicate0에만 같은 입력 re-score와 backward를 적용한다. Synthetic q는 task0=0.2·task3=0.1·나머지0.0875이며 p=0.1로 서로 다른 weight0.5/1을 검사한다. 각 group의 인공 return `[5,0,…,0]`은 **자연 성공이나 allocator 효과가 아닌 gradient 연결 검사**다.

P0의 fragment loss horizon은8이며 학습 계약의 H512를 재현하는 실행이 아니다. 실제 첫 terminal까지의 fragment 길이를 기록하고 이 fixture에만 적용한다. 전체 worker/channel·multi-rank·긴 rollout·optimizer·적응 history는 검증하지 않는다. P0 통과를 학습 pilot 준비 완료나 연구 효과 입증으로 해석하지 않는다.

상한은 task2개·최대16 fragments, batch-query≤4/총 query-slot≤32, re-score≤4, backward≤4(작은 tensor gradient 포함), **optimizer0**, 실행 action≤128, reset≤64, constructor/reset/정착 포함 control calls≤1,024, physics substeps≤100,000, 1GPU·wall≤7,200초다. 현재 코드의 예정 query는2회×8, re-score4회, backward3회이며 실패한 시도도 예약된 budget을 소비한다. Counter는 호출 전에 증가하며 시간 초과 시 launcher가 이번 고유 container를 종료한다. Image build/prepare는 각각3,600초 상한이며 설치 비용을 GPU 학습 비용으로 섞지 않는다. Same-input logprob 허용차0.05는 **실측으로 검증되지 않은 고정 검사값**이며 실패 후 자동 완화하지 않는다.

## 재개 환경과 저장 위치

정확한 값은 [sources.json](../내용/sources.json)의 `p0_preparation`이 소유하고 launcher가 plan을 만든다. 별도 lock JSON을 중복 관리하지 않는다.

| 항목 | 설정과 확인 경계 |
|---|---|
| Host/daemon | local Linux x86-64/amd64, Unix Docker endpoint. DOCKER_HOST/CONTEXT·buildx override를 거부. 원격/cloud·Host Python/MPS 실험 경로 없음 |
| GPU/메모리 | CUDA·BF16·EGL 가능한 NVIDIA 1개. 선택한 준비 하한: free VRAM32GiB·daemon RAM32GiB. 계획 권고 VRAM48–80GiB/RAM64GiB/free disk100GB; **실측 최소치나 fit 보장 아님**. 여유 disk는 build 전에 수동 확인 |
| Base | `rlinf/rlinf@sha256:b5563d95f681478555c4af63ca988b19d1a113306dbdee15a79fff47d320b5cb`, linux/amd64, CUDA12.8.1, `/opt/venv/openvla-oft/bin/python`. Manifest compressed layers 약17.6GB; 실제 다운로드/압축 해제 용량 별도 |
| Driver | CUDA12.8.1 release와 맞춘 보수적 선택값570.124.06 이상. 모든 호환 경로의 이론적 최소치라는 뜻이 아님. 실제 device allocation/import/BF16/EGL은 컨테이너에서 재확인 |
| Sources | 위 RLinf·LIBERO pin + OpenVLA-OFT `e4287e94541f459edc4feabc4e181f537cd569a8`, transformers fork `bc339d9ad707454c0c115970db43c260067c61ab`. Commit·선택 파일 hash 검증; mutable pip/apt 설치 없음 |
| Dependency 검증 | Base layer는 digest로 고정했지만 source overlay와 설치 package의 호환성은 미확인. build의 package 목록·prepare의 module 실제 경로·CUDA/BF16·native P0를 단계별 기록. 실패 시 결과를 보존하고 recipe 수정 후 새 fingerprint로 rebuild |
| Checkpoint/normalizer | 위 N2 revision·20개 파일 원격 identity, `/cache/model`, `libero_goal_no_noops`. Prepare에서 payload hash 대조; P0는 offline |
| Rendering | `MUJOCO_GL=egl`, `PYOPENGL_PLATFORM=egl`, GPU capabilities `compute,utility,graphics`; RGB256²→기존 processor224²·center crop,20Hz,정착15steps |
| Assets/cache | source·LIBERO assets는 image 내부 `/opt/allocation`; weights는 소유권 label이 붙은 전용 Docker volume `paper-allocation-p0-<fingerprint16>`의 `/cache`. P0에서 cache read-only, 결과만 `/results`에 host bind |

근거: [RLinf 공식 OpenVLA-OFT 실행 문서](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/openvla_oft.html), [NVIDIA CUDA12.8.1 release notes](https://docs.nvidia.com/cuda/archive/12.8.1/cuda-toolkit-release-notes/index.html), [Docker Desktop GPU 지원 범위](https://docs.docker.com/desktop/features/gpu/). 문서와 원격 image manifest/config를 이번에 확인했지만 실제 image build의 대체 증거는 아니다.

<a id="resume"></a>
## 다른 컴퓨터에서 재개

먼저 **이 실행 파일들이 포함된 repository revision을 전달**해야 한다. 현재 turn은 commit/push하지 않았고 다른 컴퓨터의 clone을 검증하지 않았다. 아래 명령은 clone한 repository 루트에서 실행한다. Host Python은 Docker 제어와 JSON 기록만 수행하며 dependency·asset·tensor·simulator·policy 실행은 Docker 안에서 한다.

```bash
python3 -B 'work/research_topics/task_allocation/재현 방법/resume.py' check --results 'work/research_topics/task_allocation/재현 방법/results/nvidia-check'
python3 -B 'work/research_topics/task_allocation/재현 방법/resume.py' build --results 'work/research_topics/task_allocation/재현 방법/results/nvidia-build'
python3 -B 'work/research_topics/task_allocation/재현 방법/resume.py' prepare --results 'work/research_topics/task_allocation/재현 방법/results/nvidia-prepare'
python3 -B 'work/research_topics/task_allocation/재현 방법/resume.py' p0 --results 'work/research_topics/task_allocation/재현 방법/results/nvidia-p0'
```

각 명령의 exit0·기록을 확인한 뒤 다음으로 진행한다. `--gpu 0`이 기본이며 결과 폴더는 매번 새 이름을 사용한다. `check`의 `HOST_ELIGIBLE_CONTAINER_UNVERIFIED`는 host metadata만 통과했다는 뜻이다. `prepare`는 weight·normalizer·state50rows·cross-split exact duplicate·asset hash를 실제 검사하고 manifest를 남기지만 RGB/gradient 검증은 아니다. Source/row/shape·hash가 다르면 중단하며 split이나 허용차를 자동 수정하지 않는다. P0 성공 상태는 `P0_PARTIAL_PATH_WIRING_PASS_ONLY`다. **성공률·목적 보존·학습 효율·방법 신규성은 여전히 미입증**이다.

주제의 image/volume은 fingerprint로 격리된다. 전용 container는 `--rm` 및 launcher 종료 정리 대상이며 기존 사용자 image/volume을 지우지 않는다. 유효한 native image·payload cache는 다음 재개에 사용한다. 폐기할 때만 결과의 image identity와 `org.paperregistry.owner=paperregistry.allocation-p0`를 대조해 해당 자산을 삭제하며 전역 prune은 사용하지 않는다.

<a id="preparation-history"></a>
## 2026-11-09 실제 준비·검사 결과

- **현재 자원:** Darwin ARM64·RAM16GiB, local Docker Desktop linux/aarch64·RAM7.65GiB·CPU10. 실제 `--gpus all` 할당은 exit125와 `could not select device driver … [[gpu]]`로 실패했다. [원시 자원 결과](./results/2026-11-09-preparation/resource_check.json)
- **Launcher:** `check` exit3, `RESOURCE_UNMET`. Native image pull/build/download 전에 차단했다. CUDA/BF16/EGL runtime은 이 컴퓨터에서 검증하지 않았다. [check 결과](./results/2026-11-09-preparation/launcher-check/local_check.json)
- **Docker 제어 검사:** 기존 ARM64 image를 immutable ID로 사용하고 network none/read-only/`--pull=never`로24개 통과. Python3.11이며 torch/numpy가 없어 stdlib guard·sampler·identity/hash·구문만 검증했다. [검사 결과](./results/2026-11-09-preparation/control_tests.json) · [명령·출력](./results/2026-11-09-preparation/control_test_run.json)
- **보존:** native image·weights·assets·host packages 설치0, 실제 tensor/정책/시뮬레이션/backward/optimizer0. 기존 사용자 image 보존·이번 일회성 container 종료 확인. Registry·reading status·기존 후보 실행 계약 변경 없음.

**준비 완료 범위:** source/image/checkpoint identity, 실행 recipe·제어 코드·actor-facing adapter 및 native fixture의 작성, 현 환경 거부와 stdlib 검사. **남은 자원/구현:** 호환 local NVIDIA에서 build/import·payload/row manifest·native 수치/IO/gradient, 이후 별도 EnvWorker/collector/다중 rank 통합과 P1 학습 비교. 같은 자원 실패나 비실험 요약을 반복할 이유는 없으며, 호환 자원이 확보되면 위 bounded P0부터 이어간다.
