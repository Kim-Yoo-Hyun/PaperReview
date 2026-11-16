# GAP-P1 — 반응형 navigation의 안전 보장과 계획 변경 직후의 공백

- 검토일: 2026-10-23 KST. 작업 **DONE**; 일반적인 adaptive calibration·위험 기반 replanning 제안은 **NO-GO**, 아래 전환 구간 진단은 **REVISE / 비교 설계 검토 진행 가능**.
- Canonical 질문: [GAP-PLAN](../../synthesis/01_planning_control.md#gap-plan-2026). [출처·revision·검토 구간·보존 ledger](../sources/reactive_navigation_safety_review_2026-10-23.json).
- 문헌·정적 source 검토다. 실험, 외부 코드 실행, dependency 설치, PDF·데이터·weight 다운로드는 하지 않았다. 신규 방법의 효과·신규성 및 native VLA 실행은 미검증이다.

## 1. 결론과 연구 가치

**“불확실성을 보정하고 위험하면 계획을 바꾼다”는 방향은 이미 강한 직접 선행이 있다.** CoRL 2025 GenSafeNav, NeurIPS 2025 Fb-CP, CoRL 2026 CERT-Replan이 각각 adaptive uncertainty를 이용한 정책, mission risk의 재배분, 위험 기반 mode 교체를 다룬다. Who Moved My Distribution?은 controller가 상대의 분포를 바꾸는 문제까지 직접 다룬다. 단순 결합·명칭 변경은 새 방법으로 추진하지 않는다. [GenSafeNav](https://proceedings.mlr.press/v305/yao25a.html), [Fb-CP](https://papers.nips.cc/paper_files/paper/2025/hash/ee1331338cdf0e4d1055304d875548df-Abstract-Conference.html), [CERT 공식 forum](https://openreview.net/forum?id=xyRbF93MWh), [Who Moved 본문](https://arxiv.org/html/2511.11567v1).

남길 질문은 **로봇의 계획 변경이 상대의 반응을 바꾼 직후, 새 오차 label이 도착하기 전/재보정이 안정되기 전의 위험–진행 손실**이다. 특히 기존 평균 coverage가 양호해도 이 구간에 실패가 집중되는지, 그 현상을 단순 지연·보수적 대기·predictor 오류로 설명할 수 있는지를 구별한다. 이는 연구자 해석이며 아직 관측된 현상이나 새 정리가 아니다.

가치는 조건부로 있다. 기존 방법들의 적용 조건 사이를 검증하는 진단으로 시작할 수 있고, GPU 없이도 비교 계약을 더 구체화할 수 있다. 다만 “모드 전환”·“반응형 보행자” 자체는 새롭지 않다. VLA를 추가하는 이유도 아직 입증하지 못했다. 상태 기반 진단이 유의미한 뒤, 시각/언어 정보가 실제로 다른 계획 선택을 요구하는 경우에만 native VLA로 확장한다. 현재 판정은 큰 학습 GO가 아니다.

## 2. Buildup 절차와 확인 깊이

| 가이드 단계 | 이번 수행 결과 |
|---|---|
| 0–1 공백·문제 범위 | 정적 장애물, 반응 없는 움직임, 로봇에 반응하는 상대를 구별하고 계획 변경 뒤 과도 구간으로 축소 |
| 2–3 문헌·가정·interface | 아래 10편/자료군, 지정 본문 8편, 4개 repository revision·20개 text source/doc/config 대조 |
| 4–5 질문·직접 충돌 | 일반 위험 trigger와 단순 reactive/non-reactive 비교를 제외; transient·지연·내생적 반응의 상호작용을 질문으로 남김 |
| 6 주장–증거 계약 | 보장 단위, 비교 정보, 예산, metric, 기각 규칙을 §5에 작성 |
| 7 가장 약한 고리 | 공개 code의 clock/track 정렬, 반응 경로, VLA waypoint와 물리 control의 연결이 미완성; 정적 확인과 실제 실행을 구별 |
| 8 판정·외부 검토 | 위 조건부 판정. 실제 외부 연구자 피드백·실험은 미수행 |

2024–2026의 직접 관련 9편과 replay 한계를 확인하기 위한 이전 SocNavBench를 대상으로 했다. 모든 학회 전수 조사나 모든 proof의 검증은 아니다. 공식 채택/게재 근거 6편, preprint 3편, 이전 benchmark 1편을 구분한다. 임시 확보한 code/doc 20개 중 12개는 지정 구간을 대조했고 8개는 경로·symbol 확인용 context다. Code revision이 원 논문 실험 revision과 같다는 증거는 없다.

| 연구 | 확인한 status·본문 버전 | 질문에 주는 근거와 경계 |
|---|---|---|
| Towards Generalizable Safety in Crowd Navigation via Conformal Uncertainty Handling | [CoRL 2025](https://proceedings.mlr.press/v305/yao25a.html); [v1 §3–4, App J/M](https://arxiv.org/html/2508.05634v1) | DtACI·CV/GST predictor·PPO-Lagrangian. Main setting은 humans가 robot을 피하지 않음; App J는 visible/invisible 교차 평가까지 포함한다. 단순 반응 여부 비교는 이미 있음 |
| Who Moved My Distribution? Conformal Prediction for Interactive Multi-Agent Systems | [arXiv 2025](https://arxiv.org/abs/2511.11567), 공식 채택 미확인; v1 §2–5/App A 지정 구간 | Interaction trajectory를 다시 수집하는 반복 CP/MPC. Lipschitz·contraction 아래 fixed point; 임의의 비연속 반응·유한 iteration 안정성을 자동 보장하지 않음 |
| Perceive With Confidence: Statistical Safety Assurances for Navigation with Learning-Based Perception | [CoRL 2024, PMLR 출판 2025](https://proceedings.mlr.press/v270/dixit25a.html); [2025 개정 v3 §III–V](https://arxiv.org/html/2403.08185v3) | 새로운 정적 환경과 planner가 방문하는 상태의 분포 변화. 환경별 worst-state cost; 실제 구현의 finite state set 경계가 있다. v3를 원 proceedings와 동일 본문으로 취급하지 않음 |
| Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization | [NeurIPS 2025](https://papers.nips.cc/paper_files/paper/2025/hash/ee1331338cdf0e4d1055304d875548df-Abstract-Conference.html); [v1 §3–5/App G 지정 구간](https://arxiv.org/html/2510.16376v1) | Mission joint risk와 posterior risk 재배분을 이미 다룸. Main analysis의 trajectory exchangeability와 별도 calibration split, App G의 likelihood-ratio weighting을 확인. 임의의 robot-responsive law 변경 보장으로 확장하지 않음 |
| CoCoNav: Conformal Control for Safe Robot Navigation in Crowds | [arXiv 2026](https://arxiv.org/abs/2608.07751), 공식 채택 미확인; [v1 §III–V](https://arxiv.org/html/2608.07751v1) | Delayed horizon별 conformal PI, soft MPC 뒤 nominal/fallback 검증. Missing track와 uncertified action을 별도 항으로 계수. 본문은 acceptance 후 code 공개 예정이라고 명시 |
| Adaptive Risk-Certified Event-Triggered Replanning for Dynamic Navigation (CERT-Replan) | [CoRL 2026 Poster](https://openreview.net/forum?id=xyRbF93MWh), 공식 API의 venue/venueid 확인; [v1 §4–6/App D 지정 구간](https://arxiv.org/html/2610.09302v1) | CVaR 기반 mode 유지/교체가 직접 충돌. Fixed-mode conditional certificate이며 §6은 robot-responsive obstacles가 현재 범위 밖이라고 명시. Hardware의 움직이는 장애물은 virtual injection |
| PopNavShift: Stress-Testing Social Navigation under Behavioral Population Shift | [arXiv 2026](https://arxiv.org/abs/2609.21838), 공식 채택 미확인; [v1 §III–IV/VII](https://arxiv.org/html/2609.21838v1) | 같은 물리 encounter의 population 변화·controller 순위·pedestrian burden 비교도 이미 있음. Synthetic persona→motion mapping은 실제 사람의 인과 반응 자료가 아님 |
| SocialNav: Training Human-Inspired Foundation Model for Socially-Aware Embodied Navigation | Registry **pr-0966**; [CVPR 2026 공식 색인](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.html); [v1 §3–5/App A.4.2](https://arxiv.org/html/2511.21135v1) | VLM brain–action 및 사회 규범 trajectory가 이미 있음. 검토한 v1 benchmark의 pedestrians는 자체 경로를 따름. 공식 URL 직접 열람은 403, CVF 검색 색인으로 status를 확인했으며 최종 PDF와 v1의 동일성을 검증하지 않음 |
| THÖR-MAGNI: A large-scale indoor motion capture recording of human movement and robot interaction | [IJRR 44(4), 2025; online 2024-10-21](https://journals.sagepub.com/doi/abs/10.1177/02783649241274794); [공식 release v2 protocol](https://zenodo.org/records/13865754) | 실제 robot–human movement, 역할·시나리오·gaze/trajectory가 존재한다. Teleop 동작/communication 조건은 새로운 controller의 반사실 반응을 제공하지 않음. Payload와 시각 정렬은 미검사 |
| SocNavBench: A Grounded Simulation Testing Framework for Evaluating Social Navigation | 이전 계보; [저자 repository](https://github.com/CMU-TBD/SocNavBench), docs 및 replay 구현 | ETH/UCY prerecorded branch와 autonomous branch를 구별. Replay의 collision pause를 양보·회피 반응으로 간주하지 않음 |

## 3. 안전 보장의 단위를 구별한 결과

| 종류 | 이 검토에서 확인한 조건 | 이 조건만으로 주장할 수 없는 것 |
|---|---|---|
| GenSafeNav의 uncertainty-aware CRL | Horizon별 실제 오차를 나중에 관측해 보정; 누적 intrusion cost를 학습에 사용 | Cost constraint/coverage가 곧 모든 episode의 무충돌 정리는 아님 |
| Who Moved의 calibration | 독립 interaction trajectory별 시간 최대 오차를 horizon별 score로 사용. CP·deployment map Lipschitz와 상수 곱 < 1 아래 수렴 | 이를 단순 framewise CP라고 낮춰 부르면 틀림. 반대로 finite stopping tolerance만으로 새 급격한 모드 전환 중 보장을 얻었다고 할 수도 없음 |
| PwC의 환경 단위 보장 | 독립 환경과 ground-truth occupancy, policy-independent cost; finite state set/안전 planner 적용 경계 | 움직이는 사람의 새로운 반응 법칙에 대한 안전 보장 |
| Fb-CP의 mission risk | Shrinking horizon에서 joint chance constraint. 계획용과 posterior 추정용 calibration을 분리; shift extension의 가중치 조건 | “기존 CP에는 episode/mission 보장이 없다”는 동기는 부정확. 알려지지 않은 반응 law의 변화도 covariate reweighting으로 해결된다고 가정할 수 없음 |
| CoCoNav의 frequency bound | 실행 첫 control에 대한 clearance violation 빈도; finite-time 항·미검출·미인증 fallback 항을 더함 | 각 순간의 조건부 확률, episode에서 한 번이라도 충돌할 확률, deadlock-free completion 보장 |
| CERT의 conditional horizon risk | 주어진 정보와 고정 후보 mode의 양의 violation loss에 대한 CVaR/union bound | 경험적 tail sample을 true conditional law로 간주하거나 다음 mode가 사람의 law를 바꿔도 같은 certificate를 그대로 적용 |

근거 위치는 §2의 본문 링크와 ledger를 따른다. Step failure 확률을 적절히 확보한 경우에도 episode bound에는 시간/agent에 대한 집계 논리가 필요하다. 반대로 trajectory-max score나 mission constraint를 사용한 선행에는 그 설계를 인정해야 한다. Average coverage·conditional coverage·mission risk·empirical collision·liveness는 서로 다른 결과다.

## 4. 공개 interface·실제 crowd 자료의 충분성

| 고정 revision | 확인한 interface | 남은 경계 |
|---|---|---|
| [GenSafeNav `01baf926`](https://github.com/tasl-lab/GenSafeNav/tree/01baf926a5c77c1a4ab28635658eb014ef4f1767) | `robot.visible=False` default; true이면 `get_human_actions`에 robot state를 넣음. `CrowdSimPred.step`이 human action 및 ACI update를 호출. 0.25 s simulation step, 5-step prediction 설정 | 상태 기반 environment. RGB·language policy interface와 물리 control의 연결은 별도. 설정 변경만으로 pretrained policy의 competence/동등 예산을 보장하지 않음 |
| [SocialNav `b958f068`](https://github.com/AMAP-EAI/SocialNav/tree/b958f0683521a024d14d183593750bddac7f75b5) | README는 training data 미공개와 별도 ABot benchmark를 명시. `citywalker.py`는 영상/waypoint history+goal→waypoint prediction, offline angle metric 경로 | Offline angle은 closed-loop crowd safety가 아님. 배포의 clock·action duration·controller/evaluator와 checkpoint 결합을 검증하지 않음 |
| [SocNavBench `2724ea85`](https://github.com/CMU-TBD/SocNavBench/tree/2724ea85ff22ca61a88ee95285dfc3fa056656c6) | `PrerecordedHuman`은 interpolation한 경로를 실행; optional pause-on-collision. Docs는 autonomous/planned agent도 구별 | 실제 경로의 재생과 counterfactual robot response는 다름. Repository 전체가 nonreactive라는 주장은 하지 않음 |
| [ABot-Navigation `2a0aefb5`](https://github.com/amap-cvlab/ABot-Navigation/tree/2a0aefb56f1e2d315bba924239e9e8ad9dca9d92) | 현재 README는 ABotN-PointBench/POIBench/Short-Horizon OVON을 설명. Point-goal docs는 `reset/predict`, local `[right, front]` waypoint, step count, collision metric을 정의 | SocialNav 논문의 원 benchmark와 현재 release를 동일시하지 않음. Reactive pedestrian·물리 clock·VLA latency를 반영한 실행 경로는 이번 docs에서 확인되지 않음 |

특히 [GenSafeNav의 `Human.update_aci`](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/crowd_sim/envs/utils/human.py#L30-L51)는 history list index를 쓰고, [prediction writer](https://github.com/tasl-lab/GenSafeNav/blob/01baf926a5c77c1a4ab28635658eb014ef4f1767/crowd_sim/envs/crowd_sim_pred_real_gst.py#L85-L113)는 valid prediction만 append하며 radius를 clip한다. **불규칙 누락을 주입하기 전에 issue time–target time–track ID가 맞는지 검증해야 한다.** 이것은 조건부 정적 위험 지적이며, 실제 misalignment나 기존 결과 오류를 재현한 것이 아니다. Infinite/large radius를 clipping하는 구현에 원래의 무제한 threshold 보장을 자동 이식하지 않는다.

THÖR-MAGNI의 scenario 3은 teleoperated moving robot, scenario 4는 speech-only와 speech+gesture/gaze 조건을 제공한다. 실제 상호작용이 전혀 없는 자료라고 배제하면 틀리다. 다만 같은 사람·동일 encounter에서 새 policy의 여러 선택을 비교한 자료인지, 통제 변수·timestamp가 충분한지는 아직 확인하지 않았다. 관측 response association을 새로운 navigation controller의 인과 효과로 치환하지 않는다. [공식 수집 protocol](https://zenodo.org/records/13865754).

Who Moved의 공개 구현은 확인한 paper/author 경로에서 식별하지 못했다. CoCoNav는 본문에 code 공개 예정이라고 쓰고, CERT project의 Code 버튼은 당시 같은 페이지로 돌아갔다. 이는 해당 선행이 없다는 뜻이나 구현이 어디에도 없다는 전수 결론이 아니다. 재구현 시 저자 결과 재현과 paper-inspired baseline을 구분한다.

## 5. 남길 질문과 비교 계약 초안 — 연구자 해석

**RQ:** 관측·predictor·계산 예산이 같은 조건에서, robot policy/route 변경 후의 *반응 의존적인 calibration 회복 지연*이 안전–진행 손실을 추가로 설명하는가? 기존 adaptive CP, 보수적 대기, 단순 risk trigger를 넘어서 그 손실이 나타나는 조건을 예측할 수 있는가?

비교의 중심은 새 알고리즘보다 조건 효과다. Reactive/nonreactive × ego mode 유지/변경 × smooth/switching 상대 반응을 교차한다. 동일 seed만 공유하지 말고 초기 배치·상대 목표·외생 noise를 고정하며, 반응 이후의 궤적은 결과이므로 억지로 같게 만들지 않는다. 별도의 physical delay 조건으로 stale observation 설명을 분리한다.

| 항목 | 고정할 내용·평가 방식 |
|---|---|
| 1차 진단 estimand | 변경 직후 고정 물리 시간 window의 excess violation/near-miss/진행 손실. `(변경−유지)_reactive − (변경−유지)_nonreactive`를 단순 delay·predictor 변경 대조와 함께 봄. 이 차이가 인과적이려면 simulator intervention과 외생 변수를 실제 통제해야 함 |
| Policy-visible input | timestamp가 있는 observation/history, 이미 실행자가 아는 route/mode 변경 event. 미래 반응 label·oracle human mode는 분석용으로만 분리 |
| Action·timing | 먼저 동일 planner의 finite 옵션: 유지, 감속, 대기, 우회. 물리 실행 tick과 재계획 tick, action hold duration, feedback 도착 시점 명시. `stop`도 상대 충돌·제동 거리 때문에 자동 safe로 놓지 않음 |
| 최소 baseline | 동일 predictor+고정 margin/MPC, DtACI 또는 ACP-MPC, deterministic uncertainty threshold/stop·wait·hysteresis, robust MPC. Iterative on-policy calibration 및 CERT/CoCo식 trigger/verification은 단계별 강한 대조로 추가; 원 코드 미확보 baseline은 paper-inspired로 표시 |
| Fairness | Observation·history·option set·horizon·calibration sample 수·재계획 횟수/시간·wall-clock latency를 맞춤. 재수집 trajectory·label 대기 비용도 포함. Predictor frozen 진단과 predictor adaptation을 분리 |
| Metric | 발행 당시 threshold에 대한 horizon/전환 후 window별 coverage, episode any-collision, near miss, timeout, deadlock, goal time, pedestrian delay, uncertified fallback/미검출 빈도. 성공 episode만의 시간을 전체 성능으로 쓰지 않음 |
| Split·통계 | Calibration/validation/test를 trajectory·scene·partner 단위로 분리. 동일 seed의 paired 차이와 episode 단위 interval. 겹치는 frame을 독립 trial 수로 세지 않음. Calibration/threshold 선택은 test 전에 고정 |
| 유의미한 결과 | 단순 보수성 증가와 구별되는 safety–progress 곡선 또는 holdout에서 반복되는 조건 예측. 전환 신호가 단순 residual threshold보다 언제 먼저/정확히 유용한지 검증 |
| 기각·축소 | 반응을 제거해도 동일하면 지연/예측 문제로 축소. 동일 budget의 고정 wait/margin/ACP가 설명하면 새 method 중단. Switch 시점/미래 의도 oracle이 있어야만 효과가 나면 배포 주장 기각. 실제 중요성 없는 인위적 반응 law만으로 인간 안전 주장 금지 |

수작업 사고실험: 전환 전까지 관측 history가 같은 두 상황이 있고, 하나에서만 새 robot route가 사람의 회피 방향을 바꾼다고 하자. 그 반응이 관측되기 전에는 과거 residual만 쓰는 monitor가 둘을 구별할 수 없다. 알려진 ego mode-change event를 사용해도 사람의 미래 반응을 정확히 아는 것은 아니다. 따라서 event-conditioned caution이 단순 고정 대기보다 나은지를 비교해야 한다. **이 예시는 기존 정리의 반례나 실제 측정 결과가 아니다.** Exchangeability·smooth-response 가정이 성립하지 않는 상황에서 보장을 가져오면 안 된다는 설계 점검이다.

## 6. VLA 연결과 자원 판정

VLA가 생성한 waypoint/route와 safety controller가 실행한 action을 나눠 기록한다. 같은 low-level controller에 VLA 후보와 geometric 후보를 연결하고, perception 정보·추론 지연·옵션 수가 같을 때의 차이를 봐야 한다. SocialNav의 사회 규범 이해를 다시 contribution으로 주장하지 않는다. Language/visual cue가 없는 2D state simulator 결과는 VLA 연구 효과가 아니다.

| 범위 | 지금 가능한 일 | 아직 필요한 것 |
|---|---|---|
| 문헌/정적 검토 | 직접 충돌·가정·code 경로 및 비교 계약 작성 완료 | 추가 실행 전 clock/track·반응 경로·split 명세의 고정 |
| 최소 synthetic 진단 | 상태 기반 반응 simulator를 활용할 경로는 있음. Learned VLA 없이 검사하는 설계 가능 | Local Docker runtime qualification, 실제 seed/perturbation/config manifest, 유효한 baseline과 logging. 이번에는 실행 가능성을 시험하지 않음 |
| Native VLA | SocialNav 공개 waypoint inference가 연결 단서 | RGB reactive environment·checkpoint·normalizer·controller·physical time packet, 로컬 Docker와 GPU. Cloud 배포 논문을 따라 원격 실행으로 우회하지 않음 |
| 실제 사람에게 일반화 | THÖR-MAGNI protocol로 관측 항목·상황 범위를 좁힐 수 있음 | Payload 정렬·participant/condition 분석 및 새 policy의 실제 상호작용 평가. GPU 확보만으로 충족되지 않음 |

## 7. 다음 TODO와 종료 기준

후속 [GAP-P2 실행 경로 심사](./REACTIVE_NAVIGATION_EXECUTION_REVIEW_2026-10-23.md)를 완료했다. 아래는 P1 당시 계획이다. 현재 구현의 ABot point-goal 좌표는 `[front,left]`이며 위 docs 기반 `[right,front]`를 실행 계약으로 사용하지 않는다. P2의 `executable=false` manifest와 다음 Docker 계약 검사가 최신 인계다.

**GAP-P2: 비교 가능한 공개 실행 구조의 정적 심사.** GenSafeNav의 실제 등록 env→step→predictor→ACI→evaluator 경로, ABot 현재 release의 physical clock/reactive dynamics, THÖR-MAGNI의 time/track/condition 문서를 대조한다. 결과물은 다음 세 가지다.

1. Synthetic diagnostic과 native VLA를 분리한 비교 계약 및 필요한 필드 목록. Oracle·frame-index 시간 혼동·test leakage를 차단한다.
2. Repo revision·entrypoint·action/observation·clock·calibration unit·metric 정의와 미확정 항목을 가진 **실행 전 manifest**. 아직 실행 불가능하면 `executable=false`를 명시한다.
3. 동일 budget의 단순 대안으로 끝나는지 판단하는 pilot 승인/수정/종료 기준. Paper 수치 재현이나 실제 효과를 사전에 요구하지 않지만, 무엇을 비교하는지는 고정해야 한다.

이 단계도 실험·학습·payload 다운로드는 포함하지 않는다. 공개 구조로 비교가 불가능하면 구현을 크게 늘리지 않고 문헌 진단으로 보존한다. GPU 대기만을 이유로 계속 활성화하지 않는다. 기존 D/E/C 후보의 판정은 바꾸지 않는다.

## 8. 유지보수 검증

신규 등록·tier·사용자 읽기 상태 변경은 없다. `py_compile`, tier 생성, repository audit, `git diff --check` 및 기존 dirty 파일 보존 결과는 source ledger의 `validation`에 기록한다. 임시 HTML·code/doc와 API 응답은 hash/검토 위치만 남기고 삭제한다. Git commit/push는 수행하지 않는다.
