# Autonomous Improvement of Instruction Following Skills via Foundation Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

VLM으로 의미 있는 경험의 수집·평가를 돕고 언어 조건 이미지 목표 생성과 goal-reaching 정책을 분리하여 자율 데이터로 학습한다.

공식 abstract는 새로운 실세계 환경의 정책 개선과 5개 tabletop 환경에서 수집한 25K trajectory 데이터 공개를 설명한다. Project는 9개 평가 scene을 설명하므로 두 숫자의 분모를 합치지 않는다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/zhou25b.html) · [저자 project/code](https://soar-autonomous-improvement.github.io/) · [공식 code](https://github.com/soar-autonomous-improvement/code-release). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 수집 scene과 평가 scene의 분리, 데이터 release의 실제 접근성, 의미 이해와 운동 능력 개선의 기여, 서로 다른 정책 정보량은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

자율 수집·hindsight 학습의 시스템 선행. 단일 VLA 내부 RL과 분해된 image-goal 정책을 비교할 대조이며 fleet를 cross-embodiment로 오인하지 않게 한다.

### Dependency and Evolution

Goal-conditioned 학습·image subgoal 생성 → SOAR 자율 개선 → 단일 언어 조건 VLA 후학습과 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 원 경험·성공 판정·학습 예산을 고정하고 언어와 image-goal 감독의 추가 정보 차이를 먼저 감사한 뒤 지시 성공과 goal-reaching 성공을 분리 평가한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 자율 경험에서 직접 언어 재라벨 학습과 image-goal 재라벨 학습은 어떤 의미 구분·기본 운동 능력 조건에서 원 지시 전이가 다른가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
