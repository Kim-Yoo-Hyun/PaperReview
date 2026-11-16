# 모바일 조작 정책 교체 시 내비게이션 종료 조건의 전이

**현행 투자 판단 — 2026-11-07:** [8개 후보 비교](../../README.md#candidate-priority)의 인프라 조건부 시스템 후보다. Manipulation·navigation 연결은 강하지만 기존 mobilization 이후 정책 교체의 재검증 비용을 설명해야 하며, 한 template·transport/상태 분기 미구현이 부담이다. 모바일 플랫폼 지원이 확보되면 상대 우선순위를 다시 판단한다.

현행 비실험 상태 검토: **2026-11-05** · [7단계 상태·기여 가설·판단 분기](#buildup-status). 기존 문헌/계약/결과를 대조한 보강이며 새 효과 관측은 없다.

**11/05 통합 판단:** 시스템/평가 후보로 유지하지만 VRL·FEEDBACK보다 구현 부담이 크다. 기존 ActiveAlign의 matched-state/data-matched 결과를 함께 대조했으며 앞단 종료 분포의 중요성 자체는 새 기여가 아니다. Frozen A/B를 동일한 실제 도착 후 전체 상태에서 실행해 종료 선택의 전이와 적은 재선택 비용을 구분한다. 한 scene template만으로 독립 장면 일반화를 주장하지 않으며 transport·state branching 구현은 여전히 미완료다.

근거·전체 상대 비교: [기존 6개+새 2개 공백 검토](../../../update/INTEGRATED_GAP_REVIEW_2026-11-05.md). 신규 paper별 확인 절과 status는 [등록 원장](../../../sources/registry_admissions_2026-11-05.json)에 통합한다. 기존 실행 계약·원시 결과·과거 source 날짜는 보존한다.

현재 판단: 좁은 평가 후보·native 미실행. 11/01 단일 비교 계약과 아래 개요가 10/28 초안에 우선한다. 2/4/4는 같은 scene template 안의 개발/조건 선택/기술적 평가이며 독립 장면 holdout이 아니다. 후반의 설계 이력은 새 실행 승인이나 참 최적 regret 추정이 아니다.

[연구 내용](../내용/README.md) · [재현 방법](../재현%20방법/README.md)

<a id="buildup-status"></a>

## 비실험 buildup 현행 상태 — 2026-11-04

**판정: 조건부 평가 후보 유지 · 내부 비교 설계 정리 · 플랫폼 연결/동일 상태 분기/효과 미검증.** [7단계 비실험 절차](../../../../research/IDEA_BUILDUP_GUIDE.md#nonexperimental-workflow)를 기존 문헌·논리·계약에 적용해 정리했다. 아래 상태는 새 실험 결과나 11/04 신규 문헌 전수조사가 아니다.

**한 문단 기여 가설:** 새 조작 정책을 배포할 때 기존 접근 거리를 재검증해야 하는지가 운영 비용을 만든다. 기여 후보는 **정책 교체에 따른 종료 조건의 재사용 손실과 적은 재선택의 효용을 구분하는 것**이다. 좋은 위치에서 조작이 잘 된다는 사실이나 거리 조정만으로 독립 기여를 주장하지 않는다.

| 비실험 단계 | 상태 | 현재 근거·완료 경계 |
|---|---|---|
| 1 문제·독자 | 정리됨 | [개요](#overview): 모바일 조작 시스템의 policy 교체·검증 담당자. 같은 로봇의 두 checkpoint이며 embodiment 전이 아님 |
| 2 가까운 선행 | 지정 범위 확인 | Mobi-π·MoTo·Semantic Handoff·Behavior-Skill 비교. Isolated skill snapshot과 실제 도착 상태의 차이는 이미 알려짐 |
| 3 질문·대안 | 정리됨 | 고정 0.9 m·A 선택 재사용·B에서 최대 12회 재선택. 정책 전반 능력 차이와 설정 민감도·선택 잡음을 구분 |
| 4 기여 서술 | 가설 초안 | 재사용 판단과 검증 비용이 중심. 현재 한 task/scene template로 일반 재검증 법칙을 주장하지 않음 |
| 5 최소 비교 | 설계됨·미실행 | [단일 계약](../재현%20방법/COMPARISON_CONTRACT.json): 2/4/4 역할, 전체 시작 사례 분모, 실제 도착→정지→A/B 분기. 재선택 이득은 참 최적 regret가 아님 |
| 6 실행 부담 | 미구현 의존성 큼 | [재현 안내](../재현%20방법/README.md): RTX simulator/정책 server·transport·물리 상태 복원 필요. 새 scene group도 없어 광범위 일반화 준비는 안 됨 |
| 7 외부 비판 | 질문 준비·미수신 | [기존 질문](../../../update/THREE_CANDIDATES_NONEXPERIMENTAL_2026-11-01.md#handoff). 실제 모바일 플랫폼 연구자의 응답 기록 없음 |

**결과에 따른 판단 — 아직 관측하지 않은 분기 포함**

| 다음 증거 | 바뀌는 판단 | 이 증거만으로 하지 않을 주장 |
|---|---|---|
| A/B가 같은 종료 조건을 선택함 | 같은 B 결과를 논리적으로 재사용하고 실제 선택 비용만 기록 | 서로 다른 stochastic rerun 차이를 설정 효과로 보고 |
| B 재선택이 나쁘거나 고정 0.9 m면 충분함 | 음의 재선택 이득도 보고하고 해당 조건에서 복잡한 선택의 동기를 줄임 | 작은 표본의 무차이를 동등성으로 해석 |
| 조건 민감도가 달라지고 유한 재검증이 반복해서 유용함 | 독립 장면/정책에서 재사용 판단 원리가 유지되는지 후속 검토 | 한 scene template의 유리한 거리를 일반 방법으로 승격 |

실제 이동 실패·정지·집기·reset에 든 시간과 계산 시간을 포함한다. 재검증 비용이 향후 몇 번의 배포에서 회수되는지는 성공의 가치·사용 횟수가 정해져야 하므로 임의 손익분기 횟수를 쓰지 않는다. 가장 큰 사람 공수는 simulator/server/상태 복원 통합이며 총 기간은 미정이다.

**외부 검토 준비:** 가장 강한 외부 질문은 “정책×도착 조건의 차이가 기존 mobilization/skill-composition 결과를 넘어 실제 교체 의사결정을 바꾸는가?”다. 한 scene template·4개 평가 사례의 한계와 실패를 포함한 비용 정의를 함께 제시한다. 실제 응답·반영이 생기면 내용과 source 위치를 기록한다. 미수신은 작은 탐색을 금지하는 진입 조건이 아니다.

**다음 확인과 문서 종료점:** 첫 구현 주에는 한 dev의 실제 이동 종료·공통 정지·두 정책 분기 trace가 가능한지 점검한다. 연결이 되지 않으면 큰 성능 sweep 대신 구현 범위를 줄인다. 현재 110 phase 후속 상한은 첫 P0의 실행 지시가 아니며 scene 일반화는 별도 자료가 필요하다. 새로운 직접 선행·자료·반례·피드백 없이 같은 문서 검토를 반복할 내부 과제로 만들지 않는다. 실행 범위·상한은 기존 계약과 [재현 안내](../재현%20방법/README.md)가 관리한다.


<a id="overview"></a>

<a id="overview-모바일-조작에서-vla-정책-간-내비게이션-종료-조건의-전이-가능성"></a>
## 모바일 조작에서 VLA 정책 간 내비게이션 종료 조건의 전이 가능성

*Transferability of Navigation Stopping Criteria across Vision-Language-Action Policies for Mobile Manipulation*

2026-11-01 · 비실험 문헌·분석 설계 보완 완료 · NVIDIA GPU 환경에서의 구현·실행·비교 검증 대기

**핵심 질문:** 기존 조작 정책에 맞춰 선택한 로봇의 접근 거리·방향 조건을 새로운 비전-언어-행동(VLA) 정책에도 그대로 적용할 수 있는가? 적용하기 어렵다면, 소수의 추가 평가만으로 조건을 다시 선택하는 것이 충분한가?

모바일 조작에서는 목표 물체 근처에 도착했더라도 시야·팔의 도달 가능성·접촉 상태에 따라 후속 조작의 성공 여부가 달라질 수 있다. Mobi-π와 MoTo는 이러한 이동과 조작의 연결을 다룬다. 본 연구는 이 연결 문제를 출발점으로, **정책을 교체할 때 기존 내비게이션 종료 조건을 재검증해야 하는 범위와 비용**을 조사하려 한다. 접근 위치 선택이나 기술 간 연결 실패 자체를 새로운 발견으로 주장하지 않는다. [Mobi-π, CoRL 2025](https://proceedings.mlr.press/v305/yang25b.html), [MoTo, CoRL 2025](https://proceedings.mlr.press/v305/wu25c.html).

첫 실험은 Behavior-Skill의 R1Pro 모바일 매니퓰레이터에서 라디오로 이동한 뒤 집는 구간으로 제한한다. 비교 대상은 동일한 π0.5 계열의 12-task 및 50-task Skill 체크포인트이며 각 모델의 정규화 통계를 유지한다. 이동 정책을 고정하고 **조작 정책만 교체**한다. 이는 모델과 정규화 설정을 함께 교체하는 배포 상황의 비교이며, 학습 데이터 규모만의 인과 효과나 서로 다른 로봇 사이의 전이를 검증하는 실험은 아니다. [Behavior-Skill, 2026 preprint](https://arxiv.org/abs/2608.30536), [공개 모델 명세](https://huggingface.co/mafangniu/Behavior-Skill-VLA-Checkpoints/blob/98941096c94b0f978391d8a0accc699c32ec8b2a/README.md).

내비게이션 종료 조건은 목표 물체까지의 수평 거리와 방향 오차로 정의한다. 최초 거리 후보는 0.6·0.9·1.2 m이며 방향 허용치는 공통으로 고정한다. 다음 세 조건을 같은 평가 사례와 시간 제한에서 비교한다. 아래 수치는 연구 설계 초안이며 측정 결과가 아니다.

| 비교 조건 | 새로운 조작 정책에 적용할 종료 조건 |
|---|---|
| 기존 조건 재사용 | 기존 조작 정책의 검증 결과로 선택한 거리 조건을 그대로 사용 |
| 고정 거리 기준선 | 정책 성공률을 이용한 선택 없이 0.9 m 사용 |
| 제한된 재검증 | 같은 후보 중 새로운 정책의 최대 12회 검증 실행으로 다시 선택 |

[추가 비실험 보완](../../../update/PRE_GPU_BUILDUP_REVIEW_2026-10-31.md#remaining-work-review)에서는 calibration 결과가 모두 0이거나 기술적 결측이 남으면 선택 근거 부족을 표시하고 고정 0.9 m fallback과 구별하도록 정했다. A의 선택 자체가 불가능하면 이를 A에 최적화한 설정의 전이 손실로 해석하지 않는다. 기존 평가 4개에서 이진 성공률 차이는 25%p 단위이므로 작은 개선이나 동등성을 확증할 수 없다. 재검증 비용과 향후 반복 사용 규모도 별도로 보고한다. 이 보완은 한 dev P0의 실행 범위를 늘리지 않는다.

실제 이동으로 도달한 상태에서 로봇을 공통 방식으로 정지시킨 뒤, 동일한 상태를 복원하여 두 조작 정책을 비교한다. 전문가 시연의 이상적인 시작 상태로 되돌린 평가와 구분한다. 독립 기술 평가와 연속 실행의 차이는 이미 선행 연구에서 다뤄졌으므로, 차이가 관찰되더라도 그 자체로 신규성을 주장하지 않는다. [Diagnosing Semantic Handoff Failures, 2026; arXiv에 RSS SemRob Workshop으로 표기](https://arxiv.org/abs/2607.06256).

주요 지표는 **전체 시작 사례 대비 이동 후 집기까지 성공한 비율**이다. 이동 실패도 분모에 포함하며, 도착 후 집기 성공률·추가 검증 횟수·물리적 실행 시간·계산 시간을 함께 보고한다. 정책×종료 조건별 결과를 남겨 정책의 전반적 성능 차이와 조건 재사용의 손실을 구별한다. 초기에는 시뮬레이터의 정답 위치로 종료 여부를 판단하므로, 실제 센서만 사용하는 배포 성능으로 일반화하지 않는다.

[GPU 전 데이터·설계 검토](../../../update/PRE_GPU_BUILDUP_REVIEW_2026-10-31.md#mobile-policy-transfer)에서 평가 episode 10개가 모두 같은 scene model·instance template을 사용함을 확인했다. **기존 2/4/4 분할은 독립 장면 평가로 사용할 수 없다.** 일부 시연의 이동 종료와 집기 시작 사이에도 annotation 프레임 차이가 있어 집기 snapshot을 실제 이동 직후 상태로 취급하지 않는다. 첫 dev는 유지하고, 후속 2/4/4의 역할은 동일-template 안의 개발/조건 선택/선택 후 기술적 평가로 좁혔다. 새로운 scene 일반화에는 추가 group이 필요하다.

현재는 문헌 비교와 초기 평가 설계를 마쳤고, **이 주제의 native 정책 실행·성능 비교는 아직 수행하지 않았다.** 10월 31일 공통 로컬 환경 재확인에서도 Docker는 Linux ARM64였으며 NVIDIA GPU 할당이 exit 125로 실패했다. 이는 실행 자원의 한계이며 연구 가설의 반증이 아니다. [최신 환경 확인](../../instruction_revision/재현%20방법/LOCAL_CHECK_2026-10-31.json).

GPU 확보 후에는 CUDA·RTX 렌더링이 가능한 Linux x86-64 로컬 Docker에서 simulator와 정책 서버의 환경 분리·통신 연결·동일 상태 복원 구현을 먼저 완료한다. 현재 자원 점검 스크립트와 설정은 있지만 native image·전환 adapter는 미구현이다. 첫 실행은 한 사례의 이동→정지→두 조작 정책 실행으로 제한해 관측·제어·복원과 기본 능력을 확인한다. 이후 물리 상태 중복과 위 분할의 해석 범위를 확정한 뒤 세 조건을 비교한다. 패키지·모델·simulator 설치와 실행은 Docker 안에서만 수행한다. [환경 설정·재개 절차](../재현%20방법/README.md#execution).

기대하는 기여는 정책 교체 시 접근 조건의 재사용 가능성과 재검증 비용을 정량화하는 것이다. 기존 조건 재사용에 손실이 있고 적은 재검증으로 회복된다면 그 발생 조건을 조사한다. 고정 거리만으로 충분하거나 차이가 작으면 그 결과에 맞춰 범위를 조정한다. 작은 표본의 무차이는 동등성 증명이 아니며, 한 로봇·동일 모델 계열의 결과를 다양한 embodiment로 일반화하지 않는다.

남은 buildup은 **실행 확인 → 작은 공정 비교 → 선행 대비 얻은 지식·한계 검토 → 진행·수정·중단 판단**이다. GPU 확보나 한 사례 실행만으로 완료되지 않는다. 독립 연구자 피드백도 아직 받지 않았으며, 본격 연구로 확대할 때 그 검토를 포함한다.

11/01 [세 후보 비실험 완결 검토](../../../update/THREE_CANDIDATES_NONEXPERIMENTAL_2026-11-01.md#handoff)와 [단일 비교 계약](../재현%20방법/COMPARISON_CONTRACT.json)에서 선택·분석 규칙을 통합했다. 유한 calibration으로 얻는 **재선택 이득은 참 최적 조건 대비 손실과 다르며 음수일 수도 있다.** 선택 동률 비용은 실패까지 포함한 모든 예정 실행의 시간이고, 같은 종료 조건의 A/B 상태 공유와 서로 다른 종료 조건이 만드는 상태 차이를 구분한다. 미구현 adapter·실제 효과·독립 외부 피드백은 남아 있다.

이전 설계와 source의 역사는 [실험 설계 문서](README.md#design-history), 현재 작업 상태는 [TODO](../../../../TODO.md)를 따른다. 이 문서는 연구 개요이며 별도의 우선순위 목록이나 실행 manifest가 아니다.

<a id="closest-work"></a>

<a id="closest-work-1-한-장-비교-무엇을-실제로-교차했는가"></a>
### 1. 한 장 비교 — 무엇을 실제로 교차했는가

표의 결과는 **저자 보고**이며 이 저장소의 재현 결과가 아니다. 같은 이름의 success라도 서로 다른 목표·분모·시작 상태이므로 논문 간 점수를 합치지 않는다.

| 논문 / 지정 근거 | 조작 시작 상태와 정책 | 보고된 비교 축·정책 정보 | 성공 판정·분모 | 비용과 해석 경계 |
|---|---|---|---|---|
| **Mobi-π**, [CoRL 2025](https://proceedings.mlr.press/v305/yang25b.html), [arXiv v2 §3–6·8, App. C–E](https://arxiv.org/html/2505.23692v2) | Base placement 후 조작. Sim은 task별 BeT 계열, real은 Diffusion Policy. 초기 arm 자세와 base–camera transform 가정 | LeLaN/VLFM/BC w Nav/제안법. 시연 첫 이미지 사용; 언어별 이미지 filtering도 부록에 설명 | Sim task success; real navigation/grasp/full success 구분. Human baseline은 사람이 고른 pose에 초기화하는 절차 | Task horizon 500 명시. Mapping·3DGS 학습·pose search가 필요; 동일 총시간 예산 비교로 해석 불가. 같은 task의 VLA 교체 실험은 확인 구간에 미보고 |
| **MoTo**, [CoRL 2025](https://proceedings.mlr.press/v305/wu25c.html), [arXiv v1 §4–5, App. A–B·D](https://arxiv.org/html/2509.01658v1) | 탐색 뒤 docking. OVMM에서는 container 발견 이후 MoTo 적용. Home-Robot/OpenVLA; real AnyGrasp/iDP3/RDT-1B | **Table 1에 {Home-Robot, OpenVLA} × {L3MVN, MoTo}가 이미 있음.** OpenVLA 등 downstream fine-tuning도 있음 | Partial SR은 앞 단계 성공 조건부; Overall SR은 전체 episode. Real subgoal completion과 task success 구별 | Step 보고. RGB와 point-cloud 정책은 입력·학습이 달라 architecture만의 효과 아님. 일반 plug-in 비교를 미연구라고 주장할 수 없음 |
| **Semantic Handoff**, [2026 preprint §III–V, App. diagnostics](https://arxiv.org/html/2607.06256v1) | Clean skill snapshot 대 preceding skill의 실제 terminal state; π0.5 skill-group checkpoints | 같은 checkpoint의 isolated/composed 평가; reached-area/arm-reach verifier ablation | Isolated: human-reviewed VLM 판정. Task: BDDL. Failure category는 verifier-derived | Skill budget + 전체 demo 길이의 2배; verifier cadence 200 steps. 실패/재시도 trace가 있으나 두 VLA의 동일 도착 상태 비교와는 다름 |
| **Behavior-Skill**, [2026 preprint §III-B–C·IV](https://arxiv.org/html/2608.30536v1) | 시연 중간 상태 복원. π0.5/GR00T N1.7 | **2정책 × Task/Skill 언어·학습 조건**. 각 architecture 안에서 조건을 맞춤 | Skill BDDL을 매 step 확인, 최초 충족 시 종료. TSCR/STSR은 독립 복원 skill의 평균 | Skill 시연 길이의 2배 horizon. 앞 navigation 실패를 겪지 않고 모든 skill을 평가하므로 end-to-end 성공 분모가 아님 |
| **ActiveAlign**, [2026 preprint §III–V, Tables I–VI](https://arxiv.org/html/2610.23378v1) | 한 번의 pre-contact wrist-view 선택 후 시작; mobile base docking 자체는 아님 | **4 VLA × Standard/Naive Active/ActiveAlign**. 마지막 조건은 학습 데이터·weights도 변경; matched-state/data controls 존재 | LIBERO completion checker; perturbed/prescribed starts 별도. 성공 replay로 training endpoint를 선별 | Suite별 rollout horizon과 AP 길이 sensitivity는 있음. AP·정렬·추론을 포함한 동일 총 물리 시간 비교는 확인 구간에서 미확인 |

Mobi-π의 §5.2와 §6.1에는 각각 held-out 5 scenes와 evaluation 10 scenes 표현이 있다. 여기서는 임의로 하나로 정합하거나 원자료 표본 수로 재집계하지 않는다. MoTo의 세부 OpenVLA 학습량 표기도 단위 해석을 더하지 않고 fine-tuning 존재만 사용했다. 이 차이들은 이번 탐색을 중단할 이유가 아니라, 나중에 해당 protocol을 재현할 때 확인할 항목이다.

<a id="closest-work-2-보고됨미보고미확인을-구별한-결과"></a>
### 2. 보고됨·미보고·미확인을 구별한 결과

`미보고`는 **위 지정 구간에서 해당 비교를 찾지 못했다**는 뜻이다. 전체 문헌의 부재 증명이 아니다. `미확인`은 현재 자료만으로 공정성·원자료 연결을 결정할 수 없다는 뜻이다.

| 확인할 비교 | 이번 확인 | HANDOFF에 주는 판단 |
|---|---|---|
| 이동 방법 × 조작 정책의 교차 비교 | **보고됨:** MoTo Table 1, real §5.3 | 처음부터 2×2 표를 만드는 것만으로 새 기여가 되지 않는다. 두 downstream 모두에서 MoTo가 L3MVN보다 높은 overall SR을 보고하므로 이 표를 순위 역전의 증거로 쓰지도 않는다. |
| 여러 VLA × upstream 관측 조건 | **보고됨:** ActiveAlign Table II | 단순 backbone 확장도 이미 있다. Adapted 결과는 frozen 정책 교체와 분리한다. |
| 독립 skill 능력과 연결 실행의 차이 | **보고됨:** Semantic Handoff; Behavior-Skill은 독립 복원 평가 제공 | “개별 성공이 연결 성공을 보장하지 않는다” 자체를 새 발견으로 삼지 않는다. |
| 같은 완전한 도착 상태를 복원해 여러 frozen VLA를 공통 goal로 비교 | **미보고:** 위 5편의 확인 구간에서 이 형태의 mobile docking 비교는 확인하지 못함 | Base pose만 같은 것으로 충분하지 않다. Arm·object·camera·직전 접촉·policy history도 비교 범위에 기록해야 한다. 이는 후속 통제 조건이며 초기 후보 자격 조건이 아니다. |
| A에서 선택·동결한 도착 설정을 B에 그대로 이전하고, 제한된 B 검증으로 재선택한 설정과 비교 | **미보고:** 확인 구간에서 명시적인 source→target 재사용/재선택 및 그 비용 비교를 찾지 못함 | 아래 작은 질문을 남긴다. 이 조합의 부재만으로 독창성이나 논문 가치를 확정하지 않는다. |
| 논문 간 동일 장면·seed·실패·budget의 episode-level 연결 | **미확인:** 원자료/실행 interface 감사는 이번 범위 밖 | 서로 다른 논문의 aggregate 점수를 빼서 교체 손실을 계산하지 않는다. |

<a id="closest-work-3-남기는-작은-질문과-비교-초안"></a>
### 3. 남기는 작은 질문과 비교 초안

**연구자 질문:** 같은 로봇·task에서 VLA A 기준으로 선택한 도착 설정을 B로 교체한 뒤에도 재사용할 수 있는가? B가 기준 시작 상태에서 더 잘한다는 사실이 실제 도착 분포에서의 개선을 예측하는가? 재검증이 필요하다면 소수의 B validation 결과로 충분한가?

이 질문의 답은 배포 시 이동 모듈 재사용, checkpoint 교체 검증, 추가 rollout 수집을 결정하는 데 쓰인다. 기존 성능표를 하나 더 만드는 것보다 **재사용 결정에 실제로 도움이 되는 정보**를 목표로 한다. 효과 방향은 정하지 않는다. 안정적으로 재사용되는 결과도 유용할 수 있지만 단순 null result만으로 출판 기여를 보장하지 않는다.

아래는 **설계 초안**이며 checkpoint·환경·threshold·표본 수가 동결된 실행 계획은 아니다.

| 항목 | 최소 비교 |
|---|---|
| 범위 | 한 embodiment, 공통 task·관측/action interface를 지원하는 frozen VLA A/B. 첫 비교에서 로봇까지 바꾸지 않음 |
| 도착 후보 | 동일한 작은 후보 집합에서 geometry/IK/충돌 기준과 공통 시연 시야 검색 기준을 사용. 기존 Mobi-π/MoTo는 선행 baseline 계보로 포함 |
| 재사용 | 별도 calibration scene에서 A로 선택한 설정을 동결하고 B의 held-out scene에 그대로 적용 |
| 강한 단순 대안 | 정책과 무관한 geometry+시야 기준; **같은 후보에서 제한된 B calibration으로 단순 재선택**. 새 learned score나 RL 없이 시작 |
| 관측할 결과 | Reference 시작 상태와 실제 도착 상태에서 A/B의 task 성공·불확실성, A 설정 재사용 대 B 재선택의 차이, 추가 calibration 비용. 정책의 전체 강약과 도착 설정 차이를 분리 |
| 공정한 범위 | 각 도착 후보에서 A/B를 비교할 때 완전한 시작 상태를 공유; 후보 간 상태 차이는 평가할 개입. 동일 task checker·후보 집합·scene split·총 물리 시간. Mapping/검색/추론 비용은 별도 보고. 도착 실패도 전체 분모에 포함하고 도착 이후 조건부 성공은 따로 기록 |
| 선택 편향 방지 | 설정을 고른 calibration 결과를 test 효과로 다시 쓰지 않음. 실패한 pose를 제외하거나 각 정책의 성공 pose만 비교하지 않음. Frame 수를 독립 scene 수로 세지 않음 |
| 해석 | 정책 간 차이만으로 architecture 원인을 주장하지 않음. Re-selection이 충분하면 그 단순 대안을 채택. 새 가설을 탐색에서 얻었다면 새 장면/holdout으로 후속 검증 |

통계적 재선택이나 regret 개념 자체는 새로운 방법이 아니다. 기존 C6의 교훈을 재사용한다. 연구로 발전시키려면 재사용 판단이 틀리는 범위 또는 안정적인 범위를 실제로 보여 주어야 한다. **그 효과를 지금 미리 입증해야만 탐색할 수 있다는 뜻은 아니다.**

<a id="public-interface"></a>

<a id="public-interface-1-확인-범위와-공개-자산"></a>
### 1. 확인 범위와 공개 자산

[Behavior-Skill 본문 §III](https://arxiv.org/html/2608.30536v1)는 human demonstration의 skill 경계 상태를 복원해 독립 평가하는 방법을 설명한다. 논문상 π0.5/GR00T 비교와 실제 공개 모델 제공 여부를 구별했다. 확인한 논문은 **2026 arXiv preprint**이며 conference acceptance를 추정하지 않는다.

| 자료 | 이번에 확인한 고정 지점 | 확인 경계 |
|---|---|---|
| [공식 benchmark](https://github.com/nubot-nudt/Behavior-Skill/tree/d3593788bdc7bd3016d307ea9529fdb500c146ba) | `d3593788bdc7bd3016d307ea9529fdb500c146ba` | README, 파일 목록, evaluator·restore·observation·websocket·예시 config/manifest 7개 지정 구간. 전체 simulator나 모든 task를 검증한 것은 아님 |
| [공식 연결 π0.5 server](https://github.com/mafangniu/pi05-behavior-skill/tree/7ca6eace02aaba2d8ce19af600b85dd04a60d720) | `7ca6eace02aaba2d8ce19af600b85dd04a60d720` | serve entry·입출력 transform·B1K wrapper 3파일. Checkpoint load/normalization 내부와 controller 전체는 미검증 |
| [checkpoint release](https://huggingface.co/mafangniu/Behavior-Skill-VLA-Checkpoints/tree/98941096c94b0f978391d8a0accc699c32ec8b2a) | `98941096c94b0f978391d8a0accc699c32ec8b2a` | Card/API 목록에 π0.5 task/skill × 50/12의 네 directory. 이 공식 연결 release에서 GR00T checkpoint를 식별하지 못함. 전 세계 미공개의 증명 아님 |
| [평가 자료 release](https://huggingface.co/datasets/mafangniu/Behavior-Skill/tree/0be968d3b61406ec366e1bcf7f50a9aa36bbc56f) | `0be968d3b61406ec366e1bcf7f50a9aa36bbc56f` | Card/API 목록 확인. 50 task·500 demo의 평가 config/snapshot 공개라는 설명이며 payload 무결성·복원 성공은 확인하지 않음 |

<a id="public-interface-2-연결-상태"></a>
### 2. 연결 상태

| 연결 | 확인한 사실 | HANDOFF에 남은 부분 |
|---|---|---|
| Task–두 정책 | R1Pro용 skill goal/instruction과 π0.5 server 연결 존재. 공개 checkpoint 목록은 π0.5 네 변형 | π0.5–GR00T 쌍 미확보. 두 π0.5 skill checkpoint는 후속 **범위 축소 후보**이며 현재 원래 쌍의 대체 검증으로 처리하지 않음 |
| 정책 입력–action | Websocket이 skill instruction을 `prompt`로 전달. Wrapper가 head/두 wrist RGB와 proprio를 구성하고 B1k transform은 23개 state 성분·앞 23개 action 출력을 사용 | Controller별 action 단위/순서·normalizer 내용·실제 tensor 호환·두 checkpoint 공통 task는 미검증. 차원 일치만으로 의미 호환을 확정하지 않음 |
| 시연 상태–복원 | Scene restore, grasp 복원, 정지/안정화 후 관측 생성. 매 skill/episode 시작에 restore와 policy reset | 복원 가능한 시연 경계와 실제 정책의 navigation terminal state는 다름. Scene/RNG/controller·policy cache를 포함한 동일 도착 분기는 미구현 |
| Navigation–조작 | `turning_on_radio/episode_00000010`에서 navigation skill 0 끝 frame 265와 pickup skill 1 시작 frame 265가 이어짐 | **시연 annotation의 인접성**이다. 공개 runner는 skill 0 rollout 결과 대신 skill 1의 시연 snapshot을 복원. 실제 handoff witness 없음 |
| 설정–선택 | 공통 skill goal·instruction을 지정할 수 있음 | Docking 후보 생성·A 선택/동결·B 재사용/재선택 API와 split/cost ledger는 확인 경로에 없음 |
| 결과–비용 | Skill success/n_steps와 running statistics 저장, duration 기반 horizon | Navigation 실패를 포함한 전체 분모·조건부 조작 성공·이동/재검증 비용·동일 도착 ID는 추가 설계 필요. 기존 n_steps를 end-to-end 비용으로 사용하지 않음 |

<a id="public-interface-3-구현을-시작하기-전에-알아둘-차이"></a>
### 3. 구현을 시작하기 전에 알아둘 차이

**실제 도착 상태를 전달하는 코드가 필요하다.** [evaluator의 초기화](https://github.com/nubot-nudt/Behavior-Skill/blob/d3593788bdc7bd3016d307ea9529fdb500c146ba/benchmark/core/evaluator.py#L183-L215)와 [episode 시작](https://github.com/nubot-nudt/Behavior-Skill/blob/d3593788bdc7bd3016d307ea9529fdb500c146ba/benchmark/core/evaluator.py#L237-L244)은 저장 skill 상태를 복원한다. Batch에서 같은 environment 객체를 재사용해도 물리 trajectory가 이어진다는 뜻은 아니다. [예시 manifest](https://github.com/nubot-nudt/Behavior-Skill/blob/d3593788bdc7bd3016d307ea9529fdb500c146ba/data/skill_init_states/task-0000/episode_00000010/state_manifest.json)는 `extraction_mode: replay`, 원본 human HDF5와 frame 경계를 기록한다. Directory의 `00000010`과 내부 `episode_id: 0`을 임의로 같다고 해석하지 않고 source path·task·skill·frame을 함께 사용해야 한다.

**복원 시 물리 상태가 가공된다.** [loader](https://github.com/nubot-nudt/Behavior-Skill/blob/d3593788bdc7bd3016d307ea9529fdb500c146ba/benchmark/states/loader.py#L70-L141)는 scene 복원 후 grasp/joint 보정, `keep_still()`과 25 physics step 등의 처리를 한다. 따라서 실제 도착을 저장하더라도 이 loader를 그대로 쓰면 순간 도착 속도·접촉을 그대로 보존한다고 주장할 수 없다. 후속 설계는 즉시 handoff와 공통 정지/안정화 후 handoff 중 하나를 선택하고, 안정화 시간을 비용에 포함해야 한다. Dataset card의 NPZ 설명은 alignment metadata 중심이다. Scene JSON 없이 NPZ만 있으면 충분하다고 간주하지 않는다.

**언어 전환과 행동 queue 전환은 별개다.** [B1K wrapper](https://github.com/mafangniu/pi05-behavior-skill/blob/7ca6eace02aaba2d8ce19af600b85dd04a60d720/src/openpi/shared/eval_b1k_wrapper.py#L259-L328)는 injected prompt를 우선하지만 `receeding_horizon`에서 남은 queue가 있으면 새 추론 없이 기존 action을 반환한다. [reset](https://github.com/mafangniu/pi05-behavior-skill/blob/7ca6eace02aaba2d8ce19af600b85dd04a60d720/src/openpi/shared/eval_b1k_wrapper.py#L92-L99)은 wrapper queue 등을 비운다. 연속 navigation→pickup에서는 목표 전환 시 queue 처리와 새 관측 취득을 명시해야 한다. 이를 아직 runtime에서 검증하지 않았다. 별도 reasoner를 켜는 `fine_grained_level > 0`도 단순 prompt 비교와 다른 조건이다.

**평가 종료와 영상 끝은 같지 않을 수 있다.** [평가 loop](https://github.com/nubot-nudt/Behavior-Skill/blob/d3593788bdc7bd3016d307ea9529fdb500c146ba/benchmark/core/evaluator.py#L249-L319)는 step 0의 goal 충족을 경고하며 자동 제외하지 않는다. 영상 기록 경로에는 결과 판정 뒤 마지막 action으로 최대 5번 더 `env.step`을 호출하는 부분이 있다. 이 추가 step은 보고된 success/n_steps에 다시 반영되지 않는다. 영상 마지막 frame을 handoff state로 삼지 말고 판정 시점·후처리 이전 상태를 따로 정의해야 한다. 또한 missing state/goal과 exception으로 빠진 skill을 집계 분모에서 누락하지 않도록 해야 한다. 이는 확인한 코드의 연결 주의점이며 논문의 전체 결과 오류를 입증한 것이 아니다.

<a id="design-history"></a>

<a id="design-history-1-범위를-좁힐-근거와-한계"></a>
### 1. 범위를 좁힐 근거와 한계

| 항목 | 확보한 근거 | 해석 경계 |
|---|---|---|
| 두 정책 | [저자 model card](https://huggingface.co/mafangniu/Behavior-Skill-VLA-Checkpoints/blob/98941096c94b0f978391d8a0accc699c32ec8b2a/README.md)는 12/50-task Skill checkpoint를 구분하고 π0.5 초기화를 설명 | 같은 계열의 **checkpoint+normalizer 묶음 교체**다. Architecture 효과·추가 task 데이터만의 인과 효과를 주장하지 않음 |
| 공통 task | [논문 §IV-A/D·Table III](https://arxiv.org/html/2608.30536v1#S4.SS4)는 전체 50-task 평가와 추가 12-task π0.5 평가를 구분하며 `Turning On Radio`를 포함 | 문헌상 평가 범위 연결. 개별 공개 weight의 학습 로그·정확한 train episode 제외 이력은 미확인; Table III 평균을 pickup 단독 성공률로 사용하지 않음 |
| 평가 단위 | [공개 eval 목록](https://huggingface.co/datasets/mafangniu/Behavior-Skill/blob/0be968d3b61406ec366e1bcf7f50a9aa36bbc56f/eval_episodes.json)의 radio 10개 episode와 [skill config](https://github.com/nubot-nudt/Behavior-Skill/blob/d3593788bdc7bd3016d307ea9529fdb500c146ba/data/skill_eval_configs/turning_on_radio/episode_00000010.yaml) | Navigation 0→pickup 1을 비교 전환으로 선택. 실제 장면/instance 중복 및 snapshot 내용은 미검증 |
| 모델 연결 | [loader](https://github.com/mafangniu/pi05-behavior-skill/blob/7ca6eace02aaba2d8ce19af600b85dd04a60d720/src/openpi/policies/policy_config.py#L46-L91)는 checkpoint별 assets에서 normalizer를 읽고 normalize/unnormalize를 적용 | Checkpoint/환경 실행 검증 아님. 같은 normalizer로 강제 통일하면 원래 정책을 바꾸므로 하지 않음 |
| 표현·제어 | [B1K data config](https://github.com/mafangniu/pi05-behavior-skill/blob/7ca6eace02aaba2d8ce19af600b85dd04a60d720/src/openpi/training/config.py#L277-L339), [실제 robot 생성 경로](https://github.com/nubot-nudt/Behavior-Skill/blob/d3593788bdc7bd3016d307ea9529fdb500c146ba/joylo/gello/robots/sim_robot/og_teleop_utils.py#L1484-L1534), [controller 설정](https://github.com/nubot-nudt/Behavior-Skill/blob/d3593788bdc7bd3016d307ea9529fdb500c146ba/joylo/gello/robots/sim_robot/og_teleop_cfg.py#L181-L232) | 공통 추론 설정의 후보를 특정했으나 action slot·gripper 해석·직렬화 복원은 native에서 대조해야 함 |

Server README는 이전 **Openpi Comet** 설명이며 `pt12/pt50` 학습 config도 `fine_grained_level=0`, `episodes_index=range(200)`을 담고 있다. 이를 released Skill 모델의 실제 학습 이력이나 논문의 eval 제외 증거로 복사하지 않는다. 이번 radio 선택은 model card·논문·평가 목록의 연결에 근거한다. 추후 주장도 우선 이 공개 평가 episode에서의 배포 진단으로 제한하며 unseen-training-scene 일반화를 주장하지 않는다.

두 normalizer는 모두 `state/actions × mean/std/q01/q99`의 32성분 배열을 포함하지만 **내용이 다르다**. 확인한 23성분 physical interface와 32성분 모델 표현은 padding/출력 절단으로 연결되는 설계다. [Normalize/Unnormalize](https://github.com/mafangniu/pi05-behavior-skill/blob/7ca6eace02aaba2d8ce19af600b85dd04a60d720/src/openpi/transforms.py#L114-L181)는 해당 차원의 quantile 통계를 사용한다. 배열 길이가 같다는 사실만으로 올바른 학습 통계·실행 호환을 증명하지 않는다.

<a id="design-history-2-한-장-비교-설계-제안-v01-미실행"></a>
### 2. 한 장 비교 설계 — 제안 v0.1, 미실행

**질문:** 고정 navigator가 만드는 radio 접근에서 A로 고른 종료 거리 설정을 B에도 재사용할 수 있는가? 정책과 무관한 고정 거리 또는 소수의 B validation으로 충분한가?

| 항목 | 첫 탐색적 진단의 선택 |
|---|---|
| 범위 | R1Pro·`turning_on_radio`의 이동→집기 전환만. Radio를 켜는 전체 task 성공·다른 robot/architecture 일반화는 다루지 않음 |
| Frozen 정책 | A=12-task Skill, B=50-task Skill. 각자 공개 normalizer 유지. **Navigator N=A를 모든 조건에 공통 고정**하여 downstream checkpoint와 이동 정책을 동시에 바꾸지 않음 |
| 입력 | 공통 head/좌·우 wrist RGB+proprio, 해당 skill instruction. Policy에 새 privileged geometry를 입력하지 않음. 종료 판단에는 simulator target/base geometry를 공통 사용하므로 첫 진단은 **privileged evaluation setting** |
| 도착 설정 K | Horizontal base–radio root 거리 `r∈{0.6,0.9,1.2} m`, target 방향 yaw 오차 `≤30°`. 각 설정은 N의 최초 조건 충족 tick에 전환. 전역 좌표 복사·teleport·임의 합성 pose 없음. 거리 후보는 효과를 보고 고른 값이 아니며 dev에서 접근 가능성만 확인 |
| Navigation 종료 | 첫 skill snapshot에서 N을 실행한다. 기존 `near` success가 먼저 rollout을 끊지 않도록 새 거리 조건으로 종료를 분리해야 함. 미도달/timeout은 그 설정의 navigation 실패. 초기부터 조건을 만족하면 `zero_travel`을 따로 기록해 실제 이동과 구별 |
| 공통 정지/분기 | 도착 tick 이후 base zero command·현재 arm/trunk position 유지·gripper command 유지로 **15 control tick(0.5 s)**의 공통 정지 동작. 물체에 `keep_still`을 적용하지 않음. 그 비용/접촉 변화도 handoff에 포함. 이후 같은 완전한 상태를 A/B에 분기; skill1 시연 snapshot으로 되돌리지 않음 |
| Queue·관측 | 전환 시 navigation action queue를 비우고 skill1 prompt로 새 관측/추론. 양쪽 branch의 controller·physics/RNG·grasp 상태를 보존하고 A/B 정책은 동일한 cold-start 규칙 사용. Snapshot에 이 정보가 없다면 동등한 상태라고 표시하지 않음 |
| 3개 비교 | **Reuse:** A calibration에서 선택한 `k_A`를 B에 사용. **Fixed:** 정책 결과를 보지 않고 `r=0.9 m` 고정. **B-select:** 동일 K·동일 calibration 묶음에서 B의 12회 이하 manipulation validation으로 `k_B` 선택. 새 selector/RL/IK 최적화 없음 |
| 선택 규칙 | Calibration의 **navigation 실패 포함 전환 성공률** 최대. 동률은 누적 물리 tick 최소, 다시 동률이면 `0.9→0.6→1.2` 순서. Test 결과는 선택에 사용하지 않음. `k_A=k_B`이면 같은 선택이라는 결과를 그대로 남김 |
| Goal·분모 | Primary=`navigation 도달 AND pickup BDDL grasped`, 시작 episode 전부가 분모. Secondary=도착률, 도착 조건부 grasp 성공, right-arm grasp 여부, 시연 skill1 시작 reference 성공, 물리 tick/추론 호출/실측 wall time. BDDL grasped와 prompt의 right-gripper 준수는 구별 |
| 시간 한도 | Action/render 30 Hz·physics 120 Hz라는 source 설정을 출발점으로 nav 600 tick(20 s), settle 15, pickup 1,800 tick(60 s). 모든 설정·정책에 같은 한도. Pickup first-hit까지만 평가; 성공 유지/자율 종료 효과는 주장하지 않음 |
| 평가 질문 | Test의 `mean(Y_B(k_B)−Y_B(k_A))`와 `mean(Y_B(k_fixed)−Y_B(k_A))`를 paired episode 단위로 보고. B 재선택 비용을 함께 제시. Reference 성공률은 competence 설명용이며 actual-arrival 성능을 대신하지 않음 |

도착 거리/각도는 별도 learned docking controller를 만들지 않고 **같은 navigation policy의 전환 시점**을 비교하려는 선택이다. 따라서 첫 결과의 범위도 이 navigator·세 거리 설정으로 제한된다. Arm/object/contact까지 함께 달라질 수 있으므로 차이를 시야나 거리만의 인과 효과로 해석하지 않는다. Fixed-distance가 유일하거나 최강의 geometry/IK baseline이라는 주장도 하지 않는다.

<a id="design-history-3-작은-예산과-split-초안"></a>
### 3. 작은 예산과 split 초안

공개 radio 목록은 `00000010, 00000250, 00000470, 00000700, 00000940, 00001250, 00001590, 00001960, 00002600, 00003000`이다. 우선 앞 **2개 dev / 다음 4개 calibration / 마지막 4개 test**의 초안을 둔다. 원본 scene·task instance·중복 episode 연결은 미검증이다. 실행 전 같은 원본 instance가 여러 split에 걸치는지 확인하고, 중복이면 group 단위로 합쳐 split을 **결과 관측 전에** 확정한다. 네 test episode가 네 독립 scene이라는 주장은 하지 않는다.

- Dev는 IO/상태 분기와 도착 설정의 물리적 도달 가능성을 점검한다. 거리 후보 수정이 필요하면 dev에서만 한 번 수정하고 버전을 올린 뒤 calibration/test를 봉인한다. Dev 성공 사례만 남기거나 test를 dev로 바꾸지 않는다.
- 최초 계획 상한은 10 source episode × 3 설정 = **30 navigation**, 같은 도착에서 A/B의 **60 pickup branch**, 각 episode의 시연 시작 reference A/B **20회**다. 한 seed 반복의 **최대 110개 phase**이며 nav 실패 시 pickup은 미실행으로 표시하되 primary outcome은 실패로 남긴다. 정책 seed 반복을 독립 scene 표본으로 세지 않는다.
- 이 중 B-select의 추가 calibration은 **4×3=12 pickup branch**다. A 선택 비용, B 재검증 비용, 공통 navigation 생성 비용, test/audit 비용을 따로 기록한다. 같은 `k`를 여러 arm이 선택하면 test rollout을 중복 계산하지 않는다. Reuse의 B calibration 비용은 0으로 정의하되 실제 전체 연구 비용을 숨기지 않는다.
- 분기 공유로 절약한 실제 계산량과 배포 시 episode별 이동 비용은 별도다. Simulator 시간 한도를 GPU wall time 추정으로 바꾸지 않는다. P0의 runtime/상태 qualification 비용도 별도 기록한다.
- 이 작은 표본은 **현상 탐색**용이다. 작은/0 차이를 “재검증이 불필요하다”는 동등성 증명으로 해석하지 않는다. 양의 차이도 단독 논문이나 광범위한 재사용 손실의 증거로 승격하지 않는다. 새로운 test로 확증하려면 별도 규모/불확실성 설계가 필요하다.

<a id="design-history-4-환경후속-구현에-넘길-최소-조건"></a>
### 4. 환경·후속 구현에 넘길 최소 조건

공통 server code는 `7ca6eace02aaba2d8ce19af600b85dd04a60d720`, benchmark는 `d3593788bdc7bd3016d307ea9529fdb500c146ba`, model release는 `98941096c94b0f978391d8a0accc699c32ec8b2a`다. Normalizer path는 각 checkpoint의 `assets/behavior-1k/2025-challenge-demos/norm_stats.json`이며 SHA-256은 다음과 같다.

| 정책 | Normalizer SHA-256 |
|---|---|
| A / `pi05-pt12-skill` | `2fca7e2050492a9ce911448f50b64da533f273b3798f4e81f0ec08a824e20bef` |
| B / `pi05-pt50-skill` | `4dde119e69123ed865072c71a714095ae746c6d294fefba910a842757a7083ce` |

첫 추론 설정 후보는 두 정책 모두 `pi05_b1k-base`, `control_mode=receeding_horizon`, `max_len=32`, inference wrapper의 `fine_grained_level=0`이다. 마지막 값은 별도 reasoner를 끄는 설정이며 Skill checkpoint를 task-prompt로 바꾸라는 뜻이 아니다. Skill prompt는 caller가 주입한다. `get_config()`는 알 수 없는 이름을 base로 fallback하므로 실제 선택 config 이름을 검증해야 한다. 학습 재현은 이번 범위에 없다.

[제어 설정](https://github.com/nubot-nudt/Behavior-Skill/blob/d3593788bdc7bd3016d307ea9529fdb500c146ba/joylo/gello/robots/sim_robot/og_teleop_cfg.py#L181-L232)은 arm/trunk absolute position, base velocity controller, smooth gripper, assisted grasp 경로다. Robot `action_normalize=False`여도 base controller에는 입력 `[-1,1]`에서 출력 한도 `[0.75,0.75,1.0]`으로의 scaling 설정이 있다. 23 action을 모두 SI velocity나 모두 joint position으로 해석하지 않는다. Model normalizer와 controller scaling을 분리한다.

OS·simulator version 참고는 [통합 환경 설정](../재현%20방법/README.md#execution-고정-근거와-환경-차이)을 따른다. Docker image/driver/GPU memory·weights 무결성·physics 복원은 미검증이다. Comet README의 inference 메모리 안내를 simulator와 두 정책의 총 VRAM 요구로 간주하지 않는다. 실제 준비는 **사용자 선택 컴퓨터의 로컬 Docker**에서만 진행한다.
