# Insights — OpenFrontier: General Navigation with Visual-Language Grounded Frontiers

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 RSS 게재본 PDF 3–9쪽과 저자 배포 저장소 대조. Full-text scope의 수치·조건만 기록했다.

## Paper-supported conclusion

영상의 frontier를 후보로 만들고 언어 목표와의 관련성을 VLM으로 점수화한다. 후보를 희소한 3D 중간 목표로 유지해 지역 제어와 전역 경로 선택에 사용한다. [원문 및 평가 절](https://roboticsproceedings.org/rss22/p067.pdf#page=5)

## Researcher interpretation

학습을 추가하지 않고 3D 관측으로 언어 내비게이션 행동을 개선하는 기준선이다.

- 같은 평가 설정에서 VLFM을 frontier 기반 비교군으로 사용한다. [pr-0540 · 원문](https://roboticsproceedings.org/rss22/p067.pdf#page=6)

## 최소 비교 실험

같은 에피소드와 지역 제어기를 두고 frontier의 거리·기하 점수와 VLM 점수를 비교한다.
