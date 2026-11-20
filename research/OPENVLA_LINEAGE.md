# OpenVLA 인용 계보

기준 논문은 Moo Jin Kim·Karl Pertsch 등의 **OpenVLA: An Open-Source Vision-Language-Action Model**이다. `pr-0051`, CoRL 2024. VLM을 로봇 시연으로 미세조정해 한 시점의 관측과 지시에서 행동 토큰을 생성한다. 이후 연구에는 이 가중치를 바꾼 논문, 배포 때 출력만 재선택한 논문, 원본 성적을 평가표에 인용한 논문이 모두 있다. [공식 게재본](https://proceedings.mlr.press/v270/kim25c.html)

## 선행 → 기준 → 후속

```text
RT-2 · Octo · Diffusion Policy                   ┐ 로봇 정책 설계와 비교
Open X-Embodiment · DROID                       ├ 훈련 자료와 비교 로봇
Prismatic VLMs · DINOv2 · LoRA                  ┘ 시각언어 백본과 적응
                             ↓
                      OpenVLA (CoRL 2024)
  ├─ 행동 표현·실행 주기 → OpenVLA-OFT, FAST, PD-VLA, π0, SmolVLA
  ├─ 관측 이력·공간 표현 → TraceVLA, SpatialVLA, MemoryVLA
  ├─ 행동 전 중간 추론   → ECoT, CoT-VLA, ACoT-VLA
  ├─ 배포 시 행동 선택   → V-GPS, RoboMonkey
  └─ 강화학습 후학습     → StARe-VLA
                           OpenVLA → OpenVLA-OFT → SimpleVLA-RL
```

가지는 각 논문이 **어디를 바꾸었는지** 보여 준다. 직접 계승 여부는 아래 표에 따로 적었다. 예를 들어 같은 추론 가지에서도 ECoT는 OpenVLA로 실험하고, ACoT-VLA는 π0.5에서 출발한다. 같은 학회 연도에 나온 ECoT·V-GPS도 자신의 본문에서 OpenVLA를 사용하므로 후속으로 배치했다.

## 확인한 선행 연구

각 행의 관계는 OpenVLA 저자의 설계와 실험에 비추어 붙인 해석이다. 간소 스키마는 제목·첫 저자 또는 팀·발표처·연도·ID·관계·출처를 담는다. 원장에 없는 논문에는 실제 arXiv ID를 썼다. 표의 쪽수는 링크한 판본의 PDF 페이지다. CoRL은 행사 연도를 사용하므로 2024년 행사의 PMLR 서지 연도는 2025로 표시될 수 있다.

| 논문 | 첫 저자·발표 | ID | 관계 | 근거와 적용 범위 | 원문 위치 |
|---|---|---|---|---|---|
| [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://proceedings.mlr.press/v229/zitkovich23a.html) | Zitkovich · CoRL 2023 | `pr-0022` | 확장 | RT-2의 행동 토큰 예측을 계승하고 공개 백본의 새 로봇 미세조정으로 적용 범위를 넓혔다. RT-2-X 실험행은 Open X 논문의 모델이다. | [§2, [7]](https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf#page=3) · [§3.2](https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf#page=4) |
| [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864) | Open X-Embodiment Collaboration · ICRA 2024 | `pr-0024` | 결합 | 여러 로봇의 시연을 훈련 혼합에 쓴다. 같은 논문의 RT-1-X·RT-2-X는 별도 비교 정책이다. | [§2, [1]](https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf#page=3) · [표 4](https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf#page=23) |
| [Octo: An Open-Source Generalist Robot Policy](https://arxiv.org/abs/2405.12213) | Octo Model Team · RSS 2024 | `pr-0052` | 대체 | 사전학습 부품을 조립한 Octo와 달리 VLM 전체가 행동을 예측하도록 설계했다. Octo를 새 로봇에 미세조정한 결과와도 비교한다. | [§2, [5]](https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf#page=3) · [표 7](https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf#page=29) |
| [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137) | Chi · RSS 2023 | `pr-0019` | 비판 | Franka의 여러 언어 지시에서는 사전학습 정책의 이득을, 정밀 단일 과제에서는 Diffusion Policy의 장점을 보고한다. 원형과 입력·출력을 맞춘 변형을 함께 비교한다. | [표 7](https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf#page=29) · [§4.2 비교 조건](https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf#page=7) |
| [Prismatic VLMs: Investigating the Design Space of Visually-Conditioned Language Models](https://proceedings.mlr.press/v235/karamcheti24a.html) | Karamcheti · ICML 2024 | `arXiv:2402.07865` | 확장 | Prismatic-7B의 시각 패치 투영과 언어 백본을 가져와 다음 로봇 행동을 예측하도록 훈련한다. | [§2, [44]](https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf#page=3) · [§3.1–3.2](https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf#page=4) |
| [DINOv2: Learning Robust Visual Features without Supervision](https://openreview.net/forum?id=a68SUt6zFt) | Oquab · TMLR 2024 | `pr-0006` | 결합 | Prismatic에서 물려받은 DINOv2 패치 특징을 SigLIP 특징과 결합한다. 독립적인 로봇 정책 체크포인트로 쓴 사례와 구별된다. | [§2, [33]](https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf#page=3) · [그림 2·§3.1](https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf#page=4) |
| [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://arxiv.org/abs/2403.12945) | Khazatsky · RSS 2024 | `pr-0732` | 결합 | DROID 시연을 Open X 혼합에 추가했다. 저자는 낮은 행동 토큰 정확도를 관찰하고 훈련 마지막 3분의 1에서 DROID를 뺐다. | [§2, [11]](https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf#page=3) · [§3.3 혼합 일정](https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf#page=5) |
| [LoRA: Low-Rank Adaptation of Large Language Models](https://openreview.net/forum?id=nZeVKeeFYf9) | Hu · ICLR 2022 | `arXiv:2106.09685` | 결합 | LoRA 저랭크 갱신을 새 로봇 적응에 적용하고 전체 튜닝·일부 층 튜닝과 같은 표에서 비교한다. | [표 1, [25]](https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf#page=8) · [표 8](https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf#page=29) |

## 확인한 후속 연구

| 논문 | 첫 저자·발표 | ID | 관계 | 근거와 적용 범위 | 원문 위치 |
|---|---|---|---|---|---|
| [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](https://www.roboticsproceedings.org/rss21/p017.html) | Kim · RSS 2025 | `pr-0750` | 직접 확장 | 원본 OpenVLA를 미세조정해 병렬 디코딩·행동 청크·연속 출력을 순차 비교한다. 표 I은 기존 논문의 원본 성적과 이 연구의 새 변형을 구별한다. | [표 I·II](https://arxiv.org/pdf/2502.19645#page=6) · [학습 설계](https://arxiv.org/pdf/2502.19645#page=4) |
| [FAST: Efficient Action Tokenization for Vision-Language-Action Models](https://www.roboticsproceedings.org/rss21/p012.html) | Pertsch · RSS 2025 | `pr-0749` | 구성 교체 | 차원별 균등 구간화와 압축 토큰화를 비교하고, 별도 실험에서 OpenVLA 코드의 토큰화를 FAST로 바꿔 같은 작업에 훈련한다. | [관련 연구, [39]](https://arxiv.org/pdf/2501.09747#page=3) · [OpenVLA 실험·그림 9](https://arxiv.org/pdf/2501.09747#page=9) |
| [PD-VLA: Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding](https://arxiv.org/abs/2503.02310) | Song · IROS 2025 | `pr-0278` | 성능 비교 | 병렬 디코딩·행동 청크를 제안하고 LIBERO에서 원본 OpenVLA를 비교 행으로 싣는다. 표 IV만으로 가중치 계승을 판단할 수 없다. | [표 IV](https://arxiv.org/pdf/2503.02310#page=5) · [표 III 절제](https://arxiv.org/pdf/2503.02310#page=5) |
| [π0: A Vision-Language-Action Flow Model for General Robot Control](https://www.roboticsproceedings.org/rss21/p010.html) | Black · RSS 2025 | `pr-0746` | 재학습 비교 | 관련 연구에서 OpenVLA의 자기회귀 행동 이산화를 다룬다. 별도 흐름 모델을 제안하고 자체 데이터 혼합으로 재학습한 OpenVLA와 비교한다. 훈련 스텝 차이와 계산량을 맞추려는 비교도 명시한다. | [§II, [24]](https://arxiv.org/pdf/2410.24164#page=3) · [OpenVLA 훈련 조건](https://arxiv.org/pdf/2410.24164#page=7) |
| [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](https://arxiv.org/abs/2506.01844) | Shukor · arXiv 2025 | `pr-0915` | 기보고 수치 비교 | LIBERO 표의 OpenVLA 성적은 선행 논문에서 가져왔다. 이 논문의 SO100·SO101 실물 평가 결과를 OpenVLA와의 실기 비교로 읽을 수 없다. | [표 2 각주](https://arxiv.org/pdf/2506.01844#page=11) · [표 3·4](https://arxiv.org/pdf/2506.01844#page=11) |
| [TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies](https://openreview.net/forum?id=b1CVu9l5GO) | Zheng · ICLR 2025 | `pr-0075` | 직접 확장 | 7B OpenVLA에 물체 이동 궤적을 그린 영상을 넣고 미세조정했다. 같은 자료로 궤적을 제외하고 다시 훈련한 대조 실험이 있다. | [표 1](https://arxiv.org/pdf/2412.10345#page=6) · [궤적·추가 학습 대조](https://arxiv.org/pdf/2412.10345#page=8) |
| [SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models](https://www.roboticsproceedings.org/rss21/p011.html) | Qu · RSS 2025 | `pr-0880` | 성능 비교 | 3D 위치 표현과 행동 격자를 도입하고 Google 로봇·WidowX 시뮬레이션에 OpenVLA 비교 행을 둔다. SimplerEnv 결과의 비교다. | [표 I·II](https://arxiv.org/pdf/2501.15830#page=6) · [설계·평가 범위](https://arxiv.org/pdf/2501.15830#page=5) |
| [MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation](https://openreview.net/forum?id=54U3XHf7qq) | Shi · ICLR 2026 | `pr-0085` | 성능 비교 | 기억을 사용하는 별도 정책과 OpenVLA를 SimplerEnv·LIBERO·실물 과제에서 비교했다. 같은 논문의 기억 벤치마크 Mikasa-Robo에는 OFT가 비교군이다. | [표 1·2](https://arxiv.org/pdf/2508.19236#page=8) · [표 3·4](https://arxiv.org/pdf/2508.19236#page=9) |
| [Robotic Control via Embodied Chain-of-Thought Reasoning](https://proceedings.mlr.press/v270/zawalski25a.html) | Zawalski · CoRL 2024 | `arXiv:2407.08693` | 직접 확장 | Bridge 조건의 OpenVLA와 추론 단계를 생성하는 정책을 비교한다. 추가 전이 실험은 배포된 OpenVLA-7B에서 출발한다. | [표 1](https://arxiv.org/pdf/2407.08693#page=7) · [공개 체크포인트 전이](https://arxiv.org/pdf/2407.08693#page=9) |
| [CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.html) | Zhao · CVPR 2025 | `pr-0773` | 성능 비교 | 시각적 하위 목표를 예측하는 VILA-U 기반 모델을 원본 OpenVLA와 비교한다. Bridge-V2 표에는 언어·시각 일반화 조건별 결과가 있다. | [표 1](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf#page=5) · [표 2·백본 절제](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf#page=7) |
| [ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models](https://openaccess.thecvf.com/content/CVPR2026/html/Zhong_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models_CVPR_2026_paper.html) | Zhong · CVPR 2026 | `pr-0804` | 성능 비교 | LIBERO 표에 원본과 OFT가 각각 한 행이다. 행동 추론을 학습한 저자 모델의 기반은 π0.5다. | [표 1·구현](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhong_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf#page=5) · [표 2](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhong_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf#page=6) |
| [Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance](https://proceedings.mlr.press/v270/nakamoto25a.html) | Nakamoto · CoRL 2024 | `pr-1143` | 배포 시 결합 | 고정된 OpenVLA가 제안하는 행동을 오프라인 가치 함수로 재선택한다. OpenVLA 쌍은 SIMPLER 표 2에 있고 실물 표 1은 Octo 계열이다. | [표 1·2](https://raw.githubusercontent.com/mlresearch/v270/main/assets/nakamoto25a/nakamoto25a.pdf#page=8) · [비교 정책·설정](https://raw.githubusercontent.com/mlresearch/v270/main/assets/nakamoto25a/nakamoto25a.pdf#page=7) |
| [RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models](https://proceedings.mlr.press/v305/kwok25a.html) | Kwok · CoRL 2025 | `pr-1232` | 배포 시 결합 | OpenVLA에서 후보를 뽑고 검증기로 재선택한다. LIBERO-Long에서 미세조정한 생성기 단독과 생성기·검증기의 성능을 비교한다. | [표 1](https://raw.githubusercontent.com/mlresearch/v305/main/assets/kwok25a/kwok25a.pdf#page=8) · [실물 비교 설정](https://raw.githubusercontent.com/mlresearch/v305/main/assets/kwok25a/kwok25a.pdf#page=6) |
| [STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models](https://arxiv.org/abs/2512.05107) | Xu · arXiv 2025 | `pr-1203` | 직접 후학습 | OpenVLA-7B 계열에서 시연 미세조정 후 단계별 강화학습을 비교한다. SimplerEnv·ManiSkill3의 시뮬레이션 결과이며 π0.5 실험군은 별도로 제시한다. | [표 1](https://arxiv.org/pdf/2512.05107#page=11) · [기반 모델·비교 조건](https://arxiv.org/pdf/2512.05107#page=9) |
| [SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html) | Li · ICLR 2026 | `pr-0957` | OFT 경유 후학습 | 원본은 LIBERO 표의 비교 행이다. 실제 RL 대상은 저자가 구현을 변경한 OpenVLA-OFT이며 여러 행동을 병렬 생성한다. | [표 3·구현 차이](https://proceedings.iclr.cc/paper_files/paper/2026/file/cbfbcb4da14235bd69b134070898ae9d-Paper-Conference.pdf#page=6) · [Backbones](https://proceedings.iclr.cc/paper_files/paper/2026/file/cbfbcb4da14235bd69b134070898ae9d-Paper-Conference.pdf#page=5) |

## 여러 후속이 지적한 한계

| 반복되는 관찰 | 독립적으로 확인되는 근거 | 해석의 범위 |
|---|---|---|
| 한 행동의 각 차원을 순서대로 생성하면 제어 주파수와 행동 청크 길이에 비용이 붙는다. | OFT는 같은 기반 모델의 디코딩·청크·출력 손실을 나눠 비교한다. FAST는 시간 상관이 큰 신호에서 차원별 토큰화의 비용을 분석한다. π0도 자체 데이터로 원본을 학습할 때 이 제약을 기술한다. | 처리량, 한 청크의 첫 행동 지연, 실제로 관측을 다시 받는 주기는 각각 다른 지표다. 세 방법의 성공률만 모아 한 구성요소의 효과량을 추정할 수 없다. OFT 표 I·II, FAST 관련 연구 및 그림 9, π0 §II·실험 설정 참조. |
| 현재 영상만 주어지면 객체가 어디서 왔는지, 직전에 무엇을 했는지 구별하기 어렵다. | TraceVLA는 동일 데이터에서 궤적을 빼는 대조 실험을, MemoryVLA는 기억이 필요한 실물 과제와 기억 유형·검색 절제를 제공한다. | 궤적 오버레이와 기억 저장은 서로 다른 개입이다. 특히 MemoryVLA의 Mikasa-Robo 수치를 원본 OpenVLA의 실패율로 대입할 수 없다. [TraceVLA 대조군](https://arxiv.org/pdf/2412.10345#page=8) · [MemoryVLA 표 5–7](https://arxiv.org/pdf/2508.19236#page=10) |
| 한 번 생성한 행동의 품질과 후보 중 좋은 행동을 선택하는 능력은 다르다. | V-GPS는 OpenVLA의 가치 유도 유무를 같은 시뮬레이터에서 비교한다. RoboMonkey는 같은 계열 생성기에 행동 검증기를 추가해 비교한다. | 두 논문은 선택기를 평가했다. 선택기 결과를 정책 가중치에 RL을 적용한 이득으로 합산하면 안 된다. [V-GPS 표 1·2](https://raw.githubusercontent.com/mlresearch/v270/main/assets/nakamoto25a/nakamoto25a.pdf#page=8) · [RoboMonkey 표 1](https://raw.githubusercontent.com/mlresearch/v305/main/assets/kwok25a/kwok25a.pdf#page=8) |

## 후속 근거가 희박한 지점

**훈련 혼합을 언제 바꿔야 하는가.** OpenVLA가 마지막 3분의 1에서 DROID를 제거한 절차는 SpatialVLA도 명시적으로 계승했다. 두 논문과 이 표의 후속에서 동일 백본·전체 데이터 예산을 고정하고 DROID의 유지·제거·점진 감량만 바꿔 목표 로봇과 다른 로봇을 함께 비교한 실험은 확인하지 못했다. [해석] 처음부터 훈련을 나눠야 하는 비용이 한 이유일 수 있다. 공간 표현과 훈련 혼합이 함께 바뀐 모델 간 비교로는 제거 시점의 효과를 분리하기 어렵다. [OpenVLA §3.3](https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf#page=5) · [SpatialVLA 훈련 혼합](https://arxiv.org/pdf/2501.15830#page=5)

**양자화한 정책의 오류와 느린 제어의 오류를 어떻게 구분하는가.** OpenVLA는 같은 조건에서 한 행동의 실행을 기다리는 제어로 다시 측정했다. 이 방식에서는 8비트 성능이 회복된다. 최근 QuantVLA처럼 저비트 정책을 평가한 후속도 있다. 이번 15편에서는 같은 실물 로봇에서 정밀도와 제어기 대기 방식을 모두 바꿔 원본의 결과가 다른 과제에서도 재현되는지 보여 준 표를 확인하지 못했다. [해석] 이 비교에는 모델 속도뿐 아니라 로봇 제어기의 실제 대기 동작을 맞출 수 있는 장비가 필요하다. 분야 전체에 후속이 없다는 추정까지 지지하지는 않는다. [OpenVLA 표 11](https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf#page=33) · [QuantVLA, CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_QuantVLA_Scale-Calibrated_Post-Training_Quantization_for_Vision-Language-Action_Models_CVPR_2026_paper.html)

## 검색과 판정 범위

2026-11-19에 원장의 VLA 논문, OpenVLA 원문의 역방향 참고문헌, OpenAlex의 OpenVLA 인용 목록에서 피인용순 상위 100개 제목을 함께 검토 대상으로 삼았다. 후속 15편은 행동 표현·기억·추론·행동 선택·RL을 대표하면서, 인용하는 쪽의 관련 연구나 기준선 표에 연결할 수 있는 논문이다. 검색 결과의 인용 횟수, 인접 읽기 순서, 저자 프로젝트 소개만으로 연결한 행은 없다. 희박한 지점은 후보 원문의 DROID·final third·blocking control·non-blocking 문맥과 별도로 검색한 `OpenVLA DROID final third ablation`, `OpenVLA 8-bit quantization blocking control`을 대조했다. [OpenAlex 인용 목록](https://api.openalex.org/works?filter=cites:W4399695759&sort=cited_by_count:desc&per_page=100&select=display_name)

**판본과 재실행 여부.** PD-VLA 표 IV의 원본 LIBERO-Spatial은 84.9이고 OFT 표 I의 원본 행은 84.7이다. 두 표의 전체 평균은 76.5다. 원본 LIBERO 표에 대조해 전사 차이를 표시하고, 논문에 적힌 각 값을 그대로 읽는다. SmolVLA처럼 기존 성적 인용이 명시된 경우에만 그렇게 표시했다. 표에 정책 이름만 있을 때는 독립 재실행·체크포인트 사용 여부를 미확인으로 둔다. [OpenVLA 표 12](https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf#page=35) · [PD-VLA 표 IV](https://arxiv.org/pdf/2503.02310#page=5) · [OFT 표 I](https://arxiv.org/pdf/2502.19645#page=6)
