# D1 1차 buildup 검사 결과

2026-10-21. **완료 범위는 문헌 비교, formulation 반례, 공개 source/자원 전제 감사다. VLA inference·학습·physics rollout은 0회다.**

## 1. 합성 관측 가능성 반례

[Script](./diagnostic.py) · [기계 판독 결과](./diagnostic_result.json).

1D delta-position model을 사용했다. 단위는 mm이고 `x(t+1)=x(t)+u(t)`, reported state `p=x+b_p`, visual position `v=x+b_v`다. 고정 world goal은 0이며 초기 참값·관측 가능한 고정 world landmark·접촉·hard stop이 없다. 이 toy에서 image를 scalar position으로 축약한 것이므로, 실제 RGB 전체의 정보를 보존한 VLA 실험은 아니다.

두 world를 비교한다.

- A: `x_A(0)=0`, `b_p=d`, `b_v=0`.
- B: `x_B(0)=d`, `b_p=0`, `b_v=−d`.

임의의 같은 delta command sequence에서 항상 `x_B=x_A+d`이므로 두 world의 `p,v`와 과거 command는 같다. 그러나 world-goal 0으로 가는 명령은 `−x_A`와 `−x_B`로 다르다. History를 늘리는 것만으로 이 gauge ambiguity는 사라지지 않는다. 같은 관측을 받는 deterministic policy의 행동도 같으므로 동일 초기 random seed의 closed-loop policy에도 논리가 적용된다.

Offset `{1,2,4,8}`, history `{1,4,16}`, seed `0…7`의 **96개 구성쌍**을 검사했다. 모두 동일 관측 history·서로 다른 world-goal action을 확인했고 최대 action 차이는 8mm였다. 이것은 미리 구성한 수학적 반례의 구현 검증이며, **96번의 독립 로봇 trial이나 통계적 성능 결과가 아니다.**

### 반례의 대조 조건

| 조건 | 결과 | 해석 |
|---|---|---|
| 같은 camera의 알려진 world landmark `L=0`을 추가 | 96/96에서 `x=v−l`, `b_p=p−x`로 복구 | Anchor가 주는 추가 정보만으로 해결. Learned model 필요성 근거 아님 |
| Robot와 goal이 함께 translation되어 상대 거리만 중요 | 96/96에서 필요한 행동 동일 | Fault identity가 불명확해도 task control에는 무관할 수 있음 |
| 깨끗한 직전 state, 동기화, 단일 additive fault | Proprio `(d,0)`, vision `(0,d)`, actuation `(d,d)` innovation이 분리 | 단순 residual baseline을 먼저 넘어야 함 |
| 두 observation channel이 동시에 이동 | `(d,d)`가 actuation과 같음 | Single-fault 가정 제거 시 같은 분류 규칙 사용 불가 |
| 실제 외력 이동이 fault onset에 발생 | 첫 innovation `(d,d)`가 actuation과 같음 | 이후 지속성·추가 관측 가정을 확인해야 함. Onset만으로 원인 확정 불가 |

Actual camera geometry, occlusion, measurement noise, contact dynamics, controller feedback와 language grounding은 이 검사에 없다. 실제 scene의 배경/목표가 이미 landmark라면 첫 반례의 가정이 성립하지 않을 수 있다. 반대로 고정 기준점 없는 상대-goal 작업에는 absolute-state 식별 자체가 불필요할 수 있다. **Observability와 task relevance를 함께 정의해야 한다**는 것이 이번 결과다.

## 2. Source와 실행 조건

[Artifact audit](./artifact_audit.json)은 public source를 Docker 메모리로 읽어 commit·path·hash·짧은 line cue만 저장했다. Dependencies·weights·dataset을 설치하거나 내려받지 않았다. GAP 13파일, openpi 6파일을 확인했고 두 tree 모두 truncated=false다.

- openpi native LIBERO input과 state adapter가 존재한다. README는 NVIDIA GPU와 inference memory `>8GB`를 안내하고 `pyproject.toml`은 CUDA JAX 경로를 포함한다. 이번 Docker daemon은 ARM64, 총 메모리 약 7.65GiB이며 container에서 `/dev/nvidia*` 장치가 0개였다. **공식 native 실행 경로를 현재 자원에서 충족하지 못했다.** CPU 실행이 이론적으로 불가능하다는 결론은 아니다.
- GAP의 공개 implementation에는 CUDA phase predictor와 CUDA config가 있다. 단순 model-free 진단과 policy 학습을 구별한다. 정책·Octo checkpoint 실행을 완료했다고 하지 않는다.
- Self-Adaptive, ReViP 등의 paper별 runnable artifact 조합이 아직 완비되지 않았다. Code URL을 찾은 사실과 재현할 수 있다는 사실을 분리한다.

## 3. 판단

| 항목 | 결과 |
|---|---|
| 문제의 존재 | 문헌 근거 있음; target D1 stratum의 실제 빈도는 미확인 |
| Broad novelty | 반대 근거 있음: modality rebalance·hardware adaptation·stream restoration·classical FDI |
| 모든 조건에서 원인 구별 가능 | 반례로 기각 |
| 원인 구별이 항상 행동에 필요 | 상대-goal 반례로 기각 |
| 좁은 조건부 연구 질문 | 유지하되 actual VLA headroom·baseline gap 미확인 |
| 본격 신규 방법 학습 | **HOLD** |

현재 권고는 **REVISE / diagnostic pilot의 조건부 검토**다. Native competence, input use, identifiable-and-action-relevant paired cases, strongest simple baseline 잔여 gap이 확보되지 않으면 D1을 연구 주제로 채택하지 않는다. 기존 C1–C6를 다시 살리는 근거로도 사용하지 않는다.

## 4. 실행·보존 경계

Python stdlib diagnostic과 public-source read만 Docker에서 실행했다. Host에는 registry notes, 작성한 검사 script, 작은 결과 JSON/manifest, Markdown만 보존했다. 다운로드한 upstream code는 container memory에만 있었고 host package/model/cache 설치는 없다. 전용 container/image 정리와 보호 파일 검증은 [VALIDATION.md](./VALIDATION.md), 실제 image/source/report hash는 [runtime_manifest.json](./runtime_manifest.json)을 따른다.
