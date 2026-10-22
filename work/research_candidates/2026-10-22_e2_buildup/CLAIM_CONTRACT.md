# E2 해석적 검사와 주장–증거 계약

- 2026-10-22. [판단](./README.md) · [직접 선행](./CLOSEST_WORK.md)
- 아래 수식·반례·비교 설계는 **연구자 도출**이다. 정책·simulation·FK 실행 결과가 아니다. 새로운 제어 이론을 주장하지 않는다.
- 실행 spec은 [QUALIFICATION_SPEC.json](./QUALIFICATION_SPEC.json), `executable=false`. 실제 task/checkpoint/seed/split·효과 크기·sample budget을 정하기 전 구현으로 넘어가지 않는다.

## 1. 하나의 Hz로 합치지 않을 변수

| 변수 | 정의 | 반드시 남길 근거 |
|---|---|---|
| Δ_label | 학습 action target의 물리적 시간 간격 | 데이터 timestamp와 label 생성 규칙 |
| H / T_pred | 예측 target 수 / 예측의 물리 시간 범위 | frame index가 아닌 target별 시간. 첫 target convention 포함 |
| Δ_cmd | 상위 target을 controller에 전달하는 간격 | 실제 issue/accept timestamp와 jitter |
| K / T_replan | 다음 VLA 계획까지 실행하는 target 수 / 시간 | async 중 시작·완료·적용 시점을 각각 기록 |
| age_RGB / age_state | 사용한 이미지·proprio의 capture 시점부터 action 적용까지의 나이 | 센서별 capture·receive·consume 시각. 반복된 frame을 새 정보로 세지 않음 |
| ℓ | inference·통신·queue로 action이 준비될 때까지의 지연 | wall time와 simulated time을 분리 |
| Δ_servo / Δ_physics | 저수준 servo / simulator integration 간격 | controller mode·gain·한계·substep 설정 |

균일 sampling의 단순 동기 경우 KΔ_cmd는 open-loop 시간 근사다. 비동기 queue에서는 동일 식을 전체 feedback age로 사용하지 않는다. H개 target의 span도 첫 target이 t인지 t+Δ인지에 따라 다르므로 timestamp를 원본으로 둔다.

## 2. 약한 주장에 대한 해석적 검사

### A. 같은 chunk 길이는 같은 정보 차단 시간이 아니다

K=8을 20 Hz로 실행하면 0.4초, 40 Hz로 실행하면 0.2초 후 재계획한다는 동기 예를 생각한다. 이는 산술적 예시이며 실제 성능 측정이 아니다. 주파수를 바꾸면서 K를 그대로 두면 명령 간격과 재관측 기회가 함께 변한다. 표현 효과만 검증하려면 물리적 horizon을 맞추고 quantization으로 정확히 맞출 수 없는 오차도 기록해야 한다.

### B. Resampling과 retiming은 다른 개입이다

같은 timed reference q*(t)를 다른 grid에서 표현하는 것과 q*(ct)로 더 빨리 움직이는 것을 구분한다. 후자는 미분 가능한 구간에서 속도를 c배, 가속도를 c²배 바꾼다. Tracking 한계·contact 결과도 바뀔 수 있다. 실제 closed-loop 궤적까지 같다고 전제하면 검증하려는 결과를 가정하는 오류다. 같은 reference·초기조건만 통제하고 실제 궤적 차이는 결과로 측정한다.

### C. Delta 병합은 물리 행동 동치를 보장하지 않는다

고정 좌표계의 단순 위치 합은 endpoint를 맞출 수 있다. 그러나 일반 회전의 composition은 교환 가능하지 않고, intermediate contact·gripper 전환·포화가 끼면 endpoint만으로 경로의 결과가 정해지지 않는다. 따라서 action aggregation의 reconstruction 점수만으로 성공 동치를 주장하지 않는다. Action이 absolute pose, body-frame delta, velocity 중 무엇인지 먼저 고정한다.

### D. Simulator wall time과 물리적 지연은 다르다

`env.step`에서만 세계가 진행되는 loop는 model call이 오래 걸려도 그 사이 물체가 움직이지 않을 수 있다. `sleep`만 넣는 것은 물리 지연 개입이 아니다. 지연 검증에는 simulation time 기준으로 계속 진행하는 scheduler 또는 명시적인 action-queue delay가 필요하고, residual inference delay도 별도로 계정해야 한다. 실제 realtime queue와 고정 step-delay emulation의 결론 범위를 나눈다.

### E. 주기 의존 metric의 착시

균일 grid의 위치 third difference를 jerk로 해석하려면 Δt³으로 나눈 물리 단위가 필요하다. Interpolation과 필터도 고정해야 한다. 성공 episode만의 완료 시간은 실패가 늘어난 방법을 빠르게 보이게 할 수 있으므로 전체 성공률과 failure-inclusive deadline 결과를 함께 보고한다. 이 원칙 자체는 새로운 metric 기여가 아니다.

## 3. 주장–증거 표

