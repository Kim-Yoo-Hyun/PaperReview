# GAP-TERM-E1 — 종료 평가에 따라 VLA 선택이 달라지는가

- 확인일: **2026-10-28 KST / DONE — 비실험 비교 정리**.
- 결론: **평가·실증 질문을 유지한다.** 최초 목표 달성으로 고른 정책이 공통 종료 규칙에서도 좋은 선택인지, 그 선택이 안정적인 범위가 어디인지 조사할 수 있다. 순위 역전·새 종료 방법을 필수 결과로 요구하지 않는다. 실제 효과·독립 논문 가치·신규성은 미확인이다.
- 범위: [GAP-TERM1](./VLA_TERMINATION_CONTRACT_REVIEW_2026-10-27.md)의 source 감사를 재사용하고 Echo·SEES·SparkVLA의 지정 본문 구간만 웹에서 재확인했다. 세 자료는 확인한 **2026 arXiv preprint 버전**이며 acceptance를 검증한 것은 아니다. P12는 2026-10-27 공식 abstract/metadata 확인에 머물며 본문 접근을 반복하지 않았다.
- [Source ledger](../sources/vla_termination_comparison_2026-10-28.json) · [Canonical 질문](../../synthesis/04_vla_generalist.md#gap-termination-2026) · [TODO](../../TODO.md). 실험·설치·GPU/Docker probe·payload 수집·신규 등록·읽기 승격 없음.

## 1. 먼저 실행 방식과 채점 기준을 분리한다

**연구자 정리:** 최초 성공(first-hit)은 채점 기준이고, 고정 시간 실행은 궤적을 만드는 규칙이다. 같은 고정 길이 기록에서 최초 달성과 끝 상태를 모두 채점할 수 있으므로 서로 배타적인 세 종류의 benchmark로 나누지 않는다. 자율 종료는 정책이 보는 정보로 종료 시점을 선택하고, 그 뒤 실제 동작도 바꾸는 개입이다.

| 질문 | 실행 방식 | 필요한 관측·채점 | 그 결과만으로 알 수 없는 것 |
|---|---|---|---|
| 예산 안에 한 번이라도 목표에 도달하는가? | 계속 실행하거나 evaluator의 최초 성공에서 기록 종료 | 같은 goal `G`의 최초 true와 episode 분모. 실패 시 예산 끝까지의 관측 필요 | 스스로 성공을 알아차리는지, 정지 후 유지하는지 |
| 계속 행동해도 끝 상태가 성공인가? | 정책 action을 고정 horizon `T`까지 계속 실행 | 동일 기록의 `G(s_T)`와 `max G(s_t)`를 각각 기록 | 종료 controller로 바꿨을 때의 결과 |
| 현재 신호가 성공을 정확히 알아차리는가? | 이미 기록된 동일 궤적에 detector 적용 | Query 시각·입력·threshold·GT 경계와 선언 시각 | 신호로 멈췄다면 달라졌을 물리 상태와 실제 완료율 |
| 스스로 적절히 끝내는가? | 허용 관측 기반 규칙 `r`이 종료를 선언하면 action을 controller `K`로 전환 | 선언·goal truth·실제 `K` 실행·이후 관측 구간 `Δ`·전체 비용 | 다른 controller/task/예산에 대한 일반 성능 |

동일한 완전한 continuation 기록에서는 끝 상태 성공이 최초 달성의 부분집합이다. 이것은 정의상 관계이며 새로운 이론이나 관측된 정책 순위 변화가 아니다. 최초 성공에서 잘린 기록의 끝을 복사해 전체 horizon의 최종 상태를 채우면 안 된다. `done`이 latched event인지 현재 goal truth인지도 구분한다.

## 2. 기존 근거에서 실제 비교 가능한 항목

`보고`는 논문에 서술된 평가, `경로`는 과거 정적 코드 감사에서 확인한 기록 경로다. **실행·공개 원자료 확보를 뜻하지 않는다.** `미확인`과 `미보고`를 0점으로 채우지 않는다.

| 자료·근거 | 최초 달성 / 끝 상태 | 신호·종료 비교 | 지금 사용할 수 있는 범위 |
|---|---|---|---|
| **OpenVLA runner**, [고정 revision의 평가 loop](https://github.com/openvla/openvla/blob/c8f03f48af692657d3060c19588038c7220e9af9/experiments/robot/libero/run_libero_eval.py#L164), 과거 C20 | 환경 `done`에서 break하는 경로. 성공 후 continuation은 없음 | 별도 native 종료 선언 경로 미확인 | First-hit protocol 예시. 종료 이후 상태·native stop 결과는 누락 |
| **Echo 논문**, [A.8–A.10](https://arxiv.org/html/2610.31569v1) | A.10은 두 모델 모두 최초 달성을 success로 채점. Baseline은 첫 성공에 중단, Echo는 horizon까지 계속 실행 | 신호는 rollout을 멈추지 않음. GT 성공 경계 이후 window의 신호 평가 | 신호 정확도와 실제 종료 효과를 분리하는 근거. 모델 간 점수 차이를 종료 규칙만의 효과로 쓰지 않음 |
| **Echo 공개 code**, [고정 revision의 loop/record](https://github.com/lyfeng001/Echo-Sim/blob/ed771cfcee11961529541edd7dcc7c16fee788d8/echo/evaluation/evaluate.py#L92), 과거 C1·C9 | 두 모델 모두 고정 horizon, event 및 `terminal_success` 기록 경로 | 신호는 기록하되 실행 중단에 미연결 | 같은 실행 기록의 두 채점 기준을 연결할 수 있는 **후보 경로**. 논문 protocol과 차이가 있으며 실제 episode packet은 이번에 확보하지 않음 |
| **SEES**, [Appendix B / Table 5](https://arxiv.org/html/2609.32698v1) | Oracle가 복합 실행을 제어하고 보조 continuation에서 두 규칙을 평가 | Terminate head 대 VLM의 신호·시각 비교. Head의 3연속 action 확률은 서로 다른 새 영상 3개의 확인과 다름 | Table 5를 온라인 종료 후 완료율로 읽지 않음. 논문 전체의 learned handoff 사용까지 없다고 주장하지 않음 |
| **SparkVLA**, [Closed-Loop Inference / Algorithm 3 / Evaluation Controls](https://arxiv.org/html/2608.16172v1) | Global criterion으로 episode 종료; complete-system 비교 | 내부 Stop은 다음 subtask 전환. Action prefix 선택도 함께 바뀜 | Subtask handoff와 전체 episode 정지를 구분. 동일 frozen action policy의 종료기 교차 실험으로 치환하지 않음 |
| **P12: Every Failure Is a Timeout**, [공식 forum](https://openreview.net/forum?id=8GyKjbTQUd), 과거 P12 | 2026-10-27 abstract는 fixed-horizon·achievement/terminal 구별을 이미 제안 | 정확한 정책×종료기 본문 비교 범위 미확인 | 당시 ICLR 2027 under review. 이번 재접근·최신 status 확인 없음. 이 개념 자체의 신규성은 주장하지 않되 세부 비교까지 해결됐다고 추정하지 않음 |

코드 3개 revision·21파일의 원 확인일과 hash는 [기존 ledger](../sources/vla_termination_contract_review_2026-10-27.json)를 따른다. 이번에는 재다운로드·재실행하거나 최신 코드와 같다고 인증하지 않았다. 위 자료들은 task·모델·입력·시간이 달라 **논문 간 aggregate 수치로 정책 순위를 계산할 수 없다**.

## 3. 남기는 작은 질문과 가능한 비교

**연구자 질문:** 같은 task·전체 물리 예산에서 **최초 달성 성적으로 선택한 VLA를 그대로 배포해도 되는가?** 공통의 간단한 종료 규칙을 적용했을 때 선택이 유지되는지, 달라진다면 실제 완료 손실과 비용이 실무적으로 의미 있는지 본다. 새 native stop head가 두 정책에 모두 있어야 시작할 수 있는 질문은 아니다.

기존 설계는 native 종료기 비교와 사전 조건부 설명을 앞세웠다. 이번 탐색에서는 **두 frozen action policy × 공통의 단순 종료 규칙**을 최소 비교로 둔다. Native 기능은 실제 제공될 때 추가한다. 이는 구현 승인이나 “모든 단순 대안을 먼저 이겨야 한다”는 입장 조건이 아니다.

| 비교 | 최소 조건·해석 |
|---|---|
| 1차: 동일 continuation 기록의 두 채점 | 두 정책의 동일 task/scene·예산에서 first-hit와 끝 상태 점수 및 차이의 불확실성 비교. 원자료가 있을 때 가능한 분석이며 이번 실행 없음. **여기서 순위가 안정적이어도 자율 종료 검증은 완료되지 않음** |
| 2차: 실제 종료 개입 | 각 정책 안에서 fixed deadline, 공통 관측 detector+threshold, 같은 detector+서로 다른 query의 연속 확인 비교. 같은 `G/K/Δ`, action weights/normalizer/controller 유지. 없는 native rule은 N/A |
| 전체 시간 | 총 예산 `B`에 정지 후 관측 `Δ`를 포함하는 설계라면 선언은 `τ≤B−Δ`, fixed deadline도 `B−Δ`로 둠. Continuation reference의 `G(s_B)`와 혼동하지 않음. 추론·센서 지연과 실제 동작 시간도 기록. 수치 미동결 |
| 성공 정의 | Native goal `G`는 유지하고 선언 시 `G`와 이후 유지 결과를 나눔. 유지·release 요구를 더한 완료 점수는 별도 deployment 계약으로 표시. 이를 원래 benchmark의 오류나 동일 지표로 부르지 않음 |
| 종료 동작 | Physics를 멈추지 않고 task에 맞는 `K` 실행. 정책 continuation·simulator freeze·pose/gripper hold·release를 구분. 과거 OpenVLA dummy action은 gripper open이므로 보편적 no-op이 아님 |
| 정보·시각 | Detector는 선언 전에 이용 가능한 공통 관측만 사용. GT는 evaluator용. 같은 held signal이나 한 chunk의 예측들을 서로 다른 관측으로 세지 않음. Detector가 actor 입력/action 생성도 바꾸면 종료 규칙만의 효과가 아님 |
| 선택·검증 | 정책 선택과 threshold 조정은 calibration scene에서, 선택의 손실은 다른 held-out scene에서 평가. 같은 test를 보고 최선 정책/threshold를 고른 뒤 그대로 우월성을 보고하지 않음 |
| 보고 단위 | 독립 scene/init-state 단위의 paired 결과와 불확실성. 조기 오종료, 성공했으나 미선언, 종료 후 손실, timeout, 시간·query 비용을 포함. 성공 trial만의 평균과 frame 수로 결론 내리지 않음 |
| 안정성 해석 | 비교 차이의 구간이 사전에 정한 실용 허용 범위 안에 있을 때만 해당 범위의 선택 안정성을 지지. 단순한 비유의성·작은 pilot만으로 동등성을 선언하지 않음 |

과거 `On`/`Open` 두 predicate에 release/dwell이 없는 사실은 [계약 심사 §4](./VLA_TERMINATION_CONTRACT_REVIEW_2026-10-27.md#4-실제-task-predicate와-종료-이후-controller)에서 재사용한다. 이것만으로 bowl/drawer가 반드시 종료 오류를 일으킨다거나 안정/불안정의 검증된 대조쌍이라고 정하지 않는다. 자연 사례·차이의 방향·새 원인 설명은 탐색에서 얻을 수 있다.

**자료의 한계:** 완전한 continuation과 online 입력이 있으면 detector가 언제 선언했을지는 사후 계산할 수 있다. 그러나 그 시점에 `K`로 바꾼 뒤의 결과는 별도 반사실이다. 이미 저장된 `K` branch, 실제 재실행 또는 검증된 동역학 근거 없이 궤적을 잘라 자율 완료율을 생성할 수 없다. 이번에는 원자료 재분석도 수행하지 않았다.

## 4. 연구 판단과 다음 행동

- **GAP-TERM-E1 DONE.** 실행/채점 축과 실제 비교 가능한 항목을 압축했다. 정책 선택의 민감도 또는 안정성을 보는 **작은 평가 후보를 유지**한다. 기존 정의·신호 정확도를 재보고하는 것만으로 독립 기여가 되지는 않지만, baseline 실패나 완성된 원인 기제가 없다는 이유로 탐색을 기각하지 않는다.
- **아직 모르는 것:** 공정한 조건에서 실제 선택이 달라지는지, 달라지는 크기·빈도·배포 의미, 단순 종료 규칙의 충분성, P12의 세부 본문 범위. 문서 완료로 이 값들을 채우지 않는다. 큰 학습·새 termination method와 과거 GAP-TERM-R1 실행은 재개하지 않는다.
- **현재 문헌 단계 종료:** 같은 P12 접근이나 21파일 감사는 반복하지 않는다. 실제 효과는 원자료 또는 실행이 필요한 미확인으로 남긴다. 이는 자원이 없다는 이유로 TERM을 폐기한다는 뜻이 아니다.
- **다음 GAP-SELECT-E1 READY — 비실험:** 완료된 HANDOFF·C1·TERM 카드로 첫 탐색 pilot의 우선 후보 하나를 고른다. 질문의 중요성, 기존 연구와의 차이, 가장 작은 관측의 정보 가치, 알려진 실행 부담을 비교한다. 선택 이유와 첫 확인 항목을 TODO/기존 카드에 남기며 새 주제·새 방법·실행 manifest를 자동 생성하지 않는다. 확인된 결과를 미리 요구하거나 미측정 성공 확률을 점수로 만들지 않는다.

실제 실행이 필요해지면 선택한 작은 비교에 맞는 입출력·환경·checkpoint·scene split·종료 동작을 먼저 확인하고 로컬 Docker에서만 진행한다. GPU 상태는 이번에 재측정하지 않았다. [HANDOFF](../research_topics/mobile_policy_transfer/내용/README.md#closest-work)·[C1](./C1_OBSERVATION_COST_REVIEW_2026-10-28.md)와 과거 다른 후보의 결과·실행 gate는 유지한다.

## 5. 문서 검증

`py_compile`, reading generator, `git diff --check`, repository audit를 완료했다. 오류·경고 **0**, registry **1,072편**, tier **47/297/486/242**, active/history 읽기 기록 **344/47**, 표준 note **5,360개**를 유지한다. Markdown **5,542개**·상대 링크 **10,990개** 검사 통과.

AGENTS·PAPER·manifest/meta·tier CSV·active/history CSV **7개가 작업 전과 byte-identical**이다. 기존 dirty **657개** 중 이번 수정 **7개** 외 **650개**와 기존 삭제 **10개**를 보존했다. 신규 파일은 이 보고서와 ledger **2개**이고 generator의 추가 내용 변화는 없다. 재사용한 source ID·title·URL 연결과 활성 TODO 상태도 확인했다. 문서 검증은 연구 효과 검증이 아니다.
