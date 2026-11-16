# Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?

> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

- Year/Venue: 2026 / arXiv
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, action-tokenization, autoregressive-policy, control-horizon
- Official paper: https://arxiv.org/abs/2610.09170
- Venue verification: main-conference acceptance unverified; preprint으로 등록
- Code/Project: https://ripl.github.io/action-tokenization-web/proact/
- Code: not_released
- Source audit: 2026-11-05: §1, §4, §6, Appendix B.2/C.3. 지정 본문 절만 확인; 전체 정독·수식 검증 아님. Venue와 읽은 preprint version을 구별. Native 실행 0; 사용자 읽기 UNREAD.

## Problem and Contribution

낮은 action reconstruction error가 좋은 autoregressive robot policy를 보장하지 않는 문제.

Token predictability와 예측 오류 후 decoding robustness를 보완하는 tokenizer 학습을 제안한다.

## Scope and Limitation

일반 reconstruction/control 불일치와 horizon 효과는 이미 다룬다. Code soon으로 표기되어 실행 검증되지 않았다. 저자 NeurIPS 표기는 exact 공식 listing을 확인하지 못해 arXiv 유지.

## Why This Paper Is Here — Researcher Interpretation

CODEC1의 broad motivation과 prefix/replanning confound를 가장 직접적으로 제한하는 선행.

입력·행동은 [method](./03_method.md), 실제 평가 범위는 [evaluation](./04_evaluation.md)을 따른다. 자동 노트는 사용자의 읽기 완료 기록이 아니다.

근거: [확인한 원문](https://arxiv.org/pdf/2610.09170v1), §1, §4, §6, Appendix B.2/C.3.
