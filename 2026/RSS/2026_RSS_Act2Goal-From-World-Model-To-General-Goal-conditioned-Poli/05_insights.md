# Act2Goal: From World Model To General Goal-conditioned Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

목표 조건부 world model의 미래 영상과 multi-scale temporal hashing을 action expert에 연결하고 hindsight goal relabeling으로 적응한다.

시뮬레이션·실물 장시간 조작과 보상 없는 online 적응을 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p015.html). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

Hindsight 목표 변경·world model·단일 정책 연결의 직접 선행이며 언어 VLA와 시각 목표 정책의 경계를 드러낸다.

### Dependency and Evolution

UVFA/HER·world model → Act2Goal → HINDSIGHT 후보의 relabeling 효과 분해.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

시각 목표 접근·hindsight 도달 상태·LoRA 갱신 범위·online 비용.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

동일 rollout에서 원 목표·hindsight 목표·성공 subset 모방을 같은 update 수로 비교한다.

### Falsifiable Question

목표 relabeling의 이득은 더 많은 성공 상태 모방만으로 설명되는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. RSS 공식 abstract를 기준으로 기록. Project는 접근되지만 이번 웹 도구에서 본문을 읽지 못해 코드 공개 상태는 not identified다. Visual-goal 정책을 언어 지시 VLA와 동일시하지 않는다.
