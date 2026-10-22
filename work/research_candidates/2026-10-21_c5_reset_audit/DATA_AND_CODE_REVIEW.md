# C5 공개 데이터·구현 감사

- Date: 2026-10-21 KST
- 실제 실행: Docker Python 표준 라이브러리로 source/metadata 읽기 및 pickle opcode 파싱.
- Source를 정적으로 확인한 것과 policy 실행을 구분한다. Upstream 학습·로봇 연결·원격 평가 job 제출은 하지 않았다.

## 고정한 공개 구현

| Repository | Commit | 검토한 interface |
|---|---|---|
| [AutoEval](https://github.com/zhouzypaul/auto_eval) | `3ea3ff44c6950433cfbcb4294a3deaa616533745` | Main eval/reset loop, config, logging 연결 |
| [robot_eval_logger](https://github.com/zhouzypaul/robot_eval_logger/tree/auto_eval) | `a8134f5551634a9991b3be96afb79c0a1bc68d2c` | AutoEval README가 지정한 `auto_eval` branch, episode 저장과 success 집계 |
| [MEDAL](https://github.com/architsharma97/medal) | `4cb0ca84b034cc5593489734cf86e02242ff0493` | 독립 eval_env에서 deployed policy 평가 |
| [MoReFree](https://github.com/yangzhao-666/MoReFree) | `c390568131c5ee3d4b2e23800d378b4a32909b0d` | 초기/평가 목표 sampling, reset-free wrapper |

전체 tree 목록과 조회한 22개 source의 URL·SHA256는 [CODE_AUDIT.json](./CODE_AUDIT.json)에 있다. Tree inventory는 payload 검사나 동작 검증이 아니다. Source 원문은 container 내부에만 두고 종료 때 정리했다.

## AutoEval에서 실제 확인한 것

[Pinned run_eval.py](https://github.com/zhouzypaul/auto_eval/blob/3ea3ff44c6950433cfbcb4294a3deaa616533745/run_eval.py)의 다음 범위를 읽었다.

- L58–66, L488–570, L668–684: bounded reset 재시도, 이미 reset된 상태면 skip, 연속 실패 후 human confirmation. 따라서 실패 reset을 무조건 조용히 버린다는 설명은 코드와 맞지 않는다.
- L588–609: motor error 뒤 평가를 다시 실행하면 `eval_infos`가 교체된다. 재시도 횟수와 개입 flag는 남지만, 이 driver의 저장 호출만으로 모든 개별 시도의 trajectory를 복원할 수는 없다.
- L636–658: 평가 trajectory·action·proprio, 평가 시간, human intervention 및 **evaluation retry** 수를 logger에 전달한다. `num_eval_retries`는 **reset attempt 수가 아니다**.
- L488–545, L668–684: reset frames는 생성하지만 이 경로에는 각 reset attempt를 `save_episode`로 저장하는 호출이 없다. Console·Slack·WandB 등 다른 기록의 존재 가능성을 배제하지 않는다.
- L418–448: 첫 저장 frame은 action 이후다. Pickle의 첫 frame을 정확한 action 전 시작 관측으로 단정할 수 없다.
- L258–265: robot metadata의 이름이 고정 문자열이다. `robot_name`만으로 다양한 scene·embodiment를 구분하면 안 된다.

[Pinned logger L160–210, L239–267](https://github.com/zhouzypaul/robot_eval_logger/blob/a8134f5551634a9991b3be96afb79c0a1bc68d2c/robot_eval_logger/eval_logger.py)는 전달된 episode outcome의 평균을 계산하고 추가 kwargs를 저장한다. 이것이 target distribution의 성공률인지 여부는 호출자가 만든 시작 분포와 sampling 과정에 달려 있다. 집계 코드만으로 논문 결과의 과대평가를 입증하지 못한다.

## 실제 공개 payload 검사

Release: [zhouzypaul/auto_eval](https://huggingface.co/datasets/zhouzypaul/auto_eval/tree/97fd71792d05e8a96a09c962843f5bdba3006ff5), revision `97fd71792d05e8a96a09c962843f5bdba3006ff5`.

| 범위 | 관측 결과 | 해석 한계 |
|---|---|---|
| API 전체 파일 목록 | 13,152개 = metadata 1,096 + trajectory pickle 12,054 + 기타 2 | 파일 수이며 실제 전체 attempted trial 수는 아님 |
| Metadata 24개 | 전부 `eval_id`, `location`, `robot_name`, `robot_type`, `time`, `evaluator_name` 여섯 key | Path 사전순에서 등간격으로 선택한 schema sample. 전체 1,096개 payload 전수 검사가 아님 |
| Trajectory 2개 | 각각 7,479,387 / 6,889,722 bytes, opcode가 STOP까지 파싱됨. `action`, `success`, `need_human_intervention`, `num_eval_retries` 등 문자열 확인 | `pickle.load`를 쓰지 않았으므로 값·성공률·정확한 top-level schema를 복원했다고 하지 않음 |
| 비용 | Metadata 포함 총 14,373,568 bytes | 영상 배열이 포함된 pickle은 읽었지만 이미지 decode/수동 annotation은 없음 |

처음·중간·마지막 metadata 폴더의 `traj_0.pkl`을 요청 후보로 정했다. 마지막 폴더의 해당 path는 inventory에 없어 실제 검사 수는 2개다. 이 사실을 reset 실패 증거로 해석하지 않는다. Metadata만 있는 run 수와 path별 payload hash·오류 목록은 [DATA_AUDIT.json](./DATA_AUDIT.json)에 남겼다.

### C5 전제와의 대조

| 필요한 정보 | 확보 수준 |
|---|---|
| Task/action/outcome | Driver와 logger 저장 경로 존재; 두 payload에서 관련 문자열 확인. 독립 human outcome 확인은 아님 |
| Evaluation 시각·run ID | 24개 metadata에서 확인. RL update round를 뜻하지 않음 |
| 같은 VLA의 checkpoint hash·optimizer update·reset policy version | 검사한 sample/source에서 완전한 join을 확보하지 못함 |
| Requested start와 실제 achieved start | 명시적 reset 목표 scene ID/요청 sampling 확률을 확보하지 못함. 관측 영상으로 사후 추정해도 요청되지 않은 상태는 복원 불가 |
| 모든 reset attempts·실패·취소·rescue duration | Human intervention flag가 대체하지 못함. 검토한 저장 경로가 per-attempt ledger를 제공하지 않음 |
| 고정 p_target의 독립 평가 | Public export를 해당 실험 설계와 연결할 identity/split을 확보하지 못함 |

**데이터 존재 gate는 통과했지만 C5의 인과·학습 효과 식별 gate는 통과하지 못했다.** 모든 공개 데이터가 부적합하다는 결론이 아니라, 이번 release/sample과 code audit로 현재 필요한 연결을 입증하지 못한 것이다. 현재 HEAD 코드가 과거 모든 dataset run을 생성했다고 가정하지 않는다.

## 다른 구현의 사용 범위

[MEDAL `medal.py` L218–254](https://github.com/architsharma97/medal/blob/4cb0ca84b034cc5593489734cf86e02242ff0493/medal.py)에는 분리된 eval_env reset과 deployed evaluation 저장이 있다. [MoReFree goal sampler L23–43](https://github.com/yangzhao-666/MoReFree/blob/c390568131c5ee3d4b2e23800d378b4a32909b0d/resetfree/goal_picker_wrapper.py)는 초기 상태 목표·평가 목표·exploration을 섞는다. 기존 baseline의 interface 근거이며 VLA 모델 실행 근거가 아니다.

현재 컴퓨터에서 이들 코드의 native VLA+physical-reset RL stack을 실행해 본 것은 아니다. AutoEval의 robot/server interface와 로컬 CPU source 감사가 가능하다는 사실을 구분한다. 학습 데이터·reset controller·체크포인트가 정해지지 않아 큰 dependency 설치나 임의 환경 이식을 하지 않았다.
