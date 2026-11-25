# Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. 평가 내용은 아래에 인용한 원문 쪽에서 추가 대조했다.
> Source audit: 2026-11-25, 평가 설계와 주요 비교를 원문에서 확인했다.

## Evaluation in One Sentence

ActiveAlign은 손목 카메라가 시점을 바꾼 직후의 관측에서 조작을 시작하도록 VLA를 재학습해 시뮬레이션과 실물에서 비교했다. [PDF 5쪽](https://arxiv.org/pdf/2610.23378v1#page=5)

## Evaluation Type and Scope

LIBERO의 시작 시점을 교란한 시험과 두 실물 작업대의 평가를 수행했다. 실물 과제 다양성(표 VII)과 가림 정도(표 VIII)는 별도 실험이다. [PDF 7쪽](https://arxiv.org/pdf/2610.23378v1#page=7)

## Dataset / Benchmark Role

기존 시연의 중간 상태를 새 카메라 시점에 맞춘 뒤 나머지 동작을 재생했다. 재생에 성공한 궤적을 적응용 자료로 썼다. 따라서 시점 이동과 학습 자료 선택이 함께 작용할 수 있다. [PDF 4쪽](https://arxiv.org/pdf/2610.23378v1#page=4)

## Metrics and Success Definition

표 I는 네 LIBERO 묶음의 평균 성공률(%), 표 VIII는 가림 수준별 실물 성공 수와 시행 수를 보고한다. 구체적인 값은 아래 표 대조에 있다. [PDF 5쪽](https://arxiv.org/pdf/2610.23378v1#page=5)

## Baselines and Fairness

고정 시점, 시점만 바꾼 동결 정책, 같은 시점 선택 뒤 조작 정책을 적응시킨 조건을 비교했다. 마지막 조건은 조작 정책의 학습 자료도 달라진다. [PDF 5쪽](https://arxiv.org/pdf/2610.23378v1#page=5)

## Ablations and Sensitivity

저자는 시각 입력 변화, 로봇 상태 변화, 성공한 연결 시연의 선택 효과를 분석한다. 표 I와 VIII에서 이들 각각의 독립 기여를 읽어낼 수는 없다. [PDF 6쪽](https://arxiv.org/pdf/2610.23378v1#page=6)

## Generalization and Failure Cases

정렬 후 시연을 재생할 수 있어야 자료를 만들 수 있다. 실패한 재생은 제외되므로 새로운 시점에서 시작 가능한 궤적 위주로 표본이 선택된다. [PDF 7쪽](https://arxiv.org/pdf/2610.23378v1#page=7)

## Statistics, Efficiency, and Reproducibility

실물 가림 표는 조건별로 90회, 가림 수준별로 30회씩 집계했다. 이 표의 분모에 과제 다양성 평가를 합산하지 않는다. [PDF 7쪽](https://arxiv.org/pdf/2610.23378v1#page=7)

## Proposed Evaluation — Researcher Interpretation

같은 policy에서 immediate/look/wait와 matched continuation adaptation을 분리한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.23378). 이번 대조의 범위는 위 쪽수와 표에 명시했다.

## 조건별 성공률

LIBERO 시점 교란에서 π0.5 성공률은 기본 46.3%, 시점 이동만 적용하면 11.5%, 적응 후 72.7%였다. 기본 정책 대비 차이는 26.4%p다. [표 I · PDF 5쪽](https://arxiv.org/pdf/2610.23378v1#page=5)

실물 가림 평가의 전체 성공 횟수는 고정 시점 35/90, 시점 이동만 17/90, 적응 후 83/90이었다. 표 VII의 과제별 실험은 별도 집계다. [표 VIII · PDF 7쪽](https://arxiv.org/pdf/2610.23378v1#page=7)
