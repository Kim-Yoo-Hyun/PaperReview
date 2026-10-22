# NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Monocular RGB video history를 VLM context로 처리하여 다음 navigation action을 출력한다.

RSS abstract는 continuous navigation simulation과 실제 환경의 cross-dataset/sim-to-real 평가를 명시한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss20/p079.html) · [저자 project/code](https://pku-epic.github.io/NaVid/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Camera-only 가정, action discretization, history truncation, 실제 low-level controller은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Foundation lineage. RGB video history에서 next action을 출력하는 navigation VLM이다. Uni-NaVid/StreamVLN을 비교할 때 선행 interface를 보충한다. **NaVILA 및 Uni-NaVid와 다른 논문**이다.

### Dependency and Evolution

VLN-CE → NaVid → Uni-NaVid/StreamVLN; NaVILA와 controller interface 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

NaVid의 history context 길이를 변화시키고 fixed task에서 success·SPL·inference latency·wrong-turn recovery를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 visual token budget에서 history 압축이 instruction grounding과 실제 navigation 성공을 유지하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
