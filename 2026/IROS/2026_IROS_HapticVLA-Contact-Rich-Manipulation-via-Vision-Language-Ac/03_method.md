# Method — HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · 저자판 v2 PDF 3–7쪽, §§III–IV의 교사·학생과 실물 과제 확인. [서지·게재 상태](https://2026.ieee-iros.org/program/paper-index/)

## 관측과 출력

교사는 촉각을 포함한 관측을 사용한다. 학생은 RGB·언어·로봇 상태로 행동 청크를 생성하며 현재 손끝 촉각을 직접 관측하지 않는다.

## 학습·실행 방법

접촉 및 과도한 파지력으로 가중한 flow matching으로 교사를 학습한다. 학생은 시각·상태에서 촉각 표현을 추정하고 교사의 행동을 모방한다.

- §III의 SmolVLA 기반 교사·학생에서 행동 전문가 학습과 촉각 증류를 바꾼다. [pr-0915 · 원문](https://arxiv.org/pdf/2603.15257v2#page=3)
