# GAP-SELECT-E1 — 첫 탐색 후보로 HANDOFF 선정

> 2026-11-17 인계: 이 문서의 폐기 후보(HANDOFF/SET/RETRIEVAL/CODEC1/ALLOC/HINDSIGHT/VRL) 계획·명령은 당시 기록이다. 현재는 RETIRED이며 새 실행 queue가 아니다. 링크는 핵심 보존본 또는 삭제 전 Git revision으로 연결한다.

- 결정일: **2026-10-28 KST / DONE — 비실험 후보 선정**.
- **우선 후보: HANDOFF.** 같은 로봇에서 VLA A에 맞춰 선택한 도착 설정을 B로 교체한 뒤에도 재사용할 수 있는지 먼저 탐색한다. C1은 대안 후보, TERM은 독립 질문을 보존하면서 공통 평가 원칙으로 활용한다.
- 이는 **후속 확인의 순서**다. 연구 효과·신규성·논문 채택 가능성·실행 준비 완료를 뜻하지 않는다. 세 후보의 증거 성숙도는 `CURATION-HYPOTHESIS` 그대로다.
- 근거는 완료된 [HANDOFF 비교](../research_topics/retired/README.md#mobile_policy_transfer), [C1 비교](./C1_OBSERVATION_COST_REVIEW_2026-10-28.md), [TERM 비교](./VLA_TERMINATION_COMPARISON_2026-10-28.md)와 [단계별 buildup 기준](../../research/IDEA_BUILDUP_GUIDE.md#stage-appropriate-gates)이다. 이번에는 새 웹 조사·동일 source 재감사 없이 기존 근거로 판단했다. 아래 우선순위는 **연구자 판단**이며 미측정 성공 확률을 수치화하지 않았다.

## 1. 세 후보를 비교한 이유

| 후보 | 답에 따라 바뀌는 결정 | 첫 관측의 정보 가치 | 알려진 부담·해석 위험 | 이번 배치 |
|---|---|---|---|---|
| **HANDOFF: VLA 교체 후 도착 설정 재사용** | 이동 모듈·도착 설정을 유지할지, B로 소규모 재검증/재선택할지 | 기준 시작 상태의 B 성능만으로 배포 판단이 충분한지 직접 확인. Geometry/시야 기준 또는 단순 B 재선택으로 충분한 결과도 유용 | 두 정책과 동일 embodiment/task의 호환 경로 필요. 실제 도착 분포·상태 복원은 미검증. 일반적인 다중 정책 비교는 이미 선행에 있음 | **첫 우선 후보** |
| **C1: 추가 관측 생략** | 매 episode에 look을 할지, 초기 관측의 간단한 gate를 쓸지 | 한 정책에서 시간–성공 trade-off를 확인하며 always/immediate의 충분성도 평가 가능 | 정책 수는 적지만 물리 look primitive·정렬·실제 정보 전달 경로가 미검증. Endpoint 호환성만 관찰하면 HANDOFF와 겹침 | **대안 후보 유지** |
| **TERM: 종료 규칙 아래 정책 선택** | First-hit 성적으로 고른 정책을 그대로 쓸지, 종료까지 포함해 재평가할지 | 완전한 공통 trace가 있다면 채점 기준의 민감도를 먼저 볼 수 있음 | 해당 raw packet은 미확보. 실제 종료 후 결과는 별도 branch 필요. 기존 평가 개념·P12와의 차이도 미확정 | **독립 탐색 보존; 공통 평가 원칙 우선 재사용** |

HANDOFF를 고른 핵심은 현재 목표인 **VLA 기반 navigation–manipulation 연결**과 배포 시 정책 교체라는 판단의 직접성이다. C1보다 실행이 쉽다고 판단한 것은 아니다. C1의 정책 수가 적다는 사실만으로 전체 비용이 낮다고 볼 수 없고, TERM도 지금 바로 가능한 offline 실험으로 확인된 상태는 아니다.

HANDOFF는 VLA 간 차이를 보지만 첫 단계에서는 **로봇을 고정**한다. 서로 다른 embodiment로의 일반화, 새 navigation 알고리즘, RL selector는 현재 주장에 포함하지 않는다. 단순 재사용이 충분한 범위를 찾아도 질문에 답할 수 있으며, 재사용 손실이 반드시 존재해야 후보 자격을 얻는 것은 아니다.

## 2. 선택한 질문과 첫 확인

**질문:** A로 고른 도착 설정을 B에도 재사용할 수 있는가? B의 기준 시작 상태 성능만으로 판단해도 되는가? 그렇지 않다면 같은 후보 집합에서 제한된 B validation으로 재선택하는 것으로 충분한가?

유지할 최소 비교는 **A 설정의 B 재사용 / 정책과 무관한 geometry·시야 기준 / 제한된 B 재선택**이다. 여기서 재사용할 것은 공통 후보 생성·선택의 설정 또는 규칙이다. 장면이 바뀌어도 같은 전역 좌표를 무조건 복사한다는 뜻이 아니다. 실제 설정의 표현은 선택할 공개 경로를 확인한 뒤 정한다.

**첫 확인 항목 — GAP-HANDOFF2:** 같은 embodiment·task에서 두 frozen VLA가 **같은 도착 상태를 받아 실행될 수 있는 공개 경로 하나**를 특정한다. 성공률을 미리 입증하는 작업이 아니라, 작은 비교의 입력과 평가 연결이 가능한지 문서·source로 한정 확인하는 작업이다.

첫 확인 대상으로 기존 비교표의 **Behavior-Skill의 π0.5/GR00T N1.7 경로**를 둔다. 기존 본문 검토에 두 VLA와 독립 상태 복원 평가가 명시돼 있어 출발점으로 택한 것이며, 공개 code/checkpoint의 현재 제공·상호 호환·실행 가능성을 확인했다는 뜻은 아니다. 특히 독립 skill snapshot은 실제 navigation 도착 상태와 같지 않다.

| 확인할 연결 | 필요한 답 | 지금 상태 |
|---|---|---|
| Task–정책 | 두 checkpoint가 같은 robot/task goal·관측/action 의미를 지원하는가? | 문헌상 비교 존재; 구체 공개 실행 경로 미확인 |
| 도착 상태–입력 | Base/arm/object/camera 상태를 연결·복원할 수 있으며 실제 이동으로 만들어진 상태인가? | 독립 snapshot 평가만으로 실제 도착 증거가 되지 않음 |
| 설정–비교 | A에서 고른 설정을 고정해 B에 적용하고 같은 후보에서 B 재선택과 비교할 수 있는가? | 표현·API 미정; 새 selector 구현 없음 |
| 결과–비용 | 공통 goal·scene identity·물리 budget 및 도착 실패/조작 성공을 분리해 기록할 경로가 있는가? | 명세 초안만 존재; native 자료 미확보 |

완료 산출물은 기존 HANDOFF 카드의 **공개 경로와 연결 상태 한 표**다. 환경 설치·weights/dataset 다운로드·adapter·실행 manifest는 만들지 않는다. 이 출발점이 맞지 않으면 이유를 기록하고 확인을 끝낸다. 같은 자료를 재검색하거나 다른 benchmark로 조용히 바꿔 원래 mobile handoff 질문을 검증했다고 표시하지 않는다.

## 3. 판단을 바꾸는 조건과 종료점

- 공통 경로가 연결되면 그 작은 비교의 실행 준비를 별도로 계획한다. **이번 선택만으로 rollout·학습을 재개하지 않는다.** 실제 실행은 필요한 계약을 확인한 뒤 로컬 Docker에서만 가능하다.
- 두 정책 또는 실제 도착 경로를 현재 공개 자산으로 연결하지 못하면 **실행 경로 미확보**로 남긴다. HANDOFF의 연구 가치가 없다는 판정이나 C1 자동 승격으로 바꾸지 않는다. C1의 작은 경로가 더 명확해진 경우에만 탐색 순서를 다시 판단할 수 있다.
- 후속 결과가 단순 geometry/시야 기준이나 B 재선택으로 충분함을 보이면 그 범위를 정리한다. 새 learned method를 만들 이유가 자동으로 생기지 않는다. 효과가 작거나 불확실한 경우에도 탐색 결과로 남기고 유리한 장면만 골라 주장하지 않는다.
- TERM의 goal/종료/controller 분리는 HANDOFF의 평가에 사용하되, **종료 후 물리 실험까지 첫 pilot의 필수 범위로 늘리지 않는다.** 선택한 성공 정의와 분모를 명시하는 수준부터 적용한다. C1도 첫 pilot에 함께 구현하지 않는다.
- 현재 후보 선정은 완료했다. 다음은 **GAP-HANDOFF2 READY — 위 공개 경로 하나의 비실험 연결 확인**이다. 광범위한 문헌 탐색·세 후보의 반복 순위 매기기를 다음 단계로 만들지 않는다.

Canonical 판단은 [HANDOFF 카드](../../synthesis/06_locomotion_whole_body.md#gap-handoff-2026), 활성 작업은 [TODO](../../TODO.md)에 반영했다. 기존 HOLD/NO-GO/RETIRED, P12 본문 미확인, C1 competence 미확인 및 사용자 읽기 상태는 유지한다. 새 프로젝트·source ledger·실행 manifest·실험 결과는 생성하지 않았다.

## 4. 문서 검증

`py_compile`, reading generator, `git diff --check`, repository audit를 완료했다. 오류·경고 **0**, registry **1,072편**, tier **47/297/486/242**, active/history 읽기 기록 **344/47**, 표준 note **5,360개**를 유지한다. Markdown **5,543개**·상대 링크 **10,997개** 검사 통과.

AGENTS·PAPER·manifest/meta·tier CSV·active/history CSV **7개가 작업 전과 byte-identical**이다. 기존 dirty **659개** 중 이번 수정 **8개** 외 **651개**와 기존 삭제 **10개**를 보존했다. 신규 파일은 이 결정 기록 **1개**뿐이며 generator의 추가 내용 변화·generated queue 변화는 없다. 활성 TODO와 세 후보의 배치도 동기화했다. 문서 무결성과 후보 선택은 연구 효과의 증명이 아니다.
