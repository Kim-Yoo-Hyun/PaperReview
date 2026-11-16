# Scaling up Memory for Robotic Control via Experience Retrieval

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Paper-supported conclusion

현재 근거는 [방법](./03_method.md)의 구성과 [평가](./04_evaluation.md)의 보고 범위다. 세부 수치·일반화 한계·재현 성공을 독립적으로 확인한 것은 아니다.

## Researcher interpretation

### Dependency and Evolution

MemoryVLA와 계층 정책의 관계를 구체화하는 NEXT다. 외부 시연 검색과 실행 중 기억을 구분하고 SET의 counting 선행을 보완한다.

위 선행 연결은 개념적 비교이며 직접 citation 계보를 검증한 뜻은 아니다.

### Research Gap and Falsifiable Question

동일한 이력 접근과 입력 token 예산에서 선택 keyframe의 이득은 단순 시간 subsampling 이후에도 남는가?

### Minimal Reproduction and Rejection Rule

먼저 선택 supervision·실패 후 이력 분포를 확인하고 proceedings의 Qwen 7B와 project의 3B 중 대상 version을 확정한다. 같은 frame 수에서 최근 관측만 사용하는 경우와 과거 관측을 검색하는 경우를 비교한다. 최근 frame 예산을 맞추면 차이가 사라지는지 확인한다. 실제 재현·정책 비교는 미실행이며, 후속 실행은 호환 로컬 Docker에서 진행한다.
