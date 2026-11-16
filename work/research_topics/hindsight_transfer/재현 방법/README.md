# 원 과제 전이를 고려한 hindsight 목표 선택 — 검증 준비 범위

- Updated: 2026-11-07 KST / **GAP-HINDSIGHT-P0-PREP — 실행 자료 작성·native 검증 대기**
- [연구 질문·N2 계약](../내용/README.md#n2-contract) · [단일 source/정적 검토 원장](../내용/sources.json)
- **연구 설계와 Docker 재개 코드 작성을 마쳤다.** 현재 Mac의 NVIDIA 할당은 exit 125, launcher 환경 확인은 exit 3으로 중단했다. 기존 CPU Docker 이미지에서 제어 검사 15개만 통과했다. 새 native image build·모델 추론·시뮬레이션·gradient·학습은 미실행이다. [재개 명령](#resume) · [실제 확인 기록](#preparation-history).

## 1. 선택한 source와 실제 확인 범위

| 항목 | 고정한 후보 / 확인 | 미확인 |
|---|---|---|
| 기준 환경 | `Lifelong-Robot-Learning/LIBERO@8f1084e3132a39270c3a13ebe37270a43ece2a01` | Native renderer·controller·초기 상태·asset 로딩 |
| 첫 task | `libero_10/LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket.bddl`, SHA-256 `2e661058917f683a25bce480015197f0a2c1911bcbc2b9dd9d947199069c9618` | 같은 failure anchor에서 두 valid label이 실제 발생하는가 |
| Success | `libero_living_room_tabletop_manipulation._check_success/_eval_predicate`; `In = contact AND contain` | Instance identity·predicate/RGB 일치·동시 conjunction 교정 |
| RL framework | `RLinf/RLinf@1bf78980d9339cbc67497eddceb9a1e3a74e2acc` | 이 최신 framework와 고정한 LIBERO revision의 package 호환성 |
| 정책 구현 | `implement_version=rlinf`의 수정 OpenVLA-OFT, `predict_action_batch → forward_inputs[action_tokens] → default_forward(compute_logprobs=True)` | Native 동일 지시 re-score 일치·gradient·환경 action 연결 |
| Checkpoint 후보 | [Haozhan72/Openvla-oft-SFT-libero10-traj1](https://huggingface.co/Haozhan72/Openvla-oft-SFT-libero10-traj1), revision `679a2cc1504b905e6cd954a46c80a9408a8ba3e0`; 공개 metadata/card MIT 확인 | Weight shards 확보/hash 검증·실제 load. 이름의 traj1만으로 학습 cohort/평가 독립성을 확정하지 않음 |
| Normalizer | 위 revision의 `dataset_statistics.json`, key `libero_10_no_noops`, SHA-256 `dbe516987e8124416af39c32d3f39ce2137ccb4e282adc590bb4bcede09fb5e1` | Loader의 실제 적용과 controller 단위. 통계의 379 trajectories는 학습에 사용한 시연 수의 직접 증거가 아님 |
| 비교 goal oracle | 원 task의 7개 non-basket 물체에 대한 `In(object,basket_1_contain_region)` | P0 observer 초안 작성·native 교정 대기. P1/P2의 후보 자격 필터·group relabel adapter는 미구현 |
| 직접 선행 | LfH v2·goal selection/auxiliary weighting의 본문/선택 코드 확인 | LfH 저자 실행 구현은 N0 checked project links에서 미식별. 현재 packet을 저자 코드 재현이라고 부르지 않음 |

표준 LIBERO의 한 scene부터 source를 선정했다. **LIBERO-PRO OOD·π0.5·VLM relabeler를 재현한 구성이 아니다.** 후보 checkpoint는 LIBERO-10용이므로 첫 비교의 성공을 새로운 task generalization으로 해석하지 않는다. 원래 pretrained corpus와 train/eval 중복은 model 이름으로 해결되지 않는다.

## 2. 행동 likelihood를 어떻게 확인할 것인가

[정적 model source](https://github.com/RLinf/RLinf/blob/1bf78980d9339cbc67497eddceb9a1e3a74e2acc/rlinf/models/embodiment/openvla_oft/rlinf/openvla_oft_action_model.py)는 action-token logits에서 categorical sampling을 하고, 같은 token을 teacher-forcing 대상으로 점수를 계산한다. 따라서 이 후보에 Gaussian MLP head나 flow-density 공식을 적용하지 않는다. 공식 OFT의 다른 구현과도 구분한다.

초기 비교를 위해 보존할 것은 다음과 같다.

- 원 observation/RGB와 crop/processor 결과, 원 지시/보조 지시의 tokenization·attention mask.
- 생성된 action tokens·실행 전 normalized action·실제 환경 action·유효 token/step mask. Float action을 재양자화하여 원 token을 복원하지 않는다.
- Sampling 당시 `π_old(z|o,g)`의 log-prob, temperature·top-k·vocabulary mask, model revision·mode·normalizer hash.
- 같은 weights/원 지시로 다시 평가한 log-prob의 일치 여부부터 확인한 뒤 지시만 h로 바꾼다. 후자의 차이는 policy improvement 측정이 아니다.
- Chunk 뒤 미실행 token·reset 뒤 observation을 학습에 포함하지 않는다. 지시가 달라져 padding 길이가 달라질 때 image/token 위치가 보존되는지도 검사해야 한다.

기준 YAML은 action dimension 7, chunk length 8, BF16, `temperature_train=1.6`, `top_k=-1`, `logprob_type=token_level`을 사용한다. **읽은 upstream 설정이지 우리 실행 검증값은 아니다.** Native 기본 clipping은 token 단위다. LfH의 action 단위 ratio와 동일하다고 가정하지 않으며 N2는 token별 ratio를 쓰고 trajectory 안에서 평균한 뒤 group을 평균하도록 정했다. Native 전역 token-mean을 그대로 복사한 것과도 다르다. Gripper 변환/양자화 때문에 token 확률을 물리 action marginal density라고 부르지 않는다.

## 3. 최소 데이터·대조 계약

| 단위 | 필요한 기록·조건 |
|---|---|
| Group | 원 goal, scene/BDDL/initial-state identity, K=8, 동일 behavior checkpoint, anchor ID. Task/init 파일 identity와 index 규칙은 N2 고정, 실제 row bytes/hash는 아직 없음 |
| Trajectory | Step/query/chunk 연결, observation·실행 action/token, 종료/시간 제한, reset 경계, 원 목표 success-once |
| Predicate trace | 7개 atomic goal과 원 conjunction의 시간별 truth, 초기 false→달성 여부, 최초 달성 시각. 서로 다른 시점의 atomic 성공을 conjunction 성공으로 합치지 않음 |
| Candidate table | 원 실패 anchor에서 참인 목표, 전체 group 보상 벡터·분산, 객체 관련성. Semantic 후보 수와 paraphrase 수 구분 |
| Paired comparison | 같은 초기 model/optimizer·자료·후보 pool에서 균등 대 객체 일치 우선. 보상 분산·gradient 원리·같은 라벨 BC는 후속 강한 대조 |
| Cost | Env/control/physics steps, VLA queries·실제 유효 tokens, candidate re-score forward/backward, labels, GPU time. 같은 update 수와 같은 총 계산 예산의 결과를 구분 |
| Evaluation | 원 goal 성공이 주 지표. 평가 실패를 후보 선택에 사용하지 않음. 분할·3 run seed·λ/c·상한·주 비교는 N2 계약 고정; 실제 payload/native 교정은 미확인 |

Label oracle는 감독 정보다. 모든 arm이 같은 oracle 후보/보상에 접근하고 actor 입력에는 privileged object state를 넣지 않는다. 후보에 따라 group reward와 advantage를 다시 계산한다. Original-goal all-failure group의 reward gradient가 0인 경우 alignment-only selector가 정보를 얻었다고 표시하지 않는다.

## 4. 준비 완료 범위와 실행 경계

N1은 직접 선행·task/predicate·categorical re-score 경로를, N2는 split·주 비교·통계·학습/상한 계약을 고정했다. N2 계약은 [sources.json](../내용/sources.json)의 `n2.contract`, 이번 P0 runtime 설정은 같은 원장의 `p0_preparation`이 소유한다. **P0 코드 작성은 N2 전체 학습 runner 구현 완료가 아니다.**

이번에 작성한 파일은 [Dockerfile](./Dockerfile), [host 제어 launcher](./resume.py), [Docker native probe](./probe.py), [제어 검사](./test_packet.py)다. README·source JSON·이 네 파일이 실행 자료이며, 생성 결과는 `results/`에만 둔다. Host launcher는 Python 표준 라이브러리로 Docker와 기록만 제어한다. 모델·simulator·패키지·weights/assets는 Docker 내부에 둔다.

[RLinf 공식 안내](https://rlinf.readthedocs.io/en/latest/rst_source/examples/embodied/openvla_oft.html)의 image를 mutable tag 대신 digest로 고정했다. **원격 manifest/config metadata만 확인했으며 image를 pull/build하거나 package import를 검증하지 않았다.** 설치된 dependency 집합은 immutable base에 의존하며 build 시 버전 목록을 기록한다. 여기에 고정 RLinf·OFT·Transformers fork·LIBERO source를 우선 import한다. 이 조합의 API 호환성은 target에서 확인해야 한다. 무제한 최신 패키지 재설치로 해결하지 않는다.

<a id="n2-learning-contract"></a>

## 5. 구현할 공통 계약과 변경해야 할 upstream 기본값

[내용 §9](../내용/README.md#n2-contract)의 수식·분할·통계·수치가 연구 설계다. 아래는 이를 실행 코드로 옮길 때 필요한 차이를 설명한다. **P0 adapter·Dockerfile·launcher 초안은 작성했다. 아래 P1/P2 학습·수집 계약은 여전히 미구현이며 P0로 검증되지 않는다.**

| 항목 | N2 계약 / 구현해야 할 부분 |
|---|---|
| Task routing | `task_order_index=0`, 파일 이름으로 A=0/B=1/C=7/D=4 확인. P0/P1/P2 학습은 A만. Native suite-wide 64/500 env launch 금지 |
| Initial states | Git blob identity는 JSON에 저장. Docker에서 파일 SHA-256·row 수≥30·정규화된 state row hash·A/B 중복을 검증. Native reset ID modulo wrap을 허용하지 않음 |
| Behavior pool | P2 시작 checkpoint θ₀를 고정하여 seed별 4 group을 먼저 수집. U/O/G의 weights·optimizer를 각각 같은 상태로 복원. 4번 업데이트 도중 새 rollout을 섞지 않음 |
| Candidate/reward | 공통 oracle 7개 atomic + conjunction trace, 초기 false 조건·동시 성공. Anchor는 실패 중 한 번 선택. 보상 0/1만 사용; native relative reward·reward_coef=5·reward filtering을 우회 |
| Advantage | Sample std(K−1)+1e−6, 상수 벡터는 0. Global normalization은 꺼야 함. Privileged object states는 observer에만 있고 actor에는 없음 |
| Ratio/reduction | Token별 original-behavior denominator 고정, 같은 temp/vocab mask. PPO eps ±0.2, trajectory별 valid token 평균→group 동일 가중 평균. FP32 log-prob/ratio/reduction, nonfinite면 stage 중단·기록 |
| Loss | `loss = −(J_g + J_h)`(U/O), `−J_g`(G). λ=1, hindsight scalar cap=off, dual clip=off, KL=0, entropy=0. 음수 최소화 loss에 원 논문의 최대화 cap을 부호 확인 없이 붙이지 않음 |
| Optimizer | Adam lr2e−6, betas .9/.999, eps1e−8, decay0, norm clip1; group당 1회·4회 기회. Zero-gradient group도 같은 기회를 기록하며 Adam state의 영향과 실제 parameter delta를 남김 |
| Trainable model | N1 modified OFT의 full-parameter 기본 경로. 실제 requires_grad tensor 목록·개수·hash를 P0에서 봉인; 모델이 원래 freeze한 부분을 임의 해제하지 않음. LoRA/양자화로의 자동 변경 없음 |
| Batching | Runtime 메모리에 맞춰 microbatch를 정하되 전체 group gradient를 누적한 뒤 한 번만 step. Microbatch마다 별도 평균/optimizer step을 하지 않음. 전체 group reduction의 단위는 유지 |
| Input/sampler | Native RGB 256→고정 crop/processor 224, goal text, no proprio, num_images=1, action7/chunk8. Prompt limit128. Temperature1.6/top-k−1/top-p1, dropout off. 이름·shape만으로 실제 IO 일치를 통과시키지 않음 |
| Episode | 최대 policy control512, settling10, aux 성공으로 조기 종료하지 않음. 원 목표 성공/오류/timeout과 미실행 suffix mask를 저장. Reset/warmup 비용 포함 |
| Evaluation | 최종 4-step checkpoint 하나·base·동일 평가 key. Training-time evaluation을 통한 best checkpoint/λ 선택 없음. Std LIBERO diagnostic이며 공인 leaderboard 재현 아님 |

[RLinf YAML](https://github.com/RLinf/RLinf/blob/1bf78980d9339cbc67497eddceb9a1e3a74e2acc/examples/embodiment/config/libero_10_grpo_openvlaoft.yaml)의 clip_high=0.28, dual `clip_ratio_c=3`, lr2e−5, weight_decay0.01, global batch/rollout 크기와 다르다. 위 변경을 override했다고 주장하려면 실제 resolved config·parameter/optimizer manifest가 필요하다. Upstream launcher를 그대로 실행하는 것은 이 계약의 실행이 아니다.

### RNG·회계·재개 기록

- RNG key는 UTF-8 문자열 `hindsight-n2|stage|master_seed|task_name|init_index|member_or_query|purpose`의 SHA-256 앞 4 byte를 unsigned big-endian seed로 사용한다. Purpose는 collection/anchor/selector/eval 등으로 나눠 선택기가 rollout RNG를 소비하지 않게 한다. Eval key와 U/O tie key에는 arm 이름을 넣지 않는다. Bootstrap만 별도 seed7401을 쓴다.
- 원/보조 log-prob에는 실제 실행 token을 넣는다. 같은 goal 재점수화 오차, gradient finite/nonzero/zero 조건, 잘못된 padding·미실행 suffix 제외를 native tensor에서 검사한다. 오차 허용값과 runtime numerical 설정은 P0 실행 전에 정하고 기록한다.
- P0는 최대 2 reset·2 query·4 re-score forward·2 backward·28 control·optimizer0·2 GPU-hours. 인공 reward/goal은 **IO fixture**로만 표시한다. 자연적인 복수 label 존재는 P1의 별도 결과다.
- P1/P2의 수치 상한은 JSON의 `stages`를 읽어 구현해야 한다. P2 training forward/backward query-record≤30,720은 96 rollout×64 query×(원 지시 3 arm+aux 2 arm) 기준이다. 실제 kernel 호출·batch 크기·유효 tokens·GPU 시간도 따로 저장한다.
- GPU-hours는 병렬 GPU마다 점유 wall time을 합산한다. P0에는 시간/step/physics guard와 실제 CUDA peak-memory 기록을 작성했다. 메모리 부족은 실패로 기록하며 자동 양자화/LoRA 전환하지 않는다. P1/P2 guard는 미구현이다. 이미지 build·payload 준비 시간과 실험 시간을 분리해서 기록한다.
- P0는 control 20 Hz, physics substep≤10,000으로 제한하고 실제 timestep을 기록하도록 작성했다. CUDA/EGL·실제 VRAM/RAM·dependency 호환성·init/weight 파일 hash는 target에서 확인해야 한다. 준비 실패 시 원인과 재개 명령을 남기며 host Python/MPS나 원격 GPU로 바꾸지 않는다.
- P0는 학습 checkpoint resume이 아니라 단계별 재실행이다. 같은 source/runtime/weights/RNG manifest를 확인하고 새 결과 디렉토리에 처음부터 실행한다. P1/P2의 optimizer/data 중단점 재개는 별도 구현해야 한다. 기술 오류 episode를 유리한 새 seed로 치환하지 않고 incomplete로 남긴다. 실험 중 계약 변경은 새 버전으로 분리한다.

**남은 실질 단계는 target의 build·payload·native IO/gradient 검증이다.** 같은 내부 문헌 검토나 가짜 데이터의 성능 비교를 반복하지 않는다. P1/P2 구현과 자연 label witness·원 과제 전이 효과는 별도다.


<a id="resume"></a>

## 6. 다른 컴퓨터에서 재개

### 대상 환경과 저장 위치

| 설정 | 선택값·근거·현재 상태 |
|---|---|
| Host/daemon | 사용자 선택 **로컬 Linux x86-64 + Docker Linux amd64 + NVIDIA Container Toolkit**. `ssh://`/TCP 원격 endpoint, Docker/builder override를 거부한다. Windows/WSL은 이 recipe의 검증 대상에 포함하지 않음 |
| GPU/driver | GPU 한 장, CUDA/BF16·EGL. Base CUDA 12.8.1에 맞춰 **570.124.06 이상을 보수적인 driver 기준으로 선택**. CUDA 12.x minor compatibility의 보편적 최소값이라는 뜻은 아님. [NVIDIA release notes](https://docs.nvidia.com/cuda/archive/12.8.1/cuda-toolkit-release-notes/index.html) |
| 메모리/디스크 | Daemon RAM 32 GiB를 준비 진입 하한으로 선택. 계획 권장 RAM 64 GiB, GPU VRAM 48–80 GiB, 여유 disk 100 GB. **실측 최소 요구량 아님**. 7B full gradient·activation/EGL 메모리는 target에서 측정; 24 GiB 카드의 성공을 보장하지 않음 |
| Base image | `rlinf/rlinf@sha256:b5563d95f681478555c4af63ca988b19d1a113306dbdee15a79fff47d320b5cb`; remote compressed layers 약 17.6 GB. 정확한 installed versions/API 호환성 미확인 |
| Python | Image의 `/opt/venv/openvla-oft/bin/python`; host에는 실험 패키지 설치하지 않음 |
| Source overlay | RLinf `1bf78980…`, OFT `e4287e94…`, Transformers fork `bc339d9a…`, LIBERO `8f1084e3…`. 전체 revision·확인 파일 SHA-256은 source JSON에 고정 |
| Attention/수치 | Fork의 **SDPA 양방향 attention**을 실제 class/config로 확인. BF16 weights, FP32 pre-softmax logits·log-prob·ratio/reduction. 같은 goal re-score 최대 절대 오차 `1e−3`; 실패 후 자동 허용값 확대 안 함 |
| Payload | 공개 checkpoint 18개 실행 파일, revision `679a2cc1…`; 4 weight shard 약 15.08 GB. LFS raw SHA-256, 작은 파일 Git blob SHA-1, normalizer 별도 SHA-256 확인. 비-LFS의 Git blob SHA-1은 raw SHA-1과 다름 |
| Cache | Docker named volume `paper-hindsight-p0-<packet SHA 앞16자>` 안 `/cache/model`, `/cache/prepared.json`; host weights/asset 디렉토리 없음. P0에서는 volume read-only |
| 결과 | 아래 `--results`에 source/config/패키지·payload identity·명령·exit·오류, P0 시 RGB/predicate/token/action/log-prob/gradient 진단 저장. 결과 폴더는 매번 새 이름 사용 |
| Network | build/prepare에만 공개 source/payload 접속. P0는 `--network none`·HF/Transformers offline |

실행 자료가 포함된 revision을 **먼저 다른 컴퓨터에 전달해야 한다**. 현재 작업은 미커밋 worktree이며 원격 push/다른 컴퓨터 clone 성공을 확인하지 않았다. 저장소만 과거 HEAD로 clone하면 이 packet이 빠질 수 있다. 전달 후 아래 명령은 저장소 루트 기준이며 특정 사용자 경로에 의존하지 않는다. 각 단계가 exit 0일 때 다음 단계로 간다. `check` 성공은 host 조건 통과일 뿐 container CUDA/EGL 검증이 아니다.

```bash
python3 -B 'work/research_topics/hindsight_transfer/재현 방법/resume.py' check --gpu 0 --results 'work/research_topics/hindsight_transfer/재현 방법/results/target-check'
python3 -B 'work/research_topics/hindsight_transfer/재현 방법/resume.py' build --gpu 0 --results 'work/research_topics/hindsight_transfer/재현 방법/results/target-build'
python3 -B 'work/research_topics/hindsight_transfer/재현 방법/resume.py' prepare --gpu 0 --results 'work/research_topics/hindsight_transfer/재현 방법/results/target-prepare'
python3 -B 'work/research_topics/hindsight_transfer/재현 방법/resume.py' p0 --gpu 0 --results 'work/research_topics/hindsight_transfer/재현 방법/results/target-p0'
```

`build`는 local Engine에서 digest base와 pinned source를 사용한다. `prepare`는 CUDA/BF16와 실제 import 경로를 확인한 뒤 weights·A/B init·asset hash를 확인한다. Init deserialization은 고정 Git blob 확인 뒤 Docker에서만 수행한다. Row count/정확 중복을 남기지만 **near-state·평가 독립성 판단은 자동 통과시키지 않는다**. A0가 존재하면 P0 IO는 가능하며, P2 split은 별도 검토 전 `approved=false`다.

P0는 **A 초기 상태 0 하나, seed11**, 생성자 포함 reset≤2, query≤2, re-score≤4, backward≤2, optimizer=0, settling 포함 control≤28, physics substeps≤10,000, 단일 GPU wall time≤2시간이다. 구현상 settling10 후 최대 한 chunk8만 실행하고 두 번째 query는 실행하지 않는다. 생성자 reset과 `mj_step`을 guard하고 wrapper의 무한 reset 재시도를 우회한다. 실제 hook 적용·reset 비용은 native에서 확인해야 한다.

원 goal의 저장 토큰 재점수화 → 같은 image와 token의 보조 지시 재점수화 → zero-advantage gradient → 음의 단위 advantage gradient fixture만 수행한다. **보조 지시는 합성 fixture이며 자연 hindsight label이나 8-trajectory GRPO group이 아니다.** 모든 log-prob를 유한값으로 확인하고 실제 실행 token mask를 적용한다. PPO clipping으로 gradient가 전부 0이면 불충분/실패로 기록하며 fixture를 유리하게 다시 뽑지 않는다. Parameter version 불변·optimizer 0을 확인한다. 성공 상태 `P0_WIRING_PASS_ONLY`도 연구 효과나 P1/P2 실행 승인이 아니다.

실패 시 같은 결과 폴더에 원인을 남긴다. 원인 수정은 새 packet fingerprint/image tag를 만들고 다시 build/prepare한다. Timeout·예외 시 이번 호출의 고유 container만 정리한다. 기존 이미지·다른 volume·사용자 자산은 삭제하지 않으며 `docker system prune`을 쓰지 않는다. Interrupted stage를 유리한 seed로 교체하지 않는다.

<a id="preparation-history"></a>

## 7. 2026-11-07 실제 확인과 남은 검증

- **현재 환경:** Darwin ARM64·host RAM16 GiB, local `desktop-linux`·Docker28.3.3·Linux aarch64 daemon RAM7.65 GiB. NVIDIA runtime 없음. [실제 GPU 할당](./results/2026-11-07-preparation/gpu_allocation.json)은 exit125, `could not select device driver ... capabilities: [[gpu]]`. [새 launcher check](./results/2026-11-07-preparation/check/local_check.json)는 exit3으로 image pull/build 전에 차단했다. 후자는 이미 확인한 GPU 실패를 재시도하지 않았다. Docker Desktop의 `--gpus` passthrough 범위는 [공식 문서](https://docs.docker.com/desktop/features/gpu/)와도 대조했다.
- **실제로 통과:** 기존 CPU image `sha256:ec14bd72…`에서 network off·repo read-only로 실행한 [제어 검사 15개](./results/2026-11-07-preparation/control_tests.json). Python 제어 코드와 endpoint·budget·hash·stale image·volume 소유권·P1/P2 진입 차단 검사다. Dockerfile build 검증은 아니다. 모델/시뮬레이션/gradient 검사가 아니다.
- **준비한 범위:** Docker recipe, 단일 source 원장의 immutable image/commit/remote weight hash, 환경 확인·단계 launcher, observer/IO/re-score/fixture gradient 코드, 재개 명령·상한·실패 기록.
- **실행 확인하지 못한 범위:** Target image build/실제 dependency import, checkpoint/init/asset payload hash·내용, EGL/RGB·predicate 교정, reset/physics hook·same-goal tolerance·gradient. Native 추론/시뮬레이션·학습 0, weights/assets 다운로드·host 패키지 설치 0. 새 image/volume를 만들지 않았고 CPU test container는 제거했다.
- **연구적으로 남은 것:** P1의 관련/비관련 자연 valid label·기본 task competence, P2 runner·분할 검토·원 목표 전이, 단순 객체 규칙/BC 이후 남는 독립 기여. GPU 확보만으로 이 조건들이 해결되지는 않는다.
