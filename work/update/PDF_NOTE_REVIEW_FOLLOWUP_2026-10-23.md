# DOC-QA2 — 남은 PDF 추출 손상 구간 원문 대조

- 검토일: 2026-10-23 KST
- 상태: **DONE — 원문 대조·수정·검증·임시 파일 삭제 완료**
- 범위: [DOC-QA1](./PDF_NOTE_REVIEW_2026-10-23.md)이 인계한 **84편·156개 노트·272개 제어문자 포함 구간**.
- 상세 근거: [PDF URL·SHA256·페이지·수정 전후 문장과 파일 hash](../sources/pdf_note_review_followup_2026-10-23.json).

## 완료 범위와 해석

| 항목 | 결과 |
|---|---:|
| 원문을 확보해 대조한 논문 | 84편 |
| 수정한 표준 노트 | 156개 |
| 원문 근거로 다시 쓴 손상 구간 | 272개 |
| 수정 근거의 서로 다른 PDF 페이지 | 97개 |
| 앞뒤 맥락·identity 확인 포함 시각 대조 페이지 | 99개 / 117개 렌더 구간 |
| 전체 표준 노트 C0/C1 검사 | 5,185개 검사 / 잔여 0개 |
| DOC-QA1과 합친 처리 범위 | 139편 / 291개 노트 / 578개 구간 |

텍스트 추출로 대상 위치를 찾고 렌더링한 수식·표·그림과 앞뒤 문맥을 직접 대조했다. 잘린 식은 확인한 의미를 서술하고 식 번호를 연결했다. 표의 열·부호·단위가 추출 과정에서 섞인 경우 해당 구간의 분류도 수정했다. 수정한 노트에는 이번 대조 범위와 ledger 링크를 추가했다.

페이지 번호는 **다운로드한 정확한 PDF의 1-based 페이지**다. 83개 파일은 과거 full-text review의 SHA256과 일치했다. DMP 1편은 Edinburgh Research Explorer의 다운로드 날짜가 붙은 cover를 포함한 파일이며, cover의 title·authors·DOI와 해당 식을 확인했다. 동일 byte라고 기록하지 않았다.

OpenReview 접근 제한으로 16편은 공개 PDF 전달 사본을 사용했고, 모두 과거 검토본 hash와 일치했다. STOMP는 대학 ROS wiki의 저자 PDF를 사용했으며 전달 경로의 인증서 예외와 hash 확인을 ledger에 남겼다. 이들은 본문 전달 경로이며 venue·acceptance의 새 근거로 사용하지 않았다.

이번 완료는 **손상 구간과 직접 연결된 분류의 수정**이다. 모든 기존 주장 정독, 일반 OCR 오류의 전수 제거, 공개 구현 실행 또는 정책 효과 검증을 의미하지 않는다. 제어문자가 없더라도 추출 문장에 의미 오류가 남을 수 있다. Reading status·사용자 분석·tier·registry identity와 기존 연구 HOLD/NO-GO 판정은 유지한다.

## 주요 수정

- **VLA·robot policy interface:** VIMA의 관측·행동 이력, RoboCat의 embodiment별 token 수와 episode 내 goal 반복, Gato의 text/action token loss mask를 복원했다. Mobile ALOHA는 static base-action zero padding, 동등 sampling 확률, RGB camera·joint-position 입력을 구분했다.
- **학습식과 제어식:** DDPM noise parameterization, GAIL cost regularizer의 유한 정의역, PPO의 최대화 objective 부호, target value network를 사용하는 초기 SAC, CQL의 배경 actor-critic 식을 각각 구분했다. Loss를 output action·latency·성능 metric으로 분류한 대상 행도 수정했다.
- **평가 표의 열과 단위:** PRISM Table 3의 과제별 값은 20 trials당 성공 횟수의 3-seed mean±std이며 평균 행은 백분율이다. SemanticKITTI의 parameters / GPU hours per epoch / seconds per point cloud를 분리하고, OccFormer의 local/global·image/3D augmentation 체크 열을 복원했다. OpenSeg의 Table 2 결과와 Table 3 initialization ablation도 분리했다.
- **표현 정의와 robot 효과:** Fin3R objective를 planning handoff로, VER state probability를 recovery command로, KinectFusion solver를 평가 결과로 잘못 연결한 구간을 수정했다. G4Splat의 Table A4는 명시된 L1 distance와 threshold 0.05를 보존했다.
- **제어 모델과 실험 범위:** Preview-control 논문의 cart-table 도식, HRP-2P parameter 기반 multibody 비교, controller objective, tracking error를 구분했다. 짧은 preview에서 tracking이 나빠진다는 결과를 곧바로 불안정·낙상으로 해석하지 않았다.

