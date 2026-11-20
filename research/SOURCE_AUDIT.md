# 원문 전수 감사

2026-11-20 KST 기준으로 감사 시작 시점의 원장 1,252개 항목을 고정했다. 논문과 저자 기술 발표 1,252건의 존재를 확인했다. 교정 전 한 항목 이상에서 사실 오류가 확인된 논문은 **109/1,252편(8.71%)**이다. 여러 필드에 걸친 오류는 총 132건이다. [교정 전 원장](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/76a2c37c00a509041be7ed66e11eb667af2e79d1/work/sources/papers.json) · [논문별 판정·교정값·원문 위치](../work/sources/batches/source_audit_2026_11.jsonl)

## 판정 기준

- **통과**는 해당 항목의 기록과 근거가 일치한다는 뜻이다. **수정 필요**는 교정 전 판정이며, 원문과 모순되거나 오류가 입증된 기록은 ‘오류’, 누락·불완전 기록을 채우거나 근거 없는 단정을 완화한 경우는 ‘보완’으로 구분한다.
- 저자 필드의 빈칸을 채우거나 `project_only`에서 구현 파일을 처음 식별한 경우는 보완으로 집계한다. `not_released`로 기록한 산출물의 실제 배포 파일을 확인한 경우는 오류다.
- **존재 불확실**은 해당 필드에 필요한 근거를 확보하지 못했다는 뜻이다. 예를 들어 저자 배포 가중치의 존재를 확인하지 못한 논문도 표제면과 발표처는 각각 통과할 수 있다. 접근 제한만으로 링크 오류나 미공개를 선언하지 않았다.
- **서지와 링크.** 원래 기재된 원문·프로젝트·코드 URL을 열고 제목이나 대상과 대조했다. 반복 404나 다른 논문으로의 연결은 오류로 셌다. 브라우저 확인 화면·접근 제한에서는 접근 가능한 동일 논문 판본을 찾고 원래 주소와 새 주소를 기록했다. 프리프린트 연도, 학회 개최연도, 논문집 출판연도, 저널 권호를 구분했다. 저자 순서는 해당 판본의 표제면 또는 출판사 서지를 따랐다. 학회 프로그램에 나열된 발표자 순서는 저자 순서로 사용하지 않았다.
- **PDF 링크.** 별도 PDF 주소가 등록된 871편 중 830편에서 파일 서명 또는 해당 논문의 표제면을 확인했다. 나머지 41편은 링크 판정에 미확인으로 반영했다. 별도 PDF 주소가 없는 논문은 공식 원문 링크로 점검했다.
- **요약과 기여.** 공식 초록과 저자 원문을 대조했다. 1,070편은 표제를 확인한 PDF 본문 또는 HTML 본문 구획을 추가로 확보했다. PDF의 선택된 쪽이나 HTML의 일부 절을 읽은 것만으로 기여 전체를 통과시키지 않았다. 원문 문장의 위치만 복원한 경우에는 저자 자신의 연구인지, 어떤 조건의 결과인지가 확인될 때까지 미확인으로 남겼다. 직전 배치의 원문 대조를 재사용한 경우 개별 근거에 날짜와 대상을 표시했다.
- **공개 여부.** 논문의 구현, 해당 버전의 모델 파일, 저자가 배포한 데이터 목록을 각각 점검했다. 비교 방법 재구현, 다른 세대의 체크포인트, 프로젝트 홈페이지는 별도로 구분했다. 부분 공개는 확인한 파일 또는 구성요소 수준에서만 통과다. 다운로드·학습·실기 재현은 이 판정에 포함되지 않는다.
- **태그.** 원래 태그가 저자의 입력·방법·평가 또는 명시된 검색 주제와 연결되는지 확인했다. 남은 태그의 역할이 모호하면 미확인으로 뒀다. 아래에는 확인된 불일치만 설명한다.
- **판본 이력.** 논문 노트에서 날짜가 적힌 과거 PDF 추출 기록은 그때 사용한 판본을 가리킨다. 현재 원문은 overview의 Official paper와 원장에서, 교체한 주소와 사유는 이 감사의 논문별 근거에서 확인할 수 있다.

## 항목별 결과

| 항목 | 교정 전 확인 오류 | 보완 | 교정 후 통과 | 교정 후 존재 불확실 |
|---|---:|---:|---:|---:|
| 링크 | 30 | 326 | 1187 | 65 |
| 제목 | 20 | 0 | 1252 | 0 |
| 저자 | 0 | 1225 | 1252 | 0 |
| 연도 | 28 | 0 | 1252 | 0 |
| 발표처·게재 | 30 | 0 | 1182 | 70 |
| 요약·기여 | 8 | 112 | 223 | 1029 |
| 코드 | 1 | 127 | 289 | 963 |
| 가중치 | 0 | 52 | 71 | 1181 |
| 데이터 | 1 | 42 | 72 | 1180 |
| 태그 | 14 | 0 | 394 | 858 |
| 공개 여부 3종 합집합(논문 수) | 2 | 186 | 25 | 1227 |

같은 논문에 오류와 보완이 함께 있으면 두 열에 각각 들어간다. 논문 기준으로는 오류 109편, 보완 1,230편, 교정 후 전 항목 통과 8편이다. 잔여 확인 오류는 0편이며, 하나 이상 미확인 필드가 남은 논문은 1,244편이다.

**[해석]** 교정 전 오류율은 이번 전수 선별에서 확인한 하한이다. 미확인 필드까지 모두 판독한 뒤의 오류율은 아직 계산할 수 없다. 전체 원장을 대상으로 한 집계여서 표본 신뢰구간을 적용하지 않는다. 후속 전수 검증은 미확인 필드를 대상으로 이어갈 필요가 있다. 연구 비교에서 인용할 요약·기여의 주체와 실험 조건, 가중치·데이터의 버전과 라이선스·공개 범위를 우선한다. 직전 CORE/NEXT 층화표본의 오류율은 모집단과 감사 전 상태가 달라 이번 수치와 합산하지 않는다. [50편 표본 감사](./SAMPLE_AUDIT.md)

## 읽기 등급별 확인 범위

| 감사 당시 등급 | 편수 | 요약·기여 통과 | 태그 통과 | 코드·가중치·데이터 모두 통과 |
|---|---:|---:|---:|---:|
| CORE | 50 | 50 | 50 | 6 |
| NEXT | 450 | 88 | 90 | 14 |
| REFERENCE | 510 | 61 | 143 | 5 |
| ARCHIVE | 242 | 24 | 111 | 0 |

## 배치별 결과

