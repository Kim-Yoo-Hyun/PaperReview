# Insights — RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Paper-supported conclusion

Reward 중심 후학습이 관측·실행 교란에 대한 강건성을 충분히 다루지 못하는 문제.에 대한 접근은 [method](./03_method.md), 지지하는 실험 범위는 [evaluation](./04_evaluation.md)에서 확인한다. 지정 절의 결과를 읽었으며 재현하거나 일반적인 우월성을 검증한 것은 아니다.

근거: [확인한 원문](https://arxiv.org/html/2511.01331v2), v2 §4.2–4.3, Algorithm 1; §5 범위.

## Researcher interpretation

FEEDBACK에서 단순 Jacobian 억제·강건 RL을 새 방법으로 제안하지 않도록 하는 직접 비교.

개념 연결: PPO → RL4VLA → robustness-aware post-training.

- 취약 조건 점검: 연구자 점검: 일반 nuisance regularization을 semantic-change 보존으로 해석하지 않는다.
- 반증 가능한 질문: 관측 민감도를 줄이는 정규화가 task-relevant 상태 변화에 필요한 반응까지 약화시키는 조건은 있는가?
- 최소 비교 제안: 같은 data/budget에서 PPO·RobustVLA·동일 데이터 BC를 clean/nuisance/physical-change 조건으로 대조한다.

이 비교는 연구자 제안이며 논문이 이미 수행한 실험이나 새 기여의 입증이 아니다. 현재 evidence maturity는 `CURATION-HYPOTHESIS`다.