수치·기호의 직접 근거와 각 논문별 제한은 ledger의 `notes[].corrections`와 해당 PDF 페이지에 있다.

## 원문 자체에 남은 해석 확인 항목

후속 상태: [DOC-QA3 원문–공개 구현 대조](./PAPER_CODE_FORMULA_REVIEW_2026-10-23.md)에서 아래 5편의 지정 code 경로를 확인했다. 원문 표기는 보존하고 공개 구현의 차이를 별도로 기록했다. 논문 실험에 사용된 정확한 revision은 미확인이다. 아래 표와 이 문서의 ledger hash는 DOC-QA2 완료 당시 snapshot이며, 후속 수정 hash는 DOC-QA3 ledger를 따른다.

다음은 손상 문자 복원과 별개다. 원문 표기를 보존하고 확인 경계를 적었으며 **논문 오류나 새로운 연구 공백으로 확정하지 않았다**. 후속 DOC-QA3은 지정 항목의 공식 구현·정오표를 읽는 비실험 작업으로 제한한다.

| 논문 | 이번 확인 | 후속 대조할 위치 |
|---|---|---|
| [Physically Executable 3D Gaussian](https://openreview.net/forum?id=HB6KvsqcAn) | PDF p. 7의 PS 식은 clipped heading-change 평균으로 읽히지만 설명은 variance라고 부름 | 공식 metric 구현의 aggregation·clipping·단위 |
| [3D QA via only 2D VLMs](https://openreview.net/forum?id=IkhJApkJQ3) | PDF p. 6 Eq. (8)의 log 안팎 target/prediction 배치가 통상적인 BCE 표기와 다름 | 저자 loss 구현 및 정오표; 노트에 표준식을 임의 대입하지 않음 |
| [RoboFlow4D](https://arxiv.org/pdf/2605.17522.pdf#page=6) | PDF p. 6의 power-law sampling 식과 γ>1에서 말단을 조밀하게 한다는 설명의 방향 불일치 | 실제 sampler의 exponent·time direction·index rounding |
| [QuadricFormer](https://arxiv.org/pdf/2506.10977#page=4) | Eq. (4)의 z 항은 2/ε₂로 인쇄되어 있음 | 공식 primitive evaluation의 exponent convention; 관행식으로 덮어쓰지 않음 |
| [LIO-SAM](https://arxiv.org/pdf/2007.00258#page=4) | Scan-matching objective의 표시식은 거리 합이며 제곱이 따로 표기되지 않음 | 공식 solver residual과 least-squares 구성; 식과 구현 경계 |

CLARE의 표시된 norm과 GSV3D의 clean-latent target 등은 이번 원문 표기대로 정리했다. 모든 표기 차이를 별도 연구 후보나 긴 반복 조사 queue로 확대하지 않는다.

## 검증·정리

Tier 생성기의 compile·재생성, 문서 유지보수 회귀 검사 5개, `git diff --check`를 통과했다. 전체 저장소 감사는 1,037편·5,185개 표준 노트에 대해 **오류 0개·경고 0개**였다. Note-artifact dry-run도 findings 0개이며, 수정 156개 노트의 hash와 272개 수정 내용이 ledger와 일치한다.

`papers.json`, `registry_meta.json`, tier CSV, active/history reading CSV의 작업 전후 SHA256이 일치한다. 같은 84편에서 수정 대상이 아닌 264개 노트와 관련 없는 기존 dirty 파일도 보존했다. Registry 수는 1,037편, CORE/NEXT/REFERENCE/ARCHIVE는 47/275/473/242편이다. Git 게시·새 실험·dependency 설치는 수행하지 않았다.

삭제 직전에 원문 파일 hash를 다시 확인하고, **PDF 84개(826,019,794 bytes), PNG 139개를 포함한 전용 작업 파일 532개와 임시 디렉토리를 삭제했다.** 기존 사용자 PDF에 손대지 않았으며 작업 종료 시 저장소 PDF는 0개다. Source ledger에는 URL·hash·PDF 페이지·렌더 대조 좌표·수정 전후 기록만 보존한다. 자세한 기계 검증과 정리 결과는 `validation`, `cleanup`을 따른다.

## 논문별 대조 범위

수정 페이지와 노트 수는 source ledger에서 집계한다. 추가로 읽은 앞뒤 페이지는 ledger의 `visually_inspected_pages`에 따로 기록한다.

| Paper ID | 논문 | 수정 노트 | 수정 근거 PDF 페이지 |
|---|---|---:|---|
| pr-0008 | [Denoising Diffusion Probabilistic Models](../../2020/NeurIPS/2020_NeurIPS_Denoising-Diffusion-Probabilistic-Models/01_overview.md) | 1 | 4 |
| pr-0040 | [VIMA: General Robot Manipulation with Multimodal Prompts](../../2023/ICML/2023_ICML_VIMA-General-Robot-Manipulation-with-Multimodal-Prompts/01_overview.md) | 3 | 4 |
| pr-0042 | [Benchmarking Knowledge Transfer for Lifelong Robot Learning](../../2023/NeurIPS/2023_NeurIPS_Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learnin/01_overview.md) | 2 | 3 |
| pr-0057 | [Continuous 3D Perception Model with Persistent State](../../2025/CVPR/2025_CVPR_Continuous-3D-Perception-Model-with-Persistent-State/01_overview.md) | 1 | 5 |
| pr-0059 | [Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation](../../2025/CoRL/2025_CoRL_Long-VLA-Unleashing-Long-Horizon-Capability-of-Vision-Lang/01_overview.md) | 1 | 3 |
| pr-0070 | [3D Vision-Language Gaussian Splatting](../../2025/ICLR/2025_ICLR_3D-Vision-Language-Gaussian-Splatting/01_overview.md) | 1 | 6 |
| pr-0081 | [Learning Geometric Reasoning Networks For Robot Task And Motion Planning](../../2025/ICLR/2025_ICLR_Learning-Geometric-Reasoning-Networks-For-Robot-Task-And-M/01_overview.md) | 4 | 4 |
| pr-0084 | [ET-SEED: EFFICIENT TRAJECTORY-LEVEL SE(3) EQUIVARIANT DIFFUSION POLICY](../../2025/ICLR/2025_ICLR_ET-SEED-EFFICIENT-TRAJECTORY-LEVEL-SE3-EQUIVARIANT-DIFFUSI/01_overview.md) | 2 | 7 |
| pr-0094 | [AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild](../../2026/ICLR/2026_ICLR_AutoFly-Vision-Language-Action-Model-for-UAV-Autonomous-Na/01_overview.md) | 3 | 4, 17 |
| pr-0106 | [Towards Physically Executable 3D Gaussian for Embodied Navigation](../../2026/ICLR/2026_ICLR_Towards-Physically-Executable-3D-Gaussian-for-Embodied-Nav/01_overview.md) | 1 | 7 |
| pr-0107 | [GPT4Scene: Understand 3D Scenes from Videos with Vision-Language Models](../../2026/ICLR/2026_ICLR_GPT4Scene-Understand-3D-Scenes-from-Videos-with-Vision-Lan/01_overview.md) | 1 | 3 |
| pr-0123 | [SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning](../../2025/NeurIPS/2025_NeurIPS_SafeVLA-Towards-Safety-Alignment-of-Vision-Language-Action/01_overview.md) | 1 | 31 |
| pr-0124 | [SoFar: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation](../../2025/NeurIPS/2025_NeurIPS_SoFar-Language-Grounded-Orientation-Bridges-Spatial-Reason/01_overview.md) | 1 | 4 |
| pr-0132 | [ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning](../../2025/ICML/2025_ICML_ReinboT-Amplifying-Robot-Visual-Language-Manipulation-with/01_overview.md) | 1 | 2, 4 |
| pr-0140 | [ReferSplat: Referring Segmentation in 3D Gaussian Splatting](../../2025/ICML/2025_ICML_ReferSplat-Referring-Segmentation-in-3D-Gaussian-Splatting/01_overview.md) | 1 | 5 |
| pr-0145 | [3D Question Answering via only 2D Vision-Language Models](../../2025/ICML/2025_ICML_3D-Question-Answering-via-only-2D-Vision-Language-Models/01_overview.md) | 1 | 6 |
| pr-0152 | [Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies](../../2026/ICML/2026_ICML_Discrete-Diffusion-VLA-Bringing-Discrete-Diffusion-to-Acti/01_overview.md) | 1 | 5 |
| pr-0164 | [RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation](../../2026/ICML/2026_ICML_RoboFlow4D-A-Lightweight-Flow-World-Model-Toward-Real-Time/01_overview.md) | 1 | 6 |
| pr-0166 | [SpikeVLA: Vision-Language-Action Models with Spiking Neural Networks](../../2026/ICML/2026_ICML_SpikeVLA-Vision-Language-Action-Models-with-Spiking-Neural/01_overview.md) | 1 | 4 |
| pr-0170 | [MiniVLN: Efficient Vision-And-Language Navigation by Progressive Knowledge Distillation](../../2025/ICRA/2025_ICRA_MiniVLN-Efficient-Vision-And-Language-Navigation-by-Progre/01_overview.md) | 1 | 4 |
| pr-0175 | [LE-Object: Language Embedded Object-Level Neural Radiance Fields for Open-Vocabulary Scene](../../2025/ICRA/2025_ICRA_LE-Object-Language-Embedded-Object-Level-Neural-Radiance-F/01_overview.md) | 3 | 5 |
| pr-0236 | [Exploiting Vision Language Model for Training-Free 3D Point Cloud OOD Detection via Graph Score Propagation](../../2025/ICCV/2025_ICCV_Exploiting-Vision-Language-Model-for-Training-Free-3D-Poin/01_overview.md) | 3 | 3 |
| pr-0237 | [Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics](../../2025/ICCV/2025_ICCV_Exploring-the-Adversarial-Vulnerabilities-of-Vision-Langua/01_overview.md) | 4 | 2, 5 |
| pr-0247 | [VLR-Driver: Large Vision-Language-Reasoning Models for Embodied Autonomous Driving](../../2025/ICCV/2025_ICCV_VLR-Driver-Large-Vision-Language-Reasoning-Models-for-Embo/01_overview.md) | 5 | 4, 6 |
| pr-0274 | [CLARE: Continual Learning for Vision-Language-Action Models via Autonomous Adapter Routing and Expansion](../../2026/RA-L/2026_RA-L_CLARE-Continual-Learning-for-Vision-Language-Action-Models/01_overview.md) | 3 | 3, 4 |
| pr-0299 | [Point-BERT: Pre-training 3D Point Cloud Transformers with Masked Point Modeling](../../2022/CVPR/2022_CVPR_Point-BERT-Pre-training-3D-Point-Cloud-Transformers-with-M/01_overview.md) | 1 | 5 |
| pr-0312 | [ReconFusion: 3D Reconstruction with Diffusion Priors](../../2024/CVPR/2024_CVPR_ReconFusion-3D-Reconstruction-with-Diffusion-Priors/01_overview.md) | 1 | 4 |
| pr-0316 | [SG-PGM: Partial Graph Matching Network with Semantic Geometric Fusion for 3D Scene Graph Alignment and Its Downstream Tasks](../../2024/CVPR/2024_CVPR_SG-PGM-Partial-Graph-Matching-Network-with-Semantic-Geomet/01_overview.md) | 1 | 3 |
| pr-0323 | [MVIP-NeRF: Multi-view 3D Inpainting on NeRF Scenes via Diffusion Prior](../../2024/CVPR/2024_CVPR_MVIP-NeRF-Multi-view-3D-Inpainting-on-NeRF-Scenes-via-Diff/01_overview.md) | 2 | 3, 5 |
| pr-0328 | [Align Your Gaussians: Text-to-4D with Dynamic 3D Gaussians and Composed Diffusion Models](../../2024/CVPR/2024_CVPR_Align-Your-Gaussians-Text-to-4D-with-Dynamic-3D-Gaussians/01_overview.md) | 2 | 3, 5 |
| pr-0347 | [TokenSplat: Token-aligned 3D Gaussian Splatting for Feed-forward Pose-free Reconstruction](../../2026/CVPR/2026_CVPR_TokenSplat-Token-aligned-3D-Gaussian-Splatting-for-Feed-fo/01_overview.md) | 2 | 4 |
| pr-0357 | [DualSplat: Robust 3D Gaussian Splatting via Pseudo-Mask Bootstrapping from Reconstruction Failures](../../2026/CVPR/2026_CVPR_DualSplat-Robust-3D-Gaussian-Splatting-via-Pseudo-Mask-Boo/01_overview.md) | 3 | 5 |
| pr-0365 | [Ov3R: Open-Vocabulary Semantic 3D Reconstruction from RGB Videos](../../2026/CVPR/2026_CVPR_Ov3R-Open-Vocabulary-Semantic-3D-Reconstruction-from-RGB-V/01_overview.md) | 1 | 6 |
| pr-0372 | [FreeSplatter: Pose-free Gaussian Splatting for Sparse-view 3D Reconstruction](../../2025/ICCV/2025_ICCV_FreeSplatter-Pose-free-Gaussian-Splatting-for-Sparse-view/01_overview.md) | 2 | 3 |
| pr-0378 | [SEGS-SLAM: Structure-enhanced 3D Gaussian Splatting SLAM with Appearance Embedding](../../2025/ICCV/2025_ICCV_SEGS-SLAM-Structure-enhanced-3D-Gaussian-Splatting-SLAM-wi/01_overview.md) | 1 | 5 |
| pr-0383 | [ExploreGS: Explorable 3D Scene Reconstruction with Virtual Camera Samplings and Diffusion Priors](../../2025/ICCV/2025_ICCV_ExploreGS-Explorable-3D-Scene-Reconstruction-with-Virtual/01_overview.md) | 2 | 4 |
| pr-0384 | [GSV3D: Gaussian Splatting-based Geometric Distillation with Stable Video Diffusion for Single-Image 3D Object Generation](../../2025/ICCV/2025_ICCV_GSV3D-Gaussian-Splatting-based-Geometric-Distillation-with/01_overview.md) | 2 | 5 |
| pr-0404 | [GaussReg: Fast 3D Registration with Gaussian Splatting](../../2024/ECCV/2024_ECCV_GaussReg-Fast-3D-Registration-with-Gaussian-Splatting/01_overview.md) | 1 | 5 |
| pr-0411 | [CityGaussianV2: Efficient and Geometrically Accurate Reconstruction for Large-Scale Scenes](../../2025/ICLR/2025_ICLR_CityGaussianV2-Efficient-and-Geometrically-Accurate-Recons/01_overview.md) | 1 | 6 |
| pr-0412 | [GS-LiDAR: Generating Realistic LiDAR Point Clouds with Panoramic Gaussian Splatting](../../2025/ICLR/2025_ICLR_GS-LiDAR-Generating-Realistic-LiDAR-Point-Clouds-with-Pano/01_overview.md) | 1 | 5 |
| pr-0420 | [Multimodality Helps Few-shot 3D Point Cloud Semantic Segmentation](../../2025/ICLR/2025_ICLR_Multimodality-Helps-Few-shot-3D-Point-Cloud-Semantic-Segme/01_overview.md) | 2 | 4 |
| pr-0423 | [G4Splat: Geometry-Guided Gaussian Splatting with Generative Prior](../../2026/ICLR/2026_ICLR_G4Splat-Geometry-Guided-Gaussian-Splatting-with-Generative/01_overview.md) | 4 | 27 |
| pr-0438 | [Fin3R: Fine-tuning Feed-forward 3D Reconstruction Models via Monocular Knowledge Distillation](../../2025/NeurIPS/2025_NeurIPS_Fin3R-Fine-tuning-Feed-forward-3D-Reconstruction-Models-vi/01_overview.md) | 3 | 6 |
| pr-0448 | [QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction](../../2025/NeurIPS/2025_NeurIPS_QuadricFormer-Scene-as-Superquadrics-for-3D-Semantic-Occup/01_overview.md) | 1 | 4 |
| pr-0455 | [Scalable Non-Equivariant 3D Molecule Generation via Rotational Alignment](../../2025/ICML/2025_ICML_Scalable-Non-Equivariant-3D-Molecule-Generation-via-Rotati/01_overview.md) | 1 | 3 |
| pr-0458 | [PRISM: Learning Realistic Depth via Physics-Grounded Noise Disentanglement with Semantic-Geometric Collaboration](../../2026/ICML/2026_ICML_PRISM-Learning-Realistic-Depth-via-Physics-Grounded-Noise/01_overview.md) | 1 | 8 |
| pr-0460 | [Rh-3DGS: Robust Open-Vocabulary Scene Understanding via Riemannian Huber Distillation and Manifold-Aware Sampling](../../2026/ICML/2026_ICML_Rh-3DGS-Robust-Open-Vocabulary-Scene-Understanding-via-Rie/01_overview.md) | 2 | 3 |
| pr-0481 | [LSSInst: Improving Geometric Modeling in LSS-Based BEV Perception with Instance Representation](../../2025/3DV/2025_3DV_LSSInst-Improving-Geometric-Modeling-in-LSS-Based-BEV-Perc/01_overview.md) | 1 | 5 |
| pr-0489 | [KinectFusion: Real-Time Dense Surface Mapping and Tracking](../../2011/ISMAR/2011_ISMAR_KinectFusion-Real-Time-Dense-Surface-Mapping-and-Tracking/01_overview.md) | 2 | 7 |
| pr-0497 | [SemanticKITTI: A Dataset for Semantic Scene Understanding of LiDAR Sequences](../../2019/ICCV/2019_ICCV_SemanticKITTI-A-Dataset-for-Semantic-Scene-Understanding-o/01_overview.md) | 4 | 6 |
| pr-0511 | [NeuS: Learning Neural Implicit Surfaces by Volume Rendering for Multi-view Reconstruction](../../2021/NeurIPS/2021_NeurIPS_NeuS-Learning-Neural-Implicit-Surfaces-by-Volume-Rendering/01_overview.md) | 1 | 5 |
| pr-0514 | [OccFormer: Dual-path Transformer for Vision-based 3D Semantic Occupancy Prediction](../../2023/ICCV/2023_ICCV_OccFormer-Dual-path-Transformer-for-Vision-based-3D-Semant/01_overview.md) | 2 | 6, 10 |
| pr-0523 | [Generative Adversarial Imitation Learning](../../2016/NeurIPS/2016_NeurIPS_Generative-Adversarial-Imitation-Learning/01_overview.md) | 2 | 6 |
| pr-0524 | [Proximal Policy Optimization Algorithms](../../2017/arxiv/2017_arxiv_Proximal-Policy-Optimization-Algorithms/01_overview.md) | 1 | 5 |
| pr-0537 | [In-Place Scene Labelling and Understanding with Implicit Scene Representation](../../2021/ICCV/2021_ICCV_In-Place-Scene-Labelling-and-Understanding-with-Implicit-S/01_overview.md) | 1 | 3 |
| pr-0544 | [OpenSeg: Scaling Open-Vocabulary Image Segmentation with Image-Level Labels](../../2022/ECCV/2022_ECCV_OpenSeg-Scaling-Open-Vocabulary-Image-Segmentation-with-Im/01_overview.md) | 2 | 13 |
| pr-0546 | [nuScenes: A Multimodal Dataset for Autonomous Driving](../../2020/CVPR/2020_CVPR_nuScenes-A-Multimodal-Dataset-for-Autonomous-Driving/01_overview.md) | 1 | 6 |
| pr-0556 | [STOMP: Stochastic Trajectory Optimization for Motion Planning](../../2011/ICRA/2011_ICRA_STOMP-Stochastic-Trajectory-Optimization-for-Motion-Planni/01_overview.md) | 2 | 2 |
| pr-0559 | [Dynamical Movement Primitives: Learning Attractor Models for Motor Behaviors](../../2013/Neural-Computation/2013_Neural-Computation_Dynamical-Movement-Primitives-Learning-Attractor-Models-fo/01_overview.md) | 1 | 7 |
| pr-0574 | [Mobile ALOHA: Learning Bimanual Mobile Manipulation using Low-Cost Whole-Body Teleoperation](../../2024/CoRL/2024_CoRL_Mobile-ALOHA-Learning-Bimanual-Mobile-Manipulation-using-L/01_overview.md) | 3 | 5 |
| pr-0575 | [Learning to Walk from Three Minutes of Real-World Data with Semi-structured Dynamics Models](../../2024/CoRL/2024_CoRL_Learning-to-Walk-from-Three-Minutes-of-Real-World-Data-wit/01_overview.md) | 3 | 14 |
| pr-0582 | [Multi-Robot Motion Planning with Diffusion Models](../../2025/ICLR/2025_ICLR_Multi-Robot-Motion-Planning-with-Diffusion-Models/01_overview.md) | 4 | 4 |
| pr-0594 | [Optimization-Based Locomotion Planning, Estimation, and Control Design for the Atlas Humanoid Robot](../../2016/Autonomous-Robots/2016_Autonomous-Robots_Optimization-Based-Locomotion-Planning-Estimation-and-Cont/01_overview.md) | 4 | 7, 11 |
| pr-0598 | [Blind Bipedal Stair Traversal via Sim-to-Real Reinforcement Learning](../../2021/RSS/2021_RSS_Blind-Bipedal-Stair-Traversal-via-Sim-to-Real-Reinforcemen/01_overview.md) | 1 | 2 |
| pr-0601 | [HumanPlus: Humanoid Shadowing and Imitation from Humans](../../2024/CoRL/2024_CoRL_HumanPlus-Humanoid-Shadowing-and-Imitation-from-Humans/01_overview.md) | 1 | 3 |
| pr-0615 | [Trust Region Policy Optimization](../../2015/ICML/2015_ICML_Trust-Region-Policy-Optimization/01_overview.md) | 3 | 4 |
| pr-0620 | [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](../../2018/ICML/2018_ICML_Soft-Actor-Critic-Off-Policy-Maximum-Entropy-Deep-Reinforc/01_overview.md) | 1 | 5 |
| pr-0622 | [Conservative Q-Learning for Offline Reinforcement Learning](../../2020/NeurIPS/2020_NeurIPS_Conservative-Q-Learning-for-Offline-Reinforcement-Learning/01_overview.md) | 2 | 2 |
| pr-0636 | [Implicit Behavioral Cloning](../../2022/CoRL/2022_CoRL_Implicit-Behavioral-Cloning/01_overview.md) | 3 | 4 |
| pr-0647 | [Global Planning for Contact-Rich Manipulation via Local Smoothing of Quasi-Dynamic Contact Models](../../2023/T-RO/2023_T-RO_Global-Planning-for-Contact-Rich-Manipulation-via-Local-Sm/01_overview.md) | 3 | 5 |
| pr-0648 | [Tactile-Driven Non-Prehensile Object Manipulation via Extrinsic Contact Mode Control](../../2024/RSS/2024_RSS_Tactile-Driven-Non-Prehensile-Object-Manipulation-via-Extr/01_overview.md) | 1 | 4 |
| pr-0659 | [DreamWaQ: Learning Robust Quadrupedal Locomotion with Implicit Terrain Imagination via Deep Reinforcement Learning](../../2023/ICRA/2023_ICRA_DreamWaQ-Learning-Robust-Quadrupedal-Locomotion-with-Impli/01_overview.md) | 1 | 3 |
| pr-0676 | [Benchmarking Safe Exploration in Deep Reinforcement Learning](../../2019/Technical-Report/2019_Technical-Report_Benchmarking-Safe-Exploration-in-Deep-Reinforcement-Learni/01_overview.md) | 2 | 14 |
| pr-0679 | [Learning Latent Dynamics for Planning from Pixels](../../2019/ICML/2019_ICML_Learning-Latent-Dynamics-for-Planning-from-Pixels/01_overview.md) | 1 | 2 |
| pr-0707 | [Failure Prediction with Statistical Guarantees for Vision-Based Robot Control](../../2022/RSS/2022_RSS_Failure-Prediction-with-Statistical-Guarantees-for-Vision/01_overview.md) | 3 | 3 |
| pr-0723 | [RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation](../../2023/arXiv/2023_arXiv_RoboCat-A-Self-Improving-Generalist-Agent-for-Robotic-Mani/01_overview.md) | 1 | 4 |
| pr-0737 | [IndustReal: Transferring Contact-Rich Assembly Tasks from Simulation to Reality](../../2023/RSS/2023_RSS_IndustReal-Transferring-Contact-Rich-Assembly-Tasks-from-S/01_overview.md) | 2 | 3 |
| pr-0768 | [Volumetric Environment Representation for Vision-Language Navigation](../../2024/CVPR/2024_CVPR_Volumetric-Environment-Representation-for-Vision-Language/01_overview.md) | 2 | 4 |
| pr-0828 | [Biped Walking Pattern Generation by using Preview Control of Zero-Moment Point](../../2003/ICRA/2003_ICRA_Biped-Walking-Pattern-Generation-by-using-Preview-Control/01_overview.md) | 4 | 3, 4, 5 |
| pr-0846 | [robosuite: A Modular Simulation Framework and Benchmark for Robot Learning](../../2020/arXiv/2020_arXiv_robosuite-A-Modular-Simulation-Framework-and-Benchmark-for/01_overview.md) | 1 | 3 |
| pr-0853 | [Human-level control through deep reinforcement learning](../../2015/Nature/2015_Nature_Human-level-control-through-deep-reinforcement-learning/01_overview.md) | 3 | 1, 6, 7 |
| pr-0857 | [A Generalist Agent](../../2022/arXiv/2022_arXiv_A-Generalist-Agent/01_overview.md) | 1 | 4 |
| pr-0924 | [FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation](../../2025/AAAI/2025_AAAI_FlowPolicy-Enabling-Fast-and-Robust-3D-Flow-Based-Policy-v/01_overview.md) | 1 | 4 |
| pr-0946 | [LIO-SAM: Tightly-coupled Lidar Inertial Odometry via Smoothing and Mapping](../../2020/IROS/2020_IROS_LIO-SAM-Tightly-coupled-Lidar-Inertial-Odometry-via-Smooth/01_overview.md) | 1 | 4 |
