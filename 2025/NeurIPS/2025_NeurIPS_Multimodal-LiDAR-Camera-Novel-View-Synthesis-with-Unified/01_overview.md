# Multimodal LiDAR-Camera Novel View Synthesis with Unified Pose-free Neural Fields

- Year/Venue: 2025 / NeurIPS poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: geometry, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Multimodal-LiDAR-Camera-Novel-View-Synthesis-with-Unified/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Nevertheless, prior research has faced challenges due to the signiﬁcant domain gap and uncoordinated convergence problems between these modalities.
- To alleviate modality conﬂicts and address the uncoordinated convergence problem, we introduce a multimodal-speciﬁc coarse-to-ﬁne training approach , facilitating the utilization of a singular hash grid for compact ...
- Regarding the challenges encountered in the aforementioned single-modality approach, Continuous Neural LiDAR Fields can provide pixel-wise depth supervision for images and directly propagate gradients to pose estimation, providing ...

## Core Idea
- Besides, to alleviate the domain gap between modalities, we propose a multimodal-speciﬁc coarse-to-ﬁne training approach for uniﬁed, compact reconstruction.
- Moreover, to further guide pose optimization of NeRF, we propose a multimodal geometric optimizer that leverages geometric relations from point clouds and photometric regularization from adjacent image frames.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Thus, compared to single-modality methods and i-NGP that with and without point clouds for depth supervision, we achieve highquality NVS and the best results across both modalities.
- The results indicate that relying solely on NeRF’s implicit pose optimization fails to achieve accurate pose estimates and leads to convergence at local optima.
- Therefore, we exclude the MMG and conduct ablation experiments with GT pose to further demonstrate the advantages of our Uniﬁed NeRF with the multimodal-speciﬁc coarseto-ﬁne training strategy (MSC2F) ...

## Limitation
- We revisit the limitations of single-modality pose-free methods in large-scale scenes.

## Contribution
- Besides, to alleviate the domain gap between modalities, we propose a multimodal-speciﬁc coarse-to-ﬁne training approach for uniﬁed, compact reconstruction.
- In light of this, we propose MUP, a pose-free framework for LiDAR-Camera joint NVS in largescale scenes.
- Moreover, to further guide pose optimization of NeRF, we propose a multimodal geometric optimizer that leverages geometric relations from point clouds and photometric regularization from adjacent image frames.

## Abstract Cue
- Pose-free Neural Radiance Field (NeRF) aims at novel view synthesis (NVS) without relying on accurate poses, exhibiting signiﬁcant practical value.
