# Self-Improving Vision-Language-Action Models with Data Generation via Residual RL

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 인용한 원문 절·표의 평가 조건을 대조했다.

## 평가 조건

잔차 전문가는 고정 VLA의 행동에서 시작해 실패 상태의 복구 자료를 모은다. 마지막 단계는 선택한 궤적으로 범용 정책을 SFT하는 과정이다. [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/163a875ab0c2631ed30b7435c4c9b8f1-Paper-Conference.pdf#page=5)

LIBERO에서는 π0와 OpenVLA로 증류한 결과를 나누어 보고한다. 잔차 전문가가 수집한 행동과 배포할 범용 정책의 결과는 별도 비교다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/163a875ab0c2631ed30b7435c4c9b8f1-Paper-Conference.pdf#page=7)

실물 평가에는 Franka와 YAM 시스템이 포함된다. YAM 삽입에서도 수집용 잔차 전문가와 그 자료를 증류한 정책의 역할을 분리한다. [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/163a875ab0c2631ed30b7435c4c9b8f1-Paper-Conference.pdf#page=9)

## Minimal Check — Researcher Proposal

연구자 제안: 먼저 base 갱신 전후 action/normalizer와 residual 입력을 대조하고 frozen residual·gain 조정·fresh residual을 동일 새 데이터 예산으로 비교한다.

실행하지 않았다. 재개는 해당 연구의 local Docker 환경·입출력 확인 뒤에 한정하며 큰 학습을 자동 실행하지 않는다.

이전 판본의 잔차 정책 검토 범위는 §3과 부록 B.2·C.1·C.2다. [초기 저자 판본](https://arxiv.org/html/2511.00091v1)
