# Method

## Brief Method
SAM 2는 SAM을 video domain으로 확장한 unified promptable segmentation model이다. image는 single-frame video로 처리하고, video에서는 각 frame의 image encoding을 streaming 방식으로 처리하면서 memory attention을 통해 과거 prompt/prediction 정보를 참조한다.

## 핵심 방법론
- Promptable Visual Segmentation(PVS): points, boxes, masks를 frame 단위 prompt로 받아 target object/part의 masklet을 예측한다.
- Image encoder: MAE-pretrained Hiera backbone을 사용해 frame feature를 추출한다.
- Prompt encoder and mask decoder: SAM과 유사하게 prompt를 mask prediction으로 변환한다.
- Memory encoder: 현재 mask prediction과 frame feature를 compact memory로 변환한다.
- Memory bank: prompted/unprompted frame의 spatial memory와 object pointer를 저장한다.
- Memory attention: 현재 frame feature가 memory bank를 cross-attend하여 object identity와 temporal context를 유지한다.
- Data engine: SAM 2를 annotation loop에 넣어 human annotator가 어려운 video/object/part를 iterative하게 label하고, 자동 masklet generation으로 dataset 규모를 확장한다.

## 원리적 동기
비디오 segmentation의 핵심 실패는 frame별 mask 품질보다 object identity 유지와 correction propagation이다. 따라서 모델은 단일 frame prompt response뿐 아니라, 과거 object state를 저장하고 현재 frame feature와 비교할 수 있어야 한다. streaming memory는 long video를 frame-by-frame 처리하면서도 interactive correction을 반영할 수 있는 구조다.

## 3D/Robotics 확장 포인트
- multi-view RGB stream의 object mask를 3D Gaussian/NeRF/TSDF/point cloud에 fuse할 수 있다.
- memory bank 개념은 robot persistent object memory와 연결된다.
- failure case인 occlusion/reappearance는 embodied perception과 object permanence 연구의 직접적인 문제다.
- 3D consistency를 넣으면 SAM2 masklet을 camera pose/depth/scene graph와 함께 정제하는 연구로 확장 가능하다.
