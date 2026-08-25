# Robotics Research Gaps

- Updated: 2026-08-25 KST
- Scope: CORE/NEXT 7개 robotics track의 cross-paper gap register
- Related ideas: [RESEARCH_IDEAS.md](./RESEARCH_IDEAS.md)
- Detailed lineages: [synthesis/](../synthesis/README.md)
- Evidence audit: 기존 CORE/NEXT 31편의 원문에서 method, ablation, evaluation, failure/limitation section을 직접 대조했고, 이번 갱신에서 2026 최신 frontier 9편의 official proceedings/project/abstract를 추가 대조했다. 새 9편의 full-text evidence는 아직 `CURATION_ONLY`로 둔다.
- Reading tracker policy: 이 감사는 저장소의 연구 synthesis를 위한 것으로, 사용자의 실제 독서 상태인 `READING_STATUS.csv`는 변경하지 않았다.

## 이 문서의 역할

이 문서는 논문별 아이디어 목록이 아니다. 트랙을 가로질러 반복되는 failure mode, 비현실적 가정, 부족한 데이터·평가, 아직 연결되지 않은 연구축과 최소 검증 실험을 관리한다.

- synthesis 문서: foundation → frontier의 **계보와 변화**
- 이 문서: 원문 비교 후에도 남는 **검증 가능한 공백**
- `RESEARCH_IDEAS.md`: 공백을 해결하기 위한 **가설과 실험 설계**

`P1`은 비교적 작은 실험으로 핵심 가설을 반증할 수 있는 gap, `P2`는 추가 데이터·하드웨어·infrastructure가 필요한 gap이다. Evidence maturity는 사용자 독서 진도와 별개다. 아래 `READING-SUPPORTED`는 각 gap마다 최소 두 편의 원문과 source location을 확인했다는 뜻이며, 직접 재현한 `EXPERIMENT-SUPPORTED`는 아직 없다. 이 문서는 targeted qualitative synthesis이지, 전 문헌을 누락 없이 screen한 systematic review는 아니다.

## 2026-08-24 frontier delta

이번 갱신은 2026 CVPR·ICML·RSS에서 현재 registry에 없던 9편을 추가하고, 기존 gap이 이미 해결된 범위를 다시 좁혔다. 최신 paper는 자동으로 gap을 지지하는 것으로 취급하지 않고, official abstract/proceedings에서 확인 가능한 counter-evidence와 남은 boundary만 반영한다.

| Gap | 새 counter-evidence | 현재 해석 |
|---|---|---|
| G-01 / G-05 | [Tabero](../2026/ICML/2026_ICML_Tabero-Learning-Gentle-Manipulation-with-Closed-Loop-Force/01_overview.md), [TactAlign](../2026/RSS/2026_RSS_TactAlign-Human-to-Robot-Policy-Transfer-via-Tactile-Align/01_overview.md) | force-quality metric과 cross-embodiment tactile alignment는 진전됐지만 sensor mechanics·contact regime 전이의 calibration은 남음 |
| G-02 | [FLARE](../2026/CVPR/2026_CVPR_FLARE-A-Failure-Aware-Framework-for-Autonomous-Correction/01_overview.md), [VLA-FixBench/FaultEval](../2026/ICML/2026_ICML_Can-VLMs-Diagnose-and-Recover-from-VLA-Manipulation-Faults/01_overview.md), [TD calibration](../2026/ICML/2026_ICML_Temporal-Difference-Calibration-in-Sequential-Tasks-Applic/01_overview.md) | failure detection·binary Retry/Reset·sequential confidence는 직접 다뤄졌고, multi-option recovery와 matched budget이 남음 |
| G-04 | [Memory Retrieval/HALO](../2026/RSS/2026_RSS_Memory-Retrieval-in-Visuomotor-Policies-for-Long-Horizon-R/01_overview.md) | task-relevant sparse retrieval과 drift 완화는 제시됐지만 stale-memory expiry와 safety intervention은 미검증 |
| G-10 | [VLA-Arena](../2026/ICML/2026_ICML_VLA-Arena-An-Open-Source-Framework-for-Benchmarking-Vision/01_overview.md) | safety·distractor·extrapolation·long-horizon 축의 공개 benchmark가 생겼지만 event-level recovery log는 별도 설계가 필요 |
| G-13 | [AVA-VLA](../2026/CVPR/2026_CVPR_AVA-VLA-Improving-Vision-Language-Action-Models-with-Activ/01_overview.md) | active visual attention과 recurrent state가 결합됐지만 physical camera cost와 stopping rule은 남음 |

이 delta의 paper note는 metadata와 official abstract/proceedings를 등록한 상태이며, `READING_STATUS.csv`에서 모두 `UNREAD / CURATION_ONLY`로 시작한다. 수치·실패 분석을 gap evidence로 승격하려면 full text의 section/table 위치를 확인해야 한다.

## 2024–2026 frontier trend map

최근 frontier는 개별 architecture의 교체보다 **closed-loop execution, failure/recovery, contact feedback, state/memory, evaluation protocol**을 명시하는 방향으로 이동하고 있다. 아래 표는 이 문서의 gap index와 연결해 trend가 어떤 검증 질문을 남기는지 기록한다.

| 경향 | 대표 registry anchor | 연구적 의미와 남은 검증 질문 |
|---|---|---|
| VLA가 language interface에서 closed-loop controller로 이동 | [OpenVLA](../2024/CoRL/2024_CoRL_OpenVLA-An-Open-Source-Vision-Language-Action-Model/01_overview.md), [π0](../2025/RSS/2025_RSS_pi0-A-Vision-Language-Action-Flow-Model-for-General-Robot/01_overview.md) | action chunk, control rate, feedback, embodiment 조건을 함께 봐야 한다. 동일 policy의 latency·feedback 차이가 실제 recovery와 long-horizon outcome을 얼마나 바꾸는지는 G-02/G-10과 연결된다. |
| failure detection에서 recovery selection으로 확장 | [SAFE](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md), [FLARE](../2026/CVPR/2026_CVPR_FLARE-A-Failure-Aware-Framework-for-Autonomous-Correction/01_overview.md), [FaultEval](../2026/ICML/2026_ICML_Can-VLMs-Diagnose-and-Recover-from-VLA-Manipulation-Faults/01_overview.md) | alert 자체보다 cause·recoverability·remaining budget에 따른 operational decision이 중요해졌다. binary Retry/Reset을 넘어 multi-option typed recovery를 비교하는 RP-2의 직접 배경이다. |
| sequential confidence와 safety calibration 강화 | [FAIL-Detect](../2025/RSS/2025_RSS_Can-We-Detect-Failures-Without-Failure-Data-Uncertainty-Aw/01_overview.md), [Temporal Difference Calibration](../2026/ICML/2026_ICML_Temporal-Difference-Calibration-in-Sequential-Tasks-Applic/01_overview.md) | 평균 success가 아니라 detection delay, false intervention, risk calibration을 측정해야 한다. calibrated score가 selector decision으로 이어지는지는 G-02의 evidence void다. |
| tactile/force가 VLA의 fast feedback 경로로 편입 | [Reactive Diffusion Policy](../2025/RSS/2025_RSS_Reactive-Diffusion-Policy-Slow-Fast-Visual-Tactile-Policy/01_overview.md), [Tabero](../2026/ICML/2026_ICML_Tabero-Learning-Gentle-Manipulation-with-Closed-Loop-Force/01_overview.md), [TactAlign](../2026/RSS/2026_RSS_TactAlign-Human-to-Robot-Policy-Transfer-via-Tactile-Align/01_overview.md) | sensor delay, calibration, contact-regime 전이와 safety–success trade-off가 핵심 변수가 됐다. sensor mechanics와 embodiment가 바뀌어도 state/uncertainty가 유지되는지는 G-01/G-05에 남는다. |
| long-horizon policy의 state/memory/skill 구조화 | [AtomicVLA](../2026/CVPR/2026_CVPR_AtomicVLA-Unlocking-the-Potential-of-Atomic-Skill-Learning/01_overview.md), [Memory Retrieval](../2026/RSS/2026_RSS_Memory-Retrieval-in-Visuomotor-Policies-for-Long-Horizon-R/01_overview.md), [PALM](../2026/CVPR/2026_CVPR_PALM-Progress-Aware-Policy-Learning-via-Affordance-Reasoni/01_overview.md) | failure 이후 continuation, stale state, phase-aware progress와 skill composition이 중요해졌다. memory expiry와 post-recovery state refresh는 G-04/G-10의 미해결 문제다. |
| world model을 policy evaluation·uncertainty에 사용 | [WorldGym](../2026/ICLR/2026_ICLR_WorldGym-World-Model-as-An-Environment-for-Policy-Evaluati/01_overview.md), [WMPO](../2026/ICLR/2026_ICLR_WMPO-World-Model-based-Policy-Optimization-for-Vision-Lang/01_overview.md) | visual fidelity보다 contact/control fidelity와 real-gain calibration이 중요해졌다. imagined rollout의 ranking이 contact·OOD에서도 유지되는지는 G-07/G-08의 검증 범위다. |
| benchmark가 final success에서 failure resolution으로 이동 | [LIBERO-Safety](../2026/ECCV/2026_ECCV_LIBERO-Safety-A-Comprehensive-Benchmark-for-Physical-and-S/01_overview.md), [VLA-Arena](../2026/ICML/2026_ICML_VLA-Arena-An-Open-Source-Framework-for-Benchmarking-Vision/01_overview.md) | event timing, perturbation, intervention cost, recovery 이후 progress를 기록해야 한다. benchmark 간 공통 event schema와 recovery-aware metric은 G-10에 해당한다. |
| humanoid·whole-body와 contact feasibility 결합 | [HumanoidBench](../2024/RSS/2024_RSS_HumanoidBench-Simulated-Humanoid-Benchmark-for-Whole-Body/01_overview.md), [HWC-Loco](../2026/ICLR/2026_ICLR_HWC-Loco-A-Hierarchical-Whole-Body-Control-Approach-to-Rob/01_overview.md) | task progress, balance, torque, contact, recovery reserve를 같은 hierarchy에서 조정해야 한다. locomotion–manipulation coupling과 hardware risk의 bandwidth 문제는 G-09/G-11로 이어진다. |
| 3D perception이 control utility·active sensing으로 재평가 | [ActiveVLA](../2026/CVPR/2026_CVPR_ActiveVLA-Injecting-Active-Perception-into-Vision-Language/01_overview.md), [PointVLA](../2026/RA-L/2026_RA-L_PointVLA-Injecting-the-3D-World-into-Vision-Language-Actio/01_overview.md) | geometry 정확도 자체보다 compute/latency-matched downstream action value가 중요해졌다. representation·view·compute의 인과 효과와 active stopping은 G-03/G-13에서 검증한다. |

