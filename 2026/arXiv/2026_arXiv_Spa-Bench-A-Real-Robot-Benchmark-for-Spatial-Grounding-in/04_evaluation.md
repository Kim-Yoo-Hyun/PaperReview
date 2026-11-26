# Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. 아래에 인용한 원문 절·표의 평가 조건을 대조했다.
> Source audit: 2026-11-25 원문 방법·평가 대조.

## 평가 조건

**Spa-Bench (robotics)** 저자들은 하나의 SO-101 실물 환경에서 공간 관계를 묻는 여섯 과제의 시연을 수집했다. 다섯 시점의 RGB 영상을 동기화해 저장하고 평가 정책에는 중앙 및 손목 영상 두 개를 제공했다. [PDF 4쪽](https://arxiv.org/pdf/2610.12696v1#page=4)

같은 물체 조작을 공간 추론 없이 직접 지시하는 대조를 다섯 과제에 적용했다. 상대 크기는 직접 지시 대조에서 제외했다. [PDF 4쪽](https://arxiv.org/pdf/2610.12696v1#page=4)

평가를 완료한 정책과 일부 조건만 시험한 정책의 분모를 구별했다. 로봇 상태를 쓰는 모델의 입력에는 영상 외에 해당 상태도 포함된다. [PDF 6쪽](https://arxiv.org/pdf/2610.12696v1#page=6)

## Proposed Evaluation — Researcher Interpretation

현재 SET의 D/R 설계와 Counting 평가 정의를 먼저 맞춘다. SO-101 결과를 VLABench simulator의 결과로 대체하지 않으며 실제 실행은 별도 조건을 따른다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.
