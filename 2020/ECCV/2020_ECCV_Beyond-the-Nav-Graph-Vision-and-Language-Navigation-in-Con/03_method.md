# Method

- Year/Venue: 2020 / ECCV
- Category: Navigation and Embodied AI
- Tags: Vision-Language Navigation, Robotics, Navigation, Benchmark
- Paper link: ./2020/ECCV/2020_ECCV_Beyond-the-Nav-Graph-Vision-and-Language-Navigation-in-Con/paper.pdf
- Code/Project: https://jacobkrantz.github.io/vlnce/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We develop a language-guided navigation task set in a continuous 3D environment where agents must execute low-level actions to follow natural language navigation directions.
- To contextualize this new task, we develop models that mirror many of the advances made in prior settings as well as single-modality baselines.

## 원리적 동기
- This paradigm enables efficient data collection and high visual fidelity compared to 3D scanning or creating synthetic environments; however, scenes are only observed from a sparse set of ...
- By being situated in continuous environments, this setting lifts a number of assumptions implicit in prior work that represents environments as a sparse graph of panoramas with edges ...
- We develop a language-guided navigation task set in a continuous 3D environment where agents must execute low-level actions to follow natural language navigation directions.

## 핵심 방법론
- Springing forth from the pages of science fiction and capturing the daydreams of weary chore-doers everywhere, the promise and potential of general-purpose robotic assistants that follow natural language ...
- Taking a small step towards this goal, recent work has begun developing artificial agents that follow natural language navigation instructions in perceptually-rich, simulated environments .
- An example instruction might be “Go down the hall and turn left at the wooden desk.
- Continue until you reach the kitchen and then stop by the kettle.” and agents are evaluated by their ability to follow the described path in (potentially novel) simulated ...
- Many of these tasks have been developed from datasets of panoramic images captured in real scenes – e.g.
