# ClevrSkills: Compositional Language And Visual Reasoning in Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

ManiSkill2 기반 환경과 demonstration dataset, 단계별 조합 과제로 언어·시각 지시 이행을 비교한다.

기초 조작에서 복합 과제로 이어지는 세 수준의 curriculum에서 VLM 기반 baseline을 평가한다. 이 등록에서는 정확한 trial 수·성공률을 새로 확정하지 않는다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2024/hash/439539557e9ba0d04055773ff1f3241c-Abstract-Datasets_and_Benchmarks_Track.html) · [저자 project/code](https://github.com/Qualcomm-AI-research/ClevrSkills). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 task 생성의 정답 정보와 자동 입력, 부분집합 허용 범위, release/contact predicate, 조합 split의 학습 support은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

VIMA·VLABench와 함께 집합/수량 후보의 기존 조합 task와 평가 predicate를 이해할 NEXT benchmark다. 여러 물체 처리·나열 표현 자체를 새 기여로 삼지 않도록 등록한다.

### Dependency and Evolution

VIMA의 multimodal prompt interface와 VLABench의 장기 지시 평가를 비교하는 개념적 연결이다. 직접 citation 계보를 새로 검증한 것은 아니다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

고정 task/predicate와 정책 입력을 먼저 대조하고, 호환 로컬 Docker에서 기본 조작을 확인한 뒤 단순 지시 대조를 설계한다. 이 등록은 실행 승인·재현 결과가 아니다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

기존 task가 제공하는 정답 물체 나열과 RGB로 예측한 목록을 구별하면, 자유 subset 수량 지시에서 추가로 비교할 조건은 무엇인가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
