# Evaluation

- Year/Venue: 2018 / TOG / SIGGRAPH
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, humanoid, motion imitation, Reinforcement Learning, physics-based control
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/xbpeng/DeepMimic
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- success rate

## Evaluation Protocol and Results
- Results for the humanoid are demonstrated for a large collection of locomotion, acrobatic, and martial arts skills, while the results for the dragon and T-Rex are demonstrated for ...
- For characters such as the T-Rex and dragon, where mocap data is not available, we demonstrate that our framework is also capable of learning skills from artist-authored keyframes.
- These results suggest that simply imitating the reference motions is not sufficient to successfully perform the tasks.
- Character Retargeting: To demonstrate the system’s capabilities in retargeting motions to different characters, we trained policies for walking, running, backflips and spinkicks on a simulated model of the ...
- Results for the humanoid are demonstrated for a large collection of locomotion, acrobatic, and martial arts skills, while the results for the dragon and T-Rex are demonstrated for ...
- For characters such as the T-Rex and dragon, where mocap data is not available, we demonstrate that our framework is also capable of learning skills from artist-authored keyframes.

## Baselines
- To investigate the extent to which the motions are adapted for a particular task, we compared the performance of policies trained to optimize both the imitation objective r ...
- For locomotion skills such as walking and running, our policies produce natural gaits that avoid many of the artifacts exhibited by previous deep RL methods [Merel et al.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
