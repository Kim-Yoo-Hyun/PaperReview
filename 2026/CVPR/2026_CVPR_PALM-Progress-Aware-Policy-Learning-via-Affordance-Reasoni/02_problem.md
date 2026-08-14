# Problem

- Year/Venue: 2026 / CVPR
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, affordance, progress estimation, long-horizon manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_CVPR_2026_paper.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- Existing methods lack internal reasoning mechanisms that can identify task-relevant interaction cues or track progress within a subtask, leading to critical execution errors such as repeated actions, missed ...
- Although existing models may infer the final goal and produce intermediate actions , they lack internal representations that disambiguate which object should be targeted next, which part or ...
- To address these challenges, we introduce PALM, a VLA framework that structures policy learning around interaction-centric affordance reasoning and subtask progress cues.

## 해결하려는 문제
- Across extensive simulation and real-world experiments, PALM consistently outperforms baselines, achieving a 91.8% success rate on LIBERO-LONG, a 12.5% improvement in average length on CALVIN ABC D, and ...
- To address these challenges, we introduce PALM, a VLA framework that structures policy learning around interaction-centric affordance reasoning and subtask progress cues.
- For example, on “clean a cluttered table,” state-of-the-art policies typically succeed initially but fail mid-task, unable to reliably complete the full sequence.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
