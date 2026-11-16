# 원 과제 전이를 고려한 VLA 강화학습의 hindsight 목표 선택

- Updated: 2026-11-07 KST / **GAP-HINDSIGHT-P0-PREP — 비실험 설계·실행 자료 작성 완료, native 검증 대기**
- 작업용 영문 제목: **Task-Relevant Hindsight Goal Selection for VLA Reinforcement Learning**. 발표 논문이나 검증된 방법 이름이 아니다.
- 판정: **좁은 비교·분석 후보로 탐색 유지.** N1에서 일반적인 adaptive goal weighting의 선행 중복을 확인했다. 새 selector의 방법 기여는 아직 약하며, 아래 공개 사례에서 단순 목표 일치 이후 남는 전이를 먼저 확인할 가치가 있다. N2에서 분할·주 비교·학습 조건·상한을 정했다. 현재 Mac의 NVIDIA 조건 미충족을 확인하고 P0 recipe/adapter/launcher를 작성했다. 다음은 호환 local NVIDIA에서 build·payload·native IO/gradient 검증이며, 기존 8개보다 출판 가능성이 높다고 판정하지 않았다.
- [정식 등록한 직접 선행](../../../../work/update/REGISTRY_MAINTENANCE_2026-11-07.md#admissions) · [단일 출처·조사 범위](./sources.json) · [재현 방법·미구현 범위](../재현%20방법/README.md) · [전체 후보](../../README.md) · [TODO](../../../../TODO.md)

## 1. 먼저 확인한 공백과 연구 질문

로봇이 “빨간 컵을 접시에 놓기”에 실패했어도 빨간 컵을 들거나 다른 컵을 접시에 놓는 행동은 수행했을 수 있다. 실패 영상을 올바르게 설명하는 보조 목표는 여러 개다. **설명이 사실이라는 것과 그 설명으로 학습하면 원래 과제가 개선된다는 것은 별개**다.

이번 질문은 **동일한 실패 경험과 학습 예산에서, 어떤 보조 언어 목표로 RL 업데이트해야 원래 지시의 성공률이 개선되는가?**다. 특히 목표와 공유하는 객체·행동·관계, 현재 정책이 그 지시에서 해당 행동을 생성할 가능성을 함께 볼 필요가 있는지 검토한다. 두 요인이 중요하다는 결론은 아직 가설이다.

가장 가까운 [LfH v2](https://arxiv.org/html/2607.09042v2#S4)는 실패를 보조 과제로 재라벨하고 원래 과제와 함께 RL로 학습한다. 따라서 **실패 재사용·언어 재라벨·단일 VLA의 RL 학습 자체는 공백이 아니다.** 이번에 확인한 범위에서는 *같은 실패에서 가능한 복수의 올바른 목표를 원 과제 전이 가치로 비교·선택하는 조건*이 충분히 밝혀졌는지 확인되지 않았다. 문헌의 무보고를 증명한 것이 아니라 후속 검토할 좁은 질문이다.

같은 VLA 정책의 파라미터를 RL로 업데이트하며 배포 시 별도 residual controller나 계층형 planner를 추가하지 않는 방향이다. 학습 자료의 라벨 생성에 VLM/사람/시뮬레이터를 쓰는 것과 배포 제어기를 추가하는 것을 구분한다. 현재 우선 범위는 **단일 로봇 manipulation**이다. Navigation·서로 다른 embodiment로의 전이는 후속이며 현재 기여에 포함하지 않는다.

## 2. 기존 후보 밖에서 비교한 방향

2024–2026 직접 관련 논문과 기존 registry를 함께 조사했다. 아래 제외는 분야 전체의 NO-GO가 아니라 **이번에 조사한 넓은 아이디어만으로 새 주제를 만들지 않겠다는 선택**이다.

| 방향 | 이번 선행 근거·판단 | 선택 |
|---|---|---|
| Flow VLA의 구조화된 탐색 노이즈 | [DPPO, ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/c0749c39aaff9e9e4c91f7118bf21b1e-Abstract-Conference.html), [ReinFlow, NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/98d6f928497d9eaad9f320fb2db3040d-Abstract-Conference.html), [StructRL, 2026 preprint](https://arxiv.org/abs/2608.15139)가 탐색/생성 과정의 학습을 직접 다룸 | 일반 노이즈 변경은 제외 |
| 과제별 붕괴 방지·불확실성에 따른 노이즈 | [2026 uncertainty-gated 연구](https://arxiv.org/abs/2609.28838)가 좁은 계산 예산에서 해당 문제를 직접 비교. ICLR 2027 제출 표기는 채택이 아님 | 새 규칙을 제안하기 전에 강한 직접 중복 |
| 실패를 다른 목표의 성공으로 재사용 | LfH 최신본과 아래 offline/언어 재라벨 계보가 이미 있음 | 일반 조합은 제외 |
| **올바른 재라벨들 사이의 원 과제 전이 가치** | 성공/라벨 정확성만으로 무엇을 배우는 게 유용한지 알 수 있는가? 기존 goal selection과 차별화 필요 | **이번 새 주제로 선택** |
| 일반 안전성·위험 회피 | 기존 registry [SafeVLA](../../../../2025/NeurIPS/2025_NeurIPS_SafeVLA-Towards-Safety-Alignment-of-Vision-Language-Action/01_overview.md) 등 직접 선행. 이번 검색만으로 새 safety gap은 확정하지 않음 | 예비 탐색, 별도 주제 생성 안 함 |
| Reset-free 개선 | 자율 데이터 수집·reset 의존성은 중요한 문제이나 이번 범위에서 단일 VLA 학습의 구체적인 차별점을 충분히 확보하지 못함 | 보류; “연구가 없다”는 의미 아님 |

훈련의 확률적 sampler와 배포 sampler 차이도 살폈지만 독립적인 gap을 확보하지 못했다. 단순한 동작 차이를 기여로 올리지 않았다. 기존 UNIFIED의 value-gradient 질문, VRL의 base 교체 후 residual 재사용, FEEDBACK의 관측 개입과는 **학습 데이터에 부여할 보조 목표의 선택**이라는 개입 대상이 다르다.

## 3. 가까운 선행이 이미 답한 것

| 선행·상태 | 확인 범위와 이미 있는 기여 | 이번에 주장하지 않을 것 |
|---|---|---|
| [SPRINT, ICRA 2024](https://doi.org/10.1109/ICRA57147.2024.10610606) | IEEE 제공 Crossref metadata·[공식 code README](https://github.com/clvrai/sprint). 언어 재라벨과 offline skill 학습 계보 | 재라벨로 과제 다양성을 늘리는 것 자체 |
| [SOAR, CoRL 2024](https://proceedings.mlr.press/v270/zhou25b.html) | 공식 proceedings abstract. 자율 경험 수집·평가와 instruction-following 정책 개선. PMLR 발행 연도는 2025 | 자율 수집/사후 라벨로 정책을 개선한다는 넓은 주장 |
| [RL4VLA, NeurIPS 2025](https://proceedings.nips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html) / [SimpleVLA-RL, ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html) | 공식 abstract·기존 registry pr-0956/0957. VLA RL 일반화·학습 경로의 기준 | VLA에 RL을 적용하거나 reward signal을 늘리는 것 자체 |
| **[LfH, 2026 arXiv v2](https://arxiv.org/html/2607.09042v2)** | §4–5·App.A–B 지정 본문 검토. 최신 title은 *Learning from Hindsight for VLA Reinforcement Learning*. Main conference 채택은 이번 확인으로 확정 안 함 | **v1만 보고 importance correction·label filtering·모방 대조가 없다고 주장하지 않음** |
| [CAST, arXiv 2025 / v2 2026](https://arxiv.org/html/2508.13446v2) | 본문 구조·초록·project/code README. 같은 관측에서 언어와 행동의 다양성을 늘리는 counterfactual augmentation | 단순 contrastive label 추가·언어 grounding 개선 자체 |
| [CounterAlign, 기존 CoRL 2026 기록](https://arxiv.org/abs/2608.21740) | 이번에는 저자 abstract 재확인; 기존 registry pr-1033의 venue 검증 보존. Expert 행동과 지시 mismatch로 offline reward/정책 학습 | 지시 불일치 negative를 만드는 것 자체 |
| [Open-ended Instruction Relabeling, 2025 arXiv](https://arxiv.org/abs/2506.20061) | 저자 abstract의 Craftax unified instruction policy. 학회 검색 결과가 섞여 이번에는 main venue를 새로 확정하지 않음 | LLM으로 실패의 보조 과제를 만드는 것 자체 |
| [HPG, ICLR 2019 계보](https://arxiv.org/abs/1711.06006), [HTRPO, IJCAI 2021](https://www.ijcai.org/proceedings/2021/459), [HinDRL, 2021/2022 계보](https://arxiv.org/abs/2112.00597) | Importance correction·trust region·task-specific hindsight goal selection의 선행. HPG/HinDRL 공식 OpenReview 접근은 challenge로 제한됨 | “목표에 맞는 hindsight를 고른다” 또는 importance sampling 자체를 신규성으로 삼지 않음 |

**최신본에서 제외한 가짜 공백:** LfH v2 §4.2·App.A.2–A.3은 local/cumulative ratio의 차이와 편향–분산 문제를 명시하며, 지시 permutation·HIR 모방 대조·cross-suite 평가도 다룬다. “보정이 없다”, “언어가 실제로 쓰이는지 전혀 확인하지 않았다”, “모방과 비교하지 않았다”는 비판은 버린다. App.A.1의 group threshold/grounding 검토와 우리의 **동일 group 안 복수 valid label 선택**을 구분한다. 다만 이 구별만으로 새 방법 가치가 입증되지는 않는다.

**재현 경계:** [LfH project](https://iamxjy.github.io/lfh-website/)의 Code 링크는 확인 시 `#`였다. 공개 실행 구현을 확보했다고 표시하지 않는다. 최신 본문과 project의 과거 title/저자 표시도 달라 본문 version을 우선한다. CAST code의 존재는 확인했으나 이번에 전체 학습 코드를 검증하지 않았다. 독립 재구현은 저자 코드 재현과 별개다.

## 4. 남은 질문과 가능한 기여

**질문:** 동일한 실패 pool에서, 원래 목표와 관계가 다른 *참인* 보조 목표를 사용하면 동일 로봇 interaction·update 예산에서 원 목표 성공의 증가가 달라지는가? 그 차이를 단순 명사/동사 일치·텍스트 유사도·원 보상 threshold보다 잘 예측해 학습에 사용할 수 있는가?

이때 세 가지를 분리한다.

1. **라벨 타당성:** 해당 궤적이 보조 목표를 실제 수행했는가? 틀린 라벨을 섞어서 selection의 효과를 만드는 실험은 주 비교가 아니다.
2. **원 과제와의 관계:** 같은 객체의 다른 조작, 다른 객체의 같은 조작, 공통 관계, 반대 동작 등을 구별한다. 반대 동작도 유용할 수 있으므로 “close에는 open을 금지” 같은 결론을 미리 넣지 않는다.
3. **정책의 행동 분포 중첩:** 행동은 원 지시에서 생성됐다. 다른 지시로 재평가할 때 likelihood가 얼마나 달라지는지 본다. 높은 overlap이 원 목표 전이를 보장하거나 state-distribution 편향을 없애지는 않는다.

작업 가설은 **라벨 정확도와 보상 변화량이 비슷해도, 원 과제와의 관계에 따라 전이 효용이 다를 수 있고 그 효용이 학습 중 바뀔 수 있다**는 것이다. 차이가 전혀 없거나 lexical overlap만으로 충분할 수도 있다.

초기 방법 후보는 현재 정책·원 지시·후보 목표에 따른 **보조 RL loss 선택/가중**이었다. **N1에서 이 일반 원리는 기존 CHER·OL-AUX·gradient similarity와 겹침을 확인했다.** 이를 새 알고리즘으로 제안하지 않는다. [N1의 좁힌 질문](#n1-review)에 따라 단순 선택 이후 남는 원 목표 전이의 차이를 먼저 조사한다.

논문으로 발전할 경우 중심 기여는 다음 둘 중 하나다.

- **학습 방법:** 원 과제 전이를 고려한 목표 선택/가중으로 같은 interaction·전체 계산 비용에서 성능 또는 효율을 개선하고 새로운 과제 조합에서도 유지함.
- **분석:** 어떤 참인 보조 목표가 언제 도움이 되는지 재사용 가능한 예측·반례를 제시하여 relabeling의 선택 결정을 바꿈.

단일 task에서 라벨 몇 개를 골라 성공률을 높인 결과나 “VLM이 틀릴 수 있다”는 설명만 남으면 독립 기여는 약하다. 석사 후보로서 문제와 최소 대조는 설명 가능하지만, 저자 코드 부재·정책 학습과 label 비용 때문에 **구현 부담은 중상, 총 기간·GPU 요구량은 미정**이다.

## 5. 가장 작은 비교 설계 초안

N0의 비교 초안은 **[N2 계약](#n2-contract)으로 통합**했다. 현재 source·분할·주 비교·loss·seed·비용·주장–증거의 기준은 §9와 단일 JSON이다. 같은 설정을 별도 초안으로 유지하지 않는다.

초기 범위는 단일 로봇 manipulation·한 VLA·공통 sim oracle이며, 같은 원 실패 경험에 참인 보조 목표가 여러 개 있어야 선택 효과를 구분할 수 있다. N2의 U(균등)/O(객체 일치)/G(원 목표만) fixed-pool 비교를 먼저 설계하고, 효과가 보이면 동일 label BC·보상 분산·gradient-reference 및 다과제 대조로 확장한다. 언어 유사도나 쉬운 label 선택이 baseline으로 존재한다는 사실만으로 이들로 충분함이 입증되지는 않는다.

배포 시 통합 정책이라는 사용자 방향은 유지한다. VLM/사람/oracle의 학습 감독과 actor의 관측 권한을 구분하고, 원 명령 성공·보조 목표 성공·전체 계산 비용을 따로 본다. Fixed-pool 업데이트 효과를 arm별 on-policy 탐색의 효과로 해석하지 않는다.

## 6. 계속할지 판단할 결과

| 관측 | 다음 판단 |
|---|---|
| 참인 라벨 사이의 전이 차이가 반복되고 단순 관계 규칙으로 충분하지 않음 | Adaptive selection/weighting으로 방법 탐색 |
| 간단한 객체·행동 일치로 충분함 | 복잡한 selector 투자 축소. 의미 있는 비용/일반화 법칙이 있으면 분석 또는 단순 recipe로 검토 |
| 겉보기 이득이 label 오류 제거·더 많은 update·reward variance로 설명됨 | 해당 알려진 요인으로 설명을 수정; 새 전이 기여 주장 보류 |
| 원 과제 성능은 같고 보조 성공만 증가함 | 목표 불일치. 방법 성공으로 보고하지 않음 |
| 유효 라벨이 단일하거나 기본 행동 능력이 없어 비교 자체가 불가함 | task/초기화 수정. 연구 가설 반증과 구분 |
| LfH/goal-selection 최신 선행에 같은 조건·방법·대조가 이미 있음 | 독립 주제 축소 또는 중단; 이름만 바꿔 계속하지 않음 |

## 7. 비실험 buildup 상태와 다음 TODO

| 단계 | 현재 상태 |
|---|---|
| 문제·독자 | 원 과제 성능을 높이려는 VLA RL 연구자; 동일 실패 자료에서 보조 목표 선택의 효과를 비교 |
| 직접 선행 | N0/N1의 본문·선택 코드 대조 완료. 일반 adaptive weighting은 기존 지식이며 전체 분야 신규성은 미확정 |
| 질문·대안 | 보상 벡터·언어 조건·주 목표 gradient 부재를 구분; 무작위/객체 일치/원 과제 RL 우선, 분산·모방·gradient 대조의 확장 조건 명시 |
| 논문 이야기 | 조건별 분석 후보. 새 selector의 우월성·출판 가능성은 미입증 |
| 최소 비교 | N2의 공개 task A/B, 개발·학습·평가 index 규칙, primary contrast·3 seed pilot·비용 상한 고정. 실제 init payload 중복·복수 valid-label witness는 미확인 |
| 실행 부담 | Source/후보 weight identity와 공통 수학 계약 작성. Native image·adapter·payload·정확한 파라미터 목록·VRAM/시간은 미검증 |
| 외부 비판 | 검토 질문 준비, 독립 응답 미수신. 피드백 부재가 작은 탐색을 금지하지 않음 |

**비실험 연구 설계 검토는 N2에서 마무리했다.** 문헌 요약·동일 metadata 조사를 다시 다음 TODO로 만들지 않는다. **다음 TODO: GAP-HINDSIGHT-P0** — P0-PREP에서 현재 Mac의 자원 미충족을 확인하고 실행 자료를 작성했다. 호환 local NVIDIA 컴퓨터에 자료를 전달한 뒤 image build·payload·native IO/gradient 검증을 진행한다. P1/P2 수집·학습은 P0 완료만으로 자동 시작하지 않는다.

과학적 판정은 **좁은 분석 후보 유지, 방법 GO 미확정**이다. Native 사례·효과·외부 피드백과 실행 준비 완료를 문서 완료와 구분한다. Registry 1,112편·reading status와 기존 후보의 실행 계약/판정은 보존했다. 외부 source의 registry 등록은 별도 표준 5-note admission을 따른다.

<a id="n1-review"></a>

## 8. N1 결과: 일반 가중 방법을 제외하고 남긴 비교

### 8.1 선행의 objective·code 대조

| 직접 반론 | 확인한 근거 | 이번 기여에서 제외하거나 대조할 것 |
|---|---|---|
| 목표와 가까운 실패를 학습 단계에 따라 선택 | [CHER, NeurIPS 2019](https://proceedings.neurips.cc/paper/2019/hash/83715fd4755b33f9c3958e1a9ee221e1-Abstract.html), 저자 `baselines/cher/her.py` | 목표 근접성과 다양성의 적응적 선택은 이미 있음. 단순한 object relevance curriculum을 새 원리라고 부르지 않음 |
| 시연이 정의한 과제 관련 hindsight 목표 | [HinDRL §4.2–4.4](https://arxiv.org/html/2112.00597#S4) | Task-specific goal distribution·부분 성공 학습은 이미 있음. 이번 선택은 같은 online group의 언어 목표이며 추가 성공 시연을 요구하지 않는 제한된 범위. 공개 저자 구현은 확인하지 못함 |
| 보조 loss가 주 loss를 돕는 정도로 가중 | [OL-AUX, NeurIPS 2019 §3–4](https://proceedings.neurips.cc/paper/2019/file/0e900ad84f63618452210ab8baae0218-Paper.pdf), 저자 `olaux/ddpg.py` | Gradient 내적 기반 online 가중은 선행. 저자 repo도 재구현임을 명시하고, 검사한 `main_task_Q_cnn_grad_tf`는 aux가 더해진 `Q_loss_tf`를 참조하므로 수식과 코드 변수를 자동 동일시하지 않음 |
| Gradient 방향 또는 validation loss로 자료 가중 | [Du et al., 2018 arXiv](https://arxiv.org/abs/1812.02224), [Ren et al., ICML 2018](https://proceedings.mlr.press/v80/ren18a.html)와 저자 `mnist/reweight.py` | 단순 cosine gate·meta-reweighting은 새 방법 아님. 별도 target validation batch를 쓰면 추가 정보/계산 비용으로 공개 |
| Desired/hindsight 목표 분포 차이를 줄이는 선택 | [OBGMGS, Neurocomputing 2024](https://doi.org/10.1016/j.neucom.2024.127734), [저자 HPG 코드](https://github.com/ShiguangSun/OBGMGS_HTRPO/blob/bda2badbe34f88216fbdd86e8fc2533ceef2d334/agents/HPG.py#L138) | Euclidean 거리 행렬과 bipartite matching을 이미 사용. Text embedding 거리로 옮긴 것만으로 신규성 주장 안 함. Publisher 초록/소개·코드 대조이며 본문 전체 검토 아님 |
| 언어 hindsight로 sparse reward를 보완 | [ETHER, 2023 arXiv](https://arxiv.org/abs/2307.15494), N0의 LfH v2 | 언어화·cold start 완화 자체를 새 기여로 삼지 않음. ETHER는 abstract 범위이며 2026 검색 노출 날짜를 발표 연도로 쓰지 않음 |

코드 commit·파일 hash·검토 위치는 [sources.json](./sources.json)의 `n1.code_review`에 있다. 외부 source는 읽기만 했으며 import·학습·패키지 설치는 하지 않았다. 위 논문 모두가 같은 VLA 비교를 했다는 뜻은 아니지만, **일반 선택/가중 원리의 독창성을 크게 제한한다.**

**남길 질문:** 같은 original-goal 실패 group에 가능한 여러 참인 언어 목표 중, 단순 객체 일치와 유효 보상 group 수를 통제한 뒤에도 원 목표 성공의 전이 차이가 남는가? 차이가 학습 초기에 주 목표 gradient가 없는 조건과 이후 조건에서 달라지는가? 이 질문은 분석 가설이며 새 원리라는 결론은 아니다.

### 8.2 공개 과제에서 확인한 최소 비교 사례

첫 후보는 [LIBERO-10의 LIVING_ROOM_SCENE2](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/8f1084e3132a39270c3a13ebe37270a43ece2a01/libero/libero/bddl_files/libero_10/LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket.bddl)다. 원 목표는 **alphabet soup와 tomato sauce를 모두 basket에 넣기**이며 실제 BDDL도 두 `In` predicate의 conjunction이다. `In`은 [contact와 containment](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/8f1084e3132a39270c3a13ebe37270a43ece2a01/libero/libero/envs/predicates/base_predicates.py#L57)를 함께 검사하고, [scene evaluator](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/8f1084e3132a39270c3a13ebe37270a43ece2a01/libero/libero/envs/problems/libero_living_room_tabletop_manipulation.py#L136)는 conjunction을 평가한다.

- **후보 목표 집합:** 같은 scene의 soup, tomato sauce, cream cheese, ketchup, orange juice, milk, butter 각각에 대해 `put <object> in the basket`을 만드는 7개 atomic 목표. 물체·predicate는 source에 있으나 이 7개 언어 목표의 group reward/후보 자격을 평가하는 adapter는 **우리의 미구현 확장**이다. P0의 atomic predicate observer 초안만 추가했으며 자연 label 검증은 아니다.
- **비교 예시:** 원 목표는 실패했지만 soup와 ketchup을 각각 basket에 넣은 한 anchor가 있다면, soup 목표는 원 과제의 구성 요소이고 ketchup 목표는 같은 행동·다른 객체다. **이는 논리적으로 가능한 사례이며 실제 rollout witness가 아니다.** 실패 빈도·두 물체 조작 능력도 미확인이다.
- **라벨 자격:** 초기 predicate가 false이고 rollout 중 true로 변한 목표만 달성 후보로 둔다. 처음부터 참인 배치나 mere paraphrase를 별도 학습 목표처럼 세지 않는다. 원 목표는 두 객체가 **같은 시점에** 안에 있어야 성공이다. 서로 다른 시점의 두 atomic 성공을 원 목표 성공으로 합치지 않는다.
- **비교 단위:** 같은 원 목표·같은 초기 상태의 K=8 group을 우선 설계한다. 실패 anchor 하나에서 달성한 후보를 만들고, 선택한 **공유 목표 하나**로 group 전체를 다시 평가한다. 후보는 anchor에서 참이어야 하지만 모든 rollout에서 참일 필요는 없다. 상수 보상 벡터는 별도로 기록하고 selection 효과의 주 비교에서는 제외한다.
- **보상 의미:** 원/보조 목표 모두 지정 predicate가 rollout 중 달성됐는지를 쓰되 전체 시간별 predicate trace를 남긴다. 원 실패의 horizon·실행된 토큰을 보조 성공 시점에 임의로 잘라내지 않는다. 원 benchmark의 success-once와 terminal success는 구분해 기록한다.

**거절한 source 해석:** `open_the_top_drawer_and_put_the_bowl_inside.bddl`은 자연어와 달리 goal에 `Open`을 명시하지 않고 `In`만 둔다. 이를 “open과 put 두 조건이 독립 검증되는 공개 과제”라고 사용할 수 없다. 이 때문에 첫 사례는 명시적인 두 `In` 조건으로 바꿨다.

초기 후보는 표준 LIBERO scene이다. LIBERO-PRO OOD 실험이나 새로운 객체 조합 일반화를 확보했다고 주장하지 않는다. 같은 BDDL 구조가 존재하는 것과 native 관측·물리 상태·checkpoint가 맞는 것은 별도다.

### 8.3 학습 신호와 의미 효과를 구분하는 조건

후보 h의 group 보상 벡터를 `r_h = (R(τ₁,h), …, R(τ_K,h))`로 기록한다. 다음 비교를 혼동하지 않는다.

1. **전체 선택 효과:** 같은 group에서 h만 바꾸되 보상 벡터도 달라질 수 있다. 실제 curriculum 선택의 효과이며 언어 의미만의 효과라고 하지 않는다.
2. **보상 벡터가 같은 경우의 진단:** `r_h1 = r_h2`인 서로 다른 목표가 실제 관측되면, 같은 advantage·행동 자료에서 instruction conditioning을 비교한다. 성공 개수만 같은 것보다 강한 대조다. 이런 쌍이 없으면 진단 불가로 남기며 다른 자료로 결과를 만들어내지 않는다.
3. **원 목표 신호가 없는 경우:** 모두 실패한 group의 GRPO reward advantage는 0이다. KL/entropy·다른 batch를 제외한 해당 reward policy gradient도 0이므로, 이 gradient와의 cosine으로 “도움 되는 목표”를 선택할 수 없다. 이는 식에서 나온 성질이며 실험 발견이 아니다. 같은 batch 기반 alignment는 명시적 fallback(균등 선택)을 사용하고, 별도 target-gradient reference를 쓰는 버전은 추가 정보가 있는 비교로 분리한다.

이 세 구분이 같은 관측에서 유효 라벨을 많이 만드는 것보다 우선이다. Label accuracy가 같다는 사실만으로 보상 sparsity·선택된 행동·gradient 크기까지 같아지지 않는다.

### 8.4 강한 단순 대조와 비용 계약

| 단계/대조 | 선택 규칙·역할 | 공정성 조건 |
|---|---|---|
| 원 목표 GRPO | 보조 loss 없음 | 같은 initial checkpoint·original-goal rollout pool. 추가 RL update 대조로 update 수 효과도 구별 |
| 균등 valid-goal 대조 | 자격을 충족한 후보에서 seed로 균등 추출, 한 group에 하나 | 동일 후보 집합·predicate 정보. LfH의 VLM 생성 분포를 재현했다는 뜻 아님 |
| 객체 일치 규칙 | 원 목표의 객체를 다루는 후보 우선, 동률은 같은 seed로 추출 | 이번 scene은 verb/relation이 같으므로 이 규칙이 특히 강함. 새로운 알고리즘으로 포장하지 않음 |
| 보상 분산 규칙 | `q_h(1-q_h)` 최대인 후보 선택, q는 group 성공 비율 | 많은 유효 advantage가 전이 효과를 설명하는지 확인. 평가 성공으로 선택하지 않음 |
| Gradient 기반 기존 원리 | 목표 gradient를 얻을 수 있는 경우의 alignment/가중 | 별도 reference 데이터·backward 횟수·0-gradient fallback 공개. 논문 DDPG/이미지 분류 구현의 그대로인 재현은 아님 |
| 동일 라벨 BC/가중 모방 | 선택된 라벨과 성공 자료를 그대로 사용 | Binary reward에서 success-only BC와 reward-weighted BC가 같은 대조가 될 수 있으므로 중복 baseline을 만들지 않음 |

처음부터 모든 arm을 학습하지 않는다. 먼저 **valid-label 존재·re-score 동일성·group reward 교정**을 확인하고 균등 선택 대 객체 일치의 작은 비교를 우선한다. 큰 학습은 별도 단계다.

동일 interaction/update 비교에서는 원 group·anchor·후보 pool·초기 파라미터/optimizer·선택 빈도·보조 loss 계수/clip 기준을 공통으로 둔다. 후보 평가와 선택에 사용한 forward/backward, 실제 action tokens, env steps, GPU 시간은 별도 기록한다. 저렴한 규칙보다 비싼 selector에 계산을 추가하고 “동일 비용”이라 부르지 않는다. 총 GPU 예산을 맞춘 비교는 update 수가 달라질 수 있는 별도 추정 대상이다.

**첫 비교의 재구현 경계:** simulator predicate를 공통 oracle로 쓰고, RLinf 수정 OpenVLA-OFT의 token likelihood 경로를 이용한다. LfH의 VLM label/reward, 주 π0.5 결과, LIBERO-PRO 전체 suite와 동일 실험이 아니다. Paper Eq.(7)의 cross-instruction local ratio 원리는 비교하되 native RLinf의 token 단위 clipping과 논문의 action 단위 집계를 혼용하지 않는다. N2에서 모든 arm의 token ratio·trajectory 평균을 동일하게 정했다. 제안 selector에만 다른 loss를 쓰지 않는다.

### 8.5 연구 판단과 남은 증거

**N1 판정은 탐색 유지·일반 방법 주장은 축소**다. 구체 task/evaluator와 re-score 경로를 찾았으므로 질문을 조사할 출발점은 생겼다. 그러나 학습 가능한 복수 라벨이 실제로 자주 나오며, 단순 객체 일치/보상 분산/모방 이후에도 추가 이득이 남는지는 전혀 측정하지 않았다. 한 scene의 oracle 진단만으로 top-tier 방법 논문을 주장할 수 없다.

향후 단순 규칙이 충분하면 복잡한 selector를 버리고, 여러 과제에서 재사용 가능한 분석이 있는지 판단한다. 유효 라벨이 거의 없으면 후보 생성·과제 범위를 수정할 문제이며 정책 전이 가설의 반증이 아니다. 실험이 없다는 이유만으로 종료하지 않지만, 일반 adaptive weighting을 다시 설명하는 것으로 기여를 채우지도 않는다. 독립 외부 피드백은 미수신이며 이번에 연락하지 않았다.


<a id="n2-contract"></a>

## 9. N2: 분할·통계·학습·중단 계약

아래 숫자와 규칙은 **우리의 작은 진단을 위한 사전 설계**다. 논문 권장값·관측 결과·검증된 실행 설정이 아니다. 기계적으로 참조할 단일 계약은 [sources.json](./sources.json)의 `n2.contract`, 구현 경계는 [재현 방법](../재현%20방법/README.md#n2-learning-contract)에 둔다.

### 9.1 공개 task와 분할

LIBERO 고정 revision의 [task map](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/8f1084e3132a39270c3a13ebe37270a43ece2a01/libero/libero/benchmark/libero_suite_task_map.py#L38)에서 다음을 확인했다. 숫자 task ID는 `task_order_index=0`에서만 사용하고 반드시 파일 이름을 함께 검증한다.

| 역할 | 공개 task / 목표 | 이 비교가 답하는 범위 |
|---|---|---|
| A: 주 학습·평가, ID 0 | SCENE2: soup와 tomato sauce를 basket에 넣기, 두 `In`의 동시 conjunction | 원래 학습한 명령의 새 초기 상태에서 개선되는가 |
| B: 별도 보존/전이 평가, ID 1 | [SCENE2: cream cheese와 butter를 basket에 넣기](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/8f1084e3132a39270c3a13ebe37270a43ece2a01/libero/libero/bddl_files/libero_10/LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket.bddl) | 같은 scene의 다른 명령에 도움이 되는가 또는 손상이 있는가. B rollout으로 학습/설정 선택 안 함 |
| C: 확장 예약, ID 7 | [SCENE1: soup와 cream cheese를 basket에 넣기](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/8f1084e3132a39270c3a13ebe37270a43ece2a01/libero/libero/bddl_files/libero_10/LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket.bddl) | 물체 배치/집합이 달라진 경우. 첫 pilot 자동 실행 대상 아님 |
| D: 관계 확장 예약, ID 4 | [SCENE5: white mug→left plate, yellow-white mug→right plate](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/8f1084e3132a39270c3a13ebe37270a43ece2a01/libero/libero/bddl_files/libero_10/LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate.bddl), 두 `On`의 conjunction | 같은 물체라도 목적지가 다른 경우. 첫 pilot 자동 실행 대상 아님 |

A/B의 regions·fixtures·objects·init 선언은 공백 정규화 후 같지만 language·goal·obj_of_interest는 다르다. **실제 initial-state 배열과 물리 상태가 같다는 증거는 아니다.** A/B는 동일한 7개 atomic `In` 후보를 공유한다. C는 4개 식품의 `In`, D는 3개 mug×2개 plate의 `On` 6개를 후보로 정의할 수 있으나 이 후보 adapter·실제 달성 가능성은 미검증이다. D의 plate 이름/시각적 좌우 대응도 따로 교정해야 한다.

[공식 loader](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/8f1084e3132a39270c3a13ebe37270a43ece2a01/libero/libero/benchmark/__init__.py)는 task별 `.pruned_init`를 읽는다. Git tree에서 해당 파일의 경로·blob SHA·크기는 확인했으며 binary payload는 받거나 역직렬화하지 않았다.

- **개발:** A init index 0–3. P0 IO와 P1 label 존재 확인에만 사용.
- **학습:** A index 4–7, seed별 각 index에서 K=8을 한 번 수집. 개발 rollout을 학습 pool에 합치지 않음.
- **평가:** A와 B 각각 index 20–29, seed별 state당 1 episode. 모든 arm과 초기 checkpoint에 같은 seed/state 묶음을 적용. 설정 선택이나 중간 best checkpoint 선정에 쓰지 않음.
- **예약:** 8–19와 30 이후는 사용하지 않음. 추후 확증 분할을 자동 확보했다고 부르지 않음.
- **실행 전 확인:** 두 파일에 최소 30개 row가 있는지, row/state hash와 task 내·task 간 중복을 Docker에서 검사. 특히 A 개발/학습 상태와 A/B 평가의 동일 물리 상태 중복은 제거 대상으로 보고한다. 중복/부족이면 **평가 결과를 보기 전에 계약을 개정**하며, runner가 임의로 index를 대체하거나 modulo wrap하지 않는다. 현재 중복이 없다는 판정은 하지 않았다.

이 분리는 **이번 RL 적응 단계의 분리**다. 초기 checkpoint의 LIBERO-10 SFT 노출은 미확정이므로 “학습에서 본 적 없는 과제/물체”라고 하지 않는다. A/B 두 과제를 독립적으로 뽑은 두 개의 task family처럼 통계에 넣지 않는다.

### 9.2 선택 개입과 추정 대상

첫 pilot은 **동일한 초기 정책에서 수집한 고정 pool의 짧은 업데이트 효과**다. Arm별 on-policy 탐색 개선·최종 sample efficiency를 검증하지 않는다.

1. 각 group은 A의 같은 initial state에서 독립 sampler stream으로 수집한 8개 trajectory다. 원 목표 평균 보상 < 0.8인 group에서 실패 anchor를 seed로 한 번 균등 선택한다. 좋은 anchor를 찾을 때까지 다시 뽑지 않는다.
2. Anchor에서 초기 false→true가 관측된 atomic 목표 중 전체 group 보상 벡터가 비상수인 목표를 공통 후보로 둔다. 후보가 없으면 aux=0; 하나뿐이면 U/O가 같은 목표를 사용한다. 후보가 적은 group도 전체 수집 비용·주 분석 분모에서 숨기지 않는다.
3. **U:** 후보에서 균등 선택. **O:** 원 목표의 객체를 다루는 후보를 우선하고 없으면 U와 동일 선택. 동률은 공통 seed/key로 정한다. **G:** 원 목표 GRPO만. 세 arm의 behavior pool·순서·초기 weights/optimizer는 동일하다.
4. P1에서 적어도 하나의 anchor에 관련/비관련 유효 목표가 함께 존재해야 이 좁은 비교를 실행할 출발점이 생긴다. 빈도 threshold를 통계적 진실처럼 정하지 않는다. P2에서 U/O 선택이 실제로 같았다면 “효과 없음” 대신 **개입 차이가 없었음**을 보고한다.

**Primary contrast:** A의 사전 지정 최종 checkpoint에서 `D_s = success(O,s) − success(U,s)`, 3개 run의 평균을 percentage point로 보고한다. U/O 각각 초기 checkpoint 및 G 대비 변화도 함께 제시해 두 arm 모두 나빠졌는데 상대 우위만 강조하지 않는다. B의 변화는 보존/전이 진단으로 분리하며 A/B 최고값을 고르거나 합쳐 주 지표를 바꾸지 않는다.

목표가 바뀌면 reward vector도 달라질 수 있으므로 primary는 **전체 선택 규칙의 효과**다. 의미 조건만의 진단은 실제 `r_h1=r_h2` 쌍과 같은 action/input 자료가 있을 때만 가능하다. 동일 성공 개수·같은 gradient norm만으로 이를 대신하지 않는다. 이 진단, 최대 보상 분산 선택, 동일 label의 success BC/가중 모방, gradient-reference 대조는 효과를 설명할 후속이며 첫 pilot에 실행했다고 기록하지 않는다.

### 9.3 공통 학습 조건

선택한 구현은 categorical token surrogate다. **[LfH Eq.(7)–(8)](https://arxiv.org/html/2607.09042v2#S4)의 정확한 재현은 아니다.** 모든 arm에 같은 조정 사항을 적용한다.

- Binary success-once reward 0/1, group sample standard deviation(`K−1`), epsilon `1e−6`; 추가 batch 전체 advantage normalization·discount·dense reward·native reward filter는 사용하지 않는다.
- 저장된 행동 token별 `ρ = exp(log πθ(z|o,h) − log π₀(z|o,g))`. 분모는 실제 수집 정책의 원 지시 log-prob이며 업데이트 후 새 정책으로 바꾸지 않는다. 시간·7차원·8-step chunk의 확률을 곱하지 않는다.
- 각 trajectory의 **실제로 실행한 token만 평균**한 뒤 group 8개를 동일 가중 평균한다. `min(ρA, clip(ρ,0.8,1.2)A)`를 최대화하며, U/O는 `J_g + λ J_h`, G는 `J_g`. Padding·미실행 chunk suffix는 제외한다.
- **λ=1, c=+∞(hindsight scalar cap 비활성)**로 고정한다. 별도의 dual clipping도 끈다. KL/entropy 계수 0, gradient norm cap 1.0. 이는 가중/clip 튜닝을 selector 효과와 분리하는 단순 진단 조건이다. Scalar cap이 없는 결과를 LfH 기본 설정의 결과로 부르지 않는다.
- Adam `lr=2e−6, β=(0.9,0.999), eps=1e−8, weight_decay=0`; 4 group×각 1회 optimizer step, 추가 epoch·warm start·best checkpoint 없음. Full-parameter 기본 경로의 실제 trainable tensor 목록은 P0에서 봉인한다. 메모리가 부족하다고 자동 LoRA로 바꾸지 않는다.
- Train/eval 모두 temperature 1.6, top-k=-1, top-p=1의 같은 categorical sampler. Eval은 gradient 없이 실행. 원 checkpoint·processor·crop·normalizer와 action_dim=7/chunk=8은 N1 identity를 유지한다. Dropout 같은 추가 확률성은 비활성화하고 sampler RNG는 분리한다.

**왜 loss 크기에 따라 λ를 정하지 않았는가:** 위 평균에서 업데이트 시작 시 같은 지시의 ratio는 1이고 group advantage 합은 0이므로, 원 objective의 스칼라 값은 혼합 성공 group에서도 0일 수 있다. 이때 **gradient는 0이 아닐 수 있다**. 모든 reward가 같을 때 gradient가 0인 경우와 다르다. 따라서 원 objective 값과 aux 값을 맞추는 규칙을 그대로 가져오지 않았다. 이는 우리 수학 계약의 성질이며 원 논문 구현의 오류를 증명한 것이 아니다. `c`도 원 논문의 hindsight cap과 RLinf의 `clip_ratio_c`를 혼동하지 않는다.

### 9.4 표본·불확실성·상한

P0 master seed는 11, P1은 17, P2 훈련 run seed는 **101, 202, 303**으로 고정한다. P2는 동일 pretrained checkpoint와 고정 state 목록에 조건부인 세 개의 수집/최적화 run이다. 같은 run의 8 rollout·7 label·수천 token을 독립 훈련 표본으로 세지 않는다.

각 seed의 U/O/G/base 성공 수와 D를 모두 보고한다. 평균 D와 함께 seed block 및 공유 evaluation state index를 각각 재표집하되 arm pairing을 유지하는 bootstrap 10,000회, seed 7401, 2.5/97.5 percentile을 **탐색용 interval**로 제시한다. 동일 state index는 모든 seed에서 같은 재표집을 사용한다. 3 run·10 state에서는 interval도 매우 불안정하며 95% coverage·검정력·동등성을 보증하지 않는다. 원칙은 [NeurIPS 2021의 few-run RL 평가 연구](https://proceedings.neurips.cc/paper/2021/hash/f514cec81cb148559cf475e7426eed5e-Abstract.html)와 [저자 rliable](https://github.com/google-research/rliable)을 참고했으나, 이 작은 paired 설계·seed 수는 우리의 선택이다. Task가 두 개뿐인 이 단계에서 benchmark IQM 순위를 만들지 않는다.

| 단계 | 사전 상한 | 산출물·진입 경계 |
|---|---|---|
| P0 IO/gradient wiring | reset≤2(생성자 포함), policy query≤2, re-score forward≤4, backward≤2, optimizer step=0; settling 포함 control≤28, 최대 2 GPU-hours | 한 관측의 원/보조 지시 token 재평가·mask/gradient 확인. 인공 reward는 wiring fixture임을 표시. 정책 성능/참 label 검증이 아님 |
| P1 label 존재 확인 | A dev 4 index×8=32 rollout, control≤16,704, query≤2,048, optimizer=0, 최대 4 GPU-hours | 전체 group의 reward trace·후보 수·관련/비관련 pair·선택 가능 빈도. 자연 witness가 없으면 상한 내 결과로 종료 |
| P2 paired pilot | 학습 수집 3×4×8=96 rollout; 평가 3 seed×2 task×10 state×(U/O/G/base)=240 rollout. 합계≤336 rollout·175,392 control·21,504 queries, optimizer≤36, 최대 24 GPU-hours | Fixed-pool 최종 비교. 학습 forward/backward 각각 query-record 환산≤30,720; 모델 batch 크기로 비용을 숨기지 않음. P0 통과만으로 자동 실행 안 함 |

P1/P2는 rollout당 제어 512와 사전 settling 10을 합친 상한이며 실패는 horizon까지, 원 목표 성공/환경 오류는 일찍 종료할 수 있다. 재시작·숨은 warmup도 비용에 포함하고 stage 상한을 넘겨 보충하지 않는다. Physics substeps/Hz와 실제 image 메모리는 native 설정으로 계측·봉인해야 한다. GPU-hours는 사용 GPU 수×점유 wall time의 합으로 측정한다. 위 시간은 **자원 소비 중단 한도이지 예상 소요 시간이나 실행 가능성 보장**이 아니다. 상한 전에 완료하지 못하면 incomplete로 보고하며 seed/평가 prefix만으로 주 결론을 만들지 않는다.

### 9.5 주장–증거와 다음 결정

| 주장 또는 관측 | 필요한 증거 / 다음 결정 |
|---|---|
| 실행 가능한 작은 비교가 있다 | source 정의뿐 아니라 P0 native IO·predicate 교정 및 P1 자연 witness 필요. 현재는 정적 source까지 |
| 객체 관련 목표 선택이 원 과제에 도움 | P2 A의 paired 차이·base/G 대비 변화·seed별 결과·불확실성. 작은 이득 하나는 방법 논문의 증거로 부족 |
| 의미적 전이 효과다 | 실제 동일 reward-vector 대조·overlap/clip/gradient 진단 필요. Primary만으로 주장 금지 |
| RL 선택 원리가 모방보다 낫다 | 같은 label·자료·예산의 강한 BC 대조 후에도 남는 효과 필요 |
| 새로운 과제에 일반화한다 | B는 이번 적응에서 안 쓴 명령일 뿐 pretraining-unseen이 아님. C/D 및 다른 task family·초기화의 사전 분리 평가 필요 |
| 관련/비관련 후보가 거의 없거나 기본 능력이 부족 | 후보 생성/과제·초기화 수정 또는 분석 범위 축소. GPU 부재나 이 witness 부재를 전이 가설 반증으로 쓰지 않음 |
| U/O가 실제 다르지만 CI가 넓고 seed 방향이 엇갈림 | 불확실로 유지. “동일하다” 결론·좋은 seed 선택·무제한 sweep 금지; 의미 있는 효과 범위와 분산으로 후속 표본 설계 |
| O가 이겨도 분산 선택·같은 label BC로 충분히 설명됨 | 복잡한 selector 신규성 축소. 재사용 가능한 분석/단순 규칙의 가치가 남는지 판단 |
| A 개선과 B 손상이 함께 나타남 | 전문화와 간섭의 trade-off로 보고. A 성공률만으로 generalist 개선이라고 하지 않음 |
| 단순 대조 이후 일관된 차이와 새로운 예측이 남음 | 그때 작은 학습 selector/다과제 검증으로 확장. 지금은 자동 방법 GO 아님 |

**N2 결론:** 연구 설계의 내부 비실험 검토는 완료했으며, 다음 실질 증거는 native IO와 자연 실패의 label 다양성이다. 가장 큰 과학적 불확실성은 단순 규칙을 넘어서는 기여의 존재이고, 자원 문제만이 아니다. 그렇다고 GPU 이전에 효과를 입증하도록 요구해 탐색을 닫지도 않는다.


<a id="p0-preparation"></a>

## 10. 최소 실행 준비 결과 — 2026-11-07

**GAP-HINDSIGHT-P0-PREP 완료는 실행 자료 작성과 현재 자원 판정의 완료다.** 현재 Mac은 ARM64·Docker daemon RAM7.65 GiB이고 NVIDIA allocation이 exit125로 실패했다. [재현 문서](../재현%20방법/README.md#resume)에 immutable image·소스·checkpoint hash와 `check → build → prepare → p0`를 통합했다. 기존 CPU Docker image의 제어 검사15개만 통과했으며 native image·payload·시뮬레이션·추론·gradient는 미검증이다.

구현 시 필요한 source 차이도 명확히 했다. 선택한 Transformers fork의 SDPA가 양방향 attention을 구현하므로 실제 class/config를 검사한다. 영상은 공식 LIBERO/OFT의 180도 회전과 gripper 변환을 유지한다. 원 goal에서 샘플한 **같은 token·같은 image**를 재점수화하고, 보조 goal의 gradient는 합성 fixture로만 확인한다. 이 검사는 자연 hindsight label의 정확성·유용성 또는 학습 효과를 입증하지 않는다.

P0 native 상한은 N2 그대로 유지하고 physics≤10,000·control20Hz·same-goal log-prob 최대 오차1e−3을 실행 전 기준으로 추가했다. P0는 optimizer0이며 P1/P2 runner·학습 재개는 아직 미구현이다. Weight/init/asset payload와 row 중복도 target에서 확인해야 한다. 실행 자료의 원격 전달·다른 컴퓨터 clone 성공은 미확인이다.

**과학적 판단은 좁은 분석 탐색 유지**다. 단순 goal weighting의 선행 중복, 관련/비관련 자연 label의 실제 존재, 객체 일치·BC 이후 남는 전이 이득이라는 불확실성이 그대로다. 자원 부족은 가설의 반증이 아니며 GPU 확보 자체도 방법 GO 근거가 아니다. P0 통과 뒤 별도로 P1을 선택해야 자연 label 비교의 식별 가능성을 판단할 수 있다.
