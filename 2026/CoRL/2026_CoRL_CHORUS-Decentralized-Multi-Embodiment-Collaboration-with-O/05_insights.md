# Insights — CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Paper-supported conclusion

서로 다른 로봇이 공유 관측·통신 없이 함께 조작하는 문제.에 대한 접근은 [method](./03_method.md), 지지하는 실험 범위는 [evaluation](./04_evaluation.md)에서 확인한다. 지정 절의 결과를 읽었으며 재현하거나 일반적인 우월성을 검증한 것은 아니다.

근거: [확인한 원문](https://arxiv.org/html/2606.12352v1), §3.1–3.3, §4.2, §5 limitations.

## Researcher interpretation

CROSSPLAY에서 여러 embodiment·local-only 협력 자체를 새 기여로 주장하지 않도록 하는 직접 선행.

개념 연결: π0.5·LatentToM → shared decentralized VLA → independent partner 평가.

- 취약 조건 점검: 연구자 점검: task의 관련 정보가 각 로봇 관측에 실제로 보이는지 확인한다.
- 반증 가능한 질문: 같은 공유 모델 복제 대신 독립적으로 후학습한 두 copy를 결합하면 협력 이득이 유지되는가?
- 최소 비교 제안: 같은 관측 접근권·motor competence에서 self-play/cross-play, 고정 역할·ready signal을 비교한다.

이 비교는 연구자 제안이며 논문이 이미 수행한 실험이나 새 기여의 입증이 아니다. 현재 evidence maturity는 `CURATION-HYPOTHESIS`다.
