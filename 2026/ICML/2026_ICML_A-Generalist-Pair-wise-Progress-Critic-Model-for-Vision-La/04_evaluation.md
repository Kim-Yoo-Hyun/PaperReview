# A Generalist Pair-wise Progress Critic Model for Vision-Language-Action Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. 아래에 인용한 원문 절·표의 평가 조건을 대조했다.
> Source audit: 2026-11-25 원문 방법·평가 대조.

## 평가 조건

InternVL2의 2B 및 8B 판본으로 두 시점의 진행도 차이와 행동 예측을 학습했다. 참조 시연을 문맥으로 제공하는 조건을 포함한다. [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26if/zhang26if.pdf#page=5)

실물 제어 기체는 AGILE PiPER다. 모델이 예측한 진행도와 PPO의 학습 보상, 모델의 직접 행동 출력은 서로 다른 경로다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26if/zhang26if.pdf#page=6)

과제를 가로질러 진행도 추정 성능을 비교한 표와 로봇 정책의 성공 평가는 각각의 기준으로 해석한다. 공개 자료 중 원 모델에 맞는 파일은 그릇 집기 예제 영상까지 확인했다. [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26if/zhang26if.pdf#page=7)

## Proposed Evaluation — Researcher Interpretation

최종 학습 그래프의 weight sharing·freeze·reward 공급 경로를 확인한 뒤 독립 성공 판정과 자기 progress 점수의 변화를 분리한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.
