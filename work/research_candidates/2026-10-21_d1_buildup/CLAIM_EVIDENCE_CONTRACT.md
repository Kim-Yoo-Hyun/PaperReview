# D1-L2 — 보정의 필요성을 판별하는 주장·증거 계약

- 후속 판정: [N1–N4 재심사](./NONEXPERIMENTAL_REVIEW.md)가 full-history의 공통 선택·정보 가치·reference 오차 조건을 확장했다. 현재 method NO-GO·진단 HOLD이며 아래 REVISE와 다음 실험 문구는 L2 당시 이력이다.
- 작성: 2026-10-22 KST. [기존 8단계 가이드](../../../research/IDEA_BUILDUP_GUIDE.md)의 3–6단계와 내부 반박을 보강한다.
- 입력: [직접 방법 감사](./BASELINE_METHOD_AUDIT.md), [baseline dossier](./BASELINE_DOSSIER.md), [기존 합성 반례](./RESULTS.md).
- 판정: **문헌·분석 계약 작성 완료 / 실제 VLA 가설 미검증 / 신규 방법 REVISE**.
- 아래 수식은 명시한 가정 아래의 **연구자 도출**이다. 논문의 실험 결과, 새로운 실행 결과, 모든 로봇에 성립하는 정리가 아니다.
- D1-L3 후속: [task·value-path 감사](./TASK_OBSERVABILITY_AUDIT.md)에서 `pi05_libero`의 state-value 경로 부재를 확인하여 primary를 OFT 후보로 변경했다. 아래 특수 수식을 실제 LIBERO의 absolute-orientation 과제로 구현했다는 증거는 확보하지 못했다.

## 1. 이번에 남기는 질문

**같은 관측·calibration·계산 예산에서, task에 필요한 정보를 보존하는 보정이 일반 복원·causal recalibration보다 필요한 조건이 실제 native VLA에 존재하는가?**

이 질문은 sensor/physical cause를 반드시 분류해야 한다는 주장을 포함하지 않는다. 원인 label 없이 좋은 행동을 고를 수 있다면 그것이 더 강한 단순 대안이다. RL의 필요성도 가정하지 않는다. 기존 방법의 적용 범위를 설명하는 결과가 남을 수 있지만 현재 독립적인 top-tier 기여라고 판정할 근거는 부족하다.

## 2. 수식으로 먼저 제거할 약한 주장

### A. 고정 회전 bias에서는 원인 분류 없이도 충분할 수 있다

실제 orientation을 `R(t) ∈ SO(3)`, report를 `P(t)=B R(t)`로 두자. `B`는 episode 내 고정된 left-multiplicative sensor bias이고, 초기 report는 `P(0)=B R(0)`다. G-PSMR의 보정 연산을 이 표기로 `C P(0)⁻¹ P(t)`라 쓰면:

```text
C P(0)⁻¹ P(t)
= C [B R(0)]⁻¹ B R(t)
= C R(0)⁻¹ R(t).

C = R(0) 이면 결과는 R(t).
```

가정은 정확한 reference, gate ON, orientation만의 오류, 일정한 B, 일관된 frame·rotation conversion, 측정 noise가 없는 경우다. 실제 suite 평균 reference가 각 episode의 참 초기 orientation과 같다고 보장하지 않는다. Gate가 닫히거나 bias가 시간에 따라 바뀌면 이 도출을 적용할 수 없다. Translation·actuator 오류도 해결했다고 볼 수 없다.

