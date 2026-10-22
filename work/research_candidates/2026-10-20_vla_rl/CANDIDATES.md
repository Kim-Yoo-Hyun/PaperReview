# 후보별 가설, 최소 비교, 중단 기준

- Updated: 2026-10-21 KST / **초기 제안의 후속 판정 — C1 보류, C2 1차 검증 종료·현재 설계 NO-GO**
- [판단](./README.md) · [선행 연구의 근거와 확인 범위](./LITERATURE.md)
- 아래 수량·margin은 설계 예시다. 구현 전 checkpoint·task·cost unit·split과 함께 고정해야 한다. 실행 manifest가 생성된 것으로 간주하지 않는다.
- C1의 현재 판단과 구체적 계약은 [C1_REVIEW.md](./C1_REVIEW.md), [C1_PROTOCOL.md](./C1_PROTOCOL.md)가 우선한다. 아래의 넓은 옵션·history·가림 설정은 모두 구현한 계약이 아니다.

## C1. 관측의 개선을 실제 조작 이득으로 연결하는 RL

### 질문과 기대 지식

**고정된 VLA가 조작할 때, 지금 실행하는 것보다 관측을 한 번 더 얻는 편이 유리한 조건을 학습할 수 있는가? 그 판단에 다단계 return이 필요한가, 아니면 visibility·pose confidence·one-step outcome prediction으로 충분한가?**

예를 들어 대상은 정면에서 잘 보이지만 손잡이의 깊이가 불명확할 수 있다. 반대로 옆으로 더 이동하면 가림은 줄어도 접근 경로가 나빠지거나 주어진 시간이 소진될 수 있다. 이 예는 아직 측정한 현상이 아니다.

기대하는 지식은 어떤 observation proxy가 어떤 조건에서 실제 조작 가능성을 잘못 순위화하는지, 그 오차가 정책 선택과 성공률에 미치는 영향이다. Value of information, POMDP, RL handoff 자체를 새 개념으로 주장하지 않는다.

### 선행 연구에서 출발하는 지점

AAWR는 search policy와 π0 handoff, TVVE는 action-loss 기반 virtual-view RL, SaPaVe는 coordinated camera/manipulation을 제공한다. 따라서 제안의 구분점은 **물리적 관측 비용과 downstream competence를 고정한 뒤, 추가 관측·즉시 실행의 장기 outcome을 비교**하는 것이다. 기존 논문 전체에 이 비교가 없다고 단정하지 않는다. [P1–P6 문헌 비교](./LITERATURE.md).

후속 확인에서 ActiveAlign·EyeRobot 2.0·EgoReveal·PhysCaP와의 충돌이 추가되었다. 위의 구분점 자체가 새 기여라는 해석은 철회한다. 현재는 선택적 관측의 순이득을 확인하는 조건부 진단으로 좁혔다. [확인 범위와 판정](./C1_REVIEW.md).

### 가장 작은 문제 설정

| 항목 | 후보 단계의 계약 |
|---|---|
| 시작 범위 | 단일 로봇, 기존 checkpoint의 native manipulation task 2종. 하나는 grasp, 하나는 handle/placement geometry가 필요한 task를 검토 |
| 고정 부분 | VLA backbone와 native action head, controller, action horizon, image preprocessing, instruction |
| 학습 가능한 부분 | `execute now / look left / look right / look closer`의 작은 supervisor. 이동 primitive는 실제 camera 또는 arm motion으로 실행 |
| 관측 | Native scene/wrist RGB, proprio, instruction, 남은 비용. Supervisor의 history는 별도 설계 대상이며 SmolVLA 자체에 과거 visual memory가 있다고 가정하지 않음. Native 입력에 없는 depth·camera pose를 무료로 추가하지 않음 |
| 결정 시점 | 관측 primitive 종료 시점. 실행 option은 같은 고정 VLA로 handoff하며 native episode budget 유지 |
| 주요 변동 | 가림 정도 × depth/part ambiguity × sensing cost. 초기 관측의 visibility와 접근 가능성을 가능한 범위에서 교차 배치 |
| Cost | Simulator control ticks를 primary unit으로 사용. 실제 wall time·query 수·camera 이동량은 별도 보고. 이미지 한 장 생성과 실제 이동을 같은 무료 행동으로 처리하지 않음 |

