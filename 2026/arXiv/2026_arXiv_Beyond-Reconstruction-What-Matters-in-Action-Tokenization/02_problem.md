# Problem — Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Target Problem

낮은 action reconstruction error가 좋은 autoregressive robot policy를 보장하지 않는 문제.

## Robotics Loop

Action chunk → discrete code → AR prediction → decoded control. Prediction horizon과 실제 execution horizon을 구분한다.

## Assumptions to Check — Researcher Interpretation

연구자 점검: reconstruction 숫자만으로 learned policy 성공을 추정하지 않는다.

개념 연결: RT-2·FAST·OAT → ProAct → executed-prefix selection 진단.

## Boundary

일반 reconstruction/control 불일치와 horizon 효과는 이미 다룬다. Code soon으로 표기되어 실행 검증되지 않았다. 저자 NeurIPS 표기는 exact 공식 listing을 확인하지 못해 arXiv 유지.

근거: [확인한 원문](https://arxiv.org/pdf/2610.09170v1), §1, §4, §6, Appendix B.2/C.3.
