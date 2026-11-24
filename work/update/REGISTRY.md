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
| 가중치 | 16 | 4 | 0 | 30 |
| 데이터 | 15 | 7 | 1 | 27 |

공개 판정일은 2026-11-19다. Y는 논문에 대응하는 저자 배포를 확인한 경우, 부분은 공개 범위가 일부 구성요소·태스크·파일에 한정된 경우다. N은 저자가 미배포 또는 공개 예정임을 명시한 경우다. 사이트나 README만 있는 저장소는 확인한 범위를 적고 공개 여부를 unknown으로 둔다. 오류가 나는 다운로드 링크, 확인하지 못한 파일, 기존 벤치마크 재사용은 `unknown`으로 남긴다. 공개 상태는 다운로드한 모델의 실행 가능성까지 보증하지 않는다. [CLIP 학습 데이터](https://github.com/openai/CLIP/blob/main/model-card.md#data) · [Habitat 2.0 장면 배포 범위](https://aihabitat.org/datasets/replica_cad/) · [RLDG 공개 코드](https://github.com/generalist-distillation/RLDG)

- **공통 태그.** 데이터 출처는 해당 논문의 학습·벤치마크 구축 자료를 기준으로 한다. 여러 출처를 사용하면 `혼합`으로 표기한다. RFMPose는 합성 자료로만 학습한 뒤 실제 관측에서도 평가해 `합성`이다. `기타`는 점군 등 허용된 나머지 범주의 구체적인 입력·형태가 확인된 경우에 쓴다. [RFMPose](https://proceedings.neurips.cc/paper_files/paper/2025/hash/618c0a236e7aace748d09bc8fbed3e4d-Abstract-Conference.html)
- **전용 태그.** VLA나 Octo처럼 언어 지시로 여러 로봇의 행동을 생성하는 범용 정책을 설계·학습한 13편에 VLA 항목을 붙였다. 휴머노이드 기종이나 시뮬레이션 모델을 실제 사용한 10편에는 역할을 함께 적었다. 두 집합은 겹친다. FAST의 H1은 행동 토큰화 데이터에 등장한다. Ψ₀는 G1에서 전신 행동을 실행하며 기존 RL 하체 추종기를 사용한다. [FAST](https://arxiv.org/html/2501.09747) · [Ψ₀](https://www.roboticsproceedings.org/rss22/p021.html)
- **한계와 선행.** 저자가 적은 제약·평가 범위는 27편, 후속 논문이 설명한 제약은 2편에서 출처를 연결했다. 선행 ID는 배치 안에서 부록 ID, 배치 밖에서는 원장의 안정 ID를 사용한다. 문헌 관계를 확인한 27편에 기록했다. `unknown`은 확인 범위를 나타내며 선행이나 한계가 없다는 뜻으로 쓸 수 없다.
- **검증 수준.** 서지와 기여를 대조한 50편 각각에 공개 여부·세부 축·후속 연구 한계 등 미확정 필드가 남아 레코드 전체는 `부분확인`이다. `미공개`는 저자가 실제로 그렇게 명시할 때 사용한다. [기존 감사와 수정 범위](../../research/SOURCE_AUDIT.md#이전-감사)

**애매한 매핑 질문**

1. 웹 이미지–텍스트 대조학습·생성 모델과 자세 추정에 독립적인 방법 태그를 둘 것인가? 현재 어휘로 표현하기 어려운 CLIP·DDPM·RFMPose의 방법론은 `unknown`으로 두었다.
2. 연속 행동의 직접 회귀와 일관성 모델을 확산·flow와 별도 값으로 관리할 것인가? OFT의 L1 직접 회귀는 행동 표현 설명에 보존하고 전용 enum은 `unknown`으로 두었다.
3. UMI처럼 사람이 들고 움직이는 계측 그리퍼 시연을 데이터 출처로 추가할 것인가? 카메라 영상과 그리퍼 궤적을 함께 쓰므로 현재 분류에서 `unknown`으로 두었다. 미공개와 미확정을 구분하는 근거도 논문별로 기록한다.

**중복 후보**는 0쌍이다. 배치 내부 1,225쌍과 배치↔나머지 원장 58,850쌍에서 공개 식별자(DOI·버전 제외 arXiv·OpenReview), 정규화 제목과 유사 제목을 검사했다. 제목의 대폭 변경과 식별자 결측이 겹치는 경우에는 한계가 있다. [유사도 판정 기준](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/92d86a2ebcd2c2b99e32ff79424a5f2cd2eee747/research/REGISTRY_AUDIT.md#3-중복-의심)

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

논문 개요 278편에 연도·발표처의 항목명만 남아 있었다. 2026-11-23에 원장의 값으로 해당 표시를 복원했다. 무결성 검사는 1,252편 모두에서 개요 상단의 연도·발표처가 한 번 표시되고 원장과 일치하는지도 확인한다. [원장](../sources/papers.json) · [검사 코드](../scripts/audit_repository.py)

- Point2Graph의 노트 5개에서 원문에 표시된 `fi`·`fl` 합자를 확인해 글꼴 전용 문자 96개를 복원했다. Audio-VLA의 노트 5개에서는 페이지 경계에서 잘려 반복된 구성요소 설명을 복원했다. 글꼴과 문자 간 대응은 논문마다 달라 검사기는 해당 줄을 표시하고 보존한다. [Point2Graph 원문](https://arxiv.org/pdf/2409.10350v1) · [Audio-VLA 그림 2](https://arxiv.org/pdf/2511.09958v1#page=3) · [문자 검사](../scripts/audit_note_artifacts.py)
- PDF 원문 확인 요청 112개 노트를 포함해 55편의 노트 135개에서 손상된 구간 306개를 대조·수정했다. 수정 구간의 확인 수준과 논문 전체 정독을 구별한다. [논문별 원문·페이지·수정 근거](../sources/pdf_note_review_2026-10-23.json) · [후속 근거](../sources/pdf_note_review_followup_2026-10-23.json)
- 논문별 출처와 증거 수준은 [원장](../sources/papers.json)이 관리하고, 사용자 읽기 이력은 [읽기 기록](../../research/READING_STATUS.csv)에 둔다.

[직전 등록 원문과 게시 검증](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/update/REGISTRY_MAINTENANCE_2026-11-18.md) · [이전 등록·유지보수 기록](https://github.com/Kim-Yoo-Hyun/PaperReview/tree/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/update)
