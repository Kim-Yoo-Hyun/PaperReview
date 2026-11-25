# Tune to Learn: How Controller Gains Shape Robot Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — RSS 본문과 arXiv v1의 지정 절·부록, 저자 공개 자료 대조 (2026-11-19).

## Paper-supported conclusion

고정 이득에서도 상태에 따라 정책이 목표를 바꾸면 작업 강성이 바뀐다. 같은 원 시연의 행동 복제에서는 고정 이득에 따라 성공률이 달랐고, 온라인 RL에서는 이득마다 행동 배율 등의 탐색을 허용하자 여러 이득에서 성공 설정을 찾았다. 시뮬레이터가 열린 루프 실물 응답을 잘 맞춘 설정도 정책 배포 시 큰 오차를 낼 수 있었다. [본문 결과](https://arxiv.org/html/2604.02523v1#S5)

## Researcher interpretation

접촉 중 강성을 조절하는 VLA의 가치를 판단하려면 동작만 출력하는 기준 정책에도 같은 힘 이력, 속도·목표 보정, 이득별 튜닝 예산을 줘야 한다. 저항이 다른 충전기에서 이 기준선으로도 힘 한도와 삽입·손 떼기를 함께 만족하는지 먼저 묻는다. 고정 이득이 충분하면 가변 강성 학습에 투자할 근거가 약해진다. 부족할 때도 간단한 힘 피드백 규칙을 함께 비교해야 학습 자체의 기여를 판정할 수 있다. [접촉 이력의 비교 결과](../../../work/research_topics/RESULTS.md#plug-match)
