# Emergence of Human to Robot Transfer in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Paper-supported conclusion

현재 근거는 [방법](./03_method.md)의 구성과 [평가](./04_evaluation.md)의 보고 범위다. 세부 수치·일반화 한계·재현 성공을 독립적으로 확인한 것은 아니다.

## Researcher interpretation

### Dependency and Evolution

Open X-Embodiment와 사람 영상 기반 로봇 학습을 잇는 NEXT 데이터 조건 연구다. Cross-embodiment 전이를 보편적 성질로 가정하지 않도록 비교 기준을 추가한다.

위 선행 연결은 개념적 비교이며 직접 citation 계보를 검증한 뜻은 아니다.

### Research Gap and Falsifiable Question

목표 robot 데이터량을 고정했을 때 human-data 이득의 변화는 scene/task 다양성과 embodiment 다양성을 각각 통제해도 남는가?

### Minimal Reproduction and Rejection Rule

먼저 사람 행동 supervision 생성·평가 task 중복을 확인한다. Robot 데이터량과 compute를 고정하고 사전학습의 task 다양성을 달리했을 때, 동일한 사람 시연 추가의 효과가 달라지는지 비교하는 설계를 제안한다. 데이터량·task 누출과 분리되지 않으면 다양성이 전이를 유발한다는 가설을 보류한다. 실제 재현·정책 비교는 미실행이며, 후속 실행은 호환 로컬 Docker에서 진행한다.
