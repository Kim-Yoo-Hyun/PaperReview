# D1 축소 가설의 다음 gate — 미실행 계획

- 최신 gate: [N1–N4 재심사](./NONEXPERIMENTAL_REVIEW.md)의 R2 재개 근거가 먼저다. 현재 신규 방법 NO-GO·진단 HOLD로 아래 pilot은 보존된 설계이며 자원 확보만으로 재개하지 않는다. G1 screening을 state 정보의 필수성 입증으로 해석하지 않는다.
2026-10-22 D1-L4까지 반영한 gate 요약. 상세한 현재 설계는 [PRE_EXPERIMENT_CONTRACT.md](./PRE_EXPERIMENT_CONTRACT.md)와 [PILOT_SPEC.json](./PILOT_SPEC.json)을 따른다. 이 문서는 실험 결과나 실행 가능한 전체 manifest가 아니다. 기존 실행 결과는 [RESULTS.md](./RESULTS.md), baseline은 [BASELINE_DOSSIER.md](./BASELINE_DOSSIER.md), 분석 근거는 [CLAIM_EVIDENCE_CONTRACT.md](./CLAIM_EVIDENCE_CONTRACT.md), 현재 후보·제외 사유는 [TASK_OBSERVABILITY_AUDIT.md](./TASK_OBSERVABILITY_AUDIT.md)에 기록한다. 큰 learned method/RL 학습은 승인한 연구 방향으로 간주하지 않는다.

## 먼저 고정할 질문과 범위

**Report 오류와 정상적인 초기 자세 변화에서 보정의 task utility가 다른가? 기존 native VLA와 간단한 보정이 충분한가?** 현재 두 intervention은 전체 관측을 맞춘 cause pair가 아니며 식별 가능성과 다른 행동의 필요성은 검증해야 할 항목이다.

- 한 Franka/LIBERO 계열에서 시작하고 다른 로봇 일반화는 후속으로 분리한다.
- 목표 기반 VLA임을 확인하기 위해 같은 scene에서 서로 다른 goal instruction을 넣는 대조를 둔다. Language가 행동에 영향을 주지 않는 task는 제외하거나 visuomotor 결과로 축소한다.
- Task family는 placement와 articulated manipulation. `libero_goal`, `task_order_index=0`에서 ID 8·0을 primary 후보, 1을 language-goal contrast, 7을 보조 후보로 고정했다. [TASK_CANDIDATES.json](./TASK_CANDIDATES.json)은 source ID를 담지만 **executable=false**다. E1에서 normalizer 작은 파일 hash는 확인했으며, 초기 상태 index·large weight hash·최종 실행 환경은 미고정이다.
- 기존 `pi05_libero`는 지정 config에서 state value가 action에 연결되지 않아 state 보정 primary에서 제외했다. Config flag만 켜거나 작은 새 policy를 학습하여 native 검증으로 대체하지 않는다.
- 현재 primary 후보는 proprio-enabled OpenVLA-OFT의 LIBERO-Goal asset이다. Code commit·model repository revision·state token 경로는 확인했고 weight hash·clean competence·state utility는 미확보다. π0.5와의 성능 차이를 state ablation으로 해석하지 않는다.
- 조사한 40개 task는 절대 EEF orientation을 직접 요구하지 않는다. Strict absolute-orientation 대조를 확보했다고 가정하지 않으며, task utility와 유해한 보정 여부로 질문을 좁힌다. Binary initial state가 같은지와 shared reset은 별도 검증해야 한다.
- 실제 물리 변화에도 입력 canonicalization이 유익할 수 있다. Physical-change라는 이유만으로 correction을 오답으로 label하지 않고 목표 수행과 paired outcome으로 판단한다.

## 입력과 정보 경계

| 구분 | 고정해야 할 내용 |
|---|---|
| Policy-visible | Native RGB views, language, native state, 과거 command/observation; 동일 history 길이와 timestamp 접근 |
| Controller | 실제 native feedback 경로 유지. Policy report-only corruption과 controller corruption을 별개 실험으로 기록 |
| Evaluator-private | Fault label·onset·magnitude, simulator true state, future success. 배포 방법에 주입 금지 |
| Geometry baseline | Calibration/kinematics/landmark 접근은 모든 comparable 방법에 동일하게 제공. GT transform이면 privileged diagnostic으로 별도 표시 |
| Action interface | Absolute/delta, coordinate frame, units, gripper mapping, chunk/execution horizon, control period 고정 전 실행 금지 |
| Ambiguous strata | 관측 비식별 조건에서 cause classification 정확도를 정답 기준으로 요구하지 않음. 가능한 동일 행동·보류 행동의 utility를 평가 |

