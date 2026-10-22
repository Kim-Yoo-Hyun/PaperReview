# D1: 관측 불일치의 원인을 구분하는 VLA

> 이 문서는 최초 제안 기록이다. 후속 [D1 buildup 결과](../2026-10-21_d1_buildup/README.md)가 현재 판정이다: REVISE / 본격 학습 HOLD. 외부 논문 등록과 최신 version 정정은 [closest-work](../2026-10-21_d1_buildup/CLOSEST_WORK.md)를 따른다. 아래 미실행 계획을 완료 실험으로 해석하지 않는다.

- 작성: 2026-10-21 KST
- 상태: **조건부 buildup 후보 / CURATION-HYPOTHESIS**. 아래는 제안한 검증이며 실험 결과가 아니다.
- [방향 비교](./README.md) · [문헌과 source 범위](./LITERATURE.md)

## 1. 남길 질문

**RGB와 proprioception이 서로 맞지 않을 때, VLA는 실제 로봇 상태 변화·관측 오류·실행 오류를 구분하여 올바른 행동을 유지할 수 있는가? 어떤 관측 조건에서는 그 구분이 불가능한가?**

핵심은 고장 감지 정확도를 높이는 데 그치지 않는다. 같은 크기의 apparent error라도 원인에 따라 보정해야 할 것이 다르다. 카메라 좌표계만 바뀐 경우, policy에 전달하는 state만 잘못된 경우, controller의 실제 실행이 달라진 경우를 섞으면 잘못된 보정이 실제 물체를 움직일 수 있다.

첫 목표는 한 로봇에서 현상과 원인 식별의 필요성을 보이는 것이다. 두 번째 embodiment는 동일한 representation·규칙의 재사용 가능성을 평가하는 후속 단계다. 처음부터 모든 로봇의 zero-shot adaptation을 주장하지 않는다.

## 2. 가장 가까운 연구와 실제 차이

