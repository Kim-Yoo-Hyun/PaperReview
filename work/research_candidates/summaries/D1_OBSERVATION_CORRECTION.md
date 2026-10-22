# D1 — 관측 오류와 실제 상태 변화에서 보정을 선택하기

- 요약일: 2026-10-22. **현재 신규 방법 NO-GO / 조건부 robustness 진단 HOLD.**
- 질문: 같은 관측 정보에서 언제 proprio/vision 보정이 행동에 유익하고 언제 해로운가? 단순 calibration·causal residual 이후에도 선택이 필요한가?

## 실제 진행과 결과

GAP·G-PSMR·ReViP와 직접 대조하고 합성 반례·Docker source audit를 수행했다. 원인 식별 가능성과 행동상 필요성은 다르다. 실제 pose 변화에도 보정이 유리할 수 있어 ‘실제 변화면 보정 금지’ 전제를 철회했다.

지정 `pi05_libero` variant의 state 값이 action으로 연결되지 않아 primary에서 제외했다. Proprio-enabled OFT Goal variant와 task0/8·contrast1·보조7을 정적 후보로 바꿨다. Native utility는 미검증이다. D1-E1 resource preflight에서 GPU allocation이 실패했고 VM RAM7.65GiB와 해당 model tensor14.05GiB를 확인했다. G0 전체 미충족·G1 정책 평가0회다. Source의 CPU fallback 존재를 native 실행 성공으로 해석하지 않는다.

## GPU가 확보되면 가능한 최소 검증

먼저 D1-R2의 차별적 task/cue 조건이 충족돼야 한다. 이후 사용자가 선택한 현재/clone 컴퓨터의 로컬 Docker에서 compatible runtime·checkpoint/normalizer·paired reset을 고정하고 clean competence와 state/goal utility를 확인한다. Report-only 오류, 실제 pose 변화, 비보정·고정 reference·causal 재보정의 matched 비교를 할 수 있다.

## GPU 외 한계

모든 양립 조건에서 같은 보정이 최적이면 cause classifier가 필요 없다. 최적 선택이 달라도 입력에 구별 정보가 없으면 RL이 이를 만들어내지 못한다. 단순 reference 조정 이후 gap, 실제 task cue와 action utility, 원문/공개 code 차이의 검증이 남았다. G1 성공만으로 top-tier 기여가 되지 않는다.

**현재 권고:** 자원만의 HOLD가 아니다. 새 task·정보·대안 이후 gap 없이 preflight를 반복하거나 learned method를 구현하지 않는다.

근거: [최신 비실험 심사](../2026-10-21_d1_buildup/NONEXPERIMENTAL_REVIEW.md), [task 감사](../2026-10-21_d1_buildup/TASK_OBSERVABILITY_AUDIT.md), [실제 preflight](../../experiments/vla_d1_e1_preflight/RESULTS.md), [비실행 계약](../2026-10-21_d1_buildup/PRE_EXPERIMENT_CONTRACT.md).

## Registry 연결 — 2026-10-22 등록

- [ActiveAlign](../../../2026/arXiv/2026_arXiv_Look-Before-You-Act-Bridging-Active-Perception-and-Vision/01_overview.md) — 2026 arXiv, `pr-1030`.
- [SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies](../../../2026/arXiv/2026_arXiv_SPACE-Enabling-Learning-from-Cross-Robot-Data-Toward-Gener/01_overview.md) — 2026 arXiv, `pr-1000`.

발표 status와 신규 5개 note의 근거는 각 overview를 따른다. 이전 buildup의 정독/코드 감사와 이번 abstract 기반 등록의 범위를 합치지 않는다.
