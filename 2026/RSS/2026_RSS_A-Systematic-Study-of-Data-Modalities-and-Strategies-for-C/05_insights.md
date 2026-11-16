# A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Paper-supported conclusion

현재 근거는 [방법](./03_method.md)의 구성과 [평가](./04_evaluation.md)의 보고 범위다. 세부 수치·일반화 한계·재현 성공을 독립적으로 확인한 것은 아니다.

## Researcher interpretation

### Dependency and Evolution

Open X-Embodiment·DataMIL·ReMix 이후 데이터 양과 종류의 효과를 분리하는 NEXT 실증 기준이다. 새로운 아키텍처보다 데이터 구성이라는 단순 대안을 먼저 검토하게 한다.

위 선행 연결은 개념적 비교이며 직접 citation 계보를 검증한 뜻은 아니다.

### Research Gap and Falsifiable Question

동일 robot-data·학습 compute 예산에서 추가 modality의 이득은 언어 grounding 개선과 action coverage 확대 중 어느 조건에 따라 달라지는가?

### Minimal Reproduction and Rejection Rule

먼저 modality별 token/compute 균형·학습 단계·task split을 확인한다. 같은 총 학습 예산에서 robot-only와 한 가지 추가 modality를 사용하는 경우를 비교하고, 추가 데이터를 주는 단계의 영향을 분리한다. 단순 compute 증가로 설명되는 결과는 modality 자체의 이득으로 해석하지 않는다. 실제 재현·정책 비교는 미실행이며, 후속 실행은 호환 로컬 Docker에서 진행한다.
