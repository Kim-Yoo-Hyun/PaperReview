# D2 buildup — 잡은 물체와 파지 자세가 이후 운반을 바꾸는 조건

- 검토일: 2026-10-22 KST
- 절차: [기존 8단계 buildup](../../../research/IDEA_BUILDUP_GUIDE.md#5-문헌에서-아이디어로-넘어가는-8단계)
- 출발점: [D2 최초 제안](../2026-10-21_vla_directions/README.md#3-후보-비교와-추천)
- **판정: 넓은 신규 방법 채택 NO-GO / 구체적 VLA 진단 질문은 조건부 HOLD.** 문제의 중요성과 새 논문으로서의 차별성은 구분한다. 기존 방법을 충분히 적용해도 남는 현상을 확보하지 못했다.
- 완료: 문헌·가정·공개 interface·해석적 필요 조건·비교/기각 계약을 검토한 비실험 1차 buildup. 정책 효과, 실행 가능성, 외부 연구자 피드백은 미검증이다.
- 산출물: [직접 문헌 비교](./CLOSEST_WORK.md), [주장–증거 계약](./CLAIM_CONTRACT.md), [source identity](./sources_2026-10-22.json), [유지보수 검증](./VALIDATION.md).

## 0. D1에서 전환한 이유

> **같은 날 후속 인계:** 사용자가 D2 후속이 어렵다면 D3를 진행하도록 지시했다. [추가 공개 자산 점검](../2026-10-22_d3_buildup/README.md#0-d2에서-전환한-이유)에서 MoManipVLA 제목의 repo는 README/그림뿐이었고, 기존 대안과 갈리는 task 예측도 새로 확보하지 못했다. D2의 NO-GO/HOLD를 유지하고 [D3 비실험 buildup](../2026-10-22_d3_buildup/README.md)을 진행했다. 아래는 D2 자체의 심사 결과다.

[D1 N1–N4](../2026-10-21_d1_buildup/NONEXPERIMENTAL_REVIEW.md)는 완료되어 있다. 남은 R1은 공개 구현/recipe, R2는 차별적인 task·cue·단순 대안의 한계, F1은 실제 외부 반박에 의존한다. 이번 확인에서 이 판단을 바꿀 새 D1 근거를 확보하지 못했다. 같은 문서·resource preflight를 반복하지 않고 사용자의 조건부 지시에 따라 D2를 검토했다. D1을 영구 폐기하거나 비실험 연구가 원천적으로 불가능하다고 판단한 것은 아니다. D1 E1/E2 HOLD와 기존 결과는 유지한다.

## 1. 해결되면 달라질 일

**로봇이 물체를 안정적으로 잡았더라도, 그 파지 때문에 통로 통과·목표 자세·놓기가 어려워지는 상황에서, 집기 전에 이후 단계까지 고려한 선택을 할 수 있는가?** 불필요한 재파지, 물체 충돌, 이동 후 배치 실패를 줄일 수 있다는 점에서 manipulation–navigation 연결에 적합하다. 그러나 실제 VLA에서 이 실패의 빈도와 크기는 아직 모른다.

최초 범위는 강체, 단일 로봇의 grasp → transport → place다. 유체·변형체·보행 안정성은 제외한다. 두 로봇의 공동 운반 결과를 서로 다른 embodiment 간 전이의 증거로 사용하지 않는다. 여러 로봇으로의 확장은 각 native controller·geometry·competence를 확보한 뒤의 별도 주장이다.

## 2. 판단에 필요한 문헌 집합

| 역할 | 이번에 대조한 문헌 | 확인 수준 |
|---|---|---|
| 기존 기하학·계획 baseline | PDDLStream, ReKep | 공개 README 및 ReKep 본문/부록·source 경로 |
| VLA/mobile interface | MoManipVLA, MoTo | 공식 venue와 관련 method/evaluation 절 |
| 파지–운반의 직접 학습 선행 | Cooperative Grasping | RA-L metadata, 공개 원문·학습/입력 source |
| global/reactive 대안 | G3F | 출판본 abstract/introduction·공식 project; 세부 solver 미감사 |
| 최신 attached-object VLA 충돌 | WBAG, CarryOn | 원문 관련 method/evaluation, 공개 자산 경계 |
| 파지 이후 결과·RL로 좁힌 주장에 대한 반례 | GTP-FA, Foresight Residual RL | 관련 objective·학습 신호·평가·한계 |

공식 CoRL/CVPR/RA-L 및 NeurIPS program을 우선했다. 최신 preprint도 novelty 충돌에서는 제외하지 않았다. Foresight Residual RL의 IROS 2026 표기는 저자 주장으로 분리했다. 정확한 title·version·venue 출처·등록 여부는 [대조표](./CLOSEST_WORK.md)에 있다. 2024–2026 전체 논문을 전수조사한 결과는 아니다.

## 3. 가정과 interface에서 확인한 핵심

ReKep은 keypoint만 비교하는 방법이 아니다. 잡은 물체를 포함한 충돌 비용이 있고, 공개 demo는 simulator geometry를 읽는다. 따라서 이를 제외한 약한 ReKep을 baseline으로 두면 안 된다. [ReKep Appendix A.8–A.9](https://arxiv.org/html/2409.01652v2), [공개 collision 경로](https://github.com/huangwl18/ReKep/blob/63c43fdba60354980258beaeb8a7d48e088e1e3e/environment.py#L221).

또한 충돌을 피하는 필터, 이후 경로가 존재하는 파지, 실제 고정된 정책이 성공하는 파지는 서로 다른 대상이다. 이 구별은 [계약 §1](./CLAIM_CONTRACT.md#1-기하학과-정책-능력을-분리하는-연구자-분석)에 도출했다. 차이가 있다는 사실만으로 새로운 학습법의 필요성이 생기지는 않는다.

## 4. 질문과 경쟁 설명

남길 수 있는 질문은 다음과 같다. **같은 추정 geometry·파지 후보·계산/데이터 예산에서, native VLA가 수행 가능한 파지를 선택하는 데 기존 geometry planner와 supervised outcome ranker 이후에도 설명되지 않는 gap이 남는가?** 이 문장은 신규성 선언이 아니라 재개 심사용 질문이다.

| 가설 | 이를 지지하려면 필요한 관찰 | 우선 비교할 대안 |
|---|---|---|
| H0: 물체 geometry를 빼먹어서 실패한다 | 동일 정책에 attached geometry를 제공하는 것만으로 개선 | VLA + attached-object planner/filter |
| H1: 지금은 안전하지만 이후 경로가 막힌다 | 동일 후보에서 whole-route/placement 검사가 선택을 바꿈 | TAMP·global planner·supervised feasibility ranking |
| H2: 경로는 있지만 native 정책이 실행하지 못한다 | 별도 witness 경로가 있고 같은 시작 상태에서 정책별 결과가 갈림 | Outcome ranking, GTP-FA 계열, foresight/residual 계열 |
| H3: 추정 geometry 또는 접촉 상태의 오차다 | Oracle geometry와 추정 geometry의 결론이 갈림 | 추정 개선·보수적 margin·실행 feedback |

H1/H2는 새로 발견한 현상이 아니다. 이번 작업은 기존 설명을 분리하고, 새 후보가 답해야 할 기준을 높인 것이다. 한 가설이 실패했다고 다른 가설이 입증되는 것도 아니다.

## 5. 직접 충돌과 신규성 판단

| 제안하려던 주장 | 현재 판단 |
|---|---|
| 물체를 붙인 geometry로 VLA를 안전하게 만든다 | ReKep·WBAG·CarryOn과 직접 충돌. 이 자체로는 NO-GO |
| 이후 운반 가능한 파지를 학습해 planner 비용을 줄인다 | Cooperative Grasping과 직접 충돌. 단일 로봇·3D·VLA 추가만으로 충분한 기여라 판단하지 않음 |
| 파지 실패와 실행 실패를 구별해 학습한다 | GTP-FA와 직접 충돌 |
| 다음 단계 성공을 고려한 reward로 VLA residual RL을 한다 | Foresight Residual RL과 직접 충돌 |
| 정보·예산·native executor를 통제하면 기존 방법의 결론이 달라지는 조건을 밝힌다 | 조건부 진단 후보. 실제 task/현상·반대 비교가 없어서 HOLD |

새 논문의 범위를 먼저 ‘mobile’ 또는 ‘cross-embodiment’로 넓혀 충돌을 피하지 않는다. 중요한 차이가 존재할 수는 있지만 그 차이가 왜 단순한 적용 이상의 지식을 주는지 아직 확보하지 못했다. 논문이 존재한다는 이유만으로 D2의 모든 조건이 해결됐다고 결론 내리지 않는다.

## 6. 주장에 필요한 증거와 기각 기준

[비교 계약](./CLAIM_CONTRACT.md)에 다음을 고정했다: policy-visible 입력/privileged evaluator 구분, 공유 후보·결정 시점·허용 행동, geometry/학습/온라인 비용 구분, 독립 outcome, 조합 분할, 경쟁 baseline, 기각 규칙. 이는 **설계 계약이며 executable manifest가 아니다**. 환경 revision, checkpoint, task ID, seed, margin, wall-time budget, sample size는 native 자격을 정하기 전에는 확정하지 않는다.

주요 기각 조건은 단순하다. Attached-object planner로 충분하면 새 planning 방법을 주장하지 않는다. Supervised ranker나 imitation으로 충분하면 RL 필수성을 주장하지 않는다. Geometry만 추가해 생긴 이득, 더 많은 후보·상호작용·oracle 정보로 생긴 이득을 learned representation의 이득으로 보고하지 않는다.

## 7. 가장 약한 연결을 비실험으로 확인한 결과

- **수식 수준:** 강체 물체는 grasp transform으로 기존 충돌 기하학에 포함된다. ‘손은 지나가지만 물체는 못 지나간다’는 해석적 예시는 현상의 가능성만 보이며 새 방법의 필요성을 증명하지 않는다.
- **공개 source 수준:** ReKep의 held-object collision 경로, Cooperative Grasping의 map/footprint/candidate 입력과 supervised loss, CarryOn의 README-only 공개 범위를 확인했다. 총 12개 text 파일의 revision/hash를 기록했다. 코드를 import하거나 실행하지 않았다.
- **Task 수준:** ReKep의 좁은 shelf/holder 예시, Cooperative Grasping의 통로 운반, WBAG의 tabletop 안전 평가, GTP-FA의 ManiSkill3 task를 대조했다. 이들로부터 **공개 native VLA·이동 base·다양한 파지·운반 통로·배치 outcome이 함께 고정된 단일 실행 계약**을 확보하지 못했다. 각 자산의 존재를 조립 완료로 취급하지 않는다.
- **측정 수준:** 유한 예산 planner의 실패는 물리적 불가능의 증거가 아니다. Top-k에서 feasible 후보가 있는 비율은 closed-loop 운반 성공률이 아니다. Safety proxy의 개선은 배치 성공 개선과 다르다.

약한 연결은 GPU만이 아니라 **선행 대비 남는 주장과 비교 가능한 native task**다. 이를 해결하지 않고 Docker 환경 구축·새 학습을 시작할 이유가 없다.

## 8. 내부 반박과 다음 판단

내부 질문 “ReKep에 attached geometry를 켜면 되는가?”, “supervised grasp ranking이면 충분한가?”, “기존 foresight RL을 적용하는 것 아닌가?”에 대해 지금은 충분한 차별적 답을 제시하지 못한다. 따라서 **현재 D2를 새 VLA+RL 방법의 주 연구 주제로 추천하지 않는다**. 분석·문헌은 후속 baseline 선정에 재사용할 가치가 있다.

재개하려면 한 task family에 대해 다음 세 항목을 함께 확보한다.

1. 실제 공개 task와 native executor의 식별자: 어떤 파지 선택이 어떤 이후 운반/배치 결정을 바꾸는지 source 수준에서 특정한다.
2. 기존 planner·ranker·GTP-FA/foresight 설명과 예측이 갈리는 조건: 관측 cue와 사용 가능한 행동도 적는다. 실험 전부터 효과를 입증하라는 뜻은 아니다.
3. 정보·후보·offline label 비용·online budget을 맞출 수 있는 비교와 독립 outcome. 전이가 목표라면 두 embodiment의 대응 계약도 별도 확보한다.

현재 이 세 항목은 미충족이다. 새로운 근거 없이 같은 문헌 반복, 대규모 환경 이식, 진단 질문을 신규 방법으로 이름만 바꾸는 작업은 진행하지 않는다. 실제 동료/지도교수 피드백은 받지 않았으며 외부 연락도 하지 않았다. [TODO](../../../TODO.md)에 D2-B1 완료, 재개 근거 대기와 실험 HOLD를 남긴다. D2 최초 심사 이후의 D3 전환은 위 후속 인계를 따른다.

| Buildup 단계 | 이번 완료 범위 | 남은 범위 |
|---|---|---|
| 1–6 | 문제·문헌·가정·경쟁 설명·신규성·비교 계약 | 새로운 근거에 따른 수정 가능 |
| 7 | 해석적 점검·read-only source/task 경계 확인 | Native competence와 정책 효과: 미실행 |
| 8 | 내부 반박과 NO-GO/HOLD 투자 판단 | 실제 외부 피드백: 미착수 |

문헌에서 확인한 충돌과 interface는 `READING-SUPPORTED`, D2의 잔여 정책 효과는 `CURATION-HYPOTHESIS`다. 사용자 reading status·registry tier는 변경하지 않았다.
