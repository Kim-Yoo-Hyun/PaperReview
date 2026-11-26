# 레지스트리 변경

논문별 출처와 판정은 원장에 남기고, 여기에는 같은 검색어를 서로 다른 뜻으로 쓰기 쉬운 사례와 등록 기준을 모았다. [논문 목록](../../PAPER.md) · [전체 통계](../../research/REGISTRY_STATS.md) · [원문 감사](../../research/SOURCE_AUDIT.md)

## 구조 검증

2026-11-26에 논문 폴더 1,266개와 표준 노트 6,330개를 원장과 대조했다. 기간별 폴더, 파일 이름의 대소문자, Markdown 상대 링크와 문서 내 앵커, 읽기 이력, 생성 색인 경로를 점검했다. 논문 폴더에 남아 있던 PDF 실패 로그 한 개를 제거했다. 선택적 PDF 수집은 공식 원문 주소를 우선하고, 실패 시 임시 파일을 정리한 뒤 명령의 오류 출력에 기록한다. [유지보수 절차](../README.md#registry-maintenance)

평가 노트를 기준으로 사전과 원장의 검색 단서가 어긋난 794편을 동기화했다. 일반 단어 `map`을 지표 `mAP`로 검색하던 규칙을 수정해 평가 지표 연결은 1,872개에서 1,430개로 줄었다. 원장과 색인에는 `cue_only`로 표시한다. [지표 사전](../sources/metric_catalog.json) · [검색 색인](../../research/REGISTRY_INDEX.csv)

π₀의 404 프로젝트 주소를 저자 페이지로 교체했고, PointWorld의 CVPR 원문 주소를 다운로드 필드에 동기화했다. 이전 감사에서 링크 판정이 남았던 36편 중 10편은 저자 페이지 또는 공식 코드 파일을 재확인했다. 나머지 26편의 판정과 교정 전 주소는 감사 원장에 남겼다. [π₀ 저자 페이지](https://www.pi.website/blog/pi0) · [PointWorld 정식 원문](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_PointWorld_Scaling_3D_World_Models_for_In-The-Wild_Robotic_Manipulation_CVPR_2026_paper.html) · [링크 판정 집계](../../research/SOURCE_AUDIT.md#항목별-결과)

<a id="reference-tag-roles"></a>

## REFERENCE 검색 태그

REFERENCE 논문의 방법·평가 절에서 제안 방법, 사용한 구성요소, 학습·예측 대상, 평가 과제를 구분한다. 각 태그의 역할, 교정 전 값, 원문 쪽은 감사 원장의 `taxonomy_review.legacy_tags`에 있다. [배치별 집계](../../research/SOURCE_AUDIT.md#reference-검색-태그)

- **센서 융합.** BEVFusion은 카메라와 LiDAR 특징을 합친다. UniAD는 여러 카메라 영상에서 추적·예측·주행 계획을 함께 학습해 `Multi-Task Learning`으로 분류했다. [BEVFusion 그림 2](https://arxiv.org/pdf/2205.13542v3#page=2) · [UniAD 방법](https://openaccess.thecvf.com/content/CVPR2023/papers/Hu_Planning-Oriented_Autonomous_Driving_CVPR_2023_paper.pdf#page=2)
- **강화학습.** Embodied-R1의 GRPO는 목표점 추론을 학습한다. Interleave-VLA의 π₀ 구현은 시연에 flow matching을 적용한다. SimWorld-Robotics에서 VLA-RL은 벤치마크의 비교군이다. [Embodied-R1 학습](https://proceedings.iclr.cc/paper_files/paper/2026/file/0f7ad318868d228b980b13cf827e85f4-Paper-Conference.pdf#page=5) · [Interleave-VLA 학습](https://proceedings.iclr.cc/paper_files/paper/2026/file/444876e32cba0408c63f5295481cfe20-Paper-Conference.pdf#page=5) · [SimWorld-Robotics 표 2](https://papers.neurips.cc/paper_files/paper/2025/file/4a81c1aad3064fb8243b8938a49ecca0-Paper-Conference.pdf#page=7)
- **실행 중 탐색과 정책 학습.** VLA-Reasoner는 시연 진행도를 회귀한 점수로 MCTS의 후보 행동을 고른다. SAGE-Nav는 내비게이션 보상으로 그래프 인코더와 저수준 정책을 A3C 학습한다. [VLA-Reasoner Ⅲ-D절](https://arxiv.org/pdf/2509.22643v2#page=4) · [SAGE-Nav 강화학습 목적함수](https://arxiv.org/pdf/2606.25497v1#page=5)
- **LiDAR와 레이더.** ODG는 LiDAR로 훈련용 정답을 만들고 카메라로 추론한다. RadarSplat은 주사식 레이더로 복원한 기하를 LiDAR로 평가한다. V2X-R의 검출기는 LiDAR와 4D 레이더를 함께 입력받는다. 레이더 입력 두 편은 감사 원장의 `unmapped_modality`에 기록했고, `radar` 검색 필터는 추가 후보로 남겼다. [ODG 식 18](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e14be0332c04c76742710e417cedb2a-Paper-Conference.pdf#page=6) · [RadarSplat 입력](https://openaccess.thecvf.com/content/ICCV2025/papers/Kung_RadarSplat_Radar_Gaussian_Splatting_for_High-Fidelity_Data_Synthesis_and_3D_ICCV_2025_paper.pdf#page=3) · [RadarSplat 평가](https://openaccess.thecvf.com/content/ICCV2025/papers/Kung_RadarSplat_Radar_Gaussian_Splatting_for_High-Fidelity_Data_Synthesis_and_3D_ICCV_2025_paper.pdf#page=6) · [V2X-R 그림 4](https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_V2X-R_Cooperative_LiDAR-4D_Radar_Fusion_with_Denoising_Diffusion_for_3D_CVPR_2025_paper.pdf#page=4)

- **조작 정책의 입력.** Transporter Networks는 정사영한 RGB-D 영상으로 시연의 집기·놓기 행동을 학습한다. RT-Trajectory는 머리 카메라 RGB와 궤적 스케치로 행동을 복제한다. 언어모형이 스케치를 그리는 조건에서도 제어 정책에 들어가는 것은 스케치다. 두 논문은 시각 모방학습 비교 대상으로 검색할 수 있다. [Transporter 입력과 행동](https://proceedings.mlr.press/v155/zeng21a/zeng21a.pdf#page=3) · [Transporter 시연 학습](https://proceedings.mlr.press/v155/zeng21a/zeng21a.pdf#page=6) · [RT-Trajectory 정책과 스케치 생성](https://proceedings.iclr.cc/paper_files/paper/2024/file/c383e44d9a878d1982d9abb838bd5d8a-Paper-Conference.pdf#page=5)

- **시뮬레이터 보정.** ASAP는 실물 G1의 궤적을 이용해 시뮬레이터의 행동 입력에 더할 보정량을 학습한다. 그림 4의 delta-dynamics는 다음 상태를 직접 보정하는 비교 방법이다. 원장에 제안 방법과 비교군의 역할을 기록했다. [ASAP 방법](https://www.roboticsproceedings.org/rss21/p066.pdf#page=3) · [그림 4와 비교 결과](https://www.roboticsproceedings.org/rss21/p066.pdf#page=5)

- **세계 모델과 제어 정책.** GWM은 RGB 관측에서 복원한 장면과 로봇 행동으로 다음 3D 장면을 예측한다. 모방학습·모델 기반 RL은 이 표현과 예측기를 활용한 실험이다. MVP는 마스크 복원으로 학습한 시각 인코더를 동결하고 시뮬레이션 조작 정책을 PPO로 학습한다. [GWM 그림 2·방법](https://openaccess.thecvf.com/content/ICCV2025/papers/Lu_GWM_Towards_Scalable_Gaussian_World_Models_for_Robotic_Manipulation_ICCV_2025_paper.pdf#page=4) · [MVP 제어기 학습](https://arxiv.org/pdf/2203.06173v1#page=3)

- **잔차 행동의 학습 신호.** A2C2는 새 관측을 받을 때마다 기본 행동에 더할 보정량을 시연 행동과의 차이로 학습한다. Foresight Residual RL은 고정한 후속 정책의 성공 확률을 종단 보상에 반영하고 PPO로 잔차 정책을 학습한다. [A2C2의 학습 목표](https://arxiv.org/pdf/2509.23224v1#page=5) · [후속 정책의 성공 확률](https://arxiv.org/pdf/2607.16506v1#page=5) · [잔차 PPO 학습](https://arxiv.org/pdf/2607.16506v1#page=6)

- **실행 시 깊이 입력.** PEAfowl은 배포 때도 네 카메라의 RGB-D를 입력받는다. 추가 깊이 교사는 훈련에만 쓴다. PROSPECT는 단안 RGB로 공간 특징을 계산하고, 미래 공간 표현의 예측을 훈련 보조 목표로 쓴다. [PEAfowl 그림 2](https://arxiv.org/pdf/2601.17885v2#page=3) · [PEAfowl 배포 사양](https://arxiv.org/pdf/2601.17885v2#page=9) · [PROSPECT 항법 입력](https://arxiv.org/pdf/2603.03739v1#page=5)

<a id="taxonomy-batches"></a>

## 다축 태그와 공개 범위

2026년 11월 25일 기준 집중 읽기 **500/500편**을 분류했다. 정규화 10개 배치의 CORE 50편·NEXT 427편에 별도 등록한 NEXT 23편이 더해진다. 두 목록은 안정 ID가 겹치지 않는다. YAML의 `registry_id`로 원장을 조회하고 `changed_from`으로 분류 전 값을 확인한다. [배치 정의](../sources/registry_meta.json) · [별도 등록 23편](../sources/batches/gapfill_2026_11.yaml)

| 분류할 때의 질문 | 판정 근거 |
|---|---|
| 무엇을 학습하거나 제어하는가? | 시연·교사 행동은 IL, 보상에 의한 정책·가치 갱신은 RL, 예측 동역학을 이용한 계획·학습은 모델기반으로 기록한다. 하위 제어기와 정책을 각각 확인한다. |
| 어느 로봇의 어떤 행동인가? | 조작·내비게이션·이동·전신제어·모바일매니퓰레이션은 실제 과업을 따른다. 로봇 형상은 명시된 기체나 구성에서 확인한다. |
| 실행 중 정책이 무엇을 볼 수 있는가? | 기록한 센서, 정책에 입력한 센서, 학습 시에만 사용한 상태를 구별한다. 장면 영상·센서 깊이·광학식 촉각·손목 힘/토크는 신호의 역할을 명시한다. |
| 자료를 어디에서 얻었는가? | 인간 영상, 실제 로봇 시연, 사람이 원격조작한 시뮬레이션, 합성 자료를 구분한다. 실물에서 평가했다는 사실은 학습 자료의 출처를 결정하지 않는다. |
| 전용 태그는 무엇을 설명하는가? | VLA의 백본·배포 시 행동 표현·학습 방식·평가 조건, 휴머노이드의 제어 범위·학습·기종·손을 기록한다. 기존 정책만 비교한 실험에는 평가 대상임을 표시한다. |
| 어떤 파일을 공개했는가? | 코드·가중치·데이터를 따로 판정한다. 구현 범위, 모델 버전, 훈련·평가용 여부를 저자가 배포한 파일에 연결한다. 미확인은 `unknown`, 저자가 공개하지 않았다고 명시한 경우는 `N`이다. |

<a id="첫-배치-태그-매핑"></a>
<a id="두-번째-배치-태그-매핑"></a>
<a id="세-번째-배치-태그-매핑"></a>
<a id="네-번째-배치-태그-매핑"></a>
<a id="다섯-번째-배치-태그-매핑"></a>
<a id="여섯-번째-배치-태그-매핑"></a>
<a id="일곱-번째-배치-태그-매핑"></a>
<a id="여덟-번째-배치-태그-매핑"></a>

### 배치별 근거

| 검토 범위 | 재사용할 때 주의할 사례 | 이전 값·원문 위치 |
|---|---|---|
| CLIP ~ RFMPose | OFT의 L1 직접 회귀와 계측용 휴대 그리퍼 시연은 기존 열거값으로 표현하기 어려워 설명을 보존했다. JALA와 Ctrl-World의 공개 판정에는 후속 교정이 있다. | [첫 50편](../sources/batches/core_next_01.yaml) |
| Diffusion Policy ~ GaussianGrasper | 연속 행동 회귀와 공간 복셀 선택은 다른 출력이다. 자세·형상 평가에 해당하는 논문은 로봇 과업의 실행 근거를 따로 찾는다. | [두 번째 50편](../sources/batches/core_next_02.yaml) |
| Clio ~ PIN-WM | DAPG의 시연·정책, RoboPack의 체크포인트·표본 데이터는 각각 공개 범위가 다르다. Q-Transformer의 과제 세부 수는 본문과 그림 표기가 달라 둘 다 기록했다. | [세 번째 50편](../sources/batches/core_next_03.yaml) |
| Dexterous World Models ~ Memory Retrieval in Visuomotor Policies | WMPO는 세계 모델 안에서 정책을 학습한다. PALM의 실물 평가는 여섯 하위 동작을 포함하는 과제 한 개다. | [네 번째 50편](../sources/batches/core_next_04.yaml) |
| DexterityGen ~ RoboSplat | DIGIT과 후속 센서 DIGIT 360의 배포처를 구별했다. CordViP의 실물 장치는 단일 UR5와 LEAP Hand다. | [다섯 번째 50편](../sources/batches/core_next_05.yaml) |
| PartInstruct ~ OopsieVerse | NavDP와 LoGoPlanner의 별칭, GR00T N1·N1.5·N1.6의 체크포인트는 판본별로 대조했다. RLinf-VLA 실물 서랍 닫기에서는 비교한 두 정책이 각각 8/10회 성공했다. | [여섯 번째 50편](../sources/batches/core_next_06.yaml) |
| USER ~ TidyBot++ | 카메라 시점을 복원하는 CoRe-VLA와 전문가 선택을 다루는 CoRE-VLA는 다른 연구다. TidyBot++의 배포 시연·가중치는 sim-v1 예제에 해당한다. | [일곱 번째 50편](../sources/batches/core_next_07.yaml) |
| PhysTwin ~ Force Policy | Spa-Bench는 저장한 카메라와 정책에 사용한 카메라가 다르다. Force Policy는 실물 세 과제를 평가했고, 확인된 정책·데이터는 상자 뒤집기용이다. | [여덟 번째 50편](../sources/batches/core_next_08.yaml) |
| Q2RL ~ Tune to Learn | Q2RL의 공개 체크포인트는 행동 복제 초기 정책이다. ControlVLA 게재본은 단기 6개와 장기 2개를 평가하며 76.7%는 단기 6개 평균이다. Tune to Learn의 G1 속도 추종과 FR3 실물 도달은 별도 비교다. | [아홉 번째 50편](../sources/batches/core_next_09.yaml) |
| Offline Policy Evaluation ~ PRISM | Real-Time EXPO-FT의 실물 조작 4과제와 Kinetix 모의 10과제를 분리했다. RoboAlign의 FAST 토큰은 정렬 보상을 계산하고, 하류 로봇은 확산 헤드의 행동을 실행한다. FoundationPose의 합성 학습 데이터·가중치와 AC²-VLA의 이전한 코드도 확인했다. | [열 번째 27편](../sources/batches/core_next_10.yaml) |

이전 배치의 NEXT 20편은 검색 태그도 원문과 대조했다. POGS는 물체의 6D 자세 추적, *Estimate, Don’t Imitate*는 상태 추정기와 기존 정책의 재사용으로 찾을 수 있다. *Recurrent World Models*의 평가 환경은 CarRacing과 Doom이다. 최초 판정과 교정 근거는 논문별 `taxonomy_review.legacy_tags`에 보존했다. [원문 감사](../../research/SOURCE_AUDIT.md#다축-태그와-공개-자료)

직접 회귀, 지도 구축·진단만 수행하는 방법, 계측용 휴대 그리퍼에서 온 시연은 기존 분류에 맞는지 미확정이다. 원문에서 확인한 실제 역할을 서술하고 불명확한 축은 `unknown`으로 둔다. 각 판정 시점의 기존 태그 전체 매핑, 중복 후보와 검색 기준, 배포 범위의 변경 내역은 원래의 표와 감사 원장에서 조회할 수 있다. [기존 태그 전체 매핑](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/6aa75b27be4ab2e88ab56cd54df5818317e7a2fb/work/update/REGISTRY.md#taxonomy-batches) · [항목별 공개 여부](../../research/SOURCE_AUDIT.md#다축-태그와-공개-자료)

<a id="reg-r18"></a>

## 등록·서지 교정

- 접촉 제어 비교표의 아홉 편 가운데 기존 다섯 편을 확인하고 네 편을 REFERENCE로 등록했다. ACP(`pr-1263`, ICRA 2025)는 시연에서 가변 강성을 배우는 기준선이다. FTP-1(`pr-1264`, CoRL 2026)은 센서 간 촉각 전이, HapticVLA(`pr-1265`, IROS 2026)는 훈련용 촉각의 증류, N₀-VTLA(`pr-1266`, arXiv 2026)는 배포 궤적을 이용한 오프라인 정책 개선을 비교하는 근거다. [논문별 원문과 평가](../../research/VLA_ACTION_SPACE.md#추가-조사)
- VLA의 정책 출력과 실행 제어기를 대조해 10편(`pr-1253`~`pr-1262`)을 REFERENCE에 등록했다. 관절각·각속도·토크를 함께 명령하는 Bi-LAT/Bi-VLA, 전신 행동을 학습한 HumanVLA/LHM-Humanoid, 힘·강성·감쇠를 다룬 Tactile-VLA/Compliance for Free/PaCo-VLA, 이동·태스크 전환을 다룬 SPOC/OneTwoVLA/G0.5다. 총 28편의 원장 포함 여부와 직접 확인한 출력·평가 조건은 비교표에서 찾을 수 있다. [VLA 행동 공간](../../synthesis/04_vla.md#vla-action-interfaces) · [원장 색인](../../research/REGISTRY_INDEX.csv)
- 공유 제어 문헌 HARMONIC과 Residual Copilot을 REFERENCE에 추가했다. 두 논문은 각각 보조 전후의 명령 기록과 보조 시연으로 학습한 정책의 실물 기어 삽입 평가를 제공한다. DROID의 RSS 게재본과 저자 배포 자료도 연결했다. [HARMONIC](../../2022/IJRR/2022_IJRR_HARMONIC-A-multimodal-dataset-of-assistive-humanrobot-coll/01_overview.md) · [Residual Copilot](../../2026/CoRL/2026_CoRL_Efficient-and-Reliable-Teleoperation-through-Real-to-Sim-t/01_overview.md) · [DROID 게재본](https://www.roboticsproceedings.org/rss20/p120.html)
- 외부 목록과 대조한 36편 중 23편을 NEXT에 등록했고 9편을 보류했다. 4편은 기존 ID와 일치했다. 직접 선행 추가 18편, 3D 추정 문헌, Ψ₀를 포함한 이전 등록의 선정 근거도 조회할 수 있다. [누락 심사와 대조 범위](../../research/GAPFILL.md#external-coverage) · [직접 선행 등록](../sources/registry_maintenance_2026-11-18.json) · [Ψ₀ 교정](../sources/registry_accuracy_2026-11-16.json)
- OpenVLA의 선행·후속 관계와 DINOv2·RT-2의 게재 서지를 대조했다. TrajOpt의 잘못된 arXiv 식별자는 IJRR 게재 DOI와 저자 PDF로 교정했다. [OpenVLA 계보](../../research/OPENVLA_LINEAGE.md) · [TrajOpt 게재본](https://doi.org/10.1177/0278364914528132) · [CORE 심화 검토](../sources/batches/tier1_vla_humanoid.yaml)

### 프리프린트 게재 확인

등록 전 원장에서 arXiv로 분류한 74편을 2026년 10개 학회 목록과 정규화 제목으로 대조했다. 이 조건에서 새로 확인된 게재본은 **0편**이었다. GR00T N1의 저자판 제목은 기존 별칭으로, πRL의 수식 표기는 arXiv ID로 확인했다. 제목이 크게 바뀐 판본이나 다른 연도·발표처의 게재 여부는 이 비교만으로 확정할 수 없다.

| 대조 대상 | 사용한 원본 목록 |
|---|---|
| 로보틱스 | [ICRA · IEEE 기탁 서지](https://api.crossref.org/works?filter=container-title%3A2026+IEEE+International+Conference+on+Robotics+and+Automation+%28ICRA%29%2Ctype%3Aproceedings-article) · [IROS 논문 색인](https://2026.ieee-iros.org/program/paper-index/) · [CoRL 채택 목록](https://2026.corl.org/program/accepted-papers/) · [RSS 게재본](https://www.roboticsproceedings.org/rss22/index.html) |
| 머신러닝·AI | [NeurIPS](https://neurips.cc/static/virtual/data/neurips-2026-orals-posters.json) · [ICLR](https://iclr.cc/static/virtual/data/iclr-2026-orals-posters.json) · [ICML](https://icml.cc/static/virtual/data/icml-2026-orals-posters.json) · [IJCAI](https://www.ijcai.org/proceedings/2026/) |
| 컴퓨터 비전 | [CVPR 게재본](https://openaccess.thecvf.com/CVPR2026?day=all) · [ECCV 공식 프로그램](https://eccv.ecva.net/static/virtual/data/eccv-2026-orals-posters.json) |

<a id="note-review"></a>

## 노트 교정

인사이트 노트 943편에 남아 있던 분류 문장을 현행 원장과 대조했다. 등급·트랙·태그가 달라진 129편은 논문 개요의 현재 분류를 참조하도록 고쳤다. 원문 해석과 사용자 읽기 기록은 보존했다. [등급·노트 동기화 명령](../README.md#registry-maintenance)

원문 쪽수와 텍스트 수정을 연결해 둔 기록이다. PDF 추출 감사에서는 55편의 노트 135개에서 306개 구간을 대조·수정했다. 11월 24일 수식·도식 감사에서는 10편의 노트 31개에서 91줄을 확인했다. 숫자는 각 감사의 단위와 범위로 해석한다. [PDF 추출 교정](../sources/pdf_note_review_2026-10-23.json) · [후속 교정](../sources/pdf_note_review_followup_2026-10-23.json) · [수식·도식 감사](../../research/SOURCE_AUDIT.md#노트의-수식과-도식) · [논문별 감사 원장](../sources/batches/source_audit_2026_11.jsonl)
