# EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video

> Evidence maturity: `ABSTRACT_CHECKED`.
> Source audit: 2026-11-16: 공식 초록·ICLR 목록·repository 확인. abstract 기반 — 본문 수동 확인 필요. 사용자 상태 UNREAD 유지.
> Canonical metadata: [01_overview.md](./01_overview.md).

## Data Interface

[공식 repository](https://github.com/apple-aiml-research/ml-egodex): RGB1080p/30Hz, HDF5의3D transforms·tracking confidence·언어 annotations. 좌표계는 recording의 ARKit origin이며 recording 사이 동일 world frame이 아니다.

## Labels and Training Boundary

언어는 자동 생성 자료를 포함해 방향/행동 설명 오류가 가능하다. 공개 loader·benchmark 도구와 모든 학습 설정의 재현 가능성을 구분한다. 논문 objective·모델·loss 상세는 본문 확인 필요.
