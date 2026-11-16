# GAP-WM1 — VLA 행동 후보 선택에서 world model을 얼마나 믿을 수 있는가?

- 검토일: 2026-10-23 KST. 문헌·공개 source 정적 검토 완료; 실험 미실행.
- 판정: **일반 후보 선택 방법은 NO-GO / 조건부 선택 오류 진단은 REVISE·HOLD**. 새 연구 GO나 분야 전체의 해결을 뜻하지 않는다.
- Canonical 질문: [GAP-WM](../../synthesis/05_world_models_safety.md#gap-wm-2026). [Source·revision ledger](../sources/world_model_selection_review_2026-10-23.json).
- C4/C6의 reward·checkpoint 평가, E2의 실행 시점 연구를 재개하거나 이름을 바꾼 제안이 아니다. 사용자 읽기 상태와 기존 후보 판정은 유지한다.

## 1. 결론과 조사 범위

**“World model로 VLA 후보를 평가하고 어려운 상태에서 더 많이 샘플링한다”는 방법은 이미 직접 선행이 있다.** VeriVLA는 이 조합을 제안하고, Cosmos Policy는 action·future·value를 결합한 계획을 수행한다. 고정 policy의 평가를 실제 실행과 비교하는 연구와 planner의 모델 오류 악용 연구도 존재한다. 새 verifier부터 구현할 근거는 부족하다. [VeriVLA §3](https://arxiv.org/html/2610.21985v1), [Cosmos Policy](https://iclr.cc/virtual/2026/poster/10006732), [Planner overfitting](https://arxiv.org/abs/1812.01129).

남기는 질문은 **고정된 후보 분포에서 보정한 평가기가, 후보 수·후보 생성 방식이 달라져 자신에게 유리한 후보를 선택한 뒤에도 신뢰할 수 있는가**다. 이 현상의 존재만으로 기여가 되지는 않는다. 어떤 조건에서 나타나고, 관측 가능한 신호가 새로운 task·proposal 방식에서도 실패를 예측하며, 단순 보수적 대안 이후 무엇이 남는지 보여야 한다. 이는 연구자 가설이며 실제 역전·성능 이득은 확인하지 않았다.

2024–2026 공식 발표 7편, 최신 preprint 4편, 이전 계보 2편을 대조했다. 그중 직접 경쟁 5편은 **지정 본문/부록 구간**을 확인했고 나머지는 공식 abstract/project 수준이다. 세 repository의 고정 revision에서 10개 source/doc 파일을 정적으로 읽었다. 전체 논문 정독·전체 구현 감사·모든 venue의 완전 탐색을 뜻하지 않는다. Registry의 Cosmos Policy·RoboDreamer·Unified World Models를 외부 직접 선행과 연결했다. 이번에는 신규 논문 등록을 하지 않았다.

## 2. 문헌 집합과 확인 깊이

| ID | 논문·공식 status | 확인 범위 | 이 질문에서의 역할 |
|---|---|---|---|
| WM01 | [RoboDreamer: Learning Compositional World Models for Robot Imagination](https://proceedings.mlr.press/v235/zhou24f.html), ICML 2024 | 공식 abstract | 구성적 robot imagination 계보; 모든 action-conditioned verifier와 같은 interface로 취급하지 않음 |
| WM02 | [Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets](https://www.roboticsproceedings.org/rss21/p015.html), RSS 2025 | 공식 abstract | Action/video의 결합과 다중 사용 방식; registry pr-0701 |
| WM03 | [General agents need world models](https://proceedings.mlr.press/v267/richens25a.html), ICML 2025 | 공식 abstract | General policy의 예측 지식과 explicit video generator의 필요성을 구별 |
| WM04 | [Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning](https://iclr.cc/virtual/2026/poster/10006732), ICLR 2026 | [arXiv v1 §4.3·5.3·6·App A.4.2](https://arxiv.org/html/2601.16163v1), 공식 code 지정 경로 | 가장 가까운 action/future/value planning baseline; registry pr-0689 |
| WM05 | [Scaling Robot Policy Evaluation via Discrete Diffusion World Model](https://proceedings.mlr.press/v306/li26hi.html), ICML 2026, dWorldEval | 최종 metadata·abstract; [preprint v1 §4.2.3·4.3](https://arxiv.org/html/2604.22152v1) | Policy ranking과 자동 성공 평가. **최종 제목/저자 목록과 preprint 구분; 최종 PDF 본문 대조는 미실시** |
| WM06 | [Benchmarking World-Model Learning with Environment-Level Queries](https://proceedings.mlr.press/v306/warrier26a.html), ICML 2026 | 공식 abstract | WorldTest/AutumnBench: rollout 유사도 밖의 질문; VLA contact 결과로 일반화하지 않음 |
| WM07 | [Parallel Stochastic Gradient-Based Planning for World Models](https://proceedings.mlr.press/v306/psenka26a.html), ICML 2026 | 공식 abstract | Planner 계보. VLA verifier에 바로 연결 가능한 구현이라고 판정하지 않음 |
| WM08 | [VeriVLA: Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Models](https://arxiv.org/html/2610.21985v1), 2026 preprint | §3·4.4·5, App B·C·D.2; 공개 verifier | Adaptive candidate verification의 직접 충돌 |
| WM09 | [DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training](https://arxiv.org/html/2610.12468v1), 2026 preprint | §3.4·4.4·5, App C.1–2; 공개 README 3개 | Action fidelity·정책 outcome 평가; recorded-action 조건의 경계 |
| WM10 | [Imperfect World Models are Exploitable](https://arxiv.org/html/2605.15960v2), 2026 preprint | §2.2·3.3–3.4·5 | 순위 역전·safe horizon 이론. 공식 acceptance는 확인하지 못함 |
| WM11 | [τ₀-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation](https://arxiv.org/abs/2608.16885), 2026 preprint | abstract·[project](https://tau0-vla.github.io/) | 상위 subtask 탐색과 하위 action-chunk 선택을 구별 |
| WM12 | [The Value Equivalence Principle for Model-Based Reinforcement Learning](https://papers.nips.cc/paper/2020/hash/3bb585ea00014b0e3ebe4c6dd165a358-Abstract.html), NeurIPS 2020 | 공식 abstract | 어떤 policy/value-function 집합에 대해 모델이 충분한지의 계보 |
| WM13 | [Mitigating Planner Overfitting in Model-Based Reinforcement Learning](https://arxiv.org/abs/1812.01129), 2018 preprint / v2 2020 | arXiv abstract·버전 | Planner가 모델 오류를 악용한다는 기존 설명; venue 추정 안 함 |

## 3. 가장 가까운 선행에서 확인한 경계

| 선행 | 논문이 직접 다루는 것 | 이번 질문에서 구별할 것 |
|---|---|---|
| Cosmos Policy | Rollout으로 보정한 모델·value를 사용하고, action 후보마다 여러 future/value를 집계한다. §5.3은 직접 Q 평가와도 비교한다. | Joint world-action model과 frozen VLA+외부 verifier는 다른 조건이다. 후보 수만 같아도 계산·rollout 데이터 예산은 같지 않다. |
| VeriVLA | 두 샘플의 변화/분산으로 trigger를 만들고 latent future와 progress로 action chunk를 선택한다. | Trigger가 training-free라는 설명을 verifier 전체의 무학습으로 읽지 않는다. App C의 critical-state proxy/AUC는 추가 계산의 인과적 이득 oracle이 아니다. |
| dWorldEval | 생성 rollout의 success와 여러 policy의 순위를 benchmark 실행과 비교한다. | 고정 policy 집합의 ranking 성과를 후보 탐색 후 선택 오류의 보장으로 사용할 수 없다. 이는 후속 질문이며 논문의 결함을 입증한 것이 아니다. |
| DreamTrue | App C.2는 4개 policy가 60개 조건에서 실행한 **240개 완성 action trajectory**를 조건으로 비디오 outcome을 비교한다. | 기록된 action을 재생성하는 평가와 모델 안에서 정책을 폐루프로 실행하는 평가, 같은 상태에서 모든 대안의 실제 결과를 얻는 평가는 다르다. |
| Imperfect World Models | 모델과 환경의 policy 선호 역전, 큰 policy 집합의 exploitation, 완화된 safe horizon을 분석한다. | Finite MDP·policy 집합 조건을 확인해야 한다. 최대 transition TV 오차를 pixel/latent error로 대체하거나, 유한 VLA 후보에서 오류가 필연적·단조 증가한다고 결론낼 수 없다. |

위 판단의 근거는 각각 WM04의 §4.3·5.3, WM08의 §3·App C, WM05 preprint의 §4.2.3·4.3, WM09의 App C.2, WM10의 §3.4·5다. Source URL은 위 표와 ledger에 고정했다. Figure만 보고 native 효과나 오류 원인을 추론하지 않았다.

## 4. 공개 interface와 실행 가능성의 경계

| 고정 repository revision | 확인 결과 | 아직 확인하지 않은 것 |
|---|---|---|
| [Cosmos `18a2acc`](https://github.com/NVlabs/cosmos-policy/tree/18a2accadf4e7a3531e56754102af5a24d2316da) | `cosmos_utils.py:780–818`에 mean·LCB·success-vote·majority-mean 집계가 이미 존재한다. LCB는 mean−std(β=1). Planning model 분기와 query 결과 보존 옵션도 확인했다. | 전체 server의 선택 경로·checkpoint와 controller 일치·native 실행은 미검증. LCB 구현의 존재는 calibration 보장이 아님 |
| [VeriVLA `f95ab14`](https://github.com/shirley430316/VeriVLA/tree/f95ab142d6b5b247b47b36137352eb6289dd86a7) | `verifier.py:41–85`에서 subchunk progress 합으로 후보를 rank한다. README checklist와 tree는 model 구조 공개, training·LIBERO/Robotwin·real-robot integration 미완료를 표시한다. | 실제 caller와 state 입력의 시점/provenance, trigger 연결·native action 실행을 확인하지 못함. Release가 일부라고 문헌 충돌이 사라지는 것은 아님 |
| [DreamTrue `991e296`](https://github.com/brave-eai/DreamTrue/tree/991e2963c015be9c5b7f21695bb82bfaaceffed8) | Model/reward README가 weight·mini data 경로와 향후 full data/annotation 공개를 안내한다. | Data payload·runtime code·모든 후보의 paired native outcome은 이번에 확인하지 않음. “공개 자료가 없다”는 전면적 부정은 하지 않음 |

문헌의 하드웨어/latency 수치는 저자 보고값이며 현재 컴퓨터에서 측정하지 않았다. Cosmos의 병렬 planning 실험과 README의 serial 최소 메모리를 같은 실행 조건으로 쓰지 않는다. VeriVLA의 추가 sampling/verification 시간과 trigger·base policy를 포함한 전체 시간도 분리해야 한다. **GPU 확보만으로 아래 비교 구성이 완성되지는 않는다.**

## 5. 남기는 질문과 최소 비교 계약 초안

**RQ:** 동일한 frozen VLA·world model·progress scorer에서, calibration 이후 후보 수 또는 proposal 분포를 바꾸면 선택된 action의 오류가 어떻게 변하는가? Policy-visible 신호로 그 변화의 조건을 예측하고, 단순 후보 제한·LCB보다 나은 판단을 할 수 있는가?

**가설 H1 — 아직 미검증:** 평균 candidate 평가 오차가 비슷해도 선택된 후보의 오차는 달라질 수 있으며, 이 차이의 일부는 support·ensemble disagreement·접촉 조건에 따라 예측 가능할 수 있다. 후보 수 증가가 항상 해롭다고 가정하지 않는다. 성공 가능한 후보가 늘어나는 이득과 선택 편향의 손해를 함께 본다.

| 비교 요소 | 고정하거나 분리할 조건 |
|---|---|
| Decision unit | 하나의 observation/history·native simulator/controller state에서 같은 실행 길이의 action chunk 선택. Episode 전체의 checkpoint 비교와 분리 |
| Policy-visible input | 관측·instruction·proprioception/history 및 모델 예측만 허용. Reset state와 실제 counterfactual outcome은 평가 전용 |
| Action set | 우선 frozen VLA에서 얻은 nested candidate pool. 후보 수 K와 noise seed를 기록하고, proposal 변경은 별도 축으로 검토. CEM/gradient는 호환성 확인 전 구현 대상으로 고정하지 않음 |
| Prediction/feedback | 먼저 실행 길이·관측 빈도를 고정하고 예측 horizon만 분리. 정책 재학습·가변 실행 시점을 동시에 바꾸지 않음 |
| Calibration/holdout | Scorer·β·threshold·risk predictor를 calibration split에서 고정. Task/reset 단위로 분할하고 proposal 방식까지 holdout. Test 결과로 경고 threshold를 고르지 않음 |
| 실제 비교 결과 | 동일 상태에서 각 후보를 branch 실행해 얻은 독립 outcome. 초기 진단은 공통 continuation policy를 사용; 이후 closed-loop 방문 상태 변화는 별도 실험 |
| Baseline | 단일/무작위 후보, 작은 K, 단순 최고 score, direct Q/no-dynamics scorer, mean/LCB, action support 제한, 짧은 예측 horizon. 데이터·입력·계산 예산을 맞춤 |
| Cost | Policy 후보 수, WM future 수, value 평가 수, denoising steps, batching·device, wall time, 실제 control gap을 따로 기록. Abstain/stop 비용도 포함 |
| Outcome | 선택 action utility, 유한 후보 집합 내 regret, reference 대비 악화율, ε 이상의 순위 역전, calibration/coverage와 비용. Reset/episode/task 단위 cluster 불확실성 사용 |

이는 **계약 초안**이다. 환경 revision·checkpoint hash·normalizer·controller·reset snapshot·seed 목록·split ID·비용 한도·최소 효과 크기 ε·trial 수가 고정되지 않았으므로 executable manifest가 아니다. Oracle은 후보 집합 안의 reference일 뿐 전역 최적 정책이 아니다. Stochastic outcome에는 반복 또는 paired random seed 설계가 필요하다.

## 6. 경쟁 설명·반증·재개 조건

| 경쟁 설명 | 구분할 대조 | 기각/축소 조건 |
|---|---|---|
| 후보에 좋은 행동이 없음 | 같은 상태의 후보별 실제 outcome으로 selection headroom 확인 | 좋은 후보가 없다면 verifier 문제가 아니므로 proposal competence로 되돌림 |
| Reward/progress 오류 | 실제/생성 future × 독립 outcome 평가/learned scorer를 교차 비교 | 실제 future에서도 scorer가 틀리면 dynamics 단독 원인 주장 중단; native scorer 적용 가능성부터 검증 |
| Action frame·normalizer·controller 불일치 | Native policy의 기존 성공과 chunk 재생을 먼저 대조 | 불일치가 해결되기 전 WM exploitation 결과로 쓰지 않음 |
| 단순 외삽·기존 conservative planning | Support restriction·작은 K·LCB·짧은 horizon·direct Q | 이 대안으로 설명되면 새 방법 중단; 유용한 적용 경계가 있을 때만 진단으로 남김 |
| 추가 계산의 latency | 동일 state의 분기 진단과 실시간 폐루프를 분리 | 실시간 하락만 보이면 selection bias가 아니라 지연 효과로 해석 |
| Holdout 우연·편향 | 새 task/proposal에 calibration 고정 후 검증 | 조건 예측이 전이되지 않으면 일반 진단 주장 축소; 한 실패 사례를 보편적 gap으로 확대하지 않음 |

재개에는 **동일 상태의 후보·모델 점수·독립 native outcome을 연결한 작은 비교 packet**이 필요하다. 저장된 단일 trajectory·video의 외관 품질·policy 평균 순위만으로 대체할 수 없다. 공개 자료와 source가 이 조건을 충족하는지 아직 확보하지 못했다. 향후 simulator branch 실행이 필요하면 사용자 선택 컴퓨터의 로컬 Docker에서만 진행한다.

## 7. Buildup 단계와 현재 결정

| 가이드 단계 | 이번 결과 |
|---|---|
| 0 공백 탐색 | Registry+외부 최근 문헌+과거 planner 계보 대조 완료. 검색은 잠정 종료 |
| 1 해결되면 달라질 일 | 더 많은 WM 계산을 사용할지, 후보/예측 범위를 제한할지 판단하는 것 |
| 2 필요한 문헌 | 13편의 source/status/확인 깊이 기록. 최종 dWorldEval 본문, robust MPC·선택 후 calibration 전체 계보는 미완료 |
| 3 가정·interface 비교 | Joint WAM, 외부 VLA verifier, policy evaluator, recorded-action 평가를 구분 |
| 4 구체 질문 | “WM이 좋다”에서 proposal 변경 후 선택 오류의 조건 예측으로 축소 |
| 5 직접 충돌 | 일반 WM selection·adaptive trigger·LCB·planner overfitting 주장은 신규 주제로 채택하지 않음 |
| 6 주장–증거 | 비교 계약 초안·경쟁 설명·기각 조건 작성; executable artifact 아님 |
| 7 취약 연결 검사 | 공개 source 정적 검사까지만 완료. Paired native packet·실험 결과 미확보 |
| 8 비판과 결정 | 내부 문헌 판단은 REVISE/HOLD. 실제 외부 연구자 피드백 미수행; 단계 8 전체 완료로 표시하지 않음 |

**연구로 발전시킬 가치:** 배포 시 계산을 더 쓰면 언제 도움이 되는지라는 의사결정 가치는 있다. 그러나 현재는 기존 planner overfitting의 VLA 적용을 넘어서는 새 지식이 확보되지 않았다. 같은 문헌을 재집계하거나 복잡한 verifier를 구현하기보다, 새 packet과 경쟁 설명 이후에도 남는 예측을 재개 조건으로 둔다.

다음 비실험 TODO는 아직 본문 심화가 덜 된 [GAP-HRI](../../synthesis/01_planning_control.md#gap-hri-2026)의 **GAP-H1**이다. RCIP·UPS·PARTNR·LLawCo를 중심으로 도움 응답의 지연/오류·상대 능력이 기존 실험에 이미 포함됐는지 먼저 확인한다. 실제 인간의 부담·신뢰를 simulated partner 점수로 대체하지 않는다.

## 8. 유지보수 검증

- 작업 전 registry audit: 오류·경고 0, 1,037편·5,185개 표준 노트.
- 작업 후 compile·tier 재생성·repository audit·diff 검사 통과. Audit 오류·경고 0; 1,037편·집중 읽기 322행·history 47행·표준 노트 5,185개 유지.
- Manifest·registry metadata·tier·active/history tracker 5개 파일의 SHA256이 작업 전과 같다. 기존 dirty 352개 중 의도한 수동 문서 7개만 추가 수정했으며 나머지 345개는 그대로 보존했다. Ledger의 13개 identity·3개 registry 연결·10개 source hash도 확인했다.
- 검토용 임시 source/doc와 API metadata는 저장소 밖에서만 보관 후 삭제했다. 재조회용 URL·commit·SHA256·확인 구간·검증 결과는 source ledger에 남겼다.
- 이번 변경은 문헌 report·ledger·수동 synthesis·guide·navigation·TODO다. 실험, dependency 설치, PDF/model/data 다운로드, registry admission, tier/읽기 상태 승격, Git 게시를 수행하지 않았다.
