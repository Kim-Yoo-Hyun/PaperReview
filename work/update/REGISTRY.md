# 레지스트리 변경

논문별 등록 근거와 분류 기준을 관리한다. 전체 규모와 교정 후 감사 결과는 해당 원장에서 확인할 수 있다. 공개 자료를 실험에 재사용할 때는 논문별 overview에서 파일의 역할을 확인한다. 기반 모델·하위 정책·최종 정책은 공개 범위가 다를 수 있다. [통계](../../research/REGISTRY_STATS.md) · [공개 파일 대조](../../research/SOURCE_AUDIT.md#core-공개-자료) · [원문 감사](../../research/SOURCE_AUDIT.md)

## 공유 제어 문헌과 공개 자료

- HARMONIC (`pr-1251`, IJRR 2022)을 REFERENCE에 등록했다. 조이스틱에서 변환한 사용자 요청과 보조 후 적용 속도를 별도 스트림으로 제공한다. 2021년 온라인 선공개와 2022년 저널 권호를 구분했다. [논문 노트](../../2022/IJRR/2022_IJRR_HARMONIC-A-multimodal-dataset-of-assistive-humanrobot-coll/01_overview.md) · [IJRR](https://doi.org/10.1177/02783649211050677) · [공식 데이터](https://harplab.github.io/harmonic/)
- Residual Copilot (`pr-1252`, CoRL 2026)을 REFERENCE에 등록했다. 같은 시도 수로 수집한 직접 조작과 보조 조작 시연으로 각각 Diffusion Policy를 학습해 기어 삽입 성공을 비교했다. 이 실험을 근거로 두 논문의 인용 관계를 연결했다. [논문 노트](../../2026/CoRL/2026_CoRL_Efficient-and-Reliable-Teleoperation-through-Real-to-Sim-t/01_overview.md) · [CoRL 공식 목록](https://www.corl.org/program/accepted-papers) · [원문 §IV-C와 표 II](https://arxiv.org/html/2603.17016#S4.SS3)
- DROID (`pr-0732`, RSS 2024)의 공식 게재 링크와 DOI를 추가하고, 수집 코드와 원시 시연 데이터의 공개 상태를 교정했다. [RSS 게재본](https://www.roboticsproceedings.org/rss20/p120.html) · [코드](https://github.com/droid-dataset/droid) · [원시 데이터 배포 안내](https://github.com/droid-dataset/droid/blob/33ae6a67274f36d2e29525b86f23a56616ef43a7/docs/the-droid-dataset.md)

현재 문서·코드·원장이 참조하지 않는 수집 입력과 과거 검토 파일 37개를 정리했다. 그중 등록 입력의 논문 항목 231건을 보존된 원장의 제목·별칭·공개 식별자·주소와 대조했다. 당시 입력 원본은 [정리 전 Git 이력](https://github.com/Kim-Yoo-Hyun/PaperReview/tree/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/sources)에서 복원할 수 있다.

전체 JSON Schema 검사에서 코드 저장소 14건의 `scope`가 허용 어휘를 벗어난 것을 확인했다. 저장소 루트 주소는 `project_landing`으로 통일했다. 공식 코드라는 구분, 실제 주소, 당시 확인일은 보존했다. 같은 값이 다시 들어오면 기존 수집 입력을 정상화하고 인식할 수 없는 값은 등록 전에 보고한다. [원장 스키마](../sources/registry.schema.json)

## 서지와 계보

OpenVLA의 인용 관계를 확인해 원장 내 관계 17건을 추가하고 기존 4건의 근거 위치를 보강했다. DINOv2 `pr-0006`는 2023년 arXiv 공개와 2024년 1월 TMLR 게재를 구분해 저널 경로를 교정했다. RT-2 `pr-0022`는 CoRL 게재본의 저자 순서와 공식 링크를 반영했다. [인용 계보](../../research/OPENVLA_LINEAGE.md) · [DINOv2 저널본](https://openreview.net/pdf?id=a68SUt6zFt) · [RT-2 게재본](https://proceedings.mlr.press/v229/zitkovich23a.html)

TrajOpt `pr-0558`의 기존 arXiv 식별자 1310.7730은 감마선 폭발에 관한 다른 논문이었다. 저자 사이트의 16쪽 PDF가 당시 본문 검토 SHA-256과 일치했고, 출판사 DOI에서 정식 표제와 IJRR 2014 게재를 확인했다. 이 ID의 폴더·노트·색인·과거 읽기 경로를 교정하고 이전 검토 당시의 표제와 경로를 보존했다. [교정된 논문](../../2014/IJRR/2014_IJRR_Motion-Planning-with-Sequential-Convex-Optimization-and-Co/01_overview.md) · [저자 배포본](https://rll.berkeley.edu/trajopt/ijrr/2013-IJRR-TRAJOPT.pdf) · [출판사 DOI](https://doi.org/10.1177/0278364914528132)

<a id="taxonomy-batches"></a>

## 첫 배치 태그 매핑

| 대상 축 | 배치의 기존 태그 | 판정 기준 |
|---|---|---|
| 방법론 · RL | `Reinforcement Learning`, `reinforcement-learning`, `real-world RL`, `offline reinforcement learning`, `offline-RL`, `implicit Q-learning`, `policy-gradient`, `Policy Gradient`, `actor-critic`, `advantage-estimation`, `reward-shaping`, `policy-invariance`, `potential-function`, `maximum entropy`, `variance-reduction`, `temporal difference`, `offline-to-online`, `reset-free learning` | 정책 최적화·보상·가치 학습이 기여일 때 RL. 성공 확률 보정에 TD를 쓴 경우는 별도다. |
| 방법론 · IL | `Imitation Learning`, `human demonstrations`, `policy distillation`, `human interventions` | 시연·교사 행동을 감독 신호로 학습하는지 확인한다. 사람이 개입했다는 사실만으로 결정할 수 없다. |
| 방법론 · 모델기반 / 고전제어 | `model predictive control`, `trajectory optimization`, `world model`, `Impedance Control`, `Planning`, `physics`, `replanning` | 동역학 또는 상태 전이를 계획·제어에 사용하면 모델기반, 임피던스 제어는 고전제어. 예측 모델 자체에는 플래너 역할을 부여하지 않는다. |
| 태스크 · 조작 | `3D manipulation`, `contact-rich manipulation`, `manipulation`, `manipulation policy`, `robot manipulation`, `real-world manipulation`, `dexterous manipulation`, `articulated objects`, `assembly`, `affordance`, `contact` | 논문이 다룬 물체 조작이나 평가 과업을 확인한다. 접촉·affordance는 단독 판정 근거가 아니다. |
| 태스크 · 이동 / 내비게이션 / 모바일매니퓰레이션 / 전신제어 | `locomotion`, `Navigation`, `Vision-Language Navigation`, `mobile manipulation`, `loco-manipulation`, `whole-body-control` | 보행 제어와 목적지 탐색을 구분한다. 이동 중 조작이나 전신 제어는 해당 과업이 확인되는 경우에 붙인다. |
| 로봇 형태 · 양팔 / 휴머노이드 / 사족보행 등 | `bimanual`, `bimanual manipulation`, `humanoid`, `legged robot`, `cross-embodiment` | 구성·기종을 확인한다. 다리형이라는 말에서 다리 수를, 여러 로봇이라는 말에서 로봇 종류를 추정할 수 없다. |
| 입력 · RGB / depth / 언어 / 기타 | `RGB-D`, `point cloud`, `sensor fusion`, `language grounding`, `open-vocabulary`, `Vision-Language Model`, `3D Scene Graph`, `topological-map` | 실제 모델·에이전트 입력만 기입한다. 점군·장면 그래프는 기타, RGB-D는 두 채널이 사용될 때 RGB와 depth다. |
| 데이터 · 인간영상 / 시뮬 / 합성 / 실제로봇 / 혼합 | `human video`, `human-video`, `synthetic data`, `simulation`, `robot data`, `robot dataset`, `community data`, `sim-to-real` | 모델 학습·벤치마크 구축에 쓴 데이터의 출처를 확인한다. 시뮬 정책의 실기 평가만으로 학습 자료가 혼합이 되지는 않는다. |
| VLA 전용 · 행동 표현 | `action tokenization`, `action tokens`, `action representation`, `action chunking`, `action-chunking`, `Diffusion`, `diffusion policy`, `Flow Matching`, `flow-matching`, `flow-policy`, `consistency policy`, `latent-action` | 실행할 행동을 생성하는 위치에서 표현을 판정한다. 이미지 확산, 자세 분포, 청크 길이, 사전학습용 토큰은 각각 다른 속성이다. |
| VLA 전용 · 백본 / 구조 / 학습 | `VLA`, `Vision-Language-Action`, `generalist policy`, `OpenVLA`, `CLIP`, `LLM`, `LLM planning`, `hierarchical policy`, `Transformer`, `pretraining`, `fine-tuning` | 행동 정책 자체의 설계·학습을 다룰 때만 적용한다. 언어 인코더, 백본과 정책 전체의 파라미터 수, 사전학습과 웹 동시학습을 구분한다. |
| 평가 · 데이터셋과 벤치마크 | `Benchmark`, `LIBERO`, `robomimic`, `robot-evaluation`, `policy-comparison` | 방법·실험 절에서 실제 사용이나 구축을 확인한 자원의 이름을 기록한다. |
| 직접 대응 없음 | `3D reasoning`, `3D representation`, `3D Vision`, `6D pose`, `active perception`, `alignment`, `calibration`, `continuous control`, `controllable generation`, `efficiency`, `efficient deployment`, `Embodied AI`, `failure detection`, `Gaussian Splatting`, `Generation`, `geometry`, `high-frequency control`, `inference efficiency`, `long-context`, `long-horizon tasks`, `multi-hypothesis`, `NVIDIA`, `offline learning`, `policy learning`, `real-time-control`, `Robotics`, `sample efficiency`, `semantic`, `SLAM`, `symmetry`, `uncertainty`, `visuomotor control` | 세부 기술·연구 목적·관련 분야는 이전 태그로 보존한다. 공통 축 값이 필요하면 해당 논문의 방법·평가에서 별도로 확인한다. |

이 표는 원문 감사 50편의 이전 태그 127종(225회)을 모두 포함한다. 같은 논문에 여러 방법·태스크·모달리티를 기록할 수 있다. 공개 수준은 태그로 변환하지 않고 저자의 배포처에서 코드·가중치·데이터를 각각 확인한다. [표본과 원문](../../research/SOURCE_AUDIT.md#이전-감사)

**적용 결과.** CORE 30편은 부록 등급 1, NEXT 20편은 등급 2로 기록했다. 50편 모두 저자 목록·소속·한 줄 요약·핵심 기여 2개와 출처가 있다. 소속은 논문에 표시된 기관의 목록이다. `id`는 원장의 연도와 선택한 공식 서지의 선두 저자 성을 사용하며, `registry_id`로 원장의 `paper_id`와 연결한다. `changed_from`에는 배치 생성 직전의 ID·등급·평면 태그·facets·발표처·링크·공개 상태와 원장에 있던 문제·방법 설명을 보존했다. 기존에 없던 축은 새로 작성했다. [첫 배치 YAML](../sources/batches/core_next_01.yaml) · [원장 연결](../sources/registry_meta.json)

| 저자 배포물 | Y | 부분 | N | unknown |
|---|---:|---:|---:|---:|
| 코드 | 40 | 3 | 1 | 6 |
| 가중치 | 16 | 8 | 0 | 26 |
| 데이터 | 15 | 7 | 1 | 27 |

11월 19일 첫 판정 후 11월 24일 SayCan·Habitat·RLDG·3D Diffusion Policy의 가중치를 `unknown`에서 `부분`으로 갱신했다. 각각 모의 탁상 정책, PointNav PPO, 커넥터 삽입 학생 정책, 시연 생성용 RL 전문가의 파일을 확인했다. [변경 전 값과 출처](../sources/batches/core_next_01.yaml) · [논문별 배포 파일](../../research/SOURCE_AUDIT.md#core-공개-자료)

Y는 논문에 대응하는 저자 배포를 확인한 경우, 부분은 확인한 배포 범위가 일부 구성요소·과제·파일에 한정된 경우다. N은 저자가 미배포 또는 공개 예정임을 명시한 경우다. 배포 근거가 부족하면 `unknown`으로 둔다. 이 양식에는 ‘해당 없음’ 값이 없어 자체 가중치나 실험 데이터가 없는 연구는 `unknown`을 유지하고 그 근거를 각 항목의 `notes`에 적었다. [분류 원장](../sources/batches/core_next_01.yaml) · [CLIP 학습 데이터](https://github.com/openai/CLIP/blob/main/model-card.md#data)

- **공통 태그.** 데이터 출처는 해당 논문의 학습·벤치마크 구축 자료를 기준으로 한다. 여러 출처를 사용하면 `혼합`으로 표기한다. RFMPose는 합성 자료로만 학습한 뒤 실제 관측에서도 평가해 `합성`이다. `기타`는 점군 등 허용된 나머지 범주의 구체적인 입력·형태가 확인된 경우에 쓴다. [RFMPose](https://proceedings.neurips.cc/paper_files/paper/2025/hash/618c0a236e7aace748d09bc8fbed3e4d-Abstract-Conference.html)
- **전용 태그.** VLA나 Octo처럼 언어 지시로 여러 로봇의 행동을 생성하는 범용 정책을 설계·학습한 13편에 VLA 항목을 붙였다. 휴머노이드 기종이나 시뮬레이션 모델을 실제 사용한 10편에는 역할을 함께 적었다. 두 집합은 겹친다. FAST의 H1은 행동 토큰화 데이터에 등장한다. Ψ₀는 G1에서 전신 행동을 실행하며 기존 RL 하체 추종기를 사용한다. [FAST](https://arxiv.org/html/2501.09747) · [Ψ₀](https://www.roboticsproceedings.org/rss22/p021.html)
- **한계와 선행.** 저자가 적은 제약·평가 범위는 27편, 후속 논문이 설명한 제약은 2편에서 출처를 연결했다. 선행 ID는 배치 안에서 부록 ID, 배치 밖에서는 원장의 안정 ID를 사용한다. 문헌 관계를 확인한 27편에 기록했다. `unknown`은 확인 범위를 나타내며 선행이나 한계가 없다는 뜻으로 쓸 수 없다.
- **검증 수준.** 서지와 기여를 대조한 50편 각각에 공개 여부·세부 축·후속 연구 한계 등 미확정 필드가 남아 레코드 전체는 `부분확인`이다. `미공개`는 저자가 실제로 그렇게 명시할 때 사용한다. [기존 감사와 수정 범위](../../research/SOURCE_AUDIT.md#이전-감사)

**애매한 매핑 질문**

1. 웹 이미지–텍스트 대조학습·생성 모델과 자세 추정에 독립적인 방법 태그를 둘 것인가? 현재 어휘로 표현하기 어려운 CLIP·DDPM·RFMPose의 방법론은 `unknown`으로 두었다.
2. 연속 행동의 직접 회귀와 일관성 모델을 확산·flow와 별도 값으로 관리할 것인가? OFT의 L1 직접 회귀는 행동 표현 설명에 보존하고 전용 enum은 `unknown`으로 두었다.
3. UMI처럼 사람이 들고 움직이는 계측 그리퍼 시연을 데이터 출처로 추가할 것인가? 카메라 영상과 그리퍼 궤적을 함께 쓰므로 현재 분류에서 `unknown`으로 두었다. 미공개와 미확정을 구분하는 근거도 논문별로 기록한다.

**중복 후보**는 0쌍이다. 배치 내부 1,225쌍과 배치↔나머지 원장 58,850쌍에서 공개 식별자(DOI·버전 제외 arXiv·OpenReview), 정규화 제목과 유사 제목을 검사했다. 제목의 대폭 변경과 식별자 결측이 겹치는 경우에는 한계가 있다. [유사도 판정 기준](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/92d86a2ebcd2c2b99e32ff79424a5f2cd2eee747/research/REGISTRY_AUDIT.md#3-중복-의심)

## 두 번째 배치 태그 매핑

2026-11-24에 첫 배치와 겹치지 않는 CORE 20편 전부와 안정 ID 순으로 다음 NEXT 30편을 정규화했다. 이 시점의 누계는 CORE 50편, NEXT 50편이며, 별도 등록 심사를 거친 NEXT 23편까지 합한 표본은 123편이었다. 각 레코드에는 원문의 URL, 쪽수와 SHA-256, 교정 전 값이 있다. [두 번째 배치 50편](../sources/batches/core_next_02.yaml) · [첫 배치 50편](../sources/batches/core_next_01.yaml) · [별도 등록 23편](../sources/batches/gapfill_2026_11.yaml)

| 기존 표기 | 원문에서 확인할 조건 | 기록할 축 |
|---|---|---|
| `Imitation Learning`, `diffusion policy`, `teleoperation` | 시연 행동을 예측하는 손실로 정책을 학습하는가 | 방법에 IL. 원격조작으로 자료만 수집한 경우에는 데이터 수집 방식에 기록한다. |
| `offline reinforcement learning`, `Q-learning`, `recovery policy` | 보상·가치·제약 비용을 학습이나 행동 선택에 사용하는가 | 방법에 RL. 보상 조건부 시퀀스 예측은 목적과 최적화 방식을 함께 적는다. |
| `VLA`, `Vision-Language Model`, `Graph Reasoning` | 영상과 지시에서 직접 행동을 생성하는가, 별도 제어기에 계획·좌표·진단을 제공하는가 | 입력의 언어와 행동 출력을 구별한다. VLA 전용 필드는 정책을 제안하거나 직접 학습한 논문에 적용한다. |
| `3D Vision`, `Gaussian Splatting`, `Planning` | 실제 관측 센서와 모델 내부의 추정량은 무엇이며, 행동 후보를 어떤 모델로 평가하는가 | 카메라에서 받은 깊이와 RGB에서 추정한 깊이를 구별한다. 점군은 입력에 해당할 때 기타로, 상태 전이를 예측해 계획할 때만 방법에 모델기반을 적는다. |
| `Navigation`, `mobile manipulation`, `bimanual manipulation` | 목표까지 이동하는가, 이동과 조작을 함께 수행하는가, 두 팔을 실제로 사용하는가 | 태스크와 로봇 형태를 각각 기록한다. 수집 기체·평가 기체가 다른 경우 그 역할을 적는다. |
| `Dataset`, `Benchmark`, `real robot` | 학습·구축 자료의 출처와 평가 환경을 각각 식별할 수 있는가 | 데이터 출처는 학습·구축에 쓴 자료를 기준으로 정한다. 실제 기기에서의 평가만 확인되면 평가 조건에 기록한다. |

**남은 분류 질문.** 행동의 직접 회귀·복셀 선택, 로봇 과제와 무관한 점군 분할·이미지 생성은 현재 열거값에 어디까지 포함할 것인가? 열거값으로 표현할 수 없는 축에는 `unknown`을 사용하고 실제 출력과 평가 대상을 해당 논문의 설명에 남긴다.

**확인 범위.** 이번 50편 중 축 전체가 `unknown`인 논문은 방법 8편, 태스크 6편, 기체 6편, 입력 0편, 데이터 출처 2편이다. VLA·언어 조건부 행동 정책 17편과 휴머노이드 5편에는 전용 필드를 적용했고 SOMA가 양쪽에 속한다. 원문이 직접 밝힌 한계를 연결한 논문은 34편, 후속 연구가 지적한 한계를 직접 연결한 논문은 3편이다. 50편 모두 레코드 단위로는 `부분확인`이다. [원문 위치와 분류](../sources/batches/core_next_02.yaml)

| 공개 범위 | Y | 부분 | N | 미확인 |
|---|---:|---:|---:|---:|
| 코드 | 33 | 5 | 4 | 8 |
| 가중치 | 4 | 16 | 0 | 30 |
| 데이터 | 0 | 22 | 1 | 27 |

‘부분’은 특정 과제·구성요소·분할의 파일을 확인한 경우다. ‘N’ 다섯 건에는 저자의 공개 예정 안내가 있다. ‘미확인’에는 배포를 확인할 수 없거나 원장의 ‘해당 없음’을 Y/N으로 옮길 수 없는 항목이 포함된다. 22편에서 배포 파일 근거 34건, 공개 예정 안내 5건, 배포 미확인으로 바로잡은 데이터 1건을 원장에도 반영했다. VoxAct-B의 `pretrained_weights.zip`에는 지각 모델 가중치가 들어 있으며 양팔 정책과 훈련 시연은 각각 다른 경로로 배포된다. [VoxAct-B 저자 배포 안내](https://github.com/VoxAct-B/voxactb/blob/1cc074b1730f52a7fd35d069d8c9099d18718bca/README.md) · [원장 감사](../../research/SOURCE_AUDIT.md#다축-태그와-공개-자료)

- 14편에서 표제면의 저자 표기·순서를 반영했다. PointNet은 Charles R. Qi와 Kaichun Mo의 이름 순서를 교정했다. RT-2의 PMLR 웹 서지는 Brianna Zitkovich로, 게재 PDF는 Anthony Brohan으로 시작한다. 두 판본 표기와 기존 명단을 보존했다. [PointNet 게재본](https://openaccess.thecvf.com/content_cvpr_2017/papers/Qi_PointNet_Deep_Learning_CVPR_2017_paper.pdf#page=1) · [RT-2 웹 서지](https://proceedings.mlr.press/v229/zitkovich23a.html) · [RT-2 게재본](https://proceedings.mlr.press/v229/zitkovich23a/zitkovich23a.pdf#page=1)
- IGL-Nav는 자세가 주어진 RGB-D 관측으로 지도를 구축한다. 목표 사진의 깊이와 카메라 내부 파라미터가 필요하며 단안 추정값을 쓴 조건도 평가했다. VISTA는 실측 장면에서의 시점 비교와 쿼드로터·Spot에서의 실제 탐색을 각각 평가했다. 두 논문의 개요와 감사 원장에 원문 위치를 반영했다. [IGL-Nav §3.1](https://openaccess.thecvf.com/content/ICCV2025/papers/Guo_IGL-Nav_Incremental_3D_Gaussian_Localization_for_Image-goal_Navigation_ICCV_2025_paper.pdf#page=3) · [IGL-Nav §5](https://openaccess.thecvf.com/content/ICCV2025/papers/Guo_IGL-Nav_Incremental_3D_Gaussian_Localization_for_Image-goal_Navigation_ICCV_2025_paper.pdf#page=8) · [VISTA §V](https://arxiv.org/pdf/2507.01125#page=7)
- **중복 후보 0쌍.** 이번 배치 내부 1,225쌍, 나머지 원장과 60,100쌍에서 DOI·버전을 제외한 arXiv ID·OpenReview ID, 정규화 제목과 유사 제목을 대조했다. 공개 식별자가 없으면서 제목이 크게 바뀐 판본은 이 방법으로 놓칠 수 있다. [기존 유사도 기준](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/92d86a2ebcd2c2b99e32ff79424a5f2cd2eee747/research/REGISTRY_AUDIT.md#3-중복-의심)

## 세 번째 배치 태그 매핑

| 기존 표기 | 원문에서 구별할 역할 | 템플릿 4에 반영할 값 |
|---|---|---|
| Scene graph, Gaussian splatting, world model | 장면을 기술하는지, 행동을 바꾸었을 때의 결과를 예측해 계획하는지 | 예측 모델로 행동을 선택하면 모델기반으로 기록한다. 지도 구축 자체에 대응하는 방법 값은 `unknown`이다. |
| Imitation, offline RL, demonstrations | 시연 행동을 모방하는 손실과 보상·가치 기반 갱신이 각각 학습에 쓰이는지 | 행동을 모방하면 IL, 보상으로 갱신하면 RL을 부여한다. 두 목적함수를 모두 쓰면 두 값을 기록한다. |
| Point cloud, state, vision | 센서 관측, 파생된 점군, 학습 시에만 보는 상태 중 무엇이 행동이나 추정의 입력인지 | 입력 역할을 본문과 대조해 RGB·depth·고유수용감각·기타를 선택한다. |
| Real robot, sim-to-real, benchmark | 데이터를 모은 곳과 평가를 수행한 곳이 어디인지 | 학습·지도 구축 자료의 출처를 기록하고, 실기 평가와 기체는 별도로 적는다. |
| Public code, pretrained, dataset | 해당 논문의 구현·학습 결과·수집 자료가 어느 경로에 어떤 파일로 있는지 | 저자 배포 파일의 범위로 Y·부분을 정한다. 외부 기반 모델이나 데이터 생성 명령만 있는 경우에는 해당 산출물의 공개를 미확인으로 둔다. |

2026-11-24에 Clio부터 PIN-WM까지 미처리 NEXT 50편의 원문과 공개 자료를 대조했다. 세 배치 150편과 별도 등록한 23편을 합하면 집중 읽기 대상 500편 중 **173편(34.6%)**에 같은 축의 태그가 있다. 나머지는 NEXT 327편이다. 이번 배치는 50편 모두 레코드 단위로 `부분확인`이다. 원문이 명시한 한계 25편, 후속 연구가 지적한 한계 5편, 등록 논문 사이의 직접 선행 관계 19건을 쪽수와 연결했다. [논문별 원문·이전 값](../sources/batches/core_next_03.yaml) · [다음 배치](../../TODO.md)

| 공개 범위 | Y | 부분 | N · 저자 공개 예정 | 미확인 |
|---|---:|---:|---:|---:|
| 코드 | 33 | 5 | 2 | 10 |
| 가중치 | 1 | 11 | 0 | 38 |
| 데이터 | 0 | 17 | 0 | 33 |

공개 범위 150개 중 67개는 배포 파일을 확인했고, 2개는 저자가 구현 공개를 예고했다. 남은 81개에는 실험 자료가 있는데도 기존 원장이 ‘해당 없음’으로 표시했던 6개가 포함된다. 예를 들어 DAPG는 네 과제의 정책과 시연을 배포했다. RoboPack은 촉각 동역학 체크포인트가 열리지만 저자의 표본 데이터 링크는 HTTP 404다. 학습 곡선·점수만 배포한 연구는 데이터 ‘부분’으로 표시하고 원시 전이 공개 여부를 따로 적었다. [DAPG 정책·시연](https://github.com/aravindr93/hand_dapg/tree/master/dapg) · [RoboPack 배포 안내](https://github.com/BoAi01/robopack) · [감사 집계](../../research/SOURCE_AUDIT.md#다축-태그와-공개-자료)

- **방법과 기체.** PointVLA의 시연 기반 미세조정과 WMNav의 학습 없는 계획에서 기존 강화학습 태그를 교정했다. RoboPanoptes는 카메라가 분산된 다관절 몸체로 쓸기·개봉·정리를 평가해 전신 조작으로 분류했다. 49편의 기존 검색 태그를 원문으로 확인했다. World Models의 게임 평가는 CarRacing·VizDoom에 한정되어 기존 Robotics 태그의 실험상 근거는 유보했다. [PointVLA §III–IV](https://arxiv.org/pdf/2503.07511#page=5) · [WMNav 표 I](https://arxiv.org/pdf/2503.02247#page=6) · [RoboPanoptes §III](https://www.roboticsproceedings.org/rss21/p042.pdf#page=3)
- **판본과 수치.** 8편의 저자 표기·순서를 교정했다. PointVLA는 RA-L 서지의 5명과 저자판 표제면의 6명을 구분했다. Q-Transformer의 실물 평가는 72개 과제다. 셋째 범주의 과제 수는 §5.1 본문에 48개, 그림 4에 47개로 인쇄되어 있다. [PointVLA 게재 서지](https://doi.org/10.1109/LRA.2026.3653303) · [PointVLA 저자판](https://arxiv.org/pdf/2503.07511#page=1) · [Q-Transformer §5.1·그림 4](https://proceedings.mlr.press/v229/chebotar23a/chebotar23a.pdf#page=6)
- **남은 분류 질문.** 장면 그래프 구축·지도화와 지도학습 기반 파지 자세 추정은 현행 방법 열거값으로 구분하기 어렵다. 방법 9편, 태스크 2편, 기체 1편, 데이터 출처 2편은 축 전체를 `unknown`으로 두고 실제 수행 역할을 서술했다. 입력 축은 50편에서 확인했다. VLA 전용 필드는 4편, 휴머노이드 전용 필드는 3편에 적용했다. [논문별 분류](../sources/batches/core_next_03.yaml)
- **중복 후보 0쌍.** 배치 내부 1,225쌍과 나머지 원장과의 60,100쌍에서 공개 식별자, 정규화한 제목·별칭, 유사 제목을 대조했다. 공통 식별자 없이 제목이 크게 달라진 판본은 판별하기 어렵다. [중복 검사 기준](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/92d86a2ebcd2c2b99e32ff79424a5f2cd2eee747/research/REGISTRY_AUDIT.md#3-중복-의심)

## 네 번째 배치 태그 매핑

| 기존 표기 | 원문에서 확인하는 내용 | 사용하는 축 |
|---|---|---|
| World model, policy optimization, model predictive control | 예측 영상을 훈련 환경으로 쓰는지, 정책 점수만 매기는지, 실행 중에 모델로 행동을 계획하는지 구분한다. | 보상으로 정책을 갱신하면 RL, 예측 전이를 이용해 계획·학습하면 모델기반을 기록한다. |
| Tactile sensing, force sensing, RGB-D | 광학식 촉각 영상, 손목 힘·토크, 장면 카메라와 추정한 깊이의 역할을 확인한다. | 접촉면 촉각, 힘·토크(기타), 장면 RGB와 센서 depth를 구별한다. |
| VLA, failure detection, benchmark, memory | 해당 논문이 언어 조건부 행동 정책을 학습하는지, 기존 정책의 실패를 검출하거나 시험하는지 확인한다. | 전용 필드는 직접 학습·제안한 정책에 붙이고 평가한 정책은 별도로 명시한다. |
| Human video, teleoperation, simulation | 사람이 물체를 다룬 영상인지, 사람이 로봇을 조작해 기록한 궤적인지, 시뮬레이터가 생성한 예제인지 확인한다. | 학습·데이터셋 구축의 출처를 기록하고 실물 평가 조건은 따로 적는다. |
| Code, model, dataset | 저자 배포처에서 구현, 체크포인트, 학습·평가 파일을 개별 확인한다. | 제3자의 백본과 생성 스크립트는 원 논문의 가중치나 데이터 배포로 집계하지 않는다. |

11월 25일 *Dexterous World Models*부터 *Memory Retrieval in Visuomotor Policies*까지 NEXT 50편을 정규화했다. 네 배치 200편과 별도 등록 23편을 합해 집중 읽기 500편 중 **223편(44.6%)**에 다축 분류가 있다. 다음 대상은 NEXT 277편이다. 배치 내부 1,225쌍과 나머지 원장과의 60,100쌍에서 DOI·버전을 제외한 arXiv ID·OpenReview ID, 제목·별칭과 유사 제목을 대조한 결과 중복 후보는 0쌍이었다. [50편의 원문 쪽수·배포처·변경 전 값](../sources/batches/core_next_04.yaml) · [다음 배치](../../TODO.md)

| 공개 범위 | Y | 부분 | N · 저자 공개 예정 | 미확인 |
|---|---:|---:|---:|---:|
| 코드 | 31 | 9 | 3 | 7 |
| 가중치 | 0 | 20 | 0 | 30 |
| 데이터 | 0 | 28 | 2 | 20 |

43편에서 배포 파일 88건과 저자의 공개 예정 안내 5건을 원장에 연결했다. 나머지 57건은 미확인이다. AT-VLA는 추론 구현을 공개했다. ActiveVLA는 구현·데이터 준비를 명시했고, 연결한 모델 저장소에는 가중치 파일이 없었다. FlowDreamer에서 확인한 파일은 깊이 추정 모듈이다. [AT-VLA 배포 안내](https://github.com/clorislili/AT-VLA) · [ActiveVLA 공개 안내](https://github.com/ZhenyangLiu/ActiveVLA-Injecting-Active-Perception-into-VLA) · [FlowDreamer 배포 파일](https://huggingface.co/sharinka0715/flowdreamer_pretrained/tree/main/depth_anything)

- **다시 열린 출처.** UniSim의 실제 데모 페이지와 IndustReal의 저자 프로젝트를 찾아 링크를 교체했다. IndustReal은 실물 페그 삽입 정책 가중치도 공개했다. PDDLStream은 종전 OJS 주소가 자동 접속 확인 화면을 반환해 AAAI가 배포하는 같은 게재본으로 교체했다. PDF의 SHA-256은 이전 요약 감사와 일치한다. 이번 50편 모두 현재 링크 항목을 통과했다. [UniSim 데모](https://universal-simulator.github.io/unisim/) · [IndustReal 배포처](https://github.com/NVlabs/industreallib) · [PDDLStream 게재본](https://cdn.aaai.org/ojs/6739/6739-40-9968-1-10-20200522.pdf)
- **방법과 평가.** WMPO의 모델 예측 제어 태그를 세계 모델 안에서의 GRPO 정책 최적화로 교정했다. Counterfactual VLA는 주행 로그에서 반사실적 추론으로 궤적 예측을 수정한다. PALM 그림 4와 표 5의 실물 평가는 여섯 하위 동작을 하나의 지시로 수행하는 과제 한 개다. [WMPO §3–4](https://proceedings.iclr.cc/paper_files/paper/2026/file/6605c7d1c1ae1521b328d036df5be1ae-Paper-Conference.pdf) · [Counterfactual VLA §3–4](https://openaccess.thecvf.com/content/CVPR2026/html/Peng_Counterfactual_VLA_Self-Reflective_Vision-Language-Action_Model_with_Adaptive_Reasoning_CVPR_2026_paper.html) · [PALM 실물 평가](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_CVPR_2026_paper.pdf#page=8)
- **저자와 판본.** 게재본 표제면을 기준으로 저자 표기 10편을 교정하고 이전 서지를 보존했다. Octopi의 둘째 저자는 Kelvin Lin, Reactive Diffusion Policy의 다섯째 저자는 Yuan Fang이다. TactAlign은 Akash Sharma의 소속이 게재본과 저자판에서 달라 판본을 함께 표시했다. [Octopi 표제면](https://www.roboticsproceedings.org/rss20/p066.pdf#page=1) · [Reactive Diffusion Policy 표제면](https://www.roboticsproceedings.org/rss21/p052.pdf#page=1) · [TactAlign 게재본](https://www.roboticsproceedings.org/rss22/p006.pdf#page=1) · [TactAlign 저자판](https://arxiv.org/pdf/2602.13579#page=1)
- **남은 분류 질문.** 촉각 표현의 자기지도 학습, 실패 검출기 보정, 그래프에서의 이동 후보 선택에는 현행 방법·행동 표현 어휘를 어디까지 적용할 것인가? 공통 방법 축 14편, 기체 4편, 자료 출처 4편은 확인한 사실을 서술하고 해당 축은 `unknown`으로 두었다. 언어 조건부 행동 정책 15편과 G1 상지 조작 1편에 전용 필드를 붙였다. 50편 모두 레코드 단위로는 `부분확인`이다. 원문이 명시한 한계·적용 조건 22편, 후속 연구에서 지적한 한계 1편, 직접 선행 16건에는 해당 쪽을 연결했다. [분류와 증거](../sources/batches/core_next_04.yaml) · [원문 감사](../../research/SOURCE_AUDIT.md#다축-태그와-공개-자료)

## 다섯 번째 배치 태그 매핑

| 기존 검색어·표기 | 원문에서 확인한 분류 기준 |
|---|---|
| task and motion planning, model predictive control | LGP·FFRob의 기하 제약과 MPPI의 미래 궤적 최적화를 `모델기반`으로 기록했다. 경험으로 정책을 개선한 경우에만 RL을 부여했다. |
| representation learning, robot data | R3M의 사람 영상 사전학습과 로봇 행동 복제에 쓰인 자료를 구분했다. Dense Object Nets의 픽셀 대응 학습은 방법 축에 맞는 값이 없어 `unknown`이다. |
| humanoid, dexterous manipulation | 고정 손목의 Allegro Hand, 팔에 장착한 다지 손, GR-1·H1의 상지 조작, 시뮬레이터가 지원하는 보행을 구별했다. |
| VLA, world model, diffusion | RT-H의 공유 모델, CodeDiffuser의 고수준 지각 코드와 저수준 확산 정책, FOREWARN의 기존 행동 후보 평가를 원문에 따라 구분했다. |
| RGB-D, tactile sensing | 입력 경로를 확인했다. SpatialVLA는 RGB에서 깊이를 추정하고, UniVLA는 실물 RGB-D 카메라의 RGB만 쓴다. DIGIT의 접촉 영상은 촉각으로 분류했다. |
| code, weights, data | 드라이버·센서 보정 모델·장면별 파라미터·궤적은 확인한 구성요소와 파일을 명시했다. 공개 예고와 배포 파일 미확인은 따로 기록했다. |

11월 25일 *DexterityGen*부터 *RoboSplat*까지 NEXT 50편의 원문을 대조했다. 다섯 배치 250편과 별도 등록 NEXT 23편을 합쳐 집중 읽기 500편 중 **273편(54.6%)**에 다축 태그가 있다. 각 레코드에 원문 쪽수, 판본 식별용 SHA-256, 변경 전 값과 공개 근거를 기록했다. [논문별 분류](../sources/batches/core_next_05.yaml) · [다음 50편](../../TODO.md)

| 자료 | 공개 Y | 부분 공개 | 공개 예정 N | 미확인 |
|---|---:|---:|---:|---:|
| 코드 | 26 | 10 | 1 | 13 |
| 가중치 | 1 | 18 | 1 | 30 |
| 데이터 | 2 | 21 | 1 | 26 |

- **공개 범위.** 원 DIGIT은 센서 드라이버를 배포했다. 기존 링크는 후속 센서 DIGIT 360을 가리켰다. DexGen의 공개 링크는 파지 최적화 모듈까지 확인된다. CodeDiffuser는 시뮬레이션 코드가 있고 실물 배포 코드와 데이터·체크포인트 다운로드는 저자 목록에 미완료로 표시돼 있다. [DIGIT 설계·드라이버](https://digit.ml/digit.html) · [DexGen](https://zhaohengyin.github.io/dexteritygen/) · [CodeDiffuser 배포 안내](https://github.com/lyttttt3333/CodeDiffuser)
- **서지와 실험 조건.** 15편의 저자 표기·순서를 교정했다. RoboVerse 게재본의 37명 중 기존 목록에서 빠진 세 사람은 Yen-Jen Wang, Dylan Goetting, Carlo Sferrazza다. CordViP의 실물 실험은 UR5 한 대와 LEAP Hand 구성으로, 기존 양팔 검색 태그를 교정했다. [RoboVerse 표제면](https://www.roboticsproceedings.org/rss21/p022.pdf#page=1) · [CordViP 실물 구성](https://www.roboticsproceedings.org/rss21/p110.pdf#page=6)
- **중복 후보.** 배치 내부 1,225쌍과 나머지 원장과의 60,100쌍에서 식별자와 제목·별칭을 대조했다. 제목 유사도로 잡힌 두 쌍은 GR00T N1(`pr-0869`)과 각각 N1.5(`pr-0917`), N1.6(`pr-0918`)이었다. 저자가 구분해 배포한 후속 버전이므로 세 ID를 유지했다. [N1 모델 카드](https://huggingface.co/nvidia/GR00T-N1-2B) · [N1.5 변경점](https://research.nvidia.com/labs/gear/gr00t-n1_5/) · [N1.6 변경점](https://research.nvidia.com/labs/gear/gr00t-n1_6/)
- **남은 분류 질문.** 자기지도 시각 대응(Dense Object Nets), 센서 융합 자세 추적(V-HOP), 로봇 데이터 수집 시스템(AutoRT)에 별도 방법 태그가 필요한가? 세 편은 현행 방법 축에 `unknown`을 썼다. VLA 및 휴머노이드 전용 필드는 각각 10편에 작성했고, 원문 한계 30편과 직접 선행 관계 13건에는 페이지를 붙였다. 50편 모두 레코드 종합 판정은 `부분확인`이다. [배치 원장](../sources/batches/core_next_05.yaml) · [공개 자료 감사](../../research/SOURCE_AUDIT.md#다축-태그와-공개-자료)

## 여섯 번째 배치 태그 매핑

| 기존 검색어·표기 | 원문의 구분과 정규화 |
|---|---|
| lifelong learning, goal-conditioned policy | GOAT는 탐색 중 물체 기억을 누적한다. 조작·이동의 기종 간 학습은 목표 이미지를 사용한다. 각각 `lifelong navigation`, `image-goal policy`로 교정했다. |
| flow, diffusion, action chunk | FlowPolicy의 단일 단계 흐름 생성과 DSRL의 고정 확산 정책 노이즈 제어를 구분했다. Q-chunking과 DQC에서 행동 묶음은 강화학습 가치 함수의 입력이다. |
| world model, VLA post-training | VLAW는 성공 궤적을 골라 흐름 목적함수로 정책을 갱신한다. VLA-MBPO는 세계 모델에서 만든 짧은 궤적으로 강화학습한다. |
| humanoid, whole-body control, navigation | GR00T의 실물 조작·이동 조작, NavDP·LoGoPlanner의 G1 경로 추종, OGBench·DQC의 모의 휴머노이드 목표 도달을 분리했다. |
| sim-to-real, real-world | SimpleVLA-RL의 네 실물 과제에 적용한 정책은 시뮬레이션 자료로 학습했다. RLinf-VLA의 실물 서랍 닫기는 실물 시연과 모의 궤적을 함께 사용했다. |

11월 25일 *PartInstruct*부터 *OopsieVerse*까지 NEXT 50편을 검토했다. 집중 읽기 500편 중 **323편(64.6%)**에 다축 태그가 있다. 공식 정규화 여섯 배치의 CORE 50편·NEXT 250편에 별도 등록한 NEXT 23편을 더한 수다. PDF 48편은 원문 쪽수와 SHA-256을, NVIDIA 웹 기술 보고서 두 편은 절 제목과 HTML SHA-256을 기록했다. AAAI 6편은 발행사가 기탁한 DOI 서지도 대조했다. 이 중 3편은 이전에 확인한 게재본과 해시가 동일한 사본을 사용했고 OC-VLA·MP1·Neural Assembler의 이번 쪽수는 저자 공개 판본 기준이다. [논문별 근거와 이전 값](../sources/batches/core_next_06.yaml)

| 저자 배포물 | Y | 부분 | N | 미확인 |
|---|---:|---:|---:|---:|
| 코드 | 38 | 5 | 0 | 7 |
| 가중치 | 3 | 19 | 0 | 28 |
| 데이터 | 0 | 21 | 1 | 28 |

86건에서 논문에 대응하는 배포 파일을 확인했다. 77건은 파일 내용을 일부 읽었고, 6건은 이용 동의가 필요한 저장소에서 리비전·파일명·크기를, 3건은 저자가 공유한 Drive 파일의 이름과 상세 페이지를 확인했다. SocialNav 저자는 원래 학습 코퍼스의 미공개 사유를 명시하면서 별도로 개편한 평가 벤치마크를 안내한다. GO-1과 GR00T N1.5·N1.6은 해당 모델의 배포 리비전을 각각 확인했다. [SocialNav 배포 안내](https://github.com/AMAP-EAI/SocialNav#-dataset--benchmark) · [N1.5](https://huggingface.co/nvidia/GR00T-N1.5-3B) · [N1.6](https://huggingface.co/nvidia/GR00T-N1.6-3B)

LoGoPlanner에 연결돼 있던 X-NavDP 체크포인트를 LoGoPlanner 전용 파일로 교체했다. Gemini Robotics 1.5의 프로젝트 주소는 2.5가 표시되는 제품 페이지에서 1.5 발표 당시의 공식 페이지로 바꿨다. RLinf-VLA의 실물 서랍 닫기에서는 지도 미세조정(SFT) 정책과 시뮬레이션 RL을 추가한 정책이 각각 8/10회 성공했다. 논문은 같은 성공 횟수에서 밀기 동작의 효율 차이를 보고했다. [LoGoPlanner 배포](https://huggingface.co/InternRobotics/LoGoPlanner) · [Gemini Robotics 1.5 발표](https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/) · [RLinf-VLA 실물 평가](https://www.roboticsproceedings.org/rss22/p089.pdf#page=9)

50편 내부 1,225쌍과 나머지 1,202편과의 60,100쌍에서 제목·별칭·식별자를 비교했다. 유사 후보 네 쌍은 GR00T N1·N1.5·N1.6 사이의 세 쌍과 NavDP·LoGoPlanner 한 쌍이었다. 저자 사이트의 별칭 `NavDP--`는 구두점을 제거하면 `NavDP`와 일치한다. 원문과 배포 버전에서 네 쌍 모두 다른 연구로 확인했다. [GR00T N1.5 보고서](https://research.nvidia.com/labs/gear/gr00t-n1_5/) · [N1.6 보고서](https://research.nvidia.com/labs/gear/gr00t-n1_6/) · [LoGoPlanner의 별칭과 선행 연구](https://steinate.github.io/logoplanner.github.io/)

분류상 남은 질문은 연속 행동을 직접 회귀하는 정책을 확산·흐름과 별도 값으로 표현할지, SIMPLER 같은 평가 중심 논문을 어떤 방법 태그로 검색할지다. RoboFlamingo·GR-1의 행동 회귀와 SIMPLER의 평가 역할을 근거에 적고 해당 축은 `unknown`으로 두었다. VLA 전용 필드 19편, 휴머노이드 전용 필드 11편, 저자 명시 한계 29편, 근거 위치를 확인한 직접 선행 관계 16건을 기록했다. [정규화 원장](../sources/batches/core_next_06.yaml) · [공개 자료 감사](../../research/SOURCE_AUDIT.md#다축-태그와-공개-자료)

## 일곱 번째 배치 태그 매핑

| 기존 검색어·표현 | 원문을 확인한 뒤의 분류 |
|---|---|
| VLA, proprioception, robustness | DISC는 지시와 상태가 제어에 기여하는 경로를 나눈다. GAP는 시각·고유수용 입력 간 불균형을 다루는 모방학습이다. 비슷한 검색어로 등록된 두 CoRE-VLA 논문은 각각 전문가 선택과 카메라 시점 복원을 다룬다. |
| action chunking, control frequency | KineDex는 행동 청크의 압축과 고주파 복호화를 학습한다. RTC와 AAC는 이미 학습한 정책을 실행할 때 청크의 경계 또는 길이를 바꾼다. |
| reward learning, evaluation | Robometer와 RoboReward의 예측 대상은 진행도·보상이다. STEP은 정책 두 개의 성공·실패를 받아 비교 실험을 언제 끝낼지 결정한다. |
| robot data, real-robot, sim-to-real | 정책 학습, 센서 보정, 실물 평가에 쓰인 자료를 구분했다. DyGRO-VLA의 실물 네 과제는 시뮬레이션 학습 이후의 전이 평가다. |

2026년 11월 25일 *USER*부터 *TidyBot++*까지 NEXT 50편을 정규화했다. 일곱 배치 350편과 별도 등록한 NEXT 23편은 서로 겹치지 않는다. 집중 읽기 500편 중 **373편(74.6%)**을 마쳤다. 50편의 방법·평가 쪽수와 PDF 해시를 남겼고, 종전 요약 감사에 해시가 있던 44편은 이번 원문과 일치했다. 저자 13편, 검색 태그 18편, 프로젝트 주소 14편을 보완했다. [논문별 분류와 변경 전 값](../sources/batches/core_next_07.yaml) · [다음 50편](../../TODO.md)

| 공개 판정 | 코드 | 가중치 | 데이터 |
|---|---:|---:|---:|
| Y | 22 | 0 | 0 |
| 부분 | 10 | 13 | 20 |
| N · 저자 안내 확인 | 5 | 0 | 0 |
| 미확인 | 13 | 37 | 30 |

RTC의 저자는 Kinetix 실험의 구현·정책·전문가 궤적을 배포했다. TidyBot++의 가중치와 시연은 sim-v1 예제에 해당한다. CAP 저자는 체크포인트 공개를 완료로 표시했지만 실행기의 기본 경로와 실제 배포처를 대조해도 가중치 파일을 특정할 수 없어 미확인으로 두었다. [RTC 저자 배포](https://github.com/Physical-Intelligence/real-time-chunking-kinetix) · [TidyBot++ 예제](https://github.com/jimmyyhwu/tidybot2) · [CAP 저자 안내](https://github.com/jeffacce/cap-policy) · [CAP 실행기](https://github.com/jeffacce/cap-policy/blob/main/imitation-in-homes/run.py)

**서지와 평가 교정.** RSS의 USER 논문 목록과 게재본 표지에서 제목 어순이 다르다. 양쪽 제목을 연결하고 게재본의 Si Xu를 포함한 18인 저자 순서를 기록했다. RoboArena도 게재 PDF에 실린 공동저자 네 명을 복원해 30명을 기록했다. ActiveAlign은 시뮬레이션의 시점 교란과 실물 가림 시험을 분리했다. RoboFollow의 실물 파일럿은 지시 집합별 과제 구성 차이까지 평가 노트에 적었다. VLA 내부 활성화 개입 연구의 LIBERO-Long 결과는 OpenVLA-7B, 실물 UR5 결과는 π0-FAST에서 얻었다. [USER 목록](https://roboticsproceedings.org/rss22/p037.html) · [USER 표지](https://roboticsproceedings.org/rss22/p037.pdf#page=1) · [RoboArena 게재본 표지](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/atreya25a/atreya25a.pdf#page=1) · [ActiveAlign 표 VIII](https://arxiv.org/pdf/2610.23378v1#page=7) · [RoboFollow 실물 파일럿](https://arxiv.org/pdf/2609.25636v1#page=7) · [VLA 개입 실험](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/haon25a/haon25a.pdf#page=6)

**중복 재검사.** 배치 내부 1,225쌍과 나머지 원장과의 60,100쌍에 대해 공개 식별자, 정규화한 제목·별칭·제목 앞의 약칭을 비교했다. 약칭이 겹친 CoRE-VLA와 CoRe-VLA는 저자와 arXiv ID가 다르다. 전자는 선택적 깊이 입력을, 후자는 카메라가 이동한 뒤의 좌표 정합을 평가해 두 항목을 유지했다. [전문가 선택](https://arxiv.org/abs/2607.03693) · [시점 복원](https://arxiv.org/abs/2609.37150)

**남은 분류 질문.** 성공 횟수에 대한 순차 검정(STEP)과 보상 모델 학습을 공통 방법 축에서 어떻게 구분할 것인가? 휴대형 접촉 그리퍼로 수집한 시연(CAP)을 어느 출처로 검색할 것인가? 이번에는 기존 분류를 유지하고 해당 축의 불확실성을 표시했다. VLA 22편과 휴머노이드 2편에 전용 필드를 작성했고, 저자가 명시한 한계 17편과 직접 선행 관계 18건에 원문 위치를 연결했다. [배치 원장](../sources/batches/core_next_07.yaml) · [전체 원문 감사](../../research/SOURCE_AUDIT.md#다축-태그와-공개-자료)

## 여덟 번째 배치 태그 매핑

| 기존 검색어·표현 | 원문에서 확인한 구분 |
|---|---|
| `deformable`, `3DGS`, `real-to-sim` | PhysTwin은 사람의 물체 상호작용 영상에서 변형체의 물리 모델을 맞춘다. Mobi-π는 이동 베이스의 시점을 고른다. PolaRiS는 재구성한 장면에서 정책의 상대 성능을 평가한다. 세 연구의 영상·깊이·가우시안 자산은 쓰임이 다르다. |
| `tactile sensing`, `force-control` | 비파지 밀기 연구는 손목 카메라에서 얻은 물체 자세와 힘·토크를 이용해 가린 상태를 추정한다. Force Policy는 손목 영상·힘·말단 자세에서 접촉 중 힘을 제어할 축을 정한다. 입력 축의 `기타`에는 힘·토크와 추정 자세의 역할을 설명했다. |
| `instruction-following`, `Benchmark` | Spa-Bench는 실제 SO-101에서 공간 관계를 직접 지시한 대조 조건과 비교한다. LIBERO-X는 사람이 시뮬레이터를 원격조작해 같은 장면의 여러 목표에 시연을 제공한다. |
| `residual-RL`, `experience-retrieval` | PLD는 자료 수집용 잔차 전문가의 궤적을 범용 정책에 증류한다. 물체 중심 잔차 연구는 실행 때도 6D 물체 자세를 받는다. 각 레코드에 RL로 갱신한 모듈과 배포 시 필요한 입력을 명시했다. |

*PhysTwin*부터 *Force Policy*까지 NEXT 50편을 대조했다. 지정 판본의 PDF 49편과 IJRR 출판사 HTML 1편에 방법·평가 위치와 해시를 기록했다. 이전 요약 감사에서 PDF 해시가 남아 있던 44편은 이번 파일과 일치했다. 저자 9편, 검색 태그 16편, 프로젝트 주소 4편을 고쳤다. VLA 전용 필드 33편과 휴머노이드 시뮬레이션 1편을 작성하고, 저자 명시 한계 20편과 직접 선행 관계 24건에 원문 위치를 연결했다. 배치 내부 1,225쌍과 기존 원장 60,100쌍에서 공개 식별자, 정규화 제목·별칭·약칭, 제목 유사도 0.92 이상을 대조한 결과 중복 후보는 0건이었다. 집중 읽기 대상의 누적 범위는 **423/500편(84.6%)**이다. [50편 원장과 이전 값](../sources/batches/core_next_08.yaml) · [감사 집계](../../research/SOURCE_AUDIT.md#다축-태그와-공개-자료)

| 공개 여부 | 코드 | 가중치·학습 파라미터 | 데이터 | 합계 |
|---|---:|---:|---:|---:|
| 연구와 연결된 배포 파일 | 33 | 17 | 21 | 71 |
| 저자의 공개 예정 안내 | 1 | 1 | 1 | 3 |
| 해당 판본·실험의 파일 미확인 | 16 | 32 | 28 | 76 |

배포 파일 65개는 본문 첫 구간을, Google Drive 파일 6개는 개별 상세 화면과 파일명을 확인했다. Force Policy는 실물에서 세 과제를 시험했으며 확인한 가중치와 훈련 데이터는 상자 뒤집기용이다. MemER 게재본의 상위 정책은 Qwen2.5-VL-7B이고, 공개된 먼지 닦기용 상위 체크포인트는 Qwen3-VL-4B다. VLAC의 원 모델은 그릇 집기 진행도 추론 예제 영상을 배포했다. 이전에 연결한 VLAC-Cut 벤치마크는 별도 후속 모델에 해당한다. [Force Policy 게재본](https://roboticsproceedings.org/rss22/p128.pdf#page=6) · [Force Policy 배포](https://drive.google.com/drive/folders/1ioEFZoJbk5hjqBs8TCiL66DwCQGdCA1E) · [MemER 게재본](https://proceedings.iclr.cc/paper_files/paper/2026/file/9da515b1ad19d032a7398f00f5ff9b0c-Paper-Conference.pdf#page=5) · [먼지 닦기 체크포인트](https://huggingface.co/ajaysri/memer-dusting-qwen3vl-4b-step-1500) · [VLAC 저자 배포](https://github.com/InternRobotics/VLAC)

판본에 따라 실험을 다르게 읽어야 하는 사례도 남겼다. Equivariant Diffusion Policy의 IJRR 확장판은 점군을 이용해 회전과 병진 대칭을 다룬다. 저자가 CoRL 선행판과 공통으로 연결한 코드에서 확인한 범위는 등변 정책 학습기다. PolaRiS의 실물 순위는 정책·환경당 20회에서 얻었고, 시뮬레이션 순위는 별도 장면으로 공동학습한 뒤 과제당 50회에서 얻었다. SOAR 원 프로젝트의 데이터 공개 예정 표시는 Berkeley가 배포한 실제 RLDS 파일을 대조해 갱신했다. [IJRR 확장판](https://sage.cnpereading.com/doi/10.1177/02783649261424445) · [CoRL 선행판](https://proceedings.mlr.press/v270/wang25a.html) · [PolaRiS 평가 절차](https://roboticsproceedings.org/rss22/p062.pdf#page=6) · [SOAR 배포 자료](https://rail.eecs.berkeley.edu/datasets/soar_release/1.0.0/)

분류상 남은 질문은 행동을 출력하지 않는 시각 귀인·오프라인 진단을 기존 방법 축에서 어떻게 검색할지다. 이 배치에서는 해당 논문의 방법 축에 `unknown`을 두고, 실물·시뮬레이션·저장된 에피소드 중 어디에서 평가했는지를 기록했다. [다음 50편](../../TODO.md)

## 외부 목록 대조와 CORE 심화 감사

2026-11-19에 서베이 3편의 참고문헌, 6개 학회 3개년 목록, 연구실·기업 3곳 및 큐레이션 1곳을 대조했다. 등록 심사 후보 17편의 출처를 논문별로 보존했다. [목록별 커버리지와 하위 주제 순위](../../research/EXTERNAL_COVERAGE.md) · [후보 YAML](../sources/batches/missing_candidates_2026.yaml)

CORE 50편에서 직접 관련된 17편을 심화 검토했다. VLA 정책 11편과 휴머노이드 관련 8편 중 NaVILA와 FAST가 양쪽에 속한다. 후속 연구의 한계는 논문이 실제 비교한 과제·조건을 표시했다. 원문이 보고한 과제 수는 전체, 일부 평가 묶음, 하한으로 구분했다. 예를 들어 π0은 기본 정책을 다섯 과제에서 시험하고 미세조정 실험에는 스무 가지가 넘는 과제를 썼다. 중복을 제거한 전체 수는 미확인이다. [심화 YAML](../sources/batches/tier1_vla_humanoid.yaml) · [π0 기본 정책 평가](https://arxiv.org/pdf/2410.24164#page=7) · [π0 미세조정 평가](https://arxiv.org/pdf/2410.24164#page=11)

첫 배치의 JALA 코드 공개 판정을 N에서 unknown으로, Ctrl-World 데이터 판정을 unknown에서 부분으로 고쳤다. 후자는 저자가 새 장면에서 수집한 예제 영상과 주석을 배포한다. 배치에서 확인한 배포 범위·출처를 반영해 원장 36편의 공개 자료 정보도 동기화했다. 예전 판정은 배치의 `changed_from`과 `revisions`에 보존한다. [JALA 공식 트리](https://github.com/BeingBeyond/JALA) · [Ctrl-World 예제](https://github.com/Robert-gyj/Ctrl-World/tree/main/dataset_example/droid_new_setup)

<a id="reg-r18"></a>

## 최근 등록

2026-11-19 누락 심사에서 36편의 출처와 기존 ID를 대조해 23편을 NEXT로 등록했다. 나머지는 보류 9편, 중복 4편이었다. 당시 원장은 1,250편, CORE·NEXT 정독 대상은 500편이었다. 등록 전 1,227편 기준의 측정은 날짜가 있는 이전 감사에 보존했다. [심사 및 커버리지](../../research/GAPFILL.md) · [원문 근거와 태그](../sources/batches/gapfill_2026_11.yaml)

- 직접 선행 18편을 추가했다. 공식 주요 학회·IJRR 12편, 기타 peer-reviewed 비교 논문 2편, preprint 4편이다. ActiveAlign은 기존 항목을 사용했다. [등록 근거](../sources/registry_maintenance_2026-11-18.json)
- 3D 추정 후보의 직접 선행 3편을 추가했다. Geometry Impact는 [ECCV 2026 정식 출판](https://link.springer.com/chapter/10.1007/978-3-032-37271-0_2), EDI와 PRISM Precision Forcing은 확인한 상태가 preprint다. [EDI](https://arxiv.org/abs/2609.34018) · [PRISM](https://arxiv.org/abs/2610.14704)
- Ψ₀와 데이터 전제 2편을 등록하고 AMO·SONIC의 설명과 공개 자료를 교정했다. [공식 근거와 교정 항목](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/update/REGISTRY_ACCURACY_PSI0_2026-11-16.md)

<a id="note-review"></a>

## 노트 품질

2026-11-24에 표준 노트 6,260개를 검색해 10편의 31개 노트에 남아 있던 글꼴 전용 문자 258개를 찾았다. 91개 줄을 해당 PDF의 인쇄된 수식·그림과 대조해 고쳤고, 같은 범위를 다시 검색해 글꼴 전용 문자와 대체 문자(U+FFFD)가 0개임을 확인했다. 논문별 기록에는 판본 해시와 교정 전 커밋·줄 번호가 있다. [감사 원장과 집계](../../research/SOURCE_AUDIT.md#노트의-수식과-도식)

- MuJoCo에서 법선 충격량과 접선 충격량, 마찰계수의 부등호를 복원했다. 표 1의 단위는 접촉이 없는 동역학의 초당 평가 횟수다. ManiGaussian 그림 1의 녹색 체크는 블록을 쌓은 예시 시행에 붙은 성공 표시다. [MuJoCo 식 4·5](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=3) · [MuJoCo 표 1](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=7) · [ManiGaussian 그림 1](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05194.pdf#page=2)
- TD-MPC2는 잠재 상태·보상·가치를 학습한 뒤 행동열의 수익을 평가해 첫 행동을 실행한다. 문제 정의와 평가 노트 2개에도 이 설명을 반영했다. SERL과 HIL-SERL의 문제 정의에서는 말단장치 명령의 예가 각각 목표 자세와 목표 트위스트로 다르다. [TD-MPC2 식 3·6](https://arxiv.org/pdf/2310.16828v2#page=4) · [SERL §3](https://arxiv.org/pdf/2401.16013v4#page=3) · [HIL-SERL §3.1](https://arxiv.org/pdf/2410.21845v3#page=4)

논문 개요 278편에 연도·발표처의 항목명만 남아 있었다. 2026-11-23에 원장의 값으로 해당 표시를 복원했다. 무결성 검사는 1,252편 모두에서 개요 상단의 연도·발표처가 한 번 표시되고 원장과 일치하는지도 확인한다. [원장](../sources/papers.json) · [검사 코드](../scripts/audit_repository.py)

- GSrec의 ECVA 서지는 제목에 *for*를, 인쇄본은 *from*을 쓴다. Li 등의 *UrbanGS*에서도 ICLR 웹 서지와 표제면의 어순이 다르다. 두 논문 모두 인쇄 제목으로도 검색할 수 있게 했다. Wang 등의 CVPR *Urban-GS*는 항공·지상 영상 결합을 다룬 별도 연구다. [GSrec 게재본](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00274.pdf#page=1) · [UrbanGS 게재본](https://proceedings.iclr.cc/paper_files/paper/2026/file/108030643e640ac050e0ed5e6aace48f-Paper-Conference.pdf#page=1) · [Urban-GS 게재본](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Urban-GS_A_Unified_3D_Gaussian_Splatting_Framework_for_Compact_and_CVPR_2026_paper.pdf#page=1)
- ARCHIVE 마지막 배치의 평가 노트 49편을 고쳤다. ScanQA는 수집된 스캔에서 답과 근거 물체를 채점하고, Holodeck은 생성한 환경에서 시뮬레이션 내비게이션을 평가하며, PRISM은 두 실물 로봇팔의 조작 성공률을 측정한다. 평가 유형과 검색 색인에 이 차이를 반영했다. [ScanQA 표 2](https://openaccess.thecvf.com/content/CVPR2022/papers/Azuma_ScanQA_3D_Question_Answering_for_Spatial_Scene_Understanding_CVPR_2022_paper.pdf#page=3) · [Holodeck 표 2](https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf#page=8) · [PRISM 표 3·4](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liang26n/liang26n.pdf#page=8)
- *LE-Object*의 기존 arXiv ID `2406.08009`는 Deng 등의 *OpenObj*에 속한다. Wang 등의 ICRA 게재본은 표 I에서 두 방법을 직접 비교한다. 게재 DOI·PDF와 표준 노트 5개, 재수집 입력을 교정했다. 과거 8쪽 PDF에 대한 문자 검사의 적용 범위도 해당 기록에 표시했다. [LE-Object 표 I](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11128304#page=5) · [OpenObj 표제·저자](https://arxiv.org/abs/2406.08009)
- *Context Graph-based Visual-Language Place Recognition*은 저자판과 ICRA 게재본의 표제가 다르다. 게재본 기준으로 문맥 그래프 구성과 후보 수별 Recall을 정리하고 그래프를 생성하는 공개 구현까지 확인했다. [게재본 그림 4](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11127699#page=4) · [저자판](https://arxiv.org/abs/2410.19341) · [구현 파일](https://github.com/woo-soojin/context-based-vlpr/blob/3556108a08c7c637256e4bb7337d51915a5dd5fa/utils/context_graph.py)

- *Active Offline Policy Selection*의 첫 저자는 게재본에 Ksenia Konyushkova로 인쇄됐다. *SPIRE*는 PMLR 서지 제목에 있는 ‘Learning’이 게재본 표제에 빠져 있다. 두 판본을 한 논문에서 찾을 수 있도록 개요와 원장에 차이를 기록했다. [NeurIPS 게재본 1쪽](https://proceedings.neurips.cc/paper_files/paper/2021/file/cec2346566ba8ecd04bfd992fd193fb3-Paper.pdf#page=1) · [SPIRE 학회 서지](https://proceedings.mlr.press/v270/zhou25a.html) · [논문별 감사](../../research/SOURCE_AUDIT.md)
- Point2Graph의 노트 5개에서 원문에 표시된 `fi`·`fl` 합자를 확인해 글꼴 전용 문자 96개를 복원했다. Audio-VLA의 노트 5개에서는 페이지 경계에서 잘려 반복된 구성요소 설명을 복원했다. 글꼴과 문자 간 대응은 논문마다 달라 검사기는 해당 줄을 표시하고 보존한다. [Point2Graph 원문](https://arxiv.org/pdf/2409.10350v1) · [Audio-VLA 그림 2](https://arxiv.org/pdf/2511.09958v1#page=3) · [문자 검사](../scripts/audit_note_artifacts.py)
- AutoHorizon의 실행 길이 계산식, PD-VLA의 토큰 갱신식, BA-GS의 관측 행렬과 VQ-VLA의 행동 인코더·디코더 도식은 렌더링한 원문과 대조해 노트 7개에 남은 손상 12줄을 복원했다. [AutoHorizon 식 6](https://arxiv.org/pdf/2602.21445v2#page=6) · [PD-VLA 식 5](https://arxiv.org/pdf/2503.02310v2#page=4) · [BA-GS 식 4](https://openaccess.thecvf.com/content/CVPR2026/papers/Ma_BA-GS_Bayesian_Adaptive_Gaussian_Splatting_for_SFM-Free_3D_Reconstruction_CVPR_2026_paper.pdf#page=4) · [VQ-VLA 그림 1](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf#page=3)
- PDF 원문 확인 요청 112개 노트를 포함해 55편의 노트 135개에서 손상된 구간 306개를 대조·수정했다. 수정 구간의 확인 수준과 논문 전체 정독을 구별한다. [논문별 원문·페이지·수정 근거](../sources/pdf_note_review_2026-10-23.json) · [후속 근거](../sources/pdf_note_review_followup_2026-10-23.json)
- CHOMP의 장애물 비용, SARA-RT의 선형 어텐션, Cassie 보행 정책의 입력 벡터를 원문에 맞춰 복원했다. 세 논문의 노트 7개에 손상된 발췌 18줄이 있었다. Cassie의 실물 정책은 속도 명령·주기 신호·자기수용감각을 받아 약 33 Hz로 관절 위치 목표를 내고, 2 kHz PD 제어기가 토크를 계산한다. [CHOMP 그림 2](https://www.ri.cmu.edu/pub_files/2009/5/icra09-chomp.pdf#page=4) · [SARA-RT 식 3](https://arxiv.org/pdf/2312.01990v1#page=3) · [Cassie 그림 2 및 III-A](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3)
- G²VLM은 실제·예측 상대 회전 사이의 측지각을 손실로 쓴다. MSGNav는 같은 영상에 보인 물체 쌍을 장면 그래프의 간선에 연결한다. VINS-Mono의 네 자유도 자세 그래프는 루프 폐쇄 잔차에 Huber 함수를 적용한다. 게재본과 저자판의 해당 식·그림을 대조해 세 논문의 노트 4개에서 손상된 6줄을 복원했다. [G²VLM 식 5](https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.pdf#page=4) · [MSGNav 그림 3](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.pdf#page=4) · [VINS-Mono 식 29](https://arxiv.org/pdf/1708.03852v1#page=11)
- 논문별 출처와 증거 수준은 [원장](../sources/papers.json)이 관리하고, 사용자 읽기 이력은 [읽기 기록](../../research/READING_STATUS.csv)에 둔다.

[직전 등록 원문과 게시 검증](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/update/REGISTRY_MAINTENANCE_2026-11-18.md) · [이전 등록·유지보수 기록](https://github.com/Kim-Yoo-Hyun/PaperReview/tree/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/update)