**결정:** 이 조건에서 fault cause classifier를 붙여 회복해도 새 메커니즘의 증거가 약하다. Reference mismatch와 시간 변화는 다음 검토 대상으로 남기되, “더 복잡한 오류”만으로 연구 가치를 주장하지 않는다. 연산의 출처는 [G-PSMR §3.5](https://www.mdpi.com/1099-4300/28/9/975)이며 위 특수 경우의 전개는 이 문서의 해석이다.

### B. 물리적 회전의 canonicalization이 항상 해로운 것은 아니다

실제 trajectory 자체가 `P(t)=B R_nom(t)`인 경우에도 위 연산은 state channel에서 B를 제거할 수 있다. 그렇다고 전체 VLA가 필요한 정보를 반드시 잃었다고 결론낼 수 없다. RGB에 변화가 남을 수 있고 task가 상대 좌표에만 의존할 수도 있기 때문이다.

**필요한 분리:**

- Task가 B에 대해 invariant하면 동일 보정이 유익할 수도 있다.
- Absolute orientation/frame이 성공 조건에 중요하면 해당 정보 보존이 필요할 수 있다.
- Full RGB·state·language·history에서 구별 가능한지를 검사해야 한다. State 한 채널의 alias는 전체 policy input의 비식별성을 뜻하지 않는다.
- 같은 visible history에서 최적 행동도 같다면 원인 구별 실패를 task 실패로 세지 않는다. 행동이 달라도 식별 불가능하면 강제 cause classification보다 보류·보수적 행동의 utility를 평가한다.

**결정:** 후속 D1-L3에서 task goal/predicate·frame을 읽었다. 40개 task에 절대 EEF orientation을 직접 요구하는 goal은 없었으며 실제 LIBERO가 이 반례를 구현한다고 선언하지 않는다. Task utility 기반의 더 좁은 대조로 수정한다.

### C. Episode 중간 fault에서 초기 gate를 이기는 것만으로는 부족하다

초기 gate가 닫혔고 이후 report 오류가 생기는 경우, episode-fixed M2 gate는 계속 닫혀 있으므로 state 보정은 identity다. 동일한 native 입력·난수·실행 조건의 M2-only 경로라면 이후 fault를 새로 판정하지 않는다. 이것은 operator 수준의 결론이지 rollout 결과가 아니다. Joint M3의 visual gate는 별도로 반응할 수 있다.

**결정:** 원논문 M2 외에 prefix-only residual/change-point와 reference 갱신 대조군을 추가해야 한다. 정답 onset·fault type·미래 clean state를 reset 신호로 쓰지 않는다. 일반 재보정만으로 충분하면 동적 gate를 새 VLA 방법의 기여로 주장하지 않는다.

### D. 결합 방법의 효과를 독립적인 두 모듈로 해석하지 않는다

State 보정 뒤 계산하는 visual disagreement는 보정 전과 달라질 수 있다. 따라서 M3가 좋아져도 “원인을 정확히 분리했다”는 설명이 자동으로 성립하지 않는다.

**결정:** B0/M1/M2/M3를 같은 reset과 augmentation 난수 schedule로 묶고, query 수와 지연을 보고한다. 동일한 random seed 문자열만으로 호출 수가 다른 경로의 난수를 맞췄다고 가정하지 않는다. 독립된 named RNG stream·query index를 사용할지는 실제 run manifest에서 고정한다.

## 3. 강화할 단순 대안 — 아직 구현하지 않음

| 대조 | 배제할 설명 | 공정성·제약 |
|---|---|---|
| B3-causal: residual/change-point + 보수적 reference 갱신 | 초기 고정 gate의 시점 한계만 고친 효과 | 관측 prefix만 사용. 실제 vision pose estimator의 오차·비용 포함; oracle onset 금지 |
| B3-task: task-conditioned clean reference | Suite 평균이 task별 정상 자세를 뭉갠 효과 | 이미 policy에 주어지는 instruction/task 정보만 사용. 같은 clean calibration pool을 모든 방법에 제공; holdout/test outcome으로 reference 선택 금지 |
| B5 원형 M1/M2/M3와 명시적 online 변형 | Stream 복원·추가 query만으로 충분 | 원형 재현과 D1 확장 구별. Calibration·augmentation·timing 비용 정렬 |
| B4 일반 fine-tune / constant scaling / GAP-style | 단순 optimization 또는 학습량의 효과 | 공식 수식과 공개 rule 차이는 [방법 감사](./BASELINE_METHOD_AUDIT.md)에 따라 version 명시; 동일 data/update budget |
| 기존 B1/B2/B6 | State shortcut·history·corruption exposure | [Dossier](./BASELINE_DOSSIER.md)의 정보·capacity·split 조건 유지 |

B3-causal/B3-task는 연구자 설계한 대조군이다. 기존 구현이나 검증된 결과를 확보했다는 뜻이 아니다. Task-conditioned reference 자체를 제안 방법의 신규성으로 주장하지 않는다. Held-out task에서 label만 보고 reference를 얻을 수 없다면 미지 task fallback 또는 동일 허용 calibration을 명시한다.

## 4. 주장–증거–기각 연결

| ID / 잠정 주장 | 필요한 최소 증거 | 반대 설명 또는 반례 | 결정 규칙 |
|---|---|---|---|
| C0. 연구할 state/goal 사용이 있다 | Native clean competence, policy-valid state/goal intervention, closed-loop utility | Mask OOD 또는 normalization clipping | State/goal이 유용하지 않으면 해당 checkpoint·task에서 D1 중단/범위 축소 |
| C1. 보정 선택의 task상 차이가 있다 | 실제 goal/predicate·frame에서 paired intervention, harmful/recovered pairs | Goal-invariant 변환, 단순 observation artifact | 두 선택의 task utility 차이가 없으면 cause-conditioned 필요성 기각 |
| C2. 차이를 prefix에서 알 수 있다 | 모든 비교군이 보는 view/history/calibration로 구별 가능한 cue | GT frame·fault label·미래 정보 누출 | 불가능한 stratum은 정확한 cause 판별 claim에서 제외; utility 문제로 수정 |
| C3. 단순 대안 이후에도 개선 여지가 있다 | Qualified B0/B3/B5와 diagnostic headroom; 필요 시 B1/B2/B4/B6 | Online recalibration·task reference·학습량만으로 충분 | 강한 단순 대안이 gap을 없애면 새 learned method NO-GO |
| C4. Task 정보를 보존한 것이 개선 원인이다 | 같은 입력/예산에서 task cue 제거·바꿈, correction-only 및 history 대조 | 추가 VLM·query·calibration 이득 | 예산·정보 통제 후 사라지면 mechanism claim 기각 |
| C5. 재사용할 적용 경계가 있다 | Held-out task·초기 상태·fault onset/magnitude에서 재현 | 한 checkpoint/특정 threshold tuning | Pilot 수치만 있으면 사례 보고로 제한; 광범위 일반화 주장 보류 |

현재 C0–C5의 실제 VLA evidence는 모두 미확보다. A–D는 불필요한 주장과 약한 비교를 제거한 분석이며 C1–C5가 참이라는 증거가 아니다. 외부 연구자 피드백도 아직 없다.

## 5. 평가 단위와 보류한 숫자

Primary 비교는 task/초기 상태/seed를 pair로 묶는다. Correction의 이득은 성공률 차이와 recovered pairs, 손해는 baseline-success→correction-failure pairs를 함께 보고한다. Physical-change 조건에서의 harmful correction은 baseline이 성공한 pair에 대한 조건부 비율과 전체 pair에 대한 비율을 분리하고 분모를 적는다. 실패 원인을 단일 trace만으로 확정하지 않는다.

입력·calibration·training·forward count·wall-clock 비용을 통제한다. Rollout frame를 독립 표본으로 세지 않는다. D0는 privileged diagnostic이며 학습하지 않은 정책에 참값을 주어도 실패할 수 있으므로 수학적 upper bound가 아니다.

G1의 clean 20회/16회 성공 기준은 [기존 pilot qualification](./PILOT_CONTRACT.md)이다. 최종 효과 크기, non-inferiority margin, sample budget은 아직 고정하지 않았다. G2 development pilot에서 분산과 비용을 본 뒤 holdout 전에 고정한다. 실험하지 않은 결과표에 예상 수치를 채우지 않는다.

## 6. 다음 행동과 buildup 판정

**D1-L3/L4 완료:** 공식 task ID·prompt/predicate·frame·native 경로는 [감사 결과](./TASK_OBSERVABILITY_AUDIT.md), perturbation·shared reset·split·정보/예산·qualification은 [후속 계약](./PRE_EXPERIMENT_CONTRACT.md)에 기록했다. Strict absolute-orientation 대조는 미확보이고 OFT Goal 0/8·contrast 1·보조 7은 조건부 후보다. L4는 R/P를 전체 관측이 같은 cause pair로 가정하지 않으며 task utility부터 검증하도록 좁혔다.

실행 가능한 명세가 되려면 실제 environment/dependency lock, checkpoint/normalizer payload hash, initial-state payload·split ledger가 필요하다. [설계 JSON](./PILOT_SPEC.json)에 perturbation·seed·cost·분할 규칙은 생성했지만 runtime freeze나 실행 manifest는 아니다. 다음 정책 실험은 OFT 후보의 G0/G1이며 현재 컴퓨터 Docker-only 조건을 따른다.

**이번 결론:** 문헌 buildup을 진행할 가치는 남지만 새 cause-conditioned VLA/RL 방법의 필요성은 확인되지 않았다. 단순 재보정과 task별 reference로 설명되는지를 배제한 뒤에만 본격 구현을 검토한다. Registry tier와 사용자 reading status는 그대로 유지한다.