이 trend map은 최신 논문을 별도 priority list로 만드는 문서가 아니다. 각 trend를 기존 foundation과 gap index에 연결해, 다음 정독·실험에서 무엇을 고정하고 어떤 outcome을 측정할지 결정하는 용도로 사용한다.

판정은 다음 네 값을 쓴다.

- `strengthened`: 여러 원문에서 같은 failure 또는 limitation이 반복됨
- `partially addressed`: 특정 조건에서는 직접적인 개선 근거가 있음
- `narrowed`: 초기 가설보다 남은 범위가 작거나 조건부임
- `rejected`: 핵심 가설이 통제 실험에서 지지되지 않음

## 인터넷 조사로 채택한 gap 도출 방법

외부 방법론을 robotics에 그대로 옮기지 않고 다음 순서로 적용한다.

1. **Map:** 논문을 method×closed-loop outcome matrix에 코딩한다. Campbell EGM처럼 범위·포함 기준·분류 사전을 먼저 정하고 너무 세분화된 빈칸보다 소수의 큰 공백을 찾는다.
2. **Localize and characterize:** Müller-Bloch·Kranz의 `localization → characterization → verification → presentation`을 따라 후보 gap의 유형과 원인을 분리한다.
3. **Explain why evidence is insufficient:** AHRQ 분류를 사용해 `I` insufficient/imprecise, `B` biased, `C` inconsistent/unknown consistency, `N` not-right/indirect information으로 표기한다. 단순히 논문 수가 적다는 이유는 불충분하다.
4. **Problematize:** Sandberg·Alvesson의 제안처럼 기존 방법이 공유하는 가정을 명시하고, 그 가정이 깨지는 robot·contact·OOD 조건을 찾는다.
5. **Verify against counter-evidence:** 최소 두 개의 독립적 method family 또는 하나의 multi-system benchmark를 대조하고, 이미 해결된 조건을 먼저 적는다. 확인 편향을 피하기 위해 성공 결과와 negative/failure result를 함께 코딩한다.
6. **Bound and decide:** 각 gap을 robotics용 `R-M-C-O-T-S`로 한정하고, 결과에 따라 gap을 유지·축소·기각할 수 있는 최소 결정 실험을 붙인다.

`R-M-C-O-T-S`는 AHRQ PICOS를 robotics에 맞게 바꾼 검증 범위다.

- `R` Robot/embodiment/sensor
- `M` Method, interface, or intervention
- `C` Comparator
- `O` Closed-loop outcome
- `T` Temporal horizon, control rate, or contact phase
- `S` Setting: task, environment, simulator/real, perturbation

Gap class는 `KV` knowledge void, `CE` contradictory evidence, `AK` action–knowledge/deployment conflict, `MC` methodological conflict, `EV` evaluation void, `TA` theory/application/transfer void를 쓴다. 이 코드는 gap의 주제가 아니라 **왜 gap이 존재하는지**를 나타낸다.

### Six macro-gaps

13개 세부 항목을 독립된 13개 research axis로 보지 않고 다음 6개 큰 공백의 검증 단위로 묶는다.

| Macro | Closed-loop location | Sub-gaps | 공통 결정 질문 |
|---|---|---|---|
| M-1 Contact feedback | policy/control → contact → feedback | G-01, G-05 | 센서·로봇·접촉 조건이 바뀌어도 fast feedback이 안전하게 유지되는가? |
| M-2 Failure and recovery | feedback → diagnosis → recovery | G-02, G-10 | failure를 검출만 하지 않고 적절한 recovery와 최종 outcome으로 연결할 수 있는가? |
| M-3 Task-effective state | observation → state → action | G-03, G-04, G-13 | 추가 geometry·memory·view가 비용보다 큰 control value를 주는 조건은 무엇인가? |
| M-4 Model-based decision | world model → evaluation/update | G-07, G-08 | imagined rollout이 contact·OOD에서 실제 policy 선택과 개선을 예측하는가? |
| M-5 Embodied deployment | task policy → whole-body control | G-09, G-11 | task/motion prior를 dynamics·contact·hardware risk와 어떻게 조정하는가? |
| M-6 Data and evidence | data → learning → generalization | G-06, G-12 | 규모와 성공 평균이 아닌 어떤 coverage가 안전한 일반화를 만드는가? |

## Gap index

| ID | Macro | Priority | Maturity | Verdict | Class / evidence reason | 검증 후 남은 핵심 공백 |
|---|---|---|---|---|---|---|
| G-01 | M-1 | P1 | `READING-SUPPORTED` | `partially addressed` | `TA+EV / C+N` | slow–fast force/tactile loop의 cross-sensor·cross-embodiment 안정성 |
| G-02 | M-2 | P1 | `READING-SUPPORTED` | `narrowed` | `AK+EV / I+C` | explicit recoverability와 동일 budget 아래 multi-option recovery 선택 |
| G-03 | M-3 | P1 | `READING-SUPPORTED` | `narrowed` | `MC+EV / B+N` | 3D 정확도가 아니라 compute-matched control utility를 검증하는 평가 |
| G-04 | M-3 | P1 | `READING-SUPPORTED` | `strengthened` | `KV+EV / I+N` | stale memory 탐지, phase-aware update, memory expiry의 안전성 |
| G-05 | M-1 | P1 | `READING-SUPPORTED` | `strengthened` | `TA+MC / C+N` | sensor mechanics에 불변인 contact state와 uncertainty 표현 |
| G-06 | M-6 | P1 | `READING-SUPPORTED` | `strengthened` | `AK+MC / I+N` | 실패 trajectory를 severity·recoverability와 함께 안전하게 재사용하는 법 |
| G-07 | M-4 | P1 | `READING-SUPPORTED` | `narrowed` | `CE+EV / C+N` | 평균 success/ranking을 넘어 contact·OOD에서 control fidelity를 보장하는 법 |
| G-08 | M-4 | P2 | `READING-SUPPORTED` | `partially addressed` | `EV+AK / I+C` | imagined policy update의 uncertainty calibration과 real gain 예측 |
| G-09 | M-5 | P1 | `READING-SUPPORTED` | `strengthened` | `AK+TA / I+N` | locomotion–manipulation coupling을 bandwidth·risk와 함께 조정하는 hierarchy |
| G-10 | M-2 | P1 | `READING-SUPPORTED` | `narrowed` | `EV+MC / B+N` | benchmark 간 공통 event taxonomy와 recovery-aware long-horizon metric |
| G-11 | M-5 | P2 | `READING-SUPPORTED` | `strengthened` | `TA+AK / I+N` | human motion prior를 contact feasibility·hardware safety와 정렬하는 법 |
| G-12 | M-6 | P2 | `READING-SUPPORTED` | `narrowed` | `CE+MC / C+N` | trajectory 수가 아닌 embodiment·outcome·condition coverage의 scaling law |
| G-13 | M-3 | P2 | `READING-SUPPORTED` | `partially addressed` | `AK+EV / I+N` | 추가 관측의 성공 이득을 latency·camera motion·risk 비용과 함께 최적화하는 법 |

