# Insights — Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Paper-supported conclusion

낮은 action reconstruction error가 좋은 autoregressive robot policy를 보장하지 않는 문제.에 대한 접근은 [method](./03_method.md), 지지하는 실험 범위는 [evaluation](./04_evaluation.md)에서 확인한다. 지정 절의 결과를 읽었으며 재현하거나 일반적인 우월성을 검증한 것은 아니다.

근거: [확인한 원문](https://arxiv.org/pdf/2610.09170v1), §1, §4, §6, Appendix B.2/C.3.

## Researcher interpretation

CODEC1의 broad motivation과 prefix/replanning confound를 가장 직접적으로 제한하는 선행.

개념 연결: RT-2·FAST·OAT → ProAct → executed-prefix selection 진단.

- 취약 조건 점검: 연구자 점검: reconstruction 숫자만으로 learned policy 성공을 추정하지 않는다.
- 반증 가능한 질문: 고정 H·rate·normalizer에서 실행 prefix metric이 실제 codec 선택을 유용하게 바꾸는가?
- 최소 비교 제안: Tokenizer-free control과 policy-generated token error를 함께 두고 held-out episode에서 full-chunk/prefix 선택의 행동 차이를 비교한다.

이 비교는 연구자 제안이며 논문이 이미 수행한 실험이나 새 기여의 입증이 아니다. 현재 evidence maturity는 `CURATION-HYPOTHESIS`다.