| 선행연구 / 확인한 본문 | 이미 해결하거나 시험한 것 | D1에서 추가로 확인할 조건 |
|---|---|---|
| [How Should VLAs Use Proprioceptive State? §4–5](https://arxiv.org/html/2608.03052v1) | state의 표현·history 길이·입력 위치를 통제하여 비교. state에는 world-frame base pose도 포함됨 | interface 순위가 아니라 잘못된 state와 잘못된 vision의 원인 구별. 원 논문을 순수 joint feedback 실험으로 오독하지 않음 |
| [Self-Adaptive VLA §III-A, IV](https://arxiv.org/html/2609.30092v1) | actuation bias와 encoder offset을 구분하여 모델링. offset은 시행 간 고정. 이전 rollout context로 적응하며 시각적 식별 필요성도 설명 | episode 중 원인 전환과 알려주지 않은 sensor corruption. 고정 offset·history 적응 자체는 새 기여에서 제외 |
| [CoRE-VLA §3.1](https://arxiv.org/html/2607.03693v1) | depth availability indicator와 modality dropout으로 expert를 선택 | availability flag는 정상인데 값이 잘못된 경우. fault label을 입력하면 이 차이는 사라짐 |
| [ReViP §3, §4.1](https://arxiv.org/html/2601.16667v1) | object drop·swap·relayout에서 visual task-stage cue로 state-driven false completion 완화 | visual evidence 자체가 잘못된 조건도 포함. 항상 vision을 더 믿는 설명과 구별 |
| [LIBERO-RIG §2–4, Appendix G](https://arxiv.org/html/2610.18843v1) | hardware/setup 11축, 한 embodiment·episode당 한 축. policy state corruption과 controller state corruption을 구분 | unknown source와 onset/전환을 조건으로 제한. 단순 복합 corruption benchmark 추가는 기여로 충분하지 않음 |

이 차이들은 해당 조건의 신규성이 확정되었다는 뜻이 아니다. Robust state estimation, fault detection/isolation, adaptive control의 기존 방법과도 비교해야 한다. 이 분야의 고전 원리를 VLA에 붙이는 것만으로 새 algorithm을 주장하지 않는다.

## 3. 우선 확인할 관측 가능성

| 조건 | 허용 관측 | 먼저 확인할 것 |
|---|---|---|
| scene camera가 이동, controller와 encoder는 정상 | RGB, state, 이전 command, timestamp | 여러 link/고정 배경 또는 wrist view가 camera 변화와 물체 변화를 구분할 단서를 주는가? |
| policy 입력 state만 offset, 실제 controller는 정상 | 같은 관측 | visual arm pose와 command–state 관계로 state 오류를 식별할 수 있는가? |
| actuation bias, encoder는 실제 움직임을 보고 | 같은 관측 | command와 실제 변화의 residual이 관측 오류와 구별되는가? |
| 실제 물체가 이동, sensors는 정상 | 같은 관측 | 정상적인 재계획을 sensor fault로 오인하지 않는가? |
| 시각적으로 arm이 가려지고 state와 실행이 함께 offset | 같은 관측 | 두 원인이 같은 observation history를 만들면 보정을 유일하게 결정할 수 없음. 이 경우를 오류 없이 판정하거나 scope에서 분리할 수 있는가? |

위의 “구별 가능” 여부는 가설이다. 물리적으로 일관된 render·kinematics·controller 개입을 정의한 뒤 확인해야 한다. 모든 조건에 식별 가능성이 있다고 가정하지 않는다. 같은 observable history에 서로 반대의 정답 action을 붙여 모델을 평가하지 않는다. 현재 이 표를 구현한 simulator fixture나 manifest는 없다.

## 4. 경쟁 설명과 가장 작은 진단

1. **H0 — 센서를 실제로 쓰지 않는다.** 특정 checkpoint가 state를 무시하면 state corruption 효과가 없는 것은 성공적인 reliability 판단이 아니다. Clean condition에서 state/history의 개입이 action과 outcome에 주는 영향을 먼저 본다. Repeated-current, shuffled history, observation mask는 진단용이며 retraining 없이 OOD 입력을 넣은 결과를 곧바로 인과 효과로 일반화하지 않는다.
2. **H1 — 고정된 모달리티 편향만 문제다.** Always-vision, always-state, fixed fusion이 모든 식별 가능한 조건에서 충분하면 adaptive estimator가 필요하지 않다. State-only baseline에는 시각적 goal 정보가 없으므로 동등한 generalist baseline으로 순위를 매기지 않고 진단 control로만 쓴다.
3. **H2 — calibration 또는 controller 문제다.** Kinematic reprojection residual과 일반적인 state estimator로 오류가 해결되면 VLA 내부 신뢰도 module은 불필요하다. Controller corruption의 피해를 policy perception 실패로 보고하지 않는다.
4. **H3 — history나 data augmentation이면 충분하다.** 같은 history 길이·training data·parameter/compute 예산의 adapter 및 corruption augmentation을 비교한다. Self-Adaptive 계열도 고정 offset 조건부터 공정하게 맞춘다.
5. **H4 — 원인을 조건으로 하는 상태 표현이 추가로 필요하다.** 위 비교 후 남은 개선이 held-out onset·fault type·task 조합에서 유지되고 clean 행동을 해치지 않는지 본다. 이것만이 제안 method를 발전시킬 근거다.

사전 진단 단위는 language로 목표가 바뀌는 **reaching/placement와 articulated interaction의 두 task family**다. 구체적인 task ID는 native checkpoint 지원과 clean competence 확인 후 고정한다. 환경을 이식하거나 새 training을 먼저 하지 않는다. 단순 픽셀 노이즈보다 원인을 분리할 물리 개입을 우선한다.

## 5. Policy interface와 누출 방지

초기 policy-visible input은 원 모델이 지원하는 RGB views, language, proprioception, 시간순 command/observation history다. 실험에서 fault type, true state, corruption magnitude, onset time은 evaluator만 보관한다. Timestamp가 원래 제공되지 않으면 모든 비교군에 동일한 추가 입력으로 명시한다. 미래 관측은 사용하지 않는다.

후보 구현이 필요해질 때 검토할 구조는 `history → state consistency / uncertainty estimate → VLA action conditioning`이다. Ground-truth fault classifier를 policy에 붙인 것은 **oracle diagnostic**일 뿐 제안 method가 아니다. Metadata availability mask를 쓰는 CoRE-VLA와 hidden fault 추론을 비교할 때도 정보 예산을 분리한다.

기하학 baseline에 robot kinematics나 camera calibration을 주면 제안 방법에도 같은 정보를 허용하거나, 추가 정보가 있는 comparator라고 명시한다. Intrinsic/extrinsic·action unit·absolute/delta action·controller gain·control period를 고정하지 않은 비교는 해석하지 않는다.

## 6. 측정과 중단 기준

| 측정 | 목적 |
|---|---|
| clean / fault / restored 조건별 task success | clean 능력 보존과 복구를 따로 확인 |
| 오류 원인별 잘못된 보정 action, 충돌·joint/force 제한 위반 | 단순 성공률 평균이 숨기는 해로운 적응 확인 |
| fault onset 이후 원인 판정과 행동 안정화까지의 시간 | latency를 실제 control period로 환산 |
| 관측 가능/불가능 조건별 결과 | 숨겨진 정보로만 풀리는 설정을 분리 |
| instruction 교환과 같은 물리 상태의 다른 목표 | VLA에서 언어가 실제 행동을 바꾸는지 확인 |
| matched data·history·inference cost | 모델 용량이나 추가 관측만으로 설명되는 효과 배제 |

다음은 **제안한 운영 기준**이며 문헌에서 관측된 수치가 아니다. Pilot 전 task·seed·severity·예산과 함께 확정한다.

- Clean competence가 충분하지 않거나 원 checkpoint가 필요한 state를 사용하지 않으면 후보 환경을 바꾸거나 보류한다. Native qualification을 건너뛰지 않는다.
- 같은 checkpoint의 oracle correction에도 회복 여지가 거의 없으면 해당 intervention을 제외한다. Retrained model의 점수와 frozen oracle의 점수는 같은 상한으로 해석하지 않는다.
- 가용 정보로 원인을 구분할 수 없다면 추가 센서·가정을 명시하거나 범위를 축소한다. Learned gate로 해결된다고 주장하지 않는다.
- Classical estimator + 원래 VLA 또는 단순 augmentation이 held-out 조건까지 해결하면 신규 method를 중단한다. 확인한 조건과 단순 해결책은 연구 기록으로 남긴다.
- 방법 비교를 할 경우 실용적 최소 효과 크기를 pilot 후 test를 보기 전에 고정한다. 예시 초안은 가장 강한 matched baseline 대비 성공률 +5 percentage points와 clean 감소 2 points 이내다. 이는 채택 판정 자체가 아니며 task-clustered uncertainty와 안전 위반을 함께 확인한다.
- 복잡한 구조의 이득이 특정 task/고장 한 종류에만 남으면 cross-embodiment/general VLA claim을 하지 않는다.

## 7. 본격 연구로 발전할 가치

**문제의 가치는 높고, 새 방법의 가치는 아직 조건부다.** 로봇별 sensor setup 차이와 배포 오류는 사용자의 다양한 로봇 목표에 직접 연결된다. 3D vision도 단순 부가 feature가 아니라 상태 일관성을 검증할 도구가 된다. 반면 일반 sensor fusion·fault isolation·hardware adaptation은 오래된 연구 문제이고 최신 VLA 문헌도 빠르게 접근하고 있다.

설득력 있는 결과는 (a) 기존 입력·제어 조건 때문에 생기는 특정 실패를 재현하고, (b) 관측 가능한 조건과 불가능한 조건을 분리하며, (c) 단순 baseline을 넘는 추가 정보 처리의 필요성을 보여주는 것이다. 새로운 architecture 이름, 몇 가지 corruption에서의 평균 개선, arXiv 최신 논문과 다른 구현만으로는 부족하다.

지금 결정은 **더 검토할 가치가 있으므로 D1의 문헌·artifact gate부터 진행**이다. 공개 code/weights/data 검증, manifest 생성, Docker runtime, 정책 실험은 아직 수행하지 않았다. Full-text 일부를 확인한 사실을 사용자 reading status나 EXPERIMENT-SUPPORTED로 승격하지 않는다.