## G-01. VLA와 접촉 제어의 시간 척도 불일치

- **Gap claim:** slow–fast tactile/force policy의 이득이 sensor mechanics, robot, delay, contact regime이 바뀌어도 안전성과 함께 유지되는지는 확인되지 않았다.
- **검증 범위 (`R-M-C-O-T-S`):** multi-sensor manipulator / calibrated slow–fast fusion / vision-only·early fusion·gated fusion / success·peak force·latency / contact event·delay·dropout / insertion·wiping, real or high-fidelity contact setup.
- **도출 근거:** `TA+EV / C+N`. 각 system에서의 성공 근거는 있지만 cross-sensor consistency가 알려지지 않았고, 현재 outcome은 전이 안정성에 간접적이다.
- **읽은 뒤 판정 — `partially addressed`:** slow semantic stream과 fast tactile/force stream을 분리하는 방향은 이미 실효성이 있다. AT-VLA는 0.04초 closed-loop 반응을 보고했고, ForceVLA2는 force-aware hybrid force–position action으로 5개 real-robot task 평균 66%를 달성했다. 최신 Tabero는 force quality를 별도 metric으로 만들고 TactAlign은 paired data 없는 cross-embodiment tactile alignment를 제시했지만, **다른 sensor mechanics·robot·contact regime에서도 calibration과 안전성이 유지되는가**는 여전히 남는다.
- **반복된 failure/가정:** 단순 tactile injection은 AT-VLA의 vanilla VLA 대비 평균 성능을 9% 낮췄고, ForceVLA2에서도 native force concatenation은 π0보다 나빴다. 새 modality가 항상 유익하며 pretrained representation을 보존한다는 가정이 성립하지 않는다.
- **부족한 평가:** control rate, sensor-to-action latency, peak/impulse force, overload, contact-event-conditioned success, missing-sensor degradation을 같은 protocol에서 보고하지 않는다. 두 논문 모두 소수 task와 단일 hardware/sensor family에 집중한다.
- **연결되지 않은 축:** action chunking·flow/diffusion ↔ tactile/force state estimation ↔ operational-space hybrid control ↔ hard safety constraint.
- **최소 반증 실험:** 동일 demonstration과 backbone으로 vision-only, early fusion, gated fusion, slow–fast residual/hybrid control을 peg insertion과 wiping에서 비교한다. sensor delay·dropout·stiffness를 독립적으로 바꾸고 success, peak force, reaction latency를 함께 측정한다.
- **Full-text support:** AT-VLA Sec. 4.4.1/Table 3 — naïve injection의 degradation과 gating 효과; ForceVLA2 Sec. 5/Table 1–3 — 20 trials/task, sudden perturbation, modality ablation.
- **Anchors:** [AT-VLA](../2026/CVPR/2026_CVPR_AT-VLA-Adaptive-Tactile-Injection-for-Enhanced-Feedback-Re/01_overview.md), [ForceVLA2](../2026/CVPR/2026_CVPR_ForceVLA2-Unleashing-Hybrid-Force-Position-Control-with-Fo/01_overview.md), [Tabero](../2026/ICML/2026_ICML_Tabero-Learning-Gentle-Manipulation-with-Closed-Loop-Force/01_overview.md), [TactAlign](../2026/RSS/2026_RSS_TactAlign-Human-to-Robot-Policy-Transfer-via-Tactile-Align/01_overview.md), [Diffusion Policy](../2023/RSS/2023_RSS_Diffusion-Policy-Visuomotor-Policy-Learning-via-Action-Dif/01_overview.md), [Reactive Diffusion Policy](../2025/RSS/2025_RSS_Reactive-Diffusion-Policy-Slow-Fast-Visual-Tactile-Policy/01_overview.md).

## G-02. Detection에서 recovery까지 닫히지 않은 loop

- **Gap claim:** calibrated failure score만으로는 failure type·recoverability·남은 risk budget에 맞는 recovery action을 선택할 수 없다.
- **검증 범위 (`R-M-C-O-T-S`):** VLA manipulator / typed recovery selector / abort·blind retry·replan / final success·irreversible failure·intervention cost / onset에서 post-recovery까지 / long-horizon benchmark perturbation wrapper.
- **도출 근거:** `AK+EV / I+C`. detection과 recovery의 개별 요소는 알려졌고 FLARE가 Retry/Reset까지 연결했다. 남은 공백은 explicit recoverability, 동일 budget, 여러 option, post-recovery outcome을 함께 통제한 비교다.
- **읽은 뒤 판정 — `narrowed`:** SAFE는 VLA latent feature로 unseen-task failure를 검출하지만 recovery learning은 scope 밖이다. Recovery RL은 safety critic과 별도 recovery policy를 연결한다. FLARE는 ID recoverable error에 Retry, OOD/state-breaking error에 Reset을 배정하고 online arbitration을 수행하며, VLA-FixBench/FaultEval은 fault taxonomy와 rollback recovery를 benchmark로 구체화한다. TD calibration은 sequential success confidence를 alert에 쓸 수 있는 방향을 보인다. 따라서 “typed recovery가 없다”는 넓은 claim은 기각하고, 남은 문제를 binary Retry/Reset을 넘어 operational recoverability와 multi-option 선택을 **같은 time/action/risk budget과 oracle decomposition**으로 검증하는 것으로 한정한다.
- **반복된 failure/가정:** scalar failure score 또는 constraint probability가 stop, retry, backtrack, reobserve, replan 중 적절한 행동을 바로 결정해 준다고 암묵적으로 본다. SAFE는 사전 성공·실패 rollout과 white-box VLA feature가 필요하며 cross-embodiment 일반화는 검증하지 않았다.
- **부족한 데이터·평가:** failure type, onset, reversibility, intervention cost, recovery action, 최종 outcome이 정렬된 multi-task dataset이 없다. detector AUROC/timeliness와 recovery success·risk를 분리해서 평가한다.
- **연결되지 않은 축:** partial-observation belief/state estimation ↔ calibrated detection ↔ causal diagnosis ↔ typed recovery option ↔ learned safety set ↔ human escalation.
- **최소 반증 실험:** LIBERO-Long에 observation, execution/contact, world-state, plan-semantic perturbation을 삽입한다. abort, blind retry, privileged replan, FLARE-style binary Retry/Reset, learned typed recovery를 같은 native horizon과 recovery budget에서 비교한다. oracle detector와 cloned-state option sweep으로 detector·selector·skill-library 병목을 분리한다.
- **Full-text support:** Recovery RL Sec. II–III/Sec. VI — safety critic과 별도 recovery policy, formal guarantee·physical evaluation의 한계; SAFE Sec. 6.4/Sec. 7/App. F.3 — low-overhead detection, cross-embodiment 한계, recovery가 scope 밖임; FLARE 공식 CVPR abstract — ID/OOD error taxonomy와 Retry/Reset recovery. VLA-FixBench/FaultEval·TD calibration은 이번 갱신에서 official project/abstract만 확인했으며 full-text location은 정독 후 추가한다.
- **Anchors:** [POMDP](../1998/Artificial-Intelligence/1998_Artificial-Intelligence_Planning-and-Acting-in-Partially-Observable-Stochastic-Dom/01_overview.md), [Recovery RL](../2020/RA-L/2020_RA-L_Recovery-RL-Safe-Reinforcement-Learning-with-Learned-Recov/01_overview.md), [SAFE](../2025/NeurIPS/2025_NeurIPS_SAFE-Multitask-Failure-Detection-for-Vision-Language-Actio/01_overview.md), [FAIL-Detect](../2025/RSS/2025_RSS_Can-We-Detect-Failures-Without-Failure-Data-Uncertainty-Aw/01_overview.md), [Counterfactual VLA](../2026/CVPR/2026_CVPR_Counterfactual-VLA-Self-Reflective-Vision-Language-Action/01_overview.md), [FLARE](../2026/CVPR/2026_CVPR_FLARE-A-Failure-Aware-Framework-for-Autonomous-Correction/01_overview.md), [VLA-FixBench/FaultEval](../2026/ICML/2026_ICML_Can-VLMs-Diagnose-and-Recover-from-VLA-Manipulation-Faults/01_overview.md), [TD calibration](../2026/ICML/2026_ICML_Temporal-Difference-Calibration-in-Sequential-Tasks-Applic/01_overview.md).

## G-03. 3D perception 향상과 control 향상의 compute-matched 인과성

