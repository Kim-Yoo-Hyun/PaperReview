# UA-Pose: Uncertainty-Aware 6D Object Pose Estimation and Online Object Completion with Partial References

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 표시한 평가 항목을 확인했다.
> Source audit: 2026-11-24 원문 대조.

## Evaluation in One Sentence

평가는 RGB-D 시퀀스의 6D 자세 정확도와 온라인 형상 완성도다. 자세에는 ADD·ADD-S의 곡선 아래 면적을, 형상에는 Chamfer 거리를 사용했다. [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.pdf#page=8)

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.

## Dataset / Benchmark Role

YCB-Video의 물체 영상, YCBInEOAT의 양팔 로봇 조작, HO3D의 사람 손 조작 영상을 사용했다. [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.pdf#page=7)

## Metrics and Success Definition

ADD·ADD-S AUC와 Chamfer 거리는 추정·재구성 지표다. 이 실험에서 로봇 정책의 과제 성공률은 측정하지 않았다. [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.pdf#page=8)

## Proposed Evaluation — Researcher Interpretation

관측 coverage를 맞추고 completion 유무의 pose 오차와 downstream 배치 오류를 분리한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2025/html/Li_UA-Pose_Uncertainty-Aware_6D_Object_Pose_Estimation_and_Online_Object_Completion_CVPR_2025_paper.html) · [저자 project/code](https://minfenli.github.io/UA-Pose/) · [공식 저장소(구현 공개 미확인)](https://github.com/minfenli/UA-Pose).
