# C3 공개 구현·수치 검증 결과

- 실행일: 2026-10-21 KST. **MECHANISM-ONLY PASS — 정책 성능 미검증**.
- [연구 후보 판단](../../research_candidates/2026-10-21_execution_interface/README.md) · [실행 전 계약](../../research_candidates/2026-10-21_execution_interface/PROTOCOL.md) · [문헌/코드 경계](../../research_candidates/2026-10-21_execution_interface/LITERATURE.md).
- Linux ARM64 Docker에서 NumPy 2.2.6·PyTorch 2.8.0 CPU로 실행. Host에 dependency를 설치하지 않았다.

## 실제 확인한 것

SimpleVLA-RL 원본의 gripper 변환, unnormalization, masked mean, PPO loss와 decoder AST를 실행했다. 저자 checkpoint의 config/statistics는 실제 파일을 사용했으며 weight는 로드하지 않았다. Synthetic categorical distribution을 사용한 1-decision 유한합 검사다. Dataset episode·native policy forward·rollout·학습 update는 각각 **0**이다.

모든 256 action token은 native 변환 후 2개 명령으로 모인다: **−1에 65개, +1에 191개**. 다른 arm coordinate는 동일하게 유지했다. 이 count를 pretrained policy의 행동 확률로 해석하지 않는다. [매핑과 파일 hash](./evidence/source_audit.json).

## 물리 행동의 확률은 같아도 PPO surrogate가 달라지는가?

Old token distribution을 uniform으로 두고 각 gripper class 안에서 확률을 재분배했다. Advantage는 실행 명령만의 함수로 구성했으며 old policy 아래 평균 0이다. Clip 설정은 공개 recipe의 low 0.2/high 0.28이다.

| 검사 | 실제 class 확률 최대 변화 | Token KL | Token PPO loss | Class PPO loss | Token / class clip fraction |
|---|---:|---:|---:|---:|---:|
| 변화 없음 | 0 | 0 | 0 | 0 | 0 / 0 |
| 내부 확률 ±10% | 0 | 0.004986 | 약 0 | 0 | 0 / 0 |
| 내부 확률 ±60% | 0 | 0.221400 | 0.067533 | 0 | 49.61% / 0 |
| 실제 class mass +0.05/−0.05 | 0.05 | 0.006114 | −0.05 | −0.05 | 0 / 0 |

**관측:** 같은 실행 분포에서도 token clipping은 내부 확률 재배치를 다르게 취급한다. Class 확률을 합친 loss는 그 변화에 불변이다. Clip 없는 두 objective는 일치했다. Class mass가 실제로 변하는 대조군과 one-token-per-action injective 대조군에서는 두 loss가 일치했다. [전체 6개 case](./evidence/ppo_cases.json). 작은 음의 KL(약 −1e−16)은 float64 roundoff다.

49.61%는 구성한 uniform distribution에서 native surrogate가 clipping된 token의 비율이다. 실제 robot rollout의 clipping 빈도나 성공률 하락을 측정한 수치가 아니다.

## 알려진 variance-reduction 원리가 성립하는 조건과 사라지는 조건

256개 token을 모두 열거해 logit-coordinate gradient mean과 variance trace를 계산했다. Marginal estimator의 mean은 raw estimator 및 expected reward의 PyTorch autograd와 1e−12 이내로 일치했다. 이 결과는 CAPG/MPG의 기존 원리와 일관된다.

| Synthetic probability 설정 | Marginalization의 variance trace 감소 |
|---|---:|
| Uniform token distribution | 99.4965% |
| 고정 seed 0–19의 nonuniform logits | 95.0657–98.2753% |
| 각 class 확률 중 99%가 대표 token 하나에 집중 | 4.0219% |
| 각 class 확률 중 99.99%가 대표 token 하나에 집중 | 0.04127% |
| 각 class 확률 중 99.9999%가 대표 token 하나에 집중 | 0.000413% |

따라서 첫 줄만 제시해 큰 실용 이득을 주장하면 잘못이다. 실제 SFT checkpoint가 소수 token에 집중하면 이득이 거의 없을 수 있다. 위 수치는 token logits에 대한 분산이며 전체 VLA parameter gradient·sample efficiency·success gain이 아니다. [26개 분포의 유한합](./evidence/gradient_variance.json).

Autoregressive token이 이후 arm token을 바꾸는 별도 반례도 기록했다. Gripper 자체는 항상 같아도 다음 arm-left probability가 0.5→0.9로 바뀔 수 있으므로 gripper marginal만으로 전체 action equivalence를 보장할 수 없다. 이는 구성한 반례이며 실제 checkpoint의 관측값은 아니다. [경계 검사](./evidence/scope_controls.json).

## 실행과 재현

실행 script: [native_probe.py](./native_probe.py). Original source는 고정 commit, checkpoint metadata는 고정 revision으로 fetch하고 SHA-256을 기록한다. 외부 코드 전체·package cache를 repository로 복사하지 않았다. 모든 assertion이 통과했다. Report의 내부 wall time 약 1.66초는 import 이후 download와 유한합 검사 시간이며 image pull·package 설치 시간이나 VLA inference latency가 아니다.

```bash
docker create --name paper-c3-interface --label paperreview.task=c3-execution-interface \
  --memory 4g --cpus 4 \
  python:3.11-slim@sha256:e88e9763f943ec1834f992a4b51e0f24500486803e8bc534e5767af9ea65f6ce sleep infinity
docker start paper-c3-interface
docker exec paper-c3-interface pip install --no-cache-dir numpy==2.2.6 torch==2.8.0
docker cp work/experiments/vla_rl_c3_interface/native_probe.py paper-c3-interface:/tmp/native_probe.py
docker exec paper-c3-interface python /tmp/native_probe.py
```

[Runtime manifest](./runtime_manifest.json)은 실제 image·package·script 및 정리 기록을 관리한다. 전용 container와 image를 제거하면 내부 source/dependency cache도 함께 제거된다. 기존 `minikube` volume은 보존한다.

## 판단

**이론적으로 가능한 현상이 현재 공개 VLA RL 코드 경로에서도 나타남을 확인했다.** 이를 새 알고리즘이나 정책 개선 결과로 승격하지 않는다. 다음 핵심 검증은 실제 native logits·advantage에서 해당 효과가 얼마나 남는지다. 현재 장비에서 대형 backbone의 학습을 재시도할 근거는 이 결과만으로 충분하지 않다.
