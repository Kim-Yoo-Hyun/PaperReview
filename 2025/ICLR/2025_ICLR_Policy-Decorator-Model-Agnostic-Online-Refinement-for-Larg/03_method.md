# Policy Decorator: Model-Agnostic Online Refinement for Large Policy Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Policy and Learning Pipeline

동결 base 위에 SAC residual을 학습하고 residual 범위와 탐색 진행을 제어한다.

## Observation, State, and Action

Base 행동 + 제한된 residual → 환경. Base 모델 계열별 적용 가능성과 학습된 residual weights의 전이는 서로 다른 주장이다.

## Training versus Deployment

초기 base 능력과 적절한 residual 크기·탐색 schedule이 학습에 중요하다.

제어 주기·horizon·loss 계수 전체는 이번 노트에서 확정하지 않았다. 실제 baseline 이식 전 원문과 code 설정을 함께 대조한다.

근거: [지정 본문](https://proceedings.iclr.cc/paper_files/paper/2025/file/45c361d4117d598d4bb6568b407e9ac9-Paper-Conference.pdf) — final paper §4.1–4.3, selected Appendix B.5; project/code README.
