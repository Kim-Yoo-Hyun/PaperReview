# VLA 중심 주제 재탐색 — RL 선택 사항

> 2026-10-22 후속 유지보수: 후보 문서들의 외부 직접 비교 문헌 중 선별 47편을 [registry에 등록](../../update/REGISTRY_ROLLUP_2026-10-22.md)했다. 아래 “미등록/registry 변경 없음”은 당시 buildup 범위다. 현재 발표 상태는 등록 report와 각 overview를 따른다. [주제별 핵심·GPU 후속·한계](../summaries/README.md)는 기존 연구 판정을 유지한다. Memory Anchors·CounterAlign·RoboFollow의 CoRL 2026 Poster를 공식 metadata로 추가 확인했다.

- 조사 기준일: 2026-10-22 KST
- 사용자 지시: VLA 위주로 주제를 다시 탐색하며 RL 결합은 필수가 아니다.
- 상태: **문헌 기반 후보 탐색 완료**. 후속 [E1-R1 심사](../2026-10-22_e1_buildup/R1_REVIEW.md)는 gate NOT_MET·REVISE·진단 HOLD다. 아래 추천은 최초 탐색 이력이며 현재 다음 gate는 TODO의 E1-R2다.
- 범위: 기존 registry와 2024–2026 공식 proceedings, 직접 충돌 가능성이 있는 최신 preprint. 전수 systematic review는 아니다.
- 문서: [문헌·버전·공개 자산](./LITERATURE.md), [E1 질문과 반증 조건](./E1_QUESTION.md), [유지보수 검증](./VALIDATION.md), [활성 TODO](../../../TODO.md).

## 이번 탐색의 결론

우선 검토할 질문은 **“새 로봇을 학습할 때, 제어 명령의 표현 차이와 실제 행동 충돌을 구분하면 기존 로봇의 능력을 더 적은 replay로 보존할 수 있는가?”**다. E1은 이를 다루는 잠정 후보다. 새 로봇의 데이터가 추가되는 상황과 기존 능력 보존을 함께 다루므로 사용자의 장기 목표에 맞는다. 첫 대상은 manipulation이며 navigation까지 일반화했다고 주장하지 않는다.

단순한 continual VLA, replay 선택, 공통 action space, adapter/MoE는 이미 연구되어 있다. **E1의 신규성은 아직 확정하지 않았다.** 기존 방법을 결합한 것 이상의 예측과 유효한 비교 자료를 확보할 때만 buildup을 진행한다. 현재 추천은 다음 비실험 검토에 시간을 쓸 가치가 있다는 판단이다.

## 검토한 방향과 선별

| 방향 | 중요한 질문 | 이번 판단 | 직접적인 이유 |
|---|---|---|---|
| **E1: 로봇 추가 학습의 행동 충돌과 replay** | 같은 물리적 효과를 내는 서로 다른 명령도 충돌로 취급하는가? 그 구분이 실제 retention을 예측하는가? | **우선 비실험 심사** | Memory Anchors의 충돌 기반 선택과 물리적 action 정렬을 대조할 수 있다. 단순 정렬+기존 replay가 충분하면 종료 |
| E2: 제어 주기가 달라질 때 행동 전이 | 물리적 시간·feedback 빈도·action representation의 영향을 분리할 수 있는가? | **예비 질문, 현재 신규 방법 채택 보류** | FAST/RDT, AAC, SPACE, Vela, PaceVLA가 직접 인접. frequency conditioning·spline·adaptive chunk 자체는 기여가 아님 |
| 메모리의 관련성·유효성 | 과거 정보가 지금 행동에 필요한지 구별하는가? | **넓은 주장은 이번 shortlist에서 제외** | HALO가 spurious retrieval/model drift를 직접 다룬다. 저장소의 기존 memory-expiry 가설도 자동 재개하지 않음 |
| VLM 능력을 보존하는 VLA 적응 | VQA 보존이 실제 action 일반화로 이어지는가? | **새 방법 후보로 승격하지 않음** | VLM2VLA와 LAP 이후, 자연어 action·LoRA·semantic retention만으로는 부족. 기존 C2 언어 평가를 이름만 바꿔 재개하지 않음 |

