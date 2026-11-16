# Accelerating Residual Reinforcement Learning With Uncertainty Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Paper-supported conclusion

불확실성 기반 탐색 제어를 사용한다. 확인한 critic 구현은 base와 residual이 합쳐진 최종 행동을 평가한다.

IEEE 직접 페이지는 접근 제약이 있어 publisher-deposited Crossref와 저자 accepted 표기로 RA-L 11(1), 2026을 확인했다. 2025 DOI/채택일을 issue 연도와 혼동하지 않는다.

근거: [지정 본문](https://arxiv.org/html/2506.17564v2) — v2 IV-B / V-D; assymetric_sac.py critic_loss_fn/actor complete-action path. Code 검토 revision: `8125f33dcf490d4cf93d57a27d3e1963a47f52ea`; 실행하지 않았다.

## Researcher interpretation

### Novelty and Dependency

현재 후보의 critic mismatch 대안을 검토할 직접 선행이다. 합성 행동 critic을 새 알고리즘으로 재주장하지 않도록 NEXT에 등록한다.

개념 비교: DDPG/SAC·imitation → residual policy refinement → VLA 후학습/독립 base 업데이트. 직접 citation edge를 새로 확정한 것은 아니다.

### Fragile Assumption

불확실성 추정과 탐색 필요성이 관련되어야 한다. Actor 입력 변화와 critic 오차는 별도로 통제해야 한다. 이는 후속 비교에서 점검할 조건이며 새로 관측한 실패가 아니다.

### Falsifiable Research Question

독립 base 교체 후 나타난 차이는 residual actor의 부적합인가, critic 재교정만으로 해소되는가?

### Minimal Comparison and Revise Rule

연구자 제안: 새 critic·공통 replay를 모든 재사용 대조군에 적용하고 actor 보존/재초기화와 uncertainty/gain 대안을 구분한다.

단순 gain·새 critic·동일 데이터 모방으로 설명되는 차이는 그 범위로 결론을 줄인다. 의미 있는 차이가 없으면 독립 방법 기여를 주장하지 않는다. 실행 실패·미실행은 연구 가설의 반증과 구분한다.