독립 pan/tilt camera가 없다면 wrist camera 이동은 arm pose도 바꾼다. 이 경우 **(a) 물리 sensing의 총효과**와 **(b) 같은 arm state에서 관측만 교체하는 진단**을 분리한다. 후자는 정보 효과의 진단일 뿐 배포 가능한 센서 이동 성과가 아니다. Virtual rendering은 이미 관측한 point cloud에서만 허용하며 가려진 simulator geometry를 무료로 제공하지 않는다.

### 먼저 틀렸다고 확인할 가설

1. **H0, base competence:** 필요한 정보가 제공된 상태에서 native base가 해당 task를 수행한다. 실패하면 sensing 연구를 시작할 수 없다.
2. **H1, ranking gap:** 비슷한 visibility/confidence의 관측이라도 남은 budget 아래 실제 성공 기대값이 다르고, 그 차이가 단순 접근 거리로 모두 설명되지 않는다.
3. **H2, sequential value:** 두 번 이상 관측하는 순서·종료 결정이 유용하며 one-step selector보다 나은 선택이 존재한다.
4. **H3, learnability:** 그 선택을 현재 허용된 history로 예측할 수 있다. Privileged state만 알아야 가능한 oracle 차이는 deployable gap이 아니다.

### 최소 진단과 비교

먼저 두 task의 소규모 development 초기 상태 20–30개에서 **즉시 실행 / 고정 관측 1회 / 두 관측 순서**를 같은 시작점에서 비교한다. 각 분기에서 VLA 내부 history·RNG·controller state도 복원해야 한다. Stochastic policy에서는 state마다 복수 rollout이 필요하며 한 번의 best branch를 true oracle로 부르지 않는다. Final test는 이 진단에 재사용하지 않는다.

| Baseline | 배제할 대안 설명 |
|---|---|
| 즉시 실행, fixed one-look, fixed scan | 관측을 늘리기만 하면 충분 |
| Detector 연속 검출 handoff / confidence threshold | AAWR식 종료 규칙으로 충분 |
| Visibility·entropy / action-loss proxy | 시각 또는 supervised action proxy로 충분. TVVE를 동일 interface로 이식하지 못하면 `style adaptation`으로 표기 |
| Outcome classifier + contextual bandit | TD·다단계 RL 없이도 충분 |
| 같은 경험의 BC·return-weighted supervisor | 행동 복제 또는 경험 선택만으로 충분 |
| 기존 RL algorithm에 task-success minus sensing-cost reward | 새 estimator·architecture 없이 표준 RL로 충분 |
| Privileged branch sweep | 가능한 개선 여지의 진단용 상한. 학습·평가 비용을 별도 기록 |

조건부 method 후보는 history-conditioned option value와 실행 option의 termination을 함께 학습하는 형태다. **이는 기존 option RL의 적용안이며 아직 알고리즘 기여가 아니다.** Standard task-cost RL보다 추가로 필요한 요소가 관찰되지 않으면 새 method 이름을 붙이지 않는다.

모든 learned selector는 동일 interaction/data budget, sensing primitive, VLA 호출 예산과 capacity 범위에서 비교한다. Oracle branch labels를 제안법에만 더 주지 않는다. 데이터 지원에 없는 관측 순서를 offline RL이 알아낼 수 있다고 가정하지 않는다.

### 지표·일반화·중단

- Primary: **정해진 total cost 안의 task success**. Success–cost curve와 paired 차이의 CI를 함께 보고한다.
- Secondary: sensor-motion cost, unnecessary look, premature handoff, task-outcome ranking error, observation shift별 worst-group success.
- Split: 초기 장면뿐 아니라 occluder geometry 또는 sensing-cost 구간을 hold out. Policy training seed와 evaluation seed를 구별한다.
- 새 method를 주장하려면 적어도 다른 task/occlusion family에서 이득이 유지되어야 한다. 한 robot에서 먼저 확인하고 navigation·cross-body는 확장으로 분리한다.

