# Towards Long-Lived Robots: Continual Learning VLA Models via Reinforcement Fine-Tuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. 아래에 인용한 원문 절·표의 평가 조건을 대조했다.
> Source audit: 2026-11-25 원문 방법·평가 대조.

## 평가 조건

NORA-Long이 생성한 FAST+ 행동 토큰의 참조 일치도와 복호화한 연속 궤적 정합도를 보상으로 계산한다. 초기 형식 검사를 통과한 출력만 궤적 비교에 사용한다. [PDF 5쪽](https://www.roboticsproceedings.org/rss22/p086.pdf#page=5)

SimplerEnv의 WidowX·Google Robot 과제, LIBERO 과제군, 실제 Franka 실험을 나눠 보고한다. 초기 다중 과제 적응과 이후 순차 학습에서 이전 과제가 유지되는지는 별도 비교다. [PDF 6쪽](https://www.roboticsproceedings.org/rss22/p086.pdf#page=6)

## Proposed Evaluation — Researcher Interpretation

동일 참조 데이터로 SFT, 동일 가중 회귀, chunk RL을 비교하고 새·기존 과제를 함께 평가한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.
