# AWAC: Accelerating Online Reinforcement Learning with Offline Datasets

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Source-Supported Evaluation Scope

시뮬레이션과 실제 다지 손·서랍 열기·밸브 조작을 평가한다.

## Metrics, Baselines, and Generalization

advantage scale·weight clipping·replay 비율·새 데이터 수집 비용.

정확한 dataset/split·trial 수·baseline budget·metric 정의·ablation 수치는 이번 초록 정리에서 확정하지 않았다. 이는 원문에 미보고됐다는 뜻이 아니다.

## Reproducibility and Limitations

저자 project·arXiv v6 확인. OpenReview forum은 browser challenge로 본문 접근 실패했고 공식 acceptance를 확인하지 못해 arXiv 2020으로 등록한다. Project의 code 링크는 식별했으나 해당 경로 직접 fetch는 실패했다.

공개 code/project가 있어도 실행 재현을 뜻하지 않는다. 실제 로봇·simulation·이론/survey의 범위를 위 평가 설명대로 구별한다.

## Proposed Comparison — Researcher Interpretation

데이터·초기 정책·학습량을 맞춰 BC·success-only BC·AWAC·online RL을 대조한다.

아직 실행하지 않았으며 예상 이득을 측정 결과로 기록하지 않는다.

## Evidence

[공식 paper/abstract](https://arxiv.org/abs/2006.09359). Code/project·확인 날짜는 [overview](./01_overview.md)를 따른다.
