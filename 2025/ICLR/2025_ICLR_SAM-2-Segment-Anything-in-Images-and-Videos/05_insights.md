# Insights

## Limitation
- 2D/video mask prediction에 집중하므로 metric geometry, 3D occupancy, physical interaction은 직접 해결하지 않는다.
- memory가 강점이지만 wrong mask가 memory에 들어가면 error accumulation이 생길 수 있다.
- object identity는 visual/mask memory에 의존하므로 severe viewpoint change, reflective/transparent objects, robot motion blur에서 추가 검증이 필요하다.
- promptable segmentation은 open-world perception의 좋은 interface지만, semantic label, affordance, action feasibility는 별도 모델과 결합해야 한다.

## Strength
- image와 video segmentation을 하나의 foundation formulation으로 묶었다.
- streaming memory 구조가 단순하면서도 real-time/interactive use case에 맞다.
- SA-V dataset은 object/part/occlusion/reappearance coverage가 넓어 downstream video/robot perception 연구의 data foundation이 된다.
- SAM 계열의 2D mask prior를 video-consistent prior로 확장했기 때문에 3D semantic mapping에 더 적합하다.

## Paper Claim
SAM 2는 promptable visual segmentation의 image-only 한계를 넘어 image/video를 통합하는 foundation model이며, 더 적은 user interaction으로 더 정확한 video masklet을 만들고 image segmentation에서도 SAM보다 빠르고 강하다.

## Future Work
- SAM 2 masklet + camera pose/depth를 결합한 temporally consistent 3D semantic map.
- memory error accumulation을 3D geometry consistency로 검출하고 정정하는 방법.
- Gaussian Splatting/NeRF feature field에 SAM2 masklet을 distill하여 open-vocabulary object field를 구축.
- robot manipulation에서 object part masklet을 affordance/contact region으로 연결.
- active perception policy가 uncertain masklet을 줄이기 위해 next best view나 clarification prompt를 선택하는 방식.

## 내 관점
SAM 2는 3D CV 논문은 아니지만, 최신 3D semantic alignment 논문들이 의존하는 2D/video mask foundation이다. 3D Vision + Robotics 연구에서는 "좋은 2D mask를 얻는 모델"이 아니라, temporal object prior를 3D memory와 어떻게 결합할지의 출발점으로 읽어야 한다.