- **Gap claim:** 보고된 3D policy 이득에서 representation 자체의 인과 효과와 추가 view·supervision·compute의 효과가 분리되지 않았다.
- **검증 범위 (`R-M-C-O-T-S`):** vision-based manipulator / RGB·point cloud·object state / matched backbone·data·view·runtime / success·collision·contact error·latency / per-action inference / pose·occlusion·calibration perturbation.
- **도출 근거:** `MC+EV / B+N`. 비교 설계의 confound로 representation effect가 편향될 수 있고 geometry metric은 closed-loop utility에 간접적이다.
- **읽은 뒤 판정 — `narrowed`:** 3D가 control에 유용하다는 직접 증거는 이미 있다. FlowBot3D는 learned 3D articulation flow로 real-world 45/70 성공을 보고했고, ActiveVLA의 component ablation은 fixed-view 87.6%/0.26초에서 active view+zoom 91.8%/0.53초로 상승했다. 남은 gap은 **3D의 이득이 추가 view, compute, supervision이 아니라 representation 자체에서 왔는지**와 그 이득이 latency를 상쇄하는지다.
- **반복된 failure/가정:** 더 dense하고 정확한 geometry가 언제나 더 좋은 policy state라고 본다. FlowBot3D의 실제 실패는 flow error뿐 아니라 contact failure·robot occlusion에서 나왔고, ActiveVLA의 가장 어려운 GemBench L4는 1.2%에 머문다.
- **부족한 평가:** 동일 backbone, data, view count, runtime budget을 고정한 2D/point cloud/object-centric/implicit-3D 비교와 downstream sensitivity 분석이 부족하다.
- **연결되지 않은 축:** geometry pretraining ↔ task-conditioned state bottleneck ↔ action/contact sensitivity ↔ real-time systems cost.
- **최소 반증 실험:** 같은 policy head와 camera stream에 RGB, point cloud, object-centric state를 연결한다. compute와 parameter를 맞추고 pose·occlusion·calibration 교란별 success, collision, contact error, latency를 측정한다.
- **Full-text support:** FlowBot3D Sec. IV-B/Sec. V — 64.3% overall success와 occlusion/contact failure 분석; ActiveVLA Sec. 4.2/Table 4/Fig. 5 — active components의 success–inference-time trade-off.
- **Anchors:** [FlowBot3D](../2022/RSS/2022_RSS_FlowBot3D-Learning-3D-Articulation-Flow-to-Manipulate-Arti/01_overview.md), [ActiveVLA](../2026/CVPR/2026_CVPR_ActiveVLA-Injecting-Active-Perception-into-Vision-Language/01_overview.md), [SUGAR](../2024/CVPR/2024_CVPR_SUGAR-Pre-training-3D-Visual-Representations-for-Robotics/01_overview.md), [RoboSpatial](../2025/CVPR/2025_CVPR_RoboSpatial-Teaching-Spatial-Understanding-to-2D-and-3D-Vi/01_overview.md), [PointVLA](../2026/RA-L/2026_RA-L_PointVLA-Injecting-the-3D-World-into-Vision-Language-Actio/01_overview.md).

## G-04. Persistent spatial memory의 staleness와 uncertainty

- **Gap claim:** persistent memory가 현재 task phase를 반영하는지 판단하고 retain·refresh·expire·verify를 안전하게 선택하는 기준이 부족하다.
- **검증 범위 (`R-M-C-O-T-S`):** mobile/manipulation VLA / confidence·phase·expiry memory / no memory·persistent memory / stale read·unsafe action·success·rescan / multi-step state transition / relocation·removal·delayed observation.
- **도출 근거:** `KV+EV / I+N`. dynamic update 방법은 있지만 stale-memory-induced control failure와 expiry decision을 직접 측정한 증거가 부족하다.
- **읽은 뒤 판정 — `strengthened`:** 최신 방법이 문제를 직접 드러낸다. MomaGraph는 관측된 state transition으로 graph edge를 갱신하지만 interaction policy는 scope 밖이고, real-robot 10 trials에서 graph generation·action sequencing error가 남았다. SOMA는 dynamic refinement로 성능을 높였지만, 원문 failure analysis에서 noisy spatial tokens 44%, irrelevant retrieval 32%, task-phase unawareness 24%를 보고한다. RSS 2026의 Memory Retrieval/HALO는 task-relevant sparse retrieval과 accumulated memory drift 완화를 제시해 retrieval 문제를 좁혔지만, stale read를 언제 폐기하거나 재관측할지는 여전히 비어 있다.
- **반복된 failure/가정:** short initial scan과 quasi-static scene, globally fixed association/fusion threshold, object-level memory가 충분하다고 본다. SOMA는 drawer open/closed 같은 phase transition과 room-scale drift를 명시적 한계로 든다.
- **부족한 데이터·평가:** relocation, disappearance, reappearance, delayed observation, loop-closure drift, false association을 독립 제어하고 stale-memory-induced unsafe action을 측정하는 benchmark가 부족하다.
- **연결되지 않은 축:** SLAM uncertainty ↔ object/phase memory ↔ VLA context retrieval ↔ active re-observation ↔ memory expiry/safety shield.
- **최소 반증 실험:** object relocation·removal·sensor dropout을 삽입하고 no-memory, persistent memory, confidence+expiry memory를 비교한다. stale read rate, unnecessary re-scan, task success, collision/unsafe grasp를 함께 측정한다.
- **Full-text support:** MomaGraph Sec. 4.3/Sec. 6.4 — state-aware graph update와 real-robot stage failure; SOMA App. D.7–D.8/Table 14–15 — dynamic-view execution error, noisy/irrelevant memory, phase·scale·safety 한계.
- **Anchors:** [MomaGraph](../2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/01_overview.md), [Spatial Memory for Out-of-Vision Manipulation](../2026/ICML/2026_ICML_Spatial-Memory-for-Out-of-Vision-Manipulation-in-Vision-La/01_overview.md), [Memory Retrieval/HALO](../2026/RSS/2026_RSS_Memory-Retrieval-in-Visuomotor-Policies-for-Long-Horizon-R/01_overview.md), [DROID-SLAM](../2021/NeurIPS/2021_NeurIPS_DROID-SLAM-Deep-Visual-SLAM-for-Monocular-Stereo-and-RGB-D/01_overview.md), [ConceptFusion](../2023/RSS/2023_RSS_ConceptFusion-Open-set-Multimodal-3D-Mapping/01_overview.md).

## G-05. Contact state의 불완전한 observability와 sensor 종속성

- **Gap claim:** tactile image나 force 자체가 아닌 probabilistic contact state를 서로 다른 sensor mechanics에서 적은 calibration으로 전이할 수 있는지는 확인되지 않았다.
- **검증 범위 (`R-M-C-O-T-S`):** 두 종류 이상 tactile/F-T sensor·gripper / shared contact latent / zero-shot·encoder calibration·end-to-end adaptation / mode accuracy·slip·control success / contact transition / matched interaction, material·stiffness sweep.
- **도출 근거:** `TA+MC / C+N`. vision-based tactile 내부의 통합 결과와 서로 다른 physical sensor 전이 결과는 일관되지 않으며, 현재 representation metric은 control transfer에 간접적이다.
- **읽은 뒤 판정 — `strengthened`:** UniTouch는 여러 vision-based tactile sensor를 하나의 embedding으로 정렬하지만 barometric·force 등 다른 출력 형식은 범위 밖이다. Tactile-Driven Non-Prehensile Manipulation은 Soft Bubble에서 Gelslim으로 옮길 때 elasticity를 다시 식별해야 했고, 더 높은 stiffness와 slip이 tracking을 악화시켰다. TactAlign은 paired data와 동일 sensor 없이 human tactile을 robot latent로 정렬하는 직접적인 counter-evidence를 제공하고, Tabero는 force-position을 분리해 contact quality를 평가하지만, 두 결과 모두 sensor mechanics와 unseen contact regime 전반의 calibration을 보장하지 않는다.
- **반복된 failure/가정:** sensor image/force를 contact state 그 자체로 취급하거나 sticking contact, constant friction, accurate elasticity를 가정한다. RoboPack 역시 SoftBubble과 task-specific cost/planner에 의존한다.
- **부족한 데이터·평가:** 같은 interaction을 여러 tactile sensor, gripper, material, mounting stiffness에서 동기화한 cross-sensor split과 calibration-budget curve가 부족하다.
- **연결되지 않은 축:** analytic contact mode ↔ learned tactile foundation representation ↔ probabilistic contact state ↔ hybrid control.
- **최소 반증 실험:** SoftBubble/GelSlim/DIGIT 또는 wrist F/T 중 두 종류 이상에서 동일 slip·contact-mode latent를 학습한다. zero-shot, encoder-only calibration, end-to-end adaptation을 같은 calibration budget으로 비교한다.
- **Full-text support:** Binding Touch Sec. 5/Table 8 — sensor token 효과와 vision-based sensor 범위; Tactile-Driven Sec. V–VI/Table IV — sensor stiffness·slip·sticking/friction 가정; RoboPack Sec. VI — 두 task/SoftBubble 범위와 task-specific planning adaptation.
- **Anchors:** [Binding Touch to Everything](../2024/CVPR/2024_CVPR_Binding-Touch-to-Everything-Learning-Unified-Multimodal-Ta/01_overview.md), [RoboPack](../2024/RSS/2024_RSS_RoboPack-Learning-Tactile-Informed-Dynamics-Models-for-Den/01_overview.md), [Tactile-Driven Non-Prehensile Manipulation](../2024/RSS/2024_RSS_Tactile-Driven-Non-Prehensile-Object-Manipulation-via-Extr/01_overview.md), [TactAlign](../2026/RSS/2026_RSS_TactAlign-Human-to-Robot-Policy-Transfer-via-Tactile-Align/01_overview.md), [Tabero](../2026/ICML/2026_ICML_Tabero-Learning-Gentle-Manipulation-with-Closed-Loop-Force/01_overview.md).

