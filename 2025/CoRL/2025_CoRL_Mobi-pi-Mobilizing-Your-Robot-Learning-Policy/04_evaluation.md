# Mobi-π: Mobilizing Your Robot Learning Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. 아래에 인용한 원문 절·표의 평가 조건을 대조했다.
> Source audit: 2026-11-25 원문 방법·평가 대조.

## 평가 조건

여러 위치에서 모은 RGB-D 이미지로 정적인 3D 가우시안 장면을 만든다. 후보 베이스 자세에서의 영상 합성에 쓰는 관측과 기존 조작 정책이 실행 때 받는 관측의 역할을 구분한다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/yang25b/yang25b.pdf#page=4)

시뮬레이션은 Franka Panda와 Omron 베이스에서 RoboCasa의 다섯 주방 과제를 사용한다. 베이스 위치를 고르는 방식에 따른 후속 조작 성공을 비교한다. [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/yang25b/yang25b.pdf#page=5)

저자는 실행 중 바뀐 장면을 갱신하지 않는 점을 한계로 적었다. 배포된 서랍 닫기 장면 모델과 LeLaN 내비게이션 가중치는 서로 다른 구성요소다. [PDF 9쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/yang25b/yang25b.pdf#page=9)

## Proposed Evaluation — Researcher Interpretation

동일 scene·도착 후보·navigation·비용에서 A 선택 재사용, 정책 무관 고정 pose, 제한된 B validation 재선택을 비교한다. 실제 이동 후 상태를 분기하고 전체 시도 분모를 보존한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.