| 가설 | 지지에 필요한 관찰 | 구별하는 비교 | 기각/축소 조건 |
|---|---|---|---|
| H_rep: 시간 표현이 별도 이득을 준다 | 동일 정보·시간·controller/compute 범위에서 잔여 행동 이득 | 동일 target/data budget의 표현 변경 vs 단순 interpolation; 학습과 execution 변경은 다른 arm | 모든 차이가 gain·시간 재조정·feedback으로 설명되면 표현 주장을 기각 |
| H_fb: 최신 관측을 쓰는 것이 차이를 설명한다 | 같은 호출 schedule에서 fresh vs stale 입력이 다른 결과 | 같은 trained residual 또는 policy, 같은 compute의 sensor별 freshness intervention | Fresh 입력이 기여하지 않거나 state-only correction으로 충분하면 vision/VLA 주장 축소 |
| H_ctrl: tracking/controller 차이가 중요하다 | gain/mode-only 대조가 차이를 설명 | 표현·시간을 고정한 controller 변경, 양쪽의 유효 operating range에 한정 | 효과가 없다고 다른 가설을 자동 채택하지 않음 |
| H_diag: 통제가 유용한 설계 지식을 더한다 | 방법 순위·권장 조건이 일관되게 바뀌거나 기존 설명을 수정 | matched causal comparison + 각 방법의 native best-system 결과를 별도 제시 | 단순 설정 오류 수정/이미 알려진 결론 반복이면 독립 연구로 종료 |

Fresh/stale 개입은 실제 capture된 과거 관측만 사용한다. Future image·GT event는 privileged diagnostic으로 따로 표시한다. Sensor age를 바꾸며 model 자체가 훈련 분포 밖으로 나가는 효과도 경쟁 설명이다. 이 비교는 freshness의 causal effect를 해당 policy에 대해 추정할 뿐 optimal policy의 보편적 가치를 증명하지 않는다.

## 4. 최소 비교와 비용 공정성

1. **Native frozen VLA:** 여러 fixed K를 validation에서 선택. Test 최적 K를 oracle baseline처럼 공정하게 표시하지 않는다. Task·scene·initial-state 분리와 paired reset 필요.
2. **단순 시간/제어 대조:** 같은 timed reference의 resampling, 물리 horizon 보존, gain-only. 그리퍼와 rotation 규칙을 명시하고 물리적 validity를 검증한다.
3. **RTC/AAC:** 호환 backbone·normalizer·controller 안에서 비교. AAC sample 수, RTC denoising/guidance, 호출 횟수·memory·wall time를 포함한다. 원 논문의 다른 모델 숫자를 직접 비교하지 않는다.
4. **A2C2:** 추가 학습 데이터·step·head parameter와 매 step 정보를 별도 비용으로 기록. Frozen learned head의 fresh/stale ablation은 mechanism 검사다. 학습된 head와 무학습 baseline의 차이를 정보 효과 하나로 읽지 않는다.
5. **Oracle/privileged:** 필요한 경우만 추가. 실제 정보·예산이 다르면 배포 baseline 또는 엄밀한 상한으로 부르지 않는다.

처음부터 모든 방법을 구현할 필요는 없다. 연구 gate가 해제되면 qualified 한 경로의 fixed horizon·단순 통제부터 시작한다. Native competence가 없으면 learned temporal module을 추가하지 않는다. 단일 backbone에서 시작한 결과를 VLA 전체·다양한 robot으로 일반화하지 않는다.

## 5. Metric·검증·중단 계약

- Primary: 동일 task predicate의 성공률과 동일 physical deadline에서의 결과. Success 정의·termination·timeout을 arm마다 바꾸지 않는다.
- Secondary: failure-inclusive 시간, event별 recovery, 실제 sensor age·deadline miss, tracking/physical smoothness와 compute. Metric은 장면별 근거와 단위를 함께 저장한다.
- Statistical unit은 독립 초기 조건/episode이며 frame을 독립 trial로 세지 않는다. Paired 차이와 불확실성을 제시한다. Task subgroup·practical margin·sample size는 qualification 뒤 결과를 보기 전에 고정한다. 현재는 미선정이며 confirmatory study라고 표시하지 않는다.
- 같게 만들 수 없는 controller domain 또는 sample/latency budget은 억지로 맞춘 척하지 않는다. Pareto 비교와 제한된 causal 비교를 분리한다.
- Reject: qualified baseline에서도 정상 능력이 없으면 중단. 쉬운 대안으로 충분하면 큰 방법을 구현하지 않는다. 통제 후 남는 차별적 현상이 없으면 E2를 standalone 주제로 종료한다.
- Revise: 한 controller·task에서만 보이면 그 범위로 제한. Effect가 관측 freshness보다 gain으로 설명되면 VLA representation 기여로 포장하지 않는다.

**현재 결과:** 이 계약의 정적·해석적 부분만 완료. 성능 표는 작성하지 않았으며 모든 효과 수치·native 자격·외부 피드백은 미확인이다.