## G-06. Failure와 suboptimal data의 안전한 재사용

- **Gap claim:** unsuccessful trajectory를 harmless suboptimality, recoverable prefix, harmful action, irreversible terminal로 나누지 않으면 평균적 conservatism만으로는 안전한 재사용을 보장할 수 없다.
- **검증 범위 (`R-M-C-O-T-S`):** offline manipulation/VLA data / typed-failure weighting·conservative learning / success-only BC·naïve mix·CQL·IQL / success·harmful update·recovery recall·worst group / pre-onset에서 post-recovery까지 / DROID-style held-out condition·embodiment.
- **도출 근거:** `AK+MC / I+N`. 실패 data는 존재하지만 learning objective와 평가에 연결된 증거가 부족하고, scalar reward는 failure semantics에 간접적이다.
- **읽은 뒤 판정 — `strengthened`:** CQL과 IQL은 offline data의 distribution shift와 OOD action value error를 줄이는 강한 foundation이지만, robot failure의 의미·severity·recoverability를 모델링하지 않는다. DROID는 약 16k unsuccessful trajectories를 공개하지만 본체 규모는 76k successful episodes로 정의하고 policy experiment는 처음 40k successful trajectories를 사용한다. 즉 failure data는 존재해도 학습 신호로 연결되지 않는다.
- **반복된 failure/가정:** scalar reward 또는 conservatism만으로 harmless suboptimality, recoverable failure, catastrophic failure를 구분할 수 있다고 본다. CQL은 deep-network lower-bound guarantee와 early stopping이 미해결이고, IQL의 improvement는 dataset action coverage에 묶인다.
- **부족한 데이터·평가:** onset, cause, severity, intervention, recovery, post-recovery outcome이 함께 정렬된 large-scale robot failure dataset과 held-out embodiment 평가가 부족하다.
- **연결되지 않은 축:** DAgger intervention ↔ CQL/IQL conservatism ↔ VLA failure detector ↔ trajectory segmentation·curation.
- **최소 반증 실험:** DROID의 success subset과 unsuccessful subset을 사용해 success-only BC, naïve mixed BC, IQL/CQL, typed-failure weighting을 비교한다. success뿐 아니라 harmful update rate, recovery opportunity recall, worst-group performance를 측정한다.
- **Full-text support:** CQL Sec. 1/Sec. 7 — distribution shift, conservative value, deep-function/early-stopping 한계; IQL Sec. 1/Sec. 6 — in-sample improvement와 dataset support; DROID Sec. III-B/Sec. V — 16k unsuccessful release와 successful-only training subset.
- **Anchors:** [DAgger](../2011/AISTATS/2011_AISTATS_A-Reduction-of-Imitation-Learning-and-Structured-Predictio/01_overview.md), [CQL](../2020/NeurIPS/2020_NeurIPS_Conservative-Q-Learning-for-Offline-Reinforcement-Learning/01_overview.md), [IQL](../2022/ICLR/2022_ICLR_Offline-Reinforcement-Learning-with-Implicit-Q-Learning/01_overview.md), [DROID](../2024/RSS/2024_RSS_DROID-A-Large-Scale-In-The-Wild-Robot-Manipulation-Dataset/01_overview.md), [RoboMimic](../2021/CoRL/2021_CoRL_What-Matters-in-Learning-from-Offline-Human-Demonstrations/01_overview.md).

## G-07. World model의 visual fidelity와 control fidelity 불일치

- **Gap claim:** average success나 visual realism이 높아도 contact·rare failure·OOD subgroup에서 world-model policy ranking이 보존된다고 할 수 없다.
- **검증 범위 (`R-M-C-O-T-S`):** VLA checkpoints·candidate actions / action-conditioned world-model OPE / real rollout ranking / subgroup rank correlation·false-safe·contact event error / multi-step rollout horizon / ID·visual OOD·contact·recovery.
- **도출 근거:** `CE+EV / C+N`. 평균 ranking 보존과 미세 contact miss가 공존하며, pixel/average metric은 safety-critical control fidelity에 간접적이다.
- **읽은 뒤 판정 — `narrowed`:** WorldGym은 세 VLA의 평균 success가 real-world 값과 평균 3.3% 차이였고 model/version/checkpoint ranking도 보존했다. 따라서 world model이 policy evaluation에 무용하다는 강한 가설은 기각된다. 남은 gap은 **어떤 policy·task·contact/OOD 조건에서 ranking이 깨지는가**다. 공식 abstract도 realistic object interaction은 여전히 어렵다고 명시한다.
- **반복된 failure/가정:** pixel realism 또는 평균 success correlation이 contact event, rare failure, action-conditioned causal correctness까지 보장한다고 본다. UWM의 모든 비교 모델은 visual distraction OOD에서 저하됐고, WMPO world model은 square가 stick에 걸리는 미세한 최종 contact failure를 놓치는 사례를 보였다.
- **부족한 평가:** video metric, trajectory return, pairwise policy ranking, contact outcome, constraint violation을 동일 rollout과 subgroup에서 함께 측정하는 protocol이 부족하다.
- **연결되지 않은 축:** generative video fidelity ↔ action-conditioned causal model ↔ policy ranking/OPE ↔ contact·safety event prediction.
- **최소 반증 실험:** 정책 checkpoint와 candidate action을 쌍으로 구성해 world-model ranking과 real rollout ranking을 비교한다. visual OOD, contact-rich, recovery 세 subgroup별 Kendall/Spearman correlation과 false-safe rate를 보고한다.
- **Full-text support:** Unified World Models Sec. IV-B — real-robot ID/OOD 결과와 distraction 저하; WorldGym Sec. 4.1–4.3 — success correlation·ranking·OOD probing; WMPO App. C — subtle stuck failure의 prediction miss.
- **Anchors:** [Unified World Models](../2025/RSS/2025_RSS_Unified-World-Models-Coupling-Video-and-Action-Diffusion-f/01_overview.md), [WorldGym](../2026/ICLR/2026_ICLR_WorldGym-World-Model-as-An-Environment-for-Policy-Evaluati/01_overview.md), [WMPO](../2026/ICLR/2026_ICLR_WMPO-World-Model-based-Policy-Optimization-for-Vision-Lang/01_overview.md), [DayDreamer](../2022/CoRL/2022_CoRL_DayDreamer-World-Models-for-Physical-Robot-Learning/01_overview.md), [TD-MPC2](../2024/ICLR/2024_ICLR_TD-MPC2-Scalable-Robust-World-Models-for-Continuous-Contro/01_overview.md).

## G-08. Imagined policy improvement의 보수성과 calibration

- **Gap claim:** world model에서 예측한 policy gain과 uncertainty가 update 크기·horizon·OOD 정도에 따라 실제 robot gain과 정렬되는지는 확인되지 않았다.
- **검증 범위 (`R-M-C-O-T-S`):** fixed VLA checkpoint / uncertainty-penalized imagined update / offline DPO·no update·penalty variants / predicted-real gain calibration·false improvement·success / horizon·trust-region sweep / contact-rich held-out model·real trials.
- **도출 근거:** `EV+AK / I+C`. real improvement 증거가 소수 task에 한정되고 model-error penalty의 consistency가 알려지지 않았다.
- **읽은 뒤 판정 — `partially addressed`:** MOPO는 dynamics uncertainty로 imagined reward를 낮춰 model exploitation을 완화했고 oracle-error penalty와의 차이가 uncertainty estimation의 중요성을 보였다. WMPO는 world model 안의 on-policy update로 한 real-robot insertion task에서 base 53%, offline DPO 60%, WMPO 70%/30 trials를 보고했다. imagined improvement가 실제 이득으로 이어질 수 있다는 증거는 생겼지만 범위는 아직 좁다.
- **반복된 failure/가정:** ensemble disagreement 또는 reward-model score가 policy update가 방문할 OOD region에서도 calibrated되어 있다고 본다. WMPO의 reward model F1이 높아도 dynamics가 미세한 jamming을 틀리게 생성하면 policy가 그 오류를 이용할 수 있다.
- **부족한 평가:** imagined rollout horizon, uncertainty calibration, policy-update size, predicted gain과 real gain을 함께 sweep한 real-robot study가 부족하다.
- **연결되지 않은 축:** offline RL conservatism ↔ epistemic dynamics uncertainty ↔ reward-model uncertainty ↔ constrained VLA update.
- **최소 반증 실험:** 같은 VLA checkpoint를 world model에서 여러 trust-region/uncertainty penalty로 업데이트한다. imagined gain, held-out model gain, 실제 30-trial gain과 false-improvement rate의 calibration curve를 비교한다.
- **Full-text support:** MOPO Sec. 5–6/Table 3 — uncertainty penalty와 oracle comparison; WMPO Sec. 4.5/App. C–D — real-robot gain, missed contact failure, action-representation 범위.
- **Anchors:** [MOPO](../2020/NeurIPS/2020_NeurIPS_MOPO-Model-based-Offline-Policy-Optimization/01_overview.md), [WMPO](../2026/ICLR/2026_ICLR_WMPO-World-Model-based-Policy-Optimization-for-Vision-Lang/01_overview.md), [TD-MPC2](../2024/ICLR/2024_ICLR_TD-MPC2-Scalable-Robust-World-Models-for-Continuous-Contro/01_overview.md).

