# Cal-QL: Calibrated Offline RL Pre-Training for Efficient Online Fine-Tuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Source-Supported Evaluation Scope

Offline-to-online fine-tuning benchmark를 비교한다. 모든 VLA 보존 문제를 해결했다고 해석하지 않는다.

## Metrics, Baselines, and Generalization

reference return·보수성·초기 탐색·데이터 혼합·성능 회복 비용.

정확한 dataset/split·trial 수·baseline budget·metric 정의·ablation 수치는 이번 초록 정리에서 확정하지 않았다. 이는 원문에 미보고됐다는 뜻이 아니다.

## Reproducibility and Limitations

공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.

공개 code/project가 있어도 실행 재현을 뜻하지 않는다. 실제 로봇·simulation·이론/survey의 범위를 위 평가 설명대로 구별한다.

## Proposed Comparison — Researcher Interpretation

같은 actor 초기화에서 critic calibration만 바꾸고 초반 task별 성공·value scale을 비교한다.

아직 실행하지 않았으며 예상 이득을 측정 결과로 기록하지 않는다.

## Evidence

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2023/hash/c44a04289beaf0a7d968a94066a1d696-Abstract-Conference.html). Code/project·확인 날짜는 [overview](./01_overview.md)를 따른다.
