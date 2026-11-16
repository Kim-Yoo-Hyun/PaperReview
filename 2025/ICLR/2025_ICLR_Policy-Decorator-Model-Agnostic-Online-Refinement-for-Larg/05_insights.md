# Policy Decorator: Model-Agnostic Online Refinement for Large Policy Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Paper-supported conclusion

동결 base 위에 SAC residual을 학습하고 residual 범위와 탐색 진행을 제어한다.

Final paper의 지정 절만 검토했고 전체 36쪽 정독은 아니다. 공식 code 링크/README 확인과 실행 검증을 구분한다.

근거: [지정 본문](https://proceedings.iclr.cc/paper_files/paper/2025/file/45c361d4117d598d4bb6568b407e9ac9-Paper-Conference.pdf) — final paper §4.1–4.3, selected Appendix B.5; project/code README.

## Researcher interpretation

### Novelty and Dependency

Frozen large policy+bounded residual의 핵심 비교 선행이다. 현재 후보의 scalar gain·탐색 schedule이라는 단순 대안을 놓치지 않도록 NEXT에 추가한다.

개념 비교: DDPG/SAC·imitation → residual policy refinement → VLA 후학습/독립 base 업데이트. 직접 citation edge를 새로 확정한 것은 아니다.

### Fragile Assumption

초기 base 능력과 적절한 residual 크기·탐색 schedule이 학습에 중요하다. 이는 후속 비교에서 점검할 조건이며 새로 관측한 실패가 아니다.

### Falsifiable Research Question

Base 업데이트 뒤 보정량만 재조정해도 이전 residual을 충분히 재사용할 수 있는가?

### Minimal Comparison and Revise Rule

연구자 제안: 원 residual·0 residual·scalar gain과 fresh residual을 먼저 비교하고 제어 주기/환경 상호작용 수를 맞춘다.

단순 gain·새 critic·동일 데이터 모방으로 설명되는 차이는 그 범위로 결론을 줄인다. 의미 있는 차이가 없으면 독립 방법 기여를 주장하지 않는다. 실행 실패·미실행은 연구 가설의 반증과 구분한다.
