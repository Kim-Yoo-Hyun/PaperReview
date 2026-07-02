# Method

- Year/Venue: 2026 / CVPR
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLM, Planning, simulation
- Paper link: ./2026/CVPR/2026_CVPR_SIMPACT-Simulation-Enabled-Action-Planning-using-Vision-La/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To overcome this, we present SIMPACT, a test-time, SIMulation-enabled ACTion Planning framework that equips VLMs with physical reasoning through simulation-in-the-loop world modeling, without requiring any additional training.
- Success rates (%) over 10 trials for each task after removing each component of our method.
- In contrast, our method integrates simulation-enabled reasoning with VLM, enabling the robot to iteratively refine its 4.3.

## 원리적 동기
- This limitation arises from training VLMs on static internet-scale visual-language data that contain no causal interactions or action-conditioned changes.
- However, they lack a grounded understanding of physical dynamics.
- To overcome this, we present SIMPACT, a test-time, SIMulation-enabled ACTion Planning framework that equips VLMs with physical reasoning through simulation-in-the-loop world modeling, without requiring any additional training.

## 핵심 방법론
- Success rates (%) over 10 trials for each task after removing each component of our method.
- In contrast, our method integrates simulation-enabled reasoning with VLM, enabling the robot to iteratively refine its 4.3.
- We compare our approach against the following baselines: (1) VLA models that are trained on largescale robot action datasets to directly predict joint velocities from visual observations and ...
- We use ⇡0.5 , a recent open-source VLA model pretrained on a large robot manipulation dataset, as a representative base- 20795 line. (2) VLM-based methods that leverage geometric ...
- We use Google Gemini 2.5 Pro as the default VLM and generate K = 10 initial action proposals, setting Kmax = 13, corresponding to a maximum of 3 ...
