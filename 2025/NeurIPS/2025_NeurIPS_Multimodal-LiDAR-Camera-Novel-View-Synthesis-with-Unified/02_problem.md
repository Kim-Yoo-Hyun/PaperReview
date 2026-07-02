# Problem

- Year/Venue: 2025 / NeurIPS poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: geometry, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Multimodal-LiDAR-Camera-Novel-View-Synthesis-with-Unified/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Nevertheless, prior research has faced challenges due to the signiﬁcant domain gap and uncoordinated convergence problems between these modalities.
- To alleviate modality conﬂicts and address the uncoordinated convergence problem, we introduce a multimodal-speciﬁc coarse-to-ﬁne training approach , facilitating the utilization of a singular hash grid for compact ...
- Regarding the challenges encountered in the aforementioned single-modality approach, Continuous Neural LiDAR Fields can provide pixel-wise depth supervision for images and directly propagate gradients to pose estimation, providing ...

## 해결하려는 문제
- Besides, to alleviate the domain gap between modalities, we propose a multimodal-speciﬁc coarse-to-ﬁne training approach for uniﬁed, compact reconstruction.
- In light of this, we propose MUP, a pose-free framework for LiDAR-Camera joint NVS in largescale scenes.
- Moreover, to further guide pose optimization of NeRF, we propose a multimodal geometric optimizer that leverages geometric relations from point clouds and photometric regularization from adjacent image frames.

## 선행 연구 / 배경 단서
- Nevertheless, prior research has faced challenges due to the signiﬁcant domain gap and uncoordinated convergence problems between these modalities.
- To alleviate modality conﬂicts and address the uncoordinated convergence problem, we introduce a multimodal-speciﬁc coarse-to-ﬁne training approach , facilitating the utilization of a singular hash grid for compact ...
- In summary, our primary contributions can be delineated as follows: (1) We propose MUP, a uniﬁed pose-free framework that combines the advantages of two modalities for pose estimation ...
