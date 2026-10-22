# VLA + RL: 새 연구 주제의 후보 검토

> 후속 2026-10-21: 사용자의 다른 주제 검증 요청으로 [별도 C3](../2026-10-21_execution_interface/README.md)를 검사했다. 공개 실행 interface·PPO loss의 mechanism 확인 결과이며 실제 정책 효과는 미검증이다. 아래는 C1/C2의 보존된 판정이다.

- 조사일: **2026-10-20–21 KST**
- 상태: **C2 1차 검증 종료 — 현재 설계 NO-GO, 본격 연구 채택 비추천. C1 보류 유지.**
- 범위: 2024–2026 manipulation·navigation·action-relevant 3D. 공식 NeurIPS·CVPR·ICML·ICLR 및 저자 본문·공개 코드를 우선 확인했다.
- 이전 방향: [종료된 cross-embodiment 검토의 핵심과 결과](../../experiments/vla_rl_cross_embodiment/RESULTS.md)
- 상세 근거: [문헌 비교](./LITERATURE.md) · [후보별 가설·비교·중단 기준](./CANDIDATES.md)
- C1의 최신 판단: [직접 충돌과 축소한 질문](./C1_REVIEW.md) · [진단 계약](./C1_PROTOCOL.md) · [native probe](../../experiments/vla_rl_active_handoff/README.md)
- 실행 결과: [strict load·243 actions 확인, 시간 제한으로 task competence 미확인](../../experiments/vla_rl_active_handoff/RESULTS.md). 성공률 평가와 C1 가설 검증은 수행하지 못했다.
- C2의 최신 판단: [빌드업 최종 결과](./C2_BUILDUP_RESULT.md) · [실제 데이터·Docker 검증](../../experiments/vla_rl_c2_first_pass/RESULTS.md) · [직접 충돌](./C2_REVIEW.md) · [진단 설계](./C2_PROTOCOL.md). 데이터 검사는 수행했으며 정책 효과는 미측정이다.

## 판단

**C1부터 진행했으나, 후속 검토에서 넓은 방법 기여의 가능성은 낮아졌다.** ActiveAlign이 관측–VLA 불일치와 데이터 적응을, EyeRobot 2.0이 gaze sequence RL을 이미 다룬다. 남길 질문은 **고정된 native VLA에서 추가 관측의 순이득이 양수인 상태만 선택할 수 있는가**다. 두 번째 후보는 목표 달성 보상으로 충분히 학습되지 않는 **수행 방식 지시의 조합 일반화**다. 둘 다 연구 가치가 입증된 방법은 아니다.

**C2도 현재 설계의 1차 검증을 NO-GO로 종료했다.** 문헌의 직접 충돌에 더해 실제 데이터에서 완전한 reward·coverage 계약을 확보하지 못했고, 현재 Docker의 reference runtime도 성립하지 않았다. 한 training task의 경유 negative 50개는 확인했지만 RL 이득의 증거는 아니다. 문헌 검토와 실행 전제를 통과한 새 방법은 아직 없다.

| 후보 | 연구 질문 | 가능성이 있는 부분 | 가장 큰 반론 | 현재 판단 |
|---|---|---|---|---|
| **C1. 선택적 관측의 순이득** | 같은 native 시간 예산에서 추가 관측을 언제 생략해야 하는가? | 상태별 순이득의 부호 변화와 배포 가능한 선택의 가치를 검증 | ActiveAlign·EyeRobot 2.0·RESCUE와 강하게 겹치며 native competence도 미확인 | **대규모 후속 실험·RL 구현 보류.** 이번 bounded probe로 투자 판단을 갱신 |
| **C2. 수행 방식까지 따르는 VLA RL** | Pair coverage를 맞춰도 새 object×waypoint×orientation 조합에서 RL 이득이 남는가? | 데이터·reward·최적화의 효과를 구분하는 진단 질문 | 직접 충돌, 완전한 label/coverage 미확보, native runtime 미충족 | **1차 검증 종료·현재 설계 NO-GO.** 정책 효과는 미측정 |

C1은 manipulation과 3D perception을 직접 연결하며, 나중에 navigation의 관측 후 local-controller handoff로 확장할 수 있다. 첫 연구에 manipulation과 navigation을 동시에 넣지는 않는다. C2도 우선 한 로봇의 검증된 native task에서 시작한다. 여러 로봇은 후속 검증 축이며 이전의 RL 전이 질문을 다시 활성화하지 않는다.

## 이미 있는 연구와 새 후보의 경계

