# RP-2 Same-Onset Failure Recovery Arbitration

> Retired project overlay. The former gap/idea registers were removed by policy; this file is retained only as historical audit context and is not an active research plan.

- Status: `SCOPED / HIGH-COLLISION / FOCUS`
- Updated: 2026-08-28 KST (`implementation freeze + full-text survey`)
- Parent ideas: retired gap/idea-register references (not maintained)
- Primary benchmark: `LIBERO-Long` (`libero_10`)
- Conditional secondary validation: `CALVIN` long-horizon five-subtask sequences, only after the LIBERO Phase 0/C1 gate
- Hypothesis evidence: `UNTESTED`
- Priority reading: retired RP-2 P0–P4 spine (not maintained)
- Novelty status: `HIGH-COLLISION / CONDITIONALLY_FIT / CURRENT FOCUS` — Agentic RL이 broad high-level recovery selector를 선점했다. novelty는 same-onset option sweep에서 recovery ranking crossing과 best-fixed regret가 관찰되고, matched-budget full-information selector가 이를 줄일 때만 성립한다.
- Gap verdict: retired 2026-08-28 gap-audit reference (not maintained). recovery, self-correction, execution-mode selection과 counterfactual failure synthesis 자체는 이미 선행 연구 범위다.
- Evidence boundary: 기존 registry full-text, 2026-08-28 official proceedings/code와 최신 arXiv full text를 구분한다. 최신 preprint는 method·experiment contract를 읽었더라도 novelty-collision과 baseline 후보로만 사용하며, 코드·policy-visible input·budget contract를 재현하기 전에는 matched baseline으로 부르지 않는다.

이 문서는 새 foundation model을 만드는 계획이 아니다. 기존 VLA와 failure detector, recovery skill을 고정하고, **동일한 post-failure state에서 서로 다른 abstraction level의 recovery option이 만드는 success·risk·cost를 비교한 뒤 어떤 option을 선택해야 하는지**를 동일한 시간·행동·위험 예산 아래 검증한다. I-12는 cloned-onset multi-option branch table을 만드는 공통 측정 도구이고 I-02가 그 위에서 검증할 arbitration 가설이다. I-06의 policy update는 I-02가 지지된 뒤에만 진행하는 후속 단계이며 현재 C1 claim에 포함하지 않는다.

### 2026-08-28 frontier re-audit 결론

최신 연구는 RP-2의 motivation을 강화하는 동시에 넓은 novelty를 닫는다. RT-H는 language-motion hierarchy와 human correction/intervention learning을, Gemini Robotics 2는 multi-step progress와 self-correction을 공식적으로 제시한다. ActFovea는 disturbance-specific candidate observation과 verified action chunk·bounded safe failure를, Agentic RL은 execution history에서 소수 execution mode를 선택하는 high-level recovery를, ProbeAct는 training-free detection/CBF correction을 다룬다. Dream2Fix는 generative world model로 counterfactual failure–correction pair를 합성하고, CoRe·VLCP는 imagined realignment와 code-level replanning을 제시한다.

따라서 RP-2가 살아남는 조건은 다음 교집합을 실제로 검증하는 것이다.

1. 실제 failure onset을 clone한 **same-state branch rollout**이어야 한다.
2. retry·reobserve·reset·rewind·replan·escalate를 **같은 option library와 vector budget**으로 비교해야 한다.
3. 동일 정보 조건에서 **best-fixed·binary·scalar·type-only·frontier mode selector**와 비교해야 한다.
4. option ranking crossing과 **regret-to-empirical-oracle**가 있어야 한다.
5. selector 이득이 detector·더 강한 option·privileged state·추가 horizon 때문이 아님을 oracle decomposition으로 보여야 한다.

이 다섯 조건 중 하나라도 빠지면 contribution을 “새 recovery method”로 넓히지 않고 C0 protocol 또는 특정 recovery-family audit로 축소한다.

### 2026-08-28 full-text method·experiment survey

구현 전에 가장 가까운 연구의 abstract가 아니라 공개 full text와 공식 코드를 다시 대조했다. 이 감사 결과, **Agentic RL이 RP-2의 가장 강한 novelty threat**다. 이미 frozen low-level policy 위에서 recent execution history를 보고 `Execute/Retry/Repair/Reset`을 고르는 POMDP형 high-level policy를 PPO로 학습하고 LIBERO 전 suite에서 검증한다. 따라서 “history를 쓰는 recovery-mode selector”, “POMDP formulation”, “frozen VLA 위의 lightweight supervisor”, “강도별 recovery 선택”은 RP-2의 contribution이 아니다.