## G-09. Locomotion과 manipulation의 bandwidth·objective 충돌

- **Gap claim:** decoupled hierarchy와 monolithic whole-body policy 사이에서 task progress, stability, perception bandwidth, hardware risk를 online으로 조정하는 interface가 부족하다.
- **검증 범위 (`R-M-C-O-T-S`):** mobile manipulator/humanoid / risk-budget hierarchy / decoupled·monolithic / success·fall·support margin·torque·recovery / locomotion-to-contact transition / door task, payload·push·camera-motion sweep.
- **도출 근거:** `AK+TA / I+N`. loco-manipulation 실패는 보고되지만 objective/bandwidth 조정을 직접 비교한 증거가 부족하고 개별 task success는 coupling mechanism에 간접적이다.
- **읽은 뒤 판정 — `strengthened`:** Whole-Body NMPC는 contact timing까지 80–190 Hz로 최적화하지만 update rate가 30 Hz 아래면 hardware performance가 크게 저하되고, 더 긴 horizon·torque constraint·model adaptation이 남는다. Mobile ALOHA에서는 action chunk 전환의 jerky motion과 visual/proprioception weighting trade-off가 나타났다. HumanoidBench의 door failure는 팔 pulling과 whole-body backward motion의 결합을 직접 보여준다.
- **반복된 failure/가정:** decoupled locomotion/manipulation policy를 합치면 momentum, contact switching, perception motion을 처리할 수 있다고 본다. 반대로 monolithic policy는 stability reward에 갇혀 task progress를 포기할 수 있다.
- **부족한 평가:** 이동 중 contact manipulation, payload, external push, head-camera motion을 함께 포함하고 task success, stability margin, recovery, peak torque를 동시에 측정하는 real-robot protocol이 부족하다.
- **연결되지 않은 축:** task planner ↔ whole-body dynamics/contact MPC ↔ learned skill policy ↔ perception bandwidth ↔ safety recovery.
- **최소 반증 실험:** mobile/humanoid가 이동하며 양팔로 문을 여는 task에서 decoupled, monolithic, risk-budget hierarchy를 비교한다. disturbance와 payload를 sweep하고 success, fall, base/end-effector error, recovery time을 측정한다.
- **Full-text support:** Whole-Body NMPC Sec. IV–V — solver rate, disturbance response, horizon/constraint 한계; Mobile ALOHA Sec. 6.2/Sec. 9 — chunk switching failure와 single-task/expert-data 범위; HumanoidBench Sec. V-E — door/highbar/hurdle failure decomposition.
- **Anchors:** [Whole-Body NMPC](../2018/RA-L/2018_RA-L_Whole-Body-Nonlinear-Model-Predictive-Control-Through-Cont/01_overview.md), [Mobile ALOHA](../2024/CoRL/2024_CoRL_Mobile-ALOHA-Learning-Bimanual-Mobile-Manipulation-using-L/01_overview.md), [HumanoidBench](../2024/RSS/2024_RSS_HumanoidBench-Simulated-Humanoid-Benchmark-for-Whole-Body/01_overview.md), [RoboPanoptes](../2025/RSS/2025_RSS_RoboPanoptes-The-All-Seeing-Robot-with-Whole-body-Dexterit/01_overview.md).

## G-10. Long-horizon 평가의 낮은 failure resolution

- **Gap claim:** benchmark별 phase/failure metric은 있지만, 공통 event schema로 recovery 시도·비용·post-recovery progress를 cross-suite 비교할 수 없다.
- **검증 범위 (`R-M-C-O-T-S`):** long-horizon manipulation/VLA / shared event logger·perturbation wrapper / native benchmark metric / stage progress·time-to-failure·recovery·irreversible event / full episode after first failure / at least two of CALVIN·LIBERO·FurnitureBench.
- **도출 근거:** `EV+MC / B+N`. custom termination과 taxonomy가 평가를 benchmark 내부로 편향시키고 final success는 recovery quality에 간접적이다.
- **읽은 뒤 판정 — `narrowed`:** 모든 benchmark가 final success만 쓰는 것은 아니다. FurnitureBench는 average completed phases와 skill별 success를, BEHAVIOR-1K는 policy/planning/grasp/place/detection failure를 구분한다. VLA-Arena는 Safety·Distractor·Extrapolation·Long Horizon의 170개 task를 공개해 stress axis를 넓혔다. 남은 gap은 이 진단이 **benchmark별 custom taxonomy에 머물고 recovery 이후 실행을 공통 방식으로 평가하지 못한다는 점**이다.
- **반복된 failure/가정:** clean reset과 benchmark 고유 termination rule이 real deployment를 대표한다고 본다. AtomicVLA는 CALVIN이 failure 후 recovery를 해도 후속 task 실행을 막아 실제 recovery capability를 과소평가할 수 있다고 지적한다.
- **부족한 평가:** 표준 perturbation, event timestamp, recovery budget, intervention cost, irreversible failure, post-recovery progress의 cross-suite schema가 없다.
- **연결되지 않은 축:** VLA benchmark ↔ failure detector ↔ recovery policy ↔ event log ↔ dataset curation.
- **최소 반증 실험:** FurnitureBench/CALVIN/LIBERO 중 두 suite에 같은 occlusion, displacement, sensor dropout, instruction correction wrapper를 적용한다. final success 외에 stage progress, time-to-failure, recovery attempts, irreversible event를 공통 schema로 기록한다.
- **Full-text support:** FurnitureBench Sec. V-D/Sec. VI — skill·phase progress와 initialization randomness; BEHAVIOR-1K Sec. 6–7/App. G — real/sim failure taxonomy; AtomicVLA Sec. 4.2 — benchmark termination이 recovered rollout을 반영하지 못하는 사례.
- **Anchors:** [FurnitureBench](../2023/RSS/2023_RSS_FurnitureBench-Reproducible-Real-World-Benchmark-for-Long/01_overview.md), [BEHAVIOR-1K](../2022/CoRL/2022_CoRL_BEHAVIOR-1K-A-Benchmark-for-Embodied-AI-with-1000-Everyday/01_overview.md), [HumanoidBench](../2024/RSS/2024_RSS_HumanoidBench-Simulated-Humanoid-Benchmark-for-Whole-Body/01_overview.md), [AtomicVLA](../2026/CVPR/2026_CVPR_AtomicVLA-Unlocking-the-Potential-of-Atomic-Skill-Learning/01_overview.md), [VLA-Arena](../2026/ICML/2026_ICML_VLA-Arena-An-Open-Source-Framework-for-Benchmarking-Vision/01_overview.md), [RLBench](../2020/RA-L/2020_RA-L_RLBench-The-Robot-Learning-Benchmark-and-Learning-Environm/01_overview.md).

## G-11. Human motion prior와 contact feasibility의 충돌

