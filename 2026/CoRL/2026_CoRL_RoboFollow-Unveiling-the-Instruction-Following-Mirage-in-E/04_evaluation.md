# RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. 평가 내용은 아래에 인용한 원문 쪽에서 추가 대조했다.
> Source audit: 2026-11-25, 평가 설계와 주요 비교를 원문에서 확인했다.

## Evaluation in One Sentence

같은 시뮬레이션 장면에 여러 지시를 배정해 의도를 제대로 골랐는지와 동작을 완수했는지를 각각 평가했다. 실물에서는 π0.5로 지시 일반화 파일럿을 수행했다. [PDF 3쪽](https://arxiv.org/pdf/2609.25636v1#page=3)

## Evaluation Type and Scope

주 평가는 시뮬레이션의 지시 분기 과제다. 실물 파일럿은 같은 물체 집합에서 학습 지시와 미관측 지시를 수행했다. [PDF 7쪽](https://arxiv.org/pdf/2609.25636v1#page=7)

## Dataset / Benchmark Role

장면만 보고 해야 할 행동을 맞히기 어렵게 같은 장면에 여러 유효한 지시를 붙였다. 실물 파일럿에서는 두 지시 집합의 집기·쌓기 조합도 달랐다. [PDF 3쪽](https://arxiv.org/pdf/2609.25636v1#page=3)

## Metrics and Success Definition

Intent Score는 단계별로 지시한 의미 대상의 선택을, Execution Score는 대응하는 동작의 성공을 측정한다. 실물 파일럿은 과제 성공 횟수를 보고했다. [PDF 5쪽](https://arxiv.org/pdf/2609.25636v1#page=5)

## Baselines and Fairness

실물 비교는 같은 π0.5를 사용했다. 두 지시 집합의 구성이 달라, 성공 횟수의 차이를 언어 지시의 새로움 하나에만 귀속할 수 없다. [PDF 7쪽](https://arxiv.org/pdf/2609.25636v1#page=7)

## Ablations and Sensitivity

시각적 배치 변화와 의미 구성을 바꾸는 시뮬레이션 평가 수준을 구분했다. 지시를 선택했지만 실제 집기가 실패한 경우에도 두 점수는 달라진다. [PDF 4쪽](https://arxiv.org/pdf/2609.25636v1#page=4)

## Generalization and Failure Cases

시각적으로 가능한 작업이 여러 개면 장면에 익숙하다는 이유만으로 지시한 작업을 선택할 수 없다. 실행 능력을 파악할 때는 의도 선택과 구분한다. [PDF 5쪽](https://arxiv.org/pdf/2609.25636v1#page=5)

## Statistics, Efficiency, and Reproducibility

실물에서 학습 지시 8개와 미관측 지시 8개를 각 5회 실행했다. 아래의 두 분모는 각각 40회다. [PDF 7쪽](https://arxiv.org/pdf/2609.25636v1#page=7)

## Proposed Evaluation — Researcher Interpretation

동일 scene·task 능력에서 지시만 바꿔 순응·실행 성공을 별도 측정한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openreview.net/forum?id=A9AQjk3dAt) · [저자 project/code](https://github.com/AutoLab-SAI-SJTU/RoboFollow). 이번 대조의 범위는 위 쪽수와 표에 명시했다.

## 조건별 성공률

실물 π0.5 파일럿은 학습 지시 8개와 미관측 지시 8개를 각각 5회 시험해 20/40회와 6/40회 성공했다. 두 지시 집합의 집기·쌓기 조합도 달랐다. [실물 파일럿 · PDF 7쪽](https://arxiv.org/pdf/2609.25636v1#page=7)
