# GAP-S3 — VLA 이동·조작 탐색과 과거 후보 재검토

- 확인일: **2026-10-28 KST / 비실험 탐색 DONE**.
- 사용자 요청: 탐색 진입 기준을 낮추고 결과의 증거 기준은 유지한다. 과거에 보류·종료한 주제도 재검토한다.
- 결과: **새 질문 1개와 재탐색 질문 2개를 보존한다.** 다음 우선 작업은 GAP-HANDOFF1이다. 후보 선정은 연구 효과·독창성·논문 채택 가능성의 입증이 아니다.
- [단계별 buildup 기준](../../research/IDEA_BUILDUP_GUIDE.md#stage-appropriate-gates), [source/검증 기록](../sources/vla_exploration_reopening_2026-10-28.json), [활성 TODO](../../TODO.md).

## 1. 이번에 결정한 것

| 순서 | 탐색 질문과 canonical 카드 | 보존 이유 | 아직 모르는 것 |
|---|---|---|---|
| 1 | [HANDOFF: 조작 VLA를 바꾸어도 좋은 도착 위치·이동 전략은 같은가?](../../synthesis/06_locomotion_whole_body.md#gap-handoff-2026) | Mobile manipulation의 모듈 재사용·정책 선택에 직접 연결된다. 기존 docking 연구를 출발점으로 교차 비교를 설계할 수 있다. | 여러 VLA에서 실제 전략 순위/재사용 범위, 단순 geometry·시야 검색의 충분성, 직접 선행의 전체 비교 범위 |
| 2 | [C1: 추가 관측은 언제 비용을 상쇄하는가?](../../synthesis/04_vla_generalist.md#gap-selective-observation-2026) | 이전 작업에서 바로 실행/look/wait의 효과 비교를 하지 않았다. 실행 준비 부족을 선택적 관측의 가치 부재로 읽을 수 없다. | 정렬된 정책에서 항상 관측·단순 선택 대비 선택의 실제 가치, 비용별 변화 |
| 3 | [TERM: 종료 규칙을 맞추면 정책 선택은 얼마나 달라지는가?](../../synthesis/04_vla_generalist.md#gap-termination-2026) | 사전 기제 없이도 중요한 평가 가정의 영향을 탐색할 수 있다. 기존 계약 감사를 재사용할 수 있다. | 변화의 유무·빈도·크기, 공정한 비교 가능 범위, P12 본문의 정확한 중복 범위 |

이는 **가설을 더 조사하기 위한 선택**이다. 세 후보 모두 현상·효과는 미확인이다. 다음 행동의 비용과 배울 내용을 기준으로 순서를 정했으며 성공 확률 점수는 만들지 않았다. 새 방법을 반드시 만들어야 한다는 전제와 RL 필요성도 제거했다.

HANDOFF와 C1은 관련되지만 질문의 단위가 다르다. 전자는 도착 전략과 downstream VLA의 호환성, 후자는 고정 정책에서 관측 행동을 추가할지의 선택이다. 후속 비교가 같은 실험으로 귀결되면 하나로 병합하며 별개 기여 수로 세지 않는다. TERM은 독립적인 평가 질문으로 대기한다.

## 2. 인터넷과 registry에서 확인한 경계

Registry title/identifier를 대조하고 2024–2026 관련 논문 **10편**의 primary 출처를 확인했다. 5편은 CVPR·CoRL·AAAI 발표 자료, 5편은 2026 preprint다. 지정 본문을 읽은 것은 Mobi-π, Behavior-Skill, Semantic Handoff, ActiveAlign **4편의 아래 구간**이다. 나머지는 공식 abstract/project 및 과거 검토의 재사용 범위를 표시했다. 모든 venue·논문을 망라한 survey나 10편 전체 정독은 아니다.

| 논문 / 확인 깊이 | 이미 알려진 범위와 이번 선택의 의미 |
|---|---|
| [SPIN, CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/html/Uppal_SPIN_Simultaneous_Perception_Interaction_and_Navigation_CVPR_2024_paper.html), 공식 검색·[저자 project abstract](https://spin-robot.github.io/) | Perception·base·arm의 공동 제어와 active vision은 기존 계보다. 이를 VLA 이름으로 다시 제안하지 않는다. SPIN을 VLA 실험으로 분류하지도 않는다. |
| [MoManipVLA, CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_MoManipVLA_Transferring_Vision-language-action_Models_for_General_Mobile_Manipulation_CVPR_2025_paper.html), 공식 검색/PDF 첫 페이지 노출·기존 D2 검토 | Fixed-base VLA를 mobile manipulation으로 연결하는 optimization 계보다. 이번에는 전체 evaluation을 다시 감사하지 않았다. |
| [MoTo, CoRL 2025](https://proceedings.mlr.press/v305/wu25c.html), 공식 abstract | Interaction keypoint와 물리적 feasibility를 이용한 docking이 선행이다. 여러 downstream 정책의 교차 비교 범위는 abstract만으로 확정하지 않는다. |
| [Mobi-π, CoRL 2025](https://proceedings.mlr.press/v305/yang25b.html), 공식 metadata + [arXiv v2 §5–6·8](https://arxiv.org/html/2505.23692v2) | Policy-aware placement, mobilization metrics, task suite와 baselines가 이미 있다. Single-task 범위와 multi-task 확장 논의를 확인했다. 단순히 도착 상태가 중요하다는 주장이나 navigation 성공과 조작 성공 분리 자체는 새롭지 않다. |
| [Affordance-Guided Coarse-to-Fine Exploration, AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/38909), 공식 abstract | Semantic affordance와 geometry를 이용한 base placement도 직접 선행이다. Abstract 결과를 우리 VLA 교차 비교의 증거로 쓰지 않는다. |
| [Behavior-Skill, 2026 preprint](https://arxiv.org/html/2608.30536v1), §III-B·IV-C | 복원한 중간 상태와 skill별 성공 조건으로 독립 평가하고, full-task에서 뒤 skill이 관측되지 않는 문제를 다룬다. Skill 분해 평가 자체를 새 기여로 삼지 않는다. |
| [Diagnosing Semantic Handoff Failures, 2026 preprint](https://arxiv.org/html/2607.06256v1), §IV–V·Appendix diagnostics | 같은 skill checkpoints의 curated snapshot/chained 상태 차이, reached-area/arm-reach 대조가 있다. 다만 isolated skill와 composed task의 판정 기준이 다르고 failure category는 verifier 기반이다. 이를 완전 통제된 VLA 간 순위 비교로 읽지 않는다. |
| [ActiveAlign, 2026 preprint](https://arxiv.org/html/2610.23378v1), §I·IV·V | Matched-state/data controls와 endpoint 오차·관측 trajectory 길이 sensitivity까지 있다. “기존 연구에 자세 통제가 없다”는 주장도 제외한다. 한 번의 pre-manipulation 관측이라는 범위를 확인했다. |
| [EyeRobot 2.0](https://arxiv.org/abs/2610.03710), 2026 공식 abstract 재확인 | RL gaze 선택이 이미 있다. Virtual fixation 등 세부 범위는 과거 [C1 본문 감사](../research_candidates/2026-10-20_vla_rl/C1_REVIEW.md)를 재사용하며 이번 abstract와 혼합하지 않는다. |
| [RESCUE](https://arxiv.org/abs/2610.13516), 2026 공식 abstract 재확인 | 개입 가치·반사실 branch·completion cost는 선행이다. Look branch라는 명칭만으로 새 평가 방법이 되지는 않는다. 상세 계약은 과거 C1 감사의 재사용이다. |

10편 중 6편은 기존 registry에 있으며 Mobi-π·AAAI base-placement·Behavior-Skill·Semantic Handoff 4편은 이번 manifest title/identifier 검색에서 찾지 못했다. 이번 작업은 후보 질문 심사이므로 신규 paper folder·note·registry 등록은 하지 않았다. Ledger에 외부 출처로 남겼다. CVF 직접 HTML 두 건은 403이었고 공식 검색 노출·저자 자료로 확인했다. Mobi-π PMLR PDF web 추출은 실패하여 arXiv v2의 명시한 구간을 사용했다. 두 버전의 전체 동일성을 주장하지 않는다.

이 대조에서 남긴 HANDOFF는 **새로운 보편적 failure 발견**이 아니라, 정책 교체 때 어떤 navigation/docking 비교를 다시 해야 하는지 묻는 탐색이다. 관련 논문이 있다는 것은 출발 근거다. 같은 질문이 이미 답해졌는지는 다음 제한된 비교에서 확인할 것이며, 현재 “아무도 하지 않았다”고 주장하지 않는다.

## 3. 과거 주제의 재검토

아래는 [요약 index의 16개 항목](../research_candidates/summaries/README.md) 전부의 이유 분류와 최근 4사례의 판단 구간 재검토다. 모든 개별 dossier·논문·실험을 재검증한 것은 아니다. C1·D2·RP-3의 개별 요약과 C1 선행 검토, TERM1·GAP-PROC1을 추가로 읽었다.

| 과거 주제 | 당시 보류/종료의 성격 | 이번 탐색 판단 |
|---|---|---|
| 초기 cross-embodiment RL | Bootstrap/대조 문제와 사용자 종료 | 실행 결과와 종료 유지. 이번 탐색을 RL 전이 실험의 재개로 바꾸지 않음 |
| 초기 latency/adaptive chunk | 직접 선행·E2 중복 | 이름을 바꾼 재제안 제외. 별도 새 질문 없음 |
| RP-2 recovery | 비교 branch·option 가치 미확인, RETIRED | 분야 반증 아님. RESCUE 직접 선행을 고려해 이번 우선 후보로 선택하지 않음 |
| RP-3 memory expiry | 일반 update 선행·memory 사용/손해 미측정 | 탐색 가능한 불확실성으로 인정하되 새 memory 질문 없이 기존 자산 재개 안 함 |
| **C1 selective observation** | Runtime competence 미확인, 비교 자체 미실행 | **비실험 탐색 재개.** 새로운 질문 카드를 만들고 rollout/학습 HOLD 분리 |
| C2 수행 방식 지시 | 현재 데이터의 label/coverage 실패 | 현재 설계 종료 유지. 다른 데이터 질문의 불가능성으로 확대하지 않음 |
| C3 action equivalence | 작은 범위의 실제 score 진단·직접 선행 | 관측된 결과 보존. 더 큰 학습을 이번에 다시 권하지 않음 |
| C4 reward audit | 독립 outcome·chronology 미확인 | 자료가 없다는 것은 효과 반증 아님. 이번에는 재검토 후보 대기 |
| C5 reset coverage | 완전한 실패/재시도 기록 미확보 | 데이터 진단 여지 보존. 기록 없는 분포를 추정해서 재개하지 않음 |
| C6 checkpoint selection | 기존 통계 방법·trial 자료 미확인 | 새 방법 필요성 약함 유지. 평가 질문 자체는 가능하나 이번 선택은 TERM |
| D1 observation correction | 단순 보정 이후 잔여 효과 미확인 | 탐색 원천 기각 사유는 아님. C1과 중복 후보를 늘리지 않고 대기 |
| D2 grasp–transport | 알려진 geometry/planning·native 미충족 | 기존 방법 NO-GO 유지. HANDOFF의 교훈으로 재사용하며 같은 문제라고 합치지 않음 |
| D3 irreversible switching | 동일 event/관측·continuation 증거 미확보 | NOT_MET 유지. 이번 새 논문의 일반 skill 평가를 Cooked–RGB witness로 승격하지 않음 |
| E1 replay/action conflict | 정상 정렬·effect 정보·두 로봇 미확인 | 자료 경계 유지. 탐색 불가능을 뜻하지 않지만 이번 3개에 추가하지 않음 |
| E2 temporal feedback | 기존 feedback family·native 미충족 | 방법 NO-GO/진단 HOLD 유지. 실행 미준비만으로 일반 현상 부재를 주장하지 않음 |
| Semantic-retention scout | VLM2VLA/LAP 직접 선행 | Broad motivation 재제안 제외. 새 행동 질문 없으므로 대기 |
| **TERM1** | 선행·사전 기제/잔여 차이 미확인 | **평가 탐색 재허용.** 기제 완성은 입장 요건이 아님. 기존 구현/확증 gate 분리 |
| AUTH4 | 이상적 초기 grounding+tracking의 조건부 충분성 | 실제 자연 조건에서의 충분성은 여전히 미측정. 후속 관찰 여지는 있지만 이번 우선순위 밖 |
| N4 DATA-TRANSFER | DataMIL 직접 masking 선행·현재 비교의 미확인 | 선행 충돌은 유지하되 모든 데이터 전이 질문의 종료로 해석하지 않음 |
| P4 reactive navigation | 실제 bounded pilot의 joint gate 실패 | **부정 결과 유지.** 같은 결과에서 유리한 subset만 골라 같은 주장을 복구하지 않음 |

선택하지 않은 항목은 모두 과학적으로 무가치해서가 아니다. 제한된 비실험 작업에서 HANDOFF 1개를 먼저 진행하고 C1·TERM을 대기로 남기는 투자 순서다. 이미 알려진 방법을 새로 주장하지 않는 기준과 실제 부정 결과를 존중하는 기준은 그대로다.

## 4. 다음 TODO와 종료점

**GAP-HANDOFF1 READY — 정책 교체와 도착 조건의 문헌 비교표.** Mobi-π·MoTo·Semantic Handoff·Behavior-Skill·ActiveAlign 5편에 한정해 다음을 정리한다.

1. 시작 상태가 시연 snapshot, 수동 배치, navigation의 실제 도착 중 무엇인지.
2. 같은 task에서 바꾼 downstream policy와 도착 전략의 조합, 제공된 policy 정보·추가 학습량.
3. 성공 predicate·validator·시간 예산 및 navigation 실패를 분모에 포함하는지.
4. 보고된 비교와 미보고/미확인 비교를 나누고, 하나의 작은 비교 질문과 강한 baseline을 고른다.

**완료 기준은 비교 가능성과 미확인을 한 장으로 명시하는 것**이다. 정책 효과·순위 역전·완성된 causal mechanism·Docker 환경까지 확보하는 것은 완료 조건이 아니다. 동일 비교가 이미 있으면 해당 결과를 수용하고 남는 범위를 수정한다. 문헌으로 더 알 수 없다면 후보를 `실험 필요·미확인`으로 보존하고 끝낸다. 자원이 없다는 이유만으로 다시 다른 주제로 자동 전환하지 않는다.

C1-E1·GAP-TERM-E1은 이후 비실험 작업으로 QUEUED다. 현 단계에서는 실행·설치·Docker/GPU probe·local PDF/weight/dataset 수집·외부 메시지·commit/push를 수행하지 않았다. 실제 연구자 피드백도 새로 확보하지 않았다.

## 5. 저장소 검증

`py_compile`, reading generator, `git diff --check`, repository audit를 완료했다. 오류·경고 **0**, registry **1,072편**, tier **47/297/486/242**, active/history **344/47**, 표준 note **5,360개** 유지. Markdown **5,539개**·상대 링크 **10,957개** 검사 통과.

AGENTS·PAPER·manifest/meta·tier CSV·active/history CSV **7개는 작업 전과 byte-identical**이다. 기존 dirty **649개** 중 이번 범위의 **7개** 외 **642개**와 기존 삭제 **10개**를 보존했다. 추가로 기존 clean tracked summary **2개**를 수정했고 신규 파일은 이 보고서와 source ledger **2개**다. Generator에서 별도 내용 변화는 없었다. 문서 무결성 검사는 정책 실험·효과 검증을 뜻하지 않는다.
