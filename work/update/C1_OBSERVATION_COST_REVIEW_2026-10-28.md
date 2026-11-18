# C1-E1 — 추가 관측을 언제 생략할 수 있는가

> 2026-11-17 인계: 이 문서의 폐기 후보(HANDOFF/SET/RETRIEVAL/CODEC1/ALLOC/HINDSIGHT/VRL) 계획·명령은 당시 기록이다. 현재는 RETIRED이며 새 실행 queue가 아니다. 링크는 핵심 보존본 또는 삭제 전 Git revision으로 연결한다.

- 확인일: **2026-10-28 KST / 비실험 문헌 비교 완료**.
- 범위: 기존 C1와 지정 3편의 arXiv v1 본문 구간·공식 abstract. 세 논문은 **2026 preprint**로 취급하며 top-tier acceptance를 확인한 것으로 표시하지 않는다. [Source ledger](../sources/c1_observation_cost_review_2026-10-28.json).
- 결론: **작은 평가·실증 질문으로 유지한다.** 같은 frozen VLA에서 초기 관측만 사용하는 간단한 규칙으로 추가 관측을 생략해 시간·동작을 줄일 수 있는지 묻는다. 성공률 유지, 선택의 필요성, 신규성·독립 논문 가치는 아직 미확인이다.
- [Canonical 질문](../../synthesis/04_vla_generalist.md#gap-selective-observation-2026), [C1 단일 요약](../research_candidates/summaries/C1_SELECTIVE_OBSERVATION.md), [TODO](../../TODO.md). 본격 rollout·학습 HOLD와 과거 결과는 보존한다.

## 1. 실제 비교된 관측·정렬·비용

아래는 **저자 보고의 지정 구간 대조**다. 논문 간 성공률을 합치거나 서로 빼지 않는다. `미보고`는 확인 구간에서 해당 비교를 찾지 못했다는 뜻이며 문헌 전체의 부재 증명이 아니다.

| 근거 | 실제 비교와 정책 정렬 | 시간·비용에서 확인한 내용 | C1에 남는 경계 |
|---|---|---|---|
| **ActiveAlign**, [§III-B–D, IV-A–B, Tables I–VI](https://arxiv.org/html/2610.23378v1) | 한 번의 pre-contact AP. Standard와 Naive Active는 기존 정책에 AP 유무를 달리하고, ActiveAlign은 정렬된 시연으로 재학습한다. Matched-state/data 통제와 mixing 통제도 명시 | Suite별 horizon·생성 pose 수 K의 sensitivity 보고. Simulation IK repositioning과 실제 연속 이동을 구분 | **Adapted 정책의 skip/always/selective 비교와 전체 물리 시간 통제는 미확인.** 원래 시연이 전혀 섞이지 않았다고 단정하지 않음. K는 초 단위 시간이 아님 |
| **EyeRobot 2.0**, [§3–6](https://arxiv.org/html/2610.03710v1) | 고정 stereo 영상에서 가상 fixation을 구성. Task별 gaze selector와 BC 조작 정책을 공동 학습하며 No Gaze·Ego+Wrist 및 표현 ablation 비교 | Sim gaze settling 1초, baseline/제안법 chunk 1/1.5초 명시 | Head/neck 이동을 다루지 않음. **재학습된 task별 gaze 시스템의 비교를 frozen VLA의 물리 look/skip 비교로 치환할 수 없음** |
| **RESCUE**, [§III, IV-A·E, V](https://arxiv.org/html/2610.13516v1) | 같은 robot-policy state에서 Continue/고정 Recover를 분기. Stop-and-reset은 해석적으로 평가 | Recover는 조건에 따라 20/30 steps; 남은 예산은 220−t. Step cost와 reset/retry를 합친 비용 모델 | 비교 가능한 개입 가치·비용 틀은 이미 존재. **현재 repertoire는 물리 look 선택이 아니지만 look branch 추가만으로 새 방법이 되지는 않음.** Reset 비용 단위·threshold를 C1의 초 단위 비용에 그대로 이전하지 않음 |
| **기존 C1**, [protocol](../research_candidates/2026-10-20_vla_rl/C1_PROTOCOL.md)·[review](../research_candidates/2026-10-20_vla_rl/C1_REVIEW.md)·[probe 결과](../experiments/vla_rl_active_handoff/RESULTS.md) | Immediate/look/wait·heuristic 비교는 설계만 존재. SmolVLA strict load·243 actions 기록 | 과거 제한된 실행에서 competence를 확인하지 못함 | **선택적 관측의 부정 결과가 아니다.** 이번에는 runtime·코드·과거 trace를 재실행하지 않음 |

세 선행을 함께 읽으면 관측 선택, 정책 정렬, 개입 비용은 모두 기존 연구의 일부다. 아직 확인하지 못한 좁은 비교는 **같은 정책을 고정하고 실제 추가 관측을 생략하는 결정이 성공과 소요 시간에 주는 영향**이다. 이를 전체 분야의 미해결 공백이나 새로운 알고리즘으로 확정하지 않는다.

## 2. 남기는 질문과 무엇을 결정하는가

**연구자 질문:** 같은 frozen VLA와 전체 물리 시간 예산에서, **관측 동작 전 정보만** 사용하는 간단한 규칙이 항상 관측하는 전략에 비해 성공률을 허용 범위 안에서 유지하면서 관측 동작·시간을 줄일 수 있는가? 초기 시야와 시작 자세에 따라 어느 전략이 충분한가?

답은 매 episode에서 관측 동작을 수행할지, 단순 gate를 쓸지, 정책을 적응시켜야 할지를 결정하는 데 쓰인다. “반드시 selective가 이긴다” 또는 “순차 RL이 필요하다”를 가정하지 않는다. 항상 관측하거나 바로 실행하는 전략이 충분한 범위를 찾는 것도 답이다. 다만 차이가 유의하지 않다는 사실만으로 동등성·안전한 생략을 주장하지 않는다.

**정렬에 대한 주의 — 연구자 해석:** AP endpoint에 적응된 정책이 skip 시작 상태도 잘 처리하는지는 따로 관찰해야 한다. 반대로 원래 정책에 look만 붙여 생기는 손실은 새 이미지의 가치와 endpoint 지원 범위를 함께 반영한다. Standard의 immediate 결과와 adapted 정책의 look 결과를 빼서 선택 자체의 이득으로 부르면 안 된다. 처음부터 양쪽 성공을 증명해야 탐색할 수 있는 것은 아니며, 관찰된 차이의 해석 범위를 제한하면 된다.

**가장 작은 구분:** C1은 한 정책 안에서 look을 할지 결정한다. [HANDOFF](../research_topics/retired/README.md#mobile_policy_transfer)는 A에서 고른 도착 설정을 B에 재사용할지 결정한다. C1의 결과가 endpoint와 정책의 호환성만 보여 준다면 HANDOFF의 한 사례로 통합하고 독립 기여 두 개로 세지 않는다.

## 3. 작은 비교 초안 — 실행 계획은 아직 아님

다음은 탐색을 위한 비교 구조다. 환경·checkpoint·표본 수·threshold·허용 손실을 동결한 manifest가 아니다. 과거 G0의 수치나 runtime 설정을 현재 실행 계획으로 자동 재사용하지 않는다.

| 축 | 최소 설계와 해석 |
|---|---|
| 시작 범위 | 한 embodiment·한 policy와 적은 task. 초기 관측에서 정의할 수 있는 시야/시작 자세 조건을 포함하되 선택 가치의 양·음 교차를 사전 요구하지 않음 |
| 기본 전략 | **Immediate / 항상 한 번의 물리 look / 초기 visibility 또는 confidence의 단순 규칙**. 강한 단순 규칙부터 비교하며 새 learned selector·RL은 시작 요건이 아님 |
| 정책 고정 | 세 전략은 같은 weights·normalizer·입력/action interface·controller를 사용. Adapted/unadapted를 볼 경우 각 checkpoint 안에서 먼저 세 전략을 비교하고 학습 비용은 별도 기록 |
| Gate 입력 | 첫 RGB/허용 proprioception/지시에서 얻는 값만 사용. Look 이후의 가시성·성공 label로 skip 여부를 고르면 oracle 진단일 뿐 실행 전략이 아님. 수동 시야 label은 사후 분석용과 deployed gate를 구별 |
| 선택과 평가 | Threshold를 고른 calibration scene과 평가 scene을 분리. 같은 완전한 시작 상태에서 전략별 분기; simulator·정책 cache/RNG·controller 복원의 유효성은 실행 전 확인. Frame을 독립 trial로 세지 않음 |
| 주 관측량 | 전체 예산 B 내 task success와 차이의 불확실성, 실제 관측 수행 비율, 성공·실패를 포함한 시간/timeout. 성공 episode만의 빠른 평균으로 효율을 주장하지 않음 |
| 비용 단위 | 물리 이동·settling·센서 대기·gate/정책 추론의 실제 지연을 기록. 겹쳐 실행되는 계산은 총 경과 시간에 중복 가산하지 않음. Sim step·카메라 pose/token 수·벽시계 시간을 분리; 모든 전략의 시작 시점부터 budget을 계산 |
| Skip 판단 | 의미 있는 성공률 손실 허용치와 시간 절감 목표는 후속 확인 전에 정함. 보존을 주장하려면 성공률 차이의 구간이 허용치와 양립해야 함. Pilot의 점추정·비유의성만으로 동등성을 선언하지 않음 |
| 보조 진단 | 시간만 맞춘 wait는 지연 효과 검사. Pose-matched/고정 시야 대조는 정보·자세를 나눌 때 추가하며 순간 camera teleport는 실제 행동 baseline으로 세지 않음. Wait 자체도 물체 동역학을 바꿀 수 있음 |
| 실패 처리 | Look 미완료·충돌·물체 이동·초기 실행 실패도 전체 분모와 비용에 포함. Success-filtered endpoint만 남겨 skip/always를 비교하지 않음 |

첫 비교의 목표는 **전체 개입 효과**다. 정보 획득만의 인과 효과를 주장하려면 추가 통제가 필요하지만 그 통제를 모두 끝내야 탐색 질문을 보존할 수 있는 것은 아니다.

과거 C1의 단일 관측 입력에 대한 정적 검토도 유효한 주의점이다. 과거 시야를 저장하지 않는 정책이 look 후 동일한 최종 입력으로 돌아온다면 새 정보를 전달할 경로가 없을 수 있다. 이를 모든 VLA의 한계로 일반화하거나 현재 checkpoint의 재검증 결과로 표시하지 않는다. 물리 이동의 endpoint 관측을 유지할지, memory를 쓸지는 이후 선택한 정책의 실제 입력에 맞춘다.

## 4. 판정·종료점·다음 행동

- **C1-E1 DONE; 탐색 질문 유지·구체화.** 지정 3편의 비교와 기존 C1의 실행 경계를 정리했다. 새 방법 채택·RL 필요성·효과·독창성은 미입증이다. 작은 진단을 검토할 가치는 있으나 독립 논문으로 발전할 가치는 실제 결과 이후 판단한다.
- 정책을 고정해도 skip/always 차이가 있는지, 단순 규칙이 충분한지는 **실험 필요·미확인**이다. 같은 세 논문을 재감사하거나 문서만 추가해서 해결할 수 없다. 그 이유로 후보를 폐기하지 않는다.
- Immediate/always가 충분하면 새 selector를 만들지 않는다. 규칙이 충분하면 그 조건과 범위를 정리한다. 차이가 작거나 불확실하면 현재 범위의 미확인으로 남긴다. 순차 RL은 one-step 선택으로 설명되지 않는 순차 결정의 필요성이 생길 때 별도로 검토한다.
- 현재는 비실험 요청이므로 여기서 C1 문헌 단계를 마친다. 다음 TODO는 **GAP-TERM-E1 READY**: 기존 자료의 first-hit/fixed-horizon/autonomous-stop 비교를 압축한다. C1·HANDOFF 질문과 과거 실행 HOLD를 보존한다.
- 향후 실행은 선택한 작은 비교에 필요한 native competence·물리 primitive·입출력·budget·scene split을 확인한 뒤 **로컬 Docker**에서만 수행한다. 현재 GPU 상태는 재확인하지 않았으며 실험·설치·PDF/weights/dataset 다운로드·신규 논문 등록·읽기 승격은 없다.

## 5. 문서 검증

`py_compile`, reading generator, `git diff --check`, repository audit를 완료했다. 오류·경고 **0**, registry **1,072편**, tier **47/297/486/242**, active/history 읽기 기록 **344/47**, 표준 note **5,360개**를 유지한다. Markdown **5,541개**·상대 링크 **10,979개** 검사 통과.

AGENTS·PAPER·manifest/meta·tier CSV·active/history CSV **7개가 작업 전과 byte-identical**이다. 기존 dirty **655개** 중 이번 수정 **8개** 외 **647개**와 기존 삭제 **10개**를 보존했다. 신규 파일은 이 보고서와 source ledger **2개**이며 generator의 추가 내용 변화는 없었다. 문서 무결성 검사는 정책 효과 검증이 아니다.
