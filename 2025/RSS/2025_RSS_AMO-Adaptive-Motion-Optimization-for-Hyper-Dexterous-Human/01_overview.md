# AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Source audit: 2026-11-16: RSS metadata·arXiv v1 §III–V/Table II–IV·공식 코드로 OCR/설명 교정. 과거2026-09-03 PDF review 기록은 보존; 사용자 reading status 변경 없음.

- Year/Venue: 2025 / RSS
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tags: Robotics, humanoid, whole-body control, trajectory optimization, sim-to-real
- Official paper: https://www.roboticsproceedings.org/rss21/p061.html
- Project: https://amo-humanoid.github.io/
- Code: https://github.com/OpenTeleVision/AMO
- Public identifiers: {"doi": "10.15607/RSS.2025.XXI.061", "arxiv": "2505.03738"}

## Why This Paper Is Here

[RSS2025 AMO](https://www.roboticsproceedings.org/rss21/p061.html)는 trajectory optimization과 sim-to-real RL로 휴머노이드의 조작 workspace를 넓힌다. Ψ₀ v1의 하위 제어기를 이해할 직접 참고 논문이다. 현재 tier는 REFERENCE이며 로봇 언어 정책 자체의 RL 방법으로 분류하지 않는다.

## Contribution and Interface

상체 자세·몸통 명령에 맞춰 하체 reference를 생성하고 RL 정책으로 추종한다. Teleoperation과 autonomous imitation upper policy에 공통 하위 제어기를 연결한다. [공식 project](https://amo-humanoid.github.io/).

## Scope and Source Correction

기존 OCR의 깨진 관절 표기·일반 템플릿·queue 이웃을 인용 관계처럼 읽게 하는 문장을 정리했다. 과거 PDF review는 provenance의 역사 기록으로 보존하며, 이번 수정은 HTML 원문 대조다. [원문](https://arxiv.org/html/2505.03738v1).
