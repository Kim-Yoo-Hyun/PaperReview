# KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

물리 추론 난점을 분리한 절차적 환경과 skill·시연·평가 baseline을 제공한다.

다양한 planning·IL·RL baseline 및 mobile manipulator 대응 실험을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p184.html) · [저자 project/code](https://prpl-group.com/kinder-site/) · [공식 code](https://github.com/Princeton-Robot-Planning-and-Learning/kindergarden). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 skill 호출 권한, 관측 특권, baseline별 compute, 절차적 split은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

VLA의 실패가 언어 표현 문제인지 물리적 의사결정 문제인지 진단할 자원이다.

### Dependency and Evolution

TAMP·RL 평가와 LIBERO의 언어 조건부 조작을 연결하되 과제 입력 차이를 보존한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 초기 상태에서 구조화된 상태 baseline과 visual policy를 비교하고 실패 원인을 분리한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

VLA의 물리 추론 실패는 인식 오차를 제거해도 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
