# Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Paper-supported conclusion

Object pose·proprioception·base action을 residual 입력으로 사용하며, paired teleoperation을 통한 정렬과 simulation 학습을 결합한다.

CoRL 공식 accepted list에서 exact title/forum을 확인했다. 읽은 것은 arXiv v1이며 final paper 동등성과 공식 학습 code 공개는 미확인이다.

근거: [지정 본문](https://arxiv.org/html/2606.18953v1) — §3.1–3.4/5.1–5.4/7, Appendix A.

## Researcher interpretation

### Novelty and Dependency

Object-centric residual의 전이를 이미 다룬 직접 충돌 선행이다. 다양한 로봇·base 갱신 전이와 sim-to-real 전이를 구분할 NEXT다.

개념 비교: DDPG/SAC·imitation → residual policy refinement → VLA 후학습/독립 base 업데이트. 직접 citation edge를 새로 확정한 것은 아니다.

### Fragile Assumption

정렬된 object pose와 행동 표현이 residual 배포에 유효해야 한다. 센서 추가와 base 교체 효과를 혼동하지 않는다. 이는 후속 비교에서 점검할 조건이며 새로 관측한 실패가 아니다.

### Falsifiable Research Question

Object-centric 상태를 유지해도 base 행동 분포가 바뀌면 기존 residual의 이득은 유지되는가?

### Minimal Comparison and Revise Rule

연구자 제안: 같은 로봇·관측·상태 추정기를 고정하고 base만 교체해 base-only·동결 residual·gain 조정부터 비교한다.

단순 gain·새 critic·동일 데이터 모방으로 설명되는 차이는 그 범위로 결론을 줄인다. 의미 있는 차이가 없으면 독립 방법 기여를 주장하지 않는다. 실행 실패·미실행은 연구 가설의 반증과 구분한다.
