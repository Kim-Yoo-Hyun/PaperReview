# 행동 tokenizer의 실행 예정 구간 복원 진단

2026-11-03 폴더 정리: 과거 실행 JSON의 명령·hash는 당시 기록을 유지한다. 현재 실행은 이 문서의 명령을 사용하고, 이전 경로는 [이동·병합 대응표](../../ORGANIZATION.json)에서 찾는다.

- 2026-11-03: 내부 buildup·Docker CPU 진단 완료. **좁은 평가 후보 보존; 신규 방법·정책 성능의 근거는 부족.** [전체 판단과 문헌](../내용/README.md).
- 공식 FAST+로 저장된 행동 배열의 encode/decode만 실행한다. VLA 추론·시뮬레이터·학습·실제 로봇 실행은 없다. 기존 정책 P0 3개와 별도다.

## 포함된 자료

| 파일 | 역할 |
|---|---|
| [CONTRACT.json](CONTRACT.json) | 실행 전 고정한 source revision·episode·normalizer·horizon·metric·budget |
| [CONTRACT_SUFFIX.json](CONTRACT_SUFFIX.json) | 최초 결과를 본 후 설계하고 별도로 실행한 고정 길이 합성 suffix 대조 |
| [probe.py](probe.py) / [suffix_probe.py](suffix_probe.py) | Docker 전용 공식 codec 진단. Source는 container tmpfs에만 다운로드 |
| [Dockerfile](Dockerfile) / [requirements.lock](requirements.lock) / [run.sh](run.sh) | Base digest·실제 dependency 버전·자원 제한·재현 entrypoint |
| [primary 결과](results/verified/results.json) / [보충 결과](results/suffix_verified/results.json) | 실제 개별 window·episode 값, hashes·normalizer·진단 결과 |
| [runtime.json](results/runtime.json) | 현재 자원·GPU 실패·실제 실행 image와 최종 recipe image·정리/검증 기록 |

## 다른 컴퓨터에서 재현

Repository root에서 실행한다. 이 packet이 포함된 revision을 전달해야 하며 현재 원격 게시 여부는 미확인이다. 아래는 기존 결과를 덮어쓰지 않는 새 출력 경로다.

```sh
sh "work/research_topics/action_tokenization/재현 방법/run.sh" check
sh "work/research_topics/action_tokenization/재현 방법/run.sh" build
sh "work/research_topics/action_tokenization/재현 방법/run.sh" run "work/research_topics/action_tokenization/재현 방법/results/replay_primary"
sh "work/research_topics/action_tokenization/재현 방법/run.sh" suffix "work/research_topics/action_tokenization/재현 방법/results/replay_suffix"
sh "work/research_topics/action_tokenization/재현 방법/run.sh" cleanup
```

- 로컬 Unix socket Docker·Linux container가 필요하다. 현재 Linux ARM64/Python 3.11.14에서 검증했다. x86-64는 같은 recipe를 제공하지만 이 작업에서 실행 검증하지 않았다. CPU 2개·container RAM 3 GiB를 할당할 여유와 image build 공간이 필요하다. GPU·CUDA·EGL·PyTorch가 필요하지 않다.
- Build 시 package index, 실행 시 Hugging Face HTTPS 접속이 필요하다. Source/데이터 revision은 계약에 고정했다. 전체 dataset·동영상 대신 명시한 metadata/parquet와 작은 tokenizer만 받는다. Run당 payload 한도 100 MiB·600초다.
- Container root와 `/app`는 read-only, `/tmp`는 512 MiB tmpfs, 선택한 결과 폴더만 `/output`으로 writable mount한다. Dataset·패키지를 host에 설치하지 않는다. Container 종료 시 임시 데이터는 사라진다.
- 기본 `run`/`suffix` 출력에는 이미 증거가 있으므로 덮어쓰기를 거부한다. `suffix`는 항상 봉인된 `results/verified/results.json`의 normalizer·window/hash를 참조한다. 새 primary 결과와 자동 연결하는 기능은 없다. 다른 계약으로 새 실험할 때 기존 결과·script를 수정하지 말고 별도 revision으로 분리한다.
- 공식 processor의 coefficient floor clipping·decode parity·frame 연속성·normalizer 퇴화 검사가 실패하면 `FAILED`다. 실패를 정책/연구 성능 결과로 바꾸지 않는다. 성공 status는 codec 진단의 성공이며 로봇 과제 성공이 아니다.
- 최종 lock image는 초기 실행 image와 package freeze가 동일함을 확인했다. 원 실험은 초기 image에서 실행했으며 양쪽 image ID를 runtime에 구분했다. Package 이름/버전 lock이며 모든 wheel의 공급망 hash까지 고정한 lock은 아니다. 새로운 플랫폼에서 byte-identical 결과를 보장하지 않는다.
- `cleanup`은 이 작업 label을 확인한 전용 tag만 제거한다. 다른 image·container나 전역 build cache를 정리하지 않는다. 현재 작업의 전용 image는 정리했으므로 재현 시 `build`부터 필요하다.

## 남은 연구 조건

전체/앞부분 오차가 다른 선택을 유도한 episode는 있었으나 데이터셋 평균의 순위 역전은 없었다. Learned codec·bitrate 정합·정책 성공·독립 외부 피드백은 미검증이다. GPU를 확보했다고 학습을 자동 시작하지 않는다. [후속 판단 조건](../내용/README.md#6-연구-가치와-다음-행동)을 먼저 따른다. Native VLA용 driver·checkpoint·VRAM 요구량은 이 packet에 포함하지 않으며 아직 구체화하지 않았다.
