# VLA의 물체 집합 선택과 수량 지시 이행

**현행 투자 판단 — 2026-11-07:** [8개 후보 비교](../../README.md#candidate-priority)의 제한된 평가 예비다. 기여는 수량 benchmark 자체보다 단순 반복 이후 남는 참조·진행·행동 병목에 있다. 다중 물체 능력과 evaluator가 미확인이고 RL 필요성도 없어 현재 주력으로 올리지 않는다.

현행 비실험 상태 검토: **2026-11-05** · [7단계 상태·기여 가설·판단 분기](#buildup-status). 기존 문헌/계약/결과를 대조한 보강이며 새 효과 관측은 없다.

**11/05 통합 판단:** 작은 평가 예비 후보로 유지한다. Spa-Bench의 counting과 기존 조합/기억 선행 때문에 새 수량 benchmark만으로 차별화하기는 어렵다. 기존 Q2/Q4의 D 대 k회 반복 R을 먼저 비교해 수량 해석·대상 참조·진행 상태·운동 능력의 설명을 분리한다. 단순 counter로 충분하면 그 이상 방법을 강제하지 않는다. 이 판단은 native 미실행 때문에 가설을 기각한 것이 아니다.

근거·전체 상대 비교: [기존 6개+새 2개 공백 검토](../../../update/INTEGRATED_GAP_REVIEW_2026-11-05.md). 신규 paper별 확인 절과 status는 [등록 원장](../../../sources/registry_admissions_2026-11-05.json)에 통합한다. 기존 실행 계약·원시 결과·과거 source 날짜는 보존한다.

현재 판단: 비실험 설계 완료·native 기본 조작 및 효과 미검증. P0 이후 첫 비교는 Q2/Q4의 원 지시 D 대 반복 R이며, 다른 비교는 조건부 후속이다. 기존 brief와 source 검토를 한 문서로 통합했다.

[연구 내용](../내용/README.md) · [재현 방법](../재현%20방법/README.md)

<a id="buildup-status"></a>

## 비실험 buildup 현행 상태 — 2026-11-04

**판정: 제한된 탐색 유지 · 의미/비교 설계 정리 · 다중 물체 능력/evaluator/효과 미검증.** [7단계 비실험 절차](../../../../research/IDEA_BUILDUP_GUIDE.md#nonexperimental-workflow)를 기존 문헌·논리·계약에 적용해 정리했다. 아래 상태는 새 실험 결과나 11/04 신규 문헌 전수조사가 아니다.

**한 문단 기여 가설:** 수량 지시가 실패했을 때 새 planner가 필요한지, 같은 정책의 단순 반복으로 충분한지 판단해야 한다. 기여 후보는 **수량 의미·허용 부분집합 선택·진행 추적·조작 능력 중 어떤 요인이 실제 성공을 제한하는지 구별하는 평가 지식**이다. Counting benchmark나 원자 작업 분해 자체는 선행 범위다.

| 비실험 단계 | 상태 | 현재 근거·완료 경계 |
|---|---|---|
| 1 문제·독자 | 정리됨 | [개요](#overview): VLA instruction/evaluation 연구자. EXACTLY-k는 특정 정답 subset 하나가 아니라 허용되는 모든 최종 집합을 판정 |
| 2 가까운 선행 | 지정 범위 확인 | [source 비교](#source-review-nonexperimental-design): ClevrSkills·VLABench·Spa-Bench·순차 조합 coverage. 기존 일반 counting/분해 주장을 제거 |
| 3 질문·대안 | 정리됨 | 수작업 의미 사례·초기 접시 점유·비대상 혼입·파지/안정 상태·지시 전환 방식 검토. 단순 k회 반복과 지각/참조 변경을 구분 |
| 4 기여 서술 | 가설 초안 | D/R의 충분성·실패 범위를 먼저 조사. 반복의 이득을 곧바로 수량 추론 개선으로 이름 붙이지 않음 |
| 5 최소 비교 | 설계됨·미실행 | [비교 계약](../재현%20방법/COMPARISON_CONTRACT.json): 빈 접시 Q2/Q4 D 대 R, 같은 slot/제어 예산. L/A·초기 점유·새 시각 조합은 조건부 후속 |
| 6 실행 부담 | P0 준비 있음·연구 구현 미완 | 단일 물체 P0 recipe/adapter와 다중 물체 실험을 구별. Task generator·최종 집합 observer·반복 wrapper 및 기본 능력 교정 필요 |
| 7 외부 비판 | 질문 준비·미수신 | [기존 질문](../../../update/THREE_CANDIDATES_NONEXPERIMENTAL_2026-11-01.md#set). 의미 사례는 독립 검토자가 검증한 benchmark가 아님 |

**결과에 따른 판단 — 아직 관측하지 않은 분기 포함**

| 다음 증거 | 바뀌는 판단 | 이 증거만으로 하지 않을 주장 |
|---|---|---|
| D가 충분히 성공하거나 R로 해결됨 | 새로운 controller의 필요성을 줄이고 단순 대안의 적용 조건을 기록 | 더 어려운 조건을 사후 추가해 첫 가설을 구제 |
| R의 이득이 특정 대상/참조/전환 선택과 함께 변함 | 수량 해석과 선택·실행 효과를 분리하는 후속 비교로 한정 | 수량 reasoning 향상이라는 단정 |
| 한 물체 능력 또는 정답 reference 대조도 실패함 | Grounding·제어·평가기부터 교정 | 실패 전체를 집합 의미 오류로 집계 |

첫 D/R 비교는 상위 지각 모델 없이 시작하도록 좁혔다. 그러나 반복 wrapper·물리 observer의 공수는 남는다. Fixed slot 시간과 총 행동 예산을 공통으로 두고, 나중에 자동 나열을 넣으면 그 지각·선택·추론 시간도 별도 비용으로 보고한다.

**외부 검토 준비:** 가장 강한 외부 질문은 “이 비교가 Spa-Bench/ClevrSkills의 이미 알려진 분해 이득과 달리 어떤 행동 원인을 구분하는가?”다. Q2/Q4 의미 정답과 D/R 입력·전환 규칙을 함께 보여 준다. 실제 응답·반영이 생기면 내용과 source 위치를 기록한다. 미수신은 작은 탐색을 금지하는 진입 조건이 아니다.

**다음 확인과 문서 종료점:** 첫 구현 주의 판단 자료는 단일 물체 IO와 집합 observer의 논리·물리 일치, D/R의 실제 참조/slot trace다. 반복 전략이 중간에 더 강한 보존 조건을 사용할 수 있음을 밝힌다. 그 전략이 원래 terminal-only task와 모든 경로에서 동등하다는 주장은 하지 않는다. 새로운 직접 선행·자료·반례·피드백 없이 같은 문서 검토를 반복할 내부 과제로 만들지 않는다. 실행 범위·상한은 기존 계약과 [재현 안내](../재현%20방법/README.md)가 관리한다.


<a id="overview"></a>

<a id="overview-vla의-물체-집합-선택과-수량-지시-이행"></a>
## VLA의 물체 집합 선택과 수량 지시 이행

*Object-Set Selection and Cardinality Instruction Following in Vision-Language-Action Policies*

2026-11-01 · 탐색적 실증 연구 후보 · 비실험 문헌·비교 설계 보완 완료, 실제 조작·효과 검증 대기

**핵심 질문:** 익숙한 물체 범주를 대상으로 “모두”와 “정확히 두 개”를 지시할 때, VLA는 조건에 맞는 최종 물체 집합을 만들 수 있는가? 자동 대상 나열이나 단순한 원자 작업 반복으로 충분한가? 개선이 있다면 수량 해석 외에 대상 선택·참조 표현·실행 방식으로 설명되는가?

예를 들어 접시 밖에 배가 세 개 있을 때 “배를 모두 접시에 넣기”는 세 개 전부를 요구한다. “배를 정확히 두 개 넣기”는 세 쌍 중 어느 쌍이든 허용한다. 한 쌍만 정답으로 채점하면 올바른 행동도 실패가 된다. 자동 나열 방법이 집기 쉬운 두 개를 선택해 성공했다면, 실제 시스템으로서는 유용할 수 있지만 수량 이해가 개선됐다는 결론은 별도의 비교가 필요하다.

수 세기·복수 정답·조합적 조작은 새로운 문제가 아니다. [ClevrSkills, NeurIPS 2024 D&B](https://proceedings.neurips.cc/paper_files/paper/2024/hash/439539557e9ba0d04055773ff1f3241c-Abstract-Datasets_and_Benchmarks_Track.html)는 조합적 로봇 과제를, [Spa-Bench, 2026 preprint](https://arxiv.org/html/2610.12696v1)는 수량 조건과 같은 장면의 직접 지시 대조를 다룬다. [Diagnosing Compositional Generalization, CoRL 2026](https://arxiv.org/html/2607.29687v1)도 지시 조합의 학습 범위와 단계별 분해를 분석한다. 따라서 분해 방법 자체를 새 기여로 주장하지 않는다. 잠정 기여는 **자동의 단순 대안이 충분한 범위와 그 이득의 해석을 공정한 행동 비교로 확인하는 것**이다.

첫 탐색은 공개 VLABench π0 정책과 익숙한 과일 범주로 한정한다. 이미 준비한 배 한 개 조작은 입출력·기본 능력 확인용이다. 여러 개의 동일 범주 물체나 색·모양 조합을 다룬 능력을 보장하지 않는다. 기존 빨간 정육면체 사례 8개는 의미 명세로 보존하고, 실제 색×모양 조합 일반화는 해당 입력·행동 능력을 확인한 후 별도로 다룬다. 공개 checkpoint의 전체 학습 노출을 알 수 없으므로 최초 결과를 학습에서 제외된 조합에 대한 OOD 성능으로 부르지 않는다.

| 비교 조건 | 확인할 내용 |
|---|---|
| 원 지시를 받는 고정 VLA | 집합·수량 지시를 그대로 이행하는 정도 |
| 같은 RGB에서 자동 선택한 대상을 한 문장으로 나열 | 자동 지각·선택·명시적 참조를 포함한 전체 시스템의 이득 |
| 위와 같은 대상·순서를 원자 지시로 분할 | 대상 선택을 고정한 상태에서 실행 분해가 주는 차이 |
| 정확히 k개 지시의 단순 k회 반복 | 빈 접시의 제한된 조건에서 더 단순한 규칙으로 충분한지 |
| 정확한 대상 목록을 주는 진단 조건 | 지각·선택 오류를 줄인 뒤에도 참조·실행이 가능한지 |

자동 조건은 evaluator의 물체 ID·정답 집합·성공 신호를 받지 않는다. “가장 왼쪽 물체”는 이동 후 다른 물체를 가리킬 수 있으므로 자연어 참조와 물체 식별의 유효성도 확인해야 한다. 원자 지시의 전환은 사전에 정한 시간 구간으로 시작하며, simulator 정답으로 성공할 때마다 전환하는 조건은 별도의 privileged 진단이다. 모든 비교는 같은 초기 물리 상태·VLA·제어 예산을 사용하고 상위 모델 호출·지연은 추가 비용으로 기록한다.

주 지표는 **공통 종료 시점에 허용된 집합과 수량을 안정적으로 만족한 비율**이다. 잠깐 목표 수를 통과한 것, 파지 중인 물체, 비대상 혼입을 구별한다. 처음 접시에 있던 물체도 최종 수량에 포함하며, 이동 금지가 명시되지 않았다면 물체를 옮겼다가 되돌렸다는 이유만으로 의미 실패로 판정하지 않는다. 실험 중 오류·결측은 분모에서 조용히 제거하지 않는다. 같은 장면의 여러 표현·seed는 독립 장면 수가 아니다.

현재 [문헌·비교·판단 기준 보완](README.md#source-review-nonexperimental-design)과 [기계 판독용 비교 계약](../재현%20방법/COMPARISON_CONTRACT.json)을 작성했다. 논리 사례의 일관성 검사는 실제 정책 검증이 아니다. 외부 연구자에게 보낼 질문은 준비했지만 피드백은 아직 받지 않았다.

**판정은 제한된 탐색 유지다.** 단순 나열·반복이면 충분할 가능성을 먼저 열어 둔다. 선행과 같은 결론만 반복하면 독립 연구로 확대할 이유가 약하다. 선택·참조·제어의 대안 설명을 구분한 뒤 재사용할 만한 경계 조건이 관찰돼야 연구 가치가 강해진다. GPU 부족이나 미관측 효과를 주제의 반증으로 취급하지 않는다.

11/01 [세 후보 비실험 완결 검토](../../../update/THREE_CANDIDATES_NONEXPERIMENTAL_2026-11-01.md#set)에서는 첫 연구 비교를 **빈 접시의 EXACTLY-k 원 지시와 원문 k만큼의 단순 반복**으로 좁혔다. 고정 slot·공통 예산에서 반복이 충분한지를 먼저 보면 상위 지각 모델 없이도 질문을 시작할 수 있다. 같은 subset의 나열/분해는 이동 후에도 참조가 유효한지 확인한 다음 단계다. 반복의 보존 지시는 보수적 중간 전략이며 원래 terminal-only 과제의 모든 경로와 동등하다고 주장하지 않는다. 평가의 논리 불변조건·물리 관측 교정 절차도 계약에 추가했다.

다음 실제 확인은 기존 [Docker 재개 절차](../재현%20방법/README.md#execution)의 단일 dev이며 실행 예산을 확대하지 않았다. Image build·CUDA/EGL·기본 조작은 미검증이고, 집합 과제 생성기·최종 집합 evaluator·반복 wrapper는 미구현이다. 자동 지각/나열은 조건부 후속이다. GPU 확보만으로 buildup이 완료되는 것은 아니다. 활성 작업은 [TODO](../../../../TODO.md)를 따른다.

<a id="source-review"></a>

<a id="source-review-2-공개-source에서-확인한-동작"></a>
### 2. 공개 source에서 확인한 동작

GitHub의 branch를 조회한 뒤 아래 commit의 raw text만 메모리에서 읽었다. 코드를 import·실행하거나 clone·설치하지 않았다. 개별 파일 hash와 읽은 범위는 ledger에 있다. Source의 정적 분기와 실제 물리 동작을 구별한다.

<a id="source-review-clevrskills-task와-언어-표현은-이미-상당-부분-존재"></a>
#### ClevrSkills — task와 언어 표현은 이미 상당 부분 존재

검토 revision: `779aec6822abe79b65a66cbbdf7ecc868aa58b59`.

- [Sort2d L69–155](https://github.com/Qualcomm-AI-research/ClevrSkills/blob/779aec6822abe79b65a66cbbdf7ecc868aa58b59/clevr_skills/tasks/sort_2d.py#L69): 객체마다 대응 texture의 area를 정하고 모든 객체의 Inside2d를 Set으로 묶는다. 일반 분류 표현과 물체별 열거 표현을 같은 task의 prompt list에 제공한다. 이것이 **자동 지각으로 만든 나열 baseline의 실험 결과**라는 뜻은 아니다. 현재 목록은 task 생성기의 정답 identity/배치를 이용한다.
- [Task._sample_int L194–207](https://github.com/Qualcomm-AI-research/ClevrSkills/blob/779aec6822abe79b65a66cbbdf7ecc868aa58b59/clevr_skills/tasks/task.py#L194): `sample=True`이면 범위에서 뽑고 False이면 max를 쓴다. Sort2d의 인자 설명은 반대로 적혀 있으므로 **실제 분기를 기준**으로 한다. Sort2d는 객체 수와 area 수에 같은 flag를 전달해 단일 인자 변경이 두 축을 바꿀 수 있다.
- [Set.evaluate L23–38](https://github.com/Qualcomm-AI-research/ClevrSkills/blob/779aec6822abe79b65a66cbbdf7ecc868aa58b59/clevr_skills/predicates/set.py#L23)는 지정된 predicate의 AND다. 임의의 k개 부분집합 선택이나 추가 비대상 배제와 동치가 아니다. [Inside2d](https://github.com/Qualcomm-AI-research/ClevrSkills/blob/779aec6822abe79b65a66cbbdf7ecc868aa58b59/clevr_skills/predicates/inside_2d.py#L8)는 OnTop을 상속한다. [OnTop L37–66](https://github.com/Qualcomm-AI-research/ClevrSkills/blob/779aec6822abe79b65a66cbbdf7ecc868aa58b59/clevr_skills/predicates/on_top.py#L37)은 resting·정지·미파지까지 보므로 단순 중심점 포함 판정으로 치환할 수 없다.
- [RotateSymmetry L66–110](https://github.com/Qualcomm-AI-research/ClevrSkills/blob/779aec6822abe79b65a66cbbdf7ecc868aa58b59/clevr_skills/tasks/rotate_symmetry.py#L66)는 texture를 공유하는 두 객체의 회전을 명시해 조합한다. 이름만 보고 임의 개수의 attribute set generator로 간주하지 않는다.
- [model factory L383–385](https://github.com/Qualcomm-AI-research/ClevrSkills/blob/779aec6822abe79b65a66cbbdf7ecc868aa58b59/clevr_skills/utils/models.py#L383)는 train/test asset pool을 읽고, top object는 그 pool에서 고른다. [train Sort2d](https://github.com/Qualcomm-AI-research/ClevrSkills/blob/779aec6822abe79b65a66cbbdf7ecc868aa58b59/clevr_skills/assets/asset_splits/train.yaml#L188)와 [test Sort2d](https://github.com/Qualcomm-AI-research/ClevrSkills/blob/779aec6822abe79b65a66cbbdf7ecc868aa58b59/clevr_skills/assets/asset_splits/test.yaml#L66)는 asset/texture 목록이다. 이 사실만으로 quantifier×속성×대상 수 조합 holdout이 구현됐다고 말할 수 없다.

<a id="source-review-vlabench-부분집합-선택과-현재-성공-판정을-구별"></a>
#### VLABench — 부분집합 선택과 현재 성공 판정을 구별

검토 revision: `cf588fe60c0c7282174fe979f5913170cfe69017`. 이는 이번 공개 code 상태이며 ICCV 최종 제출 revision과 동일하다고 확인한 것은 아니다.

- [ClusterConfigManager L192–270](https://github.com/OpenMOSS/VLABench/blob/cf588fe60c0c7282174fe979f5913170cfe69017/VLABench/tasks/config_manager.py#L192)는 두 class에서 객체를 뽑고 두 container의 class 배정을 서로 바꾼 두 결과를 허용한다. [ClusterTask L20–43](https://github.com/OpenMOSS/VLABench/blob/cf588fe60c0c7282174fe979f5913170cfe69017/VLABench/tasks/hierarchical_tasks/composite/base.py#L20)는 이를 OR-of-AND로 만든다. **여러 유효 결과를 허용하는 평가 구조는 이미 있다.** 이것이 n개 중 임의 k개를 고르는 과제와 같은 것은 아니다.
- [Contain/NotContain L43–90](https://github.com/OpenMOSS/VLABench/blob/cf588fe60c0c7282174fe979f5913170cfe69017/VLABench/tasks/condition.py#L43)는 각각 전달받은 identity 목록에만 적용된다. 특정 두 객체의 Contain만으로 세 번째 객체나 비대상이 들어간 경우까지 배제하지 못한다. Exactly-k에는 전체 후보 집합의 cardinality와 비대상 제외가 함께 필요하다. `entities[-1]` 접근도 있어 empty set 사례는 기존 condition에 빈 목록을 넣는 방식으로 처리하면 안 된다. 이는 정적 source 판단이며 실행 중 오류를 관측한 것은 아니다.
- [CommonContainer L46–54](https://github.com/OpenMOSS/VLABench/blob/cf588fe60c0c7282174fe979f5913170cfe69017/VLABench/tasks/components/container.py#L46)의 point 포함 판정과 ClevrSkills의 resting·release 판정은 다른 의미다. 어느 엔진을 쓰든 물리적 최종 판정은 따로 고정해야 한다.
- [task termination L298–303](https://github.com/OpenMOSS/VLABench/blob/cf588fe60c0c7282174fe979f5913170cfe69017/VLABench/tasks/dm_task.py#L298)과 [runner L136–167](https://github.com/OpenMOSS/VLABench/blob/cf588fe60c0c7282174fe979f5913170cfe69017/VLABench/evaluation/evaluator/base.py#L136)는 종료/성공 시 조기 탈출한다. **k를 잠깐 통과한 뒤 초과하는지**는 이 기본 루프의 성공만으로 알 수 없다. 공통 평가 종료 시각 또는 안정화 조건을 지정해야 하며, 이것을 별도 TERM 연구의 재개로 해석하지 않는다. 다른 terminal 원인까지 감사한 것은 아니다.
- 같은 runner는 매 관측에서 [get_instruction L290–295](https://github.com/OpenMOSS/VLABench/blob/cf588fe60c0c7282174fe979f5913170cfe69017/VLABench/tasks/dm_task.py#L290)를 부르며 list이면 하나를 sample한다. 원 표현/나열 표현의 대조에서는 episode 안에서 지시를 고정해야 한다. 이 코드 경로가 이번 특정 task에서 실제 prompt 변경을 일으켰다는 관측은 없다.

<a id="source-review-spa-bench-가장-직접적인-중복과-남은-차이"></a>
#### Spa-Bench — 가장 직접적인 중복과 남은 차이

[본문 §III·Appendix A–B](https://arxiv.org/html/2610.12696v1)는 count×전이 holdout·직접 조작 지시·재진술·무행동 조건을 이미 구별한다. [공개 scene/checklist CT-CF09](https://huggingface.co/datasets/Spa-Bench/spa-bench-data-information)에는 bowl 안 두 물체와 table 위 후보, 특정 물체를 추가/제거하는 직접 대조, 어느 table 물체든 하나를 추가하는 counting 지시가 연결되어 있다. 원본 XLSM/영상/trajectory payload는 받지 않았다.

따라서 **free-choice counting 자체, scene-matched direct 지시, 목표가 이미 충족된 조건**도 새 기여로 세지 않는다. 이번 차이는 속성에 제한된 후보 집합과 all/exactly-k를 조합한 비교다. 확인한 source 범위를 넘어 Spa-Bench 전체에 그 조합이 절대 없다고 주장하지 않는다. Spa-Bench의 무행동 성공은 행동 개시까지 제한하지만, 아래 사례는 최종 집합만 정의하므로 같은 metric이 아니다.

<a id="source-review-3-8개-의미-사례와-공정-비교"></a>
### 3. 8개 의미 사례와 공정 비교

[SEMANTIC_CASES.json](../재현%20방법/SEMANTIC_CASES.json)은 **이번 작업에서 수작업으로 정의한 의미 명세**다. 실제 장면·수집 데이터·정책 실패가 아니며 `executable=false`다. RGB/pose/visibility/reachability는 아직 없다. r1 같은 ID는 evaluator 설명에만 쓰고 정책에 주지 않는다.

U를 장면 inventory, P를 지시 속성을 만족하는 부분집합, S를 최종 tray 구성이라 하면 **all: S=P**, **exactly-k: S⊆P이고 |S|=k**로 정의한다. 지시문에 `no other objects`를 명시했다. 이 표기는 기존 집합 논리이며 새 이론이 아니다. 중간 이동 경로에는 제약을 추가하지 않는다.

| 사례 | 조건 | 유효한 최종 집합 수 | 최소 membership 변경 수 | 비교의 의미/제한 |
|---|---|---:|---:|---|
| Q1 | 빨간 cube 2개, all | 1 | 2 | Q2와 동일 장면·동일 정답 |
| Q2 | 같은 장면, exactly 2 | 1 | 2 | 목표가 같은 quantifier 표현 대조 |
| Q3 | 빨간 cube 3개, all | 1 | 3 | 대상 수와 실행 길이가 함께 바뀜 |
| Q4 | Q3 장면, exactly 2 | 3 | 2 | Q2와 최소 이동 개수는 같지만 선택 자유도 증가 |
| Q5 | 같은 장면, 빨간 object exactly 2; 빨간 cylinder도 대상 | 6 | 2 | 속성 범위와 grasp geometry도 바뀜 |
| Q6 | Q4에 비대상 2개 추가 | 3 | 2 | 목표는 같지만 지각/충돌 난도는 아직 미통제 |
| Q7 | Q4에서 r1은 처음부터 tray 안 | 3 | 1 | 최종 2개와 새로 2번 옮기기를 구별 |
| Q8 | 대상 0개, all; 없으면 tray를 비우도록 명시 | 1: 공집합 | 0 | Empty-set 경계. 최종 성공만으로 무행동을 입증하지 않음 |

여기서 변경 수는 `min |S△S_initial|`이라는 **논리적 하한**일 뿐 robot action·시간·물리적 실행 비용이 아니다. Q7에서 r1을 빼고 r2/r3를 넣는 것도 유효하므로 한 번 추가하는 경로만 정답으로 강제하지 않는다.

Q4의 `{r1,r2}`와 `{r1,r3}`는 모두 정답이다. `{r1,r2,r3}`는 초과, `{r1,r2,b1}`은 비대상 포함, `{r1,b1}`은 총수는 맞지만 속성이 틀려 오답이다. 이는 evaluator가 구별해야 할 **논리적 예**이며 native 판정을 실행한 결과가 아니다.

**단순 나열 대조의 보완:** 정답 집합이 유일한 Q1/Q2에서 표현 차이를 먼저 비교한다. Q4에서 나열 baseline이 하나의 pair를 고르면 free-choice 원 지시보다 선택을 제한하고 물리 난도도 바뀐다. 두 성공률의 차이를 그대로 순수 언어 이해 이득으로 읽을 수 없다. 선택한 subset/순서/추가 관측과 비용을 기록하며, 이후 동일 subset의 실행 능력 진단과 전체 free-choice 성공을 따로 보고해야 한다. 정답 identity·좌표를 자동 baseline에 제공하지 않는다.

<a id="source-review-4-그대로-사용수정새-구현의-경계"></a>
### 4. 그대로 사용·수정·새 구현의 경계

| 경로 | 그대로 재사용할 수 있는 것 | 추가로 필요한 것 | 이번 상태 |
|---|---|---|---|
| ClevrSkills Sort2d | texture 분류·일반/열거 prompt·모든 지정 predicate의 AND | 한 tray의 attribute-selected goal, 임의 k개/비대상/empty 조건, 대상 수와 distractor 독립 sampling, pair별 고정된 prompt·최종 평가 | source 수준 재사용 후보. **8개 사례를 그대로 실행하는 upstream task는 아님** |
| VLABench cluster | 기존 object/container·skill interface, 복수 해답 OR 구조, 공개 policy adapter 경로 | 목표 선택 task/config와 전체 집합 evaluator, stable identity·predicate 경계·공통 종료 계약, checkpoint의 해당 object/skill 능력 확인 | 우선 실행 준비를 검토할 경로. 새 task wrapper가 필요하며 변경량을 아직 측정하지 않음 |
| Spa-Bench Counting | 공개 수량/직접 지시 scene 정의·real-robot 결과를 비교 근거로 재사용 | 이번 필터 조합의 새 real scenes와 적절한 시연/평가; simulator를 공개했다고 가정할 수 없음 | 비교 문헌. 로컬 simulator 실행 경로로 대체하지 않음 |

필요한 확장은 기존 manipulation 엔진 위의 **새 과제·평가 구성**이며, 새 물리 엔진을 요구하는 근거는 현재 없다. 반대로 source 몇 줄 수정만으로 작동한다는 증거도 없다. 기존 train/test asset pool·보이는 객체 수만으로 조합 holdout이 확보되지는 않는다. 모델의 불명확한 pretraining exposure와 새 controlled fine-tuning split을 구별해야 한다.


<a id="source-review-nonexperimental-design"></a>

<a id="source-review-5-비실험-비교채점에서-유지할-핵심"></a>
### 5. 비실험 비교·채점에서 유지할 핵심

| 항목 | 단일 계약에 고정한 내용 | 해석 경계 |
|---|---|---|
| 시작 범위 | 익숙한 범주의 두/세 instance·빈 접시; Q5 속성/geometry, Q6 distractor, Q7 기존 점유, Q8 empty는 확장 | 한 배 조작 P0가 여러 물체·새 asset 능력을 보장하지 않음 |
| D/R 우선 | 원문 k만큼 고정 slot에서 한 물체 지시, 총 제어·query 예산 공통, oracle 성공 전환 금지 | 분할·queue·보존 subgoal이 함께 달라짐; 순수 수량 추론 효과 아님 |
| L/A 후속 | 같은 초기 RGB의 예측 inventory·subset·순서·참조를 공유 | D/L은 대상 선택을 포함한 pipeline 효과; 쉬운 subset 선택도 따로 기록 |
| 정보 | Evaluator ID·정답 mask/pose·native 성공을 자동 조건에 제공하지 않음 | 내부 track key만으로 VLA의 물체 참조가 해결되지 않음 |
| 채점 | 전체 inventory의 기하적 점유 G와 안정 배치 S를 분리; terminal window에서 G=S이고 허용 가족에 속해야 성공 | 잡힌 비대상 누락·first-hit를 최종 성공으로 처리 금지 |
| 시간 | 공통 H 제어 + W hold, 현재 손가락/관절 상태 유지; 강제 release 없음 | H/W·geometry/contact/속도 tolerance는 별도 dev 교정 후 비교 전에 동결 |
| 선택 자유 | EXACTLY-k에서는 가능한 모든 k-subset 허용, 선택되지 않은 eligible은 자동 오류 아님 | 고정 subset 대조는 원래 자유선택 과제를 제한한 별도 조건 |
| 오류·통계 | 모든 예정 시도·관측·기술 결측·성공 분모, paired 결측 범위와 조건부 결과 병기 | 같은 ancestor의 seed/표현은 독립 장면 아님; 작은 N의 무차이는 동등성 아님 |
| 비용·추적 | scene/snapshot/RNG·case/arm/prompt·선택/참조·source/checkpoint·control/query/상위 token·latency·종료 집합 기록 | 추가 지각·반복 비용을 숨기지 않음 |

Q7 확장에서는 기존 안쪽 물체와 새 최종 집합의 차이를 보고 제거·추가 모두 다뤄야 한다. Q8의 최종 empty와 no-action은 다르다. 중간 이동 금지가 없는 terminal-only 지시에서 비대상을 옮겼다가 돌려놓은 것을 자동 의미 위반으로 세지 않는다. 집합 최소 대칭차는 실제 motor action 수가 아니다.

N1에서는 기존 8개 추상 사례의 가능한 최종 집합 292개를 문서 정의와 대조했다. ALL/EXACTLY-two의 조건부 동치, 자유 subset, 비대상 혼입, 일시 성공 뒤 초과, 파지 중 혼입, 초기 점유, empty/no-action 반례를 점검했다. 이것은 **의미 명세 일관성**이며 실제 scene·simulator·parser·정책 검증이 아니다.

<a id="source-review-추가-선행과-source-경계"></a>
#### 추가 선행과 source 경계

- [RoboMME 공식 abstract](https://proceedings.mlr.press/v306/dai26c.html)의 history-dependent memory 범위와 현재 보이는 집합을 구별한다.
- [MESA 저자 project](https://www.pair.toronto.edu/MESA/)는 언어/공간·distractor 비교 근거다. 당시 CoRL 2026 저자 표기의 공식 확인은 미완료였으며 이번 신규 등록 대상이 아니다.
- [순차 조합 진단](https://arxiv.org/abs/2607.29687)은 coverage·context/action shift·단계 분해의 선행이다. N1은 v1 지정 절을 확인했고, REG-R6 등록은 최신 v2 abstract와 공개 소개를 기준으로 한다. 11/03 [공식 CoRL accepted list](https://www.corl.org/program/accepted-papers)에서 exact title/forum을 확인해 기존 pr-1080을 CoRL로 갱신했다. Spotlight와 final-text 동일성은 별도 확인하지 않았으며 N1의 당시 분석 범위는 유지한다.
- N1에서 확인한 release `e29c4447…`의 [success.py](https://github.com/YixiaoWang7/Diagnosing_Compositional_Generalization_Robot/blob/e29c44474495b341d19636bbf90f3cf0fcb1d2d2/projects/corl2026_cg/src/corl2026_cg/evaluation/success.py)는 복수 container와 stage success를, [config 안내](https://github.com/YixiaoWang7/Diagnosing_Compositional_Generalization_Robot/blob/e29c44474495b341d19636bbf90f3cf0fcb1d2d2/projects/corl2026_cg/configs/README.md)는 공개 baseline과 논문 sparse-coverage 설정의 차이를 설명한다. 저자 release를 논문 전체 재현이나 frozen VLA와 동일한 실험으로 취급하지 않는다.

<a id="source-review-6-결과별-판단과-남은-일"></a>
### 6. 결과별 판단과 남은 일

D가 충분하면 추가 방법 동기가 약해진다. R/L이 충분하면 간단한 interface와 비용/조건 지식의 가치를 본다. A가 특정 subset·참조·slot에서만 좋아지면 그 대안 설명부터 분리한다. Oracle 직접 지시도 실패하면 기본 조작·참조를 먼저 확인한다. 선행과 동일한 결론만 남으면 독립 주제 투자를 줄인다.

현재 처리 가능한 문헌·논리·분석 설계는 완료했다. 외부 검토용 반대 주장·질문은 [세 후보 통합 검토](../../../update/THREE_CANDIDATES_NONEXPERIMENTAL_2026-11-01.md#set)에 있다. 실제 외부 피드백, 기본 능력, 물리적 교정과 효과는 미확인이다. 자원 부족은 가설의 반증이 아니며 같은 문헌/실패 probe를 반복하지 않는다. 실제 재개는 [P0 안내](../재현%20방법/README.md#execution)·[TODO](../../../../TODO.md)를 따른다.

<a id="source-review-7-탐색검증-이력의-핵심-보존"></a>
### 7. 탐색·검증 이력의 핵심 보존

- 최초 탐색에서 양팔 역할 반전은 TwinVLA·BiRoAD의 기존 적응/대조와 겹쳐 미선정, 도구 전이는 Semantic Contact Fields·Creative Robot Tool Use의 알려진 범위를 넘어선 비교를 정하지 못해 미선정했다. 분야 전체 NO-GO는 아니다. 링크·확인 수준은 탐색 ledger에 보존했다.
- GAP-SET-R1은 ClevrSkills/VLABench/Spa-Bench source와 8개 사례를 심사했고, 당시 두 GPU 후보 외에 SET의 최소 준비를 제안했다. 당시 최대 2회 제안은 이후 P0의 **1회·200 step·40 inference**로 구체화되어 더 이상 실행 기준이 아니다.
- GAP-SET-N1은 범주부터 시작하는 비교·subset/참조·최종 집합·분모/비용/split을 보완했다. PRE-GPU-3에서 D/R 우선·동적 참조·교정 절차를 추가했다. 단계 8의 독립 피드백까지 완료된 것은 아니다.
- 원래 SCOUT/R1/N1은 모델·simulator·parser·Docker 실행 없이 문헌/정적 code/문서 정합성을 확인했다. 세 단계의 registry는 당시 1,077편·표준 노트 5,385개였고 repository audit는 오류·경고 0이었다. 보호 파일은 각 단계 20개(계획 날짜 한 줄 외 보존)/20개/29개이며 사용자 읽기 기록·기존 준비 packet을 유지했다.
- 최초 준비와 재점검의 실제 Docker 결과는 별도 [P0 준비 통합 기록](../재현%20방법/README.md#preparation-history)에 보존한다. 이 문서 병합은 새로운 실험이나 과거 evidence 승격이 아니다.
