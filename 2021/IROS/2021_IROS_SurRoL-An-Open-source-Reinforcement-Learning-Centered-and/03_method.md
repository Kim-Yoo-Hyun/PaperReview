# Method

- Year/Venue: 2021 / IROS
- Category: Robot Learning and Data
- Tags: Robotics, surgical robotics, Reinforcement Learning, simulation, sim-to-real, dexterous manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/med-air/SurRoL
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- — Autonomous surgical execution relieves tedious routines and surgeon’s fatigue.
- Recent learning-based methods, especially reinforcement learning (RL) based methods, achieve promising performance for dexterous manipulation, which usually requires the simulation to collect data efficiently and reduce the hardware ...
- The existing learning-based simulation platforms for medical robots suffer from limited scenarios and simplified physical interactions, which degrades the real-world performance of learned policies.

## 원리적 동기
- The existing learning-based simulation platforms for medical robots suffer from limited scenarios and simplified physical interactions, which degrades the real-world performance of learned policies.
- However, robot learning typically requires a large amount of labeled data and interactions with the environment , , , usually infeasible on real surgical robots due to the ...
- — Autonomous surgical execution relieves tedious routines and surgeon’s fatigue.

## 핵심 방법론
- Approx @2mm Interact Approx @1mm Success Rate (%) Approx Approx @2mm @3mm 36.0±12.4 76.5±4.3 88.8±5.9 34.2±16.5 52.5±9.6 70.7±19.9 76.8±14.2 81.3±1.5 Interact B.
- Deployment on the Real-World dVRK To demonstrate transferability, we conduct physical experiments by deploying the policies trained in SurRoL to the real-world dVRK platform.
- Four tasks, PSM GauzeRetrieve, NeedlePick, PegTransfer, and ECM StaticTrack, are selected for demonstration.
- Thanks to the compatible dVRK interface, we can smoothly transfer the learned skills, with experiment snapshots shown in Fig.
- For the first three PSM tasks, we set up the physical experiment following the setting of and carefully align a 10cm2 workspace to ensure consistency between the simulated ...
