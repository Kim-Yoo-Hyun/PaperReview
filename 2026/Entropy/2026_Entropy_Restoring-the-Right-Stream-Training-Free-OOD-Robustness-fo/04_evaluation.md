# Restoring the Right Stream: Training-Free OOD Robustness for Vision–Language–Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> Source audit: 2026-11-24에 아래 쪽수의 평가 설정과 결과를 대조했다.

## Evaluation in One Sentence

1,120개 새 인스턴스에서 상태 입력 보정 후 초기 자세 교란의 성공률은 23.8%에서 28.7%로 변했다(Holm 보정 p=0.287). 보정이 활성화되는 별도의 600개 확인 표본에서는 26.3%에서 32.2%로 변했다. [PDF 10쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=10) · [PDF 12쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=12)

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.

OpenVLA-OFT에 대한 LIBERO-Plus 교란 실험. 표 1은 기존 짝지은 평가, 표 2는 새 인스턴스에서의 블라인드 평가다. [PDF 9쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=9) · [PDF 10쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=10)

## Dataset / Benchmark Role

LIBERO-Plus의 초기 로봇 자세와 시점 등 교란 유형을 평가에 사용했다. [PDF 9쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=9) · [PDF 10쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=10)

## Metrics and Success Definition

동일 인스턴스에서 측정한 작업 성공률과 조건별 차이를 비교했다. 초기 자세 교란과 전체 교란 평균을 따로 보고한다. [PDF 9쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=9) · [PDF 10쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=10)

## Baselines and Fairness

고정된 원래 정책과 시각 보정·상태 보정·결합 보정을 같은 과제 인스턴스에서 비교했다. [PDF 9쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=9) · [PDF 10쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=10)

## Ablations and Sensitivity

표 2에서 시각 보정만 적용한 경우, 상태 보정만 적용한 경우와 둘을 함께 적용한 경우를 같은 교란에서 비교한다. [PDF 10쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=10)

## Generalization and Failure Cases

기존 평가와 겹치지 않는 블라인드 표본과 보정 활성 조건의 확인 표본으로 나누었다. 각각의 결과는 해당 표본 조건에서 해석한다. [PDF 10쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=10) · [PDF 12쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=12)

## Statistics, Efficiency, and Reproducibility

- 표 2는 대응 인스턴스의 부트스트랩 구간과 다중비교 보정 p값을 보고한다. [PDF 10쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=10)
- 표 3에서 별도로 모집한 600개 초기 자세 교란은 보정이 활성화되는 조건이다. 이 표본의 성공률은 26.3%에서 32.2%로 변했다. [PDF 12쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=12)

## Proposed Evaluation — Researcher Interpretation

물리적 이동과 state reporting offset을 나누어 보정의 이득·손해를 비교한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

LIBERO-Plus의 대응 시행과 별도로 확보한 새 인스턴스에서 시각 보정, 상태 보정 및 결합 보정의 결과를 비교했다. [PDF 9쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=9) · [PDF 10쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=10) · [PDF 11쪽](https://mdpi-res.com/d_attachment/entropy/entropy-28-00975/article_deploy/entropy-28-00975.pdf#page=11)
