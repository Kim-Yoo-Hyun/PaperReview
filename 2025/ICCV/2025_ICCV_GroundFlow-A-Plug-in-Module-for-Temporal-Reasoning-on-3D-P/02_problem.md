# Problem

- Year/Venue: 2025 / ICCV
- Category: 3D Vision-Language Grounding
- Tags: 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_GroundFlow-A-Plug-in-Module-for-Temporal-Reasoning-on-3D-P/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Effectively retrieving relevant previous information is essential for solving this problem, yet current visual grounding methods lack a design for temporal fusion.
- Due to the lack of an effective module for collecting related historical information, state-of-theart 3DVG methods face significant challenges in adapting to the SG3D task.
- However, these methods are primarily designed for object-centric 3DVG tasks and face significant challenges when applied to sequential grounding tasks.

## 해결하려는 문제
- Training Objective Following the SG3D benchmark , we use the same cross-entropy loss to optimize the dual-stream model and the query-based model.
- This allows GroundFlow to improve the 3DVG baseline methods consistently as task steps increases. • We achieve state-of-the-art performance on SG3D benchmark across five datasets without using large ...
- While 3D LLMs achieve state-of-the-art results in various 3D tasks, they still face significant difficulty adapting to the complex SG3D problem .

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
