# 작업 인계 역사 — 2026-10-22 종료 시점

이 문서는 당시 TODO의 보존본이다. 아래의 다음 행동·자원 제한은 당시 기록이며 활성 작업은 [현재 TODO](../../TODO.md)를 따른다. 2026-10-23 통합 시 상대 링크만 새 위치로 옮겼다.

# 연구 작업 TODO / 다음 세션 인계

- 갱신: 2026-10-22 KST
- 직전 완료: **DOC-R1 / 연구 후보별 핵심·GPU 후속·한계 통합, REG-R1 / 외부 문헌 registry 갱신 — DONE**. 다음 연구 gate는 E2-R1·E1-R2의 새 근거 대기다.
- 판단: 후보 요약과 registry 유지보수이며 연구 판정 재개가 아니다. E2-B1 DONE / 일반 신규 방법 NO-GO·진단 REVISE/HOLD, E2-R1·E1-R2 WAITING_EVIDENCE를 유지한다.
- 범위: 지금 할 작업과 직전 산출물의 navigation. 논문 중요도·읽기 순서는 [READING_PLAN.md](../../research/READING_PLAN.md), 현재 근거는 [E2 buildup](../research_candidates/2026-10-22_e2_buildup/README.md), 상세 이력은 [update log](UPDATES_2026-10-22.md)가 관리한다.

## 바로 이어서 할 일

**DOC-R1 / REG-R1 DONE:** [주제별 단일 요약 16개](../research_candidates/summaries/README.md)에 실제 결과·GPU 확보 후 최소 검증·GPU 외 한계·재개 조건을 작성했다. [직접 비교 문헌 47편 등록](REGISTRY_ROLLUP_2026-10-22.md) 후 전체 1,037편 / CORE 47 · NEXT 275 · REFERENCE 473 · ARCHIVE 242다. 기존 4,950개 note·990개 manifest record·351개 사용자 읽기 행을 보존했다. [검증](REGISTRY_ROLLUP_VALIDATION_2026-10-22.md). 문서 완료는 연구 gate 통과나 실험 재개를 뜻하지 않는다.

**E2-B1 비실험 심사 완료. 다음 gate는 E2-R1 / WAITING_EVIDENCE다.** [결과](../research_candidates/2026-10-22_e2_buildup/README.md), [직접 선행 9편](../research_candidates/2026-10-22_e2_buildup/CLOSEST_WORK.md), [pinned source 감사](../research_candidates/2026-10-22_e2_buildup/SOURCE_INTERFACE_AUDIT.md), [비교/기각 계약](../research_candidates/2026-10-22_e2_buildup/CLAIM_CONTRACT.md)을 작성했다. RTR의 controller mode 동시 변경, AAC의 관측/실행 길이 경로, A2C2의 기존 delay/horizon 분리를 확인했다. 설정 차이는 성능 차이·논문 오류의 증거가 아니다.

재개에는 [E2 명세](../research_candidates/2026-10-22_e2_buildup/QUALIFICATION_SPEC.json)의 일관된 task–checkpoint–normalizer–controller–evaluator packet, 물리 시간 정의, 기존 대안과 구별할 예측/개입이 필요하다. 효과를 먼저 입증하라는 조건은 아니다. GPU 확보·같은 문헌 재조회·추가 checklist만으로 재개하지 않는다. 큰 학습·환경 이식은 HOLD이며 현재 E2를 주력 신규 방법으로 추천하지 않는다. Native 효과와 실제 외부 피드백은 미완료다.

## E1과 최초 scout의 보존 판단

**E1-R1 심사 완료. E1-R2 / WAITING_EVIDENCE로 보존한다.** [후속 결과](../research_candidates/2026-10-22_e1_buildup/R1_REVIEW.md)는 RH20T cfg3/5의 공통 task ID 59개와 task 6/8의 source view key, X-VLA-Pt의 Franka/UR pose-native 경로를 확보했다. 카메라 key를 독립 trial로 세지 않으며, 두 dataset의 장점을 하나의 qualified 경로로 합치지 않는다. 정상 pose 잔차를 넘어서는 추가 정보와 해당 task의 model–controller–evaluator 연결은 미확보다.

