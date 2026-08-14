# Method

- Year/Venue: 2022 / CVPR
- Category: Robotics-Enabling 3D Perception
- Tags: Robotics, 3D Vision, digital twin, articulated objects, interaction, implicit representation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://ut-austin-rpl.github.io/Ditto/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- We introduce Ditto to learn articulation model estimation and 3D geometry reconstruction of an articulated object through interactive perception.
- Conclusion We introduce Ditto, an implicit neural representationbased model for recreating digital twins of articulated objects through interactive perception.
- We hope to extend our method to reconstruct the full kinematic tree of a composite object with multiple joints and parts via consecutive interactions and aggregation of model ...

## 원리적 동기
- Digitizing physical objects into the virtual world has the potential to unlock new research and applications in embodied AI and mixed reality.
- This work focuses on recreating interactive digital twins of real-world articulated objects, which can be directly imported into virtual environments.
- We introduce Ditto to learn articulation model estimation and 3D geometry reconstruction of an articulated object through interactive perception.

## 핵심 방법론
- Conclusion We introduce Ditto, an implicit neural representationbased model for recreating digital twins of articulated objects through interactive perception.
- We hope to extend our method to reconstruct the full kinematic tree of a composite object with multiple joints and parts via consecutive interactions and aggregation of model ...
- In our current model, we use two separate decoders in PointNet++ for geometry and articulation.
- We use interactions to create novel sensory data for inferring articulation.
- We use a simulated robot arm to interact with the digital twin and transfer the actions back to the real world after calibrating the simulated and real robot ...