- **Gap claim:** human pose similarity를 높이는 retargeting이 robot morphology·torque·contact·runtime safety 제약 아래에서 task-feasible motion을 만든다고 보장할 수 없다.
- **검증 범위 (`R-M-C-O-T-S`):** humanoid morphologies / dynamics·contact-aware retargeting / kinematic-only·feasibility filter / task success·fall·torque/contact violation·coverage / clip-to-long-horizon execution / simulation plus selected hardware validation.
- **도출 근거:** `TA+AK / I+N`. 개별 system의 stabilization 증거는 있지만 morphology별 feasibility 전이와 rejected-motion outcome 증거가 부족하다.
- **읽은 뒤 판정 — `strengthened`:** DeepMimic은 retargeted motion을 physics policy로 안정화하지만 phase synchronization, morphology별 PD tuning, manual similarity reward가 필요하다. HumanPlus는 fixed retarget mapping과 humanoid의 적은 DoF 때문에 인간 motion의 일부만 재현할 수 있다고 명시한다. OmniH2O는 infeasible retargeted motion을 filtering하고도 extreme disturbance/OOD goal에 safety guarantee가 없다.
- **반복된 failure/가정:** human pose similarity와 kinematic retargeting이 robot torque, balance, contact, visibility까지 대변한다고 본다. hardware DoF, root odometry, pose-estimation occlusion이 reference 품질과 실행 가능성을 동시에 바꾼다.
- **부족한 데이터·평가:** human reference, retargeted trajectory, feasibility label, rejected motion, real execution outcome이 정렬된 dataset과 contact/torque violation metric이 부족하다.
- **연결되지 않은 축:** motion prior ↔ contact-aware retargeting ↔ system identification ↔ residual control ↔ runtime safety filter.
- **최소 반증 실험:** 같은 motion set에 kinematic-only, feasibility-filtered, dynamics-optimized retargeting을 적용한다. tracking reward와 task reward를 분리하고 success, fall, torque/contact violation, rejected-motion coverage를 측정한다.
- **Full-text support:** DeepMimic Sec. 10.3–11 — retargeting과 phase/PD/reward 한계; HumanPlus Sec. 8.2/Sec. 10 — recovery와 fixed mapping/DoF/occlusion 한계; OmniH2O Sec. 3/Fig. 3/Sec. 5 — infeasible-motion filter와 safety·odometry 한계.
- **Anchors:** [DeepMimic](../2018/TOG-SIGGRAPH/2018_TOG-SIGGRAPH_DeepMimic-Example-Guided-Deep-Reinforcement-Learning-of-Ph/01_overview.md), [HumanPlus](../2024/CoRL/2024_CoRL_HumanPlus-Humanoid-Shadowing-and-Imitation-from-Humans/01_overview.md), [OmniH2O](../2024/CoRL/2024_CoRL_OmniH2O-Universal-and-Dexterous-Human-to-Humanoid-Whole-Bo/01_overview.md), [ASAP](../2025/RSS/2025_RSS_ASAP-Aligning-Simulation-and-Real-World-Physics-for-Learni/01_overview.md).

## G-12. Data scale와 data coverage의 혼동

- **Gap claim:** trajectory count나 scene diversity 하나로는 task×embodiment×sensor×operator×outcome coverage와 worst-group generalization을 설명할 수 없다.
- **검증 범위 (`R-M-C-O-T-S`):** multi-embodiment robot data / coverage-aware subset·scaling / equal-budget random·single-axis-balanced subset / average·worst-group·new-embodiment·recovery / training scale curve / OXE/DROID-style heterogeneous metadata.
- **도출 근거:** `CE+MC / C+N`. diversity 효과는 있지만 단일 hardware·task 결과와 cross-embodiment claim의 consistency가 알려지지 않았고, trajectory count는 condition coverage에 간접적이다.
- **읽은 뒤 판정 — `narrowed`:** “trajectory 수만 늘리면 된다”는 가설은 Data Scaling Laws가 직접 약화시켰다. 4개 real-world task에서 environment/object diversity가 demonstrations-per-condition보다 중요했고 후자는 일정 수준 뒤 포화됐다. 다만 이 결과는 single-task, 한 collection interface/policy family, 네 task에 한정된다.
- **반복된 failure/가정:** environment/object diversity가 task, embodiment, sensor, operator, failure coverage를 대표한다고 본다. DROID는 564 scenes·86 tasks로 넓지만 같은 Franka hardware stack을 쓰며, unsuccessful 16k를 공개하면서도 주 policy 학습은 successful subset을 사용한다.
- **부족한 평가:** task × embodiment × sensor × operator × outcome coverage와 worst-group performance를 동시에 공개하는 표준과 cross-embodiment scaling law가 부족하다.
- **연결되지 않은 축:** empirical scaling law ↔ coverage-aware subset selection ↔ cross-embodiment adapter ↔ failure-aware curation ↔ worst-group evaluation.
- **최소 반증 실험:** 같은 trajectory budget에서 random, environment/object-balanced, embodiment-balanced, failure-aware subset을 뽑아 동일 generalist policy를 학습한다. 평균 success와 함께 worst-group·new-embodiment·failure-recovery 성능을 보고한다.
- **Full-text support:** Data Scaling Laws Sec. 4–7 — diversity scaling, demonstration saturation, four-task/single-policy limitation; DROID Sec. III/Sec. V — scene diversity 통제 실험, same-hardware scope, success/failure composition.
- **Anchors:** [Data Scaling Laws](../2025/ICLR/2025_ICLR_Data-Scaling-Laws-in-Imitation-Learning-for-Robotic-Manipu/01_overview.md), [DROID](../2024/RSS/2024_RSS_DROID-A-Large-Scale-In-The-Wild-Robot-Manipulation-Dataset/01_overview.md), [Open X-Embodiment](../2024/ICRA/2024_ICRA_Open-X-Embodiment-Robotic-Learning-Datasets-and-RT-X-Model/01_overview.md), [Octo](../2024/RSS/2024_RSS_Octo-An-Open-Source-Generalist-Robot-Policy/01_overview.md), [π0.5](../2025/CoRL/2025_CoRL_pi0.5-a-Vision-Language-Action-Model-with-Open-World-Gener/01_overview.md).

## G-13. Active perception의 비용 대비 control value

- **Gap claim:** additional view의 geometric information gain이 언제 action decision을 바꾸어 sensing·camera motion·collision risk 비용을 상쇄하는지를 판단하는 stopping rule이 부족하다.
- **검증 범위 (`R-M-C-O-T-S`):** active-camera manipulator / action-value or disagreement stopping / fixed view·geometry entropy·fixed-view-count / success gain per second·travel·collision·unnecessary view / pre-action and mid-task view acquisition / occluded grasp·articulation with physical camera budget.
- **도출 근거:** `AK+EV / I+N`. virtual active-view 이득은 있지만 physical camera cost와 policy-level stopping에 대한 증거가 부족하고, geometry gain은 action value에 간접적이다.
- **읽은 뒤 판정 — `partially addressed`:** ActiveVLA는 이 trade-off를 처음부터 일부 계량한다. fixed view 87.6%/0.26초 대비 view selection+zoom은 91.8%/0.53초였고, 세 view 이후 성능이 포화되며 compute가 증가했다. AVA-VLA는 recurrent state와 active visual attention을 POMDP 설정에 결합해 state-side counter-evidence를 추가한다. 따라서 active perception의 가치가 없다는 문제가 아니라 **어떤 순간에 추가 관측 비용을 지불할지 결정하는 policy-level criterion**과 physical camera budget이 남는다.
- **반복된 failure/가정:** geometry/visibility gain이 action decision gain과 같다고 본다. Where2Act는 single snapshot ambiguity를 명시하고, FlowBot3D는 occlusion 때문에 flow prediction이 틀릴 때 multi-view/temporal filtering을 제안하지만 실제 view acquisition cost는 최적화하지 않는다.
- **부족한 평가:** sensing latency, physical camera travel, view-switch disturbance, head–arm coordination, collision risk와 task success를 하나의 budget 아래 비교하는 protocol이 부족하다. ActiveVLA의 virtual re-rendering cost는 physical camera motion cost와 다르다.
- **연결되지 않은 축:** geometric uncertainty ↔ expected action change/value of information ↔ view planning ↔ active camera control ↔ manipulation policy.
- **최소 반증 실험:** fixed-view, geometry-entropy, predicted-action-disagreement, learned value-of-information criterion을 같은 view/time/travel budget에서 비교한다. success gain per second, collision, unnecessary view rate를 측정한다.
- **Full-text support:** ActiveVLA Sec. 4.2/Table 4/Fig. 5 — success–latency·view-count trade-off; Where2Act Sec. 6 — single-frame ambiguity; FlowBot3D Sec. IV-B/Sec. V — robot occlusion failure와 multi-view 제안.
- **Anchors:** [ActiveVLA](../2026/CVPR/2026_CVPR_ActiveVLA-Injecting-Active-Perception-into-Vision-Language/01_overview.md), [AVA-VLA](../2026/CVPR/2026_CVPR_AVA-VLA-Improving-Vision-Language-Action-Models-with-Activ/01_overview.md), [Where2Act](../2021/ICCV/2021_ICCV_Where2Act-From-Pixels-to-Actions-for-Articulated-3D-Object/01_overview.md), [FlowBot3D](../2022/RSS/2022_RSS_FlowBot3D-Learning-3D-Articulation-Flow-to-Manipulate-Arti/01_overview.md).

## Evidence audit ledger

아래 표는 이번 갱신에서 실제로 원문 위치를 확인한 범위를 요약한다. `FULL TEXT`는 abstract만이 아니라 본문·표·failure/limitation을 확인했다는 뜻이다. 이 표는 사용자의 reading tracker를 대신하지 않는다.