E2의 잔여 질문은 **동일한 물리 경로와 prediction horizon을 유지해도 접촉 구간에서 feedback 빈도 차이 때문에 transfer가 깨지는가**다. 다만 SPACE는 이미 control-frequency shift를 평가하고 Vela/PaceVLA도 시간 표현을 바꾼다. Classical retiming/controller를 포함한 본문·구현 비교 전에는 차별성을 주장할 수 없다. E1 다음 자동 실행 queue로 두지 않는다.

## 탐색 중 수정한 해석

1. **“VLA는 잘 잊지 않는다”와 “실환경에서는 잊는다”를 모순으로 제안하지 않는다.** ICML 2026 연구와 실환경 연구는 모두 잘 설정한 replay의 효과를 보고한다. 학습·평가 조건이 다른 결과를 직접 비교해 새로운 현상을 만들 수 없다. [P4/P12](./LITERATURE.md).
2. **최신 버전으로 범위를 수정했다.** 실환경 연구의 v1은 4-task 중심이지만 v3는 단일 팔·양팔 10-task stream과 비대칭 replay까지 다룬다. “다른 kinematic configuration의 continual learning이 없다”는 주장도 제외한다. [v3 §VI–VII](https://arxiv.org/html/2605.26820v3#S6).
3. **모듈 교환·빠른 재학습은 새 진단이 아니다.** ICML 연구 §5가 이미 backbone/action-head swap과 recovery를 수행했다. [P4 본문](https://arxiv.org/html/2603.03818v2#S5).
4. **충돌이 큰 데이터의 replay 선택도 기존 방법이다.** E1은 Memory Anchors를 강한 baseline으로 삼아야 한다. 서로 다른 로봇의 command 차이를 물리적 충돌과 구별한다는 잔여 가설만 남긴다. [P10 §4](https://arxiv.org/html/2608.26545v1#S4).

## 기존 후보와의 관계

- C1–C6 및 D1–D3 판정은 그대로 보존한다. 이번 작업은 사용자가 요청한 새 탐색이다.
- E1은 RL update의 로봇 간 이득 전이를 검증했던 종료 프로젝트와 다르다. 지도학습/IL의 순차 적응에서 **과거 능력 보존과 replay 선택의 판단 근거**를 다룬다. 이전 runtime·checkpoint·정책 능력을 이어받지 않는다.
- D1의 센서 오류 원인 판별, D2의 운반 geometry, D3의 비가역 사건 후 goal 수정은 활성 질문으로 가져오지 않는다.
- 3D vision은 E1에서 action의 물리적 효과를 비교할 frame·pose의 관측 근거를 제공할 수 있다. 3D encoder 추가 자체를 기여로 삼지 않는다.
- RL은 필요성이 확인될 때 선택할 후속 수단이다. 이번 E1의 첫 비교는 supervised adaptation과 replay로 충분하다.

## 최초 탐색 당시의 buildup 위치와 후속 작업

[기존 8단계 guide](../../../research/IDEA_BUILDUP_GUIDE.md)에 따라 문제·문헌 역할·가정·질문·직접 충돌·반증 조건을 **탐색 수준으로** 정리했다. 단계 5의 전체 구현 대조와 단계 6의 실행 계약은 아직 완료하지 않았다. 단계 7의 정책/데이터 검증, 단계 8의 실제 외부 피드백도 미완료다.

최초 후속 작업으로 **E1-L1: 직접 방법과 데이터 interface 심사**를 선정했다. 이 작업과 비실험 buildup 및 [R1 후속 심사](../2026-10-22_e1_buildup/R1_REVIEW.md)를 완료했으며 현재 REVISE·진단 HOLD다. 실제 다음 gate는 [TODO](../../../TODO.md)의 E1-R2다. 최초 추천을 새 방법 채택이나 native qualification 완료로 해석하지 않는다.

공식 논문·코드 링크를 확보한 것과 실행 자격을 구분한다. 이번에는 실험·설치·Docker preflight·모델/영상/trajectory/PDF 저장을 하지 않았다. 외부 비교 문헌은 이 dossier에 기록했으며 registry 990편·tier·사용자 reading status를 유지한다.
