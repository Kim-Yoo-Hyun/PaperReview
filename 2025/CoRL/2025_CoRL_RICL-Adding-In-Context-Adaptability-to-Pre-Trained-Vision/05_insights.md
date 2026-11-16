# RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Paper-supported conclusion

현재 근거는 [방법](./03_method.md)의 구성과 [평가](./04_evaluation.md)의 보고 범위다. 세부 수치·일반화 한계·재현 성공을 독립적으로 확인한 것은 아니다.

## Researcher interpretation

### Dependency and Evolution

OpenVLA·π0 계열의 후학습과 시연 검색을 잇는 직접 선행이다. 현재 bank 확장 질문에서 이미 알려진 ICL 능력·검색 이득을 신규성으로 재주장하지 않도록 NEXT로 등록한다.

위 선행 연결은 개념적 비교이며 직접 citation 계보를 검증한 뜻은 아니다.

### Research Gap and Falsifiable Question

같은 target 시연과 policy를 유지할 때 다른 목표 시연의 추가가 기존 과제 결과에 주는 변화는 task별 검색으로 제거되는가?

### Minimal Reproduction and Rejection Rule

먼저 시연 구간·action interpolation·task split·검색 query를 원문과 맞춘다. 같은 시연 개수와 입력 token 예산에서 무작위 시연과 검색 시연을 비교하는 작은 paired 진단을 제안한다. Target support나 길이만으로 차이가 설명되면 검색 방식의 고유한 이득이라는 해석을 축소한다. 실제 재현·정책 비교는 미실행이며, 후속 실행은 호환 로컬 Docker에서 진행한다.