| Gap | FULL TEXT 확인 논문 | 확인한 핵심 위치 |
|---|---|---|
| G-01 | AT-VLA; ForceVLA2 | Sec. 4.4.1/Table 3; Sec. 5/Table 1–3 |
| G-02 | Recovery RL; SAFE; FLARE | Sec. II–III/VI; Sec. 6.4/7/App. F.3; Sec. 3–4 |
| G-03 | FlowBot3D; ActiveVLA | Sec. IV-B/V; Sec. 4.2/Table 4/Fig. 5 |
| G-04 | MomaGraph; SOMA | Sec. 4.3/6.4; App. D.7–D.8/Table 14–15 |
| G-05 | Binding Touch; RoboPack; Tactile-Driven | Sec. 5/Table 8; Sec. VI; Sec. V–VI/Table IV |
| G-06 | CQL; IQL; DROID | Sec. 1/7; Sec. 1/6; Sec. III-B/V |
| G-07 | Unified World Models; WorldGym; WMPO | Sec. IV-B; Sec. 4.1–4.3; App. C |
| G-08 | MOPO; WMPO | Sec. 5–6/Table 3; Sec. 4.5/App. C–D |
| G-09 | Whole-Body NMPC; Mobile ALOHA; HumanoidBench | Sec. IV–V; Sec. 6.2/9; Sec. V-E |
| G-10 | FurnitureBench; BEHAVIOR-1K; AtomicVLA | Sec. V-D/VI; Sec. 6–7/App. G; Sec. 4.2 |
| G-11 | DeepMimic; HumanPlus; OmniH2O | Sec. 10.3–11; Sec. 8.2/10; Sec. 3/5 |
| G-12 | Data Scaling Laws; DROID | Sec. 4–7; Sec. III/V |
| G-13 | ActiveVLA; Where2Act; FlowBot3D | Sec. 4.2; Sec. 6; Sec. IV-B/V |

이번 갱신의 새 논문은 아래처럼 official abstract/proceedings까지만 확인했다. full-text 확인 전에는 기존 `READING-SUPPORTED` 판정을 대체하지 않는다.

| Frontier delta | Official source에서 확인한 범위 |
|---|---|
| FLARE | CVPR 2026 abstract의 perturbation/bridging, Retry/Reset, MLLM monitor |
| VLA-FixBench/FaultEval | ICML 2026 listing/project의 fault taxonomy, rollback recovery, LIBERO·real-robot evaluation cue |
| VLA-Arena | ICML 2026 project의 170 tasks와 Safety/Distractor/Extrapolation/Long Horizon axes |
| Tabero | arXiv/GitHub abstract의 tactile benchmark, decoupled force-position interface, force-quality metrics |
| TD calibration | arXiv abstract의 sequential calibration과 TD/value connection |
| AVA-VLA | CVPR 2026 abstract의 recurrent state와 active visual attention framing |
| TactAlign / Memory Retrieval / DexterityGen | RSS 2026 official program abstracts의 cross-embodiment tactile alignment, sparse long-horizon retrieval, RL-primitives + teleoperation controller |

## Gap 갱신 규칙

후보를 active gap으로 유지하려면 다음 survival gate를 모두 통과해야 한다.

1. 주제가 아닌 하나의 검증 가능한 `Gap claim`이 있다.
2. gap class와 evidence reason이 분리되어 있다.
3. `R-M-C-O-T-S`의 비교 범위가 있다.
4. 최소 두 개의 독립 method family 또는 multi-system benchmark의 source location이 있다.
5. 지지 근거뿐 아니라 counter-evidence와 이미 해결된 boundary가 있다.
6. 핵심 claim을 유지·축소·기각할 수 있는 최소 반증 실험이 있다.
7. 기존 macro/sub-gap과 실질적으로 중복되지 않는다.

통과하지 못한 항목은 `CANDIDATE QUESTION`으로 내리고 active index에 두지 않는다. 현재 G-01–G-13은 이 기준을 통과했지만, `READING-SUPPORTED`가 바로 실제 gap의 존재 증명을 뜻하는 것은 아니다.

논문을 추가로 정독하거나 실험을 재현할 때 각 gap에 다음을 기록한다.

1. 기존 판정이 `strengthened`, `partially addressed`, `narrowed`, `rejected` 중 어떻게 변했는가.
2. paper-supported evidence의 section/table/figure 위치는 어디인가.
3. 해결된 조건과 아직 남은 boundary는 무엇인가.
4. 기존 최소 실험으로 핵심 가설을 여전히 반증할 수 있는가.

Gap은 “논문이 적다”가 아니라 **현재 방법이 어떤 조건에서 실패하고 어떤 실험으로 반증 가능한가**로 유지한다. `EXPERIMENT-SUPPORTED` 승격에는 재현 환경, seed/trial 수, baseline, metric, 결과가 필요하다.

### Priority criteria

- **Impact:** closed-loop task success, contact safety, recovery, deployment에 줄 수 있는 영향
- **Evidence deficit:** 단순한 소수 논문보다 inconsistent·biased·indirect evidence의 정도
- **Decision value:** negative result도 현재 설계 선택을 바꿀 수 있는지
- **Feasibility:** existing policy, dataset, simulator, robot으로 핵심 claim을 먼저 검사할 수 있는지
- **Strategic fit:** robotics-first 폐루프에 속하며 VLA·3D가 control 성능으로 연결되는지

`P1/P2`는 중요도 등급이 아니라 **첫 decision experiment의 dependency**를 나타낸다. 중요해도 신규 hardware·dataset·benchmark가 필요하면 P2로 둔다.

## External source audit

### Research-gap methodology

- [AHRQ — Frameworks for Determining Research Gaps During Systematic Reviews](https://effectivehealthcare.ahrq.gov/sites/default/files/pdf/methods-future-research-steps-framework_research.pdf): gap의 원인을 insufficient/imprecise, biased, inconsistent/unknown, not-right information으로 나누고 PICOS로 범위를 정의하는 근거.
- [Müller-Bloch & Kranz — A Framework for Rigorously Identifying Research Gaps](https://aisel.aisnet.org/icis2015/proceedings/ResearchMethods/2/): qualitative review에서 localization, characterization, verification, presentation을 분리한 근거.
- [Sandberg & Alvesson — Generating Research Questions Through Problematization](https://journals.aom.org/doi/abs/10.5465/amr.2009.0188): gap spotting만이 아니라 기존 문헌의 공유 가정을 도전하는 질문을 만들기 위한 근거.
- [Campbell Collaboration — Evidence and Gap Map Guidance](https://journals.sagepub.com/doi/full/10.1002/cl2.1125): 사전 범위, comprehensive/mutually exclusive category, coding dictionary, 소수의 큰 gap, critical appraisal를 채택한 근거.
- [PRISMA 2020](https://www.prisma-statement.org/): 검색·screening·보고의 투명성을 위한 참조다. PRISMA는 gap 발견 algorithm이 아니며, 이 문서를 systematic review로 표방하는 근거로 쓰지 않는다.
- [IEEE RAS Technical Committee on Performance Evaluation and Benchmarking](https://www.ieee-ras.org/performance-evaluation/activities/): robotics gap을 measurable·replicable experimental protocol로 연결하는 분야 내 근거.

### Frontier paper status

2026 frontier의 venue/status와 abstract-level claim은 2026-08-24에 아래 primary source로 재검증했다. 본문의 세부 판단은 위 ledger의 full text에서 가져왔고, 이번 delta는 별도 abstract-only 표기로 유지한다.

- [MomaGraph — ICLR 2026 / OpenReview](https://openreview.net/forum?id=3eTr9dGwJv)
- [Spatial Memory for Out-of-Vision Manipulation — ICML 2026 / OpenReview](https://openreview.net/forum?id=5i888dLp8N)
- [WorldGym — ICLR 2026](https://iclr.cc/virtual/2026/poster/10008029)
- [WMPO — ICLR 2026](https://iclr.cc/virtual/2026/poster/10007263)
- [ForceVLA2 — CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.html)
- [AT-VLA — CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.html)
- [ActiveVLA — CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.html)
- [AtomicVLA — CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_AtomicVLA_Unlocking_the_Potential_of_Atomic_Skill_Learning_in_Robots_CVPR_2026_paper.html)
- [FLARE — CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_FLARE_A_Failure-Aware_Framework_for_Autonomous_Correction_and_Recovery_in_CVPR_2026_paper.html)
- [VLA-Arena — ICML 2026](https://vla-arena.github.io/)
- [Tabero — arXiv / code](https://arxiv.org/abs/2605.27886), [GitHub](https://github.com/NathanWu7/Tabero)
- [Temporal Difference Calibration — arXiv](https://arxiv.org/abs/2604.20472)
- [AVA-VLA — CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention_CVPR_2026_paper.html)
- [TactAlign — RSS 2026](https://roboticsconference.org/program/papers/6/)
- [Memory Retrieval in Visuomotor Policies — RSS 2026](https://roboticsconference.org/program/papers/10/)
- [DexterityGen — RSS 2026](https://roboticsconference.org/2026/program/papers/103/)
