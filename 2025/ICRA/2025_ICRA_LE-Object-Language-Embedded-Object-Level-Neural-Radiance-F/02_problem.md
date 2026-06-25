# Problem

## 왜 문제인가
NeRF/3DGS는 장면을 잘 렌더링하지만 언어 질의, open-vocabulary semantics, instance-level grounding을 직접 지원하지 않는 경우가 많다.

## 해결하려는 문제
- 연구 유형: language-aware Gaussian/implicit 3D scene representation
- 목표: 3D geometry/semantics와 language/action 사이의 mismatch를 줄이고, 실제 embodied setting에서 쓸 수 있는 표현 또는 policy를 만드는 것.
- 중요한 이유: 로봇은 closed-set category 인식보다 더 복합적인 공간 관계, affordance, 장기 계획, sensor noise를 다뤄야 한다.
- Abstract problem cue: However, existing methods face some limitations: they either focus on learning point-wise features, resulting in blurry semantic understanding, or solely tackle object-level reconstruction, thereby ...

## 선행 연구 분석
- 2D VLM/LLM은 semantic prior가 강하지만 metric 3D 구조와 physical feasibility가 약하다.
- 고전 3D geometry/SLAM은 구조적 안정성이 있지만 open-vocabulary language grounding과 high-level reasoning이 약하다.
- 이 논문은 두 축을 결합하는 흐름 안에서, `semantic` 관점의 개선을 제안한다.
