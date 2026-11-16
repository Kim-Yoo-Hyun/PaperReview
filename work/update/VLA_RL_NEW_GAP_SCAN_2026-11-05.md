# 기존 후보 밖에서 다시 찾은 VLA + RL 연구 공백

> 후속 사용자 요청 반영: 현재 판단은 [기존 6개+새 2개 통합 검토](./INTEGRATED_GAP_REVIEW_2026-11-05.md)가 우선한다. 아래 순위·등록/미등록 수는 직전 탐색 당시 기록이다. 후속 작업에서 외부 논문 12편을 등록했으며 VLA-Trace의 공식 EMNLP 게재도 확인했다.

- 조사일: 2026-11-05 KST
- 요청: 현재 찾아 둔 gap과 6개 준비 주제를 반복 검토하는 대신 외부 문헌에서 새 질문을 찾는다.
- 판단: **RL 이후의 피드백 활용 변화**를 첫 탐색 후보로, **독립적으로 학습한 로봇 사이의 협력 일반화**를 두 번째 후보로 남긴다.
- 증거 수준: `CURATION-HYPOTHESIS`. 공백의 존재·방법의 신규성·효과가 확정된 상태는 아니다. 작은 탐색에 들어갈 질문과 강한 대안이 있다는 판단이다.
- [출처·확인 범위 원장](../sources/vla_rl_new_gap_scan_2026-11-05.json) · [활성 TODO](../../TODO.md) · [buildup 기준](../../research/IDEA_BUILDUP_GUIDE.md#nonexperimental-workflow)

## 1. 이번 검색이 기존 후보 검토와 다른 점

먼저 외부의 RL post-training, 해석 가능성, world-model 학습, 다중 로봇 협력, 사람 교정 학습을 검색했다. 이후 registry와 기존 질문을 대조했다. 최종 근거 원장은 **2024–2026년 29편과 오래된 MARL 기반 2편**, 합계 31편이다. 이 중 현재 registry와 일치하는 논문은 10편, 등록되지 않은 외부 논문은 21편이다. 최근 29편만 보면 외부 논문은 19편이다. 이 수는 발견한 모든 검색 결과나 정독 완료 수가 아니다.

최근 공식 근거에는 CoRL·ICML 2024, NeurIPS·CoRL 2025, ICLR·ICML·RSS 2026 proceedings 및 NeurIPS 2026 공식 프로그램이 포함된다. 초점은 manipulation과 협력 mobile manipulation이다. 모든 CVPR/ICCV/ECCV/ICRA/IROS/journal 논문을 전수 확인했다거나 단독 navigation 전체의 공백을 조사했다고 주장하지 않는다. 최신 preprint도 직접 중복을 찾는 데 사용하되 채택 논문과 구별했다. 공식 초록까지만 본 자료와 지정 본문·부록까지 본 자료는 원장의 `review_scope`가 구분한다.

2024 기반은 [OpenVLA](https://proceedings.mlr.press/v270/kim25c.html), [RoboDreamer](https://proceedings.mlr.press/v235/zhou24f.html), [3D-VLA](https://proceedings.mlr.press/v235/zhen24a.html)로 연결했다. 이들을 최근 방법과 경쟁하는 새 결과처럼 취급하지 않는다. OpenVLA는 CoRL 2024 논문이며 PMLR 발행 연도는 2025다.

**출판 상태 주의:** CHORUS는 [저자 project](https://chorus-model.github.io/)와 [연구실](https://iprl.stanford.edu/)이 CoRL 2026 채택을 표시하지만 이번에 학회 자체의 채택 페이지까지 확보하지 못했다. CTRL-STEER의 CVPR 표기는 저자가 보고한 **VisCon workshop**이며 main conference가 아니다. DRILL과 Not All Features는 [NeurIPS 2026 공식 목록](https://neurips.cc/Downloads/2026)에서 제목을 확인했다. 프로그램 등재를 proceedings 출판 완료와 동일하게 쓰지 않는다.

## 2. 후보 비교

| 순서 | 새로운 질문 | 기여가 될 수 있는 지점 | 기존 후보와의 구별 | 주된 부담 |
|---|---|---|---|---|
| 1 | **RL은 VLA가 현재 관측으로 행동을 수정하는 방식을 어떻게 바꾸는가?** | RL의 성공률 증가를 설명하는 조건과 피드백 평가 원리; 필요할 때 표적 학습으로 확장 | residual 재사용·관측 획득·chunk 빈도 조정이 아니라 post-training에 따른 행동 의존성 변화 | 공개 checkpoint로 진단 시작 가능. RL 자체의 인과 효과에는 데이터/학습량을 맞춘 추가 비교 필요 |
| 2 | **함께 학습하지 않은 VLA 로봇끼리도 RL의 협력 이득이 유지되는가?** | 개별 조작 능력과 협력 관습의 과적합을 분리; 다양한 팀원에 대한 학습·평가 | 한 로봇의 navigation→manipulation 정책 교체나 로봇 간 가중치 전이가 아닌 동시 협력 | 두 정책·다중 로봇 환경·팀원 집합 필요. 공개 실행 자산의 적합성 미확인 |
| 이번에는 채택하지 않음 | 좋은 world-model 예측을 실제 VLA 개선으로 연결 | 중요한 분야지만 아래 직접 선행이 핵심 주장을 이미 다룸 | 과거 verifier/WM 선택 주제로 돌아가지 않음 | 새 차이 없이 pipeline만 구성하면 기여가 불명확 |
| 이번에는 채택하지 않음 | 사람 교정·advantage weighting 개선 | 구체적인 남은 추정 대상이 있어야 함 | 기존 reward 검증 후보의 이름 변경을 피함 | 최신 직접 선행 및 실제 intervention 자료 비교 필요 |

순서는 **석사 기간 내 첫 관측을 얻는 부담과 질문의 설명력**에 대한 연구자 판단이다. 채택 확률·성능 점수는 아니다. 두 번째는 다양한 로봇이라는 장기 방향에 더 직접적이지만 첫 번째보다 구현 부담이 크다.

<a id="feedback"></a>

## 3. 1순위: RL post-training 이후의 시각 피드백 활용

### 이미 알려진 것과 남겨 둘 질문

[What Can RL Bring to VLA Generalization?, NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html)은 SFT와 RL의 시각·의미·실행 일반화를 비교하고, **실행 중 물체 이동**도 이미 평가했다. 따라서 “RL이 perturbation에 강한가”, “물체를 옮겨 본다”는 실험 자체는 새 기여가 아니다.

[Not All Features, NeurIPS 2026 프로그램 / v6](https://arxiv.org/pdf/2603.19233v6)의 §4.7–4.8·Appendix B는 activation 주입 시 좌표에 묶인 행동, 경로별 역할, 개입의 한계를 다룬다. **주입한 정책이 좌표를 따른다는 결과를 정상 정책이 항상 관측을 무시한다는 결론으로 바꾸면 안 된다.** 실제로 본문의 비주입 정책은 이동한 물체를 따라간다. 절대 좌표와 장면 상대 좌표의 완전한 구별도 저자가 남긴 한계다.

[Embodied Interpretability, ICML 2026](https://proceedings.mlr.press/v306/zhang26gz.html)은 시각 영역의 개입적 중요도와 nuisance attribution을, [VLA-Trace §3](https://arxiv.org/html/2605.30117v1)은 학습 단계의 표현 변화·attention knockout·입력 교란을 다룬다. [CoRL 2025 steering](https://proceedings.mlr.press/v305/haon25a.html)과 [CTRL-STEER](https://arxiv.org/abs/2606.00269)도 있으므로 “VLA를 해석한다”, “RL로 activation을 조절한다” 자체를 새 방법으로 내세우지 않는다.

**새 탐색 질문:** 같은 작업에서 RL의 실행 개선이 나타날 때, 그 개선은 **목표 관련 상태 변화에 대한 적절한 반응**, **무관한 시각 변화에 대한 둔감성**, **더 나은 기본 운동 행동** 중 무엇과 연결되는가? RL을 거친 정책이 항상 관측을 더 많이 이용해야 한다고 가정하지 않는다. 필요한 변화에는 반응하고 불필요한 변화는 무시하는 구별이 중요하다. 이번에 읽은 직접 선행의 확인 범위에서는 이 분해를 데이터 대조와 함께 충분히 답했는지 확정되지 않았다. 이것이 후속 탐색의 대상이다.

### 판단을 바꿀 작은 비교

1. **출발점:** 동일 계열의 warmup·SFT·RL 공개 checkpoint를 사용한다. [RL4VLA 공식 README](https://github.com/gen-robot/RL4VLA)는 세 checkpoint와 평가 경로를 제공한다. 공개됐다는 사실과 실제 로딩·호환성 검증은 별개다. README의 RL/warmup과 SFT는 normalizer key도 다르므로 각각의 원 설정을 확인하고 **해독된 물리 행동 단위**를 맞춘다.
2. **물리 개입:** 같은 초기 장면에서 (a) 변화 없음, (b) 목표는 유지하면서 대상 위치를 바꿈, (c) 작업에 무관한 배경만 바꿈을 구분한다. 변화는 물리적으로 유효해야 하며 평가지점/시점과 로봇 상태를 기록한다. 기본 조작 능력과 정상 성공률도 같이 보고한다.
3. **정보 개입:** fresh observation과 일정 구간 이전 관측을 재사용하는 조건을 비교한다. 후자는 인위적인 입력 분포 변화이므로 정상/배경 대조를 포함하고 proprio·언어·제어 주기·action horizon을 바꾸지 않는다. 전체 이미지를 가리면 로봇 자신의 상태도 사라질 수 있으므로 이를 순수한 물체 피드백 제거라고 부르지 않는다.
4. **주요 관측:** 최종 성공, 변화 후 첫 유효 수정의 방향/지연, 목표 관련 변화와 배경 변화에 대한 행동 차이. 단순 action 변화량·attention·linear probe만으로 기능적 활용을 입증하지 않는다. 내부 activation 개입은 행동 차이를 확인한 뒤 사용하는 보조 분석이다.
5. **강한 대안:** 같은 RL rollout에서 얻은 성공 데이터 SFT와 return-weighted imitation, 추가 학습량, 더 짧은 action horizon, 단순 관측 augmentation을 분리한다. 초기 공개 checkpoint 비교는 **진단**이며 training data와 예산이 같지 않으면 “RL objective 때문에 생겼다”고 주장하지 않는다.

가능한 행동 지표는 아래 차이다. 이는 새 estimator나 causal mediation 증명이 아니라 사전 해석을 돕는 기술 통계다.

```text
B(policy) =
  [success(physical change, fresh) - success(physical change, stale)]
- [success(no change, fresh)       - success(no change, stale)]

Compare B(RL) with B(SFT), alongside all four success rates
and the nuisance-change controls.
```

Ceiling/floor, stale 입력의 분포 이탈, 서로 다른 방문 상태가 이 차이를 바꿀 수 있다. 따라서 초기 상태 단위 pairing과 uncertainty를 보고하고, 후속 원인 주장에는 동일 상태에서의 행동 대조 및 학습 데이터 대조가 필요하다. 단순히 B가 크면 더 좋은 정책이라는 순위를 만들지 않는다.

### 결과에 따라 연구를 어떻게 발전시킬 것인가

- **RL이 작업 관련 변화에 더 잘 반응하고 데이터 대조 후에도 남음:** 어떤 학습 조건이 그 변화를 만드는지 분석하고, 그 조건을 표적으로 하는 curriculum/학습 절차를 검토한다.
- **성공률은 늘지만 피드백 활용 차이는 작음:** 기본 운동 능력·실패 상태 노출·관측 불변성의 설명을 대조한다. 중요한 기존 해석을 바꾸는 일관된 결과라면 실증 연구로 발전할 수 있다.
- **같은 데이터의 모방이 차이를 설명함:** RL objective 고유 효과 주장은 줄이고, 상호작용 데이터의 어떤 구성이 도움이 되는지 좁힌다. 과거 cross-embodiment transfer 실험을 자동 재개하지 않는다.
- **정보 차단 방식만 바꾸면 결론이 뒤집힘:** 효과보다 진단의 타당성 문제가 먼저다. 평가 방법을 보정하며 강한 기제 주장은 유보한다.

**새 방법의 선점 위험:** [RobustVLA v2](https://arxiv.org/html/2511.01331v2)는 이미 observation/action perturbation에 대한 RL regularization을 제안한다. [Contrastive Representation Regularization, ICML 2026](https://proceedings.mlr.press/v306/kim26ao.html)도 control 관련 표현 정규화의 직접 선행이다. “robustness loss를 추가한다”를 독립 기여로 미리 약속하지 않는다. 여기서 RobustVLA는 arXiv:2511.01331이며 비슷한 이름의 다른 multi-modal robustness 논문과 합치지 않는다.

**현재 가능성:** 탐색할 가치가 있다. VLA+RL 중심성이 명확하고 이미 공개된 전후 checkpoint에서 관측을 시작할 경로가 있다. 다만 top-tier 실증 연구에는 새로운 일반화 가능한 설명·공정 비교·충분한 반복과 추가 모델/과제가 필요하다. 아직 효과도, 필요한 GPU 메모리도 검증하지 않았다.

<a id="cross-play"></a>

## 4. 2순위: 독립적으로 학습한 VLA 로봇 사이의 협력

### 선행과 남겨 둘 질문

[Latent Theory of Mind, CoRL 2025](https://proceedings.mlr.press/v305/he25a.html)은 분산 diffusion 정책의 협력과 일시적인 실패/지연을 다룬다. [CHORUS §3–4](https://arxiv.org/html/2606.12352v1)는 공통 VLA를 여러 로봇에서 독립 실행하고, §4.2에서 동료의 **scripted lateral perturbation**에 대한 반응도 평가했다. 여러 로봇을 한 VLA로 제어하거나 동료의 지연/위치 변화에 반응하는 것 자체는 새 공백이 아니다.

[Cooperative Multi-Agent VLA via Reinforced Fine Tuning §4–5](https://arxiv.org/html/2609.36588v1)는 개별 agent credit filtering과 latent-space RL을 이미 결합한다. 이 방법은 local 관측 외에 공유 third-person RGB도 사용한다. CHORUS와 비교할 때 관측 접근권을 같다고 가정하면 안 된다.

**새 탐색 질문:** RL로 함께 학습한 팀의 성공률이 높아져도, **각자 조작은 가능한 다른 VLA 팀원과 조합했을 때** 협력이 유지되는가? 실패한다면 개별 능력 부족, 관측 부족, 타이밍 차이, 서로 다른 협력 관습 중 무엇 때문인가? 특히 VLA의 공통 task/role semantics가 임의의 관습 형성을 줄이는지, 반대로 공동 RL이 특정 동료에게 과적합시키는지를 묻는다. 이번에 확인한 VLA 논문에서 독립 팀원 조합에 대한 충분한 답은 확보하지 못했다.

이 문제의 일반 형태는 새롭지 않다. [Other-Play, ICML 2020](https://proceedings.mlr.press/v119/hu20a.html), [Fictitious Co-Play, NeurIPS 2021](https://papers.neurips.cc/paper_files/paper/2021/hash/797134c3e42371bb4979a462eb2f042a-Abstract.html)이 강한 기반이다. 최신 [HOLA](https://arxiv.org/abs/2607.04972)는 미지의 팀원·환경·팀 규모를, [MATE](https://arxiv.org/abs/2610.06025)는 joint attention을 통한 관습 일반화를 다룬다. 따라서 “population RL을 VLA에 적용한다” 또는 “shared attention으로 협력한다”만으로 신규성을 주장하지 않는다.

### 첫 비교와 기여의 조건

- **문제 단위:** 한 로봇의 정책 교체가 아니라 두 로봇이 동시에 물체를 넘기거나 함께 운반하는 한 task. 처음부터 여러 embodiment·팀 규모·navigation까지 모두 바꾸지 않는다.
- **분리할 변수:** 각 role의 motor competence, 동일한 관측 접근권, 제어 주기/latency, 성공 가능한 역할·접근 방향의 여러 조합. 관습 차이가 실제로 필요한 task여야 한다.
- **비교 행렬:** 함께 학습한 A–A/B–B와 처음 조합한 A–B/B–A. 추가 checkpoint 쌍은 같은 정책을 공유하므로 모두 독립 표본으로 세지 않는다. 정책별 성공 가능성·팀별 task 성공·대기/충돌/낙하를 함께 기록한다.
- **필수 단순 대안:** 고정 역할 prompt, 대기/ready 규칙, 다양한 팀원과의 population training. 명시적 ready bit나 중앙 제어는 정보가 더 많은 별도 조건으로 보고한다. 통신을 추가한 이득을 같은 정보에서의 방법 개선으로 섞지 않는다.
- **표적 후속:** co-adaptation이 실제 남을 때만 goal/role 표현의 정렬, 팀원 조건부 credit 또는 학습 상대 다양화를 검토한다. 이미 있는 MARL 기법을 이기는 새 모듈이 반드시 필요한 것은 아니며, 어떤 prior가 충분한지 규명하는 결과도 가능하다.

[Cross-implementation cross-play 연구](https://arxiv.org/abs/2608.03644)는 seed만 다른 평가와 구현까지 다른 평가를 이미 구분했다. 이 논문은 Other-Play에서 seed 평가가 유용한 proxy일 수 있다는 결과도 보고한다. 따라서 “기존 cross-play 평가는 모두 잘못됐다”거나 “cross-implementation 자체가 신규”라고 주장하지 않는다.

**축소 조건:** 역할 prompt/간단한 동기화만으로 충분하면 그것이 유효한 설계 지침인지 먼저 판단한다. 단순히 알려진 MARL 현상을 로봇 하나에 옮긴 수준이면 독립 방법 투자를 줄인다. 반대로 VLA의 task semantics와 지속적인 물리 협력 사이의 상호작용이 일관되게 관측된다면 기여가 선명해진다.

**현재 가능성:** 연구 방향과 잘 맞는 전략 후보다. 다만 공개 코드/다중 로봇 simulator/지원 checkpoint의 실제 적합성은 아직 심사하지 않았다. 두 물리 로봇이 즉시 있어야 탐색할 수 있다고 단정하지도, simulation-only로 모든 주장을 검증할 수 있다고 보장하지도 않는다.

## 5. 새 검색에서 제외하거나 낮춘 방향

| 초기 방향 | 직접 확인한 선행 | 이번 결정 |
|---|---|---|
| World model 안에서 VLA를 RL로 학습 | [WMPO, ICLR 2026](https://openreview.net/pdf?id=qE2FyvRvuF), [VLAW, ICML 2026](https://proceedings.mlr.press/v306/guo26i.html), [VLA-MBPO, ICML 2026](https://proceedings.mlr.press/v306/zhang26ez.html), [RISE, RSS 2026](https://roboticsproceedings.org/rss22/p012.html) | 결합 자체는 이미 존재. VLAW는 실패/접촉 fidelity를, VLA-MBPO는 branched rollout을 직접 다룸 |
| 보기 좋은 영상과 action-conditioned reliability의 차이 | [MiraBench §3–4](https://arxiv.org/html/2605.29360v1), [CauVA, RSS 2026](https://roboticsproceedings.org/rss22/p016.html) | 실패를 성공처럼 생성하는 편향·action sensitivity를 새 발견으로 삼지 않음. CauVA의 causal 명칭을 causal identification 보장으로 해석하지 않음 |
| 유용한 imagined rollout을 고르거나 정책 개선을 직접 학습 | [U-GROW](https://arxiv.org/abs/2609.22879), [DRILL §5.5–6](https://arxiv.org/html/2610.30814v1), [TIF, 11/03 preprint](https://arxiv.org/abs/2611.04873) | DRILL은 downstream-return objective와 utility 진단까지 제시. TIF는 execution feedback에 따른 candidate audit/선별 후 BC. broad proposal의 중복이 강해 새 후보에서 제외 |
| 사람의 교정·실패 행동을 더 잘 이용 | [Set-Supervised Diffusion Policy, RSS 2026](https://roboticsproceedings.org/rss22/p080.html), [Dissecting Advantage-Guided Post-Training §IV–V](https://arxiv.org/html/2609.28161v1) | positive/negative correction 및 advantage 구성·calibration·활용 비교가 이미 있음. continuation-policy attribution이라는 더 좁은 질문은 미심사 상태로 두고 승격하지 않음 |

DRILL의 저자 명시 한계는 simulation-only와 추가 계산 비용이다. 그러나 “실물로 옮긴다”만으로 자동 새 기여는 아니다. TIF는 새 논문이므로 초록 기준으로 broad collision만 판단했고 세부 방법의 우열을 평가하지 않았다. 이 제외는 world model·사람 교정 분야 전체에 대한 NO-GO가 아니다.

## 6. 기존 후보와 겹치지 않는 연구 단위

| 기존 항목 | 새 후보가 다루는 다른 단위 |
|---|---|
| VRL: base VLA 교체 후 residual 재사용 | Feedback 후보는 residual 없이 post-training 전후 정책의 행동 의존성을 조사 |
| C1: 추가 관측의 선택 / D1: 관측 오류·상태 변화 구별 | 새 센서/관측 선택기나 오류 복원기를 설계하지 않고, 동일 관측 조건에서 학습에 따라 피드백의 기능이 어떻게 달라지는지 분석 |
| E2·초기 latency/chunk 질문 | 입력·control rate·horizon을 통제하며 RL/SFT 학습 차이를 분석. 단순 chunk 단축 효과면 그 설명을 수용 |
| 초기 VLM 의미 보존·RL cross-embodiment transfer | VQA/언어 능력 보존이나 다른 robot으로의 학습 이득 전달이 주 outcome이 아님 |
| HANDOFF: 한 mobile manipulator의 접근→조작 interface | Cross-play 후보는 동시 행동하는 두 agent 사이의 공동 관습과 접촉 협력 |
| GAP-HRI: 사람 도움의 응답 신뢰도·질문/개입 선택 | Cross-play는 자율 robot policy 조합의 일반화. 사람이 답하는 신뢰도나 질문 정책이 아님 |
| 과거 GAP-WM·C4/C6 | World-model/reward 검증을 새 이름으로 재개하지 않으며 새 검색에서 직접 중복 확인 자료로만 사용 |

## 7. 이번 종료 범위와 다음 행동

**완료:** 외부 출처를 통한 새 후보 발견, 최근 직접 중복 확인, 기존 주제와의 비교 단위 구별, 두 후보의 기여 초안·강한 대안·판단을 바꿀 작은 관측 정리. 저장소의 준비 주제는 계속 6개이며 이번 두 개는 아직 별도 실행 주제로 승격하지 않았다.

**미완료:** 후보별 직접 선행의 전체 implementation 심사, checkpoint revision·data lineage 고정, 실제 비교/효과 검증, 독립 외부 피드백. 문헌 탐색 단계 완료를 비실험 buildup 전체 완료로 표시하지 않는다.

**다음 TODO는 GAP-FEEDBACK-N1:** RL4VLA의 warmup/SFT/RL 계보와 normalizer·평가 환경 source를 대조하고, 공개 checkpoint 진단으로 알 수 있는 것과 새 data-matched 학습이 필요한 주장을 구분한다. 그 결과를 위 후보 카드에 통합하고 첫 물리 변화×관측 조건을 명세한다. 모든 source를 완독하거나 새로운 loss를 확정해야만 탐색할 수 있다는 gate는 두지 않는다. 필요해진 source만 더 읽는다.

현재 요청은 문헌에서 새 공백을 찾는 작업이다. 이번에는 실험·dependency 설치·weights/assets 다운로드·local PDF 변경·신규 registry 등록·reading status 승격을 하지 않았다. 실험 준비/재개를 선택하는 후속 작업에서 현재 local Docker 조건을 다시 확인하며, 조건이 충족되면 허용된 최소 실행까지 진행한다.

## 8. 저장소 검증

작업 전·후 repository audit 모두 오류·경고 0이다. Generator 문법 검사와 `build_reading_tiers.py`, `git diff --check`, staged diff 검사를 통과했다. Source 원장의 정규화 title 대조와 수량 검사도 통과했다.

Registry는 1,098편·표준 노트 5,490개, CORE 47 / NEXT 321 / REFERENCE 488 / ARCHIVE 242를 유지한다. 작업 시작 시 6,051개 비-PDF 파일의 hash와 staged diff를 대조해 기존 변경 파일은 TODO·VLA synthesis·주제 index·update index 4개뿐임을 확인했다. 삭제된 기존 파일은 없고 staged diff·canonical manifest·active/history 읽기 기록은 그대로다. 새 파일은 공통 조사 문서와 source JSON 2개다. PDF에는 쓰기/삭제 작업을 하지 않았다.
