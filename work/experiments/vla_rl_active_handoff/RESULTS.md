# C1 native probe 결과와 투자 판단

- 실행 종료: **2026-10-21 KST**
- 판정: **공개 checkpoint load·실제 환경 입출력 확인. Task competence·C1 효과는 미확인. 큰 후속 실험과 RL 학습은 보류.**
- [고정 조건·재실행 경로](./README.md) · [원시 결과와 package versions](./native_probe.json) · [image/source hash·실행 상태·정리 기록](./runtime_manifest.json)
- 연구 판단: [문헌 충돌](../../research_candidates/2026-10-20_vla_rl/C1_REVIEW.md) · [조건부 진단 계약](../../research_candidates/2026-10-20_vla_rl/C1_PROTOCOL.md)

## 실제로 확인한 결과

| 항목 | 관측 결과 |
|---|---|
| 실행 환경 | 현재 컴퓨터의 ARM64 Docker, CPU 6개 제한·memory 7 GiB 제한·OSMesa |
| 의존성 | Image build 성공, `pip check` 통과. Host 패키지 설치 없음 |
| Policy | 고정 SmolVLA LIBERO checkpoint 전체 strict load 성공. 새 head·학습 없음 |
| 입력 | 실제 LIBERO scene/wrist RGB 각각 `[1,3,256,256]`, state `[1,8]`, task instruction |
| 출력·환경 진행 | 매번 finite 7D action을 확인한 뒤 **243 control steps** 실행 |
| Task | `libero_spatial/0`, prescribed init index 0, seed 71000, native horizon 280 |
| 종료 | **`budget_exhausted`**. 900초 기준을 action 시작 전에 검사하여 실행 중 step 완료 후 **903.13초**에 종료 |
| Success | 종료 전 success condition 미관측. 원시 `success=null`; 완결된 실패 episode나 성공률 0%로 취급하지 않음 |
| 두 번째 task | `libero_goal/0`는 전체 시간 예산이 소진되어 **미시작** |
| 처리량 | 평균 policy inference **3.558초/호출**, 해당 실행에서는 호출마다 action 1개 |
| 메모리 | Process 최대 RSS **5,364,132 KiB ≈ 5.12 GiB**. OOM 없음, container exit code 0 |
| Initial states | 실행한 spatial task에서 50개 확인. Goal task의 init count는 runtime 미확인 |

Native control period 20 Hz와 실제 CPU inference 처리율은 다르다. 이 probe는 실시간 실행 성능을 입증하지 않았다. CPU float32·현재 package revision의 결과이며 논문이나 CUDA 평가 수치의 재현이라고 하지 않는다.

## 이 결과로 말할 수 없는 것

- 성공률, 20 states/task의 기본 능력 qualification, task/seed 일반화.
- 추가 관측의 이득, 물리 관측 primitive의 reachability, 시점 변화 후 continuation competence.
- RL이 고정 규칙·one-step prediction·imitation보다 유리하다는 결론.

243/280 steps는 완료 비율이나 성공 확률이 아니다. 시간 제한 때문에 관측을 중단한 한 시도다. 현재 결과로 checkpoint가 나쁘다거나 C1 가설이 반증됐다고 결론 내리지 않는다.

## 계산 비용과 다음 판단

측정한 평균을 단순 적용하면 `20×280 + 20×300 = 11,600` actions의 **추론만 약 11.47시간**이다. 이는 두 task를 각각 20회 최대 길이로 실행할 때의 계획용 외삽이다. 조기 성공은 시간을 줄일 수 있고, task별 입력 차이·환경 처리·초기화는 시간을 바꾼다. 그 40회 실험을 수행한 결과가 아니다. Branch sweep과 반복 seed는 이보다 추가 비용이 든다.

문헌에서는 ActiveAlign·EyeRobot 2.0·RESCUE와의 충돌로 넓은 방법·평가 기여가 약해졌다. 실행에서는 능력이 검증된 비교 기반까지 확보하지 못했다. **따라서 현재 C1에 큰 학습·rollout 예산을 추가 배정하지 않는다.** 조건부 질문과 진단 명세는 보존하고, 다음 저비용 작업은 C2의 직접 충돌 문헌을 같은 수준으로 대조하는 것이다. C2의 신규성이 통과했다는 의미는 아니다.

## 실행 자산과 보존 범위

CPU wheel을 명시하고 CMake binary path를 지정해 Docker build 문제를 해결했다. 연구 정책·task·horizon·flow steps를 성능에 맞춰 바꾸지 않았다.

결과 추출 후 이번 전용 container 1개, image 1개, 모델·simulator assets를 담은 volume 1개와 build-cache 12개를 제거했다. 무관한 `minikube` volume은 보존했다. 남긴 것은 자체 probe source·Dockerfile·명세·작은 JSON 결과이며 package·checkpoint·simulator assets는 repository에 없다.
