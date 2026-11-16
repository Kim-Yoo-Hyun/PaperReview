# EXPO: Stable Reinforcement Learning with Expressive Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Paper-supported conclusion

Expressive base의 imitation 업데이트와 Gaussian edit 정책의 Q 기반 업데이트를 결합하고, base/edit 행동을 value로 선택한다.

공개 code를 읽었지만 실행하지 않았다. Co-adaptation 결과를 독립 base release 교체 후 동결 editor의 전이 근거로 확대하지 않는다.

근거: [지정 본문](https://arxiv.org/html/2507.07986v3) — §4 / Algorithm 1; expo_learner.py selected update paths. Code 검토 revision: `bbd571306b413e05d5d4b01a6efa20352c2b891a`; 실행하지 않았다.

## Researcher interpretation

### Novelty and Dependency

Residual/editor와 value 선택을 결합한 강한 직접 baseline이다. Q 선택·base 모방·editor RL이라는 조합 자체의 신규성 주장을 막는 NEXT다.

개념 비교: DDPG/SAC·imitation → residual policy refinement → VLA 후학습/독립 base 업데이트. 직접 citation edge를 새로 확정한 것은 아니다.

### Fragile Assumption

Q 값이 base/edit 후보 선택에 유용해야 하며 base와 editor가 함께 적응하는 학습 분포를 전제한다. 이는 후속 비교에서 점검할 조건이며 새로 관측한 실패가 아니다.

### Falsifiable Research Question

독립적인 base 교체 후 actor 재사용의 이득은 EXPO식 value 선택과 동일 old-data 재학습을 넘어서는가?

### Minimal Comparison and Revise Rule

연구자 제안: co-adaptation과 독립 교체를 분리하고 base-only·warm-start·fresh editor·value 선택의 입력과 새 환경 상호작용 예산을 맞춘다.

단순 gain·새 critic·동일 데이터 모방으로 설명되는 차이는 그 범위로 결론을 줄인다. 의미 있는 차이가 없으면 독립 방법 기여를 주장하지 않는다. 실행 실패·미실행은 연구 가설의 반증과 구분한다.
