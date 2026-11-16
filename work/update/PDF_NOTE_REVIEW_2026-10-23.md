# DOC-QA1 — PDF 추출 노트 원문 대조

- 검토일: 2026-10-23 KST
- 상태: **DONE — 원문 대조·수정·검증·임시 파일 삭제 완료**
- 범위: 기존 게시 검사에서 지정한 **112개 노트 / 55편**. 같은 논문의 반복 오류도 함께 수정했다.
- 상세 근거: [논문별 PDF URL·SHA256·페이지, 파일별 수정 hash, 후속 목록](../sources/pdf_note_review_2026-10-23.json).

## 완료 범위

| 구분 | 결과 |
|---|---:|
| 요청한 112개 노트의 제어문자 오류 구간 | 253개 대조·수정 |
| 같은 논문에서 추가 발견한 22개 노트의 제어문자 구간 | 41개 대조·수정 |
| D* Lite의 제어문자 없이 남은 손상된 의사코드·표 항목 | 12개 추가 수정; 기존 대상 밖 노트 1개 포함 |
| 수정한 노트 합계 | **135개 / 55편** |
| 원문을 대조해 수정한 구간 | **306개** |
| 수정 근거가 있는 PDF 페이지 | 75개; 필요한 앞뒤 페이지도 확인 |
| 수정한 노트의 C0/C1 제어문자 잔여 | **0개** |

PDF를 임시 디렉토리에 내려받고 title·author 맥락으로 동일 연구인지 확인했다. 텍스트는 위치를 찾는 데 사용했고, 수식·표·의사코드는 렌더링한 원문 페이지로 대조했다. 접근이 제한된 OpenReview 파일은 공식 proceedings 또는 저자 arXiv 공개본으로 대체했다. 페이지는 proceedings 인쇄 번호가 아니라 **해당 다운로드본의 1부터 시작하는 PDF 페이지 번호**다. 개정본 제목·페이지 차이는 상세 기록에 남겼다.

이번은 손상된 추출 구간 및 직접 연결된 표 분류를 보정한 작업이다. 135개 노트의 모든 기존 주장에 대한 정독·재검증이나 실험 재현을 의미하지 않는다. 읽기 status·사용자 분석·tier·registry identity는 유지한다.

## 중요한 수정