재개에는 [현재 evidence packet](../research_candidates/2026-10-22_e1_buildup/R1_EVIDENCE_REQUIREMENTS.json)의 source-view→physical/converted episode 연결, command·시간·scene 근거, native 평가 경로와 정상 정렬 이후 차별적 예측이 필요하다. [§7의 실제 데이터 또는 명시적 simulator 범위](../research_candidates/2026-10-22_e1_buildup/R1_REVIEW.md#7-연구-가치와-다음-행동) 중 일관된 경로를 선택해야 한다. 효과를 실험 전에 입증하라는 조건은 아니다. 같은 metadata 재집계·GPU 확보만으로 재개하지 않는다. E2 전환은 이후 사용자의 새 조건부 요청에 따른 것이다. 실제 정책 실행과 외부 피드백은 미완료다.

**VLA-S1 당시 결과:** [문헌 16편](../research_candidates/2026-10-22_vla_rescout/LITERATURE.md), 최신 버전 수정, 4개 방향의 충돌/선별과 E1의 반증 조건을 정리했다. 당시 E1만 추가 심사를 추천했다. E2 시간 표현은 예비 질문으로 남겼고 이번에 B1 심사를 완료했다. 일반 memory/semantic retention은 새 후보로 승격하지 않았다. 외부 11편은 dossier 기록이며 registry admission은 아니다.

## 기존 후보의 완료와 재개 gate

**D3-B1 완료.** D2의 추가 MoManipVLA 후보 repo는 README/그림뿐이었고 기존 방법과 다른 예측을 확보하지 못해 HOLD를 유지했다. 사용자의 조건부 지시에 따라 [D3 8단계 비실험 심사](../research_candidates/2026-10-22_d3_buildup/README.md)를 수행했다. 문헌 8편·공개 text source 23개, Cooked 상태의 불변식, task 후보·강한 단순 baseline·기각 조건을 정리했다. 실제 정책 효과와 외부 피드백은 미완료다.

**D3-L1 완료.** [Task·policy 자격 심사](../research_candidates/2026-10-22_d3_buildup/TASK_POLICY_AUDIT.md)에서 공개 text source 32개·task 45 annotation 200개를 확인했다. Task-ID 기반 모델과 language-capable LL을 구분했고, 후자의 stock server가 외부 지시를 읽지 않는 점과 원래 goal/Q-score가 유지되는 점을 확인했다. [비실행 명세](../research_candidates/2026-10-22_d3_buildup/QUALIFICATION_SPEC.json)에 필요한 protocol을 작성했다. Source 경로는 확인했지만 실제 관측·정책 효과는 미검증이다.

**D3-R1 공개 심사 완료 / gate NOT_MET.** [추가 결과](../research_candidates/2026-10-22_d3_buildup/R1_REVIEW.md): annotation과 raw 파일 stem 200/200을 연결했지만 실제 사건–RGB pair는 미확보다. P2 평가에는 hotdog가 없고 turn-off 0/3은 burner였다. 별도 P4도 조리 전 placement 보고이며 checkpoint release를 식별하지 못했다. 전/후 시간 정렬·기본 능력·단순 predicate 대조를 보완했다.

**D3의 재개 gate는 D3-R2 / WAITING_EVIDENCE로 보존한다.** [증거 명세](../research_candidates/2026-10-22_d3_buildup/R1_EVIDENCE_REQUIREMENTS.json)의 동일 instance event/관측 packet·필요 skill 능력·matched 비교 자격을 확보할 때 재심사한다. 같은 문서 재조회나 adapter 구현을 자동 TODO로 반복하지 않는다. 이후 사용자의 새 VLA 탐색 요청으로 활성 작업을 VLA-S1/E1-L1로 변경했다.

**D2-B1 완료.** D1의 잔여 R1/R2/F1에 새 근거가 없어 사용자의 조건부 지시에 따라 D2로 전환했다. [기존 8단계에 따른 비실험 심사](../research_candidates/2026-10-22_d2_buildup/README.md)에서 문헌 10편·source text 12개, 가정/입력/학습 신호, 해석적 필요 조건, 비교/기각 계약을 검토했다. Native 실험과 실제 외부 피드백은 미완료다.

**D2-R1은 WAITING_EVIDENCE로 보존한다.** Attached geometry, 운반 가능한 grasp 학습, grasp/execution attribution, foresight RL 모두 직접 선행이 있다. 구체적인 공개 native task·executor, 기존 대안과 예측이 갈리는 조건, 공정한 비교를 함께 확보하기 전에는 구현/학습으로 진행하지 않는다. [재개 조건](../research_candidates/2026-10-22_d2_buildup/README.md#8-내부-반박과-다음-판단). 이번 D3 전환은 사용자의 후속 조건부 지시에 따른 것이다.

**우선순위 1–4 완료.** [비실험 재심사 결과](../research_candidates/2026-10-21_d1_buildup/NONEXPERIMENTAL_REVIEW.md): 선행과의 직접 충돌, 공통 최적 선택·정보 가치, task/평가의 대안 설명, RL 필요성을 심사했다. 현재 설계는 신규 방법 투자 NO-GO이며 실제 VLA 가설의 실험적 반증은 아니다.

**D1-R2는 보류 후보의 재개 gate로 유지한다.** 보정 선택의 예측이 갈리는 물리적으로 타당한 task, 가용 관측 cue, 단순 calibration/residual로 설명되지 않을 근거가 함께 필요하다. GPU 확보만으로 E1을 자동 재개하지 않는다. [기존 E1 resource preflight](../experiments/vla_d1_e1_preflight/RESULTS.md)의 자원 미확보·G0 전체 미충족·G1 미실행은 유지한다. 새 근거 없이 같은 문헌·preflight를 반복하지 않는다.

| ID | 상태 | 구체적인 작업 | 완료 기준 / 산출물 | 의존성 |
|---|---|---|---|---|
| DOC-R1 | DONE | 모든 기존 후보의 핵심·GPU 후속·한계를 주제별 한 파일로 요약 | [16개 요약 index](../research_candidates/summaries/README.md), 상세 근거와 등록 논문 연결 | NO-GO/HOLD/RETIRED 유지 |
| REG-R1 | DONE | 후보별 직접 비교·평가 문헌 누락 보완과 registry 동기화 | [47편 등록](REGISTRY_ROLLUP_2026-10-22.md), [무결성·보존 검증](REGISTRY_ROLLUP_VALIDATION_2026-10-22.md) | 신규 NEXT 18편은 UNREAD; 자동 정독 승격 없음 |
| E2-B1 | DONE | VLA의 시간 표현·feedback 빈도에 대한 8단계 비실험 buildup | [결과](../research_candidates/2026-10-22_e2_buildup/README.md), [source 감사](../research_candidates/2026-10-22_e2_buildup/SOURCE_INTERFACE_AUDIT.md), [검증](../research_candidates/2026-10-22_e2_buildup/VALIDATION.md). 일반 방법 NO-GO·진단 REVISE/HOLD | 단계 7 정적/해석적 부분·8 내부 판단. Native/실제 외부 피드백 제외 |
| E2-R1 | WAITING_EVIDENCE | 하나의 native 비교 packet과 차별적 예측의 재심사 | [현재 명세](../research_candidates/2026-10-22_e2_buildup/QUALIFICATION_SPEC.json): task/model/controller/time/evaluator 연결과 기존 대안 이후 질문 | 효과 사전 입증 요구는 아님. 같은 문헌 반복·GPU만으로 충족하지 않음 |
| E2-E1 | HOLD_RESEARCH | Qualified 경로의 최소 시간/feedback 비교 | R1 이후 현재 컴퓨터 Docker runtime·reset·split·budget을 확정하고 native/simple baseline부터 | 실행 spec 미완성·정책 실행 0회. 기존 D1-E2와 다른 ID |
| E2-F1 | NOT_STARTED | 실제 외부 반박 검토 | One-page 질문·closest work·source 차이·기각 기준에 대한 동료/지도교수 의견 | 내부 심사와 구분. 외부 발송은 명시적 요청 필요 |
| VLA-S1 | DONE | VLA 중심·RL 선택 사항으로 주제 재탐색 | [결과](../research_candidates/2026-10-22_vla_rescout/README.md), [문헌](../research_candidates/2026-10-22_vla_rescout/LITERATURE.md), [검증](../research_candidates/2026-10-22_vla_rescout/VALIDATION.md). E1 추가 심사 추천 | 연구 신규성·정책 효과·8단계 buildup 완료가 아님 |
| E1-L1 | DONE | 직접 방법·공개 data interface 심사 | [선행](../research_candidates/2026-10-22_e1_buildup/CLOSEST_WORK.md), [source/metadata 감사](../research_candidates/2026-10-22_e1_buildup/SOURCE_ASSET_AUDIT.md). 공개 release·mask·비용·annotation 확인과 미확보 경계 기록 | 심사 완료이며 code release/payload/native qualification 완료는 아님 |
| E1-B1 | DONE | 기존 8단계에 따른 비실험 1차 buildup | [결과](../research_candidates/2026-10-22_e1_buildup/README.md), [해석적 검사·계약](../research_candidates/2026-10-22_e1_buildup/CLAIM_CONTRACT.md), [검증](../research_candidates/2026-10-22_e1_buildup/VALIDATION.md). REVISE·진단 HOLD | 1–6 문헌/설계, 7 정적·해석적 부분, 8 내부 판단. Native/외부 피드백 제외 |
| E1-R1 | DONE | 실제 두 로봇의 비교 packet과 차별적 예측 자격 심사 | [결과](../research_candidates/2026-10-22_e1_buildup/R1_REVIEW.md), [metadata](../research_candidates/2026-10-22_e1_buildup/R1_METADATA_AUDIT.json), [검증](../research_candidates/2026-10-22_e1_buildup/VALIDATION.md#stage-1). 검토 완료·gate NOT_MET | RH20T 공통 task 59개, X-VLA interface·pose residual/시간/mask·prompt 대조. 정책 실행 없음 |
| E1-R2 | WAITING_EVIDENCE | 새 source/효과 정보/native 경로를 갖춘 재개 packet 심사 | [현재 요건](../research_candidates/2026-10-22_e1_buildup/R1_EVIDENCE_REQUIREMENTS.json), [구체적 다음 경로](../research_candidates/2026-10-22_e1_buildup/R1_REVIEW.md#7-연구-가치와-다음-행동) | 같은 metadata 재집계·GPU만으로 충족 안 됨. 새로운 packet이 생길 때 심사 |
| E1-E1 | HOLD_RESEARCH | E1의 native qualification·최소 비교 | R1 미충족 조건을 R2에서 해소한 뒤 현재 컴퓨터 Docker 자원·runtime와 실행 계약을 별도로 확정 | 새 연구 E1의 실험 ID. 과거 D1-E1과 다름. 현재 정책 실행 0회 |
| E1-F1 | NOT_STARTED | 실제 외부 반박 검토 | One-page 문제·선행·핵심 반례에 대한 지도교수/동료 피드백 | 내부 심사와 구분. 외부 발송은 명시적 요청 필요 |
| D3-B1 | DONE | 기존 8단계에 따른 D3 비실험 1차 buildup | [결과](../research_candidates/2026-10-22_d3_buildup/README.md), [문헌](../research_candidates/2026-10-22_d3_buildup/CLOSEST_WORK.md), [task/비교 계약](../research_candidates/2026-10-22_d3_buildup/TASK_CONTRACT.md). REVISE·추가 비실험 검토 추천 | 단계 7 정적 부분·8 내부 판단까지. Native/외부 피드백 제외 |
| D3-L1 | DONE | Cooking task의 policy·data·관측·goal 평가 경로 자격 심사 | [결과](../research_candidates/2026-10-22_d3_buildup/TASK_POLICY_AUDIT.md), [spec](../research_candidates/2026-10-22_d3_buildup/QUALIFICATION_SPEC.json), [검증](../research_candidates/2026-10-22_d3_buildup/VALIDATION.md#stage-1). 실행 자격 PARTIAL | Source 32개·annotation 200개. Native 효과·실행 qualification 완료가 아님 |
| D3-R1 | DONE | Cooked 전후 관측과 language LL continuation의 공개 재개 근거 심사 | [결과](../research_candidates/2026-10-22_d3_buildup/R1_REVIEW.md), [증거 명세](../research_candidates/2026-10-22_d3_buildup/R1_EVIDENCE_REQUIREMENTS.json), [검증](../research_candidates/2026-10-22_d3_buildup/VALIDATION.md#stage-2). 검토 완료·재개 gate NOT_MET | 기존 수치의 task 범위 수정·원자료 identity 연결·비교 교란 심사. 실험 없음 |
| D3-R2 | WAITING_EVIDENCE | 새 event/관측·continuation 증거 packet의 재개 심사 | [필요 조건](../research_candidates/2026-10-22_d3_buildup/R1_REVIEW.md#7-다음-행동과-재개-조건). 같은 instance의 근거와 matched 비교 자격 | 새로운 공개 자료 또는 별도 범위의 Docker qualification. 같은 metadata 재조회·GPU 확보만으로 충족하지 않음 |
| D3-E1 | HOLD_RESEARCH | Native competence와 사건 전후 switching 비교 | R1에서 미충족인 조건을 R2에서 해소하고 공정 비교·실행 계약을 충족한 후 현재 컴퓨터 Docker만 사용 | 문서 완료와 구분. 이번 범위에서 실험 제외. Runtime/seed/sample size 미선정; 정책 실행 0회 |
| D3-F1 | NOT_STARTED | 실제 외부 반박 검토 | 지도교수/동료의 반박과 반영 기록 | 내부 판단과 구분. 외부 발송은 명시적 요청 필요 |
| D2-B1 | DONE | 기존 8단계 절차에 따른 D2 비실험 1차 buildup | [결과](../research_candidates/2026-10-22_d2_buildup/README.md), [직접 문헌](../research_candidates/2026-10-22_d2_buildup/CLOSEST_WORK.md), [비교 계약](../research_candidates/2026-10-22_d2_buildup/CLAIM_CONTRACT.md). 넓은 방법 NO-GO·진단 HOLD | 1–6 문헌/설계, 7 정적 부분, 8 내부 판단 완료. Native/외부 피드백 제외 |
| D2-R1 | WAITING_EVIDENCE | 단일 task family의 재개 근거 확보 | 공개 native task/executor 식별자 + 기존 대안과 다른 예측·cue + matched 비교. 실험 전 효과 입증을 요구하지 않음 | 새로운 source/task 분석. 현재 문헌 반복이나 GPU 확보만으로 충족 안 됨 |
| D2-E1 | HOLD_RESEARCH | Native competence 및 geometry/planner/ranker 이후 gap | R1 통과 후에만 현재 컴퓨터 Docker에서 실행 계약 확정·최소 검증 | Task·checkpoint·runtime·split은 미선정, 실제 정책 실행 0회 |
| D2-F1 | NOT_STARTED | 실제 외부 반박 검토 | 지도교수/동료의 피드백과 반영 기록 | 내부 반박과 구분. 외부 발송은 명시적 요청 필요 |
| D1-N1 | DONE | G-PSMR/GAP/ReViP의 주장·실험 단위 직접 충돌 재심사 | [재심사 §1](../research_candidates/2026-10-21_d1_buildup/NONEXPERIMENTAL_REVIEW.md#1-d1-n1--주장실험-단위-직접-충돌-재심사). 버전·접근 한계 명시; 구현 미확보는 R1 | 공개 원문·공식 project |
| D1-N2 | DONE | Full observation에서 보정 선택이 필요한 조건 도출 | [재심사 §2](../research_candidates/2026-10-21_d1_buildup/NONEXPERIMENTAL_REVIEW.md#2-d1-n2--보정-선택이-필요한-조건). 공통 선택·regret·정보 가치·frozen policy 경계 | D1-L2 |
| D1-N3 | DONE | Goal 0/8·contrast 1의 반대 관점 심사 | [재심사 §3](../research_candidates/2026-10-21_d1_buildup/NONEXPERIMENTAL_REVIEW.md#3-d1-n3--현재-task의-적합성-반대-심사). Source 6개 재확인; 핵심 novelty task 미자격 | D1-L3/L4 |
| D1-N4 | DONE | RL 필요성과 최종 연구 위치 심사 | [재심사 §4](../research_candidates/2026-10-21_d1_buildup/NONEXPERIMENTAL_REVIEW.md#4-d1-n4--rl-필요성과-최종-연구-위치). 현재 method NO-GO, 진단 HOLD | D1-N1–N3 |
| D1-R2 | WAITING_EVIDENCE | 진단 pilot을 재개할 구체적 근거 심사 | [세 가지 재개 조건](../research_candidates/2026-10-21_d1_buildup/NONEXPERIMENTAL_REVIEW.md#43-다음-행동과-재개-조건). 예측·cue·단순 대안의 한계; 실험 전 효과 입증을 요구하는 것은 아님 | 새로운 source 또는 task 분석. 자원 변화만으로 충족 안 됨 |
| D1-L1 | DONE | 직접 baseline의 method/interface와 release 경계 보강 | [방법 감사](../research_candidates/2026-10-21_d1_buildup/BASELINE_METHOD_AUDIT.md), [source 기록](../research_candidates/2026-10-21_d1_buildup/baseline_method_sources_2026-10-22.json), dossier 수정. 재현 성공은 아님 | 기존 baseline dossier |
| D1-L2 | DONE | 보정의 필요성을 판별할 claim–evidence와 단순 대안 심사 | [분석·기각 계약](../research_candidates/2026-10-21_d1_buildup/CLAIM_EVIDENCE_CONTRACT.md). 모든 정책 결과 수치는 미실행 | D1-L1의 확인 범위 |
| D1-L3 | DONE | 실제 task 후보와 policy-visible 정보의 적합성 검토 | [40개 task·native 경로 감사](../research_candidates/2026-10-21_d1_buildup/TASK_OBSERVABILITY_AUDIT.md), [후보 4개 명세](../research_candidates/2026-10-21_d1_buildup/TASK_CANDIDATES.json). 실제 visibility·성능은 미검증 | D1-L2 완료 |
| D1-L4 | DONE | OFT/선정 task의 마지막 비실험 검증 계약 | [계약](../research_candidates/2026-10-21_d1_buildup/PRE_EXPERIMENT_CONTRACT.md), [spec](../research_candidates/2026-10-21_d1_buildup/PILOT_SPEC.json), [검증](../research_candidates/2026-10-21_d1_buildup/VALIDATION.md#stage-4). Report/초기 실제 자세 변화·reset/split/budget·기각 기준. 실행 artifact·효과 검증 아님 | D1-L3 완료; runtime/payload·realised split은 E1 |
| D1-R1 | WAITING_SOURCE | G-PSMR 구현·calibration manifest, GAP rule 차이/Octo recipe, ReViP 최신 구현/원문 확인 | 공개 release 또는 직접 source로 남은 항목을 확인. G-PSMR 수식상 gate 시점은 이미 확인 | 외부 자산 공개·접근; 다른 문헌 작업의 전면 blocker 아님 |
| D1-E1 | HOLD_RESEARCH | 후보 OFT의 clean competence·orientation/goal screening | [Docker resource preflight 수행](../experiments/vla_d1_e1_preflight/RESULTS.md). G0 전체 미충족, G1 0회. G1 통과만으로 유용한 state의 필요성을 입증하지 않음 | 먼저 R2 재심사, 이후 현재 컴퓨터 Docker 자원·payload/split/reset qualification. 자원 미확보도 계속 유지 |
| D1-E2 | HOLD_RESEARCH | 단순 baseline 이후 잔여 gap 검증 | G2/G3 paired rollout·비용·negative 결과에 근거한 채택 판단 | R2, E1, baseline qualification. 자동 실행 queue에서 제외 |
| D1-F1 | NOT_STARTED | 동료/지도교수 반박 검토 | 실제 피드백과 반영 기록 | 공유할 one-page brief; 외부 발송은 별도 명시적 요청 필요 |

## 직전에 완료한 것

- [x] **2026-10-22 / DOC-R1·REG-R1:** [후보별 단일 요약 16개](../research_candidates/summaries/README.md)와 [문헌 47편 등록](REGISTRY_ROLLUP_2026-10-22.md). 표준 note 235개 추가, 발표 상태·동일 논문 버전 확인, 기존 notes·manifest·읽기 이력 보존. 정책 실험·설치·PDF/weight 다운로드 없음.
- [x] **2026-10-22 / E2-B1:** [8단계 비실험 buildup](../research_candidates/2026-10-22_e2_buildup/README.md) 완료. 공식 proceedings 4편과 직접 preprint 5편, 세 방법 family의 pinned source를 대조했다. 시간 재표현/retiming/feedback/controller를 분리하고 넓은 방법 주장은 NO-GO, 진단은 REVISE/HOLD로 남겼다. 주력 연구 채택은 보류, E2-R1은 새 비교 packet 대기다. 정책 실행·설치·registry 변경 없음.
- [x] **2026-10-22 / E1-R1:** [후속 buildup](../research_candidates/2026-10-22_e1_buildup/R1_REVIEW.md) 완료. 공개 RH20T view metadata 82,920개에서 UR5/Franka 공통 task ID 59개·task 6/8 후보를 확인했다. X-VLA-Pt의 미래 pose·시간 보간·실제 loss·두 domain 경로, RoboInter VLM/VLA release 경계를 감사했다. 정상 pose residual 이후 차별적 예측은 미확보, REVISE·진단 HOLD. [현재 명세](../research_candidates/2026-10-22_e1_buildup/R1_EVIDENCE_REQUIREMENTS.json)의 R2 evidence 대기. Registry·tier·읽기 상태 유지, 정책 실행 0회.
- [x] **2026-10-22 / E1-L1·B1:** [E1 buildup](../research_candidates/2026-10-22_e1_buildup/README.md). 직접 선행의 VLA estimator/MIR·물리 정렬 범위, 공개 action mask·replay step scaling, RoboMIND annotation 6,073개와 EE anomaly 보고, RH20T 시간/pose API를 감사했다. 가중 metric 동치·망각 방향 반례·counterfactual 정보 한계를 도출했다. 새 방법 채택 보류, REVISE·진단 HOLD. R1은 evidence 대기, 실험/외부 피드백 미완료. Registry·tier·읽기 상태 유지.
- [x] **2026-10-22 / VLA-S1:** [새 주제 탐색](../research_candidates/2026-10-22_vla_rescout/README.md). 공식 proceedings 8편 포함 16편 비교, 실환경 continual v3·PaceVLA v2 반영. E1을 조건부 비실험 심사 후보로 남겼다. Registry/tier/reading status 유지, 정책 실행·설치 없음.
- [x] **2026-10-22 / D3-R1:** [공개 근거 심사](../research_candidates/2026-10-22_d3_buildup/R1_REVIEW.md) 완료. Raw/annotation stem 200/200, 실제 사건·RGB 정렬 미확보. P2 skill 평가의 task·대상·미공개 evaluator 경계를 확인했고 P4는 post-event witness가 아님을 확인했다. 두 추가 arXiv 평가 연구와 대조해 단순 predicate·기본 능력·time/goal/denominator 통제를 보강했다. Gate NOT_MET, 연구 REVISE·실험 HOLD. Registry와 reading status 유지.
- [x] **2026-10-22 / D3-L1:** [자격 심사](../research_candidates/2026-10-22_d3_buildup/TASK_POLICY_AUDIT.md)에서 task 45의 실제 dataset/source 연결과 정책 후보를 확보했다. 공개 annotation 200개 모두 마지막 skill은 turn-on이며 event timestamp와 post-event 성공은 입증하지 않는다. Language LL model 경로와 고정 지시 server를 분리하고 양쪽 action queue·goal/termination/Q-score·absolute joint hold 계약을 작성했다. D3 REVISE·실행 PARTIAL·full-task/학습 HOLD. Registry 유지, 정책 실행 0회.
- [x] **2026-10-22 / D2 재개 심사 + D3-B1:** 추가 공개 자산이 D2 재개 근거를 충족하지 못해 HOLD 유지 후 D3로 전환했다. [D3 결과](../research_candidates/2026-10-22_d3_buildup/README.md): 일반 switching/rollback 방법은 직접 충돌, 목표 가능성을 구분하는 진단으로 REVISE. Cooked·dicing source, SafeLoop의 실행 mode, VoLo의 정보 차이, task별 baseline recipe 경계를 확인했다. 외부 4편은 dossier에 기록했고 registry는 유지했다. [검증](../research_candidates/2026-10-22_d3_buildup/VALIDATION.md).
- [x] **2026-10-22 / D1 전환 심사 + D2-B1:** D1의 판정을 바꿀 새 비실험 근거를 확보하지 못해 보류를 유지하고 D2를 검토했다. [D2 결과](../research_candidates/2026-10-22_d2_buildup/README.md): ReKep/WBAG, Cooperative Grasping, GTP-FA/foresight RL까지 좁힌 주장과 충돌. 넓은 신규 방법 투자 NO-GO·구체적 진단 HOLD. 외부 6편은 비교 dossier에 기록했고 registry 신규 등록은 하지 않았다. [검증](../research_candidates/2026-10-22_d2_buildup/VALIDATION.md).
- [x] **2026-10-22 / D1-N1–N4:** 요청한 우선순위 네 항목을 비실험으로 완료했다. [결과](../research_candidates/2026-10-21_d1_buildup/NONEXPERIMENTAL_REVIEW.md), [source 경계](../research_candidates/2026-10-21_d1_buildup/nonexperimental_sources_2026-10-22.json). 현재 신규 방법 투자 NO-GO·진단 HOLD. Native 효과 검증·외부 피드백 완료는 아니다.
- [x] **2026-10-22 / D1-E1 resource preflight:** Docker process 실행과 GPU allocation 실패, 실제 VM memory·게시된 model 크기를 확인했다. Goal normalizer 내용/hash, remote/local code 차이와 unpinned downloader를 감사했다. [결과·한계](../experiments/vla_d1_e1_preflight/RESULTS.md). E1/G1 완료 표시가 아니며 전용 container/image는 정리했다.
- [x] **2026-10-22 / D1-L4:** Report 오류와 정상 controller로 만든 초기 자세 변화를 분리하고 reset replay·split·예산·qualification 계약을 고정했다. Source 8개 추가 확인에서 flat state의 fixture/controller memory 누락 위험과 expert-success filtering 경로를 확인했다. [결과](../research_candidates/2026-10-21_d1_buildup/PRE_EXPERIMENT_CONTRACT.md). 실제 정책 episode는 0이며 미확보 runtime/payload는 null로 보존했다.
- [x] **2026-10-22 / D1-L3:** 40개 task의 실제 goal과 모델/controller 경로 감사. `pi05_libero`의 state-value 전제 실패를 발견하여 OFT Goal 후보로 변경했고 task ID 0/8·1/7을 정했다. Source 90개·hash와 모델 목록 확인은 정적 검토이며 실행이 아니다. [결과](../research_candidates/2026-10-21_d1_buildup/TASK_OBSERVABILITY_AUDIT.md).
- [x] **2026-10-22 / D1-L1:** 직접 baseline 정밀 대조. G-PSMR 초기 고정 gate·결합 순서, GAP 공식판과 공개 rule 차이·training entrypoint의 정적 문법 오류, ReViP 버전 경계 기록. [검토 결과](../research_candidates/2026-10-21_d1_buildup/BASELINE_METHOD_AUDIT.md).
- [x] **2026-10-22 / D1-L2:** 일정한 회전 bias를 단순 보정으로 제거할 수 있는 조건 도출; causal 재보정·task별 reference 대조, 주장별 반증 조건·paired metric 명세 작성. **연구자 분석이며 정책 검증이 아님.** [결과와 다음 행동](../research_candidates/2026-10-21_d1_buildup/CLAIM_EVIDENCE_CONTRACT.md).
- [x] **2026-10-22 / baseline 문헌 확보:** π0.5, OpenVLA-OFT, GAP, Octo, G-PSMR, ReViP의 역할·공개 자산·비교 조건 작성. [Dossier](../research_candidates/2026-10-21_d1_buildup/BASELINE_DOSSIER.md).
- [x] **2026-10-22 / source identity 확인:** 4개 repo의 9개 source 파일과 OFT model repository revision·파일 목록 확인. 설치·weight 다운로드·실행은 아님. [정적 기록](../research_candidates/2026-10-21_d1_buildup/baseline_sources_2026-10-22.json).
- [x] **2026-10-21 / D1 1차 buildup:** 관측 가능성·행동 필요성 반례, 직접 문헌 비교와 공개 interface 감사. Native VLA 효과는 미검증. [결과](../research_candidates/2026-10-21_d1_buildup/RESULTS.md).
- [x] **2026-10-21 / 외부 문헌 등록:** 16편 추가 후 registry 990편, CORE 47 / NEXT 257 / REFERENCE 444 / ARCHIVE 242. [이력](UPDATES_2026-10-21.md).

## 재개할 때 유지할 조건

- E1-L1/B1/R1의 비실험 심사는 완료했다. R1 gate는 NOT_MET이며 E1-R2 재개 심사와 이후 Docker qualification을 구분한다. 문서 완료를 runtime qualification·연구 효과 입증으로 해석하지 않는다. E1 및 D1/D2/D3의 연구 gate를 통과하기 전에는 과거 실행 허가만으로 학습을 재개하지 않는다.
- 현재 디렉토리는 paper registry이며 실제 작업 artifact는 `work/`에 둔다. 이 파일은 단일 작업 인계표다.
- 문헌·정적 source 읽기와 정책 실험을 구분한다. D1-E1 요청은 현재 컴퓨터 Docker의 G0 검증과, 조건 충족 시 G1 진행을 허용한다. Dependency·model/data는 Docker 내부에서만 취급하고 resource gate 실패 시 큰 다운로드·학습을 시작하지 않는다. 호스트에는 패키지를 설치하지 않는다.
- 공식 GPU 경로가 없다는 이유로 새로운 작은 정책을 학습해 native VLA 검증을 대신하지 않는다.
- C1–C6의 기존 NO-GO/HOLD는 유지한다. 새로운 재개 근거 없이 다시 실험하지 않는다.
- Registry 노트 생성·정적 검토로 사용자 READ/REPRODUCED 상태를 올리지 않는다. 기존 사용자 변경을 보존한다.
- 미공개 구현은 `WAITING_SOURCE`로 남기되 독립적인 문헌·분석 작업을 계속한다. 코드 링크 존재를 실행 검증으로 취급하지 않는다.
- N1–N4 이후의 현재 연구 판정을 우선한다. 과거 L4/E1의 자원 확보 후 재개 문구만으로 실험을 재개하지 않는다. R2를 먼저 확인한다.

## 갱신 규칙과 인터넷 참고

상태는 `READY → IN_PROGRESS → DONE`으로 관리한다. 순서가 남으면 `QUEUED`, 자산·자원 의존성은 `WAITING_SOURCE`/`WAITING_RESOURCE`, 새 연구 근거를 기다리면 `WAITING_EVIDENCE`, 연구 판단상 실행을 보류하면 `HOLD_RESEARCH`, 미착수 별도 검토는 `NOT_STARTED`로 표시한다. `DONE`은 **정의한 문서·검토 작업의 완료**이며 연구 가설이 참이라는 뜻이 아니다. 시작/완료 시 결과 링크·다음 행동·보류 사유를 갱신한다.

인터넷에서 다음 운영 방식을 참고했다. 아래의 로컬 파일 형식·상태 이름·완료 기준은 이 저장소에 맞춘 설계다.

- [GitHub 공식 Issues guide](https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues): 큰 작업을 작은 항목으로 나누고, 의존성과 metadata·관련 산출물을 연결하는 방식.
- [The Turing Way — Ways of Working](https://github.com/the-turing-way/the-turing-way/blob/main/ways_of_working.md): 공개 연구 프로젝트에서 작업 목록과 project management 기록을 지속적으로 점검하는 운영 사례.

전체 이력을 이 파일에 복제하지 않는다. 최근 완료와 활성 항목만 유지하고 상세 결과는 날짜별 log로 연결한다. 외부 issue 생성·연락·자동 일정 등록은 하지 않았다.