Source 수준의 후보 interface는 [L3 감사](./TASK_OBSERVABILITY_AUDIT.md)에 확인했다: OSC_POSE delta, 20 Hz environment, OFT 기본 8-action queue, native gripper mapping. Runtime 설정과 일치하는지는 미검증이다. Packet bias와 실제 controller feedback fault를 별개로 유지하며 body quaternion/site rotation의 frame 연결을 확인한다.

## 단계별 비교와 reject rule

| Gate | 최소 검사 | 진행 조건 / 기각·수정 조건 |
|---|---|---|
| G0: 실행 기반 | Native checkpoint+normalizer+environment와 clean rollout | Compatible 자원이 없으면 HOLD. 설치 성공만으로 통과시키지 않음 |
| G1: 현상 존재 | Task 0/8 clean 20 paired initial groups씩, contrast 1도 20회; orientation 오류와 goal swap | Clean task별 ≥16/20, 지정 corruption/goal swap 대비 ≥4/20 net 차이를 pilot 투자 기준으로 사용. OOD mask·action 차이만으로 utility를 입증하지 않음 |
| G2: 타당성·headroom | Neutral-prelude clean / report-only orientation bias / 정상 OSC prelude로 만든 초기 자세 변화, 각각 paired reset | 물리 validity·노출 기준과 clean qualification 통과 필요. R의 privileged 복원은 구현 sanity이며 P에서 true-state는 native와 같음. Visual/actuation/target 변화는 후속 branch |
| G3: 단순 설명 | Native policy, always-vision/state-mask, fixed-history, residual/state estimator, matched augmentation; GAP·ReViP·Self-Adaptive·G-PSMR의 재현 가능한 matched variant | 강한 단순 baseline이 잔여 gap을 없애면 방법 연구 STOP. Baseline 구현·tuning이 미흡하면 learned method의 우월성 주장 불가 |
| G4: 별도 holdout | Onset·magnitude·task/initial state를 development와 분리; 동적 전환은 G2/G3 통과 후 | 여러 조건에서 실질적 이득과 clean 유지가 함께 있어야 확대. Tiny pilot의 숫자를 일반화 결론으로 쓰지 않음 |

20회·16/20과 net 4/20 차이는 **다음 pilot을 위한 사전 qualification 기준**이며 논문의 최종 통계적 검정력 기준이 아니다. G1의 action 민감도만으로 state의 유용성을 입증하지 않는다. Frame·normalization·inverse input 복원, closed-loop 결과를 함께 확인한다. 지정 orientation probe의 실패를 모든 state component의 무용성으로 일반화하지 않는다.

## Baseline fairness와 ablation

구체적인 논문·variant·공개 자산·B0–B6/D0 역할은 [baseline 계약](./BASELINE_DOSSIER.md)을 따른다. State mask와 vision-only trained policy, 논문 재현과 다른 backbone으로 옮긴 port를 구분한다.

- 같은 pretrained checkpoint, demonstration pool, observation/history, environment actions, resets, query 수, wall-clock budget. 모델 크기/추가 VLM/rollout context 차이는 따로 보고한다.
- State masking의 성능 저하는 OOD masking artifact일 수 있다. Native vision-only/augmentation variant와 구별한다.
- Online 추론은 prefix만 사용한다. Offline full-episode ProTracer나 fault-aware comparator는 공정 배포 baseline으로 계산하지 않는다.
- G-PSMR의 초기 고정 gate와 online 변형을 구분한다. Causal change-point/recalibration과 task-conditioned reference를 B3 대조에 포함하며 정답 onset·test outcome은 사용하지 않는다. B0/M1/M2/M3의 난수·query·결합 순서를 통제한다.
- GAP 공개 snapshot의 문법 오류와 공식 수식/공개 rule 차이는 [방법 감사](./BASELINE_METHOD_AUDIT.md)에 기록했다. 수정 diff·선택 규칙·적용 branch를 명시하기 전 GAP 재현 또는 runnable baseline으로 표시하지 않는다.
- Required ablations: cause label 없이 동일 correction, oracle cause만 제공, oracle state만 제공, history 제거, repeated-current 같은 slot 수, language goal contrast, fixed landmark 제거.
- Synthetic corruption만 잘 구별하는 shortcut을 피하도록 perturbation 크기와 생성 규칙을 train/test에서 분리한다. Fault label 분류율은 보조 지표다.

