# Insights

## Limitation
강한 benchmark 성능이 실제 로봇 센서 노이즈, rolling shutter, 동적 객체, 저조도 환경까지 보장하지는 않는다.

## Strength
- `3D reconstruction, calibration, and geometric consistency` 문제를 3D geometry와 language/action prior를 함께 쓰는 방향으로 밀어붙인다.
- 사용자의 연구 키워드 중 `geometry, depth, 3D Vision`와 직접적으로 연결된다.

## Paper Claim
- 논문의 중심 claim은 기존 2D-only, closed-set, 또는 task-specific 접근보다 더 일반화 가능한 3D-aware representation/policy/reasoning을 제공한다는 것이다.
- Abstract result cue: By exploiting context-balanced anchors, it achieves search-free, pixel-wise dense alignment and efficient loop closure without costly feature matching.

## Future Work
- dynamic scene, partial observation, sensor noise, cross-embodiment transfer, real-time inference, safety-aware planning을 추가 검증하는 것이 중요하다.
- 3D scene graph/semantic Gaussian/SLAM map을 VLA policy의 persistent memory로 연결하는 방향이 유망하다.

## 내 관점
- 이 논문은 `3D Equivariance, Calibration, and Registration` 축에서 읽어야 한다.
- 후속 연구 아이디어: language-grounded 3D memory를 만들고, robot policy가 이를 action feasibility와 uncertainty까지 포함해 조회하도록 설계한다.
