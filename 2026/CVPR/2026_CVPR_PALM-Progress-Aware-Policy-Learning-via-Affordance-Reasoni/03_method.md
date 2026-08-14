# Method

- Year/Venue: 2026 / CVPR
- Category: VLA and Generalist Robot Policies
- Tags: Robotics, VLA, affordance, progress estimation, long-horizon manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_CVPR_2026_paper.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- To address these challenges, we introduce PALM, a VLA framework that structures policy learning around interaction-centric affordance reasoning and subtask progress cues.

## 원리적 동기
- Existing methods lack internal reasoning mechanisms that can identify task-relevant interaction cues or track progress within a subtask, leading to critical execution errors such as repeated actions, missed ...
- Although existing models may infer the final goal and produce intermediate actions , they lack internal representations that disambiguate which object should be targeted next, which part or ...
- To address these challenges, we introduce PALM, a VLA framework that structures policy learning around interaction-centric affordance reasoning and subtask progress cues.

## 핵심 방법론
- Ablation studies of affordance components on CALVIN ABC D and LIBERO-LONG benchmarks demonstrate the effectiveness of the four components of affordance prediction. increases (e.g., 82.0% for five consecutive ...
- This is a +17.7% absolute improvement over the strongest prior baseline (Seer at 64.3%) at the 5-task horizon.
- PALM also yields the longest average task trajectory (4.48), exceeding Seer (3.98) and ⇡0 (3.92), indicating significantly more stable execution over extended sequences.
- Importantly, results confirm that the progress-aware policy is critical for longhorizon generalization, as removing the progress prediction (PALM 7 progress) reduces performance consistently across horizons (e.g., average length ...
- Moreover, as shown in Table 2, across all four LIBERO suites, PALM achieves state-of-the-art performance with an average success rate of 94.5%.