## Metric과 예정 결과표

Primary는 task success와 harmful correction rate다. 후자는 원래 목표를 만족할 수 있는 physical-change episode에서 보정이 실패를 유발한 paired 차이로 정의하며, 단일 trace의 counterfactual을 추정하지 않는다. Collision/joint-limit violation, action latency, onset→recovery time, clean/fault/ambiguous strata를 함께 보고한다.

Harmful pair는 같은 초기 조건에서 baseline 성공·correction 실패인 경우다. Baseline-success pair에 대한 조건부 비율과 전체 pair에 대한 비율을 분모와 함께 구분하고 recovered pair도 보고한다. Operator 수준의 분석을 이 metric의 관측 결과로 대체하지 않는다.

| Method | Clean success | Observable fault success | Physical-change success | Ambiguous utility | Harmful correction | Latency / query budget |
|---|---|---|---|---|---|---|
| Native / strongest simple / proposed / diagnostic | 미실행 | 미실행 | 미실행 | 미실행 | 미실행 | 미실행 |

Methods 비교는 같은 task/seed/초기 상태를 pair로 묶는다. Uncertainty는 task와 seed dependence를 반영해 보고하며 frame를 독립 sample로 세지 않는다. G2의 pilot 분산을 본 뒤 **holdout 이전** 실질 효과·clean non-inferiority margin과 sample budget을 고정한다. 기존 제안의 +5pp/−2pp 예시는 확정 threshold가 아니다.

## 실행 전 남은 gate

- [x] 직접 선행의 지정 본문 절과 공개 interface 감사; 미확인 영역 기록.
- [x] 반례·simple residual diagnostic, Docker 결과·hash 보존.
- [x] 핵심 baseline 6편 선정, 공식 publication·공개 자산 위치·interface·공정성 계약 확보. 새로운 실험 없음.
- [x] D1-L1 직접 방법·공개 구현 경계 감사 및 D1-L2 분석·단순 대안·claim/reject 계약 작성. 실제 효과는 미검증.
- [x] D1-L3 실제 task definition·goal/frame·관측/행동 source 감사. 후보 4개, π0.5 state-value 전제 실패 및 OFT 대체 후보 기록. Empirical 적합성은 미검증.
- [x] D1-L4 [비실험 계약](./PRE_EXPERIMENT_CONTRACT.md)과 [설계 spec](./PILOT_SPEC.json) 생성. Physical qualification·runtime·realised split·정책 효과는 미검증이며 executable=false.
- [x] D1-E1 [Docker resource preflight](../../experiments/vla_d1_e1_preflight/RESULTS.md) 수행. GPU allocation 실패, VM memory·model 크기, normalizer hash·source/download 경계 확인. G0 전체 통과·native 실행은 아님.
- [ ] G-PSMR code·calibration/rotation 구현, ReViP 최신 release, GAP 공식판/공개 코드 차이와 Octo recipe 등 재현 세부 검토 완료. 수식 수준 G-PSMR gate 시점은 확인함.
- [ ] 현재 컴퓨터 Docker에서 native checkpoint 실행을 충족하는 경로 확인.
- [ ] Checkpoint/normalizer·task IDs·simulator commit·seeds·fault generator·비용 단위를 담은 실제 run manifest 생성.
- [ ] G0–G3 정책 pilot 실행.
- [ ] 동료/지도교수의 실제 외부 피드백.

E1을 착수하여 resource preflight까지 수행했지만 G0 전체·G1은 미충족/미실행이다. OFT CPU fallback과 주석 처리된 FlashAttention 설정을 확인했으므로 GPU가 코드상 절대 필수라고 단정하지 않는다. 현재 실행 자원이 qualified하지 않은 것이 HOLD 근거다. 동일 조건의 재검사를 반복하지 않고 관련 자원/실행 범위가 바뀔 때 재개한다. 기존 π0.5 계획 재사용, 대규모 다운로드·학습·임의 CPU 이식, 외부 연락·원격 자원 사용은 하지 않았다.
