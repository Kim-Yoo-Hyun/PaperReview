# RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 표시한 평가 항목을 확인했다.
> Source audit: 2026-11-24 원문 대조.

## Evaluation in One Sentence

LIBERO에서 수집한 원 에피소드 1,562개 중 262개가 실패했다. 128,340건은 저장한 체크포인트에서 복원·실행한 반사실적 분기다. [PDF 3쪽](https://arxiv.org/pdf/2610.13516v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2610.13516v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2610.13516v1#page=5)

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.

## Dataset / Benchmark Role

OpenVLA-OFT와 π0.5의 LIBERO-Plus가 주 분석이며, 약화한 정책과 기본 환경을 대조 조건으로 사용했다. [PDF 4쪽](https://arxiv.org/pdf/2610.13516v1#page=4)

## Metrics and Success Definition

복구 성공 확률의 Jeffreys 사후분포 25% 분위수가 기준 τ에 도달하는지를 개입별로 평가했다. [PDF 3쪽](https://arxiv.org/pdf/2610.13516v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2610.13516v1#page=4)

## Baselines and Fairness

계속 실행과 스크립트 복구를 같은 체크포인트에서 비교했다. [PDF 3쪽](https://arxiv.org/pdf/2610.13516v1#page=3) · [PDF 5쪽](https://arxiv.org/pdf/2610.13516v1#page=5)

## Statistics, Efficiency, and Reproducibility

원 에피소드 1,562개에서 체크포인트 10,083개를 분기했다. 체크포인트당 초기 분기 수는 4개이고 기준 경계 근처에서 16개로 늘렸다. [PDF 4쪽](https://arxiv.org/pdf/2610.13516v1#page=4)

## Proposed Evaluation — Researcher Interpretation

동일 failure onset에서 continue/hold/개입을 branch해 비용 포함 outcome을 비교한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.13516).