| 배치 | 안정 ID | 편수 | 교정 전 오류 논문 | 확인 오류율 | 보완 논문 | 교정 후 미확인 논문 |
|---:|---|---:|---:|---:|---:|---:|
| [1](#batch-01) | pr-0001–pr-0100 | 100 | 9 | 9.00% | 100 | 97 |
| [2](#batch-02) | pr-0101–pr-0200 | 100 | 3 | 3.00% | 100 | 100 |
| [3](#batch-03) | pr-0201–pr-0300 | 100 | 9 | 9.00% | 100 | 100 |
| [4](#batch-04) | pr-0301–pr-0400 | 100 | 5 | 5.00% | 100 | 100 |
| [5](#batch-05) | pr-0401–pr-0500 | 100 | 4 | 4.00% | 100 | 100 |
| [6](#batch-06) | pr-0501–pr-0600 | 100 | 10 | 10.00% | 100 | 100 |
| [7](#batch-07) | pr-0601–pr-0700 | 100 | 16 | 16.00% | 100 | 99 |
| [8](#batch-08) | pr-0701–pr-0800 | 100 | 14 | 14.00% | 100 | 99 |
| [9](#batch-09) | pr-0801–pr-0900 | 100 | 10 | 10.00% | 100 | 99 |
| [10](#batch-10) | pr-0901–pr-1000 | 100 | 4 | 4.00% | 100 | 100 |
| [11](#batch-11) | pr-1001–pr-1100 | 100 | 15 | 15.00% | 100 | 100 |
| [12](#batch-12) | pr-1101–pr-1200 | 100 | 8 | 8.00% | 100 | 100 |
| [13](#batch-13) | pr-1201–pr-1252 | 52 | 2 | 3.85% | 30 | 50 |

## 태그 불일치

| ID | 제거 | 반영 | 원문에서 확인한 차이 |
|---|---|---|---|
| pr-0043 | Planning | multi-view | 카메라 여러 대의 BEV로 3D 감지와 지도 분할을 평가한다. 경로 계획 출력을 평가하지 않는다. [원문](https://arxiv.org/abs/2203.17270) |
| pr-0313 | sensor fusion | — | 단일 LiDAR 스캔으로 빈 영역을 완성한다. [원문](https://openaccess.thecvf.com/content/CVPR2024/html/Nunes_Scaling_Diffusion_Models_to_Real-World_3D_LiDAR_Scene_Completion_CVPR_2024_paper.html) |
| pr-0316 | sensor fusion, LiDAR | point cloud | 기하·의미 특징을 융합한다. §4의 3RScan은 RGB-D 실내 재구성에서 얻은 점군이다. [원문](https://openaccess.thecvf.com/content/CVPR2024/html/Xie_SG-PGM_Partial_Graph_Matching_Network_with_Semantic_Geometric_Fusion_for_CVPR_2024_paper.html) |
| pr-0321 | sensor fusion | — | 학습 감독은 단일 시점에서 얻은 두 번 반사된 LiDAR 신호다. [원문](https://openaccess.thecvf.com/content/CVPR2024/html/Klinghoffer_PlatoNeRF_3D_Reconstruction_in_Platos_Cave_via_Single-View_Two-Bounce_Lidar_CVPR_2024_paper.html) |
| pr-0333 | sensor fusion, LiDAR | semantic occupancy | 같은 카메라 모달리티에서 시계열 점유 예측을 융합한다. [원문](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Rethinking_Temporal_Fusion_with_a_Unified_Gradient_Descent_View_for_CVPR_2025_paper.html) |
| pr-0412 | sensor fusion | — | 입력 LiDAR 관측으로 새로운 LiDAR 관측을 렌더링한다. [원문](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8e86fd925dda476f574689f4ce748193-Abstract-Conference.html) |
| pr-0745 | action generation | image generation | 원 논문이 학습하는 대상은 생성 확률 경로이며, 검증은 ImageNet 영상 생성이다. 로봇 행동 생성은 이 방법의 후속 응용이다. [원문](https://iclr.cc/virtual/2023/poster/11309) |
| pr-0835 | Robotics | — | 원 논문은 시간차 예측·수렴의 특수 경우 및 예시를 검증한다. 로봇 실험이나 로봇 모델은 연구 대상에 포함되지 않는다. [원문](https://doi.org/10.1007/BF00115009) |
| pr-1011 | action-interface, cross-embodiment | grasping, motion planning, manipulation | 실패를 집기와 후속 계획에 귀속하고 여러 정책 계열을 비교한다. 실험의 전이 단위는 기체가 아니다. [원문](https://neurips.cc/virtual/2026/poster/155467) |
| pr-1030 | action-interface, cross-embodiment | active perception, manipulation, robustness | 시점 변경이 만든 첫 관측·자세의 분포 변화를 다룬다. 전이 평가의 단위는 카메라 조건·정책·과제다. [원문](https://arxiv.org/abs/2610.23378) |
| pr-1031 | VLA, action-interface, cross-embodiment | active perception, bimanual manipulation, Reinforcement Learning, Imitation Learning | 양안 주시 제어를 강화학습하고 그리퍼 정책을 행동복제로 학습한다. 평가 변수는 시선과 카메라 배치다. [원문](https://arxiv.org/abs/2610.03710) |
| pr-1033 | action-interface, cross-embodiment | offline-RL, counterfactual, manipulation | 같은 전문가 궤적에서 반사실적 행동 감독을 구성한다. 분할은 물체 위치·과제 교란이며 기체 간 전이를 시험하지 않는다. [원문](https://arxiv.org/abs/2608.21740) |
| pr-1035 | action-interface, cross-embodiment | action representation, language grounding, manipulation | 동일한 목표에서 언어로 지정된 실행 제약을 구분한다. 시뮬과 실물에서 제약 준수를 평가한다. [원문](https://arxiv.org/abs/2603.17524) |
| pr-1121 | reward-modeling | Reinforcement Learning | 데모 행동과의 일치·정렬·출력 형식으로 보상을 정의한다. 사전학습한 보상 모델이 없어도 적용하도록 설계했다. [원문](https://roboticsproceedings.org/rss22/p086.html) |

## 논문별 판정

**✓** 통과 · **오→✓** 사실 오류 교정 · **보→✓** 누락·근거 보완 · **?** 존재 불확실 · **오→? / 보→?** 확인된 기록을 교정하거나 보완했고 같은 항목에 미확인 사항이 남았다. 각 행은 안정 ID 순서다. `work/sources/batches/source_audit_2026_11.jsonl`의 같은 ID에서 필드별 원문 주소, 이전 값·교정값, 접근 상태, 배포 파일 또는 대조 위치를 확인할 수 있다.

<a id="batch-01"></a>

### 배치 01

| ID · 공식 표제 | 링크 | 제목 | 저자 | 연도 | 발표처·게재 | 요약·기여 | 코드 | 가중치 | 데이터 | 태그 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [pr-0001](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html) Attention Is All You Need | ✓ | ✓ | 보→✓ | ✓ | ✓ | 오→✓ | ✓ | ? | ? | ? |
| [pr-0002](https://arxiv.org/abs/1810.04805) BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | 보→✓ | ? | ? |
| [pr-0003](https://proceedings.neurips.cc/paper_files/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) Language Models are Few-Shot Learners | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | 보→? | ? | ? | ? |
| [pr-0004](https://iclr.cc/static/virtual/data/iclr-2021-orals-posters.json) An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale | ✓ | ✓ | 보→✓ | ✓ | ✓ | 오→✓ | ✓ | 보→✓ | ? | ? |
| [pr-0005](https://proceedings.mlr.press/v139/radford21a.html) Learning Transferable Visual Models From Natural Language Supervision | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| [pr-0006](https://arxiv.org/abs/2304.07193) DINOv2: Learning Robust Visual Features without Supervision | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | 보→✓ | ? | ? |
| [pr-0007](https://openaccess.thecvf.com/content/ICCV2023/html/Kirillov_Segment_Anything_ICCV_2023_paper.html) Segment Anything | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | 보→✓ | ? | ? |
| [pr-0008](https://proceedings.neurips.cc/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html) Denoising Diffusion Probabilistic Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-0009](https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html) High-Resolution Image Synthesis with Latent Diffusion Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? |
| [pr-0010](https://arxiv.org/abs/2003.08934) NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | ? | 보→✓ | ✓ |
| [pr-0011](https://arxiv.org/abs/2308.04079) 3D Gaussian Splatting for Real-Time Radiance Field Rendering | ✓ | ✓ | 보→✓ | ✓ | ✓ | 오→✓ | ✓ | 보→✓ | 보→✓ | ? |
| [pr-0012](https://api.crossref.org/works/10.1109/cvpr.2017.16) PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? |
| [pr-0013](https://proceedings.neurips.cc/paper_files/paper/2017/hash/d8bf84be3800d12f74d8b05e9b89836f-Abstract.html) PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? |
| [pr-0014](https://proceedings.neurips.cc/paper_files/paper/2020/hash/15231a7ce4ba789d13b722cc5c955834-Abstract.html) SE(3)-Transformers: 3D Roto-Translation Equivariant Attention Networks | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0015](https://proceedings.mlr.press/v139/satorras21a.html) E(n) Equivariant Graph Neural Networks | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? |
| [pr-0016](https://api.crossref.org/works/10.1109/tro.2015.2463671) ORB-SLAM: A Versatile and Accurate Monocular SLAM System | ✓ | ✓ | 보→✓ | ✓ | ✓ | 오→✓ | ✓ | ? | ? | ? |
| [pr-0017](https://proceedings.neurips.cc/paper_files/paper/2021/hash/89fcd07f20b6785b92134bd6c1d0fa42-Abstract.html) DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ |
| [pr-0018](https://proceedings.neurips.cc/paper_files/paper/2021/hash/7f489f642a0ddb10272b5c31057f0663-Abstract.html) Decision Transformer: Reinforcement Learning via Sequence Modeling | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? |
| [pr-0019](https://www.roboticsproceedings.org/rss19/p026.html) Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | 보→✓ | 보→✓ | ✓ |
| [pr-0020](https://proceedings.mlr.press/v205/ichter23a.html) Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ✓ |
| [pr-0021](https://arxiv.org/abs/2212.06817) RT-1: Robotics Transformer for Real-World Control at Scale | ✓ | ✓ | 보→✓ | 오→✓ | 오→✓ | 보→✓ | 보→✓ | 보→✓ | 보→✓ | ? |
| [pr-0022](https://proceedings.mlr.press/v229/zitkovich23a.html) RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | ✓ | ✓ | ✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0023](https://proceedings.mlr.press/v202/driess23a.html) PaLM-E: An Embodied Multimodal Language Model | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0024](https://arxiv.org/abs/2310.08864) Open X-Embodiment: Robotic Learning Datasets and RT-X Models | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | 보→✓ | ? | ✓ | ✓ |
| [pr-0025](https://arxiv.org/abs/1912.08830) ScanRefer: 3D Object Localization in RGB-D Scans using Natural Language | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0026](https://referit3d.github.io/) ReferIt3D: Neural Listeners for Fine-Grained 3D Object Identification in Real-World Scenes | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0027](https://openaccess.thecvf.com/content/ICCV2021/html/Zhao_3DVG-Transformer_Relation_Modeling_for_Visual_Grounding_on_Point_Clouds_ICCV_2021_paper.html) 3DVG-Transformer: Relation Modeling for Visual Grounding on Point Clouds | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0028](https://api.crossref.org/works/10.1109/icra48891.2023.10160969) Visual Language Maps for Robot Navigation | ✓ | 오→✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0029](https://www.roboticsproceedings.org/rss19/p074.html) CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0030](https://www.roboticsproceedings.org/rss19/p066.html) ConceptFusion: Open-set Multimodal 3D Mapping | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ |
| [pr-0031](https://openaccess.thecvf.com/content/ICCV2023/html/Kerr_LERF_Language_Embedded_Radiance_Fields_ICCV_2023_paper.html) LERF: Language Embedded Radiance Fields | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0032](https://openaccess.thecvf.com/content/CVPR2023/html/Peng_OpenScene_3D_Scene_Understanding_With_Open_Vocabularies_CVPR_2023_paper.html) OpenScene: 3D Scene Understanding with Open Vocabularies | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0033](https://proceedings.neurips.cc/paper_files/paper/2023/hash/d77b5482e38339a8068791d939126be2-Abstract-Conference.html) OpenMask3D: Open-Vocabulary 3D Instance Segmentation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0034](https://proceedings.neurips.cc/paper_files/paper/2023/hash/413885e70482b95dcbeeddc1daf39177-Abstract-Conference.html) 3D-LLM: Injecting the 3D World into Large Language Models | ? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0035](https://arxiv.org/abs/2308.04352) 3D-VisTA: Pre-trained Transformer for 3D Vision and Text Alignment | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0036](https://proceedings.mlr.press/v205/shridhar23a.html) Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation | ✓ | ✓ | 보→✓ | 오→✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0037](https://proceedings.mlr.press/v229/goyal23a.html) RVT: Robotic View Transformer for 3D Object Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| [pr-0038](https://proceedings.mlr.press/v229/huang23b.html) VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0039](https://arxiv.org/abs/2209.07753) Code as Policies: Language Model Programs for Embodied Control | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0040](https://proceedings.mlr.press/v202/jiang23b.html) VIMA: Robot Manipulation with Multimodal Prompts | 보→✓ | 오→✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ✓ | ✓ | ? |
| [pr-0041](https://api.crossref.org/works/10.1109/lra.2022.3180108) CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks | 보→? | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | 보→✓ | 보→✓ | 보→✓ | ✓ |
| [pr-0042](https://proceedings.neurips.cc/paper_files/paper/2023/hash/8c3c666820ea055a77726d66fc7d447f-Abstract-Datasets_and_Benchmarks.html) LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ |
| [pr-0043](https://arxiv.org/abs/2203.17270) BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | 오→✓ |
| [pr-0044](https://arxiv.org/abs/2205.13542) BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0045](https://openaccess.thecvf.com/content/CVPR2023/html/Hu_Planning-Oriented_Autonomous_Driving_CVPR_2023_paper.html) Planning-oriented Autonomous Driving | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0046](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_DUSt3R_Geometric_3D_Vision_Made_Easy_CVPR_2024_paper.html) DUSt3R: Geometric 3D Vision Made Easy | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0047](https://arxiv.org/abs/2406.09756) Grounding Image Matching in 3D with MASt3R | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0048](https://arxiv.org/abs/2401.12168) SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0049](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_LL3DA_Visual_Interactive_Instruction_Tuning_for_Omni-3D_Understanding_Reasoning_and_CVPR_2024_paper.html) LL3DA: Visual Interactive Instruction Tuning for Omni-3D Understanding, Reasoning, and Planning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | 보→✓ | ? | ? |
| [pr-0050](https://proceedings.mlr.press/v235/huang24ae.html) An Embodied Generalist Agent in 3D World | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | 보→✓ | ? |
| [pr-0051](https://proceedings.mlr.press/v270/kim25c.html) OpenVLA: An Open-Source Vision-Language-Action Model | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ |
| [pr-0052](https://www.roboticsproceedings.org/rss20/p090.html) Octo: An Open-Source Generalist Robot Policy | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ |
| [pr-0053](https://proceedings.mlr.press/v270/xu25c.html) VLM-Grounder: A VLM Agent for Zero-Shot 3D Visual Grounding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ✓ |
| [pr-0054](https://proceedings.mlr.press/v270/huang25g.html) ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0055](https://proceedings.mlr.press/v270/liu25i.html) VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | 보→✓ | ? |
| [pr-0056](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html) VGGT: Visual Geometry Grounded Transformer | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | 보→✓ | ? | ? |
| [pr-0057](https://arxiv.org/abs/2501.12387) Continuous 3D Perception Model with Persistent State | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0058](https://proceedings.mlr.press/v305/li25g.html) 3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation | ? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0059](https://proceedings.mlr.press/v305/fan25a.html) Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0060](https://proceedings.mlr.press/v305/wu25c.html) MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0061](https://proceedings.mlr.press/v305/black25a.html) π0.5: a Vision-Language-Action Model with Open-World Generalization | ? | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0062](https://proceedings.mlr.press/v305/deng25a.html) GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0063](https://proceedings.mlr.press/v305/munje25a.html) SocialNav-SUB: Benchmarking VLMs for Scene Understanding in Social Robot Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0064](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_GenSplat_Bridging_the_Generalization_Gap_in_3DGS_Language_Comprehension_CVPR_2026_paper.html) GenSplat: Bridging the Generalization Gap in 3DGS Language Comprehension | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0065](https://openaccess.thecvf.com/content/CVPR2026/html/Meng_ST4R-Splat_Spatio-Temporal_Referring_Segmentation_in_4D_Gaussian_Splatting_CVPR_2026_paper.html) ST4R-Splat: Spatio-Temporal Referring Segmentation in 4D Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0066](https://proceedings.iclr.cc/paper_files/paper/2025/hash/3bfee3bc6639c36e6e7b058db909f760-Abstract-Conference.html) HAMSTER: Hierarchical Action Models for Open-World Robot Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0067](https://proceedings.iclr.cc/paper_files/paper/2025/hash/fce176458ff542940fa3ed16e6f9c852-Abstract-Conference.html) GravMAD: Grounded Spatial Value Maps Guided Action Diffusion for Generalized 3D Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0068](https://proceedings.iclr.cc/paper_files/paper/2025/hash/eb261df4322a8bd0a73093c4d8a0d02d-Abstract-Conference.html) ImagineNav: Prompting Vision-Language Models as Embodied Navigator through Scene Imagination | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0069](https://proceedings.iclr.cc/paper_files/paper/2025/hash/804a1a9de5787e3597b4bb64e1a48ec3-Abstract-Conference.html) VLAS: Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0070](https://proceedings.iclr.cc/paper_files/paper/2025/hash/98ed250b203d1ac6b24bbcf263e3d4a7-Abstract-Conference.html) 3D Vision-Language Gaussian Splatting | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0071](https://proceedings.iclr.cc/paper_files/paper/2025/hash/70a06501001e1820fd1eb9ee821302d2-Abstract-Conference.html) AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0072](https://proceedings.iclr.cc/paper_files/paper/2025/hash/909f526db5127f8bd8158af32d9e313a-Abstract-Conference.html) LLaRA: Supercharging Robot Learning Data for Vision-Language Policy | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0073](https://proceedings.iclr.cc/paper_files/paper/2025/hash/421fcf51a0e243f15f977553a6f482cb-Abstract-Conference.html) SPA: 3D Spatial-Awareness Enables Effective Embodied Representation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0074](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d274ea8b3c7f526f79ac9ce75ee3c8df-Abstract-Conference.html) DenseGrounding: Improving Dense Language-Vision Semantics for Ego-centric 3D Visual Grounding | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0075](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8667f264f88c7938a73a53ab01eb1327-Abstract-Conference.html) TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0076](https://proceedings.iclr.cc/paper_files/paper/2025/hash/7ba6b5b03ae07151a9a353b51f943290-Abstract-Conference.html) DenseMatcher: Learning 3D Semantic Correspondence for Category-Level Manipulation from a Single Demo | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0077](https://proceedings.iclr.cc/paper_files/paper/2025/hash/639f9db06bf70c4ff44cf22a7f92cb08-Abstract-Conference.html) 3D-SPATIAL MULTIMODAL MEMORY | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0078](https://proceedings.iclr.cc/paper_files/paper/2025/hash/2c8047bf3ed8ef6905351608d641f02f-Abstract-Conference.html) Articulate-Anything:  Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0079](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b364c8cbb3f229f40d5873e877391bd2-Abstract-Conference.html) 3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary Affordance Detection in 3D Worlds | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0080](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d826f5aadb26db488b8686097ceea2d1-Abstract-Conference.html) UniGS: Unified Language-Image-3D Pretraining with Gaussian Splatting | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0081](https://proceedings.iclr.cc/paper_files/paper/2025/hash/561dd71d04695c85e1c0f6a0fbe0bd85-Abstract-Conference.html) Learning Geometric Reasoning Networks For Robot Task And Motion Planning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0082](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a3cf318fbeec1126da21e9185ae9908c-Abstract-Conference.html) PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0083](https://proceedings.iclr.cc/paper_files/paper/2025/hash/49f80e4d2471ad4f2edf4f5f1ab62339-Abstract-Conference.html) RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0084](https://proceedings.iclr.cc/paper_files/paper/2025/hash/969a11f489c59c50c2cfe8c407c68a9b-Abstract-Conference.html) ET-SEED: EFFICIENT TRAJECTORY-LEVEL SE(3) EQUIVARIANT DIFFUSION POLICY | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0085](https://proceedings.iclr.cc/paper_files/paper/2026/hash/1fa3d6ccbcd15f7285fee666b2bd57be-Abstract-Conference.html) MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0086](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3cbe9fcdccb2399bcd6e6d01cbcae1fd-Abstract-Conference.html) From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0087](https://proceedings.iclr.cc/paper_files/paper/2026/hash/fb1b83b35e96998ddfc0ce1dab635445-Abstract-Conference.html) Seeing Across Views: Benchmarking Spatial Reasoning of Vision-Language Models in Robotic Scenes | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0088](https://proceedings.iclr.cc/paper_files/paper/2026/hash/37294f033582ac0064bf90fa557c2573-Abstract-Conference.html) Spatially Guided Training for Vision-Language-Action Model | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0089](https://proceedings.iclr.cc/paper_files/paper/2026/hash/f81332c0e757b169c66d436ec2fff624-Abstract-Conference.html) Vision-Language-Action Instruction Tuning: From Understanding to Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0090](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d2eedb7ecf14b50967c5de98e30e0ffc-Abstract-Conference.html) From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0091](https://proceedings.iclr.cc/paper_files/paper/2026/hash/b81d83165e3145a2e7d33bb5e33ea913-Abstract-Conference.html) RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0092](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7b122d0a0dcb1a86ffa25ccba154652b-Abstract-Conference.html) OmniEVA: Embodied Versatile Planner via Task-Adaptive 3D-Grounded and Embodiment-aware Reasoning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0093](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6bb891f36b1e5aa28f72f00a7c78bb94-Abstract-Conference.html) Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0094](https://proceedings.iclr.cc/paper_files/paper/2026/hash/2e9f9cde1b709281a06dd14f679e4c51-Abstract-Conference.html) AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0095](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0f7ad318868d228b980b13cf827e85f4-Abstract-Conference.html) Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0096](https://proceedings.iclr.cc/paper_files/paper/2026/hash/9baf31febefde7bd76023c2d2f13cbd7-Abstract-Conference.html) MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0097](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d676c05a8fb93ad9231508d95567c498-Abstract-Conference.html) Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0098](https://proceedings.iclr.cc/paper_files/paper/2026/hash/82ad13ec01f9fe44c01cb91814fd7b8c-Abstract-Conference.html) HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0099](https://proceedings.iclr.cc/paper_files/paper/2026/hash/444876e32cba0408c63f5295481cfe20-Abstract-Conference.html) Interleave-VLA: Enhancing Robot Manipulation with Image-Text Interleaved Instructions | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0100](https://proceedings.iclr.cc/paper_files/paper/2026/hash/2aa3da3c1463ee2cdaaee94be4f8ba3f-Abstract-Conference.html) RobotArena $\infty$: Scalable Robot Benchmarking via Real-to-Sim Translation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |

<a id="batch-02"></a>

### 배치 02

| ID · 공식 표제 | 링크 | 제목 | 저자 | 연도 | 발표처·게재 | 요약·기여 | 코드 | 가중치 | 데이터 | 태그 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [pr-0101](https://proceedings.iclr.cc/paper_files/paper/2026/hash/e705c234619bd9db3548421e94516fea-Abstract-Conference.html) Sim2Real VLA: Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0102](https://proceedings.iclr.cc/paper_files/paper/2026/hash/314129fede356d33eb7719d9edb01cc7-Abstract-Conference.html) Generalizable Coarse-to-Fine Robot Manipulation via Language-Aligned 3D Keypoints | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0103](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3812c3c803e986eca64000fe92467991-Abstract-Conference.html) JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0104](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cd830afc6208a346e4ec5caf1b08b4b4-Abstract-Conference.html) Uncertainty-Aware Gaussian Map for Vision-Language Navigation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0105](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0dadf17389895a1d660a178d1140e07c-Abstract-Conference.html) EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0106](https://proceedings.iclr.cc/paper_files/paper/2026/hash/274d0146144643ee2459a602123c60ff-Abstract-Conference.html) Towards Physically Executable 3D Gaussian for Embodied Navigation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0107](https://proceedings.iclr.cc/paper_files/paper/2026/hash/fef126561bbf9d4467dbb8d27334b8fe-Abstract-Conference.html) GPT4Scene: Understand 3D Scenes from Videos with Vision-Language Models | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0108](https://neurips.cc/virtual/2025/poster/116823) BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0109](https://neurips.cc/virtual/2025/oral/130277) Dynam3D: Dynamic Layered 3D Tokens Empower VLM for Vision-and-Language Navigation | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0110](https://neurips.cc/virtual/2025/poster/118219) VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0111](https://neurips.cc/virtual/2025/poster/118306) RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0112](https://neurips.cc/virtual/2025/poster/118204) Scaffolding Dexterous Manipulation with Vision-Language Models | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0113](https://neurips.cc/virtual/2025/poster/119747) ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0114](https://neurips.cc/virtual/2025/poster/115816) DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robotic Manipulation | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0115](https://papers.neurips.cc/paper_files/paper/2025/hash/4a81c1aad3064fb8243b8938a49ecca0-Abstract-Conference.html) SimWorld-Robotics: Synthesizing Photorealistic and Dynamic Urban Environments for Multimodal Robot Navigation and Collaboration | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0116](https://neurips.cc/static/virtual/data/neurips-2025-orals-posters.json) Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0117](https://neurips.cc/virtual/2025/poster/117079) Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0118](https://neurips.cc/virtual/2025/poster/118121) VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0119](https://neurips.cc/virtual/2025/poster/115166) 4D-VLA:  Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0120](https://neurips.cc/virtual/2025/poster/119733) BeliefMapNav: 3D Voxel-Based Belief Map for Zero-Shot Object Navigation | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0121](https://neurips.cc/virtual/2025/poster/118226) DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0122](https://neurips.cc/virtual/2025/poster/115408) OWMM-Agent: Open World Mobile Manipulation With Multi-modal Agentic Data Synthesis | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0123](https://neurips.cc/virtual/2025/poster/116975) SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0124](https://neurips.cc/virtual/2025/poster/116350) SoFar: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0125](https://neurips.cc/virtual/2025/poster/116120) NavBench: Probing Multimodal Large Language Models for Embodied Navigation | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0126](https://neurips.cc/virtual/2025/poster/119081) ViSPLA: Visual Iterative Self-Prompting for Language-Guided 3D Affordance Learning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0127](https://neurips.cc/virtual/2025/poster/120199) ChatVLA-2: Vision-Language-Action Model with Open-World Reasoning | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0128](https://neurips.cc/virtual/2025/poster/120169) ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0129](https://neurips.cc/virtual/2025/poster/117952) Spatial Understanding from Videos: Structured Prompts Meet Simulation Data | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0130](https://neurips.cc/virtual/2025/poster/116373) 3D Equivariant Visuomotor Policy Learning via Spherical Projection | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0131](https://neurips.cc/virtual/2025/poster/115127) Segment then Splat: Unified 3D Open-Vocabulary Segmentation via Gaussian Splatting | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0132](https://proceedings.mlr.press/v267/zhang25dr.html) ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0133](https://proceedings.mlr.press/v267/zhang25w.html) UP-VLA:  A Unified Understanding and Prediction Model for Embodied Agent | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0134](https://proceedings.mlr.press/v267/wen25g.html) DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0135](https://proceedings.mlr.press/v267/huang25u.html) OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0136](https://proceedings.mlr.press/v267/kim25ad.html) Test-Time Adaptation for Online Vision-Language Navigation with Feedback-based Reinforcement Learning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0137](https://proceedings.mlr.press/v267/zhu25u.html) SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0138](https://proceedings.mlr.press/v267/jain25b.html) Unifying 2D and 3D Vision-Language Understanding | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0139](https://proceedings.mlr.press/v267/cao25a.html) From Thousands to Billions: 3D Visual Language Grounding via Render-Supervised Distillation from 2D VLMs | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0140](https://proceedings.mlr.press/v267/he25h.html) ReferSplat: Referring Segmentation in 3D Gaussian Splatting | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0141](https://proceedings.mlr.press/v267/yang25f.html) EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0142](https://proceedings.mlr.press/v267/shi25d.html) Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0143](https://proceedings.mlr.press/v267/fang25c.html) SAM2Act: Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0144](https://proceedings.mlr.press/v267/hu25h.html) VTGaussian-SLAM: RGBD SLAM for Large Scale Scenes with Splatting View-Tied 3D Gaussians | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0145](https://proceedings.mlr.press/v267/wang25ef.html) 3D Question Answering via only 2D Vision-Language Models | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ✓ |
| [pr-0146](https://proceedings.mlr.press/v267/li25by.html) VIP: Vision Instructed Pre-training for Robotic Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0147](https://proceedings.mlr.press/v267/mcvay25a.html) LOCATE 3D: Real-World Object Localization via Self-Supervised Learning in 3D | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0148](https://proceedings.mlr.press/v267/pan25c.html) How Do Images Align and Complement LiDAR? Towards a Harmonized Multi-modal 3D Panoptic Segmentation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0149](https://icml.cc/virtual/2026/poster/61610) Joint Navigation and Manipulation Planning with 3D Interaction Chains | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0150](https://proceedings.mlr.press/v306/sun26an.html) AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0151](https://icml.cc/virtual/2026/poster/65809) TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0152](https://icml.cc/virtual/2026/poster/62902) Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0153](https://icml.cc/virtual/2026/poster/60897) HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0154](https://icml.cc/virtual/2026/poster/61922) HALO: A Unified Vision-Language-Action Model for Embodied Multimodal Chain-of-Thought Reasoning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0155](https://icml.cc/virtual/2026/poster/61887) LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0156](https://icml.cc/virtual/2026/poster/66214) Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0157](https://icml.cc/virtual/2026/poster/60801) LAGEA: Language Guided Embodied Agents for Robotic Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0158](https://icml.cc/virtual/2026/poster/62192) RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0159](https://icml.cc/virtual/2026/poster/62528) Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0160](https://icml.cc/virtual/2026/poster/64290) Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0161](https://icml.cc/virtual/2026/poster/62900) Reasoning-VLA: An Efficient and Spatial-Guided General Vision-Language-Action Reasoning Model for Autonomous Driving | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0162](https://icml.cc/virtual/2026/oral/71118) XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0163](https://icml.cc/virtual/2026/poster/63554) Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0164](https://icml.cc/virtual/2026/poster/62543) RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0165](https://icml.cc/virtual/2026/poster/61401) RoboOmni: Actions Are Just Another Modality for Vision-Language Models | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0166](https://icml.cc/virtual/2026/poster/63548) SpikeVLA: Vision-Language-Action Models with Spiking Neural Networks | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0167](https://icml.cc/virtual/2026/poster/64902) MapDream: Task-Driven Map Learning for Vision-Language Navigation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0168](https://icml.cc/virtual/2026/poster/60472) Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0169](https://icml.cc/virtual/2026/oral/71166) SpatioLM: Towards General Physical Spatial Intelligence in Vision-Language Models | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0170](https://api.crossref.org/works/10.1109/icra55743.2025.11127306) MiniVLN: Efficient Vision-And-Language Navigation by Progressive Knowledge Distillation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0171](https://api.crossref.org/works/10.1109/icra55743.2025.11128264) VLM-GroNav: Robot Navigation Using Physically Grounded Vision-Language Models in Outdoor Environments | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0172](https://api.crossref.org/works/10.1109/icra55743.2025.11127464) IRef-VLA: A Benchmark for Interactive Referential Grounding with Imperfect Language in 3D Scenes | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0173](https://api.crossref.org/works/10.1109/icra55743.2025.11128782) Graph2Nav: 3D Object-Relation Graph Generation to Robot Navigation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0174](https://api.crossref.org/works/10.1109/icra55743.2025.11127471) Point2Graph: An End-To-End Point Cloud-Based 3D Open-Vocabulary Scene Graph for Robot Navigation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0175](https://api.crossref.org/works/10.1109/icra55743.2025.11128304) LE-Object: Language Embedded Object-Level Neural Radiance Fields for Open-Vocabulary Scene | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0176](https://api.crossref.org/works/10.1109/icra55743.2025.11128002) Gaussian Splatting Visual MPC for Granular Media Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0177](https://api.crossref.org/works/10.1109/icra55743.2025.11127328) Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0178](https://api.crossref.org/works/10.1109/icra55743.2025.11128336) VITaL Pretraining: Visuo-Tactile Pretraining for Tactile and Non-Tactile Manipulation Policies | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0179](https://api.crossref.org/works/10.1109/icra55743.2025.11127699) Context Graph-based Visual-Language Place Recognition | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0180](https://api.crossref.org/works/10.1109/icra57385.2026.11697407) RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0181](https://api.crossref.org/works/10.1109/icra57385.2026.11697481) Audio-VLA: Adding Contact Audio Perception to Vision-Language-Action Model for Robotic Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0182](https://api.crossref.org/works/10.1109/icra57385.2026.11697462) DAM-VLA: A Dynamic Action Model-Based Vision-Language-Action Framework for Robot Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0183](https://api.crossref.org/works/10.1109/icra57385.2026.11697046) MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0184](https://api.crossref.org/works/10.1109/icra57385.2026.11697164) FP3: A 3D Foundation Policy for Robotic Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0185](https://api.crossref.org/works/10.1109/icra57385.2026.11695889) FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0186](https://api.crossref.org/works/10.1109/ICRA57385.2026.11697552) Scalable Vision-Language-Action Model Pretraining for Robotic Manipulation with Real-Life Human Activity Videos | 보→✓ | 오→✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0187](https://arxiv.org/abs/2507.00886) GaussianVLM: Scene-Centric 3D Vision-Language Models Using Language-Aligned Gaussian Splats for Embodied Reasoning and Beyond | 보→✓ | ✓ | 보→✓ | 오→✓ | 오→✓ | 보→✓ | ? | ? | 보→✓ | ? |
| [pr-0188](https://api.crossref.org/works/10.1109/icra57385.2026.11695776) OmniVLA: Physically-Grounded Multimodal VLA with Unified Multi-Sensor Perception for Robotic Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0189](https://api.crossref.org/works/10.1109/icra57385.2026.11697566) OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0190](https://api.crossref.org/works/10.1109/icra57385.2026.11696905) EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0191](https://api.crossref.org/works/10.1109/icra57385.2026.11696861) LaViRA: Language-Vision-Robot Actions Translation for Zero-Shot Vision Language Navigation in Continuous Environments | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0192](https://api.crossref.org/works/10.1109/icra57385.2026.11696379) Goal-VLA: Image-Generative VLMs As Object-Centric World Models Empowering Zero-Shot Robot Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0193](https://api.crossref.org/works/10.1109/icra57385.2026.11695971) VLA-Reasoner: Empowering Vision-Language-Action Models with Reasoning Via Online Monte Carlo Tree Search | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0194](https://arxiv.org/abs/2507.01125) VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online Semantic Gaussian Splatting | 보→✓ | ✓ | 보→✓ | ✓ | 오→✓ | ? | ? | ? | ? | ✓ |
| [pr-0195](https://api.crossref.org/works/10.1109/icra57385.2026.11695811) Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0196](https://api.crossref.org/works/10.1109/icra57385.2026.11697173) Semantically Consistent Language Gaussian Splatting for 3D Point-Level Open-Vocabulary Querying | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0197](https://api.crossref.org/works/10.1109/icra57385.2026.11697135) SINGER: An Onboard Generalist Vision-Language Navigation Policy for Drones | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0198](https://api.crossref.org/works/10.1109/icra57385.2026.11696642) TagaVLM: Topology-Aware Global Action Reasoning for Vision-Language Navigation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0199](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/808_ECCV_2024_paper.php) QUAR-VLA: Vision-Language-Action Model for Quadruped Robots | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0200](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1407_ECCV_2024_paper.php) SceneVerse: Scaling 3D Vision-Language Learning for Grounded Scene Understanding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |

<a id="batch-03"></a>

### 배치 03

| ID · 공식 표제 | 링크 | 제목 | 저자 | 연도 | 발표처·게재 | 요약·기여 | 코드 | 가중치 | 데이터 | 태그 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [pr-0201](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3330_ECCV_2024_paper.php) Uni3DL: A Unified Model for 3D Vision-Language Understanding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0202](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6043_ECCV_2024_paper.php) Unifying 3D Vision-Language Understanding via Promptable Queries | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0203](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5642_ECCV_2024_paper.php) 3D Open-Vocabulary Panoptic Segmentation with 2D-3D Vision-Language Distillation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0204](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9223_ECCV_2024_paper.php) 3D Weakly Supervised Semantic Segmentation with 2D Vision-Language Guidance | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0205](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6612_ECCV_2024_paper.php) Dense Multimodal Alignment for Open-Vocabulary 3D Scene Understanding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0206](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4252_ECCV_2024_paper.php) Open-Vocabulary 3D Semantic Segmentation with Text-to-Image Diffusion Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0207](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5197_ECCV_2024_paper.php) Global-Local Collaborative Inference with LLM for Lidar-Based Open-Vocabulary Detection | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0208](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5194_ECCV_2024_paper.php) ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ |
| [pr-0209](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1143_ECCV_2024_paper.php) NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | 보→✓ | ? | ✓ |
| [pr-0210](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1255_ECCV_2024_paper.php) SceneGraphLoc: Cross-Modal Coarse Visual Localization on 3D Scene Graphs | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0211](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3785_ECCV_2024_paper.php) Heterogeneous Graph Learning for Scene Graph Prediction in 3D Point Clouds | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0212](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7914_ECCV_2024_paper.php) OpenIns3D: Snap and Lookup for 3D Open-vocabulary Instance Segmentation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0213](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4516_ECCV_2024_paper.php) SGS-SLAM: Semantic Gaussian Splatting For Neural Dense SLAM | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0214](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7983_ECCV_2024_paper.php) TCLC-GS: Tightly Coupled LiDAR-Camera Gaussian Splatting for Autonomous Driving | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0215](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3958_ECCV_2024_paper.php) GaussianFormer: Scene as Gaussians for Vision-Based 3D Semantic Occupancy Prediction | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0216](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/996_ECCV_2024_paper.php) DreamScene360: Unconstrained Text-to-3D Scene Generation with Panoramic Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0217](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3146_ECCV_2024_paper.php) EchoScene: Indoor Scene Generation via Information Echo over Scene Graph Diffusion | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0218](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/12578_ECCV_2024_paper.php) BlenderAlchemy: Editing 3D Graphics with Vision-Language Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0219](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/11636_ECCV_2024_paper.php) Exploiting Semantic Reconstruction to Mitigate Hallucinations in Vision-Language Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0220](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Egocentric_Action-aware_Inertial_Localization_in_Point_Clouds_with_Vision-Language_Guidance_ICCV_2025_paper.html) Egocentric Action-aware Inertial Localization in Point Clouds with Vision-Language Guidance | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0221](https://openaccess.thecvf.com/content/ICCV2025/html/Jang_Identity-aware_Language_Gaussian_Splatting_for_Open-vocabulary_3D_Semantic_Segmentation_ICCV_2025_paper.html) Identity-aware Language Gaussian Splatting for Open-vocabulary 3D Semantic Segmentation | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0222](https://openaccess.thecvf.com/content/ICCV2025/html/Cai_Baking_Gaussian_Splatting_into_Diffusion_Denoiser_for_Fast_and_Scalable_ICCV_2025_paper.html) Baking Gaussian Splatting into Diffusion Denoiser for Fast and Scalable Single-stage Image-to-3D Generation and Reconstruction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0223](https://openaccess.thecvf.com/content/ICCV2025/html/Chow_OV-SCAN_Semantically_Consistent_Alignment_for_Novel_Object_Discovery_in_Open-Vocabulary_ICCV_2025_paper.html) OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0224](https://openaccess.thecvf.com/content/ICCV2025/html/Tian_CCL-LGS_Contrastive_Codebook_Learning_for_3D_Language_Gaussian_Splatting_ICCV_2025_paper.html) CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0225](https://openaccess.thecvf.com/content/ICCV2025/html/Jiao_CLIP-GS_Unifying_Vision-Language_Representation_with_3D_Gaussian_Splatting_ICCV_2025_paper.html) CLIP-GS: Unifying Vision-Language Representation with 3D Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0226](https://openaccess.thecvf.com/content/ICCV2025/html/Petit_DiSCO-3D__Discovering_and_Segmenting_Sub-Concepts_from_Open-vocabulary_Queries_in_ICCV_2025_paper.html) DiSCO-3D : Discovering and Segmenting Sub-Concepts from Open-vocabulary Queries in NeRF | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0227](https://openaccess.thecvf.com/content/ICCV2025/html/Wu_EmbodiedOcc_Embodied_3D_Occupancy_Prediction_for_Vision-based_Online_Scene_Understanding_ICCV_2025_paper.html) EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ✓ |
| [pr-0228](https://openaccess.thecvf.com/content/ICCV2025/html/Miao_FedVLA_Federated_Vision-Language-Action_Learning_with_Dual_Gating_Mixture-of-Experts_for_Robotic_ICCV_2025_paper.html) FedVLA: Federated Vision-Language-Action Learning with Dual Gating Mixture-of-Experts for Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0229](https://openaccess.thecvf.com/content/ICCV2025/html/Lin_GroundFlow_A_Plug-in_Module_for_Temporal_Reasoning_on_3D_Point_ICCV_2025_paper.html) GroundFlow: A Plug-in Module for Temporal Reasoning on 3D Point Cloud Sequential Grounding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0230](https://openaccess.thecvf.com/content/ICCV2025/html/Guo_IGL-Nav_Incremental_3D_Gaussian_Localization_for_Image-goal_Navigation_ICCV_2025_paper.html) IGL-Nav: Incremental 3D Gaussian Localization for Image-goal Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0231](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_LangScene-X_Reconstruct_Generalizable_3D_Language-Embedded_Scenes_with_TriMap_Video_Diffusion_ICCV_2025_paper.html) LangScene-X: Reconstruct Generalizable 3D Language-Embedded Scenes with TriMap Video Diffusion | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0232](https://openaccess.thecvf.com/content/ICCV2025/html/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.html) ORION: A Holistic End-to-End Autonomous Driving Framework by Vision-Language Instructed Action Generation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0233](https://openaccess.thecvf.com/content/ICCV2025/html/Zhao_PhysSplat_Efficient_Physics_Simulation_for_3D_Scenes_via_MLLM-Guided_Gaussian_ICCV_2025_paper.html) PhysSplat: Efficient Physics Simulation for 3D Scenes via MLLM-Guided Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0234](https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html) CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0235](https://openaccess.thecvf.com/content/ICCV2025/html/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.html) Details Matter for Indoor Open-vocabulary 3D Instance Segmentation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0236](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Exploiting_Vision_Language_Model_for_Training-Free_3D_Point_Cloud_OOD_ICCV_2025_paper.html) Exploiting Vision Language Model for Training-Free 3D Point Cloud OOD Detection via Graph Score Propagation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0237](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.html) Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0238](https://openaccess.thecvf.com/content/ICCV2025/html/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.html) GeoProg3D: Compositional Visual Reasoning for City-Scale 3D Language Fields | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0239](https://openaccess.thecvf.com/content/ICCV2025/html/Ahmed_Kestrel_3D_Multimodal_LLM_for_Part-Aware_Grounded_Description_ICCV_2025_paper.html) Kestrel: 3D Multimodal LLM for Part-Aware Grounded Description | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0240](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.html) LIRA: Reasoning Reconstruction via Multimodal Large Language Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | 보→✓ | 보→✓ | ? |
| [pr-0241](https://openaccess.thecvf.com/content/ICCV2025/html/Daxberger_MM-Spatial_Exploring_3D_Spatial_Understanding_in_Multimodal_LLMs_ICCV_2025_paper.html) MM-Spatial: Exploring 3D Spatial Understanding in Multimodal LLMs | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0242](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Moto_Latent_Motion_Token_as_the_Bridging_Language_for_Learning_ICCV_2025_paper.html) Moto: Latent Motion Token as the Bridging Language for Learning Robot Manipulation from Videos | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0243](https://openaccess.thecvf.com/content/ICCV2025/html/Su_OVA-Fields_Weakly_Supervised_Open-Vocabulary_Affordance_Fields_for_Robot_Operational_Part_ICCV_2025_paper.html) OVA-Fields: Weakly Supervised Open-Vocabulary Affordance Fields for Robot Operational Part Detection | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0244](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.html) Open-Vocabulary Octree-Graph for 3D Scene Understanding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0245](https://openaccess.thecvf.com/content/ICCV2025/html/Li_Towards_Long-Horizon_Vision-Language-Action_System_Reasoning_Acting_and_Memory_ICCV_2025_paper.html) Towards Long-Horizon Vision-Language-Action System: Reasoning, Acting and Memory | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0246](https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_VGMamba_Attribute-to-Location_Clue_Reasoning_for_Quantity-Agnostic_3D_Visual_Grounding_ICCV_2025_paper.html) VGMamba: Attribute-to-Location Clue Reasoning for Quantity-Agnostic 3D Visual Grounding | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0247](https://openaccess.thecvf.com/content/ICCV2025/html/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.html) VLR-Driver: Large Vision-Language-Reasoning Models for Embodied Autonomous Driving | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0248](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.html) VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0249](https://openaccess.thecvf.com/content/ICCV2025/html/Huang_ViewSRD_3D_Visual_Grounding_via_Structured_Multi-View_Decomposition_ICCV_2025_paper.html) ViewSRD: 3D Visual Grounding via Structured Multi-View Decomposition | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0250](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Mamba-3VL_Taming_State_Space_Model_for_3D_Vision_Language_Learning_ICCV_2025_paper.html) Mamba-3VL: Taming State Space Model for 3D Vision Language Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0251](https://openaccess.thecvf.com/content/ICCV2025/html/Fang_MeshLLM_Empowering_Large_Language_Models_to_Progressively_Understand_and_Generate_ICCV_2025_paper.html) MeshLLM: Empowering Large Language Models to Progressively Understand and Generate 3D Mesh | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0252](https://openaccess.thecvf.com/content/ICCV2025/html/Wu_On-Device_Diffusion_Transformer_Policy_for_Efficient_Robot_Manipulation_ICCV_2025_paper.html) On-Device Diffusion Transformer Policy for Efficient Robot Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0253](https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_PASG_A_Closed-Loop_Framework_for_Automated_Geometric_Primitive_Extraction_and_ICCV_2025_paper.html) PASG: A Closed-Loop Framework for Automated Geometric Primitive Extraction and Semantic Anchoring in Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0254](https://openaccess.thecvf.com/content/ICCV2025/html/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.html) PlaceIt3D: Language-Guided Object Placement in Real 3D Scenes | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0255](https://openaccess.thecvf.com/content/ICCV2025/html/Deng_Boost_3D_Reconstruction_using_Diffusion-based_Monocular_Camera_Calibration_ICCV_2025_paper.html) Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0256](https://openaccess.thecvf.com/content/ICCV2025/html/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.html) FROSS: Faster-Than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0257](https://openaccess.thecvf.com/content/ICCV2025/html/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.html) Vision-Language Interactive Relation Mining for Open-Vocabulary Scene Graph Generation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0258](https://openaccess.thecvf.com/content/ICCV2025/html/Gong_ZeroKey_Point-Level_Reasoning_and_Zero-Shot_3D_Keypoint_Detection_from_Large_ICCV_2025_paper.html) ZeroKey: Point-Level Reasoning and Zero-Shot 3D Keypoint Detection from Large Language Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0259](https://arxiv.org/abs/2606.23686) LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | 보→✓ | ✓ |
| [pr-0260](https://arxiv.org/abs/2602.21445) VLA Knows Its Limits: Adaptive Execution Horizons for Robot Policies | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0261](https://arxiv.org/abs/2606.22540) PolicyTrim: Boosting Intrinsic Policy Efficiency of Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | 보→✓ | ? | ✓ |
| [pr-0262](https://api.crossref.org/works/10.1109/lra.2024.3432348) GaussianGrasper: 3D Language Gaussian Splatting for Open-vocabulary Robotic Grasping | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0263](https://arxiv.org/abs/2404.13696) Clio: Real-time Task-Driven Open-Set 3D Scene Graphs | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0264](https://api.crossref.org/works/10.1109/lra.2024.3355751) FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ✓ |
| [pr-0265](https://api.crossref.org/works/10.1109/lra.2024.3441495) Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0266](https://api.crossref.org/works/10.1109/lra.2024.3490402) S3E: A Multi-Robot Multimodal Dataset for Collaborative SLAM | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0267](https://api.crossref.org/works/10.1109/lra.2025.3534523) Search3D: Hierarchical Open-Vocabulary 3D Segmentation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0268](https://api.crossref.org/works/10.1109/LRA.2025.3544909) TinyVLA: Toward Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation | ✓ | 오→✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ✓ |
| [pr-0269](https://api.crossref.org/works/10.1109/lra.2025.3547643) Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0270](https://api.crossref.org/works/10.1109/lra.2025.3575235) HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0271](https://arxiv.org/abs/2412.17769) ActiveGS: Active Scene Reconstruction using Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ✓ |
| [pr-0272](https://api.crossref.org/works/10.1109/lra.2026.3653303) PointVLA: Injecting the 3D World into Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0273](https://lab-of-ai-and-robotics.github.io/LAMP/) LAMP: Implicit Language Map for Robot Navigation | ✓ | ✓ | 보→✓ | 오→✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0274](https://api.crossref.org/works/10.1109/lra.2026.3693992) CLARE: Continual Learning for Vision-Language-Action Models via Autonomous Adapter Routing and Expansion | 오→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0275](https://arxiv.org/abs/2602.11575) ReaDy-Go: Real-to-Sim Dynamic 3D Gaussian Splatting Simulation for Environment-Specific Visual Navigation with Moving Obstacles | 오→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0276](https://api.crossref.org/works/10.1109/lra.2026.3707356) Compact Object-Level Representations with Open-Vocabulary Understanding for Indoor Visual Relocalization | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0277](https://api.crossref.org/works/10.1109/iros60139.2025.11246682) VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | 보→✓ | ✓ |
| [pr-0278](https://api.crossref.org/works/10.1109/iros60139.2025.11247519) PD-VLA: Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0279](https://api.crossref.org/works/10.1109/iros60139.2025.11246684) WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0280](https://api.crossref.org/works/10.1109/iros60139.2025.11246368) Helpful DoggyBot: Open-World Object Fetching using Legged Robots and Vision-Language Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0281](https://api.crossref.org/works/10.1109/iros60139.2025.11247378) OpenGS-Fusion: Open-Vocabulary Dense Mapping with Hybrid 3D Gaussian Splatting for Refined Object-Level Understanding | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0282](https://arxiv.org/abs/2411.12185) LiV-GS: LiDAR-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments | ✓ | ✓ | 보→✓ | ✓ | 오→✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0283](https://arxiv.org/abs/2412.18381) MR-COGraphs: Communication-efficient Multi-Robot Open-vocabulary Mapping System via 3D Scene Graphs | ✓ | ✓ | 보→✓ | ✓ | 오→✓ | ? | ? | ? | ? | ? |
| [pr-0284](https://api.crossref.org/works/10.1109/tro.2025.3552348) Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ✓ |
| [pr-0285](https://api.crossref.org/works/10.1109/iros60139.2025.11247413) OpenObject-NAV: Open-Vocabulary Object-Oriented Navigation Based on Dynamic Carrier-Relationship Scene Graph | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0286](https://api.crossref.org/works/10.1109/iros60139.2025.11246145) SORT3D: Spatial Object-centric Reasoning Toolbox for Zero-Shot 3D Grounding Using Large Language Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0287](https://api.crossref.org/works/10.1109/iros60139.2025.11247555) FunGraph: Functionality Aware 3D Scene Graphs for Language-Prompted Scene Interaction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0288](https://api.crossref.org/works/10.1109/iros60139.2025.11245845) FOCI: Trajectory Optimization on Gaussian Splats | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0289](https://api.crossref.org/works/10.1109/iros60139.2025.11246997) GSplatVNM: Point-of-View Synthesis for Visual Navigation Models Using Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0290](https://api.crossref.org/works/10.1109/iros60139.2025.11247514) GRaD-Nav: Efficiently Learning Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ✓ |
| [pr-0291](https://2026.ieee-iros.org/program/paper-index/) LIT-GS: LiDAR-Inertial-Thermal 3D Gaussian Splatting for Illumination-Robust Mapping | ✓ | 오→✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0292](https://arxiv.org/abs/2606.19190) FAST-LIVGO: A Degeneracy-Robust LiDAR-Inertial-Visual-GNSS Fusion Odometry | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0293](https://arxiv.org/abs/2606.25497) SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0294](https://api.crossref.org/works/10.1145/3326362) Dynamic Graph CNN for Learning on Point Clouds | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0295](https://api.crossref.org/works/10.1109/iccv.2019.00651) KPConv: Flexible and Deformable Convolution for Point Clouds | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0296](https://arxiv.org/abs/1904.08755) 4D Spatio-Temporal ConvNets: Minkowski Convolutional Neural Networks | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0297](https://openaccess.thecvf.com/content/ICCV2021/html/Zhao_Point_Transformer_ICCV_2021_paper.html) Point Transformer | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0298](https://openaccess.thecvf.com/content/CVPR2021/html/Yin_Center-Based_3D_Object_Detection_and_Tracking_CVPR_2021_paper.html) Center-Based 3D Object Detection and Tracking | ✓ | 오→✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0299](https://openaccess.thecvf.com/content/CVPR2022/html/Yu_Point-BERT_Pre-Training_3D_Point_Cloud_Transformers_With_Masked_Point_Modeling_CVPR_2022_paper.html) Point-BERT: Pre-training 3D Point Cloud Transformers with Masked Point Modeling | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0300](https://arxiv.org/abs/2203.06604) Masked Autoencoders for Point Cloud Self-supervised Learning | ✓ | 오→✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |

<a id="batch-04"></a>

### 배치 04

| ID · 공식 표제 | 링크 | 제목 | 저자 | 연도 | 발표처·게재 | 요약·기여 | 코드 | 가중치 | 데이터 | 태그 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [pr-0301](https://arxiv.org/abs/1912.13192) PV-RCNN: Point-Voxel Feature Set Abstraction for 3D Object Detection | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0302](https://arxiv.org/abs/2203.05625) PETR: Position Embedding Transformation for Multi-View 3D Object Detection | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0303](https://arxiv.org/abs/2206.10092) BEVDepth: Acquisition of Reliable Depth for Multi-view 3D Object Detection | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0304](https://openaccess.thecvf.com/content/CVPR2023/html/Li_VoxFormer_Sparse_Voxel_Transformer_for_Camera-Based_3D_Semantic_Scene_Completion_CVPR_2023_paper.html) VoxFormer: Sparse Voxel Transformer for Camera-based 3D Semantic Scene Completion | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0305](https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Depth_Anything_Unleashing_the_Power_of_Large-Scale_Unlabeled_Data_CVPR_2024_paper.html) Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0306](https://openaccess.thecvf.com/content/CVPR2024/html/Ke_Repurposing_Diffusion-Based_Image_Generators_for_Monocular_Depth_Estimation_CVPR_2024_paper.html) Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation | ✓ | 오→✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0307](https://proceedings.neurips.cc/paper_files/paper/2024/hash/26cfdcd8fe6fd75cc53e92963a656c58-Abstract-Conference.html) Depth Anything V2 | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0308](https://openaccess.thecvf.com/content/CVPR2024/html/Piccinelli_UniDepth_Universal_Monocular_Metric_Depth_Estimation_CVPR_2024_paper.html) UniDepth: Universal Monocular Metric Depth Estimation | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0309](https://openaccess.thecvf.com/content/CVPR2024/html/Charatan_pixelSplat_3D_Gaussian_Splats_from_Image_Pairs_for_Scalable_Generalizable_CVPR_2024_paper.html) pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0310](https://openaccess.thecvf.com/content/CVPR2024/html/Guedon_SuGaR_Surface-Aligned_Gaussian_Splatting_for_Efficient_3D_Mesh_Reconstruction_and_CVPR_2024_paper.html) SuGaR: Surface-Aligned Gaussian Splatting for Efficient 3D Mesh Reconstruction and High-Quality Mesh Rendering | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0311](https://openaccess.thecvf.com/content/CVPR2024/html/Keetha_SplaTAM_Splat_Track__Map_3D_Gaussians_for_Dense_RGB-D_CVPR_2024_paper.html) SplaTAM: Splat Track & Map 3D Gaussians for Dense RGB-D SLAM | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0312](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_ReconFusion_3D_Reconstruction_with_Diffusion_Priors_CVPR_2024_paper.html) ReconFusion: 3D Reconstruction with Diffusion Priors | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0313](https://openaccess.thecvf.com/content/CVPR2024/html/Nunes_Scaling_Diffusion_Models_to_Real-World_3D_LiDAR_Scene_Completion_CVPR_2024_paper.html) Scaling Diffusion Models to Real-World 3D LiDAR Scene Completion | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | 오→✓ |
| [pr-0314](https://openaccess.thecvf.com/content/CVPR2024/html/Dutt_Diffusion_3D_Features_Diff3F_Decorating_Untextured_Shapes_with_Distilled_Semantic_CVPR_2024_paper.html) Diffusion 3D Features (Diff3F): Decorating Untextured Shapes with Distilled Semantic Features | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0315](https://openaccess.thecvf.com/content/CVPR2024/html/Xu_3DiffTection_3D_Object_Detection_with_Geometry-Aware_Diffusion_Features_CVPR_2024_paper.html) 3DiffTection: 3D Object Detection with Geometry-Aware Diffusion Features | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0316](https://openaccess.thecvf.com/content/CVPR2024/html/Xie_SG-PGM_Partial_Graph_Matching_Network_with_Semantic_Geometric_Fusion_for_CVPR_2024_paper.html) SG-PGM: Partial Graph Matching Network with Semantic Geometric Fusion for 3D Scene Graph Alignment and Its Downstream Tasks | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | 오→✓ |
| [pr-0317](https://openaccess.thecvf.com/content/CVPR2024/html/Cheng_HandDiff_3D_Hand_Pose_Estimation_with_Diffusion_on_Image-Point_Cloud_CVPR_2024_paper.html) HandDiff: 3D Hand Pose Estimation with Diffusion on Image-Point Cloud | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0318](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_IPoD_Implicit_Field_Learning_with_Point_Diffusion_for_Generalizable_3D_CVPR_2024_paper.html) IPoD: Implicit Field Learning with Point Diffusion for Generalizable 3D Object Reconstruction from Single RGB-D Images | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0319](https://openaccess.thecvf.com/content/CVPR2024/html/Zou_Triplane_Meets_Gaussian_Splatting_Fast_and_Generalizable_Single-View_3D_Reconstruction_CVPR_2024_paper.html) Triplane Meets Gaussian Splatting: Fast and Generalizable Single-View 3D Reconstruction with Transformers | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0320](https://openaccess.thecvf.com/content/CVPR2024/html/Lyu_Total-Decom_Decomposed_3D_Scene_Reconstruction_with_Minimal_Interaction_CVPR_2024_paper.html) Total-Decom: Decomposed 3D Scene Reconstruction with Minimal Interaction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0321](https://openaccess.thecvf.com/content/CVPR2024/html/Klinghoffer_PlatoNeRF_3D_Reconstruction_in_Platos_Cave_via_Single-View_Two-Bounce_Lidar_CVPR_2024_paper.html) PlatoNeRF: 3D Reconstruction in Plato's Cave via Single-View Two-Bounce Lidar | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | 오→✓ |
| [pr-0322](https://openaccess.thecvf.com/content/CVPR2024/html/Lu_3D_Geometry-Aware_Deformable_Gaussian_Splatting_for_Dynamic_View_Synthesis_CVPR_2024_paper.html) 3D Geometry-Aware Deformable Gaussian Splatting for Dynamic View Synthesis | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0323](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_MVIP-NeRF_Multi-view_3D_Inpainting_on_NeRF_Scenes_via_Diffusion_Prior_CVPR_2024_paper.html) MVIP-NeRF: Multi-view 3D Inpainting on NeRF Scenes via Diffusion Prior | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0324](https://openaccess.thecvf.com/content/CVPR2024/html/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.html) Bayesian Diffusion Models for 3D Shape Reconstruction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0325](https://openaccess.thecvf.com/content/CVPR2024/html/Schroppel_Neural_Point_Cloud_Diffusion_for_Disentangled_3D_Shape_and_Appearance_CVPR_2024_paper.html) Neural Point Cloud Diffusion for Disentangled 3D Shape and Appearance Generation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0326](https://openaccess.thecvf.com/content/CVPR2024/html/Ren_TIGER_Time-Varying_Denoising_Model_for_3D_Point_Cloud_Generation_with_CVPR_2024_paper.html) TIGER: Time-Varying Denoising Model for 3D Point Cloud Generation with Diffusion Process | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0327](https://openaccess.thecvf.com/content/CVPR2024/html/Yi_GaussianDreamer_Fast_Generation_from_Text_to_3D_Gaussians_by_Bridging_CVPR_2024_paper.html) GaussianDreamer: Fast Generation from Text to 3D Gaussians by Bridging 2D and 3D Diffusion Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0328](https://openaccess.thecvf.com/content/CVPR2024/html/Ling_Align_Your_Gaussians_Text-to-4D_with_Dynamic_3D_Gaussians_and_Composed_CVPR_2024_paper.html) Align Your Gaussians: Text-to-4D with Dynamic 3D Gaussians and Composed Diffusion Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0329](https://openaccess.thecvf.com/content/CVPR2025/html/Tang_SPARS3R_Semantic_Prior_Alignment_and_Regularization_for_Sparse_3D_Reconstruction_CVPR_2025_paper.html) SPARS3R: Semantic Prior Alignment and Regularization for Sparse 3D Reconstruction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0330](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_UniPre3D_Unified_Pre-training_of_3D_Point_Cloud_Models_with_Cross-Modal_CVPR_2025_paper.html) UniPre3D: Unified Pre-training of 3D Point Cloud Models with Cross-Modal Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ✓ |
| [pr-0331](https://openaccess.thecvf.com/content/CVPR2025/html/Tang_DroneSplat_3D_Gaussian_Splatting_for_Robust_3D_Reconstruction_from_In-the-Wild_CVPR_2025_paper.html) DroneSplat: 3D Gaussian Splatting for Robust 3D Reconstruction from In-the-Wild Drone Imagery | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0332](https://openaccess.thecvf.com/content/CVPR2025/html/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.html) SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0333](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Rethinking_Temporal_Fusion_with_a_Unified_Gradient_Descent_View_for_CVPR_2025_paper.html) Rethinking Temporal Fusion with a Unified Gradient Descent View for 3D Semantic Occupancy Prediction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | 오→✓ |
| [pr-0334](https://openaccess.thecvf.com/content/CVPR2025/html/Huang_V2X-R_Cooperative_LiDAR-4D_Radar_Fusion_with_Denoising_Diffusion_for_3D_CVPR_2025_paper.html) V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0335](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Touch2Shape_Touch-Conditioned_3D_Diffusion_for_Shape_Exploration_and_Reconstruction_CVPR_2025_paper.html) Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0336](https://openaccess.thecvf.com/content/CVPR2025/html/Li_CraftsMan3D_High-fidelity_Mesh_Generation_with_3D_Native_Diffusion_and_Interactive_CVPR_2025_paper.html) CraftsMan3D: High-fidelity Mesh Generation with 3D Native Diffusion and Interactive Geometry Refiner | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0337](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_PartGen_Part-level_3D_Generation_and_Reconstruction_with_Multi-view_Diffusion_Models_CVPR_2025_paper.html) PartGen: Part-level 3D Generation and Reconstruction with Multi-view Diffusion Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0338](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_SeaLion_Semantic_Part-Aware_Latent_Point_Diffusion_Models_for_3D_Generation_CVPR_2025_paper.html) SeaLion: Semantic Part-Aware Latent Point Diffusion Models for 3D Generation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0339](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_DIFIX3D_Improving_3D_Reconstructions_with_Single-Step_Diffusion_Models_CVPR_2025_paper.html) DIFIX3D+: Improving 3D Reconstructions with Single-Step Diffusion Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0340](https://openaccess.thecvf.com/content/CVPR2025/html/Lee_DiET-GS_Diffusion_Prior_and_Event_Stream-Assisted_Motion_Deblurring_3D_Gaussian_CVPR_2025_paper.html) DiET-GS: Diffusion Prior and Event Stream-Assisted Motion Deblurring 3D Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0341](https://openaccess.thecvf.com/content/CVPR2025/html/Dai_EAP-GS_Efficient_Augmentation_of_Pointcloud_for_3D_Gaussian_Splatting_in_CVPR_2025_paper.html) EAP-GS: Efficient Augmentation of Pointcloud for 3D Gaussian Splatting in Few-shot Scene Reconstruction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0342](https://openaccess.thecvf.com/content/CVPR2025/html/Zhong_Taming_Video_Diffusion_Prior_with_Scene-Grounding_Guidance_for_3D_Gaussian_CVPR_2025_paper.html) Taming Video Diffusion Prior with Scene-Grounding Guidance for 3D Gaussian Splatting from Sparse Inputs | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0343](https://openaccess.thecvf.com/content/CVPR2025/html/Shen_High-fidelity_3D_Object_Generation_from_Single_Image_with_RGBN-Volume_Gaussian_CVPR_2025_paper.html) High-fidelity 3D Object Generation from Single Image with RGBN-Volume Gaussian Reconstruction Model | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0344](https://openaccess.thecvf.com/content/CVPR2025/html/Leonard_Light_Transport-aware_Diffusion_Posterior_Sampling_for_Single-View_Reconstruction_of_3D_CVPR_2025_paper.html) Light Transport-aware Diffusion Posterior Sampling for Single-View Reconstruction of 3D Volumes | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0345](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_G3Flow_Generative_3D_Semantic_Flow_for_Pose-aware_and_Generalizable_Object_CVPR_2025_paper.html) G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0346](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_Uni3R_Unified_3D_Reconstruction_and_Semantic_Understanding_via_Generalizable_Gaussian_CVPR_2026_paper.html) Uni3R: Unified 3D Reconstruction and Semantic Understanding via Generalizable Gaussian Splatting from Unposed Multi-View Images | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0347](https://openaccess.thecvf.com/content/CVPR2026/html/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.html) TokenSplat: Token-aligned 3D Gaussian Splatting for Feed-forward Pose-free Reconstruction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0348](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_E2EGS_Event-to-Edge_Gaussian_Splatting_for_Pose-Free_3D_Reconstruction_CVPR_2026_paper.html) E2EGS: Event-to-Edge Gaussian Splatting for Pose-Free 3D Reconstruction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0349](https://openaccess.thecvf.com/content/CVPR2026/html/Ding_ExtrinSplat_Decoupling_Geometry_and_Semantics_for_Open-Vocabulary_Understanding_in_3D_CVPR_2026_paper.html) ExtrinSplat: Decoupling Geometry and Semantics for Open-Vocabulary Understanding in 3D Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0350](https://openaccess.thecvf.com/content/CVPR2026/html/Lv_Gau-Occ_Geometry-Completed_Gaussians_for_Multi-Modal_3D_Occupancy_Prediction_CVPR_2026_paper.html) Gau-Occ: Geometry-Completed Gaussians for Multi-Modal 3D Occupancy Prediction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0351](https://openaccess.thecvf.com/content/CVPR2026/html/Song_PointGS_Semantic-Consistent_Unsupervised_3D_Point_Cloud_Segmentation_with_3D_Gaussian_CVPR_2026_paper.html) PointGS: Semantic-Consistent Unsupervised 3D Point Cloud Segmentation with 3D Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0352](https://openaccess.thecvf.com/content/CVPR2026/html/Noda_3D_Gaussian_Splatting_with_Self-Constrained_Priors_for_High_Fidelity_Surface_CVPR_2026_paper.html) 3D Gaussian Splatting with Self-Constrained Priors for High Fidelity Surface Reconstruction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0353](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_AERGS-SLAM_Auto-Exposure-Robust_Stereo_3D_Gaussian_Splatting_SLAM_CVPR_2026_paper.html) AERGS-SLAM: Auto-Exposure-Robust Stereo 3D Gaussian Splatting SLAM | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ✓ |
| [pr-0354](https://openaccess.thecvf.com/content/CVPR2026/html/Ma_BA-GS_Bayesian_Adaptive_Gaussian_Splatting_for_SFM-Free_3D_Reconstruction_CVPR_2026_paper.html) BA-GS: Bayesian Adaptive Gaussian Splatting for SFM-Free 3D Reconstruction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0355](https://openaccess.thecvf.com/content/CVPR2026/html/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.html) C-GenReg: Training-Free 3D Point Cloud Registration by Multi-View-Consistent Geometry-to-Image Generation with Probabilistic Modalities Fusion | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0356](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.html) Distilling Unsigned Distance Function for Surface Reconstruction from 3D Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0357](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_DualSplat_Robust_3D_Gaussian_Splatting_via_Pseudo-Mask_Bootstrapping_from_Reconstruction_CVPR_2026_paper.html) DualSplat: Robust 3D Gaussian Splatting via Pseudo-Mask Bootstrapping from Reconstruction Failures | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0358](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_GaussFusion_Improving_3D_Reconstruction_in_the_Wild_with_A_Geometry-Informed_CVPR_2026_paper.html) GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0359](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_GaussianZoom_Progressive_Zoom-in_Generative_3D_Gaussian_Splatting_with_Geometric_and_CVPR_2026_paper.html) GaussianZoom: Progressive Zoom-in Generative 3D Gaussian Splatting with Geometric and Semantic Guidance | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0360](https://openaccess.thecvf.com/content/CVPR2026/html/Tao_Geometry-Aware_Cross-Modal_Graph_Alignment_for_Referring_Segmentation_in_3D_Gaussian_CVPR_2026_paper.html) Geometry-Aware Cross-Modal Graph Alignment for Referring Segmentation in 3D Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0361](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_HAD_Hallucination-Aware_Diffusion_Priors_for_3D_Reconstruction_CVPR_2026_paper.html) HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0362](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_L3DR_3D-aware_LiDAR_Diffusion_and_Rectification_CVPR_2026_paper.html) L3DR: 3D-aware LiDAR Diffusion and Rectification | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0363](https://openaccess.thecvf.com/content/CVPR2026/html/Jiao_MAPo_Motion-Aware_Partitioning_of_Deformable_3D_Gaussian_Splatting_for_High-Fidelity_CVPR_2026_paper.html) MAPo: Motion-Aware Partitioning of Deformable 3D Gaussian Splatting for High-Fidelity Dynamic Scene Reconstruction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0364](https://openaccess.thecvf.com/content/CVPR2026/html/He_NG-GS_NeRF-guided_3D_Gaussian_Splatting_Segmentation_CVPR_2026_paper.html) NG-GS: NeRF-guided 3D Gaussian Splatting Segmentation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0365](https://openaccess.thecvf.com/content/CVPR2026/html/Gong_Ov3R_Open-Vocabulary_Semantic_3D_Reconstruction_from_RGB_Videos_CVPR_2026_paper.html) Ov3R: Open-Vocabulary Semantic 3D Reconstruction from RGB Videos | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0366](https://openaccess.thecvf.com/content/CVPR2026/html/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.html) SDGS: Spatial Difference Guided Gaussian Splatting for Simultaneous Localization and 3D Reconstruction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0367](https://openaccess.thecvf.com/content/CVPR2026/html/Feng_SR3R_Rethinking_Super-Resolution_3D_Reconstruction_With_Feed-Forward_Gaussian_Splatting_CVPR_2026_paper.html) SR3R: Rethinking Super-Resolution 3D Reconstruction With Feed-Forward Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0368](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Urban-GS_A_Unified_3D_Gaussian_Splatting_Framework_for_Compact_and_CVPR_2026_paper.html) Urban-GS: A Unified 3D Gaussian Splatting Framework for Compact and High-Fidelity Aerial-to-Street Reconstruction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0369](https://openaccess.thecvf.com/content/CVPR2026/html/Tran_VarSplat_Uncertainty-aware_3D_Gaussian_Splatting_for_Robust_RGB-D_SLAM_CVPR_2026_paper.html) VarSplat: Uncertainty-aware 3D Gaussian Splatting for Robust RGB-D SLAM | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0370](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_GaussianGrow_Geometry-aware_Gaussian_Growing_from_3D_Point_Clouds_with_Text_CVPR_2026_paper.html) GaussianGrow: Geometry-aware Gaussian Growing from 3D Point Clouds with Text Guidance | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0371](https://openaccess.thecvf.com/content/ICCV2025/html/Wulff_Dream-to-Recon_Monocular_3D_Reconstruction_with_Diffusion-Depth_Distillation_from_Single_Images_ICCV_2025_paper.html) Dream-to-Recon: Monocular 3D Reconstruction with Diffusion-Depth Distillation from Single Images | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0372](https://openaccess.thecvf.com/content/ICCV2025/html/Xu_FreeSplatter_Pose-free_Gaussian_Splatting_for_Sparse-view_3D_Reconstruction_ICCV_2025_paper.html) FreeSplatter: Pose-free Gaussian Splatting for Sparse-view 3D Reconstruction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0373](https://openaccess.thecvf.com/content/ICCV2025/html/Wei_RayletDF_Raylet_Distance_Fields_for_Generalizable_3D_Surface_Reconstruction_from_ICCV_2025_paper.html) RayletDF: Raylet Distance Fields for Generalizable 3D Surface Reconstruction from Point Clouds or Gaussians | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0374](https://openaccess.thecvf.com/content/ICCV2025/html/Fan_RIOcc_Efficient_Cross-Modal_Fusion_Transformer_with_Collaborative_Feature_Refinement_for_ICCV_2025_paper.html) RIOcc: Efficient Cross-Modal Fusion Transformer with Collaborative Feature Refinement for 3D Semantic Occupancy Prediction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0375](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Distilling_Diffusion_Models_to_Efficient_3D_LiDAR_Scene_Completion_ICCV_2025_paper.html) Distilling Diffusion Models to Efficient 3D LiDAR Scene Completion | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0376](https://openaccess.thecvf.com/content/ICCV2025/html/Kung_RadarSplat_Radar_Gaussian_Splatting_for_High-Fidelity_Data_Synthesis_and_3D_ICCV_2025_paper.html) RadarSplat: Radar Gaussian Splatting for High-Fidelity Data Synthesis and 3D Reconstruction of Autonomous Driving Scenes | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0377](https://openaccess.thecvf.com/content/ICCV2025/html/Gan_GaussianOcc_Fully_Self-supervised_and_Efficient_3D_Occupancy_Estimation_with_Gaussian_ICCV_2025_paper.html) GaussianOcc: Fully Self-supervised and Efficient 3D Occupancy Estimation with Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0378](https://www.openaccess.thecvf.com/content/ICCV2025/html/Wen_SEGS-SLAM_Structure-enhanced_3D_Gaussian_Splatting_SLAM_with_Appearance_Embedding_ICCV_2025_paper.html) SEGS-SLAM: Structure-enhanced 3D Gaussian Splatting SLAM with Appearance Embedding | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0379](https://openaccess.thecvf.com/content/ICCV2025/html/Sheng_SpatialSplat_Efficient_Semantic_3D_from_Sparse_Unposed_Images_ICCV_2025_paper.html) SpatialSplat: Efficient Semantic 3D from Sparse Unposed Images | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0380](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_MGSR_2D3D_Mutual-boosted_Gaussian_Splatting_for_High-fidelity_Surface_Reconstruction_under_ICCV_2025_paper.html) MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | 보→? | ✓ |
| [pr-0381](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_QuickSplat_Fast_3D_Surface_Reconstruction_via_Learned_Gaussian_Initialization_ICCV_2025_paper.html) QuickSplat: Fast 3D Surface Reconstruction via Learned Gaussian Initialization | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0382](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_DeGauss_Dynamic-Static_Decomposition_with_Gaussian_Splatting_for_Distractor-free_3D_Reconstruction_ICCV_2025_paper.html) DeGauss: Dynamic-Static Decomposition with Gaussian Splatting for Distractor-free 3D Reconstruction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0383](https://openaccess.thecvf.com/content/ICCV2025/html/Kim_ExploreGS_Explorable_3D_Scene_Reconstruction_with_Virtual_Camera_Samplings_and_ICCV_2025_paper.html) ExploreGS: Explorable 3D Scene Reconstruction with Virtual Camera Samplings and Diffusion Priors | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0384](https://openaccess.thecvf.com/content/ICCV2025/html/Tao_GSV3D_Gaussian_Splatting-based_Geometric_Distillation_with_Stable_Video_Diffusion_for_ICCV_2025_paper.html) GSV3D: Gaussian Splatting-based Geometric Distillation with Stable Video Diffusion for Single-Image 3D Object Generation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ✓ |
| [pr-0385](https://openaccess.thecvf.com/content/ICCV2025/html/Peng_A_Lesson_in_Splats_Teacher-Guided_Diffusion_for_3D_Gaussian_Splats_ICCV_2025_paper.html) A Lesson in Splats: Teacher-Guided Diffusion for 3D Gaussian Splats Generation with 2D Supervision | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0386](https://openaccess.thecvf.com/content/ICCV2025/html/Schwarz_Generative_Gaussian_Splatting_Generating_3D_Scenes_with_Video_Diffusion_Priors_ICCV_2025_paper.html) Generative Gaussian Splatting: Generating 3D Scenes with Video Diffusion Priors | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0387](https://openaccess.thecvf.com/content/ICCV2025/html/Fang_NeRF_Is_a_Valuable_Assistant_for_3D_Gaussian_Splatting_ICCV_2025_paper.html) NeRF Is a Valuable Assistant for 3D Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0388](https://openaccess.thecvf.com/content/ICCV2025/html/Pan_Liberated-GS_3D_Gaussian_Splatting_Independent_from_SfM_Point_Clouds_ICCV_2025_paper.html) Liberated-GS: 3D Gaussian Splatting Independent from SfM Point Clouds | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0389](https://openaccess.thecvf.com/content/ICCV2025/html/Pan_DiGA3D_Coarse-to-Fine_Diffusional_Propagation_of_Geometry_and_Appearance_for_Versatile_ICCV_2025_paper.html) DiGA3D: Coarse-to-Fine Diffusional Propagation of Geometry and Appearance for Versatile 3D Inpainting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0390](https://openaccess.thecvf.com/content/ICCV2025/html/Marks_Tree_Skeletonization_from_3D_Point_Clouds_by_Denoising_Diffusion_ICCV_2025_paper.html) Tree Skeletonization from 3D Point Clouds by Denoising Diffusion | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0391](https://openaccess.thecvf.com/content/ICCV2025/html/Go_VideoRFSplat_Direct_Scene-Level_Text-to-3D_Gaussian_Splatting_Generation_with_Flexible_Pose_ICCV_2025_paper.html) VideoRFSplat: Direct Scene-Level Text-to-3D Gaussian Splatting Generation with Flexible Pose and Multi-View Joint Modeling | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0392](https://openaccess.thecvf.com/content/ICCV2025/html/Xiang_Repurposing_2D_Diffusion_Models_with_Gaussian_Atlas_for_3D_Generation_ICCV_2025_paper.html) Repurposing 2D Diffusion Models with Gaussian Atlas for 3D Generation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0393](https://openaccess.thecvf.com/content/ICCV2025/html/Yuan_Robust_and_Efficient_3D_Gaussian_Splatting_for_Urban_Scene_Reconstruction_ICCV_2025_paper.html) Robust and Efficient 3D Gaussian Splatting for Urban Scene Reconstruction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0394](https://openaccess.thecvf.com/content/ICCV2025/html/Baik_Learning_3D_Object_Spatial_Relationships_from_Pre-trained_2D_Diffusion_Models_ICCV_2025_paper.html) Learning 3D Object Spatial Relationships from Pre-trained 2D Diffusion Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0395](https://openaccess.thecvf.com/content/WACV2025/html/Yao_DepthSSC_Monocular_3D_Semantic_Scene_Completion_via_Depth-Spatial_Alignment_and_WACV_2025_paper.html) DepthSSC: Monocular 3D Semantic Scene Completion via Depth-Spatial Alignment and Voxel Adaptation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0396](https://openaccess.thecvf.com/content/WACV2025/html/Dastmalchi_Test-Time_Adaptation_of_3D_Point_Clouds_via_Denoising_Diffusion_Models_WACV_2025_paper.html) Test-Time Adaptation of 3D Point Clouds via Denoising Diffusion Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0397](https://openaccess.thecvf.com/content/WACV2025/html/Wang_UW-GS_Distractor-Aware_3D_Gaussian_Splatting_for_Enhanced_Underwater_Scene_Reconstruction_WACV_2025_paper.html) UW-GS: Distractor-Aware 3D Gaussian Splatting for Enhanced Underwater Scene Reconstruction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0398](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3187_ECCV_2024_paper.php) MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0399](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3212_ECCV_2024_paper.php) GS-LRM: Large Reconstruction Model for 3D Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0400](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/2662_ECCV_2024_paper.php) MVSGaussian: Fast Generalizable Gaussian Splatting Reconstruction from Multi-View Stereo | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |

<a id="batch-05"></a>

### 배치 05

| ID · 공식 표제 | 링크 | 제목 | 저자 | 연도 | 발표처·게재 | 요약·기여 | 코드 | 가중치 | 데이터 | 태그 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [pr-0401](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5636_ECCV_2024_paper.php) GeoCalib: Learning Single-image Calibration with Geometric Optimization | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ✓ |
| [pr-0402](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3580_ECCV_2024_paper.php) CG-SLAM: Efficient Dense RGB-D SLAM in a Consistent Uncertainty-aware 3D Gaussian Field | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0403](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5218_ECCV_2024_paper.php) GeoGaussian: Geometry-aware Gaussian Splatting for Scene Rendering | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0404](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/2380_ECCV_2024_paper.php) GaussReg: Fast 3D Registration with Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0405](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/2887_ECCV_2024_paper.php) SAGS: Structure-Aware 3D Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0406](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/274_ECCV_2024_paper.php) Surface Reconstruction for 3D Gaussian Splatting via Local Structural Hints | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0407](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4195_ECCV_2024_paper.php) Gaussian Grouping: Segment and Edit Anything in 3D Scenes | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0408](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/8870_ECCV_2024_paper.php) SG-NeRF: Neural Surface Reconstruction with Scene Graph Optimization | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | 보→✓ | ? | ? | ? |
| [pr-0409](https://proceedings.iclr.cc/paper_files/paper/2025/hash/857b34d81f0a8bfe3e18879dee3b5086-Abstract-Conference.html) No Pose, No Problem: Surprisingly Simple 3D Gaussian Splats from Sparse Unposed Images | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0410](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8cbde11e5e271ef9ff67fc9f292e43ed-Abstract-Conference.html) SplatFormer: Point Transformer for Robust 3D Gaussian Splatting | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0411](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d218ec74edbfc494fa7d7a253951c603-Abstract-Conference.html) CityGaussianV2: Efficient and Geometrically Accurate Reconstruction for Large-Scale Scenes | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0412](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8e86fd925dda476f574689f4ce748193-Abstract-Conference.html) GS-LiDAR: Generating Realistic LiDAR Point Clouds with Panoramic Gaussian Splatting | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | 오→✓ |
| [pr-0413](https://proceedings.iclr.cc/paper_files/paper/2025/hash/804f1fac094d7b751410b50066da3a63-Abstract-Conference.html) ComPC: Completing a 3D Point Cloud with 2D Diffusion Priors | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0414](https://proceedings.iclr.cc/paper_files/paper/2025/hash/623307df18da128262aaf394cdcfb235-Abstract-Conference.html) Flow Distillation Sampling: Regularizing 3D Gaussians with Pre-trained Matching Priors | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0415](https://proceedings.iclr.cc/paper_files/paper/2025/hash/6518f9339196e172fa0ceef48a85543a-Abstract-Conference.html) DiffSplat: Repurposing Image Diffusion Models for Scalable Gaussian Splat Generation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0416](https://proceedings.iclr.cc/paper_files/paper/2025/hash/64d4ff4fff788cdffe236f9ce8b09400-Abstract-Conference.html) GotenNet: Rethinking Efficient 3D Equivariant Graph Neural Networks | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0417](https://proceedings.iclr.cc/paper_files/paper/2025/hash/76c5401551bbe8337dc38a2bd5eb394e-Abstract-Conference.html) LaGeM: A Large Geometry Model for 3D Representation Learning and Diffusion | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0418](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a9cae5b74cfc8f71c39a4e646db819c2-Abstract-Conference.html) SC-OmniGS: Self-Calibrating Omnidirectional Gaussian Splatting | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0419](https://proceedings.iclr.cc/paper_files/paper/2025/hash/03bdba50e3741ac5e3eaa0e55423587e-Abstract-Conference.html) ThermalGaussian: Thermal 3D Gaussian Splatting | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0420](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8b21a7ea42cbcd1c29a7a88c444cce45-Abstract-Conference.html) Multimodality Helps Few-shot 3D Point Cloud Semantic Segmentation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0421](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f53437debdd397c42929d929614bc705-Abstract-Conference.html) Segment Any 3D Object with Language | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0422](https://proceedings.iclr.cc/paper_files/paper/2026/hash/829d8117138ea1ea3eae65bd526ff727-Abstract-Conference.html) Dens3R: A Foundation Model for 3D Geometry Prediction | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0423](https://proceedings.iclr.cc/paper_files/paper/2026/hash/e0ac27bf3327c9cb99cc5f548db4f73a-Abstract-Conference.html) G4Splat: Geometry-Guided Gaussian Splatting with Generative Prior | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0424](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5fcacc84d87c97bee5baecb3fb8f6e88-Abstract-Conference.html) Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0425](https://proceedings.iclr.cc/paper_files/paper/2026/hash/b8932994f80e23f6dd535f0762ed3ef4-Abstract-Conference.html) GaussianFusion: Unified 3D Gaussian Representation for Multi-Modal Fusion Perception | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0426](https://proceedings.iclr.cc/paper_files/paper/2026/hash/039bc8e424e1fc196b4203555b54ebc4-Abstract-Conference.html) GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0427](https://proceedings.iclr.cc/paper_files/paper/2026/hash/49f42aafbcce59b2665640cb9f3d794f-Abstract-Conference.html) RayI2P: Learning Rays for Image-to-Point Cloud Registration | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0428](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3a10c46572628d58cb44fb705f25cbbf-Abstract-Conference.html) SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0429](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cb2266111eadcfa2c02187ace64e2183-Abstract-Conference.html) UniSplat: Unified Spatio-Temporal Fusion via 3D Latent Scaffolds for Dynamic Driving Scene Reconstruction | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0430](https://proceedings.iclr.cc/paper_files/paper/2026/hash/108030643e640ac050e0ed5e6aace48f-Abstract-Conference.html) UrbanGS: Efficient and Scalable Architecture for Geometrically Accurate Large-Scene Reconstruction | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0431](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6fa4a1def9d60b5bf6078e13c900c45c-Abstract-Conference.html) WorldSplat: Gaussian-Centric Feed-Forward 4D Scene Generation for Autonomous Driving | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0432](https://proceedings.iclr.cc/paper_files/paper/2026/hash/e1f20114b5233d395486f9cf5b3e0535-Abstract-Conference.html) IGGT: Instance-Grounded Geometry Transformer for Semantic 3D Reconstruction | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0433](https://proceedings.iclr.cc/paper_files/paper/2026/hash/9a0ca0a65535cc70ab9c6e71ed830136-Abstract-Conference.html) SimULi: Real-Time LiDAR and Camera Simulation with Unscented Transforms | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0434](https://proceedings.iclr.cc/paper_files/paper/2026/hash/c196239c5f9481e0db2755f31fe4585f-Abstract-Conference.html) Geometry Forcing: Marrying Video Diffusion and 3D Representation for Consistent World Modeling | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0435](https://neurips.cc/virtual/2025/poster/118540) EAG3R: Event-Augmented 3D Geometry Estimation for Dynamic and Extreme-Lighting Scenes | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0436](https://neurips.cc/virtual/2025/poster/118929) SIU3R: Simultaneous Scene Understanding and 3D Reconstruction Beyond Feature Alignment | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0437](https://neurips.cc/virtual/2025/poster/117447) OnlineSplatter: Pose-Free Online 3D Reconstruction for Free-Moving Objects | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0438](https://neurips.cc/virtual/2025/poster/115951) Fin3R: Fine-tuning Feed-forward 3D Reconstruction Models via Monocular Knowledge Distillation | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0439](https://neurips.cc/static/virtual/data/neurips-2025-orals-posters.json) PLANA3R: Zero-shot Metric Planar 3D Reconstruction via Feed-forward Planar Splatting | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0440](https://neurips.cc/virtual/2025/poster/117748) GeGS-PCR: Fast and Robust Color 3D Point Cloud Registration with Two-Stage Geometric-3DGS Fusion | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0441](https://neurips.cc/virtual/2025/poster/116898) MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0442](https://neurips.cc/virtual/2025/poster/118967) Multimodal LiDAR-Camera Novel View Synthesis with Unified Pose-free Neural Fields | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0443](https://neurips.cc/virtual/2025/poster/116149) Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0444](https://neurips.cc/virtual/2025/poster/117899) Spiral: Semantic-Aware Progressive LiDAR Scene Generation and Understanding | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0445](https://neurips.cc/virtual/2025/poster/119271) ODG: Occupancy Prediction Using Dual Gaussians | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0446](https://neurips.cc/virtual/2025/poster/116646) U-CAN: Unsupervised Point Cloud Denoising with Consistency-Aware Noise2Noise Matching | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0447](https://neurips.cc/virtual/2025/poster/115683) Point-MaDi: Masked Autoencoding with Diffusion for Point Cloud Pre-training | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0448](https://neurips.cc/virtual/2025/poster/116903) QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0449](https://neurips.cc/virtual/2025/poster/117322) VA-GS: Enhancing the Geometric Representation of Gaussian Splatting via View Alignment | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0450](https://proceedings.mlr.press/v267/jiang25k.html) Generative Point Cloud Registration | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0451](https://proceedings.mlr.press/v267/hong25c.html) PF3plat: Pose-Free Feed-Forward 3D Gaussian Splatting for Novel View Synthesis | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0452](https://proceedings.mlr.press/v267/ai25a.html) GAPrompt: Geometry-Aware Point Cloud Prompt for 3D Vision Model | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0453](https://proceedings.mlr.press/v267/kim25r.html) Thickness-aware E(3)-Equivariant 3D Mesh Neural Networks | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0454](https://proceedings.mlr.press/v267/takmaz25a.html) Towards Learning to Complete Anything in Lidar | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0455](https://proceedings.mlr.press/v267/ding25a.html) Scalable Non-Equivariant 3D Molecule Generation via Rotational Alignment | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0456](https://icml.cc/virtual/2026/poster/65079) VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0457](https://icml.cc/virtual/2026/poster/65052) WorldMirror: Universal 3D World Reconstruction with Any-Prior Prompting | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0458](https://icml.cc/virtual/2026/poster/65722) PRISM: Learning Realistic Depth via Physics-Grounded Noise Disentanglement with Semantic-Geometric Collaboration | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0459](https://icml.cc/virtual/2026/poster/62351) PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0460](https://icml.cc/virtual/2026/poster/62937) Rh-3DGS: Robust Open-Vocabulary Scene Understanding via Riemannian Huber Distillation and Manifold-Aware Sampling | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0461](https://icml.cc/virtual/2026/poster/65536) S2GS: Streaming Semantic Gaussian Splatting for Online Scene Understanding and Reconstruction | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0462](https://icml.cc/virtual/2026/poster/62657) EnerGS: Energy-Based Gaussian Splatting with Partial Geometric Priors | 보→✓ | 오→✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0463](https://icml.cc/virtual/2026/poster/62119) Flow Equivariant World Models: Structured Memory for Dynamic Environments | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0464](https://icml.cc/virtual/2026/poster/62601) Affine-Equivariant Kernel Space Encoding for NeRF Editing | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0465](https://icml.cc/virtual/2026/poster/64540) Rethinking Serialization in Linear 3D Vision: Decoupling Anisotropic Geometry from Isotropic Semantics | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0466](https://icml.cc/virtual/2026/poster/64558) Weakly Supervised Cross-Modal Learning for 4D Radar Scene Flow Estimation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0467](https://3dvconf.github.io/2025/schedule_updated2.csv) MASt3R-SfM: a Fully-Integrated Solution for Unconstrained Structure-from-Motion | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0468](https://3dvconf.github.io/2025/schedule_updated2.csv) FlowMap: High-Quality Camera Poses, Intrinsics, and Depth via Gradient Descent | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0469](https://3dvconf.github.io/2025/schedule_updated2.csv) Flash3D: Feed-Forward Generalisable 3D Scene Reconstruction from a Single Image | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0470](https://3dvconf.github.io/2025/schedule_updated2.csv) AGS-Mesh: Adaptive Gaussian Splatting and Meshing with Geometric Priors for Indoor Room Reconstruction Using Smartphones | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0471](https://3dvconf.github.io/2025/schedule_updated2.csv) LoopSplat: Loop Closure by Registering 3D Gaussian Splats | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0472](https://3dvconf.github.io/2025/schedule_updated2.csv) WaterSplatting: Fast Underwater 3D Scene Reconstruction using Gaussian Splatting | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0473](https://3dvconf.github.io/2025/schedule_updated2.csv) SparseGS: Sparse View Synthesis using 3D Gaussian Splatting | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0474](https://3dvconf.github.io/2025/schedule_updated2.csv) LangOcc: Open Vocabulary Occupancy Estimation via Volume Rendering | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0475](https://3dvconf.github.io/2025/schedule_updated2.csv) Efficient Continuous Group Convolutions for Local SE(3) Equivariance in 3D Point Clouds | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0476](https://3dvconf.github.io/2025/schedule_updated2.csv) SSRFlow: Semantic-aware Fusion with Spatial Temporal Re-embedding for Real-world Scene Flow | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0477](https://3dvconf.github.io/2025/schedule_updated2.csv) SMORE: Simultaneous Map and Object REconstruction | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0478](https://3dvconf.github.io/2025/schedule_updated2.csv) iFusion: Inverting Diffusion for Pose-Free Reconstruction from Sparse Views | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0479](https://3dvconf.github.io/2025/schedule_updated2.csv) GRIN: Zero-Shot Metric Depth with Pixel-Level Diffusion | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0480](https://3dvconf.github.io/2025/schedule_updated2.csv) CoE: Deep Coupled Embedding for Non-Rigid Point Cloud Correspondences | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0481](https://3dvconf.github.io/2025/schedule_updated2.csv) LSSInst: Improving Geometric Modeling in LSS-Based BEV Perception with Instance Representation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0482](https://openaccess.thecvf.com/content_ICCV_2019/html/Choy_Fully_Convolutional_Geometric_Features_ICCV_2019_paper.html) Fully Convolutional Geometric Features | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | 보→✓ | 보→✓ | ? |
| [pr-0483](https://api.crossref.org/works/10.1109/iccv.2019.00362) Deep Closest Point: Learning Representations for Point Cloud Registration | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0484](https://iclr.cc/static/virtual/data/iclr-2021-orals-posters.json) Score-Based Generative Modeling through Stochastic Differential Equations | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0485](https://iclr.cc/virtual/2023/oral/12607) DreamFusion: Text-to-3D using 2D Diffusion | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0486](https://proceedings.neurips.cc/paper_files/paper/2022/hash/960a172bc7fbf0177ccccbb411a7d800-Abstract-Conference.html) Flamingo: a Visual Language Model for Few-Shot Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0487](https://proceedings.mlr.press/v202/li23q.html) BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0488](https://openaccess.thecvf.com/content_cvpr_2016/html/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.html) Structure-from-Motion Revisited | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0489](https://api.crossref.org/works/10.1109/ISMAR.2011.6092378) KinectFusion: Real-Time Dense Surface Mapping and Tracking | 오→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0490](https://arxiv.org/abs/1604.01093) BundleFusion: Real-time Globally Consistent 3D Reconstruction using On-the-fly Surface Reintegration | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0491](https://arxiv.org/abs/2007.10985) PointContrast: Unsupervised Pre-training for 3D Point Cloud Understanding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0492](https://openaccess.thecvf.com/content/CVPR2023/html/Gao_ULIP_Learning_a_Unified_Representation_of_Language_Images_and_Point_CVPR_2023_paper.html) ULIP: Learning a Unified Representation of Language, Images, and Point Clouds for 3D Understanding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | 보→✓ | ? |
| [pr-0493](https://arxiv.org/abs/1910.02527) 3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0494](https://openaccess.thecvf.com/content/ICCV2021/html/Barron_Mip-NeRF_A_Multiscale_Representation_for_Anti-Aliasing_Neural_Radiance_Fields_ICCV_2021_paper.html) Mip-NeRF: A Multiscale Representation for Anti-Aliasing Neural Radiance Fields | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0495](https://arxiv.org/abs/2201.05989) Instant Neural Graphics Primitives with a Multiresolution Hash Encoding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0496](https://arxiv.org/abs/1702.04405) ScanNet: Richly-annotated 3D Reconstructions of Indoor Scenes | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ✓ |
| [pr-0497](https://api.crossref.org/works/10.1109/iccv.2019.00939) SemanticKITTI: A Dataset for Semantic Scene Understanding of LiDAR Sequences | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0498](https://openaccess.thecvf.com/content/CVPR2022/html/Azuma_ScanQA_3D_Question_Answering_for_Spatial_Scene_Understanding_CVPR_2022_paper.html) ScanQA: 3D Question Answering for Spatial Scene Understanding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | 오→✓ | ? |
| [pr-0499](https://arxiv.org/abs/1709.06158) Matterport3D: Learning from RGB-D Data in Indoor Environments | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0500](https://openaccess.thecvf.com/content_ICCV_2019/html/Savva_Habitat_A_Platform_for_Embodied_AI_Research_ICCV_2019_paper.html) Habitat: A Platform for Embodied AI Research | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ |

<a id="batch-06"></a>

### 배치 06

| ID · 공식 표제 | 링크 | 제목 | 저자 | 연도 | 발표처·게재 | 요약·기여 | 코드 | 가중치 | 데이터 | 태그 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [pr-0501](https://proceedings.mlr.press/v155/zeng21a.html) Transporter Networks: Rearranging the Visual World for Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? |
| [pr-0502](https://proceedings.mlr.press/v164/shridhar22a.html) CLIPort: What and Where Pathways for Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | 보→✓ | ? | ? | ? |
| [pr-0503](https://arxiv.org/abs/2112.05124) Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation | ✓ | ✓ | 보→✓ | 오→✓ | 오→✓ | ? | ? | ? | ? | ? |
| [pr-0504](https://api.crossref.org/works/10.1109/cvpr.2018.00472) VoxelNet: End-to-End Learning for Point Cloud Based 3D Object Detection | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0505](https://api.crossref.org/works/10.1109/cvpr.2019.01298) PointPillars: Fast Encoders for Object Detection from Point Clouds | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0506](https://arxiv.org/abs/2008.05711) Lift, Splat, Shoot: Encoding Images from Arbitrary Camera Rigs by Implicitly Unprojecting to 3D | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? |
| [pr-0507](https://arxiv.org/abs/1512.03012) ShapeNet: An Information-Rich 3D Model Repository | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-0508](https://proceedings.neurips.cc/paper_files/paper/2018/hash/f5f8590cd58a54e94377e6ae2eded4d9-Abstract.html) PointCNN: Convolution On X-Transformed Points | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0509](https://openaccess.thecvf.com/content/ICCV2021/html/Zhang_Self-Supervised_Pretraining_of_3D_Features_on_Any_Point-Cloud_ICCV_2021_paper.html) Self-Supervised Pretraining of 3D Features on any Point-Cloud | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0510](https://openaccess.thecvf.com/content/CVPR2022/html/Barron_Mip-NeRF_360_Unbounded_Anti-Aliased_Neural_Radiance_Fields_CVPR_2022_paper.html) Mip-NeRF 360: Unbounded Anti-Aliased Neural Radiance Fields | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0511](https://proceedings.neurips.cc/paper_files/paper/2021/hash/e41e164f7485ec4a28741a2d0ea41c74-Abstract.html) NeuS: Learning Neural Implicit Surfaces by Volume Rendering for Multi-view Reconstruction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0512](https://openaccess.thecvf.com/content_cvpr_2017/html/Song_Semantic_Scene_Completion_CVPR_2017_paper.html) Semantic Scene Completion From a Single Depth Image | ✓ | 오→✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0513](https://openaccess.thecvf.com/content/CVPR2022/html/Cao_MonoScene_Monocular_3D_Semantic_Scene_Completion_CVPR_2022_paper.html) MonoScene: Monocular 3D Semantic Scene Completion | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0514](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_OccFormer_Dual-path_Transformer_for_Vision-based_3D_Semantic_Occupancy_Prediction_ICCV_2023_paper.html) OccFormer: Dual-path Transformer for Vision-based 3D Semantic Occupancy Prediction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0515](https://iclr.cc/static/virtual/data/iclr-2021-orals-posters.json) Denoising Diffusion Implicit Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0516](https://arxiv.org/abs/2207.12598) Classifier-Free Diffusion Guidance | ✓ | ✓ | 보→✓ | 오→✓ | 오→✓ | ? | ? | ? | ? | ? |
| [pr-0517](https://arxiv.org/abs/1802.08219) Tensor Field Networks: Rotation- and Translation-Equivariant Neural Networks for 3D Point Clouds | ✓ | ✓ | 보→✓ | ✓ | ? | 보→✓ | ✓ | ? | ? | ? |
| [pr-0518](https://arxiv.org/abs/1602.07576) Group Equivariant Convolutional Networks | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0519](https://proceedings.neurips.cc/paper_files/paper/2014/hash/91c56ce4a249fae5419b90cba831e303-Abstract.html) Depth Map Prediction from a Single Image using a Multi-Scale Deep Network | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0520](https://arxiv.org/abs/1806.01260) Digging Into Self-Supervised Monocular Depth Estimation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0521](https://openaccess.thecvf.com/content/ICCV2021/html/Ranftl_Vision_Transformers_for_Dense_Prediction_ICCV_2021_paper.html) Vision Transformers for Dense Prediction | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? |
| [pr-0522](https://proceedings.mlr.press/v15/ross11a.html) A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0523](https://proceedings.neurips.cc/paper_files/paper/2016/hash/cc7e2b878868cbae992d1fb743995d8f-Abstract.html) Generative Adversarial Imitation Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0524](https://arxiv.org/abs/1707.06347) Proximal Policy Optimization Algorithms | ✓ | ✓ | 보→✓ | ✓ | ? | ✓ | ✓ | ? | ? | ✓ |
| [pr-0525](https://api.crossref.org/works/10.1109/ISMAR.2007.4538852) Parallel Tracking and Mapping for Small AR Workspaces | 보→✓ | 오→✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0526](https://api.crossref.org/works/10.1007/978-3-319-10605-2_54) LSD-SLAM: Large-Scale Direct Monocular SLAM | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0527](https://www.roboticsproceedings.org/rss11/p01.html) ElasticFusion: Dense SLAM Without A Pose Graph | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0528](https://proceedings.neurips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract-Conference.html) Training language models to follow instructions with human feedback | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0529](https://proceedings.neurips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html) Chain-of-Thought Prompting Elicits Reasoning in Large Language Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0530](https://openaccess.thecvf.com/content/CVPR2022/html/He_Masked_Autoencoders_Are_Scalable_Vision_Learners_CVPR_2022_paper.html) Masked Autoencoders Are Scalable Vision Learners | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0531](https://openaccess.thecvf.com/content/ICCV2021/html/Caron_Emerging_Properties_in_Self-Supervised_Vision_Transformers_ICCV_2021_paper.html) Emerging Properties in Self-Supervised Vision Transformers | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0532](https://arxiv.org/abs/2303.05499) Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | 보→✓ | ? | ? |
| [pr-0533](https://proceedings.mlr.press/v139/jia21b.html) Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision | ✓ | 오→✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0534](https://proceedings.mlr.press/v162/li22n.html) BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? |
| [pr-0535](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6dcf277ea32ce3288914faf369fe6de0-Abstract-Conference.html) Visual Instruction Tuning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0536](https://proceedings.mlr.press/v164/jang22a.html) BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning | ✓ | ✓ | 보→✓ | 오→✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0537](https://openaccess.thecvf.com/content/ICCV2021/html/Zhi_In-Place_Scene_Labelling_and_Understanding_With_Implicit_Scene_Representation_ICCV_2021_paper.html) In-Place Scene Labelling and Understanding with Implicit Scene Representation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0538](https://proceedings.mlr.press/v229/shen23a.html) Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0539](https://openaccess.thecvf.com/content_cvpr_2018/html/Anderson_Vision-and-Language_Navigation_Interpreting_CVPR_2018_paper.html) Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ |
| [pr-0540](https://api.crossref.org/works/10.1109/ICRA57147.2024.10610712) VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ |
| [pr-0541](https://arxiv.org/abs/2004.02857) Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ |
| [pr-0542](https://aclanthology.org/2020.emnlp-main.356/) Room-Across-Room: Multilingual Vision-and-Language Navigation with Dense Spatiotemporal Grounding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0543](https://iclr.cc/static/virtual/data/iclr-2022-orals-posters.json) Language-driven Semantic Segmentation | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0544](https://api.crossref.org/works/10.1007/978-3-031-20059-5_31) Scaling Open-Vocabulary Image Segmentation with Image-Level Labels | ✓ | 오→✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0545](https://arxiv.org/abs/2201.02605) Detecting Twenty-thousand Classes using Image-level Supervision | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0546](https://api.crossref.org/works/10.1109/cvpr42600.2020.01164) nuScenes: A Multimodal Dataset for Autonomous Driving | ? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0547](https://proceedings.neurips.cc/paper_files/paper/2023/hash/cabfaeecaae7d6540ee797a66f0130b0-Abstract-Datasets_and_Benchmarks.html) Occ3D: A Large-Scale 3D Occupancy Prediction Benchmark for Autonomous Driving | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0548](https://openaccess.thecvf.com/content_CVPR_2020/html/Sun_Scalability_in_Perception_for_Autonomous_Driving_Waymo_Open_Dataset_CVPR_2020_paper.html) Scalability in Perception for Autonomous Driving: Waymo Open Dataset | ✓ | 오→✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0549](https://proceedings.mlr.press/v164/wang22b.html) DETR3D: 3D Object Detection from Multi-view Images via 3D-to-2D Queries | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0550](https://api.crossref.org/works/10.1109/JRA.1987.1087068) A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0551](https://api.crossref.org/works/10.1109/70.508439) Probabilistic Roadmaps for Path Planning in High-Dimensional Configuration Spaces | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0552](https://lavalle.pl/papers/Lav98c.pdf) Rapidly-Exploring Random Trees: A New Tool for Path Planning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0553](https://cdn.aaai.org/AAAI/2002/AAAI02-072.pdf) D* Lite | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0554](https://cdn.aaai.org/AAAI/2002/AAAI02-089.pdf) FastSLAM: A Factored Solution to the Simultaneous Localization and Mapping Problem | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0555](https://api.crossref.org/works/10.1109/ROBOT.2009.5152817) CHOMP: Gradient Optimization Techniques for Efficient Motion Planning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0556](https://api.crossref.org/works/10.1109/ICRA.2011.5980280) STOMP: Stochastic Trajectory Optimization for Motion Planning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0557](https://arxiv.org/abs/1105.1186) Sampling-based Algorithms for Optimal Motion Planning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0558](https://api.crossref.org/works/10.1177/0278364914528132) Motion Planning with Sequential Convex Optimization and Convex Collision Checking | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0559](https://api.crossref.org/works/10.1162/NECO_a_00393) Dynamical Movement Primitives: Learning Attractor Models for Motor Behaviors | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0560](https://proceedings.neurips.cc/paper_files/paper/2014/hash/c7c9344b5a3c0533e29fa69ce807cf08-Abstract.html) Learning Neural Network Policies with Guided Policy Search under Unknown Dynamics | 오→✓ | ✓ | 보→✓ | 오→✓ | 오→✓ | 오→✓ | 보→? | ? | ? | ✓ |
| [pr-0561](https://api.crossref.org/works/10.1109/iros.2017.8202133) Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0562](https://www.roboticsproceedings.org/rss13/p58.html) Dex-Net 2.0: Deep Learning to Plan Robust Grasps with Synthetic Point Clouds and Analytic Grasp Metrics | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0563](https://proceedings.mlr.press/v87/kalashnikov18a.html) Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation | ✓ | 오→✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0564](https://www.roboticsproceedings.org/rss17/p011.html) RMA: Rapid Motor Adaptation for Legged Robots | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0565](https://proceedings.mlr.press/v164/rudin22a.html) Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0566](https://www.roboticsproceedings.org/rss19/p016.html) Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ |
| [pr-0567](https://api.crossref.org/works/10.1109/icra57147.2024.10611597) SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0568](https://api.crossref.org/works/10.1109/icra57147.2024.10610665) NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0569](https://api.crossref.org/works/10.1109/icra57147.2024.10611254) Resilient Legged Local Navigation: Learning to Traverse with Compromised Perception End-to-End | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0570](https://api.crossref.org/works/10.1109/icra57147.2024.10611621) Learning Vision-Based Bipedal Locomotion for Challenging Terrain | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0571](https://api.crossref.org/works/10.1109/icra57147.2024.10611305) Hearing Touch: Audio-Visual Pretraining for Contact-Rich Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0572](https://arxiv.org/abs/2309.08770) Constrained Bimanual Planning with Analytic Inverse Kinematics | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0573](https://proceedings.mlr.press/v270/sferrazza25a.html) Body Transformer: Leveraging Robot Embodiment for Policy Learning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0574](https://proceedings.mlr.press/v270/fu25b.html) Mobile ALOHA: Learning Bimanual Mobile Manipulation using Low-Cost Whole-Body Teleoperation | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | 보→✓ | ? | ? | ✓ |
| [pr-0575](https://proceedings.mlr.press/v270/levy25a.html) Learning to Walk from Three Minutes of Real-World Data with Semi-structured Dynamics Models | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0576](https://proceedings.mlr.press/v270/xing25a.html) Bootstrapping Reinforcement Learning with Imitation for Vision-Based Agile Flight | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0577](https://proceedings.mlr.press/v270/chisari25a.html) Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0578](https://openaccess.thecvf.com/content/CVPR2024/html/Uppal_SPIN_Simultaneous_Perception_Interaction_and_Navigation_CVPR_2024_paper.html) SPIN: Simultaneous Perception, Interaction and Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0579](https://proceedings.iclr.cc/paper_files/paper/2025/hash/7571c9d44179c7988178593c5b62a9b6-Abstract-Conference.html) Geometry-aware RL for Manipulation of Varying Shapes and Deformable Objects | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0580](https://proceedings.iclr.cc/paper_files/paper/2025/hash/88b7b2c896506daabc8d3fd587055167-Abstract-Conference.html) Data Scaling Laws in Imitation Learning for Robotic Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0581](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e5b5c402bb7bd5e60bede6961d6fe39e-Abstract-Conference.html) Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0582](https://proceedings.iclr.cc/paper_files/paper/2025/hash/eee6efe709623f36483e3fbb0bb513dd-Abstract-Conference.html) Multi-Robot Motion Planning with Diffusion Models | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0583](https://proceedings.iclr.cc/paper_files/paper/2025/hash/27aa3a0e6d63db269977bb2df5607cb8-Abstract-Conference.html) ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0584](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f05a11e682bf9c57ab62f7cff08fbe5b-Abstract-Conference.html) Sensor-Invariant Tactile Representation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0585](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d5a1f97d2b922da92e880d13b7d2bf02-Abstract-Conference.html) DexTrack: Towards Generalizable Neural Tracking Control for Dexterous Manipulation from Human References | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0586](https://neurips.cc/virtual/2025/poster/116341) Object-centric 3D Motion Field for Robot Learning from Human Videos | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0587](https://proceedings.iclr.cc/paper_files/paper/2026/hash/eb9b18ccb76a1156af5779ffdca1d91f-Abstract-Conference.html) Rodrigues Network for Learning Robot Actions | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0588](https://proceedings.iclr.cc/paper_files/paper/2026/hash/fe7f375ef01e43f17d2c32b28a176577-Abstract-Conference.html) Mean Flow Policy with Instantaneous Velocity Constraint for One-step Action Generation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0589](https://api.crossref.org/works/10.1109/icra57385.2026.11696487) OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ✓ | ? |
| [pr-0590](https://api.crossref.org/works/10.1109/icra57385.2026.11696105) Push Anything: Single- and Multi-Object Pushing From First Sight with Contact-Implicit MPC | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0591](https://api.crossref.org/works/10.1109/ROBOT.2002.1013335) A Realtime Pattern Generator for Biped Walking | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0592](https://api.crossref.org/works/10.1142/S0219843605000594) Synthesis of Whole-Body Behaviors through Hierarchical Control of Behavioral Primitives | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0593](https://api.crossref.org/works/10.1007/s10514-015-9476-6) Momentum Control with Hierarchical Inverse Dynamics on a Torque-Controlled Humanoid | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0594](https://www.research.ed.ac.uk/en/publications/optimization-based-locomotion-planning-estimation-and-controldesi/) Optimization-Based Locomotion Planning, Estimation, and Control Design for the Atlas Humanoid Robot | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0595](https://arxiv.org/abs/1804.02717) DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0596](https://proceedings.mlr.press/v100/xie20a.html) Learning Locomotion Skills for Cassie: Iterative Design and Sim-to-Real | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0597](https://www.roboticsproceedings.org/rss16/p031.html) Learning Memory-Based Control for Human-Scale Bipedal Locomotion | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0598](https://www.roboticsproceedings.org/rss17/p061.html) Blind Bipedal Stair Traversal via Sim-to-Real Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0599](https://www.roboticsproceedings.org/rss20/p061.html) HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0600](https://www.roboticsproceedings.org/rss20/p107.html) Expressive Whole-Body Control for Humanoid Robots | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |

<a id="batch-07"></a>

### 배치 07

| ID · 공식 표제 | 링크 | 제목 | 저자 | 연도 | 발표처·게재 | 요약·기여 | 코드 | 가중치 | 데이터 | 태그 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [pr-0601](https://proceedings.mlr.press/v270/fu25a.html) HumanPlus: Humanoid Shadowing and Imitation from Humans | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0602](https://proceedings.mlr.press/v270/he25b.html) OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0603](https://proceedings.mlr.press/v270/zhang25a.html) WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts | 오→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0604](https://www.roboticsproceedings.org/rss21/p061.html) AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ✓ |
| [pr-0605](https://www.roboticsproceedings.org/rss21/p064.html) Learning Humanoid Standing-up Control across Diverse Postures | 오→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0606](https://www.roboticsproceedings.org/rss21/p065.html) LangWBC: Language-Directed Humanoid Whole-Body Control via End-to-End Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0607](https://www.roboticsproceedings.org/rss21/p066.html) ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0608](https://www.roboticsproceedings.org/rss21/p068.html) BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0609](https://www.roboticsproceedings.org/rss21/p070.html) HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0610](https://proceedings.mlr.press/v305/li25i.html) Hold My Beer: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0611](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8c854e7870dc67e0b410a266cd45e0ad-Abstract-Conference.html) HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0612](https://openaccess.thecvf.com/content/CVPR2026/html/Ben_Gallant_Voxel_Grid-based_Humanoid_Locomotion_and_Local-navigation_across_3-D_Constrained_CVPR_2026_paper.html) Gallant: Voxel Grid-Based Humanoid Locomotion and Local Navigation across 3-D Constrained Terrains | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0613](https://openaccess.thecvf.com/content/CVPR2026/html/He_VIRAL_Visual_Sim-to-Real_at_Scale_for_Humanoid_Loco-Manipulation_CVPR_2026_paper.html) VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0614](https://openaccess.thecvf.com/content/CVPR2026/html/Xue_Opening_the_Sim-to-Real_Door_for_Humanoid_Pixel-to-Action_Policy_Transfer_CVPR_2026_paper.html) Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0615](https://proceedings.mlr.press/v37/schulman15.html) Trust Region Policy Optimization | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0616](https://arxiv.org/abs/1509.02971) Continuous Control with Deep Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | 보→? | ? | ? | ✓ |
| [pr-0617](https://proceedings.neurips.cc/paper_files/paper/2017/hash/453fadbd8a1a3af50a9df4df899537b5-Abstract.html) Hindsight Experience Replay | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0618](https://proceedings.mlr.press/v70/achiam17a.html) Constrained Policy Optimization | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0619](https://arxiv.org/abs/1802.09477) Addressing Function Approximation Error in Actor-Critic Methods | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? |
| [pr-0620](https://proceedings.mlr.press/v80/haarnoja18b.html) Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ |
| [pr-0621](https://proceedings.neurips.cc/paper_files/paper/2020/hash/a322852ce0df73e204b7e67cbbef0d0a-Abstract.html) MOPO: Model-based Offline Policy Optimization | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0622](https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html) Conservative Q-Learning for Offline Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0623](https://proceedings.neurips.cc/paper_files/paper/2021/hash/a8166da05c5a094f7dc03724b41886e5-Abstract.html) A Minimalist Approach to Offline Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0624](https://iclr.cc/virtual/2022/poster/5941) Offline Reinforcement Learning with Implicit Q-Learning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ |
| [pr-0625](https://proceedings.mlr.press/v229/chebotar23a.html) Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions | ✓ | ✓ | 보→✓ | 오→✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0626](https://proceedings.iclr.cc/paper_files/paper/2026/hash/24a0f56452202e8433d582dbf5095c32-Abstract-Conference.html) Cross-Embodiment Offline Reinforcement Learning for Heterogeneous Robot Datasets | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0627](https://proceedings.iclr.cc/paper_files/paper/2026/hash/b650f2838de7e1e817b5408b48a19a63-Abstract-Conference.html) What Matters for Batch Online Reinforcement Learning in Robotics? | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0628](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7ff013b7e372ba5b790352ccd6908f03-Abstract-Conference.html) Efficient Reinforcement Learning by Guiding World Models with Non-Curated Data | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0629](https://api.crossref.org/works/10.1145/1015330.1015430) Apprenticeship Learning via Inverse Reinforcement Learning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0630](https://cdn.aaai.org/AAAI/2008/AAAI08-227.pdf) Maximum Entropy Inverse Reinforcement Learning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0631](https://proceedings.mlr.press/v78/finn17a.html) One-Shot Visual Imitation Learning via Meta-Learning | 오→✓ | ✓ | 보→✓ | ✓ | ✓ | 오→✓ | 보→✓ | ? | ✓ | ✓ |
| [pr-0632](https://arxiv.org/abs/1710.11248) Learning Robust Rewards with Adversarial Inverse Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0633](https://roboticsproceedings.org/rss14/p49.html) Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0634](https://proceedings.mlr.press/v100/lynch20a.html) Learning Latent Plans from Play | ✓ | ✓ | 보→✓ | 오→✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0635](https://proceedings.mlr.press/v100/gupta20a.html) Relay Policy Learning: Solving Long-Horizon Tasks via Imitation and Reinforcement Learning | ✓ | ✓ | 보→✓ | 오→✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0636](https://proceedings.mlr.press/v164/florence22a.html) Implicit Behavioral Cloning | ✓ | ✓ | 보→✓ | 오→✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0637](https://proceedings.mlr.press/v229/mandlekar23a.html) MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0638](https://www.roboticsproceedings.org/rss20/p054.html) Offline Imitation Learning Through Graph Search and Retrieval | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0639](https://www.roboticsproceedings.org/rss21/p023.html) Robot Data Curation with Mutual Information Estimators | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0640](https://www.roboticsproceedings.org/rss21/p025.html) Robot Learning with Super-Linear Scaling | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0641](https://publications.ri.cmu.edu/controllability-of-pushing) Controllability of Pushing | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0642](https://diglib.eg.org/items/5e09458c-a0c5-4899-a46d-2a233b0f82bd) Contact-Invariant Optimization for Hand Manipulation | 오→✓ | ✓ | 보→✓ | 오→✓ | 오→✓ | 오→✓ | 보→? | ? | ? | ✓ |
| [pr-0643](https://api.crossref.org/works/10.1109/ICRA.2014.6907001) Control-Limited Differential Dynamic Programming | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0644](https://www.roboticsproceedings.org/rss14/p58.html) In-Hand Manipulation via Motion Cones | 오→✓ | ✓ | 보→✓ | 오→✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0645](https://openaccess.thecvf.com/content_CVPR_2020/html/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.html) GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | 보→✓ | 보→✓ | ✓ | ✓ |
| [pr-0646](https://api.crossref.org/works/10.1109/icra48506.2021.9561877) Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0647](https://api.crossref.org/works/10.1109/tro.2023.3300230) Global Planning for Contact-Rich Manipulation via Local Smoothing of Quasi-Dynamic Contact Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0648](https://www.roboticsproceedings.org/rss20/p135.html) Tactile-Driven Non-Prehensile Object Manipulation via Extrinsic Contact Mode Control | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0649](https://www.roboticsproceedings.org/rss20/p130.html) RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0650](https://www.roboticsproceedings.org/rss20/p132.html) Towards Tight Convex Relaxations for Contact-Rich Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0651](https://www.roboticsproceedings.org/rss21/p053.html) Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-0652](https://www.roboticsproceedings.org/rss21/p111.html) Complementarity-Free Multi-Contact Modeling and Optimization for Dexterous Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0653](https://api.crossref.org/works/10.1126/scirobotics.aau5872) Learning Agile and Dynamic Motor Skills for Legged Robots | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0654](https://roboticsproceedings.org/rss14/p10.html) Sim-to-Real: Learning Agile Locomotion For Quadruped Robots | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0655](https://arxiv.org/abs/2010.11251) Learning Quadrupedal Locomotion over Challenging Terrain | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0656](https://api.crossref.org/works/10.1126/scirobotics.abk2822) Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0657](https://www.roboticsproceedings.org/rss18/p022.html) Rapid Locomotion via Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0658](https://proceedings.mlr.press/v205/margolis23a.html) Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0659](https://api.crossref.org/works/10.1109/icra48891.2023.10161144) DreamWaQ: Learning Robust Quadrupedal Locomotion with Implicit Terrain Imagination via Deep Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0660](https://roboticsproceedings.org/rss19/p056.html) Demonstrating A Walk in the Park: Learning to Walk in 20 Minutes With Model-Free Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0661](https://api.crossref.org/works/10.1126/scirobotics.adi7566) ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots | ? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0662](https://api.crossref.org/works/10.1109/icra57147.2024.10610200) Extreme Parkour with Legged Robots | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0663](https://www.roboticsproceedings.org/rss21/p122.html) Human2LocoMan: Learning Versatile Quadrupedal Manipulation with Human Pretraining | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0664](https://www.roboticsproceedings.org/rss21/p124.html) SATA: Safe and Adaptive Torque-Based Locomotion Policies Inspired by Animal Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0665](https://www.roboticsproceedings.org/rss21/p125.html) Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0666](https://hal.science/lirmm-00831097) Dynamic Whole-Body Motion Generation under Rigid Contacts and Other Unilateral Constraints | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0667](https://api.crossref.org/works/10.1177/0278364914521306) Hierarchical Quadratic Programming: Fast Online Humanoid-Robot Motion Generation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0668](https://api.crossref.org/works/10.1109/lra.2018.2800124) Whole-Body Nonlinear Model Predictive Control Through Contacts for Quadrupeds | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0669](https://arxiv.org/abs/2311.16098) On Bringing Robots Home | 오→✓ | ✓ | 보→✓ | ✓ | ? | ? | 보→✓ | 보→✓ | 보→✓ | ? |
| [pr-0670](https://www.roboticsproceedings.org/rss20/p091.html) Demonstrating OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0671](https://www.roboticsproceedings.org/rss21/p042.html) RoboPanoptes: The All-Seeing Robot with Whole-body Dexterity | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0672](https://www.roboticsproceedings.org/rss21/p128.html) SafeMimic: Towards Safe and Autonomous Human-to-Robot Imitation for Mobile Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0673](https://www.roboticsproceedings.org/rss21/p033.html) Demonstrating MOSART: Opening Articulated Structures in the Real World | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0674](https://www.roboticsproceedings.org/rss21/p156.html) ArticuBot: Learning Universal Articulated Object Manipulation Policy via Large Scale Simulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0675](https://arxiv.org/abs/1609.06408) Control Barrier Function Based Quadratic Programs for Safety Critical Systems | 오→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0676](https://cdn.openai.com/safexp-short.pdf) Benchmarking Safe Exploration in Deep Reinforcement Learning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0677](https://api.crossref.org/works/10.1109/lra.2021.3070252) Recovery RL: Safe Reinforcement Learning with Learned Recovery Zones | ✓ | ✓ | 보→✓ | 오→✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0678](https://arxiv.org/abs/1803.10122) Recurrent World Models Facilitate Policy Evolution | 오→✓ | 오→✓ | 보→✓ | ✓ | 오→✓ | ? | ? | ? | ? | ? |
| [pr-0679](https://arxiv.org/abs/1811.04551) Learning Latent Dynamics for Planning from Pixels | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0680](https://iclr.cc/static/virtual/data/iclr-2020-orals-posters.json) Dream to Control: Learning Behaviors by Latent Imagination | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0681](https://arxiv.org/abs/2203.04955) Temporal Difference Learning for Model Predictive Control | ✓ | ✓ | 보→✓ | ✓ | 오→✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0682](https://proceedings.mlr.press/v205/wu23c.html) DayDreamer: World Models for Physical Robot Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0683](https://arxiv.org/abs/2301.04104) Mastering diverse control tasks through world models | ✓ | 오→✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0684](https://proceedings.iclr.cc/paper_files/paper/2024/hash/cf73d57b6dcda32b293df7c2d5341f49-Abstract-Conference.html) TD-MPC2: Scalable, Robust World Models for Continuous Control | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ |
| [pr-0685](https://www.roboticsproceedings.org/rss21/p153.html) PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0686](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Dexterous_World_Models_CVPR_2026_paper.html) Dexterous World Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0687](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0ae94013da7cd459402fd77874e09ee3-Abstract-Conference.html) Ctrl-World: A Controllable Generative World Model for Robot Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ |
| [pr-0688](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6605c7d1c1ae1521b328d036df5be1ae-Abstract-Conference.html) WMPO: World Model-based Policy Optimization for Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | 보→✓ | ? | ? |
| [pr-0689](https://proceedings.iclr.cc/paper_files/paper/2026/hash/748becc400a57c0e31cfe6a2e7951467-Abstract-Conference.html) Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0690](https://openaccess.thecvf.com/content/CVPR2026/html/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.html) AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0691](https://openaccess.thecvf.com/content/CVPR2026/html/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.html) ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0692](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_AtomicVLA_Unlocking_the_Potential_of_Atomic_Skill_Learning_in_Robots_CVPR_2026_paper.html) AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0693](https://openaccess.thecvf.com/content/CVPR2026/html/Peng_Counterfactual_VLA_Self-Reflective_Vision-Language-Action_Model_with_Adaptive_Reasoning_CVPR_2026_paper.html) Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0694](https://openaccess.thecvf.com/content/CVPR2026/html/Song_FM-Steer_Enhance_Generalist_Policies_with_Value-Guided_Cascaded_Denoising_CVPR_2026_paper.html) FM-Steer: Enhance Generalist Policies with Value-Guided Cascaded Denoising | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0695](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_CVPR_2026_paper.html) PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0696](https://proceedings.neurips.cc/paper_files/paper/2025/hash/392d0d05e2f514063e6ce6f8b370834c-Abstract-Conference.html) SAFE: Multitask Failure Detection for Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0697](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ad222e6e38e26e3f00d85829b9e02f43-Abstract-Conference.html) Learning to Be Uncertain: Pre-training World Models with Horizon-Calibrated Uncertainty | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0698](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7f5e909ac0324db03506b380c695ffaf-Abstract-Conference.html) WorldGym: World Model as An Environment for Policy Evaluation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0699](https://proceedings.mlr.press/v235/zhou24f.html) RoboDreamer: Learning Compositional World Models for Robot Imagination | 오→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0700](https://proceedings.iclr.cc/paper_files/paper/2024/hash/c4d66eae503694424123b93ac0fbaf17-Abstract-Conference.html) Learning Interactive Real-World Simulators | ? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |

<a id="batch-08"></a>

### 배치 08

| ID · 공식 표제 | 링크 | 제목 | 저자 | 연도 | 발표처·게재 | 요약·기여 | 코드 | 가중치 | 데이터 | 태그 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [pr-0701](https://www.roboticsproceedings.org/rss21/p015.html) Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0702](https://arxiv.org/abs/2501.10100) Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics | ✓ | ✓ | 보→✓ | ✓ | ? | 보→✓ | 보→? | ? | ? | ? |
| [pr-0703](https://api.crossref.org/works/10.1109/LRA.2026.3653273) FlowDreamer: A RGB-D World Model With Flow-Based Motion Representations for Robot Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | 보→✓ | ? | ? |
| [pr-0704](https://computationalrobotics.seas.harvard.edu/GPC/) Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling | ✓ | 오→✓ | 보→✓ | 오→✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0705](https://arxiv.org/abs/2602.15922) World Action Models are Zero-shot Policies | ✓ | ✓ | 보→✓ | ✓ | 오→✓ | 보→✓ | 보→? | ? | ? | ? |
| [pr-0706](https://proceedings.mlr.press/v229/ren23a.html) Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0707](https://www.roboticsproceedings.org/rss18/p042.html) Failure Prediction with Statistical Guarantees for Vision-Based Robot Control | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0708](https://www.roboticsproceedings.org/rss21/p137.html) Dynamic Safety in Complex Environments: Synthesizing Safety Filters with Poisson's Equation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0709](https://www.roboticsproceedings.org/rss20/p066.html) Octopi: Object Property Reasoning with Large Tactile-Language Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0710](https://proceedings.mlr.press/v270/higuera25a.html) Sparsh: Self-supervised touch representations for vision-based tactile sensing | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | 보→✓ | ? | ? |
| [pr-0711](https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Binding_Touch_to_Everything_Learning_Unified_Multimodal_Tactile_Representations_CVPR_2024_paper.html) Binding Touch to Everything: Learning Unified Multimodal Tactile Representations | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0712](https://openaccess.thecvf.com/content/ICCV2021/html/Mo_Where2Act_From_Pixels_to_Actions_for_Articulated_3D_Objects_ICCV_2021_paper.html) Where2Act: From Pixels to Actions for Articulated 3D Objects | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0713](https://openaccess.thecvf.com/content/ICCV2021/html/Gadre_Act_the_Part_Learning_Interaction_Strategies_for_Articulated_Object_Part_ICCV_2021_paper.html) Act the Part: Learning Interaction Strategies for Articulated Object Part Discovery | 오→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0714](https://openaccess.thecvf.com/content/CVPR2022/html/Jiang_Ditto_Building_Digital_Twins_of_Articulated_Objects_From_Interaction_CVPR_2022_paper.html) Ditto: Building Digital Twins of Articulated Objects from Interaction | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | 보→✓ | ? | ? | ? |
| [pr-0715](https://www.roboticsproceedings.org/rss18/p018.html) FlowBot3D: Learning 3D Articulation Flow to Manipulate Articulated Objects | 오→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0716](https://api.crossref.org/works/10.1109/LRA.2022.3142397) Universal Manipulation Policy Network for Articulated Objects | ✓ | 오→✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ |
| [pr-0717](https://proceedings.neurips.cc/paper_files/paper/2023/hash/0e7e2af2e5ba822c9ad35a37b31b5dd4-Abstract-Conference.html) Where2Explore: Few-shot Affordance Learning for Unseen Novel Categories of Articulated Objects | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0718](https://proceedings.mlr.press/v205/huang23c.html) Inner Monologue: Embodied Reasoning through Planning with Language Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0719](https://api.crossref.org/works/10.1109/icra48891.2023.10161317) ProgPrompt: Generating Situated Robot Task Plans using Large Language Models | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | 보→✓ | ? | ? | ? |
| [pr-0720](https://proceedings.mlr.press/v229/rana23a.html) SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-0721](https://arxiv.org/abs/2303.12153) Text2Motion: From Natural Language Instructions to Feasible Plans | ✓ | ✓ | 보→✓ | ✓ | 오→✓ | ? | ? | ? | ? | ? |
| [pr-0722](https://arxiv.org/abs/2304.11477) LLM+P: Empowering Large Language Models with Optimal Planning Proficiency | 오→✓ | ✓ | 보→✓ | ✓ | ? | ? | ✓ | ? | ? | ? |
| [pr-0723](https://arxiv.org/abs/2306.11706) RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | 오→✓ | ? | ? | ? | ? | ? |
| [pr-0724](https://papers.nips.cc/paper_files/paper/2024/hash/e0f393e7980a24fd12fa6f15adfa25fb-Abstract-Conference.html) Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | 보→✓ | ? | ? |
| [pr-0725](https://proceedings.mlr.press/v229/xu23a.html) XSkill: Cross Embodiment Skill Discovery | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0726](https://www.roboticsproceedings.org/rss19/p015.html) AnyTeleop: A General Vision-Based Dexterous Robot Arm-Hand Teleoperation System | 오→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0727](https://proceedings.mlr.press/v229/wang23a.html) MimicPlay: Long-Horizon Imitation Learning by Watching Human Play | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0728](https://arxiv.org/abs/2311.01977) RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches | ✓ | ✓ | 보→✓ | 오→✓ | 오→✓ | ? | ? | ? | ? | ? |
| [pr-0729](https://proceedings.mlr.press/v270/iyer25a.html) OPEN TEACH: A Versatile Teleoperation System for Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0730](https://proceedings.mlr.press/v205/li23a.html) BEHAVIOR-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities and Realistic Simulation | 오→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0731](https://arxiv.org/abs/2406.02523) RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0732](https://www.roboticsproceedings.org/rss20/p120.html) DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ✓ |
| [pr-0733](https://proceedings.mlr.press/v229/walke23a.html) BridgeData V2: A Dataset for Robot Learning at Scale | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0734](https://api.crossref.org/works/10.1109/icra57147.2024.10611615) RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0735](https://www.roboticsproceedings.org/rss19/p041.html) FurnitureBench: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0736](https://www.roboticsproceedings.org/rss18/p035.html) Factory: Fast Contact for Robotic Assembly | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ |
| [pr-0737](https://www.roboticsproceedings.org/rss19/p039.html) IndustReal: Transferring Contact-Rich Assembly Tasks from Simulation to Reality | ? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0738](https://proceedings.mlr.press/v155/lin21a.html) SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0739](https://arxiv.org/abs/2105.03655) FlingBot: The Unreasonable Effectiveness of Dynamic Manipulation for Cloth Unfolding | ✓ | ✓ | 보→✓ | 오→✓ | 오→✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0740](https://arxiv.org/abs/2012.03385) Learning to Rearrange Deformable Cables, Fabrics, and Bags with Goal-Conditioned Transporter Networks | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0741](https://iclr.cc/static/virtual/data/iclr-2022-orals-posters.json) DiffSkill: Skill Abstraction from Differentiable Physics for Deformable Object Manipulations with Tools | 오→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0742](https://www.roboticsproceedings.org/rss18/p017.html) DextAIRity: Deformable Manipulation Can be a Breeze | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0743](https://www.roboticsproceedings.org/rss21/p130.html) Flying Hand: End-Effector-Centric Framework for Versatile Aerial Manipulation Teleoperation and Policy Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0744](https://api.crossref.org/works/10.1109/iros51168.2021.9635867) SurRoL: An Open-source Reinforcement Learning Centered and dVRK Compatible Platform for Surgical Robot Learning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0745](https://iclr.cc/virtual/2023/poster/11309) Flow Matching for Generative Modeling | ? | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | 오→✓ |
| [pr-0746](https://www.roboticsproceedings.org/rss21/p010.html) π0: A Vision-Language-Action Flow Model for General Robot Control | ? | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ |
| [pr-0747](https://proceedings.mlr.press/v164/mandlekar22a.html) What Matters in Learning from Offline Human Demonstrations for Robot Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| [pr-0748](https://ojs.aaai.org/index.php/ICAPS/article/view/6739) PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0749](https://www.roboticsproceedings.org/rss21/p012.html) FAST: Efficient Action Tokenization for Vision-Language-Action Models | ? | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ |
| [pr-0750](https://www.roboticsproceedings.org/rss21/p017.html) Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | ✓ | ? | ✓ |
| [pr-0751](https://www.roboticsproceedings.org/rss21/p052.html) Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | 보→✓ | 보→✓ | ? |
| [pr-0752](https://www.roboticsproceedings.org/rss21/p073.html) Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0753](https://arxiv.org/abs/1909.12271) RLBench: The Robot Learning Benchmark & Learning Environment | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0754](https://proceedings.iclr.cc/paper_files/paper/2025/hash/45c1f6a8cbf2da59ebf2c802b4f742cd-Abstract-Conference.html) SAM 2: Segment Anything in Images and Videos | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0755](https://openaccess.thecvf.com/content/CVPR2024/html/Qin_LangSplat_3D_Language_Gaussian_Splatting_CVPR_2024_paper.html) LangSplat: 3D Language Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0756](https://openaccess.thecvf.com/content/CVPR2024/html/Shi_Language_Embedded_3D_Gaussians_for_Open-Vocabulary_Scene_Understanding_CVPR_2024_paper.html) Language Embedded 3D Gaussians for Open-Vocabulary Scene Understanding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0757](https://openaccess.thecvf.com/content/CVPR2024/html/Koch_Open3DSG_Open-Vocabulary_3D_Scene_Graphs_from_Point_Clouds_with_Queryable_CVPR_2024_paper.html) Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0758](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.html) CLIP-Driven Open-Vocabulary 3D Scene Graph Generation via Cross-Modality Contrastive Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0759](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_EmbodiedScan_A_Holistic_Multi-Modal_3D_Perception_Suite_Towards_Embodied_AI_CVPR_2024_paper.html) EmbodiedScan: A Holistic Multi-Modal 3D Perception Suite Towards Embodied AI | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0760](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_SUGAR_Pre-training_3D_Visual_Representations_for_Robotics_CVPR_2024_paper.html) SUGAR: Pre-training 3D Visual Representations for Robotics | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0761](https://openaccess.thecvf.com/content/CVPR2024/html/Ryu_Diffusion-EDFs_Bi-equivariant_Denoising_Generative_Modeling_on_SE3_for_Visual_Robotic_CVPR_2024_paper.html) Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling on SE(3) for Visual Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0762](https://openaccess.thecvf.com/content/CVPR2024/html/Ma_Hierarchical_Diffusion_Policy_for_Kinematics-Aware_Multi-Task_Robotic_Manipulation_CVPR_2024_paper.html) Hierarchical Diffusion Policy for Kinematics-Aware Multi-Task Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0763](https://openaccess.thecvf.com/content/CVPR2024/html/Ni_Generate_Subgoal_Images_before_Act_Unlocking_the_Chain-of-Thought_Reasoning_in_CVPR_2024_paper.html) Generate Subgoal Images before Act: Unlocking the Chain-of-Thought Reasoning in Diffusion Model for Robot Manipulation with Multimodal Prompts | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0764](https://openaccess.thecvf.com/content/CVPR2024/html/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.html) ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0765](https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.html) Holodeck: Language Guided Generation of 3D Embodied AI Environments | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0766](https://openaccess.thecvf.com/content/CVPR2024/html/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.html) MultiPLY: A Multisensory Object-Centric Embodied Large Language Model in 3D World | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0767](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_Lookahead_Exploration_with_Neural_Radiance_Representation_for_Continuous_Vision-Language_Navigation_CVPR_2024_paper.html) Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0768](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Volumetric_Environment_Representation_for_Vision-Language_Navigation_CVPR_2024_paper.html) Volumetric Environment Representation for Vision-Language Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0769](https://openaccess.thecvf.com/content/CVPR2024/html/Yan_GS-SLAM_Dense_Visual_SLAM_with_3D_Gaussian_Splatting_CVPR_2024_paper.html) GS-SLAM: Dense Visual SLAM with 3D Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0770](https://openaccess.thecvf.com/content/CVPR2024/html/Yang_RegionPLC_Regional_Point-Language_Contrastive_Learning_for_Open-World_3D_Scene_Understanding_CVPR_2024_paper.html) RegionPLC: Regional Point-Language Contrastive Learning for Open-World 3D Scene Understanding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0771](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Towards_CLIP-driven_Language-free_3D_Visual_Grounding_via_2D-3D_Relational_Enhancement_CVPR_2024_paper.html) Towards CLIP-driven Language-free 3D Visual Grounding via 2D-3D Relational Enhancement and Consistency | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0772](https://openaccess.thecvf.com/content/CVPR2025/html/Song_RoboSpatial_Teaching_Spatial_Understanding_to_2D_and_3D_Vision-Language_Models_CVPR_2025_paper.html) RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0773](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.html) CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0774](https://openaccess.thecvf.com/content/CVPR2025/html/Tian_PDFactor_Learning_Tri-Perspective_View_Policy_Diffusion_Field_for_Multi-Task_Robotic_CVPR_2025_paper.html) PDFactor: Learning Tri-Perspective View Policy Diffusion Field for Multi-Task Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0775](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_ReasonGrounder_LVLM-Guided_Hierarchical_Feature_Splatting_for_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.html) ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0776](https://openaccess.thecvf.com/content/CVPR2025/html/Jun-Seong_Dr._Splat_Directly_Referring_3D_Gaussian_Splatting_via_Direct_Language_CVPR_2025_paper.html) Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0777](https://openaccess.thecvf.com/CVPR2025?day=all) Chain of Semantics Programming in 3D Gaussian Splatting Representation for 3D Vision Grounding | ? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0778](https://openaccess.thecvf.com/content/CVPR2025/html/Li_SeeGround_See_and_Ground_for_Zero-Shot_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.html) SeeGround: See and Ground for Zero-Shot Open-Vocabulary 3D Visual Grounding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0779](https://openaccess.thecvf.com/content/CVPR2025/html/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.html) RoboGround: Robotic Manipulation with Grounded Vision-Language Priors | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0780](https://openaccess.thecvf.com/content/CVPR2025/html/Jia_Lift3D_Policy_Lifting_2D_Foundation_Models_for_Robust_3D_Robotic_CVPR_2025_paper.html) Lift3D Policy: Lifting 2D Foundation Models for Robust 3D Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0781](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Object-Centric_Prompt-Driven_Vision-Language-Action_Model_for_Robotic_Manipulation_CVPR_2025_paper.html) Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0782](https://openaccess.thecvf.com/content/CVPR2025/html/Ma_SpatialLLM_A_Compound_3D-Informed_Design_towards_Spatially-Intelligent_Large_Multimodal_Models_CVPR_2025_paper.html) SpatialLLM: A Compound 3D-Informed Design towards Spatially-Intelligent Large Multimodal Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0783](https://openaccess.thecvf.com/content/WACV2025/html/Wang_AIDE_Improving_3D_Open-Vocabulary_Semantic_Segmentation_by_Aligned_Vision-Language_Learning_WACV_2025_paper.html) AIDE: Improving 3D Open-Vocabulary Semantic Segmentation by Aligned Vision-Language Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0784](https://openaccess.thecvf.com/content/WACV2025/html/Fu_Scene-LLM_Extending_Language_Model_for_3D_Visual_Reasoning_WACV_2025_paper.html) Scene-LLM: Extending Language Model for 3D Visual Reasoning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0785](https://openaccess.thecvf.com/content/ICCV2025/html/Gao_3D_Gaussian_Map_with_Open-Set_Semantic_Grouping_for_Vision-Language_Navigation_ICCV_2025_paper.html) 3D Gaussian Map with Open-Set Semantic Grouping for Vision-Language Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0786](https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_Move_to_Understand_a_3D_Scene_Bridging_Visual_Grounding_and_ICCV_2025_paper.html) Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0787](https://openaccess.thecvf.com/content/ICCV2025/html/Hou_Dita_Scaling_Diffusion_Transformer_for_Generalist_Vision-Language-Action_Policy_ICCV_2025_paper.html) Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0788](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Robotics_Manipulation_with_Long-Horizon_ICCV_2025_paper.html) VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0789](https://openaccess.thecvf.com/content/ICCV2025/html/Lu_GWM_Towards_Scalable_Gaussian_World_Models_for_Robotic_Manipulation_ICCV_2025_paper.html) GWM: Towards Scalable Gaussian World Models for Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0790](https://openaccess.thecvf.com/content/ICCV2025/html/Li_SceneSplat_Gaussian_Splatting-based_Scene_Understanding_with_Vision-Language_Pretraining_ICCV_2025_paper.html) SceneSplat: Gaussian Splatting-based Scene Understanding with Vision-Language Pretraining | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0791](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_AutoOcc_Automatic_Open-Ended_Semantic_Occupancy_Annotation_via_Vision-Language_Guided_Gaussian_ICCV_2025_paper.html) AutoOcc: Automatic Open-Ended Semantic Occupancy Annotation via Vision-Language Guided Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0792](https://openaccess.thecvf.com/content/ICCV2025/html/Zemskova_3DGraphLLM_Combining_Semantic_Graphs_and_Large_Language_Models_for_3D_ICCV_2025_paper.html) 3DGraphLLM: Combining Semantic Graphs and Large Language Models for 3D Scene Understanding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | 보→✓ | ? | ? |
| [pr-0793](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_D3D-VLP_Dynamic_3D_Vision-Language-Planning_Model_for_Embodied_Grounding_and_Navigation_CVPR_2026_paper.html) D3D-VLP: Dynamic 3D Vision-Language-Planning Model for Embodied Grounding and Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0794](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_EmbodiedSplat_Online_Feed-Forward_Semantic_3DGS_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2026_paper.html) EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0795](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.html) ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0796](https://openaccess.thecvf.com/content/CVPR2026/html/Li_ConsisVLA-4D_Advancing_Spatiotemporal_Consistency_in_Efficient_3D-Perception_and_4D-Reasoning_for_CVPR_2026_paper.html) ConsisVLA-4D: Advancing Spatiotemporal Consistency in Efficient 3D-Perception and 4D-Reasoning for Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0797](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_Localizing_Structuring_and_Rendering_Bridging_3D_and_2D_Vision-Language-Action_Models_CVPR_2026_paper.html) Localizing, Structuring, and Rendering: Bridging 3D and 2D Vision-Language-Action Models for Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | 보→✓ | ? | ? | ? |
| [pr-0798](https://openaccess.thecvf.com/content/CVPR2026/html/Hu_G2VLM_Geometry_Grounded_Vision_Language_Model_with_Unified_3D_Reconstruction_CVPR_2026_paper.html) G$^2$VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0799](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_MSGNav_Unleashing_the_Power_of_Multi-modal_3D_Scene_Graph_for_CVPR_2026_paper.html) MSGNav: Unleashing the Power of Multi-modal 3D Scene Graph for Zero-Shot Embodied Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0800](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.html) SpatialStack: Layered Geometry-Language Fusion for 3D VLM Spatial Reasoning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |

<a id="batch-09"></a>

### 배치 09

| ID · 공식 표제 | 링크 | 제목 | 저자 | 연도 | 발표처·게재 | 요약·기여 | 코드 | 가중치 | 데이터 | 태그 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [pr-0801](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_GA-VLN_Geometry-Aware_BEV_Representation_for_Efficient_Vision-Language_Navigation_CVPR_2026_paper.html) GA-VLN: Geometry-Aware BEV Representation for Efficient Vision-Language Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0802](https://openaccess.thecvf.com/content/CVPR2026/html/Cheng_Grounded_3D-Aware_Spatial_Vision-Language_Modeling_CVPR_2026_paper.html) Grounded 3D-Aware Spatial Vision-Language Modeling | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0803](https://openaccess.thecvf.com/content/CVPR2026/html/Ni_SemanticVLA_Towards_Semantic_Reasoning_over_Action_Memorization_via_Synergistic_Explicit_CVPR_2026_paper.html) SemanticVLA: Towards Semantic Reasoning over Action Memorization via Synergistic Explicit Trace and Latent Action Planning | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0804](https://openaccess.thecvf.com/content/CVPR2026/html/Zhong_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models_CVPR_2026_paper.html) ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0805](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SaPaVe_Towards_Active_Perception_and_Manipulation_in_Vision-Language_Action_Models_CVPR_2026_paper.html) SaPaVe: Towards Active Perception and Manipulation in Vision-Language Action Models for Robotics | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0806](https://openaccess.thecvf.com/content/CVPR2026/html/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.html) OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0807](https://openaccess.thecvf.com/content/CVPR2026/html/Bang_LightSplat_Fast_and_Memory-Efficient_Open-Vocabulary_3D_Scene_Understanding_in_Five_CVPR_2026_paper.html) LightSplat: Fast and Memory-Efficient Open-Vocabulary 3D Scene Understanding in Five Seconds | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0808](https://openaccess.thecvf.com/content/CVPR2026/html/Ye_LangRef3DGS_Natural_Language-Guided_3D_Referential_Segmentation_from_Partial_Observations_via_CVPR_2026_paper.html) LangRef3DGS: Natural Language-Guided 3D Referential Segmentation from Partial Observations via 3D Gaussian Splatting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0809](https://openaccess.thecvf.com/content/CVPR2026/html/Li_RealVLG-R1_A_Large-Scale_Real-World_Visual-Language_Grounding_Benchmark_for_Robotic_Perception_CVPR_2026_paper.html) RealVLG-R1: A Large-Scale Real-World Visual-Language Grounding Benchmark for Robotic Perception and Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ✓ |
| [pr-0810](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SIMPACT_Simulation-Enabled_Action_Planning_using_Vision-Language_Models_CVPR_2026_paper.html) SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0811](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_DiffuView_Multi-View_Diffusion_Pretraining_for_3D_Aware_Robotic_Manipulation_CVPR_2026_paper.html) DiffuView: Multi-View Diffusion Pretraining for 3D Aware Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0812](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_FLARE_A_Failure-Aware_Framework_for_Autonomous_Correction_and_Recovery_in_CVPR_2026_paper.html) FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0813](https://icml.cc/virtual/2026/poster/64203) Can VLMs Diagnose and Recover from VLA Manipulation Faults? | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0814](https://icml.cc/virtual/2026/poster/61388) VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0815](https://icml.cc/virtual/2026/poster/65669) Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0816](https://proceedings.mlr.press/v306/francis-meretzki26a.html) Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ |
| [pr-0817](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention_CVPR_2026_paper.html) AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0818](https://www.roboticsproceedings.org/rss22/p006.html) TactAlign: Human-to-Robot Policy Transfer via Tactile Alignment | 오→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0819](https://www.roboticsproceedings.org/rss22/p010.html) Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control | 오→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0820](https://www.roboticsproceedings.org/rss21/p103.html) DexterityGen: Foundation Controller for Unprecedented Dexterity | 오→✓ | ✓ | 보→✓ | 오→✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0821](https://api.crossref.org/works/10.1016/S0004-3702(98)00023-X) Planning and Acting in Partially Observable Stochastic Domains | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0822](https://api.crossref.org/works/10.1109/TSSC.1968.300136) A Formal Basis for the Heuristic Determination of Minimum Cost Paths | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0823](https://api.crossref.org/works/10.1115/1.3662552) A New Approach to Linear Filtering and Prediction Problems | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0824](https://api.crossref.org/works/10.1115/1.3139652) Hybrid Position/Force Control of Manipulators | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0825](https://api.crossref.org/works/10.1115/1.3140702) Impedance Control: An Approach to Manipulation: Part I—Theory | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-0826](https://api.crossref.org/works/10.1109/34.121791) A Method for Registration of 3-D Shapes | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0827](https://api.crossref.org/works/10.1109/ROBOT.1992.219918) Planning Optimal Grasps | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0828](https://api.crossref.org/works/10.1109/ROBOT.2003.1241826) Biped Walking Pattern Generation by using Preview Control of Zero-Moment Point | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0829](https://api.crossref.org/works/10.1109/ICRA.2011.5980391) Hierarchical Task and Motion Planning in the Now | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0830](https://icml.cc/2011/papers/323_icmlpaper.pdf) PILCO: A Model-Based and Data-Efficient Approach to Policy Search | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0831](https://api.crossref.org/works/10.1109/IROS.2012.6386109) MuJoCo: A Physics Engine for Model-Based Control | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0832](https://www.ijcai.org/Proceedings/15/Papers/274.pdf) Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning | ? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0833](https://api.crossref.org/works/10.1109/icra.2017.7989202) Information Theoretic MPC for Model-Based Reinforcement Learning | ? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0834](https://api.crossref.org/works/10.1177/0278364917739114) FFRob: Leveraging Symbolic Planning for Efficient Task and Motion Planning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0835](https://doi.org/10.1007/BF00115009) Learning to Predict by the Methods of Temporal Differences | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | 오→✓ |
| [pr-0836](https://doi.org/10.1007/BF00992698) Q-Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0837](https://doi.org/10.1007/BF00992696) Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0838](https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html) Policy Gradient Methods for Reinforcement Learning with Function Approximation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-0839](https://proceedings.neurips.cc/paper_files/paper/2022/hash/90d17e882adbdda42349db6f50123817-Abstract-Conference.html) Behavior Transformers: Cloning k modes with one stone | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | 보→✓ | ? | ? | ? |
| [pr-0840](https://proceedings.mlr.press/v87/florence18a.html) Dense Object Nets: Learning Dense Visual Object Descriptors By and For Robotic Manipulation | 오→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0841](https://arxiv.org/abs/2203.06173) Masked Visual Pre-training for Motor Control | 오→✓ | ✓ | 보→✓ | ✓ | ? | 보→✓ | ? | ? | ? | ? |
| [pr-0842](https://proceedings.mlr.press/v205/nair23a.html) R3M: A Universal Visual Representation for Robot Manipulation | ? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0843](https://arxiv.org/abs/2303.18240) Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence? | ✓ | ✓ | 보→✓ | ✓ | 오→✓ | ? | ? | ? | ? | ? |
| [pr-0844](https://proceedings.mlr.press/v100/yu20a.html) Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0845](https://proceedings.mlr.press/v100/dasari20a.html) RoboNet: Large-Scale Multi-Robot Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0846](https://arxiv.org/abs/2009.12293) robosuite: A Modular Simulation Framework and Benchmark for Robot Learning | ✓ | ✓ | 보→✓ | ✓ | ? | 보→✓ | ? | ? | ? | ? |
| [pr-0847](https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/hash/eda80a3d5b344bc40f3bc04f65b7a357-Abstract-round2.html) ManiSkill: Generalizable Manipulation Skill Benchmark with Large-Scale Demonstrations | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0848](https://api.crossref.org/works/10.3390/s17122762) GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0849](https://api.crossref.org/works/10.1109/LRA.2020.2977257) DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0850](https://api.crossref.org/works/10.1109/LRA.2022.3146945) TACTO: A Fast, Flexible, and Open-source Simulator for High-Resolution Vision-based Tactile Sensors | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0851](https://xbpeng.github.io/projects/AMP/) AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0852](https://openaccess.thecvf.com/content/ICCV2023/html/Luo_Perpetual_Humanoid_Control_for_Real-time_Simulated_Avatars_ICCV_2023_paper.html) Perpetual Humanoid Control for Real-time Simulated Avatars | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0853](https://doi.org/10.1038/nature14236) Human-level control through deep reinforcement learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0854](https://proceedings.mlr.press/v48/mniha16.html) Asynchronous Methods for Deep Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0855](https://arxiv.org/abs/1806.06920) Maximum a Posteriori Policy Optimisation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ? |
| [pr-0856](https://arxiv.org/abs/2104.08212) MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-0857](https://arxiv.org/abs/2205.06175) A Generalist Agent | ✓ | ✓ | 보→✓ | ✓ | 오→✓ | ? | ? | ? | ? | ? |
| [pr-0858](https://arxiv.org/abs/2401.12963) AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents | 보→✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-0859](https://www.roboticsproceedings.org/rss20/p049.html) RT-H: Action Hierarchies Using Language | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0860](https://arxiv.org/abs/2503.20020) Gemini Robotics: Bringing AI into the Physical World | ✓ | ✓ | 보→✓ | ✓ | ? | 보→✓ | ? | ? | ? | ? |
| [pr-0861](https://arxiv.org/abs/2108.10470) Isaac Gym: High Performance GPU Based Physics Simulation For Robot Learning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0862](https://api.crossref.org/works/10.1109/LRA.2023.3270034) Orbit: A Unified Simulation Framework for Interactive Robot Learning Environments | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0863](https://arxiv.org/abs/2511.04831) Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning | ✓ | ✓ | 보→✓ | ✓ | ? | 오→✓ | ? | ? | ? | ✓ |
| [pr-0864](https://proceedings.iclr.cc/paper_files/paper/2024/hash/70c26937fbf3d4600b69a129031b66ec-Abstract-Conference.html) Eureka: Human-Level Reward Design via Coding Large Language Models | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0865](https://www.roboticsproceedings.org/rss20/p094.html) DrEureka: Language Model Guided Sim-To-Real Transfer | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0866](https://arxiv.org/abs/2210.13702) DeXtreme: Transfer of Agile In-hand Manipulation from Simulation to Reality | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0867](https://arxiv.org/abs/2409.14393) MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0868](https://api.crossref.org/works/10.1109/icra55743.2025.11128549) HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0869](https://arxiv.org/abs/2503.14734) NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid Robots | ? | ✓ | 보→✓ | ✓ | ? | ? | ? | 보→✓ | ? | ? |
| [pr-0870](https://proceedings.mlr.press/v305/jang25a.html) DreamGen: Unlocking Generalization in Robot Learning through Video World Models | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0871](https://proceedings.mlr.press/v306/gao26q.html) DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ |
| [pr-0872](https://api.crossref.org/works/10.1126/scirobotics.aed4592) SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? |
| [pr-0873](https://www.roboticsproceedings.org/rss20/p045.html) Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ |
| [pr-0874](https://api.crossref.org/works/10.1109/ICRA57147.2024.10610040) SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-0875](https://api.crossref.org/works/10.1109/ICRA57147.2024.10610421) Robot Fine-Tuning Made Easy: Pre-Training Rewards and Policies for Autonomous Real-World Reinforcement Learning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0876](https://www.roboticsproceedings.org/rss21/p002.html) Demonstrating ViSafe: Vision-enabled Safety for High-speed Detect and Avoid | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0877](https://www.roboticsproceedings.org/rss21/p001.html) Learned Perceptive Forward Dynamics Model for Safe and Platform-aware Robotic Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0878](https://www.roboticsproceedings.org/rss21/p007.html) Certifiably-Correct Mapping for Safe Navigation Despite Odometry Drift | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0879](https://www.roboticsproceedings.org/rss21/p008.html) Kinodynamic Trajectory Following with STELA: Simultaneous Trajectory Estimation & Local Adaptation | 오→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→? | ? | ? | ? |
| [pr-0880](https://www.roboticsproceedings.org/rss21/p011.html) SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | 보→✓ | ? | ? |
| [pr-0881](https://www.roboticsproceedings.org/rss21/p013.html) Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | 보→✓ | ? | ? |
| [pr-0882](https://www.roboticsproceedings.org/rss21/p014.html) Learning to Act Anywhere with Task-centric Latent Actions | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0883](https://www.roboticsproceedings.org/rss21/p016.html) CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0884](https://www.roboticsproceedings.org/rss21/p018.html) NaVILA: Legged Robot Vision-Language-Action Model for Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| [pr-0885](https://www.roboticsproceedings.org/rss21/p019.html) ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-0886](https://www.roboticsproceedings.org/rss21/p028.html) RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ |
| [pr-0887](https://www.roboticsproceedings.org/rss21/p021.html) Demonstrating GPU Parallelized Robot Simulation and Rendering for Generalizable Embodied AI with ManiSkill3 | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0888](https://www.roboticsproceedings.org/rss21/p022.html) RoboVerse: A Unified Platform, Benchmark and Dataset for Scalable and Generalizable Robot Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0889](https://www.roboticsproceedings.org/rss21/p034.html) Vysics: Object Reconstruction Under Occlusion by Fusing Vision and Contact-Rich Physics | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0890](https://www.roboticsproceedings.org/rss21/p036.html) Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0891](https://www.roboticsproceedings.org/rss21/p039.html) Map Space Belief Prediction for Manipulation-Enhanced Mapping | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0892](https://www.roboticsproceedings.org/rss21/p037.html) V-HOP: Visuo-Haptic 6D Object Pose Tracking | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0893](https://www.roboticsproceedings.org/rss21/p056.html) PP-Tac: Paper Picking Using Omnidirectional Tactile Feedback in Dexterous Robotic Hands | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0894](https://www.roboticsproceedings.org/rss21/p057.html) GeoDEx: A Unified Geometric Framework for Tactile Dexterous and Extrinsic Manipulation under Force Uncertainty | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0895](https://www.roboticsproceedings.org/rss21/p059.html) Demonstrating REASSEMBLE: A Multimodal Dataset for Contact-rich Robotic Assembly and Disassembly | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0896](https://www.roboticsproceedings.org/rss21/p060.html) Robust Peg-in-Hole Assembly under Uncertainties via Compliant and Interactive Contact-Rich Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0897](https://www.roboticsproceedings.org/rss21/p072.html) CodeDiffuser: Attention-Enhanced Diffusion Policy via VLM-Generated Code for Instruction Ambiguity | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0898](https://www.roboticsproceedings.org/rss21/p074.html) Unified Video Action Model | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0899](https://www.roboticsproceedings.org/rss21/p075.html) DexWild: Dexterous Human Interactions for In-the-Wild Robot Policies | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0900](https://www.roboticsproceedings.org/rss21/p076.html) From Foresight to Forethought: VLM-In-the-Loop Policy Steering via Latent Alignment | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |

<a id="batch-10"></a>

### 배치 10

| ID · 공식 표제 | 링크 | 제목 | 저자 | 연도 | 발표처·게재 | 요약·기여 | 코드 | 가중치 | 데이터 | 태그 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [pr-0901](https://www.roboticsproceedings.org/rss21/p079.html) FACTR: Force-Attending Curriculum Training for Contact-Rich Policy Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0902](https://www.roboticsproceedings.org/rss21/p106.html) Dex1B: Learning with 1B Demonstrations for Dexterous Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0903](https://www.roboticsproceedings.org/rss21/p109.html) Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0904](https://www.roboticsproceedings.org/rss21/p110.html) CordViP: Correspondence-based Visuomotor Policy for Dexterous Manipulation in Real-World | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | 보→✓ | ? | ? |
| [pr-0905](https://www.roboticsproceedings.org/rss21/p145.html) Prompting with the Future: Open-World Model Predictive Control with Interactive Digital Twins | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0906](https://www.roboticsproceedings.org/rss21/p146.html) Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0907](https://www.roboticsproceedings.org/rss21/p148.html) PartInstruct: Part-level Instruction Following for Fine-grained Robot Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0908](https://www.roboticsproceedings.org/rss21/p149.html) You Only Teach Once: Learn One-Shot Bimanual Robotic Manipulation from Video Demonstrations | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | 보→✓ | ? | ? |
| [pr-0909](https://www.roboticsproceedings.org/rss21/p150.html) Manual2Skill: Learning to Read Manuals and Acquire Robotic Skills for Furniture Assembly Using Vision-Language Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0910](https://www.roboticsproceedings.org/rss21/p152.html) RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation | 오→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0911](https://www.roboticsproceedings.org/rss21/p155.html) Bridging Perception and Action: Spatially-Grounded Mid-Level Representations for Robot Generalization | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0912](https://www.roboticsproceedings.org/rss21/p157.html) DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0913](https://api.crossref.org/works/10.1109/iros60139.2025.11247088) AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0914](https://api.crossref.org/works/10.1126/scirobotics.ads5033) Precise and dexterous robotic manipulation via human-in-the-loop reinforcement learning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0915](https://arxiv.org/abs/2506.01844) SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | ✓ | ✓ | 보→✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ |
| [pr-0916](https://arxiv.org/abs/2510.03342) Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-0917](https://research.nvidia.com/labs/gear/gr00t-n1_5/) GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | 보→✓ | ? | ? |
| [pr-0918](https://research.nvidia.com/labs/gear/gr00t-n1_6/) GR00T N1.6: An Improved Open Foundation Model for Generalist Humanoid Robots | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | 보→✓ | ? | ? |
| [pr-0919](https://ojs.aaai.org/index.php/AAAI/article/view/38947) Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0920](https://ojs.aaai.org/index.php/AAAI/article/view/38919) MP1: MeanFlow Tames Policy Learning in 1-step for Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0921](https://ojs.aaai.org/index.php/AAAI/article/view/34866) Self-Correcting Robot Manipulation via Gaussian-Splatted Foresight | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0922](https://ojs.aaai.org/index.php/AAAI/article/view/33613) Neural Assembler: Learning to Generate Fine-Grained Robotic Assembly Instructions from Multi-View Images | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0923](https://ojs.aaai.org/index.php/AAAI/article/view/33610) Instruction-Augmented Long-Horizon Planning: Embedding Grounding Mechanisms in Embodied Mobile Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0924](https://ojs.aaai.org/index.php/AAAI/article/view/33617) FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0925](https://proceedings.mlr.press/v202/ball23a.html) Efficient Online Reinforcement Learning with Offline Data | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ✓ |
| [pr-0926](https://www.roboticsproceedings.org/rss20/p067.html) 3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ |
| [pr-0927](https://proceedings.mlr.press/v229/shah23a.html) ViNT: A Foundation Model for Visual Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ? | ? | ? | ✓ |
| [pr-0928](https://www.roboticsproceedings.org/rss20/p073.html) GOAT: GO to Any Thing | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0929](https://www.roboticsproceedings.org/rss20/p118.html) Partially Observable Task and Motion Planning with Uncertainty and Risk Awareness | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0930](https://www.roboticsproceedings.org/rss20/p071.html) Consistency Policy: Accelerated Visuomotor Policies via Consistency Distillation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0931](https://www.roboticsproceedings.org/rss20/p048.html) Diffusion Meets DAgger: Supercharging Eye-in-hand Imitation Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0932](https://www.roboticsproceedings.org/rss20/p092.html) Any-point Trajectory Modeling for Policy Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0933](https://www.roboticsproceedings.org/rss20/p069.html) MIRAGE: Cross-Embodiment Zero-Shot Policy Transfer with Cross-Painting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0934](https://www.roboticsproceedings.org/rss20/p093.html) Pushing the Limits of Cross-Embodiment Learning for Manipulation and Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0935](https://proceedings.iclr.cc/paper_files/paper/2024/hash/71639c317fb0bf398835627b4418693e-Abstract-Conference.html) Vision-Language Foundation Models as Effective Robot Imitators | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | 보→✓ | ? | ? |
| [pr-0936](https://proceedings.iclr.cc/paper_files/paper/2024/hash/2c37c5bcef24b9541550261dcd63261b-Abstract-Conference.html) Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0937](https://proceedings.neurips.cc/paper_files/paper/2024/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html) RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0938](https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html) Latent Action Pretraining from Videos | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0939](https://proceedings.mlr.press/v235/zhen24a.html) 3D-VLA: A 3D Vision-Language-Action Generative World Model | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ |
| [pr-0940](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8e6f3d53b2bef98fce17e699557f5f11-Abstract-Conference.html) VLMimic: Vision Language Models are Visual Imitation Learner for Fine-grained Actions | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0941](https://proceedings.mlr.press/v270/li25c.html) Evaluating Real-World Robot Manipulation Policies in Simulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | 보→✓ | ? |
| [pr-0942](https://www.roboticsproceedings.org/rss20/p002.html) Parallel and Proximal Linear-Quadratic Methods for Real-Time Constrained Model-Predictive Control | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0943](https://www.roboticsproceedings.org/rss20/p003.html) Differentiable Robust Model Predictive Control | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0944](https://www.roboticsproceedings.org/rss20/p110.html) Linear-time Differential Inverse Kinematics: an Augmented Lagrangian Perspective | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0945](https://api.crossref.org/works/10.1109/TRO.2018.2853729) VINS-Mono: A Robust and Versatile Monocular Visual-Inertial State Estimator | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0946](https://api.crossref.org/works/10.1109/IROS45743.2020.9341176) LIO-SAM: Tightly-coupled Lidar Inertial Odometry via Smoothing and Mapping | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0947](https://arxiv.org/abs/2107.06829) FAST-LIO2: Fast Direct LiDAR-inertial Odometry | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0948](https://proceedings.neurips.cc/paper_files/paper/2021/hash/021bbc7ee20b71134d53e20206bd6feb-Abstract.html) Habitat 2.0: Training Home Assistants to Rearrange their Habitat | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ |
| [pr-0949](https://proceedings.iclr.cc/paper_files/paper/2024/hash/430894999584d0bd358611e2ecf00b15-Abstract-Conference.html) Habitat 3.0: A Co-Habitat for Humans, Avatars, and Robots | ? | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0950](https://openaccess.thecvf.com/content_CVPR_2020/html/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.html) SAPIEN: A SimulAted Part-Based Interactive ENvironment | ? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0951](https://proceedings.iclr.cc/paper_files/paper/2025/hash/c0749c39aaff9e9e4c91f7118bf21b1e-Abstract-Conference.html) Diffusion Policy Policy Optimization | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ |
| [pr-0952](https://proceedings.mlr.press/v267/park25f.html) Flow Q-Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ |
| [pr-0953](https://proceedings.neurips.cc/paper_files/paper/2025/hash/50348e8f9aef984abe0ea1ec2a326f78-Abstract-Conference.html) Reinforcement Learning with Action Chunking | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0954](https://proceedings.iclr.cc/paper_files/paper/2026/hash/eafa5259d9eabb1b501592475dbc82dd-Abstract-Conference.html) Decoupled Q-Chunking | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0955](https://proceedings.mlr.press/v305/wagenmaker25a.html) Steering Your Diffusion Policy with Latent Space Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0956](https://proceedings.nips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html) What Can RL Bring to VLA Generalization? An Empirical Study | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0957](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html) SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0958](https://www.roboticsproceedings.org/rss22/p089.html) RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0959](https://api.crossref.org/works/10.1126/scirobotics.aed6267) Performant robotic manipulation with real-world reinforcement learning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | 보→✓ | ? |
| [pr-0960](https://proceedings.mlr.press/v306/guo26i.html) VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0961](https://proceedings.mlr.press/v306/zhang26ez.html) Towards Practical World Model-based Reinforcement Learning for Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ |
| [pr-0962](https://roboticsproceedings.org/rss22/p012.html) Self-Improving Robot Policy with Compositional World Model | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0963](https://roboticsproceedings.org/rss20/p079.html) NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | 보→✓ | ? | ? |
| [pr-0964](https://api.crossref.org/works/10.1109/icra57385.2026.11696748) NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0965](https://api.crossref.org/works/10.1109/icra57385.2026.11696190) StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | 보→✓ | ? | ? |
| [pr-0966](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_SocialNav_Training_Human-Inspired_Foundation_Model_for_Socially-Aware_Embodied_Navigation_CVPR_2026_paper.html) SocialNav: Training Human-Inspired Foundation Model for Socially-Aware Embodied Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-0967](https://api.crossref.org/works/10.1109/icra57385.2026.11696935) LoGoPlanner: Localization Grounded Navigation Policy with Metric-aware Visual Geometry | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | 보→✓ | ? | ? |
| [pr-0968](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_PointWorld_Scaling_3D_World_Models_for_In-The-Wild_Robotic_Manipulation_CVPR_2026_paper.html) PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | 보→✓ | ? | ? |
| [pr-0969](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ecd92623ac899357312aaa8915853699-Abstract-Conference.html) OGBench: Benchmarking Offline Goal-Conditioned RL | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0970](https://www.roboticsproceedings.org/rss22/p098.html) OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ✓ |
| [pr-0971](https://roboticsproceedings.org/rss22/p037.html) USER: A Unified and Extensible System for Online Real-World Policy Learning in Embodied AI | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0972](https://proceedings.mlr.press/v306/lin26af.html) DyGRO-VLA: Cross-Task Scaling of Vision–Language–Action Models via Dynamic Grouped Residual Optimization | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0973](https://arxiv.org/abs/2603.28475) Tac2Real: Reliable and GPU Visuotactile Simulation for Online Reinforcement Learning and Zero-Shot Real-World Deployment | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0974](https://arxiv.org/abs/2603.25685) Persistent Robot World Models: Stabilizing Multi-Step Rollouts via Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0975](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_MoManipVLA_Transferring_Vision-language-action_Models_for_General_Mobile_Manipulation_CVPR_2025_paper.html) MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0976](https://www.roboticsproceedings.org/rss22/p004.html) Semantic Contact Fields for Category-Level Generalizable Tool Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-0977](https://www.roboticsproceedings.org/rss22/p147.html) DISC: Decoupling Instruction from State-Conditioned Control via Policy Generation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | 보→✓ | ? | ? |
| [pr-0978](https://www.roboticsproceedings.org/rss22/p141.html) Contact-Anchored Policies: Contact Conditioning Creates Strong Robot Utility Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0979](https://arxiv.org/abs/2608.03052) How Should Vision-Language-Action Models Use Proprioceptive State? | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-0980](https://arxiv.org/abs/2609.30092) Self-Adaptive VLA for Robust Robot Deployment | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-0981](https://arxiv.org/abs/2601.16667) ReViP: Mitigating False Completion in Vision-Language-Action Models with Vision-Proprioception Rebalance | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ✓ |
| [pr-0982](https://arxiv.org/abs/2607.03693) CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts | ✓ | ✓ | 보→✓ | ✓ | 오→✓ | ? | ? | ? | ? | ? |
| [pr-0983](https://arxiv.org/abs/2609.37150) CoRe-VLA: Preserving Cross-View Coordination in VLAs under Camera Shifts | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-0984](https://arxiv.org/abs/2610.18843) LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-0985](https://arxiv.org/abs/2506.03574) SwitchVLA: Execution-Aware Task Switching for Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-0986](https://arxiv.org/abs/2510.21817) VITA-E: Natural Embodied Interaction with Concurrent Seeing, Hearing, Speaking, and Acting | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ✓ | 보→✓ | ? | ✓ |
| [pr-0987](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ff7373914a96956f2a7cacbdf3b0b8d8-Abstract-Conference.html) WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control | 오→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-0988](https://jjjenghi.github.io/dialogvla/static/paper/DialogVLA.pdf) DialogVLA: Bridging Reasoning Action in Bimanual Manipulation via Parallel Mixture-of-Experts | 보→✓ | ✓ | 보→✓ | ✓ | 오→✓ | ? | ? | ? | ? | ? |
| [pr-0989](https://proceedings.iclr.cc/paper_files/paper/2026/hash/2b3bb2c95195130977a51b3bb251c40a-Abstract-Conference.html) When would Vision-Proprioception Policies Fail in Robotic Manipulation? | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? |
| [pr-0990](https://api.crossref.org/works/10.3390/e28090975) Restoring the Right Stream: Training-Free OOD Robustness for Vision–Language–Action Policies | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0991](https://proceedings.mlr.press/v306/liu26bu.html) Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0992](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7a0f8055c838df8e62329a76c7c6403d-Abstract-Conference.html) Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0993](https://www.roboticsproceedings.org/rss22/p203.html) LAP: Language-Action Pre-training Enables Zero-Shot Cross-Embodiment Transfer | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0994](https://openaccess.thecvf.com/content/CVPR2026/html/Liang_Adaptive_Action_Chunking_at_Inference-time_for_Vision-Language-Action_Models_CVPR_2026_paper.html) Adaptive Action Chunking at Inference-time for Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0995](https://arxiv.org/abs/2608.26545) Memory Anchors for Continual Robot Learning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-0996](https://arxiv.org/abs/2602.09722) Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-0997](https://arxiv.org/abs/2605.26820) Can Vision-Language-Action Models Learn from Real-World Data Continually without Forgetting? | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-0998](https://arxiv.org/abs/2512.05693) HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | 보→✓ | ? | ? |
| [pr-0999](https://arxiv.org/abs/2610.05230) Vela: Scaling Vision-Language-Action Models with Adaptive Action Curve Parametrization | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1000](https://arxiv.org/abs/2606.24049) SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies | ✓ | ✓ | 보→✓ | ✓ | ? | ✓ | ? | ? | ? | ? |

<a id="batch-11"></a>

### 배치 11

| ID · 공식 표제 | 링크 | 제목 | 저자 | 연도 | 발표처·게재 | 요약·기여 | 코드 | 가중치 | 데이터 | 태그 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [pr-1001](https://arxiv.org/abs/2610.25961) PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ? | ✓ | ? | ? | ? | ? |
| [pr-1002](https://papers.nips.cc/paper_files/paper/2025/hash/300ccb2187dedd4edcc07f7e76d8e553-Abstract-Conference.html) Real-Time Execution of Action Chunking Flow Policies | ? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1003](https://proceedings.mlr.press/v305/arachchige25a.html) SAIL: Faster-than-Demonstration Execution of Imitation Learning Policies | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-1004](https://proceedings.mlr.press/v306/wang26lj.html) Learning High-Frequency Continuous Action Chunks in Latent Space | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1005](https://arxiv.org/abs/2509.23224) Leave No Observation Behind: Real-time Correction for VLA Action Chunks | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1006](https://arxiv.org/abs/2610.01626) Measuring the Stability Assumption Behind Action Chunking | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1007](https://api.crossref.org/works/10.1109/LRA.2026.3653338) Cooperative Grasping for Collective Object Transport in Constrained Environments | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1008](https://api.crossref.org/works/10.1109/LRA.2025.3562005) Globally-Guided Geometric Fabrics for Reactive Mobile Manipulation in Dynamic Environments | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-1009](https://arxiv.org/abs/2610.01083) WBAG: A Whole-Body and Attached-Geometry Safety Framework for Vision-Language-Action Manipulation | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1010](https://arxiv.org/abs/2610.21453) CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1011](https://neurips.cc/virtual/2026/poster/155467) Grasp-Then-Plan with Failure Attribution: A Closed Two-Stage Framework for Precise and Generalizable Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | ? | ? | 오→✓ |
| [pr-1012](https://arxiv.org/abs/2607.16506) Foresight Residual RL for Long-Horizon Robot Manipulation with Vision-Language-Action Models | 오→✓ | ✓ | 보→✓ | ✓ | 오→✓ | ? | 보→? | ? | ? | ? |
| [pr-1013](https://arxiv.org/abs/2609.26313) SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation | ✓ | ✓ | 보→✓ | ✓ | 오→✓ | ? | ✓ | 보→✓ | ? | ? |
| [pr-1014](https://arxiv.org/abs/2606.07723) VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-1015](https://proceedings.neurips.cc/paper_files/paper/2025/hash/56d748a1d7128158681280be7668e0d3-Abstract-Conference.html) Robust and Scalable Autonomous Reinforcement Learning in Irreversible Environments | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1016](https://openaccess.thecvf.com/content/CVPR2026W/GRAIL-V/html/Gong_RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following_CVPRW_2026_paper.html) RePlan-Bot: Multi-Level Replanning for Embodied Instruction Following | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1017](https://proceedings.neurips.cc/paper/2019/hash/15825aee15eb335cc13f9b559f166ee8-Abstract.html) Online Continual Learning with Maximal Interfered Retrieval | 오→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1018](https://proceedings.mlr.press/v119/reddy20a.html) Learning Human Objectives by Evaluating Hypothetical Behavior | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1019](https://proceedings.neurips.cc/paper/2021/hash/1fa6269f58898f0e809575c9a48747ef-Abstract.html) Information Directed Reward Learning for Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1020](https://openaccess.thecvf.com/content/ICCV2025/html/Ayalew_PROGRESSOR_A_Perceptually_Guided_Reward_Estimator_with_Self-Supervised_Online_Refinement_ICCV_2025_paper.html) PROGRESSOR: A Perceptually Guided Reward Estimator with Self-Supervised Online Refinement | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1021](https://www.roboticsproceedings.org/rss22/p140.html) Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | 보→✓ | 보→✓ | 보→✓ | ? |
| [pr-1022](https://arxiv.org/abs/2601.00675) RoboReward: General-Purpose Vision-Language Reward Models for Robotics | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1023](https://iclr.cc/static/virtual/data/iclr-2022-orals-posters.json) Autonomous Reinforcement Learning: Formalism and Benchmarking | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1024](https://proceedings.mlr.press/v162/sharma22a.html) A State-Distribution Matching Approach to Non-Episodic Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1025](https://proceedings.mlr.press/v305/zhou25a.html) AutoEval: Autonomous Evaluation of Generalist Robot Manipulation Policies in the Real World | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1026](https://papers.nips.cc/paper_files/paper/2021/hash/cec2346566ba8ecd04bfd992fd193fb3-Abstract.html) Active Offline Policy Selection | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1027](https://roboticsproceedings.org/rss21/p077.html) Is Your Imitation Learning Policy Better than Mine? Policy Comparison with Near-Optimal Stopping | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1028](https://roboticsproceedings.org/rss22/p076.html) Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ |
| [pr-1029](https://proceedings.mlr.press/v305/anwar25a.html) Efficient Evaluation of Multi-Task Robot Policies With Active Experiment Selection | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1030](https://arxiv.org/abs/2610.23378) Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation | ✓ | ✓ | 보→✓ | ✓ | ? | ✓ | ? | ? | ? | 오→✓ |
| [pr-1031](https://arxiv.org/abs/2610.03710) EyeRobot 2.0: Active Gaze for Precise Manipulation without Wrist Cameras | ✓ | ✓ | 보→✓ | ✓ | ? | ✓ | ? | ? | ? | 오→✓ |
| [pr-1032](https://arxiv.org/abs/2610.13516) RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1033](https://arxiv.org/abs/2608.21740) CounterAlign: Counterfactual Supervision for Vision-Language-Action Models | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | ? | ? | 오→✓ |
| [pr-1034](https://arxiv.org/abs/2609.25636) RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | 보→✓ | ? |
| [pr-1035](https://arxiv.org/abs/2603.17524) ExecVLA: Following Fine-Grained Execution Constraints in Vision-Language-Action Models with Bi-Level Action Representation | ✓ | ✓ | 보→✓ | ✓ | ? | ✓ | ? | ? | ? | 오→✓ |
| [pr-1036](https://proceedings.mlr.press/v80/fujita18a.html) Clipped Action Policy Gradient | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1037](https://arxiv.org/abs/1806.05134) Marginal Policy Gradients: A Unified Family of Estimators for Bounded Action Spaces with Applications | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1038](https://proceedings.iclr.cc/paper_files/paper/2025/hash/16466b6c95c5924784486ac5a3feeb65-Abstract-Conference.html) What Matters in Learning from Large-Scale Datasets for Robot Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1039](https://proceedings.iclr.cc/paper_files/paper/2026/hash/033d9e8dbbbc0ad90e59222cf1db0fc2-Abstract-Conference.html) DataMIL: Selecting Data for Robot Imitation Learning with Datamodels | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1040](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8c2ecd140ebe227a531edc9a0c3b69d4-Abstract-Conference.html) Difference-Aware Retrieval Policies for Imitation Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1041](https://proceedings.iclr.cc/paper_files/paper/2025/hash/412360d2dd428c26f34918c8d682cf7e-Abstract-Conference.html) STAFF: Speculative Coreset Selection for Task-Specific Fine-tuning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1042](https://proceedings.iclr.cc/paper_files/paper/2026/hash/c7d04ce5e71efdfc7a4a78f7161238a9-Abstract-Conference.html) Can Small Training Runs Reliably Guide Data Curation? Rethinking Proxy-Model Practice | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1043](https://proceedings.mlr.press/v305/haon25a.html) Mechanistic Interpretability for Steering Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1044](https://proceedings.mlr.press/v270/skand25a.html) Simple Masked Training Strategies Yield Control Policies That Are Robust to Sensor Failure | ✓ | ✓ | 보→✓ | 오→✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1045](https://openaccess.thecvf.com/content/CVPR2026/html/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.html) LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | 보→✓ | 보→✓ | ? |
| [pr-1046](https://roboticsproceedings.org/rss20/p133.html) THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | 보→✓ | ? |
| [pr-1047](https://proceedings.mlr.press/v306/dai26c.html) RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1048](https://proceedings.mlr.press/v306/li26hi.html) Scaling Robot Policy Evaluation via Discrete Diffusion World Model | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1049](https://proceedings.mlr.press/v305/yao25a.html) Towards Generalizable Safety in Crowd Navigation via Conformal Uncertainty Handling | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1050](https://www.roboticsproceedings.org/rss20/p007.html) JIGGLE: An Active Sensing Framework for Boundary Parameters Estimation in Deformable Surgical Environments | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1051](https://roboticsproceedings.org/rss20/p010.html) AdaptiGraph: Material-Adaptive Graph-Based Neural Dynamics for Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | 보→✓ | 보→✓ | ? |
| [pr-1052](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5748_ECCV_2024_paper.php) Robo-ABC: Affordance Generalization Beyond Categories via Semantic Correspondence for Robot Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1053](https://api.crossref.org/works/10.1109/ICRA55743.2025.11127987) Beyond Sight: Finetuning Generalist Robot Policies with Heterogeneous Sensors via Language Grounding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1054](https://arxiv.org/abs/2510.03827) LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ✓ | ? | ? | ✓ |
| [pr-1055](https://api.crossref.org/works/10.1109/lra.2026.3741771) Colosseum V2: Benchmarking Generalization for Vision-Language-Action Models | ✓ | 오→✓ | 보→✓ | ✓ | 오→✓ | ? | ? | ? | ? | ✓ |
| [pr-1056](https://proceedings.mlr.press/v305/atreya25a.html) RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1057](https://api.crossref.org/works/10.1109/LRA.2026.3656785) A Taxonomy for Evaluating Generalist Robot Manipulation Policies | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1058](https://api.crossref.org/works/10.1177/02783649241276017) FMB: A functional manipulation benchmark for generalizable robotic learning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1059](https://proceedings.mlr.press/v270/hejna25a.html) ReMix: Optimizing Data Mixtures for Large Scale Imitation Learning | ✓ | ✓ | 보→✓ | 오→✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1060](https://api.crossref.org/works/10.1109/ICRA55743.2025.11127809) DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | 보→✓ | ? |
| [pr-1061](https://proceedings.mlr.press/v270/jiang25a.html) TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction | ✓ | ✓ | 보→✓ | 오→✓ | ✓ | ✓ | ✓ | 보→✓ | 보→✓ | ? |
| [pr-1062](https://proceedings.mlr.press/v305/bharadhwaj25a.html) Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-1063](https://proceedings.mlr.press/v270/xu25b.html) Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs | ✓ | ✓ | 보→✓ | 오→✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1064](https://proceedings.mlr.press/v270/wu25a.html) TidyBot++: An Open-Source Holonomic Mobile Manipulator for Robot Learning | ✓ | ✓ | 보→✓ | 오→✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1065](https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.html) PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | 보→✓ | ? |
| [pr-1066](https://api.crossref.org/works/10.1177/02783649261424445) Equivariant diffusion policy for sample-efficient robotic manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ✓ |
| [pr-1067](https://www.nature.com/articles/s42256-025-01045-3) A process-centric manipulation taxonomy for the organization, classification and synthesis of tactile robot skills | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1068](https://proceedings.mlr.press/v270/ferrandis25a.html) Learning Visuotactile Estimation and Control for Non-prehensile Manipulation under Occlusions | ✓ | ✓ | 보→✓ | 오→✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1069](https://proceedings.mlr.press/v267/richens25a.html) General agents need world models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1070](https://proceedings.mlr.press/v306/warrier26a.html) Benchmarking World-Model Learning with Environment-Level Queries | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1071](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0b9ff9baa226af39f86045ecdc173672-Abstract-Conference.html) Delphic Offline Reinforcement Learning under Nonidentifiable Hidden Confounding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1072](https://proceedings.iclr.cc/paper_files/paper/2026/hash/4415e8cb0741bc0beb79b316f0856108-Abstract-Conference.html) Causal Imitation Learning under Expert-Observable and Expert-Unobservable Confounding | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1073](https://proceedings.mlr.press/v305/yang25b.html) Mobi-π: Mobilizing Your Robot Learning Policy | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1074](https://arxiv.org/abs/2608.30536) Behavior-Skill: A Fine-Grained Benchmark for Evaluating Vision-Language-Action Policies in Long-Horizon Tasks | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ✓ | ? |
| [pr-1075](https://roboticsproceedings.org/rss22/p143.html) ReSteer: Quantifying and Refining the Steerability of Multitask Robot Policies | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1076](https://arxiv.org/abs/2609.30913) Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1077](https://arxiv.org/abs/2610.21251) Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ✓ | ? | ? | ? |
| [pr-1078](https://proceedings.neurips.cc/paper_files/paper/2024/hash/439539557e9ba0d04055773ff1f3241c-Abstract-Datasets_and_Benchmarks_Track.html) ClevrSkills: Compositional Language And Visual Reasoning in Robotics | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1079](https://arxiv.org/abs/2610.12696) Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ✓ |
| [pr-1080](https://www.corl.org/program/accepted-papers) Diagnosing Compositional Generalization in Sequential Robot Tasks | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | 보→✓ | ? |
| [pr-1081](https://proceedings.mlr.press/v305/sridhar25a.html) RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? |
| [pr-1082](https://proceedings.iclr.cc/paper_files/paper/2026/hash/9da515b1ad19d032a7398f00f5ff9b0c-Abstract-Conference.html) Scaling up Memory for Robotic Control via Experience Retrieval | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | 보→✓ | ? | ? |
| [pr-1083](https://roboticsproceedings.org/rss22/p097.html) LIBERO-X: Robustness Litmus for Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ✓ | ? |
| [pr-1084](https://roboticsproceedings.org/rss22/p007.html) A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-1085](https://roboticsproceedings.org/rss22/p072.html) Emergence of Human to Robot Transfer in Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1086](https://roboticsproceedings.org/rss22/p058.html) Learning Native Continuation for Action Chunking Flow Policies | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ |
| [pr-1087](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Dejavu_Towards_Experience_Feedback_Learning_for_Embodied_Intelligence_CVPR_2026_paper.html) Dejavu: Towards Experience Feedback Learning for Embodied Intelligence | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1088](https://robot-saga.github.io/) SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1089](https://aclanthology.org/2026.acl-long.190/) Stable Language Guidance for Vision–Language–Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1090](https://api.crossref.org/works/10.1109/LRA.2026.3682441) LILAC: Language-Conditioned Object-Centric Optical Flow for Open-Loop Trajectory Generation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1091](https://proceedings.iclr.cc/paper_files/paper/2026/hash/163a875ab0c2631ed30b7435c4c9b8f1-Abstract-Conference.html) Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | ? | ? | ? |
| [pr-1092](https://arxiv.org/abs/2606.18953) Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-1093](https://iclr.cc/virtual/2026/poster/10008723) EXPO: Stable Reinforcement Learning with Expressive Policies | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1094](https://arxiv.org/abs/2605.25477) EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1095](https://proceedings.iclr.cc/paper_files/paper/2025/hash/45c361d4117d598d4bb6568b407e9ac9-Abstract-Conference.html) Policy Decorator: Model-Agnostic Online Refinement for Large Policy Model | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1096](https://api.crossref.org/works/10.1109/LRA.2025.3636808) Accelerating Residual Reinforcement Learning With Uncertainty Estimation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1097](https://api.crossref.org/works/10.1109/ICRA.2018.8463162) Overcoming Exploration in Reinforcement Learning with Demonstrations | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1098](https://proceedings.mlr.press/v306/sun26al.html) From Prior to Pro: Efficient Skill Mastery via Distribution Contractive RL Finetuning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1099](https://neurips.cc/virtual/2026/poster/150087) Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | 보→✓ | ? | ? |
| [pr-1100](https://neurips.cc/virtual/2026/poster/148883) Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |

<a id="batch-12"></a>

### 배치 12

| ID · 공식 표제 | 링크 | 제목 | 저자 | 연도 | 발표처·게재 | 요약·기여 | 코드 | 가중치 | 데이터 | 태그 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [pr-1101](https://proceedings.mlr.press/v306/zhang26gz.html) Embodied Interpretability: Linking Causal Understanding to Generalization in Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? |
| [pr-1102](https://arxiv.org/abs/2511.01331) RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ✓ |
| [pr-1103](https://proceedings.mlr.press/v305/he25a.html) Latent Theory of Mind: A Decentralized Diffusion Architecture for Cooperative Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1104](https://arxiv.org/abs/2606.12352) CHORUS: Decentralized Multi-Embodiment Collaboration with One VLA Policy | ✓ | ✓ | 보→✓ | ✓ | 오→✓ | ? | ? | ? | ? | ? |
| [pr-1105](https://arxiv.org/abs/2609.36588) Cooperative Multi-Agent Vision-Language-Action Models via Reinforced Fine Tuning | ? | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1106](https://neurips.cc/virtual/2026/poster/148289) DRILL: Training World Models to Improve Policies, Not Predict Pixels | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1107](https://proceedings.mlr.press/v306/jang26c.html) RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1108](https://arxiv.org/abs/2610.05492) When Does Retrieval Help? A Study of In-Context Adaptation in Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1109](https://arxiv.org/abs/2610.09170) Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies? | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1110](https://aclanthology.org/2026.emnlp-main.2076/) VLA-Trace: Diagnosing Vision-Language-Action Models through Representation and Behavior Tracing | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | ? | ? | ? |
| [pr-1111](https://proceedings.mlr.press/v306/zhang26if.html) A Generalist Pair-wise Progress Critic Model for Vision-Language-Action Robots | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | 보→✓ | 보→✓ | ? |
| [pr-1112](https://proceedings.iclr.cc/paper_files/paper/2025/hash/57da66da25d0ce77e0129b246f358851-Abstract-Conference.html) Studying the Interplay Between the Actor and Critic Representations in Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1113](https://arxiv.org/abs/2607.09042) Learning from Hindsight for VLA Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1114](https://api.crossref.org/works/10.1109/ICRA57147.2024.10610606) SPRINT: Scalable Policy Pre-Training via Language Instruction Relabeling | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | 보→✓ | ? |
| [pr-1115](https://proceedings.mlr.press/v270/zhou25b.html) Autonomous Improvement of Instruction Following Skills via Foundation Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1116](https://proceedings.neurips.cc/paper_files/paper/2025/hash/98d6f928497d9eaad9f320fb2db3040d-Abstract-Conference.html) ReinFlow: Fine-tuning Flow Matching Policy with Online Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | 보→✓ | ? |
| [pr-1117](https://arxiv.org/abs/2508.13446) CAST: Counterfactual Labels Improve Instruction Following in Vision-Language-Action Models | ✓ | ✓ | 보→✓ | 오→✓ | 오→✓ | ? | ✓ | ? | 보→✓ | ? |
| [pr-1118](https://roboticsproceedings.org/rss22/p062.html) PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1119](https://roboticsproceedings.org/rss22/p068.html) LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1120](https://roboticsproceedings.org/rss22/p079.html) Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1121](https://roboticsproceedings.org/rss22/p086.html) Towards Long-Lived Robots: Continual Learning VLA Models via Reinforcement Fine-Tuning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | ? | ? | 오→✓ |
| [pr-1122](https://roboticsproceedings.org/rss22/p091.html) MolmoSpaces: Large-Scale Open Ecosystem for Robot Manipulation and Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | 보→✓ | ? |
| [pr-1123](https://roboticsproceedings.org/rss22/p099.html) FlashSAC: Fast and Stable Off-Policy Reinforcement Learning for High-Dimensional Robot Control | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1124](https://roboticsproceedings.org/rss22/p128.html) Force Policy: Learning Hybrid Force-Position Control Policy under Interaction Frame for Contact-Rich Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1125](https://roboticsproceedings.org/rss22/p153.html) When Life Gives You BC, Make Q-functions: Extracting Q-values from Behavior Cloning for On-Robot Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1126](https://roboticsproceedings.org/rss22/p184.html) KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | 보→✓ | ✓ |
| [pr-1127](https://roboticsproceedings.org/rss22/p201.html) Long-Context Robot Imitation Learning by Focusing on Key History Frames | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1128](https://roboticsproceedings.org/rss22/p208.html) TMRL: Diffusion Timestep-Modulated Pretraining Enables Exploration for Efficient Policy Finetuning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1129](https://roboticsproceedings.org/rss22/p210.html) LDA-1B: Scaling Latent Dynamics Action Model via Universal Embodied Data Ingestion | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1130](https://proceedings.mlr.press/v305/zhang25a.html) ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1131](https://proceedings.mlr.press/v305/li25c.html) ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? |
| [pr-1132](https://proceedings.mlr.press/v305/seneviratne25a.html) HALO : Human Preference Aligned Offline Reward Learning for Robot Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1133](https://openaccess.thecvf.com/content/CVPR2026/html/Fei_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models_CVPR_2026_paper.html) SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1134](https://openaccess.thecvf.com/content/CVPR2026/html/Luo_Joint-Aligned_Latent_Action_Towards_Scalable_VLA_Pretraining_in_the_Wild_CVPR_2026_paper.html) Joint-Aligned Latent Action: Towards Scalable VLA Pretraining in the Wild | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1135](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_CoMo_Learning_Continuous_Latent_Motion_from_Internet_Videos_for_Scalable_CVPR_2026_paper.html) CoMo: Learning Continuous Latent Motion from Internet Videos for Scalable Robot Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1136](https://openaccess.thecvf.com/content/CVPR2026/html/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.html) General Process Reward Modeling for Robotic Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1137](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html) RehearseVLA: Simulated Post-Training for VLAs with Physically-Consistent World Model | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1138](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_MoMa-Kitchen_A_100K_Benchmark_for_Affordance-Grounded_Last-Mile_Navigation_in_Mobile_ICCV_2025_paper.html) MoMa-Kitchen: A 100K+ Benchmark for Affordance-Grounded Last-Mile Navigation in Mobile Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ✓ |
| [pr-1139](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.html) EC-Flow: Enabling Versatile Robotic Manipulation from Action-Unlabeled Videos via Embodiment-Centric Flow | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | 보→✓ | 보→✓ | ? |
| [pr-1140](https://proceedings.mlr.press/v270/stachowicz25a.html) Lifelong Autonomous Improvement of Navigation Foundation Models in the Wild | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1141](https://proceedings.mlr.press/v270/anwar25a.html) Contrast Sets for Evaluating Language-Guided Robot Policies | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | ? | ? | ? |
| [pr-1142](https://proceedings.mlr.press/v270/zhou25a.html) SPIRE: Synergistic Planning, Imitation, and Reinforcement Learning for Long-Horizon Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1143](https://proceedings.mlr.press/v270/nakamoto25a.html) Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1144](https://proceedings.iclr.cc/paper_files/paper/2026/hash/68b7f71467c83d5d32275c5acbf6b588-Abstract-Conference.html) DEAS: DEtached value learning with Action Sequence for Scalable Offline RL | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | 보→✓ | ? |
| [pr-1145](https://proceedings.iclr.cc/paper_files/paper/2026/hash/64a0192102e1421a2b2c15ae0bdb9f3a-Abstract-Conference.html) Dichotomous Diffusion Policy Optimization | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1146](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8e3e3488623d64c493a7f11cf1f2e49f-Abstract-Conference.html) Emergent Dexterity Via Diverse Resets and Large-Scale Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1147](https://proceedings.iclr.cc/paper_files/paper/2026/hash/514bdfb12b318ad02c6f28dc68f2feea-Abstract-Conference.html) CE-Nav: Flow-Guided Reinforcement Refinement for Cross-Embodiment Local Navigation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1148](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e0d760e4495abf701b97c8acda111372-Abstract-Conference.html) PRIMT: Preference-based Reinforcement Learning with Multimodal Feedback and Trajectory Synthesis from Foundation Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1149](https://proceedings.neurips.cc/paper_files/paper/2025/hash/bc09efb501c801ed92e181e26a885c2d-Abstract-Conference.html) Enhancing Tactile-based Reinforcement Learning for Robotic Control | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1150](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b63a24a1832bd14fa945c71f535c0095-Abstract-Conference.html) RLVR-World: Training World Models with Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1151](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Fast-ThinkAct_Efficient_Vision-Language-Action_Reasoning_via_Verbalizable_Latent_Planning_CVPR_2026_paper.html) Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | ? | ? | ? |
| [pr-1152](https://openaccess.thecvf.com/content/CVPR2026/html/Liang_MM-ACT_Learn_from_Multimodal_Parallel_Generation_to_Act_CVPR_2026_paper.html) MM-ACT: Learn from Multimodal Parallel Generation to Act | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | 보→✓ | 보→✓ | ? |
| [pr-1153](https://link.springer.com/chapter/10.1007/978-3-032-37531-5_16) ContextFlow: In-Context Flow Matching for Robot Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | 보→✓ | ? |
| [pr-1154](https://link.springer.com/chapter/10.1007/978-3-032-37023-5_14) EvoVLA: Self-evolving Vision-Language-Action Model | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1155](https://link.springer.com/chapter/10.1007/978-3-032-37152-2_3) Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | 보→✓ | ? |
| [pr-1156](https://arxiv.org/abs/2510.01623) VLA-R1: Enhancing Reasoning in Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | 보→✓ | 보→✓ | ? |
| [pr-1157](https://arxiv.org/abs/2511.17889) MobileVLA-R1: Reinforcing Vision-Language-Action for Mobile Robots | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | 보→✓ | ? |
| [pr-1158](https://arxiv.org/abs/2602.12281) Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment | ? | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-1159](https://peafowlvla.github.io/) PEAfowl: Perception-Enhanced Multi-View Vision-Language-Action for Bimanual Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1160](https://api.crossref.org/works/10.1109/LRA.2026.3729462) PROSPECT: Unified Streaming Vision-Language Navigation via Semantic–Spatial Fusion and Latent Predictive Representation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1161](https://arxiv.org/abs/2506.14009) GRAD-NAV++: Vision-Language Model Enabled Visual Drone Navigation With Gaussian Radiance Fields and Differentiable Dynamics | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? |
| [pr-1162](https://arxiv.org/abs/2606.11743) TacCoRL: Integrating Tactile Feedback into VLA via Simulation | ✓ | ✓ | 보→✓ | ✓ | 오→✓ | ? | ? | ? | ? | ? |
| [pr-1163](https://arxiv.org/abs/2609.23614) CompVLA: A Variable Compliance Vision-Language-Action Model for Contact-rich Manipulation | ✓ | ✓ | 보→✓ | ✓ | 오→✓ | ? | ? | ? | ? | ? |
| [pr-1164](https://arxiv.org/abs/2606.09337) TORL-VLA: Tactile Guided Online Reinforcement Learning for Contact-Rich Manipulation | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ✓ | ? | ? | ✓ |
| [pr-1165](https://arxiv.org/abs/2609.22840) ForceRFT: Refining VLA Actions through Force-Guided Residual Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1166](https://api.crossref.org/works/10.1109/LRA.2025.3551637) FORGE: Force-Guided Exploration for Robust Contact-Rich Manipulation Under Uncertainty | 보→? | ✓ | 보→✓ | ✓ | ✓ | ? | 오→✓ | ? | ? | ? |
| [pr-1167](https://arxiv.org/abs/2610.24512) ContactBench 1.0: A Benchmark for Everyday Contact-Rich Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ✓ | ? | ? | ? |
| [pr-1168](https://arxiv.org/abs/2609.01596) Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ✓ | ? | ? | ? |
| [pr-1169](https://arxiv.org/abs/2609.13516) Constraint-Grounded Reinforcement Learning for Variable Impedance Control in Contact-Rich Robotic Insertion | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1170](https://arxiv.org/abs/2601.15541) CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1171](https://arxiv.org/abs/2510.25889) πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ? | ✓ | ? | ? | ? | ? |
| [pr-1172](https://proceedings.iclr.cc/paper_files/paper/2026/hash/618c95f4557c15b253fb0e6f548ea0c0-Abstract-Conference.html) RL's Razor: Why Online Reinforcement Learning Forgets Less | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1173](https://arxiv.org/abs/2604.23121) Breaking Lock-In: Preserving Steerability under Low-Data VLA Post-Training | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1174](https://arxiv.org/abs/2608.07314) TEMPO: Semantic-Action Decoupled RL Post-Training for Vision-Language-Action Models | 오→✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1175](https://arxiv.org/abs/2602.17659) When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs | ✓ | ✓ | 보→✓ | ✓ | 오→✓ | ? | ✓ | ? | ? | ? |
| [pr-1176](https://link.springer.com/chapter/10.1007/978-3-032-37369-4_24) Trajectory-Level Continuous Action Representation for Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1177](https://arxiv.org/abs/2611.01390) Same Path, Less Time: Training-Free Fast Execution of Vision-Language-Action Models under Inference Latency | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1178](https://arxiv.org/abs/2609.37307) ActMem-VLA: Action-History Memory with Dual-Expert Denoising for Long-Horizon Vision-Language-Action Policies | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ✓ |
| [pr-1179](https://arxiv.org/abs/2611.14488) Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1180](https://arxiv.org/abs/1506.02438) High-Dimensional Continuous Control Using Generalized Advantage Estimation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ |
| [pr-1181](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa09/readings/NgHaradaRussell-shaping-ICML1999.pdf) Policy invariance under reward transformations: Theory and application to reward shaping | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1182](https://proceedings.mlr.press/v37/schaul15.html) Universal Value Function Approximators | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1183](https://proceedings.neurips.cc/paper/2017/hash/350db081a661525235354dd3e19b8c05-Abstract.html) Successor Features for Transfer in Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-1184](https://arxiv.org/abs/2006.09359) AWAC: Accelerating Online Reinforcement Learning with Offline Datasets | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ✓ | ? | ? | ? |
| [pr-1185](https://ojs.aaai.org/index.php/AAAI/article/view/7727) Relative Entropy Policy Search | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1186](https://proceedings.mlr.press/v78/laskey17a.html) DART: Noise Injection for Robust Imitation Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1187](https://api.crossref.org/works/10.1016/S0004-3702(99)00052-1) Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1188](https://api.crossref.org/works/10.1177/0278364913495721) Reinforcement learning in robotics: A survey | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1189](https://arxiv.org/abs/2004.07219) D4RL: Datasets for Deep Data-Driven Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1190](https://proceedings.neurips.cc/paper_files/paper/2023/hash/c44a04289beaf0a7d968a94066a1d696-Abstract-Conference.html) Cal-QL: Calibrated Offline RL Pre-Training for Efficient Online Fine-Tuning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1191](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6d7c4a0727e089ed6cdd3151cbe8d8ba-Abstract-Conference.html) HIQL: Offline Goal-Conditioned RL with Latent States as Actions | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? |
| [pr-1192](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8ffb4e3118280a66b192b6f06e0e2596-Abstract-Conference.html) Is Value Learning Really the Main Bottleneck in Offline RL? | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1193](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0c66099070429b9b49ad8bb19c740c22-Abstract-Conference.html) Horizon Reduction Makes RL Scalable | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1194](https://api.crossref.org/works/10.1146/annurev-control-030323-022510) Deep Reinforcement Learning for Robotics: A Survey of Real-World Successes | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-1195](https://www.roboticsproceedings.org/rss22/p015.html) Act2Goal: From World Model To General Goal-conditioned Policy | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1196](https://www.roboticsproceedings.org/rss22/p016.html) Causal World Modeling for Robot Control | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1197](https://www.roboticsproceedings.org/rss22/p139.html) Tune to Learn: How Controller Gains Shape Robot Policy Learning | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1198](https://www.roboticsproceedings.org/rss22/p154.html) Offline Policy Evaluation for Manipulation Policies via Discounted Liveness Formulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1199](https://arxiv.org/abs/2601.19634) AC2-VLA: Action-Context-Aware Adaptive Computation in Vision-Language-Action Models for Efficient Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1200](https://arxiv.org/abs/2607.29613) WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |

<a id="batch-13"></a>

### 배치 13

| ID · 공식 표제 | 링크 | 제목 | 저자 | 연도 | 발표처·게재 | 요약·기여 | 코드 | 가중치 | 데이터 | 태그 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [pr-1201](https://arxiv.org/abs/2609.18207) Reinforcement Learning for Real-Time Vision-Language-Action Policies | ✓ | ✓ | 보→✓ | ✓ | ? | ✓ | ✓ | ? | ? | ? |
| [pr-1202](https://arxiv.org/abs/2603.21341) RoboAlign: Learning Test-Time Reasoning for Language-Action Alignment in Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ✓ |
| [pr-1203](https://arxiv.org/abs/2512.05107) STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1204](https://www.roboticsproceedings.org/rss22/p021.html) Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| [pr-1205](https://proceedings.iclr.cc/paper_files/paper/2026/hash/07fcc6e2b89439d3ee5ab60939aaa6a0-Abstract-Conference.html) EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1206](https://arxiv.org/abs/2510.08807) Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation | ✓ | ✓ | 보→✓ | 오→✓ | 오→✓ | ? | ? | ? | ✓ | ? |
| [pr-1207](https://openaccess.thecvf.com/content/CVPR2024/html/Wen_FoundationPose_Unified_6D_Pose_Estimation_and_Tracking_of_Novel_Objects_CVPR_2024_paper.html) FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects | ? | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1208](https://proceedings.mlr.press/v270/dass25a.html) Learning to Look: Seeking Information for Decision Making via Policy Factorization | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1209](https://api.crossref.org/works/10.1177/02783649251411922) Active 6D pose estimation for textureless objects using multi-view RGB frames | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ✓ |
| [pr-1210](https://openaccess.thecvf.com/content/CVPR2025/html/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.html) UA-Pose: Uncertainty-Aware 6D Object Pose Estimation and Online Object Completion with Partial References | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1211](https://proceedings.neurips.cc/paper_files/paper/2025/hash/618c0a236e7aace748d09bc8fbed3e4d-Abstract-Conference.html) RFMPose: Generative Category-level Object Pose Estimation via Riemannian Flow Matching | ✓ | ✓ | 보→✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ |
| [pr-1212](https://roboticsproceedings.org/rss22/p145.html) Universal Pose Pretraining for Generalizable Vision-Language-Action Policies | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | 보→✓ | ? | ? |
| [pr-1213](https://roboticsproceedings.org/rss22/p056.html) Robo3R: Enhancing Robotic Manipulation with Accurate Feed-Forward 3D Reconstruction | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | 보→✓ | 보→✓ | ? |
| [pr-1214](https://openaccess.thecvf.com/content/CVPR2026/html/Qian_GeoPredict_Leveraging_Predictive_Kinematics_and_3D_Gaussian_Geometry_for_Precise_CVPR_2026_paper.html) GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1215](https://ojs.aaai.org/index.php/AAAI/article/view/38921) ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1216](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Action-Geometry_Prediction_with_3D_Geometric_Prior_for_Bimanual_Manipulation_CVPR_2026_paper.html) Action-Geometry Prediction with 3D Geometric Prior for Bimanual Manipulation | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ✓ | ? | ? | ? |
| [pr-1217](https://papers.neurips.cc/paper_files/paper/2025/hash/aa1b1a959c80086cba61d0fd66de412f-Abstract-Conference.html) Real-World Reinforcement Learning of Active Perception Behaviors | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | 보→✓ | ? | ? | ? |
| [pr-1218](https://ojs.aaai.org/index.php/AAAI/article/view/29139) Colored Noise in PPO: Improved Exploration and Performance through Correlated Action Sampling | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1219](https://link.springer.com/article/10.1007/s10514-024-10164-6) Guiding real-world reinforcement learning for in-contact manipulation tasks with Shared Control Templates | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1220](https://arxiv.org/abs/2403.10874) Robotic task success evaluation under multi-modal non-parametric object pose uncertainty | 보→✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1221](https://arxiv.org/abs/2608.15139) StructRL: Structured Action-Space Exploration for Flow-Based VLAs | ✓ | ✓ | 보→✓ | ✓ | ? | ✓ | ? | ? | ? | ? |
| [pr-1222](https://arxiv.org/abs/2509.19292) SOE: Sample-Efficient Robot Policy Self-Improvement via On-Manifold Exploration | ✓ | ✓ | 보→✓ | 오→✓ | 오→✓ | ? | ? | ? | ? | ? |
| [pr-1223](https://arxiv.org/abs/2509.11364) ActivePose: Active 6D Object Pose Estimation and Tracking for Robotic Manipulation | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1224](https://arxiv.org/abs/2609.23504) Imagine then Verify: Affordance-Targeted Active Perception for Task-Oriented Grasping in Cluttered Scenes | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1225](https://arxiv.org/abs/2609.34018) Estimate, Don't Imitate: Reusing Differentiable State-Based Policies for Visuomotor Control | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1226](https://link.springer.com/chapter/10.1007/978-3-032-37271-0_2) Understanding the Impact of Geometric Foundation Models on Vision-Language-Action Models | ✓ | ✓ | 보→✓ | ✓ | ✓ | ? | ? | ? | ? | ? |
| [pr-1227](https://arxiv.org/abs/2610.14704) PRISM: Precision Forcing for Generalist Vision-Language-Action Policies | ✓ | ✓ | 보→✓ | ✓ | ? | ? | ? | ? | ? | ? |
| [pr-1228](https://proceedings.neurips.cc/paper_files/paper/2024/hash/67b0e7c7c2a5780aeefe3b79caac106e-Abstract-Conference.html) DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ |
| [pr-1229](https://api.crossref.org/works/10.1109/icra55743.2025.11127299) Improving Vision-Language-Action Model with Online Reinforcement Learning | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1230](https://api.crossref.org/works/10.1109/icra55743.2025.11128601) MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1231](https://www.corl.org/program/accepted-papers) MEM: Multi-Scale Embodied Memory for Vision Language Action Models | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1232](https://proceedings.mlr.press/v305/kwok25a.html) RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| [pr-1233](https://arxiv.org/abs/2606.17055) T-Rex: Tactile-Reactive Dexterous Manipulation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| [pr-1234](https://roboticsproceedings.org/rss22/p005.html) Contact-Grounded Policy: Dexterous Visuotactile Policy with Generative Contact Grounding | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1235](https://roboticsproceedings.org/rss20/p058.html) Advancing Humanoid Locomotion: Mastering Challenging Terrains with Denoising World Model Learning | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1236](https://proceedings.mlr.press/v305/li25h.html) CLONE: Closed-Loop Whole-Body Humanoid Teleoperation for Long-Horizon Tasks | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1237](https://proceedings.mlr.press/v305/xiong25a.html) Vision in Action: Learning Active Perception from Human Demonstrations | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1238](https://arxiv.org/abs/2606.09258) Back to the Familiar Future: Failure Recovery for VLA Policies via Pre-Imagined Milestone Selection | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1239](https://arxiv.org/abs/2606.21386) VLA-FAIL: Efficient Task Failure Detection for Finetuned Vision-Language-Action Models | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1240](https://arxiv.org/abs/2605.27724) HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | 보→✓ | ✓ |
| [pr-1241](https://proceedings.neurips.cc/paper_files/paper/2024/hash/4364fef031fdf7bfd9d1c9c56b287084-Abstract-Conference.html) Active Perception for Grasp Detection via Neural Graspness Field | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1242](https://proceedings.mlr.press/v305/zhang25l.html) KineDex: Learning Tactile-Informed Visuomotor Policies via Kinesthetic Teaching for Dexterous Manipulation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ |
| [pr-1243](https://proceedings.mlr.press/v305/wu25d.html) UniTac2Pose: A Unified Approach Learned in Simulation for Category-level Visuotactile In-hand Pose Estimation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1244](https://roboticsproceedings.org/rss21/p054.html) ViTaSCOPE: Visuo-tactile Implicit Representation for In-hand Pose and Extrinsic Contact Estimation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1245](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e19b6f65791e350347bcff8a3955cb5b-Abstract-Conference.html) VTDexManip: A Dataset and Benchmark for Visual-tactile Pretraining and Dexterous Manipulation with Reinforcement Learning | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ |
| [pr-1246](https://roboticsproceedings.org/rss22/p129.html) ViTacFormer: Learning Cross-Modal Representation for Visuo-Tactile Dexterous Manipulation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1247](https://arxiv.org/abs/2606.11767) Blind Dexterous Grasping via Real2Sim2Real Tactile Policy Learning | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1248](https://arxiv.org/abs/2603.04531) PTLD: Sim-to-real Privileged Tactile Latent Distillation for Dexterous Manipulation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1249](https://arxiv.org/abs/2611.01659) HuG: Learning Humanoid Whole-Body Affordance-Aware Grasping with Active Perception | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ |
| [pr-1250](https://arxiv.org/abs/2606.06194) ActiveMimic: Egocentric Video Pretraining with Active Perception | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ |
| [pr-1251](https://api.crossref.org/works/10.1177/02783649211050677) HARMONIC: A multimodal dataset of assistive human–robot collaboration | 보→✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ | ? |
| [pr-1252](https://www.corl.org/program/accepted-papers) Efficient and Reliable Teleoperation through Real-to-Sim-to-Real Shared Autonomy | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 보→✓ | ✓ | ? |
