# GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping

> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-20 게재본의 표제면·방법·평가 절 대조. [게재 정보](https://openaccess.thecvf.com/content_CVPR_2020/html/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.html) · [원문](https://openaccess.thecvf.com/content_CVPR_2020/papers/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.pdf)

- Year/Venue: 2020 / CVPR
- Authors: Hao-Shu Fang, Chenxi Wang, Minghao Gou, Cewu Lu
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, grasping, Benchmark, 6-DoF grasp
- Official paper: https://openaccess.thecvf.com/content_CVPR_2020/html/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.html
- Code/Project: https://graspnet.net/

## Why This Paper Is Here

GraspNet-1Billion은 복잡하게 쌓인 물체의 RGB-D 관측, 6자유도 파지 자세, 분석적 판정 절차와 점군 기반 기준 모델을 함께 제공한다.

## Main Claims and Actual Contribution

- 장면과 물체 좌표를 연결해 파지 주석을 구성하고, 후보 자세를 물리적 기준으로 평가한다. 기준 네트워크는 점군에서 접근 방향과 그 밖의 파지 파라미터를 나누어 예측한다. §§3–4.
- 게재본은 97,280장의 RGB-D 영상과 10억 개 이상의 파지 자세를 보고한다. 데이터 규모는 초록 및 §3, 방법 간 비교와 실제 파지 비교는 §5에서 확인할 수 있다.

## Evaluation Scope

분석적 파지 점수와 실물 파지의 대응은 논문이 시험한 물체·그리퍼와 조건에서 평가했다.

## 배포 범위 대조

- 코드 — 저자 구현 파일 · models/graspnet.py [배포 파일](https://raw.githubusercontent.com/graspnet/graspnet-baseline/280c215129f759ed8649cb4e89fc5dfee55f4f80/models/graspnet.py)
- 가중치 — GraspNet 기준 모델의 RealSense 학습 가중치 파일이다. [배포 파일](https://drive.google.com/file/d/1hd0G8LN6tRpi4742XOTEisbTXNZ-1jmk/view)
- 데이터 — 공식 학습 자료의 첫 분할 배포 파일이다. [배포 파일](https://drive.google.com/file/d/1wQx8IJ_Lok3hVK_nchQUzgw88QBGZ5iq/view)
