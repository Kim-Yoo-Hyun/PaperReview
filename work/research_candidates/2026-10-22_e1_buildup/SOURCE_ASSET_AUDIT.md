# E1 공개 구현·데이터 자격 심사

- 날짜: 2026-10-22. Public text/JSON만 메모리에서 읽었다. 외부 코드 실행·설치·모델/영상/HDF5/NPY/PDF 저장은 없다.
- API/tree/파일 응답 identity·SHA-256·실패/재시도는 [ledger](./sources_2026-10-22.json)에 보존했다. 파일을 읽었다는 사실을 전체 repository 재현으로 해석하지 않는다.
- 판정: **문헌·source 심사 DONE / 실제 비교 자격 PARTIAL**.
- 후속 [E1-R1](./R1_REVIEW.md)에서 RH20T 공통 task·source view key와 X-VLA interface를 추가 확보했다. 아래의 미확보 항목은 최초 심사 이력이며 현재 자격·재개 조건은 후속 문서가 우선한다.

## 1. 실제 source에서 확인한 경로

| 자산·고정 revision | 읽은 위치와 확인 사실 | 비교 설계에 주는 의미 |
|---|---|---|
| ContinualVLA `d84ed7a811f95218e79ac5f0906465147ad7e1e3` | [replay_buffer.py](https://github.com/Agentic-Intelligence-Lab/ContinualVLA/blob/d84ed7a811f95218e79ac5f0906465147ad7e1e3/src/openpi/training/replay_buffer.py): transition/episode subset과 원 dataset의 index를 보관. [builder](https://github.com/Agentic-Intelligence-Lab/ContinualVLA/blob/d84ed7a811f95218e79ac5f0906465147ad7e1e3/scripts/build_replay_buffers.py): 기존 buffer에서 downsample | 작은 index JSON 크기를 실제 replay 저장 비용으로 세면 안 된다. RGB·state·action payload와 underlying archive 접근을 센다 |
| 같은 repo | [train_pytorch.py L693–710, 764–779](https://github.com/Agentic-Intelligence-Lab/ContinualVLA/blob/d84ed7a811f95218e79ac5f0906465147ad7e1e3/scripts/train_pytorch.py#L693): replay ratio에 따라 총 step을 `1/(1-ratio)`로 늘리고 step마다 new/replay 선택 | 같은 epoch 표기만으로 equal-compute가 아니다. 총 optimizer step와 실제 new/replay exposure를 별도 고정/보고. v3의 모든 비대칭 recipe와 checkpoint 재현까지 확인한 것은 아님 |
| 같은 repo | [data_loader.py L370–388](https://github.com/Agentic-Intelligence-Lab/ContinualVLA/blob/d84ed7a811f95218e79ac5f0906465147ad7e1e3/src/openpi/training/data_loader.py#L370): data transform 후 지정 norm stats, 이후 model transform | 정상 preprocessing을 모든 selector에 공통 적용. 실제 release별 stats·coverage는 미검증 |
| HiMoE `2a2c063dc5cf1159c54d7355af774876a58fa843` | [transforms.py L158–160, 451–515](https://github.com/ZhiyingDu/HiMoE-VLA/blob/2a2c063dc5cf1159c54d7355af774876a58fa843/src/moevla/transforms.py#L451): clipping/normalization, 유효 slot padding과 state mask. [moevla.py L387–390](https://github.com/ZhiyingDu/HiMoE-VLA/blob/2a2c063dc5cf1159c54d7355af774876a58fa843/src/moevla/models/moevla.py#L387): loss에 data mask 적용 | Missing DoF를 모두 실제 zero target으로 취급하는 비교는 이 공개 구현을 대표하지 않는다. 실제 mask correctness·runtime는 미검증 |
| LAP `3958d1466d5b92445b67de7d4202c19608ad4d56` | [frame_transforms.py](https://github.com/lihzha/lap/blob/3958d1466d5b92445b67de7d4202c19608ad4d56/src/lap/policies/transforms/frame_transforms.py): state rotation 기반 EEF frame 변환, dataset별 축·부호 처리 | OXE에 공통 vector가 있어도 dataset semantics가 동일한 것은 아니다. 이 경로만으로 task pairing·실제 command tracking은 확보되지 않는다 |
| Rethink `d3739abda923ffddaf01d6d8d74bf3d439068106` | [state_action.py](https://github.com/BeingBeyond/Rethink_VLA/blob/d3739abda923ffddaf01d6d8d74bf3d439068106/src/dataset/transform/state_action.py): rotation 변환과 metadata별 normalizer | 전처리 대안의 구현은 존재. 전체 두 로봇 데이터 변환·native 능력을 검증한 것은 아님 |
| MIR `35eda78bcdd35025b16b0b1039a926d34aad4851` | [mir.py L294–353](https://github.com/optimass/Maximally_Interfered_Retrieval/blob/35eda78bcdd35025b16b0b1039a926d34aad4851/mir.py#L294): virtual update, old sample의 `post_loss - pre_loss`, 큰 순서로 검색 | 원본은 classifier cross-entropy. VLA flow/loss·optimizer에 맞춘 adaptation과 비용 계약 필요. 코드 실행 없음 |

Memory Anchors/SPACE의 공식 release 상태와 VLA estimator 미확인 범위는 [직접 선행 문서](./CLOSEST_WORK.md)에 둔다. CLARE는 revision/tree 식별까지만 했으므로 구체적 runtime 대조 근거로 쓰지 않는다. 기존 OFT/Octo 사용 이력을 두 로봇의 신규 qualification으로 승계하지 않는다.

## 2. RoboMIND: schema가 있어도 effect label이 바로 유효하지 않다

공식 dataset은 [RSS 2025 등록](https://www.roboticsproceedings.org/rss21/p152.html)과 registry에 이미 존재한다. Source schema revision은 `28ede3eb1bc8a051be76e560a831fe3f0c32319f`다. [v1.2 schema](https://github.com/x-humanoid-robomind/x-humanoid-robomind.github.io/blob/28ede3eb1bc8a051be76e560a831fe3f0c32319f/static/all_robot_h5_info_v1.2.md)는 xyz m, rotation rad, joint rad를 기술한다. Franka/UR 예시는 master joint, puppet joint/EE, RGB를 제공하지만 명시적 real-robot timestamp·controller semantics는 해당 예시에서 확인하지 못했다. Master signal을 실제 전송 command로 자동 해석하지 않는다.

배포 측 [품질 보고](https://github.com/Open-X-Humanoid/RoboMIND-dataset-utils/blob/77d7b311cbf2f16624c941f46b2a75042858ff06/README.md)는 `h5_ur_1rgb`, `h5_simulation`, `h5_sim_franka_3rgb`의 거의 상수인 EE pose 이상과 joint/URDF를 통한 FK 대안을 명시한다. 이는 **저자 검사 보고**이며 우리가 payload 전체를 재검사한 결과가 아니다. FK로 pose를 복구해도 timestamp, frame, controller와 counterfactual contact 결과는 별도 문제다.

### 실제 공개 annotation 검사

같은 고정 revision의 `static/language_description_annotation_json/` 세 JSON을 파싱했다. 기준은 각 record의 `id`와 두 번째 path component인 task folder다. 경로·instruction metadata 검사이며 physical array 실험이 아니다.

| 공개 파일 | annotation record | task folder | 파일 내 중복 id |
|---|---:|---:|---:|
| [h5_franka_1rgb.json](https://github.com/x-humanoid-robomind/x-humanoid-robomind.github.io/blob/28ede3eb1bc8a051be76e560a831fe3f0c32319f/static/language_description_annotation_json/h5_franka_1rgb.json) | 161 | 2 | 0 |
| [h5_franka_3rgb.json](https://github.com/x-humanoid-robomind/x-humanoid-robomind.github.io/blob/28ede3eb1bc8a051be76e560a831fe3f0c32319f/static/language_description_annotation_json/h5_franka_3rgb.json) | 3,287 | 90 | 0 |
| [h5_ur_1rgb.json](https://github.com/x-humanoid-robomind/x-humanoid-robomind.github.io/blob/28ede3eb1bc8a051be76e560a831fe3f0c32319f/static/language_description_annotation_json/h5_ur_1rgb.json) | 2,625 | 75 | 0 |

합계 **6,073 records**다. 전체 dataset의 trajectory 수나 모든 task coverage로 일반화하지 않는다. Franka-1RGB/UR의 exact folder 교집합은 `bread_on_table` 하나, Franka-3RGB/UR은 0이다. 문자열 교집합은 task 의미의 동일성 검사나 공통 task 부재의 증명이 아니다.

- `bread_on_table`의 첫 Franka record `1016_143350`은 basket에서 bread를 집는 설명이고, UR `1014_145647`은 bread를 pepper 옆에 놓는 설명이다. 같은 folder name만으로 같은 goal pair로 채택하지 않는다.
- 유사 goal 후보: Franka `h5_franka_1rgb/bread_in_basket/.../1016_161244/data`와 UR `h5_ur_1rgb/bread_in_basket_1/.../1014_141531/data`. 각각 task folder에 86/18 annotation이 있고 첫 설명은 bread→basket이다. 이는 **semantic discovery**이며 matched object/scene·same feasible effect·sample quality·독립 split을 확인한 것은 아니다.
- `bread_in_basket_old`의 첫 UR 설명은 bread를 가져가는 행동이다. Suffix를 지운 일괄 매칭은 금지한다.
- 3RGB JSON은 최초 4 MB text bound에서 중단되었고, 16 MB로 범위를 조정한 재조회에서 성공했다. 빈 dataset으로 보고하지 않는다.

[HF card](https://huggingface.co/datasets/x-humanoid-robomind/RoboMIND)와 API의 revision `e7ffe31d1fe983a42c3d7b79d192f554fc05b86e`에서 `gated=auto`를 확인했다. 공개 GitHub metadata와 gated physical payload를 구분한다. 조건 수락·로그인·payload 접근은 하지 않았다. 접근 제한 자체를 연구 가치의 기각 이유로 쓰지 않는다.

## 3. RH20T: 시간·pose 경로의 대안

[공식 API](https://github.com/rh20t/rh20t_api/tree/aa3124434729ed622109a29b2cbb9f3bbb1c5eeb)의 [configs.json](https://github.com/rh20t/rh20t_api/blob/aa3124434729ed622109a29b2cbb9f3bbb1c5eeb/configs/configs.json)에는 7 configurations가 있다. UR5는 cfg3/4, Franka는 cfg5, Flexiv는 cfg1/2, Kuka는 cfg6/7이다. 같은 robot model의 sensor/gripper configuration 차이를 새 embodiment 수로 세지 않는다.

[README](https://github.com/rh20t/rh20t_api/blob/aa3124434729ed622109a29b2cbb9f3bbb1c5eeb/README.md)와 [scene.py](https://github.com/rh20t/rh20t_api/blob/aa3124434729ed622109a29b2cbb9f3bbb1c5eeb/rh20t_api/scene.py#L470)에서 millisecond timestamp, camera/base-aligned TCP, joint, force, gripper command/info 경로를 확인했다. Image는 가까운 timestamp를 고르고 수치 신호는 인접 시점으로 보간한다. **정렬 API 존재가 실제 동기화 정확도의 검증은 아니다.** Gripper command와 달리 arm command/desired target은 이 조사에서 독립 field로 식별하지 못했다. 관측 TCP를 명령이라고 다시 이름 붙이지 않는다.

[공개 task JSON](https://rh20t.github.io/static/task_description.json)은 149 keys다. Project의 발표 task 수와 다를 수 있으므로 최신 JSON key 수를 논문 실험 수로 고치지 않는다. `task_0008` block placement, `task_0006` block pushing은 후보 설명이나 cfg3/5에 모두 존재하는 episode manifest·동일 goal의 검증은 미확보다.

## 4. Qualification 결론

| 조건 | 현재 |
|---|---|
| 서로 다른 두 로봇 identity와 public text interface | PASS: Franka/UR 후보와 고정 source 식별 |
| 공통 goal의 실제 episode pair | PARTIAL: annotation-level 후보만 존재 |
| 정상 pose·frame·time·command semantics | PARTIAL: schema/known anomaly/조회 경로 확보, payload 검증 없음 |
| 예측한 새 command의 counterfactual 효과 | NOT_MET: 유효 forward map/오차 범위 미확보 |
| 두 로봇을 지원하는 동일 pretrained VLA와 clean competence | NOT_MET: 실행 model·checkpoint pair 미선정 |
| 기존 aligned AnchorER/MIR 이후 차별적 native 예측 | NOT_MET: 해석적 필요 조건만 확보 |

이 상태에서 dataset 전체 다운로드·FK 패키지 설치·새 policy 학습을 시작하지 않는다. 다음 심사는 [구체적 evidence packet](./EVIDENCE_REQUIREMENTS.json)에 의존하며, 단순 metadata 재집계로 완료시킬 수 없다.
