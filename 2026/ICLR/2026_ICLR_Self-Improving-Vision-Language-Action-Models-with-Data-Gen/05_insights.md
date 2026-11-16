# Self-Improving Vision-Language-Action Models with Data Generation via Residual RL

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Paper-supported conclusion

동결 VLA 위에 residual specialist를 학습하고, 배포 조건을 고려한 hybrid rollout에서 얻은 데이터를 generalist의 supervised fine-tuning에 사용한다.

ICLR 공식 program의 채택과 읽은 arXiv v1을 구별한다. 최종본 동등성·동일 residual의 반복 base 갱신 전이·공식 전체 학습 code는 확인하지 않았다.

근거: [지정 본문](https://arxiv.org/html/2511.00091v1) — §3, Appendix B.2/C.1/C.2.

## Researcher interpretation

### Novelty and Dependency

VLA의 residual 개선→데이터 생성→base 갱신을 잇는 직접 선행이다. 현재 후보에서 이 루프 자체를 새 기여로 주장하지 않도록 NEXT에 추가한다.

개념 비교: DDPG/SAC·imitation → residual policy refinement → VLA 후학습/독립 base 업데이트. 직접 citation edge를 새로 확정한 것은 아니다.

### Fragile Assumption

Specialist가 개선한 행동과 데이터 수집 분포가 후학습에 유용해야 한다. Base가 바뀐 뒤 이전 residual의 호환성은 별도 질문이다. 이는 후속 비교에서 점검할 조건이며 새로 관측한 실패가 아니다.

### Falsifiable Research Question

독립적으로 업데이트된 base에 이전 residual을 유지할 때, 새로운 residual 학습보다 이득이 남는 조건은 무엇인가?

### Minimal Comparison and Revise Rule

연구자 제안: 먼저 base 갱신 전후 action/normalizer와 residual 입력을 대조하고 frozen residual·gain 조정·fresh residual을 동일 새 데이터 예산으로 비교한다.

단순 gain·새 critic·동일 데이터 모방으로 설명되는 차이는 그 범위로 결론을 줄인다. 의미 있는 차이가 없으면 독립 방법 기여를 주장하지 않는다. 실행 실패·미실행은 연구 가설의 반증과 구분한다.
