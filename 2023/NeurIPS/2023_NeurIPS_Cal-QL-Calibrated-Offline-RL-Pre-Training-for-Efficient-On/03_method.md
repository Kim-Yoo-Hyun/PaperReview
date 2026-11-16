# Cal-QL: Calibrated Offline RL Pre-Training for Efficient Online Fine-Tuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Method and Contribution

Conservative value의 scale을 reference policy 가치와 정렬하여 online 갱신에 유용한 초기화를 학습한다.

## Observation, State, and Action

Offline data → calibrated conservative critic·정책 → online fine-tuning.

## Objective and Training / Inference Boundary

초록에서 확인한 학습 구성이다. 정확한 loss·gradient 경로·학습/추론 차이·controller 또는 memory 시간 단위는 본문 확인이 필요하다.

점검 항목: reference return·보수성·초기 탐색·데이터 혼합·성능 회복 비용.

## Method-Specific Comparison — Researcher Interpretation

같은 actor 초기화에서 critic calibration만 바꾸고 초반 task별 성공·value scale을 비교한다.

이 비교는 제안이며 실행 결과나 논문의 ablation이 아니다.

## Evidence Boundary

[공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2023/hash/c44a04289beaf0a7d968a94066a1d696-Abstract-Conference.html). 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
