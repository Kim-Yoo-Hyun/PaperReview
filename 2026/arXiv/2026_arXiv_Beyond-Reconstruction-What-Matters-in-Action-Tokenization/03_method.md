# Method — Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Pipeline and Learning Rule

Token predictability와 예측 오류 후 decoding robustness를 보완하는 tokenizer 학습을 제안한다.

## Observation, State and Action

Action chunk → discrete code → AR prediction → decoded control. Prediction horizon과 실제 execution horizon을 구분한다.

## Temporal and Implementation Boundary

Control rate, action horizon, optimizer 전체 설정·checkpoint 호환성은 이번 노트에서 확정하지 않았다. 확인한 pipeline과 source 절을 넘어 수식·실행 가능성을 추정하지 않는다. Code URL의 존재는 native 실행 검증이 아니다.

근거: [확인한 원문](https://arxiv.org/pdf/2610.09170v1), §1, §4, §6, Appendix B.2/C.3.
