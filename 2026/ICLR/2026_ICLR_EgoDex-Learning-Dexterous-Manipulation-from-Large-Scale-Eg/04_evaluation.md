# EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video

> Evidence maturity: `ABSTRACT_CHECKED`.
> Source audit: 2026-11-16: 공식 초록·ICLR 목록·repository 확인. abstract 기반 — 본문 수동 확인 필요. 사용자 상태 UNREAD 유지.
> Canonical metadata: [01_overview.md](./01_overview.md).

## Evaluation Type and Scope

DATASET / BENCHMARK. [초록](https://arxiv.org/abs/2505.11709)은829시간·194과제의 인간 조작 자료와 hand-trajectory 예측 평가를 제시한다.

## Dataset / Benchmark Role

[공식 repository](https://github.com/apple-aiml-research/ml-egodex)의725h train/7h test/97h additional은 초기 고정 split 뒤 추가 자료를 구분한다. 829h×30Hz의 규모는 약90M frames이며900M으로 기록하지 않는다.

## Metrics and Success Definition

Hand-trajectory 예측 지표를 robot success rate로 바꾸지 않는다. 정확한 metric 정의·수치는 본문 확인 필요.

## Baselines and Fairness

not recorded — 이번 검토는 초록/공개 data 안내 범위다. 로봇 downstream 비교에는 동일 retargeting·시연량·추가 label 접근권이 필요하다.

## Ablations and Sensitivity

not recorded — 본문 수동 확인 필요.

## Generalization and Failure Cases

자동 언어 오표기·손 추적 confidence·episode별 좌표계를 확인한다. Test/additional 자료를 섞어 평가 독립성을 주장하지 않는다.

## Statistics, Efficiency, and Reproducibility

데이터·loader·benchmark code 공개 확인. 로컬 데이터 다운로드·학습·실험은 미실행이며 full training recipe 재현성은 미확인.