- **C1:** 능동 탐색 RL은 [AAWR, NeurIPS 2025](https://papers.neurips.cc/paper_files/paper/2025/hash/aa1b1a959c80086cba61d0fd66de412f-Abstract-Conference.html), action-loss view RL은 [TVVE, CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Bai_Learning_to_See_and_Act_Task-Aware_Virtual_View_Exploration_for_CVPR_2026_paper.html)에 있다. 추가 확인한 [ActiveAlign](https://arxiv.org/html/2610.23378v1)과 [EyeRobot 2.0](https://arxiv.org/html/2610.03710v1)은 venue 미검증 preprint다. 이들의 직접 충돌과 비교 조건은 [후속 검토](./C1_REVIEW.md)에 통합했다. Frozen VLA라는 제한이나 RL을 붙인다는 것만으로 차별화하지 않는다.
- **C2:** Language grounding뿐 아니라 실행 제약·같은 scene의 지시 비교·dependency coverage도 선행 연구가 있다. CounterAlign·RoboFollow·조합 일반화 연구의 CoRL 2026 status와 source 범위는 [C2 후속 검토](./C2_REVIEW.md)에 통합했다. 남길 질문은 동일 coverage·data·label에서 RL 최적화의 추가 가치다.

두 후보의 primary claim은 새 backbone이나 RL 알고리즘이 아니다. 먼저 기존 목적함수·평가가 구분하지 못하는 조건을 입증하고, 기존 strong baseline으로 해결되지 않을 때만 방법을 설계한다. 단순 benchmark 확장이나 평균 성공률 상승만 남으면 top-tier 기여로 부족하다.

## 이번에 우선 후보에서 제외한 방향

| 방향 | 제외·보류 이유 |
|---|---|
| 일반적인 failure detector → retry/reset selector | 기존 RP-2와 겹친다. [RESCUE](https://arxiv.org/abs/2610.13516)는 intervention별 counterfactual outcome과 비용 평가까지 다룬 최신 충돌이다. |
| 오래된 memory를 RL로 갱신·폐기 | 기존 retired RP-3와 같은 문제다. 이번 작업에서 재개하지 않는다. |
| 언어 instruction을 RL로 다시 써서 frozen VLA 개선 | [VLA Grounder](https://arxiv.org/abs/2607.04517)와 직접 충돌한다. |
| 일반적인 continual VLA RL / forgetting 방지 | [Simple Recipe Works](https://arxiv.org/abs/2603.11653)가 sequential LoRA + on-policy RL을 강한 baseline으로 제시한다. Forgetting을 먼저 입증하지 않고 새 모듈부터 제안할 근거가 없다. |
| Success와 safety를 함께 평가하고 constrained RL 적용 | [SafeVLA, NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e185c7be603426028c32ae1003a59d78-Abstract-Conference.html) 및 여러 새 safety benchmark와 겹친다. Safety를 고려한다는 것만으로 C2를 차별화하지 않는다. |
| Adaptive chunk·slow/fast 실행·일반 지연 보정 | 이전 문헌 검토에서 넓은 신규성 주장이 성립하지 않았다. [이전 결과 요약](../../experiments/vla_rl_cross_embodiment/RESULTS.md) 참조. |

## 문헌 검토 완료 범위와 남은 판단

- [x] 이전 방향의 핵심 결과 보존과 전용 실행 자산 정리.
- [x] 기존 registry와 retired project의 범위를 확인하고 새 검색 수행.
- [x] 직접 충돌 논문의 본문 관련 절·공식 venue·일부 코드 interface 확인.
- [x] 두 후보의 반증 가능 가설, 대안 설명, baseline, 지표, 중단 기준 작성.
- [x] C1 추가 직접 충돌 4편의 관련 본문과 공개 interface 확인.
- [x] Native SmolVLA checkpoint·LIBERO revision·입출력·bounded probe 예산 고정.
- [x] Docker bounded probe 실행과 결과·자원 비용 기록, 전용 실행 자원 정리.
- [x] 과거 시각 관측을 기억한다는 가정을 제거하고, 시간·자세·policy support confound와 반증 기준 작성.
- [x] C2의 추가 직접 충돌·공식 status 및 20개 공개 파일의 관련 부분 정적 감사.
- [x] 실제 task 8개와 공개 dataset 파일 목록 확인, atomic/pair coverage를 갖는 4/4 split 초안 검증.
- [x] C2 G0 감사 수행: 400개 metadata·training instruction 200개·payload 12쌍·경유 trace 50개 확인. 완전한 계약은 미충족.
- [x] C2 G1 reference 경로 검사: ARM64 의존성·GPU 할당 실패와 checkpoint 미식별 기록.
- [x] C2 연구 투자 판단: 현재 설계 NO-GO로 종료. G2–G4는 미실행이며 재개 조건 없이는 진행하지 않음.
- [ ] C1 empirical precondition과 물리 primitive 확인: 현재 보류.
- [ ] 전문가 피드백 및 독립 재현.

현재 **C1은 보류, C2는 현재 설계의 채택 심사를 종료**했다. 두 후보 모두 top-tier 방법 기여로 채택할 근거는 부족하다. 데이터 검사와 정책 효과 검증을 구분한다.

## 다음 순서

1. **C2에 추가 학습·환경 이식 작업을 배정하지 않는다.** [재개 조건](./C2_BUILDUP_RESULT.md)을 만족할 새로운 데이터·실행 근거가 있을 때만 최소 진단을 다시 검토한다.
2. C1은 [native probe](../../experiments/vla_rl_active_handoff/README.md)의 결과와 [진단 계약](./C1_PROTOCOL.md)을 보존한다. 공개 평가 recipe와 base competence, 관측에 특유한 새로운 설명이 확보되기 전에는 큰 rollout sweep으로 확대하지 않는다.
3. C1을 재개할 근거가 생긴 경우에만 G0 competence → 물리 primitive 고정 → 동일 budget의 immediate/look/wait/heuristic 비교로 진행한다. One-step predictor·표준 RL·aligned adaptation으로 충분하면 새 방법 구현을 중단한다.

재개할 경우 후보별 전용 Docker 공간으로 분리한다. C2의 데이터 검사·의존성 probe 결과와 정리 내역은 [실행 기록](../../experiments/vla_rl_c2_first_pass/RESULTS.md)에 보존한다. Registry admission·tier·사용자 정독 상태는 변경하지 않았다.
