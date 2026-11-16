# Insights — Cooperative Multi-Agent Vision-Language-Action Models via Reinforced Fine Tuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Paper-supported conclusion

단일 로봇 사전학습 VLA에 협력 기술을 부여하고 시연 이상의 성능으로 개선한다.에 대한 접근은 [method](./03_method.md), 지지하는 실험 범위는 [evaluation](./04_evaluation.md)에서 확인한다. 지정 절의 결과를 읽었으며 재현하거나 일반적인 우월성을 검증한 것은 아니다.

근거: [확인한 원문](https://arxiv.org/html/2609.36588v1), §4.2–4.3, §5, Appendix C.1.

## Researcher interpretation

CROSSPLAY에서 VLA+MARL 결합 자체의 신규성을 배제하는 가장 가까운 RL 선행.

개념 연결: CHORUS·latent-space RL → cooperative RFT → independent partner compatibility.

- 취약 조건 점검: 연구자 점검: 팀 전체 성공과 agent별 credit 추정을 동일시하지 않는다.
- 반증 가능한 질문: Co-adaptation의 성능 이득과 낯선 partner에 대한 호환성 사이에 trade-off가 있는가?
- 최소 비교 제안: motor ability·shared-view access·데이터를 맞추고 joint RL, independent RL, population training의 partner matrix를 비교한다.

이 비교는 연구자 제안이며 논문이 이미 수행한 실험이나 새 기여의 입증이 아니다. 현재 evidence maturity는 `CURATION-HYPOTHESIS`다.