- **기호를 일괄 치환하지 않았다.** 같은 NUL이 괄호, 음수 부호, Γ 등 서로 다른 glyph에 해당했다. 수식 전체가 잘린 경우 검증한 의미를 서술하고 식 번호를 연결했다.
- **방법과 결과를 구분했다.** B-spline 정의를 latency로, reward를 action output 또는 recovery로, queue API를 failure/ablation으로 배치한 표 항목을 수정했다. 원문 근거가 없는 제어 주파수·실험 결과는 채우지 않았다.
- **학습식과 구현의 차이를 남겼다.** DP3의 개념 noise loss와 implementation의 sample prediction, DDPG의 배경 Bellman 식과 target-network 구현, DreamVLA의 training-only prediction head를 구분했다.
- **오염된 각주·잘못된 anchor를 바로잡았다.** 3D-VisTA의 column 경계를 넘는 문장에 섞인 저자 각주, Instant-NGP의 figure credit, SAM2Act·MomaGraph의 공개본 페이지 차이를 확인했다.
- **D* Lite:** LPA*와 D* Lite의 탐색 방향·rhs 정의를 분리하고, 그림에서 queue 연산을 다시 확인했다. 저자 정오표는 Figure 4 line 33″의 no-known-path 주석에 `rhs(s_start)=∞`를 사용하도록 명시하며 이번 CMU PDF도 해당 표기를 사용한다. [저자 정오표](https://idm-lab.org/bib/abstracts/Koen02e.html).
- **Sampling-based Algorithms for Optimal Motion Planning:** PDF p. 25의 Theorem 31 증명에는 tail event와 complement 표기의 불일치가 원문에도 남아 있다. 깨진 식을 확정된 등식으로 복원하지 않고 그 한계를 명시했다. [원문 p. 25](https://arxiv.org/pdf/1105.1186#page=25).

## 후속 품질 점검

전체 5,185개 표준 노트를 C0/C1까지 확대 검사하니 이번 55편 밖의 **84편 / 156개 노트**에 다른 제어문자가 남아 있었다. 이 중 153개는 C0, 나머지 3개는 C1 검출에 따른 추가 대상이다. 기존 112개 NUL 대상과 별개이며 아직 원문 대조하지 않았다. [상세 기록의 `remaining_outside_scope`](../sources/pdf_note_review_2026-10-23.json)에 경로·line·codepoint·hash를 남기고 DOC-QA2로 인계한다. 제어문자 존재만으로 올바른 수식이나 사실 오류 여부를 추정하지 않는다.

`audit_note_artifacts.py`는 이제 C0/C1을 검출하고 해당 노트를 자동 cleanup에서 제외한다. `splitlines()`가 일부 제어문자를 줄 경계로 숨기던 문제도 수정했다. 회귀 검사는 제어문자 검출 및 원문 보존을 확인한다. 기존 `high` extraction-quality flag와 metadata-artifact 0건 기록은 과거 자동 추출 검사의 결과이며 본문 정확성 인증이 아니다.

**후속 완료:** 위 84편·156개 노트는 [DOC-QA2](./PDF_NOTE_REVIEW_FOLLOWUP_2026-10-23.md)에서 원문 대조·수정을 마쳤다. DOC-QA1 ledger의 `remaining_outside_scope`는 당시 인계 snapshot으로 보존하며, 현재 처리 결과·수정 후 hash는 [후속 ledger](../sources/pdf_note_review_followup_2026-10-23.json)를 따른다.

## 검증과 임시 파일 정리

수정한 135개 노트의 파일 hash와 잔여 제어문자 0개를 확인했다. `READING_STATUS.csv`, `READING_STATUS_HISTORY.csv`, `papers.json`은 작업 전후 SHA256이 일치한다. Tier 생성기와 수정한 검사 코드의 compile, tier 재생성, 문서 유지보수 회귀 검사 5개, `git diff --check`가 통과했다. 저장소 무결성 검사도 1,037편·5,185개 표준 노트에 대해 오류·경고 0개로 통과했다. 이는 위 DOC-QA2의 내용 검토 대기 항목이 해결되었다는 뜻은 아니다.

삭제 전에 다운로드본 55개의 SHA256과 수정 근거 75개 페이지의 렌더 존재를 확인했다. **이번에 받은 PDF 55개(513,014,284 bytes), 임시 이미지 213개를 포함한 작업용 파일 575개와 전용 임시 디렉토리를 삭제했다.** 기존 사용자 PDF에는 손대지 않았으며 작업 종료 시 저장소 PDF는 0개다. 원문·추출 전문·이미지 대신 URL·SHA256·페이지·수정 이력만 남겼다.

## 논문별 범위

아래 표는 실제 수정된 노트 수와 수정 근거의 PDF 페이지다.

| Paper ID | 논문 | 수정 노트 | 대조 PDF 페이지 |
|---|---|---:|---|
| pr-0495 | [Instant Neural Graphics Primitives with a Multiresolution Hash Encoding](../../2022/SIGGRAPH/2022_SIGGRAPH_Instant-Neural-Graphics-Primitives-with-a-Multiresolution/01_overview.md) | 5 | 5, 8 |
| pr-0510 | [Mip-NeRF 360: Unbounded Anti-Aliased Neural Radiance Fields](../../2022/CVPR/2022_CVPR_Mip-NeRF-360-Unbounded-Anti-Aliased-Neural-Radiance-Fields/01_overview.md) | 3 | 6 |
| pr-0947 | [FAST-LIO2: Fast Direct LiDAR-inertial Odometry](../../2022/T-RO/2022_T-RO_FAST-LIO2-Fast-Direct-LiDAR-inertial-Odometry/01_overview.md) | 3 | 4, 5 |
| pr-0479 | [GRIN: Zero-Shot Metric Depth with Pixel-Level Diffusion](../../2025/3DV/2025_3DV_GRIN-Zero-Shot-Metric-Depth-with-Pixel-Level-Diffusion/01_overview.md) | 3 | 5 |
| pr-0868 | [HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots](../../2025/ICRA/2025_ICRA_HOVER-Versatile-Neural-Whole-Body-Controller-for-Humanoid/01_overview.md) | 2 | 2 |
| pr-0683 | [Mastering Diverse Domains through World Models](../../2025/Nature/2025_Nature_Mastering-Diverse-Domains-through-World-Models/01_overview.md) | 3 | 6, 7 |
| pr-0126 | [ViSPLA: Visual Iterative Self-Prompting for Language-Guided 3D Affordance Learning](../../2025/NeurIPS/2025_NeurIPS_ViSPLA-Visual-Iterative-Self-Prompting-for-Language-Guided/01_overview.md) | 2 | 2 |
| pr-0121 | [DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge](../../2025/NeurIPS/2025_NeurIPS_DreamVLA-A-Vision-Language-Action-Model-Dreamed-with-Compr/01_overview.md) | 2 | 4 |
| pr-0436 | [SIU3R: Simultaneous Scene Understanding and 3D Reconstruction Beyond Feature Alignment](../../2025/NeurIPS/2025_NeurIPS_SIU3R-Simultaneous-Scene-Understanding-and-3D-Reconstructi/01_overview.md) | 1 | 5 |
| pr-0143 | [SAM2Act: Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation](../../2025/ICML/2025_ICML_SAM2Act-Integrating-Visual-Foundation-Model-with-A-Memory/01_overview.md) | 1 | 6 |
| pr-0137 | [SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space](../../2025/ICML/2025_ICML_SE3-Equivariant-Diffusion-Policy-in-Spherical-Fourier-Spac/01_overview.md) | 1 | 6 |
| pr-0288 | [FOCI: Trajectory Optimization on Gaussian Splats](../../2025/IROS/2025_IROS_FOCI-Trajectory-Optimization-on-Gaussian-Splats/01_overview.md) | 4 | 3 |
| pr-0056 | [VGGT: Visual Geometry Grounded Transformer](../../2025/CVPR/2025_CVPR_VGGT-Visual-Geometry-Grounded-Transformer/01_overview.md) | 1 | 3 |
| pr-0779 | [RoboGround: Robotic Manipulation with Grounded Vision-Language Priors](../../2025/CVPR/2025_CVPR_RoboGround-Robotic-Manipulation-with-Grounded-Vision-Langu/01_overview.md) | 1 | 5 |
| pr-0702 | [Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics](../../2025/arXiv/2025_arXiv_Robotic-World-Model-A-Neural-Network-Simulator-for-Robust/01_overview.md) | 1 | 4 |
| pr-0375 | [Distilling Diffusion Models to Efficient 3D LiDAR Scene Completion](../../2025/ICCV/2025_ICCV_Distilling-Diffusion-Models-to-Efficient-3D-LiDAR-Scene-Co/01_overview.md) | 4 | 3, 4 |
| pr-0390 | [Tree Skeletonization from 3D Point Clouds by Denoising Diffusion](../../2025/ICCV/2025_ICCV_Tree-Skeletonization-from-3D-Point-Clouds-by-Denoising-Dif/01_overview.md) | 3 | 4 |
| pr-0245 | [Towards Long-Horizon Vision-Language-Action System: Reasoning, Acting and Memory](../../2025/ICCV/2025_ICCV_Towards-Long-Horizon-Vision-Language-Action-System-Reasoni/01_overview.md) | 3 | 5 |
| pr-0585 | [DexTrack: Towards Generalizable Neural Tracking Control for Dexterous Manipulation from Human References](../../2025/ICLR/2025_ICLR_DexTrack-Towards-Generalizable-Neural-Tracking-Control-for/01_overview.md) | 1 | 7 |
| pr-0579 | [Geometry-aware RL for Manipulation of Varying Shapes and Deformable Objects](../../2025/ICLR/2025_ICLR_Geometry-aware-RL-for-Manipulation-of-Varying-Shapes-and-D/01_overview.md) | 1 | 5 |
| pr-0067 | [GravMAD: Grounded Spatial Value Maps Guided Action Diffusion for Generalized 3D Manipulation](../../2025/ICLR/2025_ICLR_GravMAD-Grounded-Spatial-Value-Maps-Guided-Action-Diffusio/01_overview.md) | 3 | 7 |
| pr-0602 | [OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning](../../2024/CoRL/2024_CoRL_OmniH2O-Universal-and-Dexterous-Human-to-Humanoid-Whole-Bo/01_overview.md) | 2 | 3 |
| pr-0926 | [3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations](../../2024/RSS/2024_RSS_3D-Diffusion-Policy-Generalizable-Visuomotor-Policy-Learni/01_overview.md) | 2 | 4 |
| pr-0324 | [Bayesian Diffusion Models for 3D Shape Reconstruction](../../2024/CVPR/2024_CVPR_Bayesian-Diffusion-Models-for-3D-Shape-Reconstruction/01_overview.md) | 3 | 3, 4 |
| pr-0023 | [PaLM-E: An Embodied Multimodal Language Model](../../2023/ICML/2023_ICML_PaLM-E-An-Embodied-Multimodal-Language-Model/01_overview.md) | 5 | 5, 8 |
| pr-0035 | [3D-VisTA: Pre-trained Transformer for 3D Vision and Text Alignment](../../2023/ICCV/2023_ICCV_3D-VisTA-Pre-trained-Transformer-for-3D-Vision-and-Text-Al/01_overview.md) | 3 | 1 |
| pr-0641 | [Controllability of Pushing](../../1995/ICRA/1995_ICRA_Controllability-of-Pushing/01_overview.md) | 5 | 3, 4, 5 |
| pr-0190 | [EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation](../../2026/ICRA/2026_ICRA_EveryDayVLA-A-Vision-Language-Action-Model-for-Affordable/01_overview.md) | 3 | 3 |
| pr-0188 | [OmniVLA: Physically-Grounded Multimodal VLA with Unified Multi-Sensor Perception for Robotic Manipulation](../../2026/ICRA/2026_ICRA_OmniVLA-Physically-Grounded-Multimodal-VLA-with-Unified-Mu/01_overview.md) | 1 | 4 |
| pr-0169 | [SpatioLM: Towards General Physical Spatial Intelligence in Vision-Language Models](../../2026/ICML/2026_ICML_SpatioLM-Towards-General-Physical-Spatial-Intelligence-in/01_overview.md) | 4 | 3 |
| pr-0456 | [VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency](../../2026/ICML/2026_ICML_VGGT-Motion-Motion-Aware-Calibration-Free-Monocular-SLAM-f/01_overview.md) | 3 | 4, 5 |
| pr-0463 | [Flow Equivariant World Models: Structured Memory for Dynamic Environments](../../2026/ICML/2026_ICML_Flow-Equivariant-World-Models-Structured-Memory-for-Dynami/01_overview.md) | 1 | 4 |
| pr-0161 | [Reasoning-VLA: An Efficient and Spatial-Guided General Vision-Language-Action Reasoning Model for Autonomous Driving](../../2026/ICML/2026_ICML_Reasoning-VLA-An-Efficient-and-Spatial-Guided-General-Visi/01_overview.md) | 1 | 5 |
| pr-0167 | [MapDream: Task-Driven Map Learning for Vision-Language Navigation](../../2026/ICML/2026_ICML_MapDream-Task-Driven-Map-Learning-for-Vision-Language-Navi/01_overview.md) | 2 | 4, 5 |
| pr-0817 | [AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention](../../2026/CVPR/2026_CVPR_AVA-VLA-Improving-Vision-Language-Action-Models-with-Activ/01_overview.md) | 1 | 4 |
| pr-0362 | [L3DR: 3D-aware LiDAR Diffusion and Rectification](../../2026/CVPR/2026_CVPR_L3DR-3D-aware-LiDAR-Diffusion-and-Rectification/01_overview.md) | 2 | 5 |
| pr-0794 | [EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding](../../2026/CVPR/2026_CVPR_EmbodiedSplat-Online-Feed-Forward-Semantic-3DGS-for-Open-V/01_overview.md) | 2 | 6 |
| pr-0364 | [NG-GS: NeRF-guided 3D Gaussian Splatting Segmentation](../../2026/CVPR/2026_CVPR_NG-GS-NeRF-guided-3D-Gaussian-Splatting-Segmentation/01_overview.md) | 4 | 4, 5 |
| pr-0369 | [VarSplat: Uncertainty-aware 3D Gaussian Splatting for Robust RGB-D SLAM](../../2026/CVPR/2026_CVPR_VarSplat-Uncertainty-aware-3D-Gaussian-Splatting-for-Robus/01_overview.md) | 4 | 4, 5 |
| pr-0350 | [Gau-Occ: Geometry-Completed Gaussians for Multi-Modal 3D Occupancy Prediction](../../2026/CVPR/2026_CVPR_Gau-Occ-Geometry-Completed-Gaussians-for-Multi-Modal-3D-Oc/01_overview.md) | 2 | 5 |
| pr-0686 | [Dexterous World Models](../../2026/CVPR/2026_CVPR_Dexterous-World-Models/01_overview.md) | 4 | 3 |
| pr-0694 | [FM-Steer: Enhance Generalist Policies with Value-Guided Cascaded Denoising](../../2026/CVPR/2026_CVPR_FM-Steer-Enhance-Generalist-Policies-with-Value-Guided-Cas/01_overview.md) | 1 | 3 |
| pr-0801 | [GA-VLN: Geometry-Aware BEV Representation for Efficient Vision-Language Navigation](../../2026/CVPR/2026_CVPR_GA-VLN-Geometry-Aware-BEV-Representation-for-Efficient-Vis/01_overview.md) | 2 | 4 |
| pr-0356 | [Distilling Unsigned Distance Function for Surface Reconstruction from 3D Gaussian Splatting](../../2026/CVPR/2026_CVPR_Distilling-Unsigned-Distance-Function-for-Surface-Reconstr/01_overview.md) | 1 | 4 |
| pr-0428 | [SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors](../../2026/ICLR/2026_ICLR_SurfSplat-Conquering-Feedforward-2D-Gaussian-Splatting-wit/01_overview.md) | 3 | 6, 15 |
| pr-0096 | [MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning](../../2026/ICLR/2026_ICLR_MomaGraph-State-Aware-Unified-Scene-Graphs-with-Vision-Lan/01_overview.md) | 4 | 6 |
| pr-0697 | [Learning to Be Uncertain: Pre-training World Models with Horizon-Calibrated Uncertainty](../../2026/ICLR/2026_ICLR_Learning-to-Be-Uncertain-Pre-training-World-Models-with-Ho/01_overview.md) | 3 | 5 |
| pr-0587 | [Rodrigues Network for Learning Robot Actions](../../2026/ICLR/2026_ICLR_Rodrigues-Network-for-Learning-Robot-Actions/01_overview.md) | 1 | 4, 5 |
| pr-0097 | [Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model](../../2026/ICLR/2026_ICLR_Spatial-Forcing-Implicit-Spatial-Representation-Alignment/01_overview.md) | 3 | 3 |
| pr-0105 | [EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation](../../2026/ICLR/2026_ICLR_EquAct-An-SE3-Equivariant-Multi-Task-Transformer-for-3D-Ro/01_overview.md) | 3 | 5 |
| pr-0634 | [Learning Latent Plans from Play](../../2020/CoRL/2020_CoRL_Learning-Latent-Plans-from-Play/01_overview.md) | 1 | 11 |
| pr-0680 | [Dream to Control: Learning Behaviors by Latent Imagination](../../2020/ICLR/2020_ICLR_Dream-to-Control-Learning-Behaviors-by-Latent-Imagination/01_overview.md) | 2 | 2, 3, 4, 5 |
| pr-0557 | [Sampling-based Algorithms for Optimal Motion Planning](../../2011/IJRR/2011_IJRR_Sampling-based-Algorithms-for-Optimal-Motion-Planning/01_overview.md) | 1 | 25 |
| pr-0616 | [Continuous Control with Deep Reinforcement Learning](../../2016/ICLR/2016_ICLR_Continuous-Control-with-Deep-Reinforcement-Learning/01_overview.md) | 3 | 3 |
| pr-0553 | [D* Lite](../../2002/AAAI/2002_AAAI_D-Lite/01_overview.md) | 5 | 2, 3, 4, 5 |
