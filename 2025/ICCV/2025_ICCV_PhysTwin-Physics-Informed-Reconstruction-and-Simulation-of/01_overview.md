# PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
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
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다.

## Problem and Importance

관측한 변형만 재현하는 모델은 새로운 물리적 상호작용을 예측하기 어렵다.

## Core Idea and Contribution

물리 simulation·geometry·Gaussian rendering을 결합해 상호작용 영상에서 역모델링한다.

## Observation–State–Action Interface

부분 interaction video → geometry/물리/외관 모델 → 새 action의 simulation.

## Evaluation Scope and Claim Boundary

변형체 재구성·미래 예측·새 상호작용과 model-based robot planning 사례를 보고한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.html) · [저자 project/code](https://jianghanxiao.github.io/phystwin-web/) · [공식 code](https://github.com/Jianghanxiao/PhysTwin). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

3D 외관 재구성과 행동에 유용한 물성 모델을 구별할 직접 연결 연구다.

## Verification Boundary

material/boundary 식별성, interaction 데이터 접근, planning 평가와 reconstruction의 분리을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
