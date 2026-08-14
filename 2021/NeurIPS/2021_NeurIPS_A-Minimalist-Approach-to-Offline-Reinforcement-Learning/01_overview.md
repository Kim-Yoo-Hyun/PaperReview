# A Minimalist Approach to Offline Reinforcement Learning

- Year/Venue: 2021 / NeurIPS
- Category: Robot Learning and Data
- Tags: Robotics, offline reinforcement learning, behavior cloning, continuous control
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/sfujim/TD3_BC
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- The solution class for this problem revolves around the idea that the learned policy should be kept close to the data-generating process (or behavior policy), and has been ...
- In other cases, there are unmentioned hyperparameters, or secondary components, such as generative models, which make offline RL algorithms difficult to reproduce, and even more challenging to tune.
- Additionally, such mixture of details slow down the run times of the algorithms, and make causal attributions of performance gains and transfers of techniques across algorithms difficult, as ...

## Core Idea
- Due to errors in value estimation from out-of-distribution actions, most offline RL algorithms take the approach of constraining or regularizing the policy with the actions contained in the ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We find that we can match the performance of state-of-the-art offline RL algorithms by simply adding a behavior cloning term to the policy update of an online RL ...
- Our offline RL baselines include two state-of-the-art algorithms, CQL [Kumar et al., 2020] and Fisher-BRC [Kostrikov et al., 2021], as well as BRAC [Wu et al., 2019] and ...
- We evaluate our proposed approach on the D4RL benchmark of OpenAI gym MuJoCo tasks [Todorov et al., 2012, Brockman et al., 2016, Fu et al., 2020], which encompasses ...

## Limitation
- Additionally, we highlight existing open challenges in offline RL research, including not only the extra implementation, computation, and hyperparameter-tuning complexities that we successfully address in this work, but ...
- Finally, we believe the sheer simplicity of our approach highlights a possible overemphasis on algorithmic complexity made by the community, and we hope to inspire future work to ...

## Contribution
- Due to errors in value estimation from out-of-distribution actions, most offline RL algorithms take the approach of constraining or regularizing the policy with the actions contained in the ...
- We find that we can match the performance of state-of-the-art offline RL algorithms by simply adding a behavior cloning term to the policy update of an online RL ...
- Built on pre-existing RL algorithms, modifications to make an RL algorithm work offline comes at the cost of additional complexity.

## Abstract Cue
- Offline reinforcement learning (RL) defines the task of learning from a fixed batch of data.
