# 종료된 연구 검토: 로봇 간 RL 개선 전이

- 종료일: 2026-10-20 KST
- 상태: **RETIRED — 사용자 요청으로 다른 VLA+RL 주제로 전환**
- 보존 범위: 연구 질문, 실제 측정한 핵심 결과, 해석과 교훈
- 이 문서는 실험 실행 명세가 아니다. 사용자 요청에 따라 기존 실행 코드·환경·모델·데이터·상세 로그를 삭제했으며, 이 요약만으로 실험을 재현할 수 없다.

## 질문과 범위

**한 로봇에서 얻은 RL 개선은 어떤 조건에서 다른 로봇에도 전달되는가? 그 이득은 성공 데이터 선택이나 return-weighted imitation으로 설명되는가?**

검토한 구성은 frozen Octo 표현, 작은 shared adapter, 로봇별 action head와 robosuite PickPlace였다. Panda·UR5e와 milk·can 조합을 계획했다. 두 로봇 모두 downstream bootstrap에 참여했으므로 unseen-embodiment zero-shot 설정이 아니다. End-to-end VLA RL의 검증도 아니다.

## 핵심 결과

아래 결과는 모두 첫 qualification cell인 **Panda / milk**다. 각 행은 별도 초기 상태 집합을 사용하므로 행 사이 수치를 직접적인 개선 효과로 비교하지 않는다. 같은 행의 정책과 teacher는 같은 초기 상태에서 평가했다.

| 검사 | 학습 정책의 stable success | Scripted teacher | 해석 |
|---|---:|---:|---|
| 초기 Gaussian BC | 1/20 | 18/20 | 기본 조작 능력 미달 |
| Clean / corrective-data 비교 | 0/20 / 1/20 | 17/20 | 해당 corrective-data 수정으로 해결되지 않음 |
| Quaternion+padding / continuous 6D rotation | 0/20 / 0/20 | 18/20 | 자세 입력의 불연속 제거만으로 해결되지 않음 |
| Single action / 짧은 action chunk | 0/20 / 2/20 | 18/20 | 사전 운영 기준인 4/20에 미달 |

마지막 두 비교는 같은 129 clean + 117 corrective training episodes, training seed 0, 정책별 5,000 updates를 사용했다. Qualification seeds는 각각 32000–32019와 33000–33019였다. Stable success는 요청 객체만 배치된 뒤 추가 12 passive ticks 후에도 성공이 유지되는 조건이다.

마지막 chunk 비교는 head 크기와 초기화를 맞췄지만 supervision 양과 재관측 간격도 달랐다. SINGLE은 640,000개, CHUNK4는 2,462,806개 action-label vectors를 사용했다. 따라서 0/20 대 2/20을 chunking만의 인과 효과로 해석하지 않는다. 한 training seed와 소수 장면으로 일반 성능을 추정할 수도 없다.

저장 action의 teacher replay는 두 로봇·두 목표·train/validation에서 총 **16/16 성공**했으며, 최대 proprio 재생 오차는 **9.63×10⁻⁶**였다. 실행·재생 경로가 작동하는 것과 learned policy의 기본 능력이 확보되는 것은 별개였다. Gripper 입력이 실제 joint state 대신 command accumulator였다는 관측 모호성도 확인했지만, 이를 실패의 유일한 원인으로 입증하지는 않았다.

## 결론의 경계

**확인한 결과:** 이 frozen-feature bootstrap은 제한된 입력·데이터·head 수정 뒤에도 최소 조작 능력을 확보하지 못했다. 이 구성에서 대규모 전이 비교를 확대할 근거가 부족했다.

**미검증:** source-only RL, BC_ALL / BC_SUCCESS / MC_RETURN / MC_ADV / IQL_SHARED 비교, 다른 robot/task cell, instruction swap, 로봇 간 positive/negative transfer. Reserved final-test seeds도 사용하지 않았다.

따라서 **“RL 개선이 다른 로봇에 전달되지 않는다” 또는 “RL은 가중 모방보다 이득이 없다”는 결론은 내릴 수 없다.** 20% qualification gate는 당시 운영상 기준이며 낮은 BC 성능에서 RL이 원리적으로 불가능하다는 명제가 아니다. 연구 질문은 반증된 것이 아니라 현재 구성에서 검증에 진입하지 못했고, 이후 사용자 결정으로 종료했다.

## 문헌 검토에서 남길 핵심

- 공통 표현과 로봇별 head, RL 경험의 generalist distillation, cross-embodiment offline RL 자체는 선행 연구에 있다. 조합만으로 신규성을 주장할 수 없다. [RLDG, RSS 2025](https://www.roboticsproceedings.org/rss21/p028.html), [Cross-Embodiment Offline RL, ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/24a0f56452202e8433d582dbf5095c32-Abstract-Conference.html).
- IQL의 actor도 advantage-weighted imitation을 사용한다. 적절한 비교는 “RL 대 imitation”이라는 이분법보다 **경험 생성·선택·weight 추정·TD bootstrapping의 효과 분리**다. [IQL, ICLR 2022](https://iclr.cc/virtual/2022/poster/5941), [RvS](https://arxiv.org/abs/2112.10751).
- 이전에 검토한 실행 지연·adaptive chunk·fast correction도 넓은 신규 주제로 유지하지 않는다. [REMAC, ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/c35834443b7881e782e52b3519fe27c7-Abstract-Conference.html), [TIC-VLA, ICML 2026](https://proceedings.mlr.press/v306/huang26cd.html)가 직접적인 비교 대상이었다. 이 지연 방향은 실험하지 않았다.

## 다음 주제로 가져갈 교훈

1. 검증된 task/checkpoint/interface를 출발점으로 삼고, 새 작은 head의 bootstrap에 연구 전체를 의존시키지 않는다.
2. 언어·관측·action의 어떤 요인을 바꾸는지와 그 요인이 정책의 행동을 실제로 바꾸는지를 먼저 확인한다.
3. 데이터 지원, label 수, feedback 간격, 학습 예산을 분리해 비교한다.
4. 단순 baseline과 prerequisite가 실패하면 원인을 확인하고 범위를 줄인다. 같은 qualification 장면에서 수정만 반복하지 않는다.
5. 구현 가능성, 연구 가설의 타당성, 최종 논문 기여를 별개로 판단한다.

현재 작업은 [새 VLA+RL 후보 문헌 검토](../../research_candidates/2026-10-20_vla_rl/README.md)다.
