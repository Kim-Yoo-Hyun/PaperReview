# EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video

> Evidence maturity: `ABSTRACT_CHECKED`.
> Source audit: 2026-11-16: 공식 초록·ICLR 목록·repository 확인. abstract 기반 — 본문 수동 확인 필요. 사용자 상태 UNREAD 유지.
> Canonical metadata: [01_overview.md](./01_overview.md).

## Paper-supported Conclusion

대규모 인간 조작의 영상·3D 손 궤적 자료와 예측 benchmark를 제공한다. [초록](https://arxiv.org/abs/2505.11709).

## Researcher Interpretation

RT-X류 robot data와 비교할 인간 데이터 전제이며 Ψ₀의 recipe 분석에 직접 필요하다. 서로 다른 embodiment의 데이터량을 프레임 수만으로 동일한 supervision이라고 보지 않는다.

## Minimal Reproduction and Falsifiable Question

고정 robot finetune budget에서 인간 사전학습 추가 여부와 retargeting 품질을 분리한다. 손 궤적 예측은 좋아져도 로봇 성공이 그대로라면 representation transfer 주장을 축소한다. 제안만 작성했고 실행하지 않았다.
