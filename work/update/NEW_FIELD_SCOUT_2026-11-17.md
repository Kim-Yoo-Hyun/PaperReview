# 새로운 검색 분야 탐색 — 선정 이력

Updated: 2026-11-17 KST. **POSE-ACTIVE-N1/N2·P0 코드 준비 완료; 다음 호환 local NVIDIA의 제한된 P0 검증.** 앞선 R1/R2·관계 기반 탐색 N1/N2·P0 준비 이력을 아래 보존한다. [출처·확인 범위](../sources/new_field_scout_2026-11-17.json) · [현재 주제](../research_topics/README.md) · [TODO](../../TODO.md).

<a id="pose-reconstruction"></a>
## 추가 탐색 — 물체 자세·능동 관측과 조작용 3D 추정

사용자가 지정한 두 축을 2024–2026 외부 논문 **20편**과 기존 registry에서 대조했다. CVPR·RSS·CoRL·NeurIPS·IJRR·AAAI의 공식 근거와 최신 arXiv를 구별했으며, 직접 중복하는 Industrial Robot 논문도 포함했다. 전 venue 전수조사나 20편 전체 정독이 아니다. 공식 초록·지정 본문·code README 확인 범위와 등록 identity는 원장 `pose_reconstruction_scout.sources`가 소유한다. 5편은 현재 registry와 일치하고 15편은 이번 탐색의 외부 근거로만 기록했다. 신규 registry 등록·reading status 승격은 없다.

| 초기 후보 | 남을 수 있는 main contribution | 우선 판단 |
|---|---|---|
| [작업에 필요한 물체 자세의 능동 관측](../research_topics/pose_active_perception/내용/README.md) | 여러 pose 가설에서 성공할 공통 행동을 학습해, 유효한 행동 다양성과 실제 관측 부족을 구별 | **N1/N2·P0 코드 준비 완료, native 대기**. 공통 성공 원리 자체의 신규성 제외. 같은 label의 lookup/분리 classifier 대비 공유 VLA 학습의 차이로 한정 |
| [조작 허용 오차를 반영하는 3D 추정](../research_topics/task_geometry_estimation/내용/README.md) | geometry 오차의 위치·방향·원인과 task tolerance를 연결해 VLA 실패를 예측하고 학습 개선 | **2순위 탐색**. SpatialVLA depth 입력 지점 부분 확인. 1번보다 비용이 높다는 단정 유보. Robo3R·GeoPredict·PRISM 이후 차이 필요 |

