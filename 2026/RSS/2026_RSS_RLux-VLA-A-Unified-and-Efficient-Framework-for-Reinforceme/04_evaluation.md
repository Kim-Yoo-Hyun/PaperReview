# RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. RSS 게재본의 시뮬레이션과 실물 평가 절을 대조했다.

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT AND SIMULATION`.

## Dataset / Benchmark Role

LIBERO, ManiSkill, RoboTwin의 모의 조작 과제로 정책을 비교했다. 실물 전이는 서랍 닫기 한 과제에서 평가했다. [PDF 6쪽](https://www.roboticsproceedings.org/rss22/p089.pdf#page=6) · [PDF 9쪽](https://www.roboticsproceedings.org/rss22/p089.pdf#page=9)

## Metrics and Success Definition

정책 성능은 과제 성공률로, 학습 시스템의 효율은 렌더링·행동 생성·학습의 GPU 배치에 따른 처리량으로 측정했다. [PDF 6쪽](https://www.roboticsproceedings.org/rss22/p089.pdf#page=6) · [PDF 8쪽](https://www.roboticsproceedings.org/rss22/p089.pdf#page=8)

## Baselines and Fairness

실물 비교를 위해 OpenVLA에 실물 전문가 시연 20개와 모의 궤적 1,000개로 지도 미세조정을 했다. 비교 모델은 같은 체크포인트에서 출발해 시뮬레이터에서 강화학습을 추가했다. 저자는 실제 카메라 자세와 팔 구성을 모의 장면에 맞췄다. [PDF 9쪽](https://www.roboticsproceedings.org/rss22/p089.pdf#page=9)

## Main Results / Claim–Evidence Map

| 정책 | 실물 서랍 닫기 | 저자가 관찰한 행동 |
|---|---|---|
| 지도 미세조정 | 시행 10회 중 8회 성공 | 밀기 전에 회전하거나 거의 움직이지 않는 행동을 출력했다. [PDF 9쪽](https://www.roboticsproceedings.org/rss22/p089.pdf#page=9) |
| 지도 미세조정 후 시뮬레이션 강화학습 | 시행 10회 중 8회 성공 | 그림 15에서 더 직접적이고 부드러운 밀기 동작을 보였다. [PDF 9쪽](https://www.roboticsproceedings.org/rss22/p089.pdf#page=9) |

## Ablations and Sensitivity

OpenVLA-OFT의 GRPO 학습에서 목표 도달 뒤 행동을 손실에서 제외하는 마스크와 궤적 길이 정규화는 LIBERO-Goal에서 유리했다. ManiSkill에서는 두 조작의 이득이 뚜렷하지 않았다. [PDF 9쪽](https://www.roboticsproceedings.org/rss22/p089.pdf#page=9)

## 추가 비교 제안

같은 정책·알고리즘·과제에서 GPU 배치만 바꾸어 초당 표본 수, 경과 시간, 같은 상호작용 횟수에서의 성공률을 함께 비교할 수 있다. 이는 연구자의 후속 실험 제안이다.
