# Method — N₀-VTLA: Scaling Vision-Tactile-Language-Action Model with Latent Tactile Tokens

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · 저자판 v1 PDF 4–10, 13–14쪽, §§3–5, Fig. 9 확인. [서지·게재 상태](https://arxiv.org/abs/2607.23782)

## 관측과 출력

실행 정책은 촉각·영상·언어·로봇 상태를 입력으로 행동 청크를 낸다. ALTER에 쓰는 진행도 추정과 궤적 비교는 학습 시 수행한다.

## 학습·실행 방법

잠재 촉각 토큰을 시각·언어 표현 및 연속 행동 전문가와 결합해 사전학습한다. 선택 단계인 ALTER는 고정된 배포 궤적에서 진행도와 국소 변화로 advantage 표지를 구성한 뒤 조건부 행동 정책을 다시 학습한다.

- §3의 상태·행동 컨테이너는 π0.5에서 계승한다. 두 팔을 위한 좌표 배치와 저자 모델의 촉각 경로는 구분한다. [pr-0061 · 원문](https://arxiv.org/pdf/2607.23782v1#page=5)
