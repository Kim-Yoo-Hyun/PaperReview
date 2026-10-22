# 연구 후보 핵심 요약 — 2026-10-22

사용자 요청에 따라 **주제별 한 파일, 총 16개**로 정리했다. 실제 buildup을 진행한 주제, 종료된 초기 방향, 과거 project overlay와 탐색 단계에서 제외한 방향을 구분한다. 이 문서는 연구 판단의 요약이며 새로운 읽기 우선순위나 실행 queue가 아니다. 활성 작업은 [TODO](../../../TODO.md), 논문 우선순위는 [READING_PLAN](../../../research/READING_PLAN.md)을 따른다.

**GPU 확보는 실행 자원 조건 하나의 변화다.** 사용자가 선택한 현재/clone 컴퓨터의 로컬 Docker에서 접근 가능한 호환 GPU·충분한 메모리·runtime을 검증해야 하며, GPU 모델/VRAM 요건을 이번에 벤치마크하지 않았다. 원격 GPU·host MPS 경로로 바꾸는 승인이 아니다. 아래 최소 검증도 해당 주제의 연구·자료 조건이 충족된 경우에만 가능하다. 이번 정리는 실험을 실행하거나 HOLD/RETIRED 판정을 해제하지 않는다.

| 주제별 단일 요약 | 현재 판정 | GPU 확보 후 검토 가능한 최소 작업 | GPU로 해결되지 않는 핵심 |
|---|---|---|---|
| [초기 로봇 간 RL 전이](./00_CROSS_EMBODIMENT_RL.md) | RETIRED | 검증된 native policy의 competence부터 다시 설계 | 기존 bootstrap 실패, weighted imitation 대조, 사용자 종료 결정 |
| [초기 실행 지연·adaptive chunk](./00_EXECUTION_LATENCY.md) | 넓은 방향 종료 | Native delay/replanning 대조 | REMAC/TIC-VLA 등 직접 선행, E2와의 중복 |
| [RP-2 실패 복구 선택](./RP2_FAILURE_RECOVERY.md) | RETIRED | 동일 failure onset의 option branch 비교 | 대안별 가치 교차·분기 동치·직접 선행 |
| [RP-3 memory expiry](./RP3_MEMORY_EXPIRY.md) | RETIRED | Fresh/stale/masked memory branch | 실제 memory 사용·정보 비용·원인 귀속 |
| [C1 선택적 추가 관측](./C1_SELECTIVE_OBSERVATION.md) | HOLD | Native competence와 immediate/look/wait 대조 | 물리 관측 primitive·시간/자세 통제·RL 필요성 |
| [C2 수행 방식 지시](./C2_EXECUTION_CONSTRAINTS.md) | 현재 설계 NO-GO | Qualified data의 reward 검사 후 native 대조 | Label/coverage 불충족·checkpoint·선행 충돌 |
| [C3 실행 행동 동치](./C3_ACTION_EQUIVALENCE.md) | 본격 학습 비추천 | 더 넓은 checkpoint/slot 진단 | 실제 효과의 작음·국소성, CAPG/MPG 계보 |
| [C4 선택적 보상 검수](./C4_REWARD_AUDIT.md) | 방법 NO-GO / 진단 HOLD | Versioned rollout의 reward·policy 대조 | 정책 chronology·독립 outcome·검수 비용 |
| [C5 reset와 학습 범위](./C5_RESET_COVERAGE.md) | 방법 NO-GO / 진단 HOLD | Frozen native policy의 reset ledger | 실패·재시도·human rescue를 포함한 완전한 기록 |
| [C6 checkpoint 선택](./C6_CHECKPOINT_SELECTION.md) | 독립 방법 NO-GO | 기존 통계적 비교 protocol 적용 | Trial-level 자료·독립 evaluator·기존 selection 방법 |
| [D1 관측 보정](./D1_OBSERVATION_CORRECTION.md) | 방법 NO-GO / 진단 HOLD | OFT native competence·보정 대조 | 선택이 갈리는 task·관측 cue·단순 보정 이후 gap |
| [D2 운반을 고려한 파지·계획](./D2_GRASP_TRANSPORT.md) | 방법 NO-GO / 진단 HOLD | 한 task의 grasp–transport–place 비교 | Attachment/planner baseline·후속 실행 가능성 label |
| [D3 비가역 사건 후 지시 변경](./D3_IRREVERSIBLE_SWITCHING.md) | REVISE / 재개 gate NOT_MET | 사건 전후 동일 instance의 continuation | Event/RGB pair·language executor·변경 goal 평가 |
| [E1 행동 충돌과 replay](./E1_ACTION_CONFLICT_REPLAY.md) | REVISE / 재개 gate NOT_MET | 정상 정렬 후 replay/retention 대조 | 실제 effect 추가 정보·episode join·두 로봇 평가 경로 |
| [E2 시간 표현과 feedback](./E2_TEMPORAL_FEEDBACK.md) | 방법 NO-GO / 진단 HOLD | 한 native 경로의 timed-reference/feedback 대조 | 시간·controller·정보/계산 통제 이후 새 지식 |
| [탐색: VLM 의미 능력 보존](./SCOUT_SEMANTIC_RETENTION.md) | 탐색에서 제외 / buildup 미진행 | VQA와 robot skill을 분리한 평가 | VLM2VLA/LAP 직접 선행·의미 능력과 행동 성능 연결 |

## 해석 규칙

- **측정됨**은 해당 문서에 명시된 실험/metadata/source 범위만 뜻한다. Code 실행, 데이터 형식 검사, 정책 성공률은 서로 대체하지 않는다.
- **NO-GO**는 현재 설계의 투자 판단이다. 연구 분야 전체의 불가능성이나 가설의 실험적 반증을 뜻하지 않는다.
- **RETIRED**는 역사 보존이다. 과거 실행 자산의 삭제 사실을 복구 가능하다고 바꾸거나 자동 재개하지 않는다.
- 현재 어느 후보도 GPU만 추가하면 즉시 본격 학습을 시작하도록 승인된 상태는 아니다. 실제 외부 연구자 피드백은 새로 받은 것이 없다.
- 일반 memory 탐색은 RP-3와 함께 보존하고, 과거 지연 방향과 E2는 관계를 명시하되 실험 이력을 합치지 않았다. C1–C6/D1–D3/E1–E2의 ID와 D1-E1 같은 하위 실험 ID를 혼동하지 않는다.

전체 연결 문헌의 이번 등록·공식 발표 상태·보존 검증은 [registry 갱신 report](../../update/REGISTRY_ROLLUP_2026-10-22.md)에 기록했다. 각 주제 파일 끝에도 해당 표준 paper note를 연결했다.

다른 컴퓨터에서의 실행 절차·artifact와 연구 gate는 [Docker 재개 안내](../../experiments/portable/README.md)를 따른다. 과거 절대 경로·컨테이너 이름은 실행 당시 증거로 보존한다.
