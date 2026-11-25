# Insights — See Selectively, Act Adaptively: Dual-Level Structural Decomposition for Bimanual Robot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`

2026-11-20에 저자 본문 v2의 III–IV절을 확인했다. [논문 정보와 출처](./01_overview.md)

## 논문이 직접 뒷받침하는 결론

구간별 시연 라벨이 있는 설정에서 같은 π₀.₅ 백본에 손목 뷰 선택과 양팔 전문가 라우팅을 결합하면 저자가 평가한 조작들의 평균 완수율이 높아졌다. 양팔 결합을 언제 쓸지 학습하는 문제에는 실물까지 검증한 선행이 있다. [본문 IV-C, IV-E](https://arxiv.org/html/2606.13279v2#S4.SS3)

## 현재 연구에서의 해석

후보 ②의 비교 대상은 같은 평균 명령 주위에서 두 팔의 탐색 오차를 얼마나 결합할지 정하는 확률 정책이다. 시연 단계 라벨로 평균 행동 경로를 고르는 위 정책과, 보상으로 탐색 공분산을 바꾸는 정책은 학습 신호와 바꾸는 변수가 다르다. StructRL의 탐색 잡음과 상태 의존 공분산, 사람이 정한 그리퍼 규칙을 함께 대조해야 한다. [StructRL](https://arxiv.org/abs/2608.15139) · [Lattice](https://proceedings.neurips.cc/paper_files/paper/2023/hash/b0ca717599b7ba84d5e4f4c8b1ef6657-Abstract-Conference.html)

최소 반증 실험은 같은 물체를 공동 파지한 상태와 각 손이 별도 목표로 이동하는 상태에서 평균 명령과 총 잡음 크기를 고정하는 것이다. 결합 정도만 바꿔 파지 유지와 독립 목표 진전을 각각 확인한다. 두 구간의 우열이 같거나 손 상태 규칙이 같은 결과를 내면 학습한 결합 가중치에 부여할 기여가 줄어든다. [후보 ② 설계](../../../work/research_topics/RESULTS.md#donor-retreat)
