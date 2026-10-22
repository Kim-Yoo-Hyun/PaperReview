# StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Fast streaming dialogue context와 slow-updating memory를 결합하고 3D-aware token pruning으로 history를 압축한다.

저자 공식 project는 VLN-CE benchmark와 여러 실제 환경의 장기 navigation을 설명한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2507.05240) · [저자 project/code](https://streamvln.github.io/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 3D pruning에 필요한 입력, KV-cache 갱신, 실제 sensor/controller 지연은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Current trend. Fast action context와 slow history memory를 결합한다. NaVid/Uni-NaVid 이후 긴 video history를 제한된 inference budget으로 처리하는 비교 대상이다. RL 자체의 논문으로 분류하지 않는다.

### Dependency and Evolution

NaVid/Uni-NaVid → StreamVLN; FeedTTA와 memory/adaptation 역할 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Sliding-window-only와 slow-fast memory를 동일 context budget으로 비교해 success·잘못된 회전·episode 시간·memory 비용을 기록한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 token·latency budget에서 slow-fast memory가 sliding-window-only보다 장기 instruction tracking을 개선하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
