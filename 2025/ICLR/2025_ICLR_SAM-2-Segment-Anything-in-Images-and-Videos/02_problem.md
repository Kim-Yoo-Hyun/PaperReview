# Problem

## 왜 문제인가
실제 환경의 perception은 정지 이미지보다 video stream에 가깝다. 로봇 카메라, AR/VR, 자율주행, manipulation view에서는 객체가 움직이고, 부분적으로 가려지고, 화면 밖으로 나갔다가 다시 등장한다. 기존 SAM은 image-level promptable segmentation의 강한 foundation이지만, frame 사이의 temporal identity와 memory가 없어서 같은 객체를 일관되게 유지하기 어렵다.

## 해결하려는 문제
- image와 video segmentation을 분리하지 않고 하나의 promptable task로 통합한다.
- 사용자가 point/box/mask prompt를 일부 frame에만 제공해도 video 전체의 masklet을 얻는다.
- 잘못된 frame에 추가 prompt를 주면 전체 masklet이 interactive하게 refinement되도록 한다.
- 기존 VOS dataset이 특정 object class, whole object, 짧은 video에 편중된 문제를 줄인다.

## 선행 연구 분석
- SAM: image promptable segmentation foundation. 강력하지만 temporal memory가 없다.
- VOS/semi-supervised VOS: 첫 frame mask를 받아 추적하지만, promptable refinement나 arbitrary object/part coverage가 제한적이다.
- SAM + tracker pipeline: SAM으로 initial mask를 만들고 tracker로 propagate하지만, tracker failure 후 correction이 비효율적이고 통합 모델이 아니다.
- 기존 VOS datasets: DAVIS, YouTube-VOS, MOSE 등은 유용하지만 "segment anything in videos" 수준의 category/part/occlusion diversity에는 부족하다.

## 3D Vision + Robotics 관점
SAM 2 자체는 2D/video segmentation 논문이지만, 로봇 perception에서는 object-level mask를 3D reconstruction, semantic mapping, Gaussian/NeRF feature field, scene graph memory로 올리는 출발점이 된다. 특히 moving camera video에서 temporal-consistent masks를 제공하므로 2D-to-3D semantic fusion과 object-centric SLAM의 foundation prior로 중요하다.
