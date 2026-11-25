# Insights — IMPACT-VLA: Interaction-aware Multimodal Propagation Attribution via Counterfactual Trajectories for Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-24에 확인한 저자 본문 §III–IV에 근거한다.

## Paper-supported conclusion

입력 대체 뒤 즉시 명령이 얼마나 달라지는지와 끝까지 실행했을 때의 성공 기여는 다른 순위를 낼 수 있다. 과제 성공이 회복된 경로가 참조 손끝 경로로 돌아오는 것도 별도 현상이다. [저자 §IV-D·E](https://arxiv.org/html/2609.15005v1#S4)

## Researcher interpretation

OpenVLA-OFT와 LIBERO를 연결한 이 평가는 폐루프에서 입력 중요도를 따진다는 주장의 직접 비교 기준이다. WidowX에서는 물리적 물체 이동과 한 프레임의 테이블 외관을 교차하고, 첫 명령의 이동과 회전을 바꿔 최종 배치를 측정할 수 있다. 참조 행동 구간 전체의 입력을 교체하는 저자 실험과 개입 단위가 다르다.

다음 연구에서 검증할 수 있는 질문은 새 영상이 필요한 상태를 사전에 구별해, 늘 새 영상을 쓰거나 한 번 대기하는 방식보다 제한된 재관측 예산에서 실제 배치를 개선하는가이다. 이 질문을 평가하려면 결과를 보지 않고 고른 과제와 동일 비용의 기본 정책이 필요하다. [WidowX 대조 결과](../../../work/research_topics/RESULTS.md#visual-feedback)
