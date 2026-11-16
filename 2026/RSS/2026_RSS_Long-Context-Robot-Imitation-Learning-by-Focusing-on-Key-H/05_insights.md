# Long-Context Robot Imitation Learning by Focusing on Key History Frames

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

VLM이 선택한 소수의 의미 있는 keyframe으로 정책 history를 압축한다.

기억이 필요한 실제 조작과 simulation 과제를 평가한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p201.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 VLM 호출 비용, event 검출의 미래 정보 누출, history 길이별 평가은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

VLA memory를 늘리는 것과 필요한 정보만 남기는 것의 차이를 검증할 직접 선행이다.

### Dependency and Evolution

History-conditioned IL·MemoryVLA와 사건 기반 memory selection을 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

추가 distractor history와 실패 후 회복 이력을 넣고 균일·최근·의미 keyframe을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 메모리 예산에서 keyframe 선택이 단순 균일 subsampling보다 일반화하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
