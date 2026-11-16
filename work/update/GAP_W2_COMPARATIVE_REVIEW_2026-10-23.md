# GAP-W2 — GEOMETRY·DATA-TRANSFER·SYSID 직접 선행 비교

- 완료일: 2026-10-23 KST
- 작업: [TODO GAP-W2](../../TODO.md)의 비실험 문헌·공개 interface 검토
- 근거: [논문별 버전·확인 구간·code revision ledger](../sources/gap_w2_review_2026-10-23.json)
- Canonical 질문: [GEOMETRY](../../synthesis/07_robotics_3d_perception.md#gap-geometry-2026), [DATA-TRANSFER](../../synthesis/02_rl_il_offline.md#gap-data-transfer-2026), [SYSID](../../synthesis/05_world_models_safety.md#gap-sysid-2026)

## 1. 판정과 이번에 바뀐 것

**GAP-W2 검토는 완료했다. 세 분야의 중요성은 유지되지만, 최초의 넓은 주장을 그대로 신규 연구로 채택하지 않는다.** 특히 DATA-TRANSFER의 “작은 정책이 고른 데이터를 VLA에 전이”는 CUPID의 실제 실험과 직접 겹친다. 아래 판단은 논문·설정의 비교 결과이며 우리의 정책 효과를 측정한 결과가 아니다.

| 후보 | 새로 확인한 직접 충돌 | 현재 판단 | 다시 검토할 조건 |
|---|---|---|---|
| GEOMETRY | PwC가 closed-loop state shift에 대한 calibration·unknown-space planning을, SemSafe가 trajectory-relevant active perception을 이미 다룸 | **REVISE / 진단 후보 HOLD** | 기존 보장 안의 실패인지, 가정 밖의 새 문제인지 분리한 scene–sensor–GT 구성과 보수적 baseline으로 설명되지 않는 예측 |
| DATA-TRANSFER | CUPID의 DP→π₀, ATHENA의 π₀→π₀.₅ 전이; smoothness 감사의 정책 설정별 선택 효과 차이 | **일반 전이 주장 NO-GO / 조건 예측 후보 HOLD** | 단순 전이 성공·실패 재보고를 넘어, 재선택 필요성을 사전에 예측하고 그 비용까지 줄이는 구체적 조건 |
| SYSID | SPI-Active의 능동 식별, ASTRA의 history 기반 abstraction 보정, SV-DRO의 task-sensitive uncertainty | **REVISE / 진단 후보 HOLD** | 단순 delay/history 보정으로 해결되지 않는 구체적 model-class 오류와 식별 가능한 probe·native telemetry |

현재 세 후보 중 즉시 구현할 GO는 없다. DATA-TRANSFER가 VLA와 가장 직접 연결되지만 가까운 선행도 가장 명확해졌으므로 자동으로 다음 프로젝트로 올리지 않는다. 다음 비실험 TODO는 이미 대기 중인 **GAP-L2: latent action의 supervision·decoder·물리 조건 전이 비교**다. GPU 부재만으로 내려진 판단이 아니며, 이전 C/D/E 후보의 보류·종료를 바꾸지 않는다.

## 2. 조사 범위와 증거 경계

GEOMETRY 5편, DATA-TRANSFER 직접 비교 5편과 scaling 배경 1편, SYSID 3편으로 **14편의 지정 본문/부록 구간**을 대조했다. 그중 registry identity가 연결된 것은 Splat-Nav `pr-0284`, Data Scaling Laws `pr-0580` 2편이다. 나머지 12편은 이번 정규화 title/arXiv 대조에서 연결되지 않았으며 formal admission이나 신규성 인증을 뜻하지 않는다. 기존 GAP-W1/V2 목록과 중복하므로 조사 편수를 합산하지 않는다.

2024–2026 자료를 사용하되, 주요 공식 근거는 CoRL·ICLR·RSS·T-RO다. 2026 preprint는 최신 직접 충돌 확인을 위해 포함했다. 전 venue 전수 조사·14편 전체 정독·논문 수식 증명 검증은 하지 않았다. 공식 게재, 저자 venue 표기, preprint를 ledger에서 분리한다. CoRL 2024 PwC의 PMLR 출판 연도는 2025다. DataMIL v2와 Scaling Laws v4는 후속 저자 버전이므로 그 상세 내용을 conference camera-ready와 동일하다고 가정하지 않는다.

공개 GitHub **6개 revision**의 README/tree와 **14개 source/config 파일의 관련 구간**을 정적으로 읽었다. 데이터 payload·checkpoint는 받거나 실행하지 않았고, PDF local cache·dependency 설치·Docker 실험·Git 게시도 수행하지 않았다. Code 존재는 end-to-end 재현 가능성의 증거가 아니다.

## 3. GEOMETRY: 지도에 대한 안전과 실제 충돌의 관계

### 직접 비교

| 논문·확인 구간 | 논문이 지지하는 범위 | 우리 질문에 주는 제약 |
|---|---|---|
| [Splat-Nav v3](https://arxiv.org/html/2403.02751v3), §III·VI·VIII; T-RO 2025 | 재구성된 Gaussian ellipsoid map의 corridor planning과 localization. §VIII는 완전히 누락된 장애물을 명시적 한계로 둠 | Map 내부의 거리/안전 지표를 독립 실제 공간 collision의 대리 정답으로 쓰면 순환 평가가 됨 |
| [A Control Barrier Function… / SAFER-Splat v2](https://arxiv.org/html/2409.09868v2), §III–V·VII | Online GSplat에서 CBF로 nominal acceleration을 보정. 지도·pose·dynamics의 가정이 필요 | Ellipsoid confidence scale나 margin은 그 자체로 실제 누락 장애물에 대한 calibrated probability가 아님. VLA action을 연결했다고 보장까지 자동 이전되지 않음 |
| [AirSplan v1](https://arxiv.org/html/2609.21226v1), §III–V | Quadrotor swept volume·FRS와 Gaussian collision risk. §IV-B3의 conformal inflation은 **FRS neural approximation**에 적용 | Map completeness 보정과 다름. §V-B에서 AirSplan/CATNIPS에는 depth supervision, Splat-Nav에는 RGB만 사용하므로 그대로 새 planner의 인과 효과로 비교하지 않음 |
| [Perceive With Confidence v2](https://arxiv.org/html/2403.08185v2), §2–4·App. F.3; [CoRL 공식 기록](https://proceedings.mlr.press/v270/dixit25a.html) | 환경 단위 calibration, state-wise worst-case score, free/occupied/unknown 공간과 safe planner. 일반 occupancy predictor로 확장하는 조건도 명시 | “Closed-loop state shift를 처음 다룬다”, “unknown 공간과 calibration을 합친다”는 신규 주장 불가. 배포 환경 분포·GT·상태/동역학 가정과 실제 유한 상태 sampling을 구분해야 함 |
| [SemSafe-3DGS v1](https://arxiv.org/html/2609.19330v1), §III–IV | Semantic risk CBF와 예상 경로 주변 정보 획득; partial map·online RGB-D·동일 A* 비교 | “Action-relevant active perception”만으로 차별화 불가. 기존 Gaussian의 uncertainty를 줄이는 것과 모든 미모델링 장애물 검출은 별개 |

SAFER-Splat의 ICRA 2025는 저자 CV/색인에 있으나 이번 IEEE 페이지는 challenge 화면이었다. AirSplan IROS 2026은 저자 표기, SemSafe는 preprint로 다룬다. Splat-Nav의 T-RO publication/IROS presentation 정합은 기존 **META-W1**에 남긴다. PwC는 v2를 사용했고, 저자/내용이 확장된 v3의 결과를 CoRL 버전에 섞지 않았다.

### 남는 질문과 비교 계약 초안

**연구자 가설:** 고정 pose·sensor에서 동일한 평균 surface error를 갖더라도, 관측 지지 영역 밖의 누락과 관측된 표면의 위치 오차는 collision–progress trade-off를 다르게 만들 수 있다. 이것은 기존 논문의 한계를 실험 조건으로 바꾼 초안이며 아직 새 기여가 아니다. 특히 PwC가 보장하는 환경/상태 범위 안에서 단지 policy를 바꾼 것을 새로운 OOD 공백으로 부르면 안 된다.

| 계약 항목 | 고정하거나 비교할 내용 |
|---|---|
| 입력/개입 | 같은 RGB 또는 RGB-D, camera pose·scale·map update 주기. 누락/표면 오차/pose 오차를 별도 축으로 두고 dynamic scene은 첫 비교에서 제외 |
| Baseline | Unknown을 occupied로 보는 occupancy/TSDF, 고정 inflation sweep, pose 보정, PwC류 calibration. 같은 nominal planner/controller 및 정지·관측 선택권 |
| 정답/분할 | 재구성 map과 독립인 mesh/geometry·충돌 판정. Scene 단위 calibration/test 분리와 sensor shift를 별도 보고 |
| 예산/지표 | Depth supervision·추가 관측·정지 시간·planning latency를 포함. Swept-volume false-free-space, collision, completion/progress를 함께 측정 |
| 기각 조건 | Pose 보정·unknown 처리·margin sweep과 같은 Pareto 곡선이면 새 uncertainty 표현의 주장을 기각. 전부 정지해서 얻은 안전을 개선으로 세지 않음 |

Splat-Nav code는 `GSplat → voxel/A* → corridor → spline`을 확인했으나 입력 model 경로와 좌표 변환 자산이 별도다. PwC code는 예측/GT box·mask tensor를 calibration에 사용하고 README는 planner와 calibration의 `Pset.pkl` 일치를 요구한다. 두 저장소의 일부 CPU fallback 표기에도 CUDA 직접 호출이 있어 **Mac CPU에서 그대로 가능하다고 판정하지 않았다**. 공개 scene의 독립 collision GT와 calibration coverage는 payload 미확인이다. C1 관측 selector·D2 attached-object 계획을 재개하지 않는다.

## 4. DATA-TRANSFER: 전이의 존재를 넘어 무엇을 예측할 것인가

### 직접 비교

| 논문·확인 구간 | 확인된 결과/설정 | 신규성·공정성에 대한 결론 |
|---|---|---|
| [DataMIL v2](https://arxiv.org/html/2505.09603v2), §4–6·App. C/D/F/G; [ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/033d9e8dbbbc0ad90e59222cf1db0fc2-Abstract-Conference.html) | Metagradient·target BC proxy, temporal grouping, target/prior co-training. LIBERO/OXE는 Octo; 선택 compute 비용과 작은 proxy model은 논의 대상 | Policy-aware 선택은 이미 존재. STRAP 원 논문과의 숫자 차이를 cross-policy transfer 실험으로 오독하지 않음. Regression estimator의 rollout과 metagradient proxy 경로도 구분 |
| [What Matters… v1](https://arxiv.org/html/2506.13536v1), §3·5·App. E; [ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/16466b6c95c5924784486ac5a3feeb65-Abstract-Conference.html) | Camera/spatial distribution을 통제한 collection/retrieval; target/co-training sampling 비율 명시 | 선택 이득이 task/camera 분포 정렬만으로 설명되는지 강한 baseline 필요. “다양성이 좋다”와 “target에 맞게 가져온다”는 다른 조건 |
| [CUPID v2](https://arxiv.org/html/2506.19121v2), §4–7.3·App. C.6; [CoRL 2025](https://proceedings.mlr.press/v305/agia25a.html) | Rollout return 기반 influence. **Single-task DP가 고른 데이터로 π₀ post-training**을 이미 평가 | DP→VLA 전이 자체는 직접 충돌. 저자의 capacity·data-quality 설명은 모든 architecture에 대한 보편 법칙으로 증명된 것은 아님 |
| [ATHENA v1](https://arxiv.org/html/2606.16208v1), §3–6.4·8 | VLA influence 연산·multi-task balancing; **π₀ 선택 subset을 π₀.₅에 이전**, 50-task 평가 | 모델 변경·multi-task로 확장하는 것만으로도 부족. 저자 CoRL 2026 표기는 공식 채택 미검증이며 결과는 preprint 주장으로 취급 |
| [Smoothness Ranks Skill, Not Success v1](https://arxiv.org/html/2610.17427v1), §5–7 | 같은 Can subset에서 GMM-BC와 DP의 jerk 선택 효과가 다름; episode-length confound 통제 | “선택 효과가 모델에 따라 다르다”도 이미 보고됨. VLA 실험은 아니고 모델·history·optimizer·batch가 함께 달라 **architecture 단독 원인**을 입증하지 않음. RoboPAD workshop은 저자 표기이며 NeurIPS main paper가 아님 |
| 배경: [Data Scaling Laws v4](https://arxiv.org/html/2410.18647v4), §6–7; [ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/88b7b2c896506daabc8d3fd587055167-Abstract-Conference.html) | Single-task 환경/물체 다양성과 visual encoder·action head 크기 비교 | 큰 backbone이 모든 데이터 선택을 무의미하게 만든다는 가정도, single-task scaling을 언어 task 일반화 법칙으로 쓰는 것도 부적절 |

**직전 GAP-W1의 질문을 수정한다.** “A가 고른 데이터가 B에도 이득인가?”는 이미 긍정 사례가 있다. 부정/모델 의존 사례도 있다. 두 결과는 task·데이터·모델이 달라 모순이 아니다. 남길 수 있는 질문은 **어떤 측정 가능한 조건에서 source subset 재사용을 중단하고 target에 맞게 재선택해야 하는가**이며, 그 질문도 공개된 일반 data-attribution/작은 모델→큰 모델 계보와 추가 대조가 필요하다.

### 조건 예측을 검토할 때 필요한 비교 계약 초안

먼저 하나의 embodiment·고정 pool·정의된 task distribution 안에서 `S_A → A`, `S_A → B`, `S_B → B`를 교차한다. `S_B`는 target-specific selector가 고른 비교 subset이지 최적 subset oracle이 아니다. 이때 `J_B(S_B) - J_B(S_A)`는 **재선택 대비 차이**이며 음수도 가능하다. True oracle regret라고 부르지 않는다.

| 계약 항목 | 필요한 내용 |
|---|---|
| 비교 단위 | Demonstration ID와 subtrajectory/timestep ID를 분리. 같은 pool·subset 수와 유효 action 수/길이를 함께 기록. Normalizer는 고정 원칙으로 추정 |
| 변화 축 | 우선 policy 한 축만 변경. Pretraining·history·chunk horizon·head를 동시에 바꾸면 bundled policy transfer로 한정하고 원인 주장을 하지 않음 |
| 강한 baseline | Random, task/camera/spatial/length-stratified selection, all-data, target-only, source selection reuse, target-specific reselection. Influence 계열과 단순 성공 데이터 선택을 별도 비교 |
| 정보/비용 | DataMIL proxy의 target demo와 CUPID/ATHENA의 selection rollout을 같은 것으로 세지 않음. Selector 학습·source/target rollout·재학습 GPU-hours와 interaction/reset 시간을 분리 |
| Holdout | Selector가 보는 validation demos/rollout과 최종 scene·object·seed 평가를 분리. Test-best checkpoint 선택을 하지 않음 |
| 핵심 예측 | 데이터 자체의 불안정 행동 제거와 특정 policy가 표현/실행하지 못하는 mode 제거를 구별. 재사용 실패를 설명한 뒤 만든 사후 규칙이 아니라 별도 policy/task holdout에서 예측해야 함 |
| 기각 조건 | Stratification·중복/길이·update 수·normalization으로 차이가 없어지거나, 경고 규칙이 target reselection보다 더 비싸면 새 방법 주장을 축소. 단지 두 모델의 순위가 다르다는 결과로 끝나면 현재 후보 종료 |

DataMIL의 공개 LIBERO 설정은 language/proprio·8-step chunk·Octo-small 및 selected index 파일의 co-training 전달을 보여준다. 그러나 HDF5→RLDS→MDS의 ID 의미가 target policy loader까지 보존되는지는 아직 end-to-end 확인하지 않았다. CUPID 공개 안내는 PushT/RoboMimic DP curation 경로이며 π₀ hardware 실험 전체가 그 안내만으로 실행 가능하다고 볼 수 없다.

Smoothness 저장소 README는 5-seed 초기 결과를 유지하지만 arXiv v1 본문은 확대된 결과에서 일부 주장을 철회한다. 이번에는 본문을 기준으로 읽었다. 공개 run config 두 개에서는 Adam/AdamW, batch·sequence/history 차이를 직접 확인했다. ATHENA project의 code 버튼은 이번 확인에서 자체 페이지를 가리켜 실행 저장소를 특정하지 못했다. 이 상태에서 3개 VLA의 대규모 학습 grid를 만들지 않는다.

## 5. SYSID: parameter error와 model-class error

| 논문·확인 구간 | 이미 다루는 문제 | 남은 경계 |
|---|---|---|
| [SPI-Active v1](https://arxiv.org/html/2505.14266v1), §3–5·7; [CoRL 2025](https://proceedings.mlr.press/v305/sobanbabu25a.html) | Physical/motor parameters, multi-step prediction, Fisher-information command excitation | Offline·multi-behavior policy 필요; humanoid active 단계의 한계. “더 유익한 동작으로 식별”은 기여가 아님 |
| [ASTRA v1](https://arxiv.org/html/2604.15289v1), §III–IV·V-E·VI | State abstraction의 비-Markov성, history encoder·task-relevant latent/reward prediction으로 simulator grounding | Known state mapping과 target trajectories 필요. Raw VLA vision에서 자동으로 누락 상태를 찾는 결과는 아님. RA-L/IROS 2026은 저자 표기 |
| [SV-DRO v1](https://arxiv.org/html/2605.19029v1), §III·V-A3·VI; [RSS 2026](https://www.roboticsproceedings.org/rss22/p061.html) | Task-sensitive parameter uncertainty로 contact-rich control. 정확한 parameter convergence와 성공 제어를 구별 | Uncertainty class가 미리 주어지며 빠뜨린 contact physics의 한계를 직접 인정. “정확한 식별보다 task utility”만으로 새 주장이 아님 |

**연구자 질문:** calibration에서 비슷한 잔차를 만드는 parameter-only model과 history model 중, 제한된 추가 probe로 새로운 command/contact의 control utility를 예측할 수 있는가? 관측 가능한 probe 아래 두 설명이 동일한 분포를 만들면 식별할 수 없다는 경계를 먼저 둔다. Hidden true parameter를 판별기의 입력으로 주어 문제를 쉽게 만들지 않는다.

| 계약 항목 | 필요한 내용 |
|---|---|
| 조건 | Parameter mismatch / omitted history·actuator structure를 명시적으로 분리. Calibration·held-out command/contact distribution 분리 |
| Baseline | Passive ID, 동일 parameter family의 active ID, 간단한 lag/delay 추정, RLS/KF, history/residual model, DR 및 진단용 oracle |
| 공정성 | 같은 관측·control rate·history 접근권·probe 시간·excitation/force 한도. Parameter estimator와 downstream controller 변경 효과를 분리 |
| 지표 | 예측 잔차와 held-out control cost·constraint violation·추가 probe 비용을 함께 보고. 질량 추정 오차만으로 결론을 내리지 않음 |
| 기각 | 단순 lag 보정이나 공통 history baseline과 차이가 없으면 독립 method 중단. 식별할 probe가 없으면 불가능 조건으로 남기고 큰 learner 구현 안 함 |

SPI-Active의 고정 revision은 Isaac Gym·CUDA와 사용자 controller checkpoint를 요구하고, README의 Dataset Replay/Visualize 및 Sim2real release는 unchecked다. Active config는 command sequence와 mass/COM/inertia/motor family를 정한다. ASTRA/SV-DRO의 native 실행 저장소는 이번 확인 범위에서 특정하지 못했다. 통제된 작은 반례의 설계는 가능하지만 실제 VLA manipulation·navigation의 현상으로 바로 연결하는 것은 추가 연구다.

## 6. 완료 산출물과 다음 행동

세 후보 각각 알려진 답, 좁힌 예측, baseline·정보·예산·지표·기각 조건, 자원과 공개 interface의 경계를 기록했다. **비교 계약은 초안이고 executable manifest·dataset join·runtime·실험 결과는 생성되지 않았다.** 신규 가설은 `CURATION-HYPOTHESIS`를 유지하고 사용자 reading status는 올리지 않았다.

- 다음: **GAP-L2**의 LAOM·VILA·ViPRA·What Matters for Latent Actions 직접 비교. 물리 supervision을 어디에 두는지와 decoder/proxy만 바뀐 효과를 분리한다.
- 보존: 세 후보의 위 조건이 새 근거로 채워질 때 재검토. 같은 검색/공개 여부 점검만 반복하지 않는다.
- 별도 metadata: META-W1은 유지한다. 신규 source를 발견한 사실과 5개 표준 note를 갖춘 formal registry admission은 구별한다.
- 검증: 아래 maintenance 검사와 보존 확인을 완료했다.

## 7. 유지보수 검증

`python3 -m py_compile work/scripts/build_reading_tiers.py`, `python3 work/scripts/build_reading_tiers.py`, `python3 work/scripts/audit_repository.py`, `git diff --check`를 통과했다. Repository audit의 오류·경고는 0이다.

- Registry 1,037편, CORE 47 / NEXT 275 / REFERENCE 473 / ARCHIVE 242, active tracker 322 / history 47, 표준 note 5,185개를 유지했다.
- Manifest·tier·active/history tracker 4개 파일 SHA256이 작업 전과 일치한다. Ledger의 14개 identity·6개 code revision·14개 source/config 파일 수를 검증했다.
- 이번 관련 문서의 로컬 링크 543개가 유효하다. 전체 audit는 Markdown 5,329개와 링크 9,809개를 검사했다.
- 시작 시 dirty 파일 161개 중 이번에 관련된 10개를 갱신했고, 나머지 151개는 SHA256으로 보존을 확인했다. 새 파일은 이 report와 source ledger 2개다. 기존 PDF note 수정은 건드리지 않았다.