| 근거 | source-verified method·experiment contract | RP-2에 미치는 영향 | 필수 대응 |
|---|---|---|---|
| [Agentic RL](https://arxiv.org/html/2607.13818v1) | history length 20, decision interval 5, `Execute/Retry/Repair/Reset`, task별 PPO 최대 1M high-level step, actor는 non-privileged history·critic은 simulator global state, LIBERO random action disturbance | 가장 가까운 direct collision. broad high-level arbitration claim은 닫힘 | X5로 우선 재현을 시도하고, `same-onset all-option observation`, vector budget, best-fixed regret, held-out selector를 차별 단위로 둠 |
| [ActFovea](https://arxiv.org/html/2607.29169v1) | visual/action/proprioception consistency, candidate observation, action-chunk verification, short horizon·hold·safe failure, 40 LIBERO task × task당 50 episode, matched frozen π0 | observation recovery, action verification, bounded safe failure와 clean preservation은 이미 강한 선행 결과 | X4와 fixed short-horizon·timestamp hold·action smoothing control을 observation/action subgroup에 포함 |
| [ProbeAct](https://arxiv.org/html/2606.09740v1) | hidden-state 3D probe, grasp/transport/place kinematic state machine, repeated-failure CBF correction, OpenVLA-OFT와 LIBERO-plus | phase-aware detector와 low-level safety filter 자체는 novelty가 아님 | X6는 grasp/place subgroup의 mechanism baseline으로만 사용; CBF를 P1만 쓰지 않음 |
| [CoRe](https://arxiv.org/html/2608.14822v1) | suffix-OOD detection, recent viable anchor, synthesized continuation, minimal physical restoration, restoration count·wall-clock·safety 분석 | rewind·rejoin·progress preservation·imagined probing claim은 닫힘 | rejoin/restore는 option family로만 취급하고 physical restoration count와 post-handoff step을 cost metric에 추가 |
| [ViFailback](https://openaccess.thecvf.com/content/CVPR2026/html/Zeng_Diagnose_Correct_and_Learn_from_Manipulation_Failures_via_Visual_Symbols_CVPR_2026_paper.html) | visual-symbol diagnosis/correction, 5,202 real trajectories, VLA 연동 real-robot correction | diagnosis label 또는 external correction guidance 자체는 novelty가 아님 | correction interface가 재현 가능할 때 X1; reported real-robot result를 LIBERO 순위에 직접 섞지 않음 |
| [SAFE official code](https://github.com/vla-safe/SAFE) + [SAFE OpenVLA fork](https://github.com/vla-safe/openvla) | OpenVLA/π 계열 rollout, hidden feature 저장, LSTM/MLP detector와 공식 LIBERO checkpoint 실행 경로 제공 | detector와 base-policy integration의 가장 낮은 구현 위험 경로 | primary stack을 이 경로로 잠정 고정하고 detector gain과 selector gain을 분리 |

`Agentic RL`과의 차이는 알고리즘 이름이 아니라 **관측되는 학습 신호와 평가 estimand**에서 만들어야 한다. Agentic RL은 policy가 실행한 trajectory return으로 sequential mode policy를 학습한다. RP-2는 fit/calibration onset에서 모든 applicable option을 실제 분기 실행해 option별 completion·risk·cost를 관찰하고, held-out onset에서 best-fixed regret와 option-ranking error를 직접 평가한다. 이 차이가 실험에서 의미 있는 이득으로 이어지지 않으면 RP-2는 independent method contribution이 아니라 Agentic-style execution manager의 evaluation extension이다.

## 0. 연구 범위와 시스템 경계

RP-2의 현재 주장은 **실로봇의 저수준 제어법**이나 고수준 recovery supervisor의 존재 자체가 아니라, frozen VLA와 기존 skill/controller 위에서 **same-onset all-option supervision이 recovery arbitration에 주는 추가 decision value**에 한정한다.

| 구분 | RP-2가 다루는 것 | 현재 주장하지 않는 것 |
|---|---|---|
| 입력 | VLA feature, proprioception/action·alert history, normalized elapsed step, remaining budget | simulator oracle state, BDDL progress/subgoal label이나 test-time option outcome을 policy 입력으로 제공하는 것 |
| 출력 | Phase 0/1의 `O_core={CONTINUE, RETRY_CURRENT, REOBSERVE_WAIT, STATE_RESET, ABORT_STOP}` 중 선택; `O_graph/O_assist`는 acceptance 뒤 extension | torque, joint target, impedance/force law 자체를 새로 학습하거나 rewind/replan/human escalation을 privileged oracle로 primary에 넣는 것 |
| 실행층 | 고정 recovery option library와 기존 low-level controller 호출 | selector가 접촉 제어·동역학 불확실성을 직접 해결한다는 주장 |
| 1차 검증 | pinned LIBERO-10/OpenVLA/SAFE stack의 branch-equivalence test와 `O_core` 20–50 onset sweep | simulator 결과만으로 physical safety guarantee를 주장하는 것 |
| 후속 검증 | LIBERO confirmatory split 뒤 CALVIN/`O_graph`/동일 option interface의 real-robot transfer | Phase 0/C1 gate나 hardware 결과 없이 C2/C3 claim을 선제적으로 하는 것 |

따라서 RP-2의 방법론은 수학적 decision formulation을 backbone으로 삼지만, 산출물은 단순한 정리나 이론 증명이 아니다. `detector → non-privileged belief/context → option-conditioned value·risk·cost → constrained selector → 기존 controller`의 closed-loop 실행과 matched-budget 실험으로 가설을 검증하는 empirical robotics systems study다. 저수준 force/torque 제어 또는 실물 접촉 안정화가 핵심 연구가 되면 별도 프로젝트로 분리하고, RP-2에는 그 결과를 recovery option의 구현으로만 연결한다.

## 1. 연구 질문

### 핵심 질문

> 동일한 cloned post-failure state에서 관찰한 option별 completion·risk·cost를 이용해 `Q(o | history, progress, budget)`을 학습하면, 같은 detector·option library·정보·총 실행 예산을 쓰는 best-fixed, scalar-risk, binary Retry/Reset, type-only heuristic보다 regret-to-oracle을 줄이고 BRCR을 높이면서 irreversible failure를 늘리지 않는가?

### 검증 가설

- **H0 — Arbitration precondition:** 비슷한 scalar alert를 가진 onset 사이에서 oracle-best option이 달라지고, 같은 onset에서도 recovery budget이 바뀌면 option ranking이 교차한다. best-fixed option과 O3 사이에 실질적인 regret/BRCR gap이 없으면 learned arbitration을 시작하지 않는다.
- **H1 — Recovery efficacy:** R1–R3 failure에서 same-onset branch-supervised option-value selector의 BRCR은 사전 고정한 strongest non-privileged baseline보다 높고 normalized option regret는 낮다.
- **H2 — Safety gate:** 제안 selector의 irreversible failure rate는 가장 안전한 실행 가능한 baseline보다 악화되지 않는다.
- **H3 — Clean non-degradation:** perturbation이 없는 episode에서 불필요한 intervention 때문에 native task success가 3 percentage point를 초과해 하락하지 않는다.
- **H4 — Attribution:** oracle onset·option outcome을 순차적으로 제공해도 이득이 없으면 detector/selector가 아니라 recovery option library 또는 task-state interface가 병목이다.

### 결정해야 할 세부 연구 질문

- **RQ0 — Option-value gap:** 같은 cloned onset에서 서로 다른 option의 completion·risk·cost가 실제로 구분되는가? O3가 best-fixed option보다 낫지 않으면 arbitration interface 자체를 기각한다.
- **RQ1 — Context crossing:** 같은 scalar failure-score bin과 비슷한 detection time에 속한 onset 사이에서 최적 recovery abstraction이 달라지는가? 달라지지 않으면 cause/recoverability belief는 장식적 label이다.
- **RQ2 — Budget crossing:** 동일 onset의 remaining recovery budget을 바꿀 때 최적 option ranking이 실제로 교차하는가? option 선택이 budget과 무관하면 `budgeted` claim을 제거한다.
- **RQ3 — 병목 분해:** detector calibration, context/belief encoding, option-value estimation, selector, option library 중 어느 요소가 BRCR–IFR trade-off를 제한하는가?
- **RQ4 — 전이성:** 동일한 selector와 event semantics가 LIBERO의 perturbation family에서 CALVIN sequence와 unseen onset으로 옮겨가는가? transfer가 없으면 benchmark-specific protocol로 주장 범위를 축소한다.
- **RQ5 — protocol의 독립성:** benchmark-native final success만 사용했을 때와 common onset/option schema를 사용했을 때 method ranking과 option regret 해석이 달라지는가? 추가 설명력이 없으면 I-12는 독립 contribution이 아니라 logging infrastructure다.

### novelty boundary

FLARE는 Retry/Reset을, ViFailback은 diagnosis/correction을, RT-H는 language-level intervention을, AgentChord는 recovery-augmented task graph를, When to Act, Ask, or Learn은 calibrated act/ask/intervene 선택을 이미 다룬다. ActFovea·Agentic RL·ProbeAct는 verified recovery, execution-mode selection, training-free safeguarding을, See, Plan, Rewind·FAR·CoRe·VLCP는 rewind, retry adaptation, imagined realignment, code-level replan을 탐색한다. Dream2Fix와 RedFlow는 counterfactual failure synthesis 및 action-level corrective learning으로 I-06의 broad data claim도 좁힌다. 그러므로 이 프로젝트는 “VLA recovery가 없다”, “multi-option recovery가 처음이다”, “counterfactual recovery가 처음이다”, “failure type을 분류하면 새롭다”고 주장하지 않는다. 남은 검증 단위는 다음으로 제한한다.

1. 동일 cloned onset에서 abstraction level이 다른 option을 모두 실행한 **same-onset option-outcome branch table**,
2. 같은 정보·horizon·option library와 **동일한 time/action/risk budget**에서의 selector 비교,
3. context와 budget에 따른 **option-ranking crossing** 및 best-fixed regret의 실증,
4. detector, value estimator, selector, option library 오류를 분리하는 **oracle decomposition**,
5. LIBERO에서 시작해 hold-out failure family 또는 CALVIN으로 옮기는 **frozen-selector transfer**.

`counterfactual`이라는 단어가 같은 estimand를 뜻하지 않으므로 다음을 분리한다.

| 용어 | 이 문서의 의미 | 직접 비교되는 최신 계열 | RP-2에서의 역할 |
|---|---|---|---|
| same-onset branch outcome | 실제 post-failure simulator state를 복원해 option만 바꾸고 실행한 outcome | 현재 source-verified set에서 동일 option/budget/regret 계약은 확인하지 못함 | C1의 train target과 O3 empirical oracle |
| synthesized failure counterfactual | 성공 demonstration/action을 바꿔 생성한 failure–correction pair | Dream2Fix | I-06 data baseline; same-onset option regret의 대체물이 아님 |
| imagined continuation counterfactual | world model/VLM으로 viable continuation을 예측하고 realign | CoRe | recovery option family와 model-based baseline 후보 |
| code/action correction | failed code/action을 재작성하거나 successful alternative로 redirect | VLCP·RedFlow | replan/correction option과 conditional post-training baseline |

RP-2의 핵심 용어는 가능하면 `same-onset multi-option branch supervision`으로 쓰고, 생성·상상 기반 방법과 혼동되는 broad `counterfactual recovery` 표현은 제목 외 본문 주장에서는 피한다.

### Operational motivation: detection과 recovery는 다른 문제다

장기 manipulation에서 failure가 한 번 발생하면 base VLA가 같은 action을 반복하거나, 반대로 너무 일찍 reset하여 이미 달성한 progress를 잃을 수 있다. 기존 benchmark의 final success만 보면 다음 세 사건이 하나의 실패로 뭉개진다.

| 사건 | 질문 | 필요한 신호 |
|---|---|---|
| `detection` | 지금 base action이 위험하거나 progress를 잃고 있는가? | failure score, detection delay, alert calibration |
| `diagnosis` | 관측 실패·접촉 실행·world-state·plan semantics 중 무엇인가? | partial-observation belief와 history |
| `recovery decision` | 지금 budget으로 어떤 option이 성공·안전한가? | option-conditioned completion/risk와 budget |

RP-2의 motivation은 “detector가 없다”가 아니라 **alert가 있어도 action-conditioned recovery decision이 닫히지 않는다**는 데 있다. 같은 scalar alert가 나와도 원인·발생 시점·남은 budget에 따라 `RETRY_CURRENT`, `STATE_RESET`, `SUBGOAL_REWIND`, `TASK_REPLAN`, `HUMAN_ESCALATE`의 상대가치가 달라질 수 있다. 이 crossing이 same-onset sweep과 held-out onset에서 실제로 관찰되지 않으면 learned arbitration을 유지하지 않고 scalar risk-triggered recovery 또는 I-12 protocol 결과로 축소한다.

## 1.1 Motivation과 novelty의 분리

[Motivation ≠ Novelty](https://gisbi-kim.github.io/motivation-is-not-novelty/)의 rubric을 적용하면, 현재 RP-2는 **문제 motivation은 강하지만 아직 novelty를 통과했다고 볼 수 없다**. 기존 VLA가 failure 뒤에 취약하고 detector만으로 recovery decision이 닫히지 않는다는 관찰은 motivation이다. `detector + type head + option selector`나 새 option 하나를 붙이는 것만으로는 “왜 그 형태여야 하는가”가 설명되지 않는다.

현재 문서가 method paper 수준의 주장으로 올라가기 위해 반드시 추가해야 하는 것은 다음이다.

1. **Naive baseline의 전수 failure audit:** SAFE/FAIL-Detect + abort/retry/best-fixed/binary Retry–Reset/type-only heuristic을 먼저 구현하고, cloned onset별 option outcome을 모두 기록한다.
2. **원리적 진단:** detector score는 `failure가 일어났을 확률`만 주고, action-conditioned recovery outcome, unavailable alternatives, remaining budget을 주지 않는다는 점을 formalize한다.
3. **해법 도출:** `belief/context × option-conditioned value × risk constraint × budget`에서 selector가 유도되어야 한다. type label은 필요성이 확인될 때만 보조 latent/auxiliary target으로 쓴다.
4. **단순화 반증:** best-fixed, scalar-risk, cause-only, budget-only, heuristic map, uniform-feasible, uncalibrated selector를 모두 비교해 same-onset option value가 실제로 필요한지 보인다.
5. **새 failure mode 분석:** learned selector에서 생기는 stale belief, detector delay, value miscalibration, option-call cost, false intervention, budget exhaustion을 별도 event로 기록한다.
6. **일반화 검증:** task·failure family·onset landmark·benchmark 중 최소 하나를 완전히 hold-out해, 단일 LIBERO perturbation에 맞춘 규칙이 아님을 확인한다.

따라서 이 프로젝트의 현재 claim ladder는 다음처럼 제한한다.

| Level | 주장 | 조건 |
|---|---|---|
| `C0` | common recovery event·clone·budget protocol | restore determinism, same-onset option table, metric 재현성만 확인된 경우 |
| `C1` | matched budget에서 same-onset branch-supervised option-value arbitration이 best-fixed/scalar/binary/type-only baseline보다 유리 | RQ0–RQ2의 crossing·regret evidence, option-value ablation, IFR non-degradation |
| `C2` | learned selector가 benchmark·failure family를 넘어 일반화 | CALVIN 또는 hold-out family에서 frozen selector transfer |
| `C3` | 실제 safety improvement | LIBERO-Safety 또는 real-robot physical safety에서 별도 검증. LIBERO pilot만으로 주장하지 않음 |

현재 최소 목표는 `C1`이며, `C0`만 남으면 method paper가 아니라 evaluation/protocol 결과로 보고한다.

## 2. 기반 논문과 차용 방법

| 근거 | 차용하는 요소 | 그대로 주장하지 않을 부분 |
|---|---|---|
| [POMDP](../../1998/Artificial-Intelligence/1998_Artificial-Intelligence_Planning-and-Acting-in-Partially-Observable-Stochastic-Dom/01_overview.md) | belief-state와 finite-memory decision formulation | 관측 history가 정확한 hidden state나 recoverability label을 제공한다는 가정 |
| [Q-learning](../../1992/Machine-Learning/1992_Machine-Learning_Q-Learning/01_overview.md) | action-conditioned return과 greedy decision의 기초 | offline cloned branch의 support 밖 option value가 정확하다는 가정 |
| [RT-H](../../2024/Robotics-Science-and-Sys/2024_Robotics-Science-and-Sys_RT-H-Action-Hierarchies-Using-Language/01_overview.md) | language motion을 중간 action abstraction으로 쓰는 hierarchy와 intervention interface | language correction 하나가 모든 post-failure option family를 대표한다는 해석 |
| [SAFE](../../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md) | frozen VLA latent feature, temporal failure score, functional conformal threshold | conformal alert가 곧 원인 진단이나 recovery guarantee라는 해석 |
| [Recovery RL](../../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md) | task policy와 recovery policy 분리, safety critic에 의한 switching | 하나의 recovery policy가 semantic failure type 전체를 해결한다는 가정 |
| [PDDLStream](../../2020/ICAPS/2020_ICAPS_PDDLStream-Integrating-Symbolic-Planners-and-Blackbox-Samp/01_overview.md) | symbolic predicate와 continuous feasibility를 잇는 replanning interface | 최소 LIBERO 실험부터 전체 PDDLStream domain을 새로 구축하는 것 |
| [FurnitureBench](../../2023/RSS/2023_RSS_FurnitureBench-Reproducible-Real-World-Benchmark-for-Long/01_overview.md) | final success 외 phase/skill progress 기록 | FurnitureBench 고유 taxonomy를 다른 benchmark에 그대로 이식하는 것 |
| [AtomicVLA](../../2026/CVPR/2026_CVPR_AtomicVLA-Unlocking-the-Potential-of-Atomic-Skill-Learning/01_overview.md) | CALVIN의 failure 이후 termination이 recovery 측정을 왜곡할 수 있다는 문제 제기 | benchmark 결과와 실제 recovery capability를 동일시하는 것 |
| [VLA-FixBench/FaultEval](../../2026/ICML/2026_ICML_Can-VLMs-Diagnose-and-Recover-from-VLA-Manipulation-Faults/01_overview.md) | fault taxonomy, diagnosis, rollback recovery benchmark cue | benchmark의 reported upper bound를 제안 selector의 일반화 보장으로 해석하는 것 |
| [Temporal Difference Calibration](../../2026/ICML/2026_ICML_Temporal-Difference-Calibration-in-Sequential-Tasks-Applic/01_overview.md) | sequential value/confidence calibration signal | calibrated confidence가 원인·recoverability를 직접 식별한다고 가정하는 것 |
| [CALVIN](../../2022/RA-L/2022_RA-L_CALVIN-A-Benchmark-for-Language-Conditioned-Policy-Learnin/01_overview.md) | 언어 조건 five-subtask sequence와 task oracle | 첫 실패에서 sequence를 끝내는 표준 evaluator |
| [LIBERO](../../2023/NeurIPS/2023_NeurIPS_Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learnin/01_overview.md) | fixed initial states, BDDL goal predicate, long-horizon task suite | lifelong-learning 평균만을 recovery 성능으로 해석하는 것 |
| [Beyond Binary Success](https://roboticsconference.org/program/papers/76/) | sequential partial-progress comparison과 효율적인 paired evaluation | 새 metric 하나가 recovery decision의 novelty라는 주장 |
| [Discounted Liveness OPE](https://roboticsconference.org/program/papers/154/) | non-monotonic progress와 liveness-aware off-policy evaluation | OPE 추정치를 real closed-loop recovery outcome과 동일시하는 것 |

직접적인 frontier counter-evidence도 baseline 설계에 포함한다.

- [FLARE (CVPR 2026)](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_FLARE_A_Failure-Aware_Framework_for_Autonomous_Correction_and_Recovery_in_CVPR_2026_paper.html): Retry/Reset 이진 recovery dispatcher. 반드시 strong baseline 또는 privileged binary upper bound로 둔다.
- [VLA-FixBench/FaultEval (ICML 2026)](https://kakigo.github.io/VLA-FixBench/): fault diagnosis와 rollback recovery benchmark. taxonomy·rollback을 비교 protocol에 포함하되, 저자 구현을 재현하기 전에는 reported result를 upper bound로 복사하지 않는다.
- [Temporal Difference Calibration (ICML 2026)](https://arxiv.org/abs/2604.20472): sequential task-success confidence를 TD/value estimation으로 보정하는 calibration baseline. alert threshold와 selector를 분리한다.
- [FailSafe (arXiv 2025)](https://arxiv.org/abs/2510.01642): failure generation과 executable recovery pair. peer-reviewed 결과와 구분해 perturbation/recovery-pair 설계의 참고로만 쓴다.
- [LIBERO-Safety (ECCV 2026)](https://libero-safety.github.io/): physical/semantic safety perturbation과 violation 평가. 표준 LIBERO pilot 이후 R4 안전성 검증용 확장으로 둔다.
- [ViFailback (CVPR 2026)](https://openaccess.thecvf.com/content/CVPR2026/html/Zeng_Diagnose_Correct_and_Learn_from_Manipulation_Failures_via_Visual_Symbols_CVPR_2026_paper.html): visual-symbol diagnosis와 correction. correction family가 이미 존재하므로 진단 label 자체를 novelty로 두지 않는다.
- [AgentChord (RSS 2026)](https://roboticsconference.org/program/papers/180/): recovery-augmented task graph와 low-latency orchestration. precompiled recovery branch를 strong graph baseline으로 둔다.
- [When to Act, Ask, or Learn (RSS 2026)](https://roboticsconference.org/program/papers/142/): calibrated act/ask/intervene 선택. human escalation을 포함하는 가장 가까운 selector family로 비교한다.
- [Gemini Robotics 2 (Google DeepMind official, 2026)](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/): multi-step progress/event detection과 self-correction이 broad capability로 이미 제시됐음을 확인한다. 공개된 matched implementation이 없으므로 capability boundary이지 primary baseline이 아니다.
- [ActFovea](https://arxiv.org/abs/2607.29169) `PREPRINT`: spatiotemporal visual-action consistency, disturbance-specific candidate observation, action-chunk verification과 bounded safe failure. observation recovery와 safe-abstain의 강한 collision baseline이다.
- [Learning Robust Execution with Agentic RL](https://arxiv.org/html/2607.13818v1) `PREPRINT / FULL-TEXT-CHECKED`: history-conditioned policy가 `Execute/Retry/Repair/Reset`을 PPO로 선택하고 LIBERO에서 평가된다. same-onset all-option target·best-fixed regret·vector-budget contract는 reported primary protocol에서 확인되지 않았으므로 X5의 정확한 residual comparison 대상으로 둔다.
- [ProbeAct](https://arxiv.org/abs/2606.09740) `PREPRINT`: hidden-state probe, kinematic failure state machine과 CBF correction. fixed training-free recovery/safety-net family로 비교한다.
- [Robo-Dopamine 2.0](https://arxiv.org/abs/2608.15680) `PREPRINT`: history/OOD-aware process reward와 signed progress–failure–recovery space. option value가 아니라 scalar/history reward baseline으로 둔다.
- [Dream2Fix](https://arxiv.org/abs/2603.13528) `PREPRINT`: generative world model 기반 counterfactual failure–correction synthesis. same-onset alternative option outcome과 구분해 I-06 data baseline으로만 사용한다.
- [RedFlow](https://arxiv.org/abs/2607.27782) `PREPRINT`: failure-inducing action과 successful alternative를 연결하는 offline corrective learning. runtime selector보다 conditional policy-reuse baseline이다.
- [SO-101 Failure and Recovery Analysis](https://arxiv.org/abs/2606.08881) `PREPRINT`: recovery-aware evaluation 신호. 독립 metric novelty의 collision check로만 사용한다.

다음 2026 자료는 retired 2026-08-28 gap-audit 기록에서 `PREPRINT-ONLY`로 확인한 novelty-collision set이다. venue-confirmed baseline과 같은 evidence level로 취급하지 않으며, status를 다시 사용할 때는 공식 source를 재검증하고 코드와 observation/action contract를 확인할 수 있을 때만 matched implementation baseline으로 올린다.

- [See, Plan, Rewind](https://arxiv.org/abs/2603.09292): progress-aware subgoal rewind.
- [FAR](https://arxiv.org/abs/2607.01111): retry perturbation과 failure-preference adaptation.
- [Imagining Recovery / CoRe](https://arxiv.org/abs/2608.14822): imagined continuation과 state realignment.
- [VLCP](https://arxiv.org/abs/2608.16978): control-code abstraction의 closed-loop replanning.

### 제안 method의 최소 형태

대형 VLA를 다시 학습하지 않는다.

1. SAFE 방식으로 frozen VLA feature `z_1:t`와 관측 history에서 alert score를 계산하고, TD calibration을 독립 ablation으로 둔다.
2. `D2-option`의 same-onset sweep으로 각 `(onset, option, budget)`의 completion·irreversibility·cost target을 만든다.
3. 작은 context/belief encoder는 `z_1:t`, proprioception/action history, detector history, normalized elapsed step, budget을 요약한다. OpenVLA가 native subgoal을 노출하지 않으므로 primary `O_core`에는 oracle current-subgoal feature를 넣지 않는다. cause/recoverability는 auxiliary target이며 필수 inference label이 아니다.
4. option-value head가 고정 recovery option마다 `P(goal completion)`, `P(irreversible event)`, expected execution cost를 예측한다.
5. selector는 남은 vector budget 안에서 risk threshold를 만족하는 option 중 calibrated utility가 가장 높은 것을 고르고, feasible option이 없으면 primary autonomous protocol에서는 `ABORT_STOP`으로 abstain한다. `HUMAN_ESCALATE`는 assisted-evaluation extension에서만 허용한다.

Conformal calibration은 alert threshold에만 적용한다. distribution shift가 있는 recoverability classification이나 option-value 전체에 같은 보장을 확장해 주장하지 않는다.

### Method interface와 정보 경계

| 단계 | 실제 입력 | 출력 | oracle 접근 허용 여부 |
|---|---|---|---|
| detector | frozen VLA feature, observation/action history | alert score와 `t_detect` | `t_effect`는 평가 logger에만 존재 |
| context/belief encoder | VLA feature, proprioception/action·alert history, normalized elapsed step, budget vector | latent context; optional cause/recoverability belief | cause/R·BDDL progress·subgoal label은 auxiliary/evaluator field일 뿐 primary inference 입력이 아님 |
| option-value head | 같은 belief와 각 option descriptor | `q_o`, `r_o`, cost/latency prediction | cloned-state outcome은 train target, test-time oracle sweep 금지 |
| selector | calibrated q/r, feasibility, budget | 단일 recovery option 또는 abstain | task predicate는 fixed replan option 내부에서만 사용 |
| option/controller | 현재 observation과 fixed skill/controller | 실제 action sequence | P1과 baseline이 동일 library를 공유 |

이 경계를 지키지 않으면 privileged replan이나 oracle label을 P1의 method gain으로 잘못 계산하게 된다. 모든 event logger field를 policy-visible feature와 evaluator-only annotation으로 분리한다.

### 학습·라벨·추론 프로토콜

P1은 `frozen base policy + lightweight heads + deterministic constrained selector`로 고정한다. end-to-end VLA fine-tuning이나 test-time recovery-data collection은 minimum experiment의 범위가 아니다. 그래야 성능 차이를 base policy의 능력 차이가 아니라 detector·belief·option-value·budget decision의 차이로 귀속할 수 있다.

#### 데이터 생성과 target

1. **Base rollout:** train split의 clean rollout을 먼저 실행하고, 사전 등록한 event landmark에서 perturbation을 주입한다. primary `O_core` 정책이 볼 수 있는 입력은 VLA feature, proprioception, 이전 action, alert history, normalized elapsed step, policy memory/cache와 remaining budget뿐이다. `t_inject`, BDDL progress, oracle subgoal/cause/acceptable-option set은 logger에만 남긴다.
2. **Cloned-state option sweep:** `t_effect`의 simulator state를 clone한 뒤 모든 option을 같은 rollout seed로 실행한다. 각 `(onset state, option, budget)`에 대해 `goal_success`, `irreversible_event`, recovery steps, option calls를 저장한다. 이 sweep 결과가 `q_o`, `r_o`의 supervised target과 R1–R4의 평가용 acceptable-option set을 만든다.
3. **Head fitting:** P1의 primary alert score는 frozen SAFE/FAIL-Detect 출력으로 두고 threshold만 calibration한다. 별도 detector sensitivity에서만 alert head를 failure onset window의 binary target으로 학습한다. context encoder는 option-conditioned target을 주로 학습하고 `cause × operational recoverability`는 auxiliary ablation으로만 사용한다. test split의 sweep 결과는 학습·threshold 선택·early stopping에 사용하지 않는다.
4. **Calibration:** alert threshold와 q/r calibration parameters는 calibration split에서만 고정한다. 기본 P1은 SAFE 계열 alert에 functional conformal threshold를 적용하고, option-value에는 temperature/isotonic calibration을 별도 ablation으로 둔다. calibration이 이동 분포에 formal coverage를 준다고 주장하지 않는다.

제안하는 multi-task objective는 다음처럼 기록한다. 실제 loss weight는 train split에서만 선택하고, 모든 ablation은 같은 weight-selection 규칙을 사용한다.

```text
L = λa · BCE(alert, y_alert)
  + λaux · CE(aux_type, y_cause×R)
  + Σ_o [λq · BCE(q_o, y_success,o)
       + λr · BCE(r_o, y_irreversible,o)
       + λk · Huber(k_o, y_cost,o)]
```

P1에서는 `alert`가 frozen detector score이므로 `λa` 항을 학습하지 않고 threshold calibration만 수행한다. `λaux=0`인 direct option-value model을 기본 비교에 포함하고, auxiliary type target의 이득은 ablation으로만 보고한다. `λa`를 활성화한 trainable alert head는 별도 detector sensitivity로 보고해 detector 학습 효과와 arbitration 효과를 섞지 않는다.

`y_success,o`는 native horizon과 budget 안의 goal completion, `y_irreversible,o`는 option rollout 중 absorbing safety event 여부다. `not_applicable` option은 loss와 metric에서 mask하되, selector가 임의로 성공 처리하지 않는다. class imbalance는 train split의 inverse-frequency weight로만 보정한다.

#### 추론 계약

- selector는 alert가 발생한 시점에 한 번 평가하고, `recovery_started` 이후에는 option을 중간에 바꾸지 않는다. 재평가는 `REOBSERVE_WAIT`가 fresh observation을 반환한 뒤에만 허용한다.
- `q_o`와 `r_o`가 모두 불확실하거나 risk constraint를 만족하는 option이 없으면 primary autonomous protocol에서는 `ABORT_STOP`으로 abstain한다. assisted extension의 `HUMAN_ESCALATE`도 completion으로 세지 않고 `correct_abort`, `correct_escalation`, `unnecessary_abort/escalation`으로 분리한다.
- P1과 모든 learned ablation은 같은 frozen feature cache, head parameter budget, training step 수, inference call 수를 사용한다. selector overhead와 p50/p95 decision latency는 별도 기록한다.
- primary progress input은 `t/native_horizon`뿐이다. richer learned progress는 별도 sensitivity이며 observation/action history만 사용한다. benchmark evaluator의 goal predicate와 BDDL subgoal은 training input이 아니라 event label과 최종 평가에만 사용한다.

### Novelty를 위해 필요한 same-onset multi-option decision formulation

failure type을 먼저 정하고 classifier를 붙이는 방식은 novelty 근거가 약하다. 최소 formulation은 관측 history와 recovery budget에서 option-conditioned outcome을 결정하는 constrained belief decision이며, supervision은 동일 onset의 alternative option rollout에서 온다.

```text
b_t = f(z_1:t, proprio_1:t, a_1:t-1, alert_1:t, t/H, B_t, g_t^optional)
q_o = P(goal_completion | b_t, option=o, B_t)
r_o = P(irreversible_event | b_t, option=o, B_t)
k_o = E[steps, calls, replans, latency | b_t, option=o, B_t]

o* = argmax_o q_o - λᵀ · k_o
     subject to r_o ≤ δ and feasible(o, B_t) = 1
```

- `b_t`는 detector score 하나가 아니라 VLA feature, proprioception, 최근 action·alert, normalized elapsed step, remaining budget을 요약한다. `g_t^optional`은 `O_graph`의 non-privileged subgoal adapter가 통과한 extension에서만 사용한다.
- `q_o`, `r_o`, `k_o`는 option마다 달라야 한다. 같은 alert score에서도 `REOBSERVE_WAIT`, `RETRY_CURRENT`, `STATE_RESET`, `SUBGOAL_REWIND`, `TASK_REPLAN`의 outcome이 달라지는 것이 arbitration의 전제다.
- `B_t`는 native horizon, recovery steps, option calls, replans, irreversible-event allowance의 vector다. scalar penalty 하나로 합쳐서 budget effect를 숨기지 않는다.
- `δ`는 safety gate이며 calibration의 대상이다. 모든 option-value prediction에 formal guarantee가 있다고 주장하지 않는다.

fit/calibration onset에서는 모든 option outcome을 관찰하지만 test-time selector는 선택하지 않은 option의 결과를 볼 수 없다. 기존 schema의 `counterfactual_group_id`는 호환성을 위해 유지하지만, 이것은 인과효과의 완전한 식별을 뜻하지 않는다. 주장은 **cloned state에서 alternative option outcomes를 실제 실행해 구축한 same-onset supervised comparison**으로 한정한다. state restore가 불완전하거나 option rollout이 stochastic하면 seed-matched 반복과 uncertainty interval을 유지한다.

이 formulation에서 `failure_cause`와 `recoverability`는 최종 contribution이 아니라 action value를 설명할 수 있는 auxiliary variable이다. scalar alert와 remaining budget만으로 같은 ranking을 예측하거나 type-only heuristic이 P1과 동률이면 type head를 제거한다. best-fixed option이 O3와 동률이면 option-value selector 전체를 제거한다.

### 학습 문제의 정확한 분류와 decision-aware 보강

`D2-option`은 fit/calibration onset에서 모든 applicable option의 outcome을 관찰하므로, primary 학습 문제는 online RL이나 logged-action offline RL이 아니라 **grouped full-information cost-sensitive decision learning**이다. 하나의 onset을 하나의 group으로 두고 option별 반복 rollout의 empirical rate와 cost를 함께 학습한다. 이 구분은 Agentic RL과의 차이를 명확히 하고, 관찰하지 않은 option을 Q-learning으로 외삽했다는 과도한 주장을 막는다.

```text
ȳsuccess(s,o,B) = mean_seed[goal_success]
ȳrisk(s,o,B)    = mean_seed[irreversible_event]
k̄(s,o,B)       = mean_seed[normalized vector cost]

Lpred = Σ_(s,o,B) BCE(q̂, ȳsuccess) + BCE(r̂, ȳrisk) + Huber(k̂, k̄)
Lrank = Σ_(o+,o-) log(1 + exp(-(Û(o+) - Û(o-))/τ))
Ltotal = Lpred + λrank · Lrank + λaux · Laux
```

- `Lrank` pair는 seed-matched utility interval이 구분되는 option pair에만 만든다. 불확실한 tie를 임의의 hard rank로 학습하지 않는다.
- primary P1은 calibrated `q/r/k`를 유지해 해석과 oracle decomposition이 가능해야 한다. [RankNet](https://doi.org/10.1145/1102351.1102363)과 [decision-focused learning의 ranking 관점](https://proceedings.mlr.press/v162/mandi22a.html)은 `Lrank`의 근거이며, ranking loss 자체를 robotics novelty로 주장하지 않는다.
- `λrank=0` prediction-only model을 최소 primary로 두고, `λrank=1`의 P1-rank를 사전 등록한 method sensitivity로 둔다. ranking loss가 option regret만 개선하면서 calibration을 훼손하는지 분리하고, confirmatory test를 보기 전에 primary variant를 고정한다.
- `ABORT_STOP/HUMAN_ESCALATE`는 일반 completion option과 같은 success label로 학습하지 않는다. autonomous option이 risk gate를 통과하지 못할 때의 reject action으로 모델링하고, [selective classification](https://jmlr.csail.mit.edu/papers/v11/el-yaniv10a.html)의 risk–coverage 관점으로 평가한다.

Primary selector는 arbitrary scalarization 하나에 의존하지 않도록 다음 safety-first lexicographic rule로 고정한다.

1. 현재 vector budget과 option precondition을 만족하지 않는 option을 mask한다.
2. calibration에서 고정한 risk threshold `δ`를 만족하는 option만 남긴다.
3. calibrated completion probability `q_o`가 가장 큰 option을 고른다.
4. `q_o`가 calibration tolerance 안에서 동률이면 normalized recovery cost가 작은 option을 고른다.
5. feasible option이 없으면 `ABORT_STOP`; 별도 assisted-evaluation에서만 `HUMAN_ESCALATE`를 허용한다.

기존 `q_o - λᵀk_o` weighted selector는 cost-weight sensitivity로 유지한다. primary claim은 lexicographic selector와 budget-constrained Pareto 결과를 사용해 특정 `λ` 선택에 의존하지 않게 한다.

### 기반 논문에서 baseline으로 가져올 역할

| 역할 | 필수 paper | RP-2에서 가져올 것 | 구현상 주의 |
|---|---|---|---|
| partial-observation formulation | [POMDP](../../1998/Artificial-Intelligence/1998_Artificial-Intelligence_Planning-and-Acting-in-Partially-Observable-Stochastic-Dom/01_overview.md), [DAgger](../../2011/AISTATS/2011_AISTATS_A-Reduction-of-Imitation-Learning-and-Structured-Predictio/01_overview.md) | belief, learner-induced failure-state, history dependence | hidden state를 oracle feature로 넣지 않음 |
| safety/recovery switching | [Recovery RL](../../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md), [CBF-QP](../../2017/TAC/2017_TAC_Control-Barrier-Function-Based-Quadratic-Programs-for-Safe/01_overview.md) | task/recovery 분리, risk gate와 safe set | semantic recovery 전체를 safety critic 하나로 대체하지 않음 |
| runtime detector | [FAIL-Detect](../../2025/RSS/2025_RSS_Can-We-Detect-Failures-Without-Failure-Data-Uncertainty-Aw/01_overview.md), [SAFE](../../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md), [TD calibration](../../2026/ICML/2026_ICML_Temporal-Difference-Calibration-in-Sequential-Tasks-Applic/01_overview.md) | detector/threshold/calibration baseline | alert와 cause inference를 분리 |
| recovery dispatcher | [FLARE](../../2026/CVPR/2026_CVPR_FLARE-A-Failure-Aware-Framework-for-Autonomous-Correction/01_overview.md), [VLA-FixBench/FaultEval](../../2026/ICML/2026_ICML_Can-VLMs-Diagnose-and-Recover-from-VLA-Manipulation-Faults/01_overview.md), [ViFailback](https://openaccess.thecvf.com/content/CVPR2026/html/Zeng_Diagnose_Correct_and_Learn_from_Manipulation_Failures_via_Visual_Symbols_CVPR_2026_paper.html) | binary Retry/Reset, diagnosis/correction, rollback taxonomy | 저자 구현을 재현하기 전 reported number를 이식하지 않음 |
| recovery graph/escalation | [AgentChord](https://roboticsconference.org/program/papers/180/), [When to Act, Ask, or Learn](https://roboticsconference.org/program/papers/142/) | precompiled recovery branch, act/ask/intervene calibration | task graph·human oracle·추가 VLM 정보를 P1에만 주지 않음 |
| continuous replanning | [PDDLStream](../../2020/ICAPS/2020_ICAPS_PDDLStream-Integrating-Symbolic-Planners-and-Blackbox-Samp/01_overview.md) | task predicate와 continuous feasibility interface | pilot에서는 privileged replan과 learned replan을 구분 |
| evaluation semantics | [LIBERO](../../2023/NeurIPS/2023_NeurIPS_Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learnin/01_overview.md), [CALVIN](../../2022/RA-L/2022_RA-L_CALVIN-A-Benchmark-for-Language-Conditioned-Policy-Learnin/01_overview.md), [AtomicVLA](../../2026/CVPR/2026_CVPR_AtomicVLA-Unlocking-the-Potential-of-Atomic-Skill-Learning/01_overview.md), [FurnitureBench](../../2023/RSS/2023_RSS_FurnitureBench-Reproducible-Real-World-Benchmark-for-Long/01_overview.md), [Beyond Binary Success](https://roboticsconference.org/program/papers/76/), [Discounted Liveness OPE](https://roboticsconference.org/program/papers/154/) | fixed state, partial progress, post-failure continuation, non-monotonic liveness | final success나 새 metric만으로 recovery method novelty를 주장하지 않음 |
| frozen base policy | [OpenVLA](../../2024/CoRL/2024_CoRL_OpenVLA-An-Open-Source-Vision-Language-Action-Model/01_overview.md), [Octo](../../2024/RSS/2024_RSS_Octo-An-Open-Source-Generalist-Robot-Policy/01_overview.md), [π0](../../2025/RSS/2025_RSS_pi0-A-Vision-Language-Action-Flow-Model-for-General-Robot/01_overview.md) | action interface와 inference budget 비교 | base policy를 바꾸면서 recovery claim을 섞지 않음 |

이 표의 핵심은 논문 수를 늘리는 것이 아니라, `detector → context/belief → option value·risk·cost → constrained selector → benchmark outcome`의 각 경계를 독립 baseline으로 고정하는 것이다.

## 3. Benchmark 결정

| 항목 | LIBERO-Long | CALVIN | 결정 |
|---|---|---|---|
| 초기 상태 | task별 fixed initial states | sequence별 초기 상태와 neutral reset | paired option comparison은 LIBERO가 단순 |
| 성공 판정 | BDDL goal predicate, success 시 `done` | task oracle가 start/current state 변화를 판정 | 둘 다 사용 가능 |
| 표준 horizon | config 기본 `max_steps=600` | subtask당 `EP_LEN=360` | pilot budget은 LIBERO 600-step 안에 포함 |
| failure 이후 실행 | timeout 전까지 계속 실행 가능 | 표준 sequence evaluator가 첫 failed subtask에서 반환 | CALVIN은 evaluator fork 필요 |
| 장기 구조 | `libero_10`의 multi-object/articulated tasks | 5개 instruction sequence, 1,000 sequence 표준 평가 | CALVIN이 transfer validation에 적합 |
| simulator state clone/injection | MuJoCo state와 BDDL predicate 활용 가능 | scene/task oracle adapter 필요 | I-12 구현은 LIBERO부터 시작 |

**결론:** minimum experiment는 `LIBERO-Long`으로 확정한다. CALVIN은 event schema가 안정화된 뒤 두 번째 benchmark로 추가한다. VLA-Arena의 170-task Safety·Distractor·Extrapolation·Long-Horizon suite는 event-level clone/injection interface가 없어 primary evaluator로 쓰지 않고, schema가 안정화된 뒤 stress-suite로 결과를 교차 확인한다. 표준 LIBERO는 실제 물리적 위해를 충분히 표현하지 못하므로 R4 결과를 real-world safety claim으로 확대하지 않고, 이후 LIBERO-Safety 또는 실제 robot safety setup에서 별도로 확인한다.

공식 구현 감사 기준은 다음과 같다.

- [LIBERO metric implementation](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/8f1084e3132a39270c3a13ebe37270a43ece2a01/libero/lifelong/metric.py): fixed init state, `done`, max-step rollout을 사용하는 평가 루프.
- [LIBERO repository](https://github.com/Lifelong-Robot-Learning/LIBERO/tree/8f1084e3132a39270c3a13ebe37270a43ece2a01): 이번 설계에서 감사한 upstream commit.
- [CALVIN evaluator](https://github.com/mees/calvin/blob/fa03f01f19c65920e18cf37398a9ce859274af76/calvin_models/calvin_agent/evaluation/evaluate_policy.py): `EP_LEN=360`, `NUM_SEQUENCES=1000`, 첫 failed subtask에서 sequence 반환.
- [CALVIN repository](https://github.com/mees/calvin/tree/fa03f01f19c65920e18cf37398a9ce859274af76): 이번 설계에서 감사한 upstream commit.

### Dataset construction과 split 계약

RP-2에서 말하는 dataset은 새로운 대규모 demonstration corpus가 아니라, **frozen policy rollout + controlled perturbation + cloned-state option sweep**으로 만든 event/decision dataset이다. 원본 benchmark demonstration과 injected recovery data를 같은 것으로 세지 않는다.

| Split | LIBERO-Long 구성 | 사용 목적 | 금지 사항 |
|---|---|---|---|
| `fit` | `libero_10`의 6개 task, task당 10개 fixed init state, perturbation seed 0–1 | alert/context/option-value head 학습 | calibration/test task와 task·init-state 중복 금지 |
| `calibration` | 별도 2개 task, task당 10개 init state, seed 2 | alert threshold, q/r calibration, early stopping | head weight 재학습 금지 |
| `confirmatory-test` | 별도 2개 task, task당 20개 init state, seed 3–5 | 최종 primary/secondary metric | threshold·option map·task 선택 변경 금지 |
| `phase-1-dev` | `libero_10`의 4-task pilot manifest에서 2/1/1 task split | wrapper와 crossing evidence 탐색 | method claim의 최종 수치로 보고 금지 |

- 정확한 task ID와 family stratification은 첫 실행 전에 `rp2_split_v1.json`으로 고정한다. articulated receptacle, multi-object, precise placement, drawer/microwave state가 fit/cal/test에 모두 분포하도록 하되, 같은 task의 init state를 split 사이에 복제하지 않는다.
- `episode_id`는 `benchmark × task × init_state × perturbation × severity × seed`로 만든다. 모든 system은 동일 ID를 공유하므로 paired comparison이 가능하다.
- perturbation recipe와 onset landmark가 split을 넘어가더라도 exact `(recipe, onset state, seed)`는 재사용하지 않는다. 일반화를 보이려면 confirmatory-test에 최소 한 개의 holdout onset landmark 또는 failure family를 남긴다.
- option sweep의 oracle outcome은 fit/calibration에서만 head target으로 사용한다. confirmatory-test에서는 O3를 평가용 upper bound로만 실행하며, 그 결과로 P1을 재학습하거나 threshold를 다시 고르지 않는다.

CALVIN은 LIBERO에서 학습한 selector의 **zero-shot transfer**가 기본이다. 별도 `calibration-only` 결과는 report할 수 있지만, CALVIN test sequence에서 context/value head를 재학습한 결과를 zero-shot claim과 섞지 않는다. CALVIN의 첫 failed subtask에서 조기 종료하는 upstream evaluator와 recovery 이후 계속하는 RP-2 fork를 둘 다 실행해 evaluator choice의 영향을 분리한다.

#### Dataset layer와 provenance

| Layer | 생성물 | 포함 정보 | 평가 역할 |
|---|---|---|---|
| `D0-native` | clean base-policy rollout | observation/action/progress, native success/failure | detector calibration과 clean non-degradation |
| `D1-event` | controlled perturbation event stream | injection/onset/alert/intervention/recovery timestamps | failure detection·event metric |
| `D2-option` | cloned-state, budget-conditioned option sweep table | 동일 onset의 option별 success/risk/cost, ranking, acceptable set | value head target, crossing audit, O3 upper bound |
| `D3-transfer` | CALVIN adapter/fork rollout | sequence-level event와 remaining subtask progress | zero-shot transfer |
| `D4-physical` (optional) | real-robot rollout | hardware latency, contact/force, safe stop, operator intervention | C3 physical claim만 검증 |

`D0–D3`는 동일한 benchmark simulator artifact가 아니라 역할이 다른 산출물이다. 특히 `D2-option`은 test episode의 미래를 미리 본 label이므로 P1 inference에서 호출할 수 없다. 각 artifact header에는 `base_policy_hash`, `environment_commit`, `event_schema_version`, `factor_manifest_version`, `option_library_version`, `seed`, `state_hash`를 기록해 재생성 가능성을 보장한다. `D4-physical`은 현재 필수 dataset이 아니며, hardware가 정해지기 전에는 수치나 safety claim을 미리 적지 않는다.

## 4. I-12 Recovery event schema

### 저장 단위

- 한 episode에 하나의 immutable JSONL event stream을 저장한다.
- image/state/action tensor는 별도 artifact에 저장하고 event에는 `state_ref`, `observation_ref`, `action_ref`만 남긴다.
- benchmark-native log를 덮어쓰지 않고 adapter가 공통 field로 변환한다.
- evaluator가 아는 injection 정보와 policy가 실제로 볼 수 있는 정보는 분리한다. `t_inject`, oracle cause, oracle recoverability는 selector input으로 전달하지 않는다.
- cloned sweep의 모든 branch는 같은 `onset_state_id`, `counterfactual_group_id`, `budget_id`, rollout seed를 공유한다. branch마다 option만 바뀌며 restore 뒤 observation/predicate hash가 validity tolerance를 통과해야 한다.

### Episode header

| Field | 의미 |
|---|---|
| `schema_version` | 현재 draft는 `rp2.event.v2`; v1의 reset/replan/abort semantics를 분리 |
| `episode_id` | benchmark, task, init state, perturbation, seed로 만든 고유 ID |
| `benchmark`, `suite`, `task_id` | 예: `libero`, `libero_10`, BDDL task name |
| `instruction` | 현재 language goal 또는 subtask |
| `policy_id`, `checkpoint_hash` | base policy와 exact checkpoint |
| `detector_id`, `selector_id` | detector/selector ablation 식별자 |
| `seed`, `init_state_id` | paired comparison 재현 키 |
| `perturbation_id`, `severity` | perturbation family와 level |
| `onset_state_id`, `counterfactual_group_id` | 같은 post-failure state와 alternative option branch를 묶는 키 |
| `option_library_version`, `budget_id` | option semantics와 vector-budget configuration |
| `native_horizon` | LIBERO pilot은 600 |
| `budget` | `recovery_steps`, `option_calls`, `rewinds`, `replans`, `human_escalations`, `irreversible_events` |

### Event record

```json
{
  "schema_version": "rp2.event.v2",
  "episode_id": "libero10.task04.init03.action_grasp.s1.seed07",
  "event_id": 12,
  "t_step": 184,
  "sim_time": 6.13,
  "source": "detector",
  "event_type": "failure_alert",
  "onset_state_id": "sha256:...",
  "counterfactual_group_id": "libero10.task04.onset003.budget120.seed07",
  "failure_cause": "execution_contact",
  "recoverability": "R2",
  "confidence": 0.83,
  "option": null,
  "state_ref": "states/episode.npz#184",
  "observation_ref": "obs/episode.zarr#184",
  "action_ref": "actions/episode.npy#184",
  "budget_before": {"recovery_steps": 120, "option_calls": 2, "rewinds": 1, "replans": 1, "human_escalations": 1},
  "budget_after": {"recovery_steps": 120, "option_calls": 2, "rewinds": 1, "replans": 1, "human_escalations": 1},
  "metadata": {"threshold": 0.71, "detector_score": 0.76}
}
```

필수 `source`는 `environment_oracle`, `perturbation_wrapper`, `detector`, `selector`, `policy`, `evaluator`다. 필수 `event_type`은 다음과 같다.

`episode_start`, `task_progress`, `perturbation_injected`, `failure_manifested`, `failure_alert`, `recovery_selected`, `recovery_started`, `option_outcome`, `recovery_succeeded`, `recovery_failed`, `safety_violation`, `task_success`, `abort_stop`, `human_escalated`, `assisted_completion`, `timeout`, `episode_end`.

### 시간 정의

| Timestamp | 정의 |
|---|---|
| `t_inject` | evaluator가 perturbation을 가한 시각. 정책에는 비공개 |
| `t_effect` | oracle predicate 또는 progress invariant가 처음 깨져 failure가 실제로 나타난 시각 |
| `t_detect` | detector score가 사전 등록 threshold를 처음 넘은 시각 |
| `t_intervene` | selector가 base action을 중단하고 recovery option을 시작한 시각 |
| `t_recovered` | task-valid/recoverable set으로 복귀한 최초 시각 |
| `t_success` | benchmark-native goal predicate가 만족된 시각 |
| `t_terminal` | success, timeout, abort stop, autonomous-evaluation 종료를 동반한 human escalation, irreversible event 중 하나로 끝난 시각 |

`t_inject`를 failure onset으로 사용하지 않는다. perturbation이 즉시 영향을 주지 않을 수 있기 때문이다. Detection delay는 `t_detect - t_effect`로 계산하며, predictive alert는 음수가 될 수 있다.

## 5. Perturbation 및 event taxonomy

Failure cause와 recoverability는 서로 다른 축으로 저장한다.

### Failure cause

| Cause | Pilot perturbation | Onset landmark | 대표 option |
|---|---|---|---|
| `observation_visibility` | RGB blackout, target occlusion, stale frame을 N step 주입 | pre-grasp 또는 pre-place | `REOBSERVE_WAIT` |
| `execution_contact` | transport 중 gripper open, 짧은 action dropout, grasp slip | post-grasp/transport | `RETRY_CURRENT`, `STATE_RESET` |
| `world_state` | reachable 영역 안에서 target/receptacle displacement | pre-grasp 또는 post-subgoal | `REOBSERVE_WAIT`, `SUBGOAL_REWIND`, `TASK_REPLAN` |
| `plan_semantic` | drawer/microwave state를 되돌리거나 다음 subgoal의 전제조건 무효화 | subgoal 사이 | `SUBGOAL_REWIND`, `TASK_REPLAN` |
| `safety_system` | critical object를 unreachable 영역으로 이동하거나 absorbing forbidden-contact predicate 발생 | interaction 직전/직후 | `ABORT_STOP`, `HUMAN_ESCALATE` |

각 perturbation은 `S1/S2` 두 severity를 먼저 사용한다. arbitrary wall-clock percentage가 아니라 `pre_grasp`, `post_grasp_transport`, `pre_place`, `between_subgoals`의 state/event landmark에서 주입한다. task semantics에 맞지 않는 조합은 실행하지 않고 `not_applicable`로 기록한다.

### Operational recoverability

| Class | 판정 기준 | 허용되는 최소 recovery |
|---|---|---|
| `R0` | perturbation 없음 또는 progress invariant가 깨지지 않음 | `CONTINUE` |
| `R1_LOCAL` | 같은 instruction을 유지한 continue/retry가 local budget 안에 성공 | `CONTINUE`, `RETRY_CURRENT` |
| `R2_OPTION` | reobserve 또는 state/controller reset 중 하나가 있어야 성공 | `REOBSERVE_WAIT`, `STATE_RESET` |
| `R3_REPLAN` | task는 달성 가능하지만 현재 subgoal/plan의 전제조건이 무효 | `SUBGOAL_REWIND`, `TASK_REPLAN` |
| `R4_EXTERNAL` | 고정 autonomous option library와 budget으로 달성 불가하거나 absorbing safety event 발생 | `ABORT_STOP`, `HUMAN_ESCALATE` |

이 label은 failure의 본질적 속성이 아니라 **현재 option library와 budget에 조건부인 실험적 속성**이다. 최종 성공 결과 하나로 사후 라벨링하지 않는다. `t_effect`의 cloned simulator state에서 각 option을 같은 seed set으로 실행하고, 성공 가능한 가장 약한 option family로 oracle class와 acceptable-option set을 만든다. injection recipe의 예상 class와 oracle sweep 결과가 다르면 둘 다 저장하고 sweep 결과를 평가 label로 사용한다.

### Recovery option library

| Option | 고정 의미 |
|---|---|
| `CONTINUE` | base policy와 hidden/cache state를 유지 |
| `ABORT_STOP` | 현재 task를 안전 정지하고 terminal failure로 종료; 도움이나 simulator reset을 성공으로 세지 않음 |
| `RETRY_CURRENT` | environment는 reset하지 않고 policy memory만 reset한 뒤 현재 instruction 재실행 |
| `REOBSERVE_WAIT` | zero/safe hold 후 fresh observation을 받고 현재 instruction 유지 |
| `STATE_RESET` | 충돌 없는 사전 등록 safe pose로 retreat하고 controller/policy memory를 reset한 뒤 현재 subgoal 재시작 |
| `SUBGOAL_REWIND` | environment physical state는 유지하고 policy/task memory와 subgoal index를 마지막 검증 checkpoint로 되돌린 뒤 suffix를 재실행 |
| `TASK_REPLAN` | 관측 가능한 state estimate에서 미완료 goal의 새 skill/subgoal 순서를 생성; privileged predicate version은 별도 oracle baseline |
| `HUMAN_ESCALATE` | safe stop 후 제한된 human correction/help를 요청; simulator에서는 사전 등록한 oracle response contract를 쓰며 native success와 분리 |

Option implementation은 모든 selector에서 공유한다. 제안 method만 더 강한 rewind/replan/help interface를 쓰는 confound를 허용하지 않는다. `STATE_RESET`은 기존 문서의 `RETREAT_RESET`, `TASK_REPLAN`은 `REPLAN`, `HUMAN_ESCALATE`와 `ABORT_STOP`의 합산 보고는 `ABORT_HELP`에 대응하지만 `rp2.event.v2`부터는 semantics를 분리한다.

`SUBGOAL_REWIND`가 simulator snapshot으로 물리 상태까지 되돌아가면 privileged oracle이다. non-privileged branch는 이미 달성한 predicate를 유지한 채 skill sequence만 rewind하거나 safe reset을 실행한다. 두 버전을 같은 baseline 이름으로 섞지 않는다.

#### Staged option library와 구현 가능성 경계

OpenVLA는 native subgoal index나 symbolic plan을 직접 노출하지 않으므로 모든 option을 처음부터 C1에 넣으면 `SUBGOAL_REWIND/TASK_REPLAN` adapter 자체가 프로젝트의 대부분을 차지할 수 있다. 이를 피하기 위해 option library를 단계화한다.

| Stage | Option set | 구현 계약 | C1 사용 |
|---|---|---|---|
| `O_core` | `CONTINUE`, `RETRY_CURRENT`, `REOBSERVE_WAIT`, `STATE_RESET`, `ABORT_STOP` | frozen VLA와 robosuite state/controller interface만으로 구현 | Phase 0/1의 필수 최소 library |
| `O_graph` | `SUBGOAL_REWIND`, `TASK_REPLAN` | observation-derived progress와 사전 등록한 non-privileged task graph가 필요 | adapter acceptance test 통과 시에만 C1에 추가 |
| `O_assist` | `HUMAN_ESCALATE` | terminal query와 고정 response/cost contract | autonomous BRCR에서 제외; assisted coverage만 평가 |
| `O_oracle` | simulator-state rewind, BDDL-predicate replan | evaluator-only privileged state | O3/diagnostic 전용 |

`O_core`만으로 Agentic RL의 `Execute/Retry/Repair/Reset`과 실질적으로 같은 interface가 되면 novelty는 same-onset branch supervision·budget crossing·regret evidence에서만 판단한다. `O_graph`를 구현하지 못했다는 이유로 P1만 privileged replan을 호출하지 않는다. 반대로 `O_core`에서 option crossing이 없으면 option 수를 늘려 억지로 crossing을 만드는 대신 arbitration claim을 기각한다.

## 6. Recovery budget

가중합 하나가 아니라 다음 budget vector를 모든 방법에 동일하게 적용한다.

| Budget | Pilot 값 | 규칙 |
|---|---:|---|
| native episode horizon | 600 step | recovery를 위해 추가 horizon을 주지 않음 |
| recovery execution | 120 step | `recovery_started`부터 `t_recovered` 또는 failure까지 누적 |
| option calls | 2 | retry를 반복해 horizon을 우회하지 못하게 함 |
| state resets | 1 | safe retreat/controller reset 반복 제한 |
| subgoal rewinds | 0 primary; 1 extension | `O_graph`가 비활성이면 0, extension에서 progress rollback 반복 제한 |
| task replans | 0 primary; 1 extension | `O_graph`가 비활성이면 0, extension에서 expensive planning intervention 제한 |
| irreversible event | 0 | 한 번 발생하면 safety gate 실패 |
| human escalation | 0 primary; 1 assisted call | native autonomous success가 아니며 correct escalation·assisted completion을 분리 |

Pilot 이후 `recovery execution ∈ {60, 120, 180}` sensitivity를 수행한다. budget을 다 쓴 뒤 recovery mode를 임의로 종료해 base action으로 위장하지 못하도록, `t_recovered`는 oracle task-valid predicate로만 닫는다.

Phase 0 budget ID는 다음처럼 고정한다. `O_graph/O_assist`가 비활성인 실험에서는 해당 quota를 0으로 기록하고 budget vector 차원을 삭제하지 않는다.

| ID | recovery steps | option calls | reset | rewind | replan | escalation |
|---|---:|---:|---:|---:|---:|---:|
| `B_low` | 60 | 1 | 0 | 0 | 0 | 0 |
| `B_mid` | 120 | 2 | 1 | 0 | 0 | 0 |
| `B_high` | 180 | 3 | 1 | 0 | 0 | 0 |
| `B_high_graph` | 180 | 3 | 1 | 1 | 1 | 0 |

`B_high_graph`는 `O_graph` acceptance를 통과한 extension에서만 사용한다. `B_low`에서 `STATE_RESET`이 infeasible인 것은 의도된 budget constraint다. 그러나 BCP를 단순 feasibility 변화만으로 주장하지 않도록, 공통 feasible option subset 안에서의 ranking transition도 별도로 보고한다.

## 7. Baseline과 oracle upper bound

### 실행 baseline

| ID | System | Detector | Recovery decision | 목적 |
|---|---|---|---|---|
| B0 | Clean native policy | 없음 | `CONTINUE` | clean competence sanity check |
| B1 | Perturbed native policy | 없음 | `CONTINUE` | perturbation damage negative control |
| B2 | SAFE + abort | 동일 SAFE | alert 시 `ABORT_STOP` | detection-only safety baseline |
| B3 | SAFE + blind retry | 동일 SAFE | 모든 alert에 `RETRY_CURRENT` | 가장 단순한 recovery baseline |
| B4 | SAFE + privileged replan | 동일 SAFE | 모든 alert에 simulator predicate 기반 `TASK_REPLAN` | planning interface의 강한 privileged baseline |
| B5 | FLARE-style binary dispatcher (`B5^learned`; 재현 불가 시 `B5^oracle`) | learned 또는 oracle-labeled | local/ID는 `RETRY_CURRENT`, state-breaking/OOD는 `STATE_RESET` | 이미 발표된 binary retry/reset counter-evidence |
| B6 | FAIL-Detect + abort | FAIL-Detect | alert 시 `ABORT_STOP` | failure-data-free detector family 비교 |
| B7 | SAFE + scalar-risk selector | 동일 SAFE | scalar task/risk score와 budget mask만으로 option 선택 | option-conditioned value가 불필요하다는 naive method |
| B8 | TD-calibrated scalar selector | TD calibration + SAFE score | calibrated scalar task value로 option 선택 | calibration만으로 arbitration이 대체되는지 확인 |
| B9 | SAFE + uniform feasible selector | 동일 SAFE | static budget/safety mask를 만족하는 option에서 uniform random 선택 | option choice가 우연히 좋아진 것인지 확인하는 null selector |
| B10 | SAFE + best-fixed-per-budget | 동일 SAFE | calibration split에서 budget별 단일 option을 고정 | context-conditioned selection이 필요한지 확인하는 핵심 baseline |
| B11 | SAFE + type-only heuristic | 동일 SAFE | cause/recoverability label을 사전 고정 option map으로 변환 | option-value learning 없이 diagnosis routing만으로 충분한지 확인 |
| P1 | SAFE + same-onset branch-supervised option-value selector | 동일 SAFE | 공용 option library에서 calibrated value·risk·cost로 constrained 선택 | 제안 방법 |

B4는 true simulator predicate를 보므로 일반 learned baseline으로 보고하지 않고 `PRIVILEGED`로 표시한다. PDDLStream 전체 구현은 continuous collision/kinematic feasibility가 실제 병목으로 확인될 때 CALVIN 또는 phase-2 extension에서 추가한다. 최소 LIBERO pilot에서는 task-specific predicate/skill graph replan으로 범위를 제한한다.

B5의 저자 코드를 동일 조건에서 재현하지 못하면 임의 구현을 FLARE 결과라고 부르지 않는다. 대신 oracle ID/OOD label을 쓰는 `privileged binary Retry/Reset`으로 이름을 바꾸어 binary taxonomy의 upper bound로 보고한다.

B9의 feasibility mask는 모든 system에 공개된 option precondition과 remaining budget만 사용한다. simulator goal predicate, oracle recoverability, option-sweep `q_o/r_o`는 mask에 넣지 않아 random null selector가 privileged baseline이 되지 않게 한다.

B10은 fit/calibration outcome에서 각 budget별 best single option을 정한 뒤 test에서는 context와 detector score에 관계없이 고정한다. O3와 B10의 gap이 learned arbitration의 최대 실용 가치를 직접 보여주므로, B10 없이 P1의 novelty를 주장하지 않는다. B11의 type label이 oracle이면 `B11^oracle`로 분리하고 primary non-privileged winner에서 제외한다.

### Frontier method-family baseline

아래 방법은 source-verified direct counter-evidence다. 저자 코드·입력·option contract가 현재 benchmark에 맞으면 동일 base policy와 budget으로 이식하고, 그렇지 않으면 reported number를 P1과 직접 비교하지 않고 option-family audit만 남긴다.

| ID | 근거 | 맞춰야 할 interface | primary 후보 조건 |
|---|---|---|---|
| X0 | RT-H | 같은 image/history, language-motion intervention, 동일 human-query/action budget | language correction을 공용 option descriptor와 cost로 매핑 가능 |
| X1 | ViFailback | 같은 image/history와 diagnosis→correction option, 동일 horizon | correction을 공용 option library로 매핑 가능 |
| X2 | AgentChord | 같은 task graph·recovery branch·latency budget | privileged task predicate 없이 branch 실행 가능 |
| X3 | When to Act, Ask, or Learn | 같은 act/ask/intervene 정보와 human-query budget | ask response contract와 intervention cost가 P1과 동일 |
| X4 | ActFovea | 같은 observation perturbation, candidate-observation set, verification·safe-failure budget | code와 action-chunk verifier를 공용 base policy에 연결 가능 |
| X5 | Agentic RL execution modes | 같은 history, execution-mode library와 option-call/horizon budget | mode semantics와 training data가 공개되어 option library를 맞출 수 있음 |
| X6 | ProbeAct | 같은 base policy, kinematic/probe input과 CBF/safe-intervention cost | hidden-state probe와 safety filter를 동일 LIBERO setting에 재현 가능 |

SPR, FAR, CoRe, VLCP, Robo-Dopamine 2.0, Dream2Fix, RedFlow는 별도 `PREPRINT-ONLY` collision set으로 기록한다. 재현 가능한 코드와 명확한 policy-visible input이 확인되기 전에는 confirmatory primary baseline으로 승격하지 않는다. 다만 rewind·retry adaptation·imagined realignment·code replan·history reward·counterfactual synthesis·action correction이 이미 존재한다는 사실 때문에 해당 요소 자체를 contribution으로 주장할 수 없다.

ActFovea full-text audit에서 단순하지만 강한 disturbance-specific control이 확인되었으므로 다음 mechanism control을 관련 subgroup에서 반드시 실행한다. 이들은 전체 failure family의 primary winner 후보가 아니라 “복잡한 selector 없이 해당 perturbation을 해결할 수 있는가”를 확인한다.

| ID | Mechanism control | 적용 subgroup | 반증하는 설명 |
|---|---|---|---|
| M0 | fixed short-horizon policy re-query | action drift, finite observation delay | 더 자주 closed loop로 돌리는 것만으로 충분한가 |
| M1 | bounded action clip + exponential smoothing | action drift, execution/contact | 단순 control regularization으로 충분한가 |
| M2 | timestamp/repeated-frame hold | stale frame, delayed/frozen observation | freshness rule만으로 reobserve/abort가 충분한가 |

M0–M2도 P1과 같은 base checkpoint, action limit, native horizon을 사용한다. 특정 subgroup에서 M0–M2가 P1과 동률이면 그 failure family에서는 learned arbitration을 주장하지 않는다.

### 비교군 계층과 공정성 계약

모든 결과를 한 순위표로 섞지 않는다. 다음 네 그룹을 별도 표와 별도 해석으로 유지한다.

| Group | 포함 system | 질문 | claim에 사용하는가 |
|---|---|---|---|
| `G0 competence/control` | B0, B1 | perturbation이 base policy를 얼마나 망가뜨리는가 | sanity check만 |
| `G1 detector/safety` | B2, B6 | alert 품질·calibration만으로 어느 정도 안전한가 | detector 비교 |
| `G2 recovery policy` | B3–B5, B7–B11, M0–M2, 재현 가능한 X0–X6 | blind/binary/privileged/scalar/random/fixed/type-only/direct recovery의 ceiling은 무엇인가 | strongest non-privileged baseline 후보와 subgroup mechanism control |
| `G3 proposed/decomposition` | P1, A1–A9, O1–O3 | same-onset multi-option supervision·budget·belief·option-value 각 요소가 필요한가 | method attribution과 claim ladder |

Primary comparison은 Phase 0/1의 development split에서 미리 정한 strongest non-privileged system `B* ∈ {B3, B5^learned, B7, B8, B10, B11^learned, X0–X6 중 matched 구현}`와 P1의 paired comparison이다. `B9`는 null selector라서 primary winner selection에는 넣지 않는다. `B*`를 confirmatory-test 결과를 본 뒤 고르지 않는다. B4, `B11^oracle`, O1–O3는 privileged diagnostic이므로 일반적인 경쟁 결과나 state-of-the-art 순위로 보고하지 않는다. 저자 구현을 재현하지 못한 X baseline과 `B5^oracle`도 primary 후보에서 제외한다.

공정성 규칙은 다음과 같이 고정한다.

1. B2/B3/B4/B7/B9–B11/P1은 같은 SAFE feature, alert threshold, base checkpoint를 공유한다. B6과 B8은 detector/calibration family를 바꾸는 별도 sensitivity다.
2. 모든 recovery option은 하나의 공용 implementation library에서 가져오며, P1만 더 강한 reset/rewind/replan/help interface를 호출할 수 없다.
3. native horizon, recovery step, option call, reset/rewind/replan, irreversible-event, human-query budget은 모든 system에 동일하다. `ABORT_STOP`과 assisted completion은 autonomous success로 처리하지 않는다.
4. threshold·λ·risk margin·heuristic map은 fit/calibration split에서만 정한다. test에서 task별로 재튜닝하거나 실패 episode를 골라 제거하지 않는다.
5. 추가 head 계산량과 option execution latency는 success와 독립된 resource metric으로 보고한다. P1이 더 느린데도 동일한 control deadline을 어기면 BRCR 개선만으로 우월성을 주장하지 않는다.

### 비교 질문별 사전 고정 pair

| 비교 질문 | 최소 pair | 해석 |
|---|---|---|
| perturbation damage | B0 vs B1 | failure injection 자체의 base-policy 손상 |
| detector-only safety | B1 vs B2/B6 | alert family가 abort safety를 얼마나 개선하는가 |
| blind recovery | B2 vs B3 | abort 대신 retry가 주는 completion/safety trade-off |
| fixed vs context-conditioned | B10 vs O3/P1 | onset context에 따른 option choice가 필요한가 |
| binary vs multi-option | B5^learned vs P1 | Retry/Reset보다 abstraction-level option arbitration이 필요한가 |
| scalar/type-only vs option value | B7/B8/B11 vs P1 | option-conditioned outcome modeling의 필요성 |
| option choice null | B9 vs P1 | 선택 policy가 random option mix보다 나은가 |
| direct frontier recovery | matched X0–X6 vs P1 | language correction/task graph/act-ask/verified observation/execution-mode/safety-net보다 same-onset option value가 필요한가 |
| detector bottleneck | O1 vs P1 | oracle onset과 learned detector의 차이 |
| selector ceiling | P1 vs O2/O3 | 현재 detector·option library에서 남은 head/selector gap |

이 pair 외의 결과는 exploratory로 표시한다. 서로 다른 base checkpoint, 서로 다른 option library, 서로 다른 horizon을 사용한 비교는 성능 순위표에 넣지 않고 별도 sensitivity로 분리한다.

### 제안 method를 약화한 필수 ablation

| ID | 제거/변경 요소 | 검증하는 주장 |
|---|---|---|
| A1 | context는 유지하고 remaining budget을 고정 | budget dimension의 필요성 |
| A2 | scalar alert와 budget만 사용하고 history·auxiliary cause/recoverability 제거 | richer context/belief의 필요성 |
| A3 | type→option 고정 heuristic map, option-value head 제거 | learned action-conditioned value의 필요성 |
| A4 | selector는 유지하되 q/r calibration 제거 | calibration과 selection의 분리 효과 |
| A5 | `q_o/r_o/k_o` 대신 scalar task/risk value 사용 | option별 outcome modeling의 필요성 |
| A6 | `REOBSERVE_WAIT`, `STATE_RESET`, `SUBGOAL_REWIND`를 제거한 reduced library | option expressivity와 method novelty의 구분 |
| A7 | 현재 observation과 scalar alert만 사용하고 temporal history/belief를 제거 | POMDP belief와 failure onset history의 필요성 |
| A8 | vector budget을 정규화된 scalar remaining budget으로 압축 | multidimensional budget의 필요성 |
| A9 | 선택된/chosen correction outcome만 사용하고 alternative option target을 mask | same-onset alternative-option supervision의 필요성 |

A1–A9는 같은 fit/calibration/test split, head budget, training seed, option library에서 실행한다. 기본은 one-factor-at-a-time(OAT)이고 P1이 primary gate를 통과한 뒤에만 `A1×A8`(context 대 scalar budget)과 `A3×A5`(heuristic routing 대 option-conditioned value) interaction을 추가한다. ablation 하나가 P1과 같은 성능을 내면 해당 component를 contribution으로 주장하지 않는다. 특히 A9가 P1과 같으면 cloned alternative outcome을 사용하는 핵심 주장을 철회하고 일반 option-value selector로 축소한다.

### 오류 분해와 upper bound

| ID | Detector | Selector | 해석 |
|---|---|---|---|
| O1 | oracle `t_effect` | learned option-value selector | selector의 순수 오류와 detector delay 분리 |
| O2 | learned SAFE | oracle acceptable-option set | detector 병목과 option 선택 병목 분리 |
| O3 | oracle `t_effect` | cloned-state option sweep | 현재 option library와 budget의 empirical upper bound |

O3는 `t_effect` state를 clone하고 각 option을 같은 rollout seed로 실행한 뒤, 다음 lexicographic rule로 고른다.

1. irreversible event가 없는 option,
2. native goal을 budget 안에 완료하는 option,
3. 추가 step과 option cost가 가장 작은 option.

O3도 skill library 밖의 행동은 만들지 못하므로 task의 절대 oracle이 아니라 **현재 recovery interface의 upper bound**다.

## 8. Primary 및 secondary metric

### Arbitration novelty prerequisite

BRCR 비교 전에 same-onset option table이 learned selector를 필요로 하는지 검사한다. cloned onset `s`, budget `B`, option `o`의 seed-averaged utility와 oracle option은 다음과 같이 고정한다.

```text
U(s,o,B) = goal_success - λrisk · irreversible_event - λcostᵀ · normalized_cost
o*(s,B) = argmax_o U(s,o,B), subject to feasibility and risk gate
```

- **Option Separability:** 같은 `(s,B)`에서 option outcome의 confidence interval이 모두 겹치지 않고 적어도 한 option pair의 success/risk/cost가 구분되는 onset 비율.
- **Context Crossing Prevalence (CCP):** 같은 detector-score bin과 비슷한 detection time에 속하지만 `o*(s,B)`가 서로 다른 onset pair의 비율.
- **Budget Crossing Prevalence (BCP):** 같은 onset에서 `B_low`, `B_mid`, `B_high` 중 budget이 바뀔 때 `o*(s,B)`가 바뀌는 비율.
- **Best-Fixed Regret (BFR):** calibration split에서 정한 budget별 best-fixed option `o_fixed(B)`와 O3의 평균 utility 차이 `E[U(s,o*,B)-U(s,o_fixed,B)]`.
- **Selector Regret:** test onset에서 O3와 learned selector의 utility 차이. option utility와 BRCR/IFR를 함께 보고해 arbitrary λ에만 의존하지 않는다.

CCP/BCP는 description이고 단독 novelty 근거가 아니다. 최소 진행 gate는 (1) option-sweep stability 통과, (2) O3가 B10 best-fixed보다 BRCR 또는 BFR에서 사전 등록한 practical margin을 넘음, (3) crossing이 한 task/perturbation artifact에만 국한되지 않음이다. 이 gate를 통과하지 못하면 P1 head를 학습하지 않는다.

### Primary outcome과 safety gate

**Budgeted Recovery Completion Rate (BRCR)**

R1–R3 perturbed episode 중 native goal을 600 step 안에 만족하고, 전체 vector budget을 넘지 않으며, irreversible event가 없는 비율이다.

```text
BRCR = mean[goal_success ∧ within_budget ∧ no_irreversible_event | R1–R3]
```

R4는 완료가 바람직한 outcome이 아니므로 BRCR 분모에서 제외하고 별도로 보고한다.

**Safety gate — Irreversible Failure Rate (IFR)**

전체 perturbed episode 중 absorbing safety violation 또는 recovery 불가능 상태로 전이한 비율이다. BRCR이 높아도 IFR non-degradation을 만족하지 못하면 H1을 지지하지 않는다.

### Secondary metric

- clean task success와 false-intervention rate
- R4 correct abort/escalation rate, assisted completion, unnecessary abort/escalation rate
- **Autonomous coverage**와 selective IFR/BRCR risk–coverage curve: `ABORT_STOP/HUMAN_ESCALATE`로 어려운 episode를 버려 성능을 부풀리는지 확인
- **Normalized Recovery Rate (NRR):** `(S_recovered - S_disturbed) / (S_clean - S_disturbed)`; denominator가 0 이하이거나 지나치게 작으면 보고하지 않고 세 성공률을 그대로 제시
- failure detection AUROC/AUPRC, `t_detect - t_effect`, missed-alert rate
- cause macro-F1, recoverability macro-F1, acceptable-option accuracy
- Option Separability, CCP, BCP, BFR와 budget별 option-ranking transition matrix
- intervention-conditioned recovery success
- recovery step, option call, policy re-query, reset/rewind/replan/query count, physically restored object 수, post-handoff step, total execution cost
- intervention 전후 유지된 task/subgoal progress
- task, cause, severity, onset landmark별 worst-group BRCR/IFR
- timeout rate와 post-recovery re-failure rate

모든 system은 동일 `init_state_id × perturbation × seed`에서 paired 비교한다. 95% stratified bootstrap confidence interval을 task와 failure family 단위로 보고하고, 평균만으로 subgroup failure를 숨기지 않는다.

### Metric 계산·집계·통계 규칙

| 관점 | 보고 metric | 계산 규칙 | 필수 비교 |
|---|---|---|---|
| 최종 recovery | BRCR, intervention-conditioned recovery success | episode 단위 binary outcome; R1–R3와 R4를 분리 | P1 vs `B*`, O3 |
| safety | IFR, safety violation precision, correct/incorrect abort | irreversible event가 한 번이라도 있으면 episode 실패 | P1의 one-sided non-inferiority |
| detector | event-level AUROC/AUPRC, alert precision/recall, `t_detect−t_effect`, missed-alert rate | episode당 첫 유효 alert 하나를 primary로, 반복 alert는 auxiliary count로 | B2/B6/B8, O1 |
| diagnosis/value | auxiliary cause·R macro-F1, per-option Brier/ECE, acceptable-option top-1/recall | class와 option별 macro average; `not_applicable` mask | A2/A5/A9, O2 |
| arbitration precondition | Option Separability, CCP, BCP, BFR | cloned onset·matched seed·budget별 O3와 B10을 비교 | B10, O3; P1 학습 전 gate |
| decision quality | O3 대비 normalized option regret, constraint violation, option agreement | `U(o)=q_o−λᵀk_o`와 risk gate를 사용해 clone-state별 계산 | P1, B7–B11, A3/A5/A9 |
| cost/latency | recovery steps, option calls, replans, added action cost, p50/p95 selector latency | native action과 recovery action을 분리하고 wall-clock도 함께 저장 | 모든 learned system |
| selective behavior | autonomous coverage, selective BRCR/IFR, risk–coverage curve, correct abort | abstain episode를 성공에서 제외하고 coverage별 위험을 함께 표시 | B2, P1, X3, ActFovea-style safe fail |
| recovered loss | NRR와 clean/disturbed/recovered success triple | `S_clean > S_disturbed`인 cell에서만 계산하고 macro-average 전에 cell별 denominator 공개 | P1, X4, M0–M2 |
| robustness | task/cause/severity/onset별 BRCR·IFR, worst-group(10th percentile) | subgroup 최소 cell 수를 사전 고정; cell이 작으면 CI만 보고 | holdout task/family, CALVIN |

`BRCR`만 올리고 detector가 늦어지거나 intervention cost가 커지는 trade-off를 숨기지 않는다. 특히 scalar-risk selector가 P1과 같은 BRCR을 내더라도 option regret·IFR·latency가 다르면 그 차이를 별도 해석한다. `O3`의 utility는 평가용 upper bound이며, P1의 training target으로 test episode에 재사용하지 않는다.

#### 추론 단위와 confidence interval

- 동일 `episode_id`의 system 결과를 한 paired block으로 묶고, bootstrap cluster는 `task_id × init_state_id × perturbation_id × severity`로 잡는다. rollout seed는 block 안의 반복으로 취급해 독립 표본처럼 세지 않는다.
- primary effect는 `ΔBRCR = BRCR(P1) − BRCR(B*)`, safety effect는 `ΔIFR = IFR(P1) − IFR(B*)`로 보고한다. 각 값에 95% paired cluster-bootstrap CI와 absolute percentage point를 함께 쓴다.
- 초기 practical margin은 `ΔBRCR ≥ +5 pp`, `ΔIFR ≤ +1 pp`(one-sided non-inferiority), clean success 하락 `≤3 pp`다. 이는 문헌의 보편 상수가 아니라 RP-2의 사전 등록 decision margin이다.
- H1/H2 외 secondary metric의 multiple comparison은 Holm correction을 적용한다. CCP/BCP는 paired cluster-bootstrap CI와 raw transition count를 함께 보고하며 p-value만으로 claim하지 않는다.
- Phase 0/1의 variance와 cluster correlation은 Phase 2의 최소 episode 수를 산정하는 데만 사용한다. confirmatory-test 결과를 본 뒤 trial 수·split·margin을 바꾸지 않는다.

#### Protocol validity metric

방법 성능 전에 event protocol 자체가 믿을 만한지 확인한다.

- **clone/restore determinism:** 같은 `state_hash × seed`를 복원했을 때 observation, task predicate, base action이 tolerance 안에서 재현되는 비율.
- **event completeness:** `episode_start → perturbation_injected → failure_manifested → alert/intervention → recovery/terminal` 필수 순서가 누락 없이 기록된 episode 비율.
- **onset consistency:** 동일 recipe의 `t_effect`가 state landmark와 oracle progress invariant에서 일관되게 검출되는 비율. `t_inject`만 기록된 episode는 primary delay metric에서 제외한다.
- **option-sweep stability:** 동일 cloned state의 repeated sweep에서 acceptable-option set과 lexicographic O3 선택이 일치하는 비율.
- **branch equivalence before action:** alternative option을 실행하기 직전 observation, task predicate, policy/controller state, budget hash가 동일한 비율. 이 값이 낮으면 same-onset multi-option claim을 할 수 없다.
- **adapter agreement:** LIBERO/CALVIN evaluator와 RP-2 adapter가 clean success, timeout, terminal event를 같은 episode ID에 대해 일치시키는 비율.

이 validity check를 통과하지 못한 episode를 조용히 제거하지 않는다. protocol-invalid count와 제외 사유를 별도 flow table로 보고한다.

## 9. 실험 행렬

### 고정 factor와 실행 순서

Primary factorial은 `cause × valid onset landmark × severity × recovery budget × system`이다. 모든 조합을 억지로 만들지 않고, task semantics상 유효한 cell만 `rp2_factor_manifest_v1.json`에 기록한다. 각 cell에는 perturbation recipe, onset predicate, severity parameter, recovery budget vector, random seed list가 들어간다.

| Factor | Primary 값 | Sensitivity/holdout | 고정 규칙 |
|---|---|---|---|
| cause | observation, execution/contact, world-state, plan-semantic | safety-system/R4, unseen family | family별 recipe 수를 동일하게 맞추려 하지 말고 cell과 sample 수를 공개 |
| onset | pre-grasp, post-grasp/transport, pre-place, between-subgoals 중 valid cell | task-specific unseen landmark 1개 이상 | `t_inject`가 아니라 `t_effect`를 기준으로 delay 계산 |
| severity | S1, S2 | S3는 Phase 2 sensitivity | S1/S2 parameter는 test 전에 고정 |
| recovery budget | `(120 steps, 2 calls, 1 reset, 1 rewind, 1 replan, 1 escalation)` | recovery steps 60/180, calls 1/3 | vector budget을 selector input과 evaluator에 동일하게 사용 |
| rollout seed | fit 0–1, calibration 2, test 3–5 | Phase 1 shortlist 3-seed repeat | same seed를 모든 system에 paired로 적용 |

각 learned system은 fit split에서 독립적으로 학습하고 calibration split에서만 threshold를 고정한다. Phase 0에서 crossing/BFR evidence가 없으면 P1/A1–A9를 만들거나 튜닝하지 않고 scalar/binary protocol 또는 I-12 infrastructure로 revise한다. crossing evidence가 있더라도 모든 ablation을 test 결과에 맞춰 선택하지 않는다.

### Phase 0 — Wrapper 및 oracle audit

아래 네 `libero_10` task를 사용한다.

1. `KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it`
2. `KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it`
3. `LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket`
4. `STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy`

articulated receptacle, multi-object sequence, precise placement를 함께 포함한다. 각 task에서 clean rollout과 state landmark를 먼저 검증하고, perturbation 직후 clone/restore가 deterministic tolerance 안에서 재현되는지 확인한다.

Phase 0의 첫 산출물은 학습된 selector가 아니라 **20–50개 valid onset의 fixed-option sweep table**이다. 각 onset에 S1 perturbation 하나와 `B_low/B_mid/B_high` budget을 적용하고 모든 applicable `O_core` option을 동일 seed에서 실행한다. 다음 순서로 gate를 판단한다.

1. restore determinism과 branch equivalence를 통과하지 못하면 I-12 wrapper부터 수정한다.
2. option outcome이 구분되지 않거나 O3가 B10 best-fixed보다 practical margin만큼 낫지 않으면 recovery library/arbitration claim을 기각한다.
3. context crossing은 있으나 budget crossing이 없으면 vector-budget claim을 제거한다.
4. 두 crossing이 관찰된 경우에만 Phase 1의 value head와 selector를 학습한다.

### Phase 1 — 최소 decision experiment

| 축 | 값 |
|---|---|
| tasks | 위 4개 LIBERO-Long task |
| perturbation | observation, execution/contact, world-state, plan-semantic |
| severity | S1, S2 |
| fixed initial states | task당 10개 |
| split | task-level `2 fit / 1 calibration / 1 holdout`; exact manifest를 먼저 고정 |
| paired scenario | `4 × 4 × 2 × 10 = 320` unique cells / system; shortlist system은 3 paired seeds |
| systems | B1–B11, M0–M2, matched X0–X6, A1–A9, P1, O1–O3 중 Phase 0 뒤 사전 등록한 shortlist |
| clean audit | 4 task × 10 init state / 실행 system |

R4 perturbation은 각 task/init state에 무조건 곱하지 않고 별도 diagnostic set으로 둔다. standard LIBERO의 R4 결과는 simulator-specific correct-abort 성능으로만 해석한다.

### Phase 2 — Confirmatory LIBERO

- `libero_10` 전체 10 task
- task당 공식 fixed initial state 20개
- four perturbation families × two severity
- task-level `6 fit / 2 calibration / 2 confirmatory-test` split을 유지하고 test task는 고정한다.
- pilot에서 사전 등록한 strongest non-privileged baseline `B*`, P1, scalar B7/B8, binary B5, null B9, best-fixed B10, type-only B11, 재현 가능한 direct frontier baseline, O1/O3만 실행한다.
- 예상 paired scenario: `10 × 20 × 4 × 2 = 1,600` unique cells / system; confirmatory systems는 test seed 3개를 사용한다.
- Phase 2에는 primary BRCR/IFR, option regret, latency, worst-group table을 모두 제출한다. pilot에서 바꾼 recipe는 새 protocol version으로 분리한다.

Phase 1 결과를 본 뒤 perturbation 정의나 threshold를 바꾸면 Phase 2에는 새 version을 부여하고 pilot과 confirmatory 결과를 섞지 않는다.

### Phase 3 — CALVIN transfer

- 고정된 100개 five-subtask sequence로 먼저 검증하고 표준 1,000 sequence는 최종 확인에만 사용한다.
- sequence의 2번째 또는 3번째 subtask에 perturbation을 삽입한다.
- 첫 subtask failure에서 반환하지 않고 남은 sequence와 post-recovery progress를 계속 기록하도록 evaluator를 fork한다.
- native five-task success count와 공통 BRCR/IFR/event metric을 함께 보고한다.
- LIBERO에서 학습한 detector/selector를 그대로 적용한 zero-shot 결과와 CALVIN calibration-only 결과를 분리한다.
- 100-sequence dev transfer에서는 recipe/threshold를 바꾸지 않고 event adapter와 logging만 검증한다. 1,000-sequence confirmatory run에서는 LIBERO test에서 고정한 selector를 그대로 사용한다.
- sequence-level metric은 native five-subtask success, first-failure recovery success, remaining-subtask completion, sequence IFR를 함께 보고한다. sequence 안의 subtask를 독립 episode로 부풀려 집계하지 않는다.

### Phase 4 — Optional real-robot transfer (`C3` gate)

Phase 1–3이 통과되어도 실물 안전성은 자동으로 따라오지 않는다. C3를 주장하려면 single-arm hardware와 고정 low-level controller에서 최소한 다음을 추가한다.

- 동일한 `rp2.event.v2` option interface를 ROS/robot wrapper에 연결하고, 실제 safe pose·emergency stop·operator escalation을 사전 등록한다.
- 2개 이상의 contact/placement task와 observation visibility, grasp/execution, world-state perturbation을 사용한다. 손상 가능성이 있는 강제 충돌은 만들지 않고, slip·occlusion·bounded action dropout처럼 recoverable perturbation부터 시작한다.
- simulator에서 학습한 selector의 zero-shot 결과와 hardware calibration-only 결과를 분리한다. real rollout을 추가해 head를 다시 학습한 결과는 새로운 `D4-physical` protocol version으로 보고한다.
- BRCR/IFR 외에 physical contact peak/impulse, joint-limit violation, emergency-stop rate, operator intervention, wall-clock recovery latency를 기록한다. real-world trial이 없으면 이 metric은 `NOT_RUN`으로 명시한다.

실로봇 phase는 RP-2의 최소 C1 목표에 필요하지 않다. 하지만 실제 로봇 연구로 확장할 때 low-level control 성능을 arbitration 성능으로 잘못 귀속하지 않도록 hardware, controller, option library를 고정해야 한다.

## 10. Threats to validity와 통제

| 위협 유형 | 구체적 threat | 결과를 왜곡하는 방식 | 문서상 통제와 남는 한계 |
|---|---|---|---|
| novelty | Agentic RL이 이미 history-conditioned four-mode recovery manager를 PPO로 학습 | high-level selector 자체를 새 방법으로 오인 | same-onset full-option supervision, vector-budget crossing, best-fixed regret가 모두 있어야 C1. X5 matched comparison 실패 시 evaluation extension으로 축소 |
| novelty | ActFovea·ProbeAct·CoRe가 verification, phase-aware intervention, rewind/rejoin을 이미 다룸 | option component 하나를 contribution으로 오인 | 각 방법을 X4/X6/option-family baseline으로 분리하고 component novelty를 주장하지 않음 |
| construct | simulator에서 정의한 `irreversible_event`가 실제 physical risk를 대표하지 않음 | IFR을 real-world safety처럼 해석 | LIBERO IFR은 simulator operational safety로만 표현; C3는 별도 hardware metric 없으면 `NOT_RUN` |
| construct | R1–R4가 option sweep outcome으로 정의되어 method 성능과 label이 순환 | easy/hard subgroup을 결과에 맞춰 구성 | recoverability는 evaluator stratification에만 쓰고 P1 inference 입력 금지; cause별 raw outcome도 함께 보고 |
| internal | option마다 구현 품질이 달라 selector 이득이 강한 option 하나에서 발생 | arbitration gain과 option engineering gain 혼합 | 모든 방법이 versioned common library 공유; option별 standalone success/cost 표와 leave-one-option-out ablation |
| internal | learned detector가 다른 onset을 선택해 same-onset 비교가 깨짐 | detector와 selector effect 혼합 | O1 oracle-onset, fixed SAFE detector group, detector sensitivity를 별도 표로 분리 |
| internal | test option sweep outcome이 selector fitting·threshold에 유출 | regret와 calibration이 낙관적으로 변함 | test O3는 prediction freeze 뒤 evaluator-only 실행; artifact access log와 split hash 검사 |
| internal | repeated branch가 simulator RNG, controller cache, policy RNG를 완전히 복원하지 못함 | option 차이가 restore artifact가 됨 | environment·controller·policy/cache·RNG snapshot을 함께 복원하고 branch equivalence test 통과 episode만 primary에 포함 |
| reproducibility | MuJoCo/robosuite action replay가 machine·version에 따라 drift | 같은 state/seed가 다른 결과 생성 | 같은 pinned container/host에서 state restore를 primary로 사용. cross-machine action replay를 equivalence 근거로 쓰지 않음 |
| external | programmatic perturbation이 자연 발생 failure와 다름 | synthetic recipe에만 맞는 selector가 됨 | recipe holdout, unseen onset, CALVIN zero-shot; 가능하면 D4 physical bounded perturbation을 별도 수행 |
| external | 낮은 base-policy competence가 recovery보다 native failure를 지배 | supervisor의 실패 원인이 불분명 | clean competence gate를 통과한 task/init state만 Phase 0에 채택하고 제외 수를 공개 |
| statistical | branch rollout을 독립 episode로 세어 sample size를 부풀림 | CI가 과도하게 좁아짐 | onset/scenario를 paired cluster로 사용하고 seed·option branch는 cluster 내부 반복으로 처리 |
| statistical | 많은 baseline·ablation·subgroup 중 좋은 결과만 선택 | false-positive contribution | primary `B*`, metric, margin, shortlist를 confirmatory test 전에 manifest에 고정; secondary는 Holm correction |
| systems | P1 latency나 추가 policy query가 horizon 밖 자원을 사용 | success gain이 추가 compute/action budget에서 발생 | low-level step, VLA query, selector wall-clock, reset/replan/query를 vector cost로 기록하고 deadline-matched 비교 |

특히 [robosuite state API](https://robosuite.ai/docs/source/robosuite.utils.html)는 simulator state의 `get_state/set_state`를 제공하지만, 공식 demonstration 문서는 action playback이 machine을 넘으면 drift할 수 있음을 경고한다. 따라서 RP-2의 same-onset 근거는 action replay가 아니라 **같은 pinned runtime에서 직접 복원한 simulator state + controller state + policy/cache/RNG state**여야 한다.

## 11. Reject / revise 기준

아래 수치는 Phase 1 실행 전에 고정할 초기 decision rule이다. pilot variance가 지나치게 크면 효과 방향을 보고 threshold를 바꾸지 말고 trial 수 산정만 다시 한다.

| 결과 | 결정 |
|---|---|
| ActFovea·Agentic RL 또는 후속 공개본이 same-onset multi-option sweep, matched vector budget, best-fixed/type-only comparison과 option regret를 이미 함께 제공 | `NOVELTY COLLISION`: learned selector method claim을 중단하고 재현·cross-suite evaluation 또는 명시적으로 남은 한 축만 extension으로 재정의 |
| Phase 0에서 option outcome이 안정적으로 분리되지 않거나 O3가 B10 best-fixed보다 BRCR/BFR practical margin을 넘지 못함 | `REJECT arbitration claim`: context-conditioned option 선택의 실용 가치가 없음 |
| CCP는 존재하지만 BCP가 없고 scalar budget ablation A8과 차이가 없음 | `REVISE`: vector-budget claim을 제거하고 context-only arbitration으로 축소 |
| O3는 B10을 이기지만 O1 learned selector가 이기지 못함 | `REVISE selector`: detector가 아니라 context/value head 또는 training target 문제 |
| O1은 이기지만 P1이 이기지 못함 | `REVISE detector`: onset delay/calibration 병목 |
| P1이 사전 고정한 `B*`보다 BRCR 5 pp 이상 개선하고 paired 95% CI가 0을 제외하며 `ΔIFR ≤ +1 pp` one-sided non-inferiority 만족 | H1 `SUPPORTED` 후보; Phase 2 진행 |
| P1의 IFR upper CI가 `B* + 1 pp`를 초과 | safety gate 실패; BRCR가 높아도 `REVISED` 또는 `REJECTED` |
| clean success가 B0 대비 3 pp 초과 하락 | alert/selector가 과민함; clean non-degradation 실패 |
| binary B5 또는 type-only B11과 P1 차이가 없음 | same-onset option-value claim 축소; binary/heuristic routing으로 충분한 조건을 분석 |
| 이득이 특정 perturbation/task에만 존재 | 범용 claim을 버리고 해당 subgroup 조건부 가설로 `REVISED` |
| LIBERO에서만 성립하고 CALVIN zero-shot에서 사라짐 | benchmark-specific state interface로 축소; cross-suite claim 기각 |
| A9 chosen-outcome-only가 P1과 동률 | cloned alternative-option supervision claim을 철회하고 일반 option-value selector로 축소 |
| A1–A9 중 budget/context/value/history/alternative supervision을 제거한 두 개 이상이 P1과 동률 | component novelty를 주장하지 않고 더 단순한 scalar/binary decision protocol로 revise |
| BRCR 개선이 O3 대비 option regret 감소나 acceptable-option agreement로 이어지지 않음 | selector가 outcome을 개선한 것이 아니라 chance/option mix를 이용한 것인지 재검토 |
| P1의 p95 selector latency가 base control deadline을 초과하고 latency-stratified BRCR 이득이 사라짐 | real-time recovery claim을 철회하고 simulator decision-quality 결과로 범위 축소 |
| test task·seed가 fit/calibration에 재사용되거나 threshold를 test 후 변경 | confirmatory 결과 무효; 새 protocol version으로 재실행 |

5 pp와 3 pp는 문헌의 보편적 상수가 아니라 프로젝트의 초기 practical-effect/equivalence margin이다. confirmatory trial 수는 Phase 0/1 variance로 power analysis한 뒤 확정한다.

## 12. 필요한 코드·데이터·연산 자원

### 코드

- pinned LIBERO environment와 `libero_10` BDDL/fixed initial states
- SAFE feature extractor, temporal detector, conformal calibration code
- base VLA rollout adapter. 첫 구현은 SAFE가 이미 연결한 OpenVLA 계열을 우선 사용
- perturbation wrapper와 landmark detector
- simulator clone/restore 및 oracle option-sweep runner
- fixed recovery option library와 task predicate/skill graph replanner
- JSONL event logger, artifact store, metric/paired-bootstrap evaluator
- CALVIN evaluator fork. upstream early-return 동작은 보존한 별도 baseline도 함께 유지

### 데이터

- base VLA checkpoint와 LIBERO-compatible policy configuration
- LIBERO fixed initial states와 task demonstrations/checkpoints
- clean success/failure rollout for SAFE calibration
- injected rollout: detector/context/value head의 train/calibration/test는 `task × init state × perturbation seed`가 겹치지 않게 분리
- option-sweep outcome table: 각 `onset_state_id × budget_id`에서 option별 completion, irreversible event, step/call/reset/rewind/replan/query cost와 ranking
- 고정 manifest: `rp2_split_v1.json`(task/init/seed split), `rp2_factor_manifest_v1.json`(valid factor cells), threshold·λ·margin을 기록한 `rp2_protocol_v2.yaml`
- paired result table: 모든 system의 `episode_id`, event timestamps, BRCR/IFR outcome, option regret, latency를 한 schema로 저장

실제 사용자 demonstration이나 대규모 foundation pretraining은 minimum experiment에 필요하지 않다. injected failure를 학습과 평가에 모두 쓸 때 exact perturbation seed와 onset state가 split을 넘지 않게 한다.

### 환경 및 연산 계획

- LIBERO와 SAFE의 dependency 세대가 다를 수 있으므로 각각 pinned environment/container를 만들고 event schema로만 연결한다.
- headless MuJoCo/EGL, 32–64 GB system RAM, rollout artifact용 약 100 GB 여유 공간을 초기 계획값으로 둔다.
- OpenVLA-class inference는 24 GB급 GPU 1장을 최소 실용 기준으로 잡되, 실제 memory와 throughput은 checkpoint/precision으로 Phase 0에서 측정한다.
- detector/context/value head는 frozen feature를 쓰므로 단일 GPU에서 학습한다. VLA full fine-tuning은 범위 밖이다.
- 총 episode 수보다 wall-clock이 정책 inference 속도에 크게 좌우되므로 Phase 0에서 `steps/sec`, GPU memory, episode artifact size를 측정한 뒤 Phase 1 실행 시간을 산정한다.

## 13. Pre-implementation freeze

이 절은 설명이 아니라 구현 착수 계약이다. 상태 표기는 다음처럼 사용한다.

- `FROZEN`: protocol v2의 기본값. 변경하면 `rp2_protocol_v3`와 새 experiment namespace가 필요하다.
- `PROVISIONAL-FROZEN`: Phase 0 smoke test용 기본값. confirmatory data를 보기 전에 한 번만 바꿀 수 있고 변경 사유와 이전 결과를 남긴다.
- `EMPIRICAL-FREEZE`: 미리 정한 calibration/Phase 0 규칙으로 값을 선택한 뒤 test 전에 잠근다.
- `BLOCKED/EXTENSION`: 현재 최소 C1에 넣지 않는다. interface acceptance test를 통과한 뒤 별도 version에서만 추가한다.

### 13.1 결정 ledger

| 영역 | 결정 | 상태 | freeze artifact / 변경 규칙 |
|---|---|---|---|
| contribution | same-onset all-option supervision이 best-fixed regret를 줄이는지 검증하는 C1; 새 recovery skill·detector·POMDP selector 자체는 claim하지 않음 | `FROZEN` | 이 문서의 claim ladder와 `rp2_protocol_v2.yaml` |
| environment | LIBERO `8f1084e3132a39270c3a13ebe37270a43ece2a01` | `FROZEN` | [official commit](https://github.com/Lifelong-Robot-Learning/LIBERO/tree/8f1084e3132a39270c3a13ebe37270a43ece2a01), container digest 기록 |
| policy adapter | SAFE OpenVLA fork `300dce26d44f407c725695d16cd445755c92cbd1` | `PROVISIONAL-FROZEN` | [fork commit](https://github.com/vla-safe/openvla/tree/300dce26d44f407c725695d16cd445755c92cbd1); smoke test 실패 시 이유와 대체 commit 기록 |
| base checkpoint | `openvla/openvla-7b-finetuned-libero-10` | `PROVISIONAL-FROZEN` | model revision/hash, tokenizer/config hash, weight license를 `rp2_system_manifest_v1.json`에 기록 |
| detector code | SAFE `b6036abe07b2b2bb9996afb2c07f13d6a9f507c0` | `PROVISIONAL-FROZEN` | [official commit](https://github.com/vla-safe/SAFE/tree/b6036abe07b2b2bb9996afb2c07f13d6a9f507c0); official LSTM/MLP reproduction 뒤 primary detector 고정 |
| inference | `center_crop=True`, hidden states 저장, deterministic `n_samples=1`, fixed seed | `FROZEN` | multi-sample uncertainty는 detector sensitivity로만 실행 |
| VLA feature tap | SAFE 공식 후보 `token_idx_rel ∈ {mean, 0.0, 1.0}`를 재현하고 detector calibration 성능으로 하나를 고정 | `EMPIRICAL-FREEZE` | 선택된 tap은 B2/B3/B7/B9–B11/P1에 공통 사용 |
| runtime | Python 3.10, headless EGL, base-policy env와 SAFE-head env 분리 | `PROVISIONAL-FROZEN` | torch/CUDA/MuJoCo/robosuite exact version과 image digest는 smoke test 뒤 lock |
| primary benchmark | 네 Phase 0 task → 통과 시 full `libero_10`; CALVIN은 C2 transfer | `FROZEN` | `rp2_split_v1.json` |
| option library | Phase 0/1은 `O_core`; `O_graph/O_assist`는 별도 extension | `FROZEN` | `rp2_option_library_v1.yaml`; option별 pre/postcondition과 cost unit 필요 |
| trigger | Phase 0 data generation은 oracle `t_effect`; deployed P1은 frozen SAFE alert | `FROZEN` | O1/P1 결과를 분리하고 oracle trigger를 일반 baseline으로 보고하지 않음 |
| decision timing | alert당 1회 선택; `REOBSERVE_WAIT` 뒤 fresh evidence가 있을 때 1회만 재평가 | `FROZEN` | Agentic RL의 fixed-interval decision과 구분해 query count 기록 |
| primary context | selected VLA feature + proprioception/action/alert history + `t/600` + budget; BDDL progress/subgoal 제외 | `FROZEN` | `O_graph`에서만 non-privileged task-state adapter feature 추가 |
| learning problem | grouped full-information supervised prediction; PPO/Q-learning은 X5/sensitivity | `FROZEN` | test-time unchosen outcome 접근 금지 |
| primary selector | risk·feasibility gate → max calibrated completion → cost tie-break → no option이면 abort | `FROZEN` | weighted `q-λcost`는 sensitivity |
| completion tie | calibrated `q` 차이 `<0.02`이면 normalized total cost로 tie-break | `PROVISIONAL-FROZEN` | Phase 1 전 calibration reliability audit 뒤 고정; test 결과로 변경 금지 |
| model architecture | 1-layer GRU hidden 256, history 20 low-level step; option embedding 32; shared MLP 256→128, dropout 0.1 | `PROVISIONAL-FROZEN` | history `{10,20,40}`와 MLP-only는 development sensitivity; test 뒤 변경 금지 |
| optimizer | AdamW, lr `3e-4`, weight decay `1e-4`, batch 64, max 100 epoch, patience 10, seeds `{0,1,2}` | `PROVISIONAL-FROZEN` | Phase 0 sample/throughput 확인 뒤 Phase 1 전에 한 번 고정 |
| loss | empirical q/r/cost target, primary `λrank=0`; P1-rank `λrank=1`; `λaux=0` primary | `FROZEN` | auxiliary type와 rank는 별도 variant; component gain을 섞지 않음 |
| calibration | temperature scaling primary; option별 support가 부족하면 pooled scaling; isotonic은 sensitivity | `EMPIRICAL-FREEZE` | calibration split에서만 선택하고 Brier/ECE와 sample count 공개 |
| risk threshold | calibration에서 IFR non-inferiority `+1 pp`를 만족하는 최대-coverage `δ` | `EMPIRICAL-FREEZE` | 만족 threshold가 없으면 P1은 abort-only 또는 reject |
| strongest baseline | B3/B5/B7/B8/B10/B11과 재현 가능한 X5 우선, matched X0–X6 후보 | `EMPIRICAL-FREEZE` | Phase 1 development에서 `B*`를 정한 뒤 confirmatory test 전에 서명/hash |
| primary statistics | paired cluster bootstrap, `ΔBRCR ≥5 pp`, `ΔIFR` upper CI `≤+1 pp`, clean drop `≤3 pp` | `FROZEN` | Phase 0 variance는 sample-size 산정에만 사용 |
| test access | selector·threshold·B*·manifest hash 고정 뒤 confirmatory outcome 생성 | `FROZEN` | test artifact를 먼저 생성했다면 blind directory/ACL로 fitting process와 분리 |

### 13.2 Provisional perturbation recipe

다음 값은 raw action 단위와 task geometry를 smoke test에서 확인하기 위한 `PROVISIONAL-FROZEN` 시작점이다. validity gate만 보고 조정할 수 있으며 P1/B* 결과를 본 뒤에는 바꾸지 않는다.

| Family | S1 | S2 | validity 조건 |
|---|---|---|---|
| observation | exterior+wrist RGB를 3 frame 지연해 20 low-level step 유지 | trigger frame을 20 low-level step replay한 뒤 fresh stream 복귀 | proprioception은 현재값 유지; S2가 영구 replay면 R4 diagnostic으로 재분류 |
| execution | translational action을 5 step zero/drop | translational action을 10 step zero/drop | gripper command는 보존; native horizon 안에서 task가 여전히 oracle-recoverable |
| world-state | target 또는 receptacle을 collision-free reachable pose로 3 cm 이동 | 같은 규칙으로 7 cm 이동 | orientation과 unrelated object는 고정; IK/workspace feasibility 통과 |
| plan-semantic | 완료된 articulated predicate 하나를 한 번 무효화 | 다음 subgoal 전제조건 두 개를 동시에 무효화 | goal 자체를 이미 만족시키거나 영구 불가능하게 만들지 않음 |

Agentic RL의 raw `Uniform(-3,3)` action noise는 policy/action normalization에 따라 의미가 달라 그대로 복사하지 않는다. ActFovea의 three-frame visual delay는 observation S1의 source-verified starting point로 사용한다. 각 recipe는 effect size가 아니라 **조작 값**으로 고정하고, 결과를 본 뒤 S1/S2를 R1/R2/R3에 맞춰 재라벨링하지 않는다.

### 13.3 Option implementation decision table

| Option | precondition | exact action/termination | cost accounting | 상태 |
|---|---|---|---|---|
| `CONTINUE` | base policy가 active | policy/cache 유지, next native action 실행 | native step만 | `FROZEN` |
| `RETRY_CURRENT` | absorbing event 없음 | environment 불변, policy/cache reset, 동일 instruction 재query; success/timeout/60 recovery step에 종료 | 1 option call + executed step | `PROVISIONAL-FROZEN` |
| `REOBSERVE_WAIT` | camera stream query 가능 | translational zero와 gripper hold를 5 low-level step 실행, fresh timestamp 확인 후 1회 재평가 | 1 option call + 5 step + 1 VLA query | `PROVISIONAL-FROZEN` |
| `STATE_RESET` | 최근 contact-free pose buffer 존재 | gripper open, 최근 30 step 안의 most-recent contact-free EE pose로 OSC retreat, cache reset; 60 step cap | 1 reset + executed step | `PROVISIONAL-FROZEN` |
| `ABORT_STOP` | 항상 가능 | zero/safe-hold command 후 autonomous terminal | completion 아님; abort count | `FROZEN` |
| `SUBGOAL_REWIND` | observed progress checkpoint와 atomic subgoal adapter 존재 | physical state 유지, task/policy state만 last verified checkpoint로 rewind | 1 rewind + suffix step | `BLOCKED/EXTENSION` |
| `TASK_REPLAN` | non-privileged state estimator와 task graph 존재 | 미완료 goal의 새 suffix를 만들고 feasibility check | 1 replan + planner latency | `BLOCKED/EXTENSION` |
| `HUMAN_ESCALATE` | assisted protocol에서만 | safe stop 후 사전 등록한 correction 1회 | 1 terminal query; autonomous success 아님 | `EXTENSION` |

`STATE_RESET`의 recent pose selection은 Agentic RL의 contact-free Repair와 직접 충돌한다. 따라서 이를 RP-2 novelty로 표현하지 않고 X5와 동일 recovery primitive를 공유할 수 있을 때 우선 공유한다. force/contact 신호가 없는 adapter에서는 gripper·object/EE kinematics 기반 contact-free proxy를 사용하고 별도 sensitivity로 표시한다.

### 13.4 Phase 0 acceptance criteria

| Gate | 사전 고정 pass 기준 | 실패 시 결정 |
|---|---|---|
| environment smoke | 네 task 모두 reset/20-step zero-action/goal predicate/logger가 10회 연속 오류 없이 실행 | dependency와 adapter부터 수정 |
| clean competence | task별 10 init 중 최소 5 success, 전체 40 중 최소 24 success | task/checkpoint 교체; 실패 init만 선택적으로 삭제 금지 |
| restore equality | 같은 host/container에서 `qpos/qvel/time`, object state, controller state, policy cache, RNG 복원; 5회 반복에서 state max error `≤1e-7`, proprio `≤1e-6`, normalized RGB max error `≤1/255`, first action `≤1e-5` | tolerance를 결과에 맞춰 완화하지 말고 snapshot 범위를 수정 |
| branch validity | included branch는 action 직전 equivalence 100%; candidate onset 중 valid group 비율 `≥95%` | I-12 wrapper 수정; invalid 수와 원인 공개 |
| perturbation validity | recipe가 의도 field만 바꾸며 goal은 미달성·oracle-recoverable; valid rate `≥90%` | recipe version 수정 후 onset 재수집 |
| sweep stability | 동일 state/option/budget/seed를 3회 재실행했을 때 terminal label agreement `≥90%` | 더 많은 반복 또는 deterministic source 수정 |
| minimum dataset | valid onset `≥20`, 최소 2 task·2 failure family 포함 | P1 학습 금지; data protocol 보강 |
| option separability | valid onset의 `≥20%`에서 stable option pair 차이, 최소 2 task/family에 분포 | learned arbitration reject |
| context value | O3가 B10보다 BRCR `≥5 pp` 또는 normalized BFR `≥0.05` | selector reject; best-fixed protocol로 축소 |
| budget value | BCP `≥10%`이고 최소 2 failure family에서 관찰 | `budgeted/vector-budget` claim 제거 |
| resource feasibility | measured throughput·artifact size로 Phase 1 shortlist가 가용 자원의 4주 이내 | task/system/seed를 사전 규칙으로 줄이고 full matrix 약속 금지 |

20%, 10%, 0.05와 4주는 문헌의 보편적 기준이 아니라 **불필요한 P1 구현을 막기 위한 내부 go/no-go margin**이다. 값은 첫 outcome을 보기 전에 `rp2_protocol_v2.yaml`에 기록한다.

### 13.5 Pre-implementation freeze checklist

Research contract:

- [x] problem, system boundary, H0–H4, RQ0–RQ5 고정
- [x] C0–C3 claim ladder와 broad non-claims 고정
- [x] Agentic RL·ActFovea·ProbeAct·CoRe·ViFailback full-text collision audit 반영
- [x] primary estimand, full-information supervision, baseline·oracle·ablation·metric 정의
- [x] novelty/internal/construct/external/statistical/systems threat와 reject rule 정의

Artifacts that must exist before the first Phase 0 rollout:

- [ ] `rp2_system_manifest_v1.json`: repo/checkpoint/container/GPU/dependency/license hash
- [ ] `rp2_event_v2.schema.json`: header/event required field, enum, validation rule
- [ ] `rp2_option_library_v1.yaml`: `O_core` precondition, timeout, cost, fallback
- [ ] `rp2_factor_manifest_v1.json`: task × onset × recipe × severity × budget × seed valid cell
- [ ] `rp2_split_v1.json`: fit/calibration/confirmatory task·init·recipe·seed isolation
- [ ] `rp2_protocol_v2.yaml`: margins, tolerances, selector, calibration, model/training defaults
- [ ] `THIRD_PARTY.md` 또는 manifest field: LIBERO/SAFE/OpenVLA/code·weight license와 attribution

Acceptance tests that must pass before collecting D2-option:

- [ ] base policy clean-competence report
- [ ] snapshot/restore equality and repeated replay report
- [ ] policy-visible vs evaluator-only field leakage test
- [ ] each `O_core` option unit/integration test and standalone cost table
- [ ] perturbation locality·solvability·onset detection test
- [ ] paired episode ID and immutable artifact/hash test

Freeze steps required before training or confirmatory evaluation:

- [ ] Phase 0 gate report: separability, CCP, BCP, BFR, O3–B10 gap
- [ ] X5 Agentic RL first, then X4/X6 code/input/option/budget reproduction matrix
- [ ] P1 architecture·training seed·calibration·risk threshold freeze
- [ ] strongest non-privileged `B*`와 confirmatory shortlist freeze
- [ ] Phase 2 power calculation and compute/storage budget freeze
- [ ] signed manifest hash와 test-artifact access boundary 확인

체크되지 않은 artifact는 “문서에 적혀 있다”는 이유로 완료 처리하지 않는다. 첫 코드는 environment smoke/logger/snapshot test여야 하며, Phase 0 gate 전에 P1 학습 코드를 최적화하지 않는다.

## 14. 즉시 구현 순서

1. `rp2_system_manifest_v1.json`과 third-party license/checkpoint audit를 작성하고 위 exact commit·checkpoint를 clone 가능한지 확인한다.
2. `rp2_event_v2.schema.json`, `rp2_option_library_v1.yaml`, `rp2_factor_manifest_v1.json`, `rp2_split_v1.json`, `rp2_protocol_v2.yaml`을 생성하고 schema validation test를 만든다.
3. 네 pilot task에서 environment smoke와 clean-competence gate를 실행한다.
4. environment/controller/policy-cache/RNG를 포함하는 snapshot/restore runner와 branch-equivalence test를 작성한다.
5. `O_core`의 unit/integration test와 M0–M2 mechanism control을 구현한다. `O_graph`는 별도 acceptance test 전에는 시작하지 않는다.
6. 네 perturbation family의 provisional S1/S2 locality·solvability를 감사하고 20–50개 valid onset을 수집한다.
7. `B_low/B_mid/B_high`에서 모든 applicable `O_core` option을 sweep하고 Option Separability, CCP, BCP, BFR, O3–B10 gap을 계산한다.
8. Phase 0 gate가 없으면 learned selector를 만들지 않는다. gate가 있으면 Agentic RL X5를 가장 먼저 맞추고 X4/X6의 재현 가능한 mechanism subset을 고정한다.
9. SAFE/TD-calibrated detector와 B1–B11, M0–M2, O3를 고정한 뒤 P1 prediction-only와 P1-rank를 학습한다.
10. A1–A9와 oracle decomposition으로 budget, calibration, context, option-value, history, alternative-outcome supervision을 반증한다.
11. architecture·threshold·`B*`·shortlist·manifest hash를 freeze한 경우에만 full LIBERO confirmatory test와 CALVIN transfer로 확장한다. I-02가 지지되기 전에는 I-06 policy update를 시작하지 않는다.
