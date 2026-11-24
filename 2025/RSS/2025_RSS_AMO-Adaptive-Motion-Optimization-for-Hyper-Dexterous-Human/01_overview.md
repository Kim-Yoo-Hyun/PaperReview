# AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Source audit: 2026-11-16: RSS metadata·arXiv v1 §III–V/Table II–IV·공식 코드로 OCR/설명 교정. 과거2026-09-03 PDF review 기록은 보존; 사용자 reading status 변경 없음. 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

- Year/Venue: 2025 / RSS
- Authors: Jialong Li, Xuxin Cheng, Tianshu Huang, Shiqi Yang, Ri-Zhao Qiu, Xiaolong Wang
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tags: Robotics, humanoid, whole-body control, trajectory optimization, sim-to-real
- Official paper: https://www.roboticsproceedings.org/rss21/p061.html
- Project: https://amo-humanoid.github.io/
- Code: https://github.com/OpenTeleVision/AMO
- Public identifiers: {"doi": "10.15607/RSS.2025.XXI.061", "arxiv": "2505.03738"}

## Why This Paper Is Here

AMO는 궤적 최적화와 sim-to-real 강화학습을 결합해 G1이 몸통과 다리 자세를 바꾸며 손이 닿는 공간을 넓힌다. [PDF 1쪽](https://www.roboticsproceedings.org/rss21/p061.pdf#page=1)

[RSS2025 AMO](https://www.roboticsproceedings.org/rss21/p061.html)는 trajectory optimization과 sim-to-real RL로 휴머노이드의 조작 workspace를 넓힌다. Ψ₀ v1의 하위 제어기를 이해할 직접 참고 논문이다. 현재 tier는 REFERENCE이며 로봇 언어 정책 자체의 RL 방법으로 분류하지 않는다.

## Contribution and Interface

- 사람의 모션과 최적화로 생성한 참조를 함께 사용해 다양한 높이와 자세 명령을 추종하도록 학습한다. [PDF 2쪽](https://www.roboticsproceedings.org/rss21/p061.pdf#page=2) · [PDF 3쪽](https://www.roboticsproceedings.org/rss21/p061.pdf#page=3)
- 몸통의 자세·높이 추종과 가용 작업 공간을 기준선과 비교하고 실물 G1에서 적응 동작을 검증한다. [PDF 5쪽](https://www.roboticsproceedings.org/rss21/p061.pdf#page=5) · [PDF 6쪽](https://www.roboticsproceedings.org/rss21/p061.pdf#page=6)

상체 자세·몸통 명령에 맞춰 하체 reference를 생성하고 RL 정책으로 추종한다. Teleoperation과 autonomous imitation upper policy에 공통 하위 제어기를 연결한다. [공식 project](https://amo-humanoid.github.io/).

## Scope and Source Correction

기존 OCR의 깨진 관절 표기·일반 템플릿·queue 이웃을 인용 관계처럼 읽게 하는 문장을 정리했다. 과거 PDF review는 provenance의 역사 기록으로 보존하며, 이번 수정은 HTML 원문 대조다. [원문](https://arxiv.org/html/2505.03738v1).
