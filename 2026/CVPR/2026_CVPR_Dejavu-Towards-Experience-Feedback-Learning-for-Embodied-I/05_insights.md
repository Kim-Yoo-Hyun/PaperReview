# Dejavu: Towards Experience Feedback Learning for Embodied Intelligence

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Paper-supported conclusion

현재 근거는 [방법](./03_method.md)의 구성과 [평가](./04_evaluation.md)의 보고 범위다. 세부 수치·일반화 한계·재현 성공을 독립적으로 확인한 것은 아니다.

## Researcher interpretation

### Dependency and Evolution

Residual RL과 retrieval의 직접 결합이므로 NEXT에 추가한다. Bank 성장·frozen backbone이라는 조합 자체를 새 연구 공백으로 주장하지 않도록 현재 후보의 선행 경계를 보완한다.

위 선행 연결은 개념적 비교이며 직접 citation 계보를 검증한 뜻은 아니다.

### Research Gap and Falsifiable Question

목표 경험을 고정하고 다른 목표 경험만 추가해도 EFN의 이득이 남는가, 아니면 성공 데이터 선택과 학습된 residual이 설명하는가?

### Minimal Reproduction and Rejection Rule

먼저 EFN의 학습/배포 갱신 경계와 success-only bank·task filter를 확인한다. 같은 경험 bank에서 검색만 사용한 대안, residual만 사용한 대안, 둘을 결합한 구성을 비교하는 진단을 제안한다. 결합 이득이 없으면 기억과 residual의 상호작용을 새로운 기여로 주장하지 않는다. 실제 재현·정책 비교는 미실행이며, 후속 실행은 호환 로컬 Docker에서 진행한다.
