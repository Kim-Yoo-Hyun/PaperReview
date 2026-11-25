# Tune to Learn: How Controller Gains Shape Robot Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — RSS 본문과 arXiv v1의 지정 절·부록, 저자 공개 자료 대조 (2026-11-19).

## 문제와 가정

같은 동작 오차에 대한 모터 토크는 비례·감쇠 이득에 따라 달라진다. 그런데 상태 피드백을 받는 정책은 다음 목표 자체를 바꿀 수 있다. 저자들은 외력에 대한 자세 유지 보상과 부드럽게 양보하는 보상을 달리해 이 두 효과를 분리했다. 부록의 힘–변위 측정에서는 구동 강성이 32배 낮은 조건에서도 학습한 정책의 작업 수준 강성이 약 5배 높았다. 서로 다른 목적함수로 만든 예시이므로 이를 같은 보상에서 이득 하나만 바꾼 효과로 환산할 수 없다. [본문 §III](https://arxiv.org/html/2604.02523v1#S3) · [부록의 유효 강성 측정](https://arxiv.org/html/2604.02523v1#A1.SS2)

지시·목표에 따른 정책 반응, 목표 위치, 관절 제어기, 접촉, 다음 관측이 한 루프를 이룬다. 같은 궤적을 따라갈 때 어떤 이득이 시연의 위치 목표를 모방하기 쉽게 하는지와, 정책이 스스로 수집한 경험으로 어떤 행동을 찾을 수 있는지는 별도 질문이다. [실험 설계](https://arxiv.org/html/2604.02523v1#S4)
