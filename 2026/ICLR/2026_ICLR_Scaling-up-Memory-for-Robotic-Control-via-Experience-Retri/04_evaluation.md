# Scaling up Memory for Robotic Control via Experience Retrieval

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. 아래에 인용한 원문 절·표의 평가 조건을 대조했다.
> Source audit: 2026-11-25 원문 방법·평가 대조.

## 평가 조건

논문의 상위 정책은 Qwen2.5-VL-7B-Instruct로 핵심 프레임과 다음 기술 지시를 예측하고 하위 π0.5가 행동을 생성한다. [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/9da515b1ad19d032a7398f00f5ff9b0c-Paper-Conference.pdf#page=5)

먼지 닦기에서 물체를 원래 위치에 되돌렸는지와 각 선반을 닦았는지를 따로 채점한다. 실제 Franka에는 외부 카메라와 손목 카메라가 있다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/9da515b1ad19d032a7398f00f5ff9b0c-Paper-Conference.pdf#page=7)

저자는 누적한 핵심 프레임을 장시간 사용 중 제거하는 메커니즘이 없다고 밝혔다. [PDF 10쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/9da515b1ad19d032a7398f00f5ff9b0c-Paper-Conference.pdf#page=10)

공개된 먼지 닦기용 상위 체크포인트는 Qwen3-VL-4B 판본이다. [저자 배포](https://huggingface.co/ajaysri/memer-dusting-qwen3vl-4b-step-1500)

## Paper-Specific Verification Questions

선택 supervision·실패 후 이력 분포·최근 frame 예산. 상위 모델의 비교는 게재본·프로젝트·배포 체크포인트의 판본을 명시한다.

제안 실험과 실제 보고 결과는 [insights](./05_insights.md)에서 구분한다.
