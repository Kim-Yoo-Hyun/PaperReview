# PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / ICCV
- Authors: Hanxiao Jiang, Hao-Yu Hsu, Kaifeng Zhang, Hsin-Ni Yu, Shenlong Wang, Yunzhu Li
- Category: Robotics-Enabling 3D Perception
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: Robotics, deformable, inverse-physics, gaussian-splatting, motion-planning
- Aliases: PhysTwin
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.html
- Venue verification: https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.html
- Code/Project: https://jianghanxiao.github.io/phystwin-web/
- Code: https://github.com/Jianghanxiao/PhysTwin
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

PhysTwin은 몇 시점에서 관측한 동영상으로 변형 물체의 모양·물리 특성·외관을 추정해 새로운 상호작용을 예측한다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.pdf#page=1)

## Core Idea and Contribution

- 형상 사전정보로 질량–스프링 모델을 초기화하고 관측된 변형을 통해 물리 파라미터와 가우시안 외관 표현을 맞춘다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.pdf#page=5)
- 관측하지 않은 상호작용에서의 변형 예측을 평가하고 추정한 모델을 목표 형상으로 물체를 움직이는 로봇 계획에 사용했다. [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.pdf#page=8)

## Observation–State–Action Interface

부분 interaction video → geometry/물리/외관 모델 → 새 action의 simulation.

## Evaluation Scope and Claim Boundary

변형체 재구성·미래 예측·새 상호작용과 model-based robot planning 사례를 보고한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.html) · [저자 project/code](https://jianghanxiao.github.io/phystwin-web/) · [공식 code](https://github.com/Jianghanxiao/PhysTwin). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

3D 외관 재구성과 행동에 유용한 물성 모델을 구별할 직접 연결 연구다.

## Verification Boundary

material/boundary 식별성, interaction 데이터 접근, planning 평가와 reconstruction의 분리을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
