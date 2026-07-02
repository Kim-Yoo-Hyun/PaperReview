# Method

- Year/Venue: 2025 / IROS
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting
- Paper link: ./2025/IROS/2025_IROS_FOCI-Trajectory-Optimization-on-Gaussian-Splats/paper.pdf
- Code/Project: https://rffr.leggedrobotics.com/works/foci/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Contrary to other approaches, which represent the robot with conservative bounding boxes that underestimate the traversability of the environment, we propose to represent the environment and the robot ...
- Safety Dist. (m) 0.51 0.56 0.27 TABLE III: Comparisons of the performance of our method with a similar 3DGS based planner and simple RRT* planner.
- In Figure 6 we compare the effect of more complex robot Gaussians on the solve time for large complex scenes such as Stonehenge.

## 원리적 동기
- However, they suffer from having slow inference speeds because new views have to be created using a computationally expensive ray-casting procedure.
- Contrary to other approaches, which represent the robot with conservative bounding boxes that underestimate the traversability of the environment, we propose to represent the environment and the robot ...

## 핵심 방법론
- Safety Dist. (m) 0.51 0.56 0.27 TABLE III: Comparisons of the performance of our method with a similar 3DGS based planner and simple RRT* planner.
- In Figure 6 we compare the effect of more complex robot Gaussians on the solve time for large complex scenes such as Stonehenge.
- The computation time is generally linear with the number of environmental Gaussians, robot Gaussians, and collision discretization points.
- In the realistic environments, the larger scenes resulted in a longer A* search time, while the more complex 3 Gaussian robot slightly increases the general solve time.
- Due to this unique ability to model the robot as a collection of Gaussians and therefore consider the robot’s orientation, the smaller safety corridor allowed for slightly shorter ...
