# Problem

## 왜 문제인가
현실의 3D reconstruction/SLAM은 calibration, pose, correspondence, temporal consistency가 불완전한 상태에서 metric geometry를 추정해야 한다.

## 해결하려는 문제
- 연구 유형: 3D reconstruction, calibration, and geometric consistency
- 목표: 3D geometry/semantics와 language/action 사이의 mismatch를 줄이고, 실제 embodied setting에서 쓸 수 있는 표현 또는 policy를 만드는 것.
- 중요한 이유: 로봇은 closed-set category 인식보다 더 복합적인 공간 관계, affordance, 장기 계획, sensor noise를 다뤄야 한다.
- Abstract problem cue: However, most prior approaches prioritize training large geometry models for low-level 3D reconstruction and treat high-level spatial understanding in isolation, overlooking the crucial interplay ...

## 선행 연구 분석
- 2D VLM/LLM은 semantic prior가 강하지만 metric 3D 구조와 physical feasibility가 약하다.
- 고전 3D geometry/SLAM은 구조적 안정성이 있지만 open-vocabulary language grounding과 high-level reasoning이 약하다.
- 이 논문은 두 축을 결합하는 흐름 안에서, `3D reconstruction, semantic, alignment, 3D Vision` 관점의 개선을 제안한다.
