# SocialNav: Training Human-Inspired Foundation Model for Socially-Aware Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

VLM brain과 trajectory action module을 결합하고 imitation 이후 socially-aware flow-exploration GRPO로 정책을 개선한다.

CVF abstract는 SocNav dataset, navigation success와 social compliance 평가를 보고한다. 정확한 metric 정의와 실제 robot trial은 확인 필요.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.html) · [저자 project/code](https://amap-eai.github.io/SocialNav/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Social label/reward 정의, 지역/환경별 규범 변화, reward hacking 및 evaluation split은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Current trend / dataset. Semantic reasoning과 trajectory generation에 socially compliant reward를 연결한다. NaVILA/VLFM의 task success 중심 비교에 행동 제약을 더한다. 기존 **SocialNav-SUB는 별도 benchmark**다.

### Dependency and Evolution

NaVILA/VLFM + flow-policy RL → SocialNav; SocialNav-SUB와 별도 entry.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Task-only reward와 social reward를 같은 policy로 비교하고 success·규범 위반·경로 길이·collision을 함께 보고한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 navigation 성공률을 유지하면서 social reward가 규범 위반을 줄이는가, 우회 비용만 늘리는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
