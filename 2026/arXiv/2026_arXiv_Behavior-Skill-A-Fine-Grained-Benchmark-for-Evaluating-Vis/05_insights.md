# Behavior-Skill: A Fine-Grained Benchmark for Evaluating Vision-Language-Action Policies in Long-Horizon Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

시연을 실행 가능한 skill로 나누고 instruction·observation/action segment·복원 가능한 중간 상태·skill 성공 조건을 연결하여 개별 skill 평가를 지원한다.

50개 household task의 시연으로 구성한 benchmark에서 π0.5와 GR00T 등 정책을 평가한다. 복원된 유효 시작 상태의 개별 능력은 이전 정책이 실제 도달한 상태에서의 연결 실행 성능과 구분한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2608.30536) · [저자 project/code](https://github.com/nubot-nudt/Behavior-Skill). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 공개 release와 논문 정책 쌍의 일치, 시연 reset과 continuation의 차이, 학습/평가 instance 분리, normalizer와 controller·queue·종료 정의은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

현재 HANDOFF P0의 직접적인 benchmark/source prerequisite다. 전체 task 성공률과 독립 skill 능력의 차이를 읽을 NEXT로 추가하되 preprint status를 유지한다.

### Dependency and Evolution

BEHAVIOR-1K → 중간 skill 상태 복원·평가; π0.5/GR00T → skill별 능력 비교; Mobile ALOHA/MoTo → 실제 이동–조작 연결과 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 task·정책·success checker에서 시연 복원 시작과 실제 navigation 도착 시작을 비교하고, 정책 교체·도착 설정·reset 차이를 분리한다. 현재 P0는 실행 준비 단계이며 실측 효과가 없다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

시연 상태에서 독립 평가한 정책의 skill 능력 순위가 실제 navigation으로 만든 도착 상태에서도 유지되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