**차별점의 출발점은 연구자 가설이다.** [DISaM](https://proceedings.mlr.press/v270/dass25a.html)은 행동 불확실성 기반 관측, [ATAP](https://arxiv.org/html/2609.23504v1)은 task affordance 가설 검증, [Naik 등](https://arxiv.org/abs/2403.10874)은 허용 오차 내 pose 불확실성을 이미 다룬다. [Robo3R](https://roboticsproceedings.org/rss22/p056.html)은 로봇 좌표의 metric reconstruction과 downstream 조작, [GeoPredict](https://openaccess.thecvf.com/content/CVPR2026/html/Qian_GeoPredict_Leveraging_Predictive_Kinematics_and_3D_Gaussian_Geometry_for_Precise_CVPR_2026_paper.html)는 궤적 주변 geometry refinement, [PRISM](https://arxiv.org/html/2610.14704v1)은 정밀도 요구에 따른 VLA 학습을 제공한다. 이 원리들을 새 조합만으로 재주장하지 않는다.

Pose/shape 불확실성·camera calibration·정당한 action multimodality를 분리하고, 가상 시점/attention과 실제 물리 관측을 구별했다. 두 후보 모두 언어 조건과 실제 행동을 확인해야 VLA 연구다. 이번에는 독립 기여·성능·실물 자원·실행 환경이 확정되지 않았고 비실험 buildup 전체가 완료된 것도 아니다. 각 주제의 `내용/README.md`와 `재현 방법/README.md`에만 상세 설계를 두었으며 별도 brief·recipe를 만들지 않았다.

**N1 후속 결과:** DISaM의 분포 간 KL과 원시 행동 분산을 구별하고, 네 논리 사례·6개 repo의 text source/README/XML 27개를 검토했다. FoundationPose 후보 좌표/score, l2l의 직접 시점 변경, SpatialVLA depth·행동 decoding, SquareNut 성공 predicate의 경계를 [주제 두 문서](../research_topics/pose_active_perception/내용/README.md#n1-result)에 통합했다. **REVISE 후 CONTINUE**, N2에서 **SpatialVLA 4-step/12-token 후보·순차 재채점·pose 집합 갱신·새 배치 evaluator·counterfactual label**을 명세했다. Pose 입력 없는 원 정책의 점수를 가설별 KL로 부르는 오류와 suffix 재채점의 attention 경계를 반영했다. 이어 **POSE-ACTIVE-P0-PREP**를 진행했으며 결과는 아래에 연결했다. 같은 비실험 검토를 반복하지 않는다. 1번이 더 쉽다는 판단은 유보한다. 문서/코드 확인을 native 호환·실행·효과로 세지 않는다.

**P0 준비 결과:** [Docker recipe·source/model pin·scene/evaluator·camera/제한된 복원·VLA 후보/재채점·제어 검사10개](../research_topics/pose_active_perception/재현%20방법/README.md#p0-preparation)를 작성했다. 새 launcher의 실제 `run`은 local daemon 연결 실패(exit3)로 중단됐다. 정적 컴파일은 통과했으나 Docker 검사·native 실행·host 설치·weight/asset 수신은 없다. Task normalizer 부재로 VLA 제어 명령은 차단한다. FoundationPose/물리 camera/전체 label·학습은 미구현이며, 다음 POSE-ACTIVE-P0는 **PREPARED_UNEXECUTED / NATIVE_RESOURCE_WAIT**다. Source·환경 metadata와 실제 실패는 원장 `pose_active_p0_preparation`에 남겼다.

앞선 GAP-RELATION-EXPLORE-P0와 유지3·예비1·폐기7 판단은 보존했다. Source text를 임시 읽기용으로 받아 revision/hash를 기록하고 사본은 제거했다. N1/N2에는 실험·Docker probe·host 설치·weights/바이너리 asset/PDF 다운로드가 없었다. P0-PREP의 read-only Docker 확인과 코드 작성은 위에 별도 기록했다. 초기 탐색 검증은 `pose_reconstruction_scout.validation`, N1은 `pose_active_n1.validation`, N2는 `pose_active_n2.validation`에 별도로 보존한다. 추가 task-sufficiency 개념 preprint는 평가 예정/venue 미확인으로 기록했으며 기존 registry에 등록하지 않았다.

<a id="relation-exploration"></a>
## 앞선 R2 선택과 관계 기반 탐색 N1 후속

사용자의 “참신하고 main contribution이 명확한 주제” 요청에 따라 구조적 탐색·능동 시스템 식별·chunk credit·회복·미래 행동 가능성 보존을 재검색했다. 접촉 관계에 조건화된 VLA의 RL 탐색을 선택했으며 카메라 적응·정책 병합은 현재 선택에서 제외했다. 2024–2026 공식 논문과 최신 preprint를 구별했고, Lattice·양팔 synergy 등 직접 비교에 필요한 더 오래된 선행도 확인했다. 검색 부재를 신규성의 증거로 사용하지 않았다.

**N1 결과는 REVISE 후 좁은 탐색 CONTINUE.** RL-SCT의 phase별 제약 전환과 Lattice의 learned full covariance를 확인하면서, ‘상관된 탐색’이나 ‘전환’만으로는 기여가 안 된다는 경계를 강화했다. 영상·지시·현재 상태로 **두 팔의 결합 정도를 학습하는 작은 actor 모듈**과 그 필요성을 묻는 설계로 좁혔다. Native 정책 효과·독립 신규성은 미확인이다.

선정 후에는 사용자 지시대로 두 폴더로 통합했다. R2의 상세 가설·수식·baseline과 N1 검토 결과를 [내용](../research_topics/relation_exploration/내용/README.md), source revision·checkpoint·입출력/환경 조건을 [재현 방법](../research_topics/relation_exploration/재현%20방법/README.md)이 소유한다. 이 공통 보고서에서 방법 설계를 중복 관리하지 않는다. 근거 원장은 기존 JSON 하나를 계속 사용한다.

<a id="next-buildup"></a>
## 관계 기반 탐색 N1/N2·P0 준비와 조건부 후속

N1의 선행/공개 source 대조, 최소 사례·반례, actor/likelihood 설계, task/checkpoint/asset metadata, 계속/수정 판단을 완료했다. 실제 공개 task는 `lift_pot`·`handover_block`·`pick_dual_bottles`이며 원래 예시의 공동 운반→배치→한 손 해제를 하나의 확보된 task라고 표현하지 않는다. Drive-target 상태와 실제 관절 측정의 차이, TOPP의 가변 실행 시간, 성공 predicate와 contact witness의 차이도 확인했다.

N2는 재구성 OpenPI loader 선택·공통 SFT 전환 조건, quantile/state-token/14D 변환과 actual qpos/TCP, 세 task의 contact witness, reset/physics/종료 비용, P0 상한을 명세했다. 선택한 RL 경로가 `gen_sparse_reward_data`임을 확정하고 정지 명령의 추가 잡음과 최대500-point downsampling을 발견해 비교 조건에 반영했다. 원 Motus fork·weight 호환·FK/evaluator 교정·환경 lock은 미검증이다.

P0-PREP에서 고정 image metadata·source/asset pin, Docker recipe·strict loader/actor·FK/contact/budget adapter·launcher·Docker 제어 검사9개를 작성했다. 새 launcher는 로컬 Unix endpoint를 확인한 뒤 daemon 연결 실패(exit3)로 차단됐다. 코드 정적 컴파일은 통과했지만 image build·제어 검사·native 실행·학습·payload 설치는 없었다. 다음은 **GAP-RELATION-EXPLORE-P0 — NATIVE_RESOURCE_WAIT**다. [재개 명령·미구현 경계](../research_topics/relation_exploration/재현%20방법/README.md#resume)에서 이어가며 준비 완료를 연구 효과 입증으로 세지 않는다.

신규 paper 등록·reading status 변경은 없다. R1/R2/N1의 검증은 원장 `validation`/`round2.validation`/`relation_n1.validation`에 역사로 보존하고, N2 검사는 `relation_n2.validation`, 현재 준비·검사·보존 결과는 `relation_p0_preparation`에 기록한다. 상세 방법과 재개 계약은 위 주제의 두 README가 소유한다.

---

## R1 조사 이력 — 아래 순위·다음 행동은 현재 선택에서 제외

사용자의 새 지시에 따라 실패 탐지·원인 분류 후속인 GAP-RELIABILITY-N1을 보류하고 다른 검색 분야를 조사했다. 기존 유지 3개·예비 1개와 폐기 7개의 판단은 바꾸지 않는다. 아래 두 항목은 **CURATION-HYPOTHESIS 단계의 초기 후보 카드**다. 실행 대기 주제나 비실험 buildup 완료 주제로 세지 않으며, 선정 전에는 후보마다 폴더·실행 recipe를 늘리지 않는다.

## 조사 범위와 선정

Registry의 제목·식별자·관련 기존 dossier를 외부 공식 proceedings 및 저자 원문과 대조했다. 2024–2026의 RSS·CVPR·ICLR·ICML·CoRL 논문을 기준점으로 삼고, 직접 중복 확인에는 2026 preprint도 포함했다. 전 venue의 전수조사나 전체 논문 정독은 아니다. 초록 확인과 지정 본문 확인은 원장에 구별했다. 검색 부재를 선행 부재의 증거로 사용하지 않는다.

| 검색 분야 | 확인한 근거와 이미 있는 답 | 이번 판단 |
|---|---|---|
| 카메라 좌표계·장착 변화와 적응 | [SpatialVLA, RSS 2025](https://roboticsproceedings.org/rss21/p011.html), [ActiveVLA, CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.html), [CamVLA](https://arxiv.org/html/2607.05396v1), [CoRe-VLA](https://arxiv.org/html/2609.37150v1). 3D 표현·능동 관측·학습된 좌표 변환·원래 시점 복원은 이미 존재 | **우선 초기 후보**: 알려지지 않은 손목 카메라 장착 변화에서 행동 이력을 이용하는 적응으로 좁힘 |
| 전문가 정책 병합·능력 통합 | [MergeVLA, CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/papers/Fu_MergeVLA_Cross-Skill_Model_Merging_Toward_a_Generalist_Vision-Language-Action_Agent_CVPR_2026_paper.pdf), [PolicyWeave](https://arxiv.org/html/2609.33125v1), [RLDG, RSS 2025](https://roboticsproceedings.org/rss21/p028.html), [REPAIR](https://arxiv.org/abs/2611.02777). 독립 RL 전문가의 단일 정책 통합·증류 자체는 이미 존재 | **차순위 초기 후보**: 같은 목표의 서로 다른 환경 적응을 조합하는 문제. 직접 중복 위험 높음 |
| 세계 모델 기반 RL·정책 평가 | [VLA-MBPO, ICML 2026](https://proceedings.mlr.press/v306/zhang26ez.html), [dWorldEval, ICML 2026](https://proceedings.mlr.press/v306/li26hi.html), [HaWMPO](https://arxiv.org/abs/2609.09941), [PrimeSim](https://arxiv.org/abs/2611.04870). 상상 rollout 활용·잘못된 성공 교정·hallucination 신뢰도는 이미 다뤄짐 | 새 주제로 선택하지 않음. 기존 세계 모델 검증 질문과 겹치며 대형 모델 구축 부담도 큼 |
| 영상 보상·실패 데이터 | [ReWiND, CoRL 2025](https://proceedings.mlr.press/v305/zhang25a.html), [Robometer, RSS 2026](https://www.roboticsproceedings.org/rss22/p140.html), [RoboReward](https://arxiv.org/html/2601.00675v2), [ICML 2026 position paper](https://proceedings.mlr.press/v306/tian26o.html) | 중요한 분야지만 ‘실패 데이터를 추가하자’는 새 기여가 아님. RoboReward에는 실제 실패와 합성 negative의 비교도 있음. 이번에는 후보를 억지로 추가하지 않음 |
| 지연·비동기 실행·행동 chunk | [Reinforcement Learning for Real-Time VLA Policies](https://arxiv.org/abs/2609.18207), [Learning to Act While Waiting](https://arxiv.org/abs/2608.23831) | 지연 조건부 RL 자체는 직접 중복. 기존 제어 주기 질문·폐기 CODEC1을 이름만 바꿔 재개하지 않음 |
| 인간 영상·latent action | [LAPA, ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html), [JALA, CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/papers/Luo_Joint-Aligned_Latent_Action_Towards_Scalable_VLA_Pretraining_in_the_Wild_CVPR_2026_paper.pdf) | 단순 영상 사전학습·신체 정렬은 직접 선행. 현 단계의 명확한 차이보다 데이터/학습 부담이 커 우선순위 낮음 |

[Octo, RSS 2024](https://www.roboticsproceedings.org/rss20/p090.html)는 새 관측·행동 공간으로의 적응이라는 기반 좌표다. 새 후보를 고정 센서 전제의 한 모델에만 해당하는 현상으로 만들지 않기 위해 비교한다. 이 표는 검색 분야 선택이며 paper reading tier를 바꾸지 않는다.

<a id="camera"></a>
## R1 우선 후보였던 질문 — 손목 카메라 장착 변화에 대한 VLA의 행동 기반 적응

**연구 질문:** 손목 카메라와 end-effector 사이의 변환이 알려지지 않게 바뀌었을 때, 짧은 영상·고유감각·행동 이력을 사용하는 단일 VLA가 작업 수행과 좌표계 식별을 함께 학습하여, 같은 시간 예산의 보정 후 실행·시점 증강보다 조작 성능을 높일 수 있는가?

고장 탐지기를 추가하는 문제가 아니라 **센서와 행동 좌표 사이의 변환을 부분 관측된 상태로 취급하는 정책 적응 문제**다. 정상적인 팔 운동 때문에 손목 영상이 움직이는 것과 카메라 브래킷의 장착 변환이 바뀌는 것을 구분한다. 초기 범위는 한 팔·고정된 외부 카메라·변화하는 손목 장착 하나다. 양쪽 카메라 변환, 물체 운동, 로봇 기구학을 모두 미지수로 두고 시작하지 않는다.

### 논문이 지지하는 범위

- **CamVLA:** 단일 RGB에서 camera-frame action과 hand–eye 변환을 예측해 base-frame action으로 합성한다. §5는 단일 외부 카메라만 사용하며 손목 카메라의 시점 교란을 다루지 않았다고 명시한다. 따라서 ‘calibration-free VLA’ 자체는 신규성이 아니다. [원문 §5](https://arxiv.org/html/2607.05396v1#S5).
- **CoRe-VLA:** 외부 시점이 바뀌어 다중 시점 정보의 활용이 어긋나는 현상을 분석하고, RGB-D 재구성과 원래 시점 렌더링으로 대응한다. Fig.1은 손목 카메라 장착이 유지되는 조건을 명시한다. 본문 §1/§4의 확인 범위에서 **외부 카메라 변화에 대한 복원**과 이번 **미지의 손목 장착 변환 추론**을 구분한다. 일반적인 cross-view coordination 공백을 다시 주장하지 않는다. [원문](https://arxiv.org/html/2609.37150v1).
- **ActiveVLA·SaPaVe:** 능동적으로 잘 보이는 관측을 얻고 조작하는 선행이다. 이들의 카메라 geometry 입력·보정 가정까지 본문/코드로 대조해야 새 질문이 남는지 판단할 수 있다. 이번에는 공식 초록/지정 공개 설명을 확인했으며 코드 검증은 하지 않았다. [ActiveVLA](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.html) · [SaPaVe](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.pdf).
- **고전적 대안:** 로봇 움직임을 이용한 hand–eye calibration은 오래된 방법이다. ‘움직여 좌표를 알아낸다’는 발상 자체는 기여가 아니다. Calibration target·정적 장면·다양한 움직임 등 정보 조건을 맞추고 비교해야 한다. [Tsai–Lenz 원문, IEEE T-RA 1989](https://kmlee.gatech.edu/me6406/handeye.pdf).

### 연구자 해석과 기여 가설

현재 근거는 **비어 있을 수 있는 평가 조건**을 지지할 뿐 새로운 방법의 필요성을 입증하지 않는다. 기여가 생길 가능성은, 같은 RGB·proprioception으로도 한 프레임만으로 구별되지 않는 장착 변환을 행동 이력으로 식별하고, 작업 이득과 식별에 필요한 움직임의 비용을 한 정책 안에서 다루는 데 있다.

방법 초안은 짧은 이력에서 잠재적인 geometry 상태를 추정하고 이를 기존 VLA action head와 함께 후학습하는 것이다. RL은 조작 성공과 추가 이동 비용을 학습하는 수단 후보이며 필수가 아니다. 동일 이력의 BC/지도 적응으로 충분하면 RL 고유 기여를 주장하지 않는다. 외부 보정 모듈 뒤에 VLA를 붙인 것만으로 unified 학습이라고 부르지 않는다.

| 비교 항목 | 최소 설계 초안 — 아직 실행 계약 아님 |
|---|---|
| 현실적 사례 | 카메라 교체·장착 오차·브래킷 변형 후 집기/배치. 작업 중 갑작스러운 변화는 후속 stress test로 분리. 실제 발생 빈도·변화 범위는 추가 확인 |
| 관측 | 동일 RGB 두 시점·joint/EEF 상태·실제 실행 action history. 정답 extrinsic·시뮬레이터 상태는 평가자/별도 oracle만 사용 |
| 비교군 | 원 VLA, 같은 총 데이터의 시점 증강 BC/RL, 이력 BC, 고정 소량 probe+고전 보정, 알려진 extrinsic oracle. 외부 view만 사용하는 정책도 포함해 손목 적응 필요성을 확인 |
| 가설의 예측 | 시각적으로 모호하지만 움직임으로 구분 가능한 변화에서 이력·정보 수집 행동의 이득이 커야 한다. 충분히 구분 가능한 단일 프레임 조건에서는 불필요한 probe가 줄어야 한다 |
| 분리할 원인 | 더 많은 영상·추가 시간·action smoothing·외부 카메라만의 정보로 설명되는 이득을 각각 대조. 단순 crop/lighting 변화와 실제 extrinsic 변화를 구분 |
| 결과 기준 | 동일 시간/움직임 예산에서 성공·복구 시간·물체 낙하/충돌. 보정 오차는 보조 지표이며 낮은 오차만으로 정책 개선을 주장하지 않음 |
| 석사 부담 | 새 foundation 사전학습 없이 한 팔·한 checkpoint·소수 task부터 가능할 수 있음. Camera API, RGB 동기화, 변경된 장착과 action frame 일관성, 최소 실물 검증 접근성은 미확인 |

**계속 볼 이유:** CV·로봇 상태 추정·행동 학습의 연결이 명확하고, 외부 perception/controller 연결을 넘어 한 VLA 내부의 적응 문제로 표현할 수 있다. 기존 FEEDBACK은 관측의 신선도/개입 가치, 과거 C1은 추가 관측 선택을 다뤘다. 이번에는 **관측–행동 좌표 변환 자체의 미지성**이 핵심이다. 결국 관측 재요청만 남는다면 별도 주제로 유지하지 않는다.

**가장 큰 약점:** 손목 카메라의 장착 변화가 실제로 중요한 실패 원인인지, 외부 시점만으로 충분하지 않은지, 표준 hand–eye 보정이나 augmentation보다 배울 것이 있는지가 아직 확인되지 않았다. 고전 보정이 같은 예산에서 문제를 해소하면 VLA+RL 방법 주제로는 축소/종료한다. 로봇이 생성한 움직임이 충분한 식별 정보를 주지 않는 상황을 RL로 해결한다고 가정하지 않는다.

<a id="merge"></a>
## R1 차순위였던 질문 — 서로 다른 환경에서 얻은 RL 적응의 단일 정책 통합

**연구 질문:** 같은 로봇·목표·행동 좌표계를 공유하지만 서로 다른 환경 요인에 적응한 VLA들의 RL 갱신을 합쳐, 각 전문가가 보지 않은 요인 조합에서도 한 정책이 이득을 유지할 수 있는가?

예를 들면 한 전문가는 시각 교란, 다른 전문가는 물리 마찰 변화에 적응한다. 두 조건이 동시에 등장하는 테스트에서 static weight merge가 충분한지, 대표 관측에서 행동 간섭을 제한하는 병합이 필요한지를 본다. 아직 새 알고리즘을 정한 것이 아니며 가장 먼저 직접 선행의 domain-shift 평가 범위를 확인한다.

- **MergeVLA, CVPR 2026:** task mask·LoRA와 action expert 구성을 병합 가능하게 설계하고 task router를 사용한다. 일반 VLA skill merging은 이미 해결 대상으로 제시됐다. [공식 본문](https://openaccess.thecvf.com/content/CVPR2026/papers/Fu_MergeVLA_Cross-Skill_Model_Merging_Toward_a_Generalist_Vision-Language-Action_Agent_CVPR_2026_paper.pdf) · [공식 코드 설명](https://github.com/MergeVLA/MergeVLA).
- **PolicyWeave, 2026 preprint:** 공통 action interface를 보존한 독립 전문가의 SFT와 RL 갱신을 병합하며, static merging과 context-guided sparse merging을 모두 다룬다. ‘RL 전문가를 joint RL 없이 합친다’도 새 기여가 아니다. §3·Appendix F가 비교 기준이며 일반화 주장 범위를 추가 대조해야 한다. [원문](https://arxiv.org/html/2609.33125v1).
- **RLDG, RSS 2025 / REPAIR, 2026 preprint:** RL 전문가의 능력을 generalist VLA에 증류하는 강한 대안이다. 배포할 때 한 정책이라는 사실만으로 방식의 독창성을 주장하지 않는다. [RLDG](https://roboticsproceedings.org/rss21/p028.html) · [REPAIR](https://arxiv.org/abs/2611.02777).

남을 수 있는 차이는 **task별 전문가 선택이 아니라 같은 task 안의 환경 적응 조합**이다. LANGRET의 하나의 정책을 RL로 갱신하며 지시별 행동을 보존하는 문제와 다르고, 폐기 VRL의 base 업데이트 뒤 외부 residual 재사용 문제와도 다르다. 다만 이것이 독립적이고 중요한 차이인지는 아직 미확정이다.

가장 먼저 shared-base/interface를 고정한 평균·TIES/DARE 등 표준 병합, PolicyWeave의 static/context 조건, 동일 총수집비의 mixed-domain RL, 전문가 자료로 증류를 비교 설계한다. 단순 병합이 충분하면 성공 조건을 분석하는 방향은 남을 수 있으나 새 병합 방법을 만들 이유는 줄어든다. 서로 다른 normalizer를 그대로 합친 인위적 실패를 공백으로 삼지 않는다. 평가에서는 visual-only·dynamics-only·동시 변화·변화 없음의 네 조건과 각 전문가의 실제 능력을 분리한다.

**차순위 이유:** 단일 VLA+RL이라는 방향 적합성은 높지만 PolicyWeave가 매우 가까우며, 적어도 두 전문가 학습과 공동 학습/증류 비교가 필요하다. 공개 checkpoint가 동일 base·normalizer를 공유하는지도 미확인이다. GPU 부재 때문이 아니라 **새 기여의 경계와 총 비교 비용** 때문에 카메라 후보 뒤에 둔다.

## R1의 다음 계획 — 현재 선택에서 제외

**GAP-CAMERA-N1**을 다음 TODO로 선택한다. 다음 항목을 하나의 비교표로 끝내며 실험 성능을 진입 조건으로 요구하지 않는다.

1. CamVLA·CoRe-VLA·ActiveVLA·SaPaVe와 온라인 hand–eye/self-calibration의 지정 본문·공개 interface를 대조한다. 실제 카메라 이동, wrist 장착 변화, 알려진 extrinsic, proprioception, history, task action을 구별한다.
2. 손목 장착만 미지수인 최소 사례 하나와 고전 보정으로 이미 충분한 사례 하나를 정한다. 시점 변화와 action-frame mismatch가 같은 문제인지 확인한다.
3. 무엇을 학습해야 기존 보정/BC보다 유용할지 하나의 차별적 예측을 작성한다. RL과 단일 정책 학습의 필요성이 없으면 방법 기여를 낮추거나 다른 질문으로 수정한다.
4. 공개 simulator의 camera attachment·extrinsic mutation·RGB/EEF timestamp·checkpoint input metadata를 읽기 전용으로 확인한다. Code/asset 호환성 확인을 실제 실행 성공으로 표시하지 않는다.
5. 짧은 문헌 심사 후 `CONTINUE / REVISE / STOP`을 결정한다. 선정되면 `내용/`과 `재현 방법/`의 두 폴더로 옮기고, 여기에는 선정 이유와 링크만 남긴다. 기존 후보의 전체 문서 절차를 복제하지 않는다.

이번에는 논문·프로젝트의 공개 설명과 지정 원문만 조사했다. 외부 논문은 아래 원장에 탐색 근거로 남겼으며 **paper registry 신규 등록은 하지 않았다**. 기존 paper ID가 없는 논문은 추가 여부를 N1에서 판단하고, 등록한다면 표준 5-note 절차를 따른다. Native code/정책 실행·Docker 환경 확인·패키지/weights 설치·PDF 로컬 다운로드는 하지 않았다. 현재 환경이 실험 불가능하다고 새로 판정한 것도 아니다.

## R1 저장소 검증

작업 전후 audit: 1,206편·6,030노트, CORE50/NEXT405/REFERENCE509/ARCHIVE242, active455/history47, 오류·경고 0. 필수 compile·tier 생성·diff 검사 통과. 작업 시작 시점의 SHA256과 비교하여 표준 노트 6,030개, canonical/runtime 보호 파일 183개, 기존 주제 dossier와 읽기 이력의 보존을 확인했다. 이번 변경은 기존 안내·합성 문서 9개와 새 보고서/원장 2개이며 삭제 0개다. 상세는 [원장](../sources/new_field_scout_2026-11-17.json)의 `validation`을 따른다. 이전 턴의 dirty 변경·삭제는 이번 작업으로 되돌리지 않았다.
