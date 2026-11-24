# ActMem-VLA: Action-History Memory with Dual-Expert Denoising for Long-Horizon Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 표시한 평가 항목을 확인했다.
> Source audit: 2026-11-24 원문 대조.

## Evaluation in One Sentence

LIBERO-Mem 평균 80.8%는 과제별 시연 길이로 정한 스텝 제한을 적용한 결과다. 공통 600스텝 제한의 결과는 그림 3, 과제별 제한은 그림 4에 실렸다. [PDF 4쪽](https://arxiv.org/pdf/2609.37307v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2609.37307v2#page=5)

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT AND SIMULATION`.

## Dataset / Benchmark Role

10개 기억 의존 시뮬레이션 과제와 실물 과제를 구분해 평가했다. [PDF 4쪽](https://arxiv.org/pdf/2609.37307v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2609.37307v2#page=5)

## Metrics and Success Definition

과제별 제한은 훈련 시연 길이의 95% 분위수를 기준으로 20스텝 단위로 올림하고 최대 600으로 제한한다. [PDF 5쪽](https://arxiv.org/pdf/2609.37307v2#page=5)

## Baselines and Fairness

시뮬레이션에서 π0.5 및 MemoryVLA와 비교했다. 실물 비교 대상은 π0.5다. [PDF 4쪽](https://arxiv.org/pdf/2609.37307v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2609.37307v2#page=5)

## Statistics, Efficiency, and Reproducibility

주 시뮬레이션 비교는 방법·과제당 시행 180회, 실물은 방법·과제당 시행 20회다. [PDF 5쪽](https://arxiv.org/pdf/2609.37307v2#page=5)

## Proposed Evaluation — Researcher Interpretation

같은 명령 이력에서 실제 접촉/효과가 달라지는 자연 사례로 관측·이력 의존성을 비교한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.37307).
