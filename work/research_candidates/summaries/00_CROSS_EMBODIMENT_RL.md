# 초기 주제 — 한 로봇의 RL 개선이 다른 로봇으로 전달되는가

- 요약일: 2026-10-22. **RETIRED — 2026-10-20 사용자 요청으로 종료.** 이후 후보의 GPU 대기 작업이 아니다.
- 질문: Source robot의 RL 이득이 target robot으로 전달되는 조건은 무엇이며 성공 데이터 선택·return-weighted imitation으로 설명되는가?

## 구성과 실제 결과

Frozen Octo 표현, shared adapter와 robot별 head, robosuite PickPlace의 Panda/UR5e × milk/can을 계획했다. 두 로봇이 downstream bootstrap에 참여하는 설정이므로 unseen-embodiment zero-shot이나 end-to-end VLA RL이 아니다.

첫 Panda/milk qualification에서 Gaussian BC 1/20, clean/corrective 비교 0/20·1/20, 자세 표현 비교 0/20·0/20, single/chunk 비교 0/20·2/20의 stable success를 측정했다. 각 행은 다른 초기 상태 집합이며 행 사이의 개선을 비교할 수 없다. Teacher는 각 paired 평가에서 17–18/20이었다. 저장 action replay는 네 robot/task 조합의 train/validation에서 16/16 성공했다.

실행·재생 경로는 작동했지만 learned policy가 당시 기준 4/20을 넘지 못했다. Chunk 비교는 supervision 양·feedback 간격도 달라 chunking의 단독 효과가 아니다. 전이·RL·weighted imitation 본 비교는 실행하지 않았다.

## GPU가 확보되면 가능한 최소 검증

재개가 명시적으로 결정되고 새 native 경로가 확보될 경우, 공개 task/checkpoint의 기본 능력·언어 의존성부터 Docker에서 확인할 수 있다. 이를 통과한 뒤 같은 데이터·초기 조건에서 BC_ALL, BC_SUCCESS, return/advantage weighting, TD 기반 RL의 역할을 분리한다. Source RL 후 target gain과 old-task loss를 함께 측정해야 한다.

## 한계와 재개 조건

GPU는 불충분한 bootstrap, action/proprio 의미, 데이터 지원, 신규성을 해결하지 않는다. RLDG·cross-embodiment offline RL·IQL/RvS가 강한 대안이다. “RL 전이가 없다”거나 “RL은 imitation보다 못하다”는 결론은 얻지 못했다. 이전 코드·환경·모델·데이터·상세 로그는 사용자 요청으로 삭제했으므로 이 기록만으로 재현할 수 없다.

**현재 권고:** 과거 작은 head를 그대로 다시 학습하지 않는다. 재개 시 검증된 native base와 source/target 분할, weighted-imitation 대조를 새로 고정한다.

근거: [보존된 핵심 결과](../../experiments/vla_rl_cross_embodiment/RESULTS.md). 문헌 링크와 수치 조건은 원 기록을 따른다.

## Registry 연결 — 2026-10-22 등록

- [Rethinking VLA Scaling](../../../2026/arXiv/2026_arXiv_Rethinking-Visual-Language-Action-Model-Scaling-Alignment/01_overview.md) — 2026 arXiv, `pr-0996`.
- [SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies](../../../2026/arXiv/2026_arXiv_SPACE-Enabling-Learning-from-Cross-Robot-Data-Toward-Gener/01_overview.md) — 2026 arXiv, `pr-1000`.
- [Forget-Me-Not](../../../2026/ICML/2026_ICML_Pretrained-Vision-Language-Action-Models-are-Surprisingly/01_overview.md) — 2026 ICML, `pr-0991`.

발표 status와 신규 5개 note의 근거는 각 overview를 따른다. 이전 buildup의 정독/코드 감사와 이번 abstract 기반 등록의 범위를 합치지 않는다.
