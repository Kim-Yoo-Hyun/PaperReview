# Method

- Year/Venue: 2026 / CVPR
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, VLA, force sensing, hybrid force-position control, contact-rich manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://openaccess.thecvf.com/content/CVPR2026/html/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- We propose ForceVLA2, an end-to-end vision–language–action framework that equips robots with hybrid force-position control and explicit force awareness.
- Conclusion We present ForceVLA2, a force-aware vision-languageaction framework with hybrid force–position control for contact-rich manipulation, and evaluate it on our ForceVLA2-Dataset of five real-world tasks.
- 2, we conduct a stepwise ablation in which we progressively add the Force Prompt (FP), Cross-Scale MoE (CM), and Multimodal Encoder (ME) modules on top of π0 , ...

## 원리적 동기
- To overcome this limitation, vision–language–action models (VLAs) extend VLMs toward physical intelligence by seamlessly connecting perception and reasoning to embodied interaction.
- However, these models remain confined to virtual domains, lacking the embodiment necessary for authentic physical understanding and interaction in real-world settings.
- We propose ForceVLA2, an end-to-end vision–language–action framework that equips robots with hybrid force-position control and explicit force awareness.

## 핵심 방법론
- Conclusion We present ForceVLA2, a force-aware vision-languageaction framework with hybrid force–position control for contact-rich manipulation, and evaluate it on our ForceVLA2-Dataset of five real-world tasks.
- 2, we conduct a stepwise ablation in which we progressively add the Force Prompt (FP), Cross-Scale MoE (CM), and Multimodal Encoder (ME) modules on top of π0 , ...
- In the Retrieve Plate task, ForceVLA2 explores the sandbox through forceguided probing; even after an initial failed grasp, it autonomously retries, showcasing robust adaptation. duce the additional modules ...
- Additional experiments focusing on the Multimodal Encoder are provided in the Appendix C.
