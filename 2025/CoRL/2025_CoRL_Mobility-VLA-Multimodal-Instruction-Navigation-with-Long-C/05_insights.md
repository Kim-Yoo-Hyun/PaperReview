# Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

장문맥 VLM의 goal-frame 선택과 topological graph 기반 하위 navigation을 결합한다.

기록된 tour를 제공한 실환경의 multimodal instruction navigation을 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/xu25b.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 tour/graph 구축 비용, goal 후보 접근, online 관측과 planner timing은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

NaVILA·NoMaD와 비교할 계층형 VLA navigation 및 환경 사전정보 기준이다.

### Dependency and Evolution

ViNT·NoMaD → Mobility VLA; NaVILA와 high/low-level interface 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 graph/controller에서 retrieval과 VLM goal selection만 바꾸어 평가한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 tour·goal 후보를 줄 때 긴 문맥 추론의 이득이 단순 frame retrieval을 넘는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
