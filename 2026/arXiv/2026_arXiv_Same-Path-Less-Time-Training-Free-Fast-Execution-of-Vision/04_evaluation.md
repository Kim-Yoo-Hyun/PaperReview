# Same Path, Less Time: Training-Free Fast Execution of Vision-Language-Action Models under Inference Latency

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 표시한 평가 항목을 확인했다.
> Source audit: 2026-11-24 원문 대조.

## Evaluation in One Sentence

표 1의 처리량은 추론 대기 시간을 포함한 제어 1,000스텝당 성공 횟수다. π0.5는 4개 과제군, SmolVLA는 2개 과제군에서 비교했다. [PDF 7쪽](https://arxiv.org/pdf/2611.01390v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2611.01390v1#page=8)

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.

## Dataset / Benchmark Role

정적 LIBERO와 표적이 움직이는 LIBERO-Dynamic 결과를 분리했다. [PDF 7쪽](https://arxiv.org/pdf/2611.01390v1#page=7) · [PDF 10쪽](https://arxiv.org/pdf/2611.01390v1#page=10)

## Metrics and Success Definition

처리량과 에피소드 성공률을 함께 보고했다. [PDF 7쪽](https://arxiv.org/pdf/2611.01390v1#page=7)

## Baselines and Fairness

동기 실행, 비동기 등속 실행 등과 비교했고 지연 0인 행은 참조값으로 표시했다. [PDF 7쪽](https://arxiv.org/pdf/2611.01390v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2611.01390v1#page=8)

## Statistics, Efficiency, and Reproducibility

표 1의 각 모델·방법·과제군 조합에서 에피소드 100개를 사용했다. 방법 간 초기 상태와 시드를 맞췄다. [PDF 7쪽](https://arxiv.org/pdf/2611.01390v1#page=7)

## Proposed Evaluation — Researcher Interpretation

동일 frozen 정책에서 stop-and-wait·비동기1배속·PTS를 같은 지연과 성공/시간으로 대조한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2611.01390).