| 관찰 | 판단 |
|---|---|
| Full-information native base도 부진 | 후보 task/base 제외. 새 head bootstrap으로 되돌아가지 않음 |
| Visibility/confidence와 outcome 순위가 충분히 일치 | C1의 핵심 gap 기각 |
| Primitive마다 같은 순위이며 fixed scan이 최선 | Adaptive/RL selector 기각 |
| One-step outcome model과 동률 | Sequential RL 필요성 기각; supervised decision 문제로 축소 |
| 관측만 교체한 진단에서는 효과가 없고 arm pose 이동만 효과 | Perception claim 제거, approach/control 문제로 재정의 |
| Task-cost standard RL만으로 해결 | 새 알고리즘 claim 제거. 비교 결과의 일반성이 충분한 경우에만 empirical study 검토 |
| 동일한 physical handoff·cost·proxy comparison을 다룬 후속 연구 발견 | 방법 구현 전 novelty 재판정 |

**수정한 가능성:** 넓은 신규성은 직접 충돌로 약해졌다. Native base와 물리적 관측 후 continuation이 성립하고 상태별 선택 가치가 남을 때만 후속 연구를 정당화할 수 있다. [Native probe](../../experiments/vla_rl_active_handoff/README.md)는 이 중 실행 전제만 확인한다.

## C2. 목표 달성과 수행 방식 준수를 함께 일반화하는 VLA RL

**2026-10-21 갱신:** [C2_REVIEW.md](./C2_REVIEW.md)에서 직접 충돌 검토를 진행했다. ExecVLA·RoboFollow·조합 일반화의 dependency-coverage 연구까지 확인하여 **넓은 방법 제안은 보류**했다. CounterAlign의 CoRL 2026 Poster status도 공식 API로 갱신했다.

남길 질문은 **atomic/pair coverage와 동일 데이터·label 예산을 맞춘 뒤에도 complete-reward RL이 balanced SFT와 return-weighted imitation보다 새로운 object×waypoint×orientation triple에서 유리한가**다. RL 효과·연구 신규성은 미입증이다.

- [평가·데이터 감사](./C2_DATA_AUDIT.md): SIMPLER-IN의 조건 변경은 Path의 physics도 변경한다. RoboFollow의 native Scene 3 task와 L2 rewrite를 C2의 holdout과 구분했다.
- [8개 실제 task의 4/4 분할](./C2_SPLIT_DRAFT.json): 모든 atomic/pair 조합을 training에 포함하면서 새로운 triple을 남기는 정적 초안이다. Episode-level split·feasibility·runtime은 미검증이다.
- [진단 설계](./C2_PROTOCOL.md): Primary `P(goal∧all constraints)`, 입력 경계, matched baselines, support·reward·optimization 구별, 반증 기준의 현재 canonical 문서다.

후속 [G0·G1 검사](../../experiments/vla_rl_c2_first_pass/RESULTS.md)를 수행했고 현재 설계의 **1차 검증은 NO-GO로 종료**했다. 부분 경유 label은 확인했으나 전체 조합의 goal/orientation·coverage 및 reference runtime이 성립하지 않았다. [빌드업 최종 판단](./C2_BUILDUP_RESULT.md)이 현재 canonical 결론이다. RL의 상대 성능은 측정하지 않았고 C2가 C1보다 더 유망하다고 입증된 것은 아니다.

## 자원·실행 판단

현재 컴퓨터는 Apple M4·16 GiB, Docker VM은 Linux ARM64·약 7.65 GiB다. C1의 bounded CPU probe는 [별도 실행 기록](../../experiments/vla_rl_active_handoff/README.md)으로 관리한다. C2는 Docker에서 데이터 감사와 의존성/GPU probe를 수행했으며 native 정책·simulator 실행에는 진입하지 않았다. 작은 supervisor를 쓴다고 VLA inference 비용이 사라지지 않으며, 이전 frozen-feature 실험을 새 후보의 runtime 증거로 사용하지 않는다.

Native base가 성립하지 않는 경우 toy head를 다시 만드는 경로를 채택하지 않는다. 모든 모델·환경 실행은 Docker로 제한하고, native 실행과 연구 효과의 검증을 구분한다.
