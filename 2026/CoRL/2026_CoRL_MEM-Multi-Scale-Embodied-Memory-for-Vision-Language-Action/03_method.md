# Method — MEM: Multi-Scale Embodied Memory for Vision Language Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## 관측과 출력

최근 관측 비디오는 압축하고 장기 이력은 텍스트로 표현한다.

## 학습·실행 방법

최근 관측 비디오는 압축하고 장기 이력은 텍스트로 표현한다. 실제 장시간 조작에서 이력에 따른 행동 적응을 평가한다.

- 저자들은 π0.5 [36]를 따라 실패 뒤 사람이 수정한 시연을 수집한다. 실험의 기본 정책은 별도 모델인 π0.6 [35]이다. §IV, targeted human feedback. [pr-0061 · 원문](https://arxiv.org/pdf/2603.03596#page=7)
