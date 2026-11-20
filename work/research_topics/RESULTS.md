# 종료·보류 결과

과거 후보의 판정과 다시 쓸 수 있는 결과를 모았다. 현재 진행 순서는 [다음 작업](../../TODO.md), 실행 중인 후보는 [연구 후보](./README.md)에서 확인한다. 종료·보류 판정은 연구 투자 판단이며, 실험하지 않은 효과는 미검증이다. 새 문헌·자료가 판정을 바꿀 때만 재심사한다.

## 문헌·실행에서 확인한 결과

| 대상 | 확인한 결과와 남은 조건 |
|---|---|
| 실행 명령만 남은 시연의 선택적 재수집 | **공개 표본에서 보류.** DROID의 제한 전 목표와 두 공유 제어 자료의 사용자 요청이 남아 있었다. 기어 맞물림 학습본에 빠진 기본 명령은 수집 코드에 기록 경로가 있다. 복원 불가능한 기록과 독립적으로 방향을 바꿀 수 있는 가이드가 같은 작업에서 확인되면 재개한다. [판정·반례·비용 비교 조건](./demonstration_recollection/내용/README.md) |
| 조립 복구에서 손목 엔코더만으로 두 행동 중 하나 선택 | **이 선택 방식은 보류.** 가정한 0.01 mm 잡음에서 고정 절차보다 성공이 적었다. 실제 손목에서 계측한 잡음이나 다른 기구의 하중 해제 신호가 두 원인을 더 잘 구별할 때 재검토한다. [손목 단독 판정](./assembly_recovery/내용/README.md#wrist-results) · [상대변위 추가 결과](./assembly_recovery/내용/README.md#relative-results) |
| 조립 복구에서 손목 왕복 후 선택한 재파지·탐색 | **한 축 오차 범위를 아는 모형에서 판별기 개발·실물 이관 보류.** ±12 mm에서 서보 변화에 따른 선택 오류가 정상 핀 보정으로 줄었다. ±9 mm에서는 즉시 재파지 후 탐색이 양쪽 첫 방향·두 이득·두 예산에서 모두 48/48개를 해결했다. 주 비교에서 고정 절차 1.355초, 진단 후 완벽하게 선택할 때도 최소 1.479초였다. 실제 공정의 허용 경로에서 원인에 따라 고정 복구의 성공·손상이 갈리는 증거가 재개 조건이다. [탐색 폭·판정](./assembly_recovery/내용/README.md#scan-results) · [서보 응답](./assembly_recovery/내용/README.md#servo-results) |
| 직전 시행이 남긴 문 기구 상태 | **실물 확대 보류.** 공개 Panda 문 정책은 장면 4개에서 문짝만 닫은 조건과 독립 복원 모두 동률이었다. 0.6초 뒤 손잡이 각도만 순간 정렬한 처치에서만 한 건 실패했다. 실제 닫기 동작과 저렴한 대기 뒤에도 정책 선택이 달라지는 독립 근거가 생기면 재검토한다. [설계·실측·한계](./reset_carryover/내용/README.md) |
| <a id="cross-embodiment"></a>로봇 간 RL 전이 | **종료.** 기본 정책의 유효 실행 능력을 확보하지 못해 전이 실험을 끝내지 못했다. 성공 시연 선별·return-weighted imitation과 RL의 효과는 미분리다. |
| <a id="execution-latency"></a>실행 지연·적응형 chunk | **종료.** 기존 latency·chunk·replanning 연구 이후 넓은 방법 차별성이 부족했다. 시간 표현과 피드백을 분리하는 문제는 [E2](#e2)에 남겼다. |
| <a id="rp2"></a>실패 복구 선택 / <a id="rp3"></a>기억 만료 | **종료.** 복구는 같은 실패 시점의 대안 행동별 결과, 기억은 실제 memory 사용과 stale 상태의 행동 영향을 분리할 근거가 미확보다. 정책 비교는 미실행이다. |
| <a id="c1"></a>C1 추가 관측 | **진단 보류.** SmolVLA strict load와 243개 명령 실행을 확인했다. 제한 시간 내 과제 수행 능력은 미확인이다. 관측 정책의 순이득과 전체 관측 비용은 미측정이다. |
| <a id="c2"></a>C2 수행 제약 | **현 설계 종료.** Metadata 400개·지시 200개·payload 12쌍·경유 trace 50개를 확인했다. 완전한 pose/reward label·coverage와 native 실행 조건은 미충족이었다. |
| <a id="c3"></a>C3 행동 토큰 동치 | **본격 학습 비추천.** 한 checkpoint의 관측 16개에서 T=1.6 전체 chunk head-score trace 감소가 약 0.496%였고 감소량의 약 99.62%가 마지막 gripper slot에 집중됐다. 정책·reward-weighted gradient 효과는 미측정이다. [저장값 재분석](../experiments/portable/README.md) |
| <a id="c4"></a>C4 보상 검수 | **방법 종료·진단 보류.** Robometer export의 571 episode와 RoboReward의 54,135 row를 별도로 확인했다. 동일 정책의 RL round·당시 보상 예측·독립 결과를 연결할 기록은 미확보다. |
| <a id="c5"></a>C5 reset 범위 | **방법 종료·진단 보류.** 공개 기록의 retry·human intervention 흔적을 확인했다. 최초 시도부터 실패·구제·reset까지 모두 계수할 기록은 미확보다. |
| <a id="c6"></a>C6 checkpoint 선택 | **방법 종료.** RACE의 checkpoint 집계 57개에는 독립적인 trial 순서·seed·초기 상태가 없었다. 집계로부터 정책 선택의 손실이나 trial 결과를 추정하지 않았다. |
| <a id="d1"></a>D1 관측 보정 | **방법 종료·진단 보류.** 실제 상태 변화에도 보정이 유리할 수 있는 반례를 확인했다. 후보 `pi05_libero`의 state 입력은 해당 action 경로에 연결되지 않았다. 대체 OFT는 local GPU 할당 실패로 정책 평가 0회다. |
| <a id="d2"></a>D2 파지와 운반 | **방법 종료·진단 보류.** ReKep·공동 파지·geometry shield가 이미 후속 운반을 고려한다. 같은 파지 후보, attached geometry, 계산 예산 아래 독립 운반 결과가 있는 비교는 미확보다. |
| <a id="d3"></a>D3 사건 후 지시 변경 | **수정 검토·보류.** 조리 annotation과 raw stem 200/200의 일치는 event–RGB 짝을 보장하지 않는다. P2의 turn-off 0/3은 burner이고 P4는 조리 전 placement다. 동일 물체 사건 전후의 관측·지시 실행 능력·변경 목표 평가가 함께 필요하다. |
| <a id="e1"></a>E1 행동 충돌과 replay | **수정 검토·보류.** RH20T 두 로봇의 공통 task ID 59개를 확인했다. View를 독립 trial로 세지 않는다. Episode/time/command 및 실제 효과를 묶은 평가 자료는 미확보다. |
| <a id="e2"></a>E2 시간 표현과 피드백 | **방법 종료·진단 보류.** 기존 RTR의 두 recipe가 horizon과 servo mode를 함께 바꾼다. 시간 표현·fresh observation·controller의 인과 효과는 미분리다. |
| <a id="semantic-retention"></a>VLM 의미 능력 보존 | **후보 미채택.** VLM2VLA·LAP가 적응·전이를 직접 다룬다. VQA 보존과 로봇 스킬·전이 결과의 연결은 미검증이다. |
| <a id="navigation"></a>반응형 주행 | **방법 종료·진단 보류.** CPU 시뮬레이션 384개 branch, 192개 paired prefix에서 사전 정의한 공동 기준을 통과하지 못했다. Native VLA는 미실행이다. [비교 결과](../experiments/reactive_nav_pilot/RESULTS.md) |

## 폐기한 후보

| 대상 | 남길 결과 |
|---|---|
| <a id="action_tokenization"></a>행동 토큰화 | 20 episode·101 window의 오프라인 복원 진단에서 양자화·복원 비교를 확보했다. 실제 정책 선택을 바꾸는 근거는 미확보다. |
| <a id="context_retrieval"></a>시연 검색 | Archive hash와 261개 frame을 확인했다. 시연 성공·독립 평가·정책 성능은 미검증이다. 목표별 검색보다 나은 근거가 부족했다. |
| <a id="object_set"></a>물체 집합 선택 | 수량·선택 평가를 설계했다. 반복 실행·외부 counter 이후에도 남는 행동 실패는 미확인이다. |
| <a id="mobile_policy_transfer"></a>이동 조작 정책 교체 | 단일 scene template를 검토했다. 도착 후 정책 A/B 분기와 성능 비교는 미실행이며 일반성을 확보할 구현 부담이 컸다. |
| <a id="task_allocation"></a>학습 예산 배분 | CPU 제어 검사 24개를 수행했다. 균등 배분·비용 보정 대비 이득과 native 학습 비용은 미측정이다. |
| <a id="hindsight_transfer"></a>Hindsight 목표 선택 | CPU 제어 검사 15개와 대조 설계를 확보했다. 자연 실패에서의 재라벨과 원 목표 전이 효과는 미검증이다. |
| <a id="vla_residual_update"></a>Residual RL 재사용 | CPU 제어 검사 9개를 수행했다. Base model 교체 후 warm-start와 동일 자료 모방 이후의 이득은 미검증이다. |

기존 후보 폴더의 원본 137개(기획·문헌 검토 13묶음과 요약 1묶음)는 정리 전 커밋에서 찾을 수 있다. C3에 사용하는 저장 입력과 launcher는 [Docker 재현](../experiments/portable/README.md)에 연결했다. [과거 후보별 원문](https://github.com/Kim-Yoo-Hyun/PaperReview/tree/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/research_candidates) · [폐기 판정과 원자료](https://github.com/Kim-Yoo-Hyun/PaperReview/tree/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/research_topics/retired) · [당시 실행 기록](https://github.com/Kim-Yoo-Hyun/PaperReview/tree/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/experiments)
