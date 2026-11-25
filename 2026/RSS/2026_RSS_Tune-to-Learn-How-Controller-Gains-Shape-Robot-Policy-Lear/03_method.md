# Tune to Learn: How Controller Gains Shape Robot Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — RSS 본문과 arXiv v1의 지정 절·부록, 저자 공개 자료 대조 (2026-11-19).

## 위치 제어와 정책

관절 위치 목표와 현재 위치 차이에 비례 이득을, 속도 항에 감쇠 이득을 적용한다. 정책은 관측에서 위치 목표를 갱신한다. 외력에 저항할지 양보할지는 이득, 정책이 보내는 목표, 학습 보상이 함께 결정한다. [정식화](https://arxiv.org/html/2604.02523v1#S3)

- **행동 복제.** 500 Hz 토크 시연을 고정 이득별 50 Hz 관절 위치 목표로 변환해 비슷한 상태 궤적에서 다른 행동 레이블을 얻는다. 여섯 과제 중 다섯 과제에는 과제당 100개 원격 조작 시연을, 블록 쌓기에는 모션 플래너 궤적을 썼다. 명목 정책은 시뮬레이터 상태를 받는 VAE/MLP다. [§IV-A](https://arxiv.org/html/2604.02523v1#S4.SS1) · [부록](https://arxiv.org/html/2604.02523v1#A1.SS3)
- **온라인 RL.** 고정 이득 조합마다 SKRL PPO를 학습하고 Optuna TPE로 관절 그룹별 행동 배율을 조정한다. FR3는 팔꿈치 쪽과 손목 쪽, G1은 하체와 상체를 나눈다. FR3 EE-Reach에서는 보상 가중치도 조정한다. 손이 있는 과제에서 그리퍼 구동 이득은 고정한다. [§IV-B](https://arxiv.org/html/2604.02523v1#S4.SS2) · [행동 변환과 성공 기준](https://arxiv.org/html/2604.02523v1#A1.SS5.SSS2)
- **전이.** 각 이득의 실물 응답으로 시뮬레이터를 동정하고, 시뮬레이션에서 배운 도달 정책을 실물에 적용해 궤적 차이를 측정한다. 명목 실물 토크 제어 1 kHz, 시뮬레이션 물리 100 Hz, 위치 목표 갱신 50 Hz다. [전이 설정과 주기](https://arxiv.org/html/2604.02523v1#A1.SS6)

공개 큐브 들기 배포본 4개는 8차원 행동과 고정 XML 구동 이득을 쓴다. 명목 이득 셀마다 내보낸 행동 배율과 실제 XML 수치가 다르다. [공개 배포본](https://github.com/younghyopark/tune-to-learn/tree/1775091ee2fdb683e1e767822e5caa87cdfdba4a/static/assets/wasm-policy)
