# GAP-N1 — 데이터 선택 정책과 VLA의 관측 정보가 다를 때

- 완료: 2026-10-25 KST. **GAP-N1 DONE: 새 비교 설계를 확보했다. 연구 채택·학습은 HOLD이며, 이 설계의 비실험 계약 심사 한 차례만 이어갈 가치가 있다.** 일반 데이터 전이 방법의 NO-GO는 유지한다.
- Canonical 질문: [GAP-DATA-TRANSFER](../../synthesis/02_rl_il_offline.md#gap-data-transfer-2026). [MEMORY](../../synthesis/04_vla_generalist.md#gap-memory-2026)는 통제 조건의 계보이며 새 memory 방법을 제안하지 않는다.
- 직전 [S1](./VLA_GAP_SELECTION_REVIEW_2026-10-24.md)의 부족한 부분인 **조건·경쟁 예측·수집 단위·최소 비교**를 좁혔다. 새로운 현상을 관측했거나 연구 효과를 입증한 것은 아니다.
- [Source와 미실행 비교 계약](../sources/proxy_observation_contract_review_2026-10-25.json). 공식 논문 3편의 metadata/abstract, 지정 본문 구간, 저자 code 2개 revision의 6개 source/doc 지정 구간을 사용했다. 추가 2개 파일은 context로만 가져왔으며 판단 근거로 사용하지 않았다. PDF·dataset·checkpoint payload와 코드 실행은 없다.

## 1. 질문과 바뀔 결정

**데이터를 고르는 정책이 보지 못하는 과거 cue를 실제 VLA는 사용할 수 있을 때, 그 정책이 고른 subset을 그대로 재사용해도 되는가?** 판단 대상은 모델의 크기 전체가 아니라 selector와 배포 정책의 **입력 정보 범위**다. 첫 비교에서는 같은 구조·초기화·학습 방식에서 cue 접근만 바꿔 capacity와 sensor 차이를 분리한다. 작은 모델→큰 VLA, 다른 로봇으로의 일반화는 그 뒤의 별도 주장이다.

예시는 RoboMME의 VideoUnmask 계열이다. 과거 영상에는 어떤 색의 cube가 어느 container 아래 있는지 보이지만 실행 시점에는 가려진다. 필요한 것은 “memory가 좋다”는 재확인이 아니라, **해당 정보를 사용할 수 없는 selector가 만든 데이터 선택을 정보가 있는 정책에 이전할 때 생기는 추가 손실**이다. 답에 따라 source subset 재사용, selector 입력 정렬, 단순 층화, target 재선택 중 선택이 달라진다. [RoboMME 공식 ICML 2026](https://proceedings.mlr.press/v306/dai26c.html), [본문 v1 App. E.5](https://arxiv.org/html/2603.04639v1).

현재 “정말 그런 손실이 발생한다”는 근거는 없다. 아래는 반증 가능한 연구자 가설이다. VLA의 language는 고정된 색 목표와 action 선택에 연결하며, 정답 위치를 subgoal 문장으로 주입한 결과를 memory-VLA 효과로 세지 않는다.

## 2. 새로 확인한 직접 선행과 기여에서 제외할 것

| 근거·확인 깊이 | 이미 알려진 답 | 이번 설계에 주는 제약 |
|---|---|---|
| [STAFF, ICLR 2025 공식](https://proceedings.iclr.cc/paper_files/paper/2025/hash/412360d2dd428c26f34918c8d682cf7e-Abstract-Conference.html), [arXiv v1 §3.1–3.2](https://arxiv.org/html/2410.01296v1#S3) | 작은 모델 점수를 target에서 일부 검증하고 구간별 선택 예산을 조절 | “cheap target audit로 proxy 선택 수정” 자체는 새 방법이 아님. Target verification 비용을 숨기지 않음. 본문 확인 버전은 conference 최종본과 구분 |
| [Can Small Training Runs Reliably Guide Data Curation?, ICLR 2026 공식](https://proceedings.iclr.cc/paper_files/paper/2026/hash/c7d04ce5e71efdfc7a4a78f7161238a9-Abstract-Conference.html), [v2 §5.2](https://arxiv.org/html/2512.24503v2#S5.SS2) | 학습 설정에 따라 데이터 순위가 달라지고 작은 학습률이 tuned-target 순위와의 대응을 개선; 이론은 random-feature model 범위 | 같은 학습률 한 점의 순위 차이를 정보 부족의 결과로 단정하지 않음. 동일 계산 예산 비교와 dataset별 tuning 예산 비교를 구분. VLA 성공률에 같은 정리가 적용된다고 주장하지 않음 |
| RoboMME 공식 abstract·App. E.5 및 공개 코드 | 기억 유형·통합 방법의 비교와 video→execution task가 존재 | 새 memory architecture/benchmark의 일반 동기는 기여에서 제외. 이번 것은 selection-stage 정보 계약의 진단 |
| [기존 W2](./GAP_W2_COMPARATIVE_REVIEW_2026-10-23.md) | CUPID DP→π0, ATHENA π0→π0.5, DataMIL, 정책 의존 선택 효과 | 전이의 존재·실패 가능성 자체는 새롭지 않음. 그 문헌의 전체 실험을 이번에 다시 정독한 것으로 기록하지 않음 |

검색은 proxy–target curation, partial observability/history, memory-dependent manipulation의 교차 조건에 한정했다. 검토한 구간에서는 아래의 동일 episode·입력 정보 조작·동일 target 재학습 비교를 확인하지 못했다. **검색 미발견은 신규성 보증이 아니다.** STAFF 전체 구현 이식이나 새로운 learned selector 개발로 곧바로 넘어가지 않는다.

## 3. 먼저 지운 잘못된 강한 주장

“Selector에 정보가 없으면 중요한 데이터를 반드시 버린다”는 주장은 성립하지 않는다. 간단한 수작업 반례를 둔다. 숨은 cue `c∈{-1,+1}`가 균등하고 정답 action이 `a=c`, current observation이 항상 같다고 하자. Current-only 상수 예측 `m`의 제곱오차는 `R(m)=1+m²`이므로 최적 예측은 `m=0`이다. 양쪽 sample의 오차는 같으며, 최적점에서 validation gradient도 0이다. 따라서 fit score나 해당 국소 gradient 기반 점수는 동률이 될 수 있다. 균형 있게 tie-break하면 특정 mode를 반드시 제거하지 않는다. 이는 로봇 실험이나 모든 influence estimator에 대한 정리가 아니다.

이 반례 때문에 **memory 필요성 → 선택 실패**를 자동 추론하지 않는다. 선택 목적함수, validation 분포, tie-break와 mode coverage가 함께 작용해야 한다. “정보가 적은 정책의 성공률이 낮다”만 관측해도 이번 가설을 지지하지 못한다.

## 4. 차별적 예측과 강한 대안

모든 최종 성능 비교는 **같은 history-enabled target B**, 같은 초기화 규칙과 학습 예산으로 한다. `S−`는 cue가 없는 selector, `S+`는 cue가 있는 selector, `Sctrl`은 cue 대신 같은 수의 무관한 과거 frame을 제외한 selector, `Sbal`은 task/목표 위치/길이 등으로 층화한 단순 선택이다. 최종 test를 subset 선택에 사용하지 않는다.

| 설명 | 기대되는 구별 패턴 | 설명을 약화시키는 결과 |
|---|---|---|
| **정보 계약 가설** | `J_B(S+)−J_B(S−)`가 `J_B(S+)−J_B(Sctrl)`보다 큼. 즉 같은 수의 무관한 frame 제거보다 cue 제거에 따른 selection 손실이 큼 | 차이가 0/반대이거나 mask 자체의 분포 이탈·길이/목표 빈도로 설명됨 |
| 최적화 설정 차이 | 작은 LR 또는 같은 tuning 예산에서 순위 차이가 사라짐 | 설정을 맞춘 뒤에도 cue 위치에 국한된 차이가 남음 |
| 단순 coverage 손실 | `Sbal` 또는 `S−`의 coverage 보정만으로 target 성능이 회복 | 같은 coverage에서도 history 접근에 따른 차이가 남음 |
| Target의 memory/실행 능력 부족 | Cue가 있어도 올바른 container 선택·집기가 안 됨 | 독립 competence 확인 후 selection 차이가 남음 |

`J`는 native task success와 첫 올바른 container 선택률을 **각각** 뜻한다. 두 수치를 하나의 reward로 섞지 않는다. `J_B(S+)−J_B(S−)`는 선택 방식 간 차이이며 oracle regret가 아니다. Subset overlap이나 score correlation은 보조 진단으로만 쓴다.

**기각/축소:** 단순 층화·정상 정렬·같은 tuning 예산으로 설명되면 새 방법 개발은 종료한다. 진단 결과로 남길 가치도 독립 조건에서 재사용 가능한 결론이 있는지 다시 심사한다. 일회성 mask 실패만으로 논문 기여를 주장하지 않는다.

## 5. 구체적인 수집·비교 설계 — 아직 만들거나 실행하지 않음

**최소 fixture:** 한 Panda·세 container의 쉬운 VideoUnmask를 출발점으로, container pose/camera/robot state는 고정하고 숨겨진 cube의 색–위치 대응만 바꾸는 3개 episode를 한 group으로 수집한다. 지시는 같은 색을 요구한다. 실제 current RGB/proprio가 같고 필요한 첫 선택이 다른지는 저장 hash/이미지 대조와 evaluator로 검증해야 한다. Container 내부 물체의 접촉·그림자·렌더 누설이 생기면 같은 관측으로 간주하지 않는다.

공개 task를 그대로 복제했다고 부르지 않는다. 확인한 source는 목표를 `bin_0`와 `color_names[0]`에 연결한다. 색만 바꾸고 지시를 고정하면 task/evaluator가 어긋날 수 있으므로 **goal 선택·planner·failure evaluator를 함께 바꾸는 fixture 설계**가 필요하다. 정답 container만 숨기는 것이 아니라 실제 evaluator와 demonstrator가 같은 목표를 사용해야 한다.

수집 상한 초안은 train 12 group, selector-validation 4 group, 최종 test 8 group, 각 3개 색 대응으로 **72 episode**다. 이는 통계적 검정력 계산에 따른 규모가 아니라 fixture를 버릴지 판단할 초기 상한이다. Pair/mask 파생본은 원 group과 같은 split에만 둔다. Group 분리가 instance holdout일 뿐 다른 task로의 일반화가 아님을 명시한다. 실패·retry·planner 시간도 기록하고 성공 trajectory만의 수를 전체 수집 비용으로 쓰지 않는다.

동일 episode에는 (a) 올바른 pre-execution history, (b) cue frame 제외, (c) 같은 수의 무관한 frame 제외라는 입력 view를 정의한다. Token 수·mask·positional index·current state·prompt가 무엇을 바꾸는지 계약에 남긴다. 학습하지 않은 null-memory mask를 기존 checkpoint에 넣어 얻은 실패는 OOD 입력 반응일 수 있어 가설의 증거로 쓰지 않는다. 단순 frozen forward 진단과 각 정보 조건에 맞게 학습한 selector 비교를 분리한다.

**단계별 비용 제한:** 첫 후속은 code/metadata 계약 확인뿐이다. 다음 fixture qualification도 별도 로컬 Docker 검증이 필요하다. 학습 budget·checkpoint hash·optimizer 설정·실측 VRAM·normalizer·selector 구현은 아직 고정하지 않았으므로 현재 계약은 `executable=false`다. 72개 수집과 target 학습을 이번에 승인된 실행 계획으로 표시하지 않는다. 실측 처리량 없이 GPU-hours를 만들어 쓰지 않는다.

## 6. 공개 자산에서 새로 확인한 연결과 미확인 부분

| 고정 revision·구간 | 확인한 연결 | 아직 대체하지 못하는 것 |
|---|---|---|
| [Benchmark VideoUnmask.py](https://github.com/RoboMME/robomme_benchmark/blob/1babf64480e28320e0f9db7992554616ceefda0e/src/robomme/robomme_env/VideoUnmask.py), L160–260·L302–343 | Seed 기반 배치/색 permutation, `bin_0` 목표와 잘못된 container pickup 실패 경로 | 동일 관측–다른 목표 matched group, wrapper 전체와 실제 native 실행 |
| [Dataset builder](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/dataset_builder/build_robomme_dataset.py), L238–299 | `exec_start_idx`, video flag, `epis_idx/step_idx`, 현재 영상/state/action chunk, 과거 feature 저장 | 원본 episode↔global ID의 끝까지 이어지는 join, 미래 frame이 memory에 들어가지 않는다는 검사 |
| [Training dataset](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/training/dataset.py), L95–161·L212–255 | Episode별 history feature와 frame sampling·mask·state normalization 경로 | 실제 checkpoint에 맞는 memory token 계약과 causal cutoff |
| [Training config](https://github.com/RoboMME/robomme_policy_learning/blob/ac846a9a4aec841e483b1dc5d620dfe426bde853/src/mme_vla_suite/training/config.py), L170–210·L230–256·L558–582 | Symbolic subgoal을 prompt로 넣는 경로와 history 없는 pi05 baseline 설정이 구별됨 | Ground-truth subgoal을 사용하지 않는 perceptual variant의 end-to-end tensor 확인 |
| 두 repository README | Dataset와 memory variant checkpoint, norm stats·Docker/CUDA 경로 안내 | Weight contents·학습 pool 중복·license/asset provenance·이 컴퓨터의 실행 자격 |

Preprocessed sample에는 `grounded_subgoal` 등이 포함된다. **존재가 곧 누설 증거는 아니지만**, 이번 perceptual 비교에서 최종 model input으로 들어가면 cue ablation이 무효가 될 수 있다. 반대로 일부 transform이 이를 제거한다는 코드 한 줄만으로 전체 train/eval 경로가 깨끗하다고 결론 내리지 않는다.

배포된 task-finetuned checkpoint가 해당 pool을 이미 학습했을 가능성도 있다. 그런 checkpoint는 실행 smoke/능력 확인에 제한해 쓰고, 새 subset으로 학습한 효과를 주장하려면 초기 weight의 학습 provenance와 split을 별도로 고정한다. 공개 checkpoint 이름만으로 미노출을 보증하지 않는다.

## 7. 판단과 다음 TODO

**발전 가능성: 제한적인 진단 후보로 한 단계 진행.** S1의 추상적 “정책에 따라 선택이 다르다”에서 입력 정보의 차이·반례·같은 target 비교·구체 fixture로 좁혔다. 이것은 새 비교 설계의 진전이며 native 효과나 top-tier 수준의 신규성 입증은 아니다. 기존 C1/E1/E2·MEMORY·CAUSAL HOLD와 초기 RL 전이 RETIRED를 재개하지 않는다.

**GAP-N2 READY — 한 차례의 비실험 계약 심사:** 지정된 두 revision에서 (1) raw→global episode/split join, (2) memory의 시간 cutoff·mask와 train/eval 동일성, (3) 실제 policy input의 subgoal/정답 누설 여부, (4) paired fixture의 goal–planner–evaluator 수정 지점을 확인한다. 결과는 구체 경로·실패 조건을 갖춘 계약으로 남긴다. 현재 README 목록을 다시 세거나 GPU가 있는지만 확인하는 작업이 아니다.

네 연결 중 하나가 현재 구성으로 성립하지 않으면 이 자산 설계를 REVISE/HOLD로 종료한다. 통과해도 새 수집·학습은 자동 시작하지 않는다. 그때에만 runtime/checkpoint/budget을 채운 로컬 Docker qualification을 다음 단계로 제시한다. 실제 외부 연구자 피드백은 별도 미완료다.

## 8. 문서·무결성

TODO와 canonical synthesis에 이 좁은 설계 및 판정을 연결했다. `py_compile`, reading-tier 생성, repository audit, `git diff --check` 통과. Registry 1,037편·집중 읽기 322편·표준 노트 5,185개, audit 오류/경고 0개다. Canonical 파일 6개와 재사용한 과거 근거의 hash를 보존했다. 기존 dirty 파일 415개 중 이번 문서/생성 대상 7개 외 408개를 보존했다. 명령별 결과와 임시 source 정리는 [ledger validation](../sources/proxy_observation_contract_review_2026-10-25.json)을 따른다.
