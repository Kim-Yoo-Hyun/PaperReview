# REG-R16 — Ψ₀ 등록과 정확성 보완

- Reviewed: 2026-11-16 KST
- 범위: 요청 논문·직접 데이터 전제 등록, AMO/SONIC 내용·metadata 교정, 전체 registry 구조 검사
- [출처·검증 원장](../sources/registry_accuracy_2026-11-16.json) · [등록 입력](../sources/registry_admissions_2026-11-16.json)

## 등록과 분류

| 논문 | 검증한 status | 등록 이유·근거 범위 |
|---|---|---|
| [Ψ₀(Psi-Zero)](../../2026/RSS/2026_RSS_An-Open-Foundation-Model-Towards-Universal-Humanoid-Loco-M/01_overview.md) | RSS2026 | 사용자 필수 요청. VLA 학습 단계·휴머노이드 데이터·하위 RL 제어의 직접 비교. 지정 본문 절 확인 |
| [EgoDex](../../2026/ICLR/2026_ICLR_EgoDex-Learning-Dexterous-Manipulation-from-Large-Scale-Eg/01_overview.md) | ICLR2026 | Ψ₀의 인간 데이터 전제. 공식 초록·data schema 검토 |
| [Humanoid Everyday](../../2025/arXiv/2025_arXiv_Humanoid-Everyday-A-Comprehensive-Robotic-Dataset-for-Open/01_overview.md) | arXiv2025 | Ψ₀의 로봇 데이터 전제. 공식 초록·project/code 검토 |

공식 표기는 **Ψ₀**이며 φ₀·π₀가 아니다. [RSS proceedings](https://www.roboticsproceedings.org/rss22/p021.html)의 DOI/title/year를 확인했다. EgoDex는 [ICLR 공식 목록](https://iclr.cc/Downloads/2026)·[OpenReview](https://openreview.net/forum?id=FFxkFMU89E)에서 확인했다. HE의 저자 ICRA2026 표기는 공식 proceedings/program으로 확정하지 못했으므로 preprint로 남겼다. 신규3편 모두 NEXT이며 사용자 상태는 UNREAD다. 기존 CORE/NEXT membership은 유지한다.

## 교정한 내용

- **Snapshot 집계:** 직전 README의 최근2024–2026 논문 수898편은 실제 manifest910편과 불일치했다. 현재는 신규3편을 포함한913편으로 교정했다. 과거 날짜별 보고서의 당시 수량은 소급 덮어쓰지 않고 이 정정 근거를 남긴다.

- **AMO:** 기존5노트에 남은 깨진 OCR 관절 표기와 generic template·부정확한 queue 계보를 지정 [원문 §III–V/Table II–IV](https://arxiv.org/html/2505.03738v1)로 교정했다. 시연 수와 평가 trial·단계별 성공을 분리했다. DOI/arXiv 및 [공개 추론 코드](https://github.com/OpenTeleVision/AMO)를 추가했다. 전체 학습 pipeline 공개나 실행 성공을 주장하지 않는다.
- **SONIC:** [arXiv v4](https://arxiv.org/abs/2511.07820)·[공식 project](https://nvlabs.github.io/GEAR-SONIC/)로 Science Robotics11(117), eaed4592의 DOI와 version을 보완하고 [공개 code](https://github.com/NVlabs/GR00T-WholeBodyControl)를 연결했다. Legacy abstract evidence 필드를 기존 FULL_TEXT_CHECKED provenance에 맞췄다. Publisher 직접 접근403과 과거 PDF 검토를 구분한다. 기존 본문은 이미21kGPUh를 기록했으므로 이 수치를 새 오류였다고 보고하지 않는다.
- **Ψ₀ 해석:** 본문 pretraining에 human/robot 자료가 함께 들어가는 점, frozen VLM 후학습과 하위 RL controller의 차이, control thread와 inference 주파수, subtask 보조 개입을 명시했다. v1 AMO 결과와 후속 SONIC release를 분리했다.
- **데이터 크기:** Ψ₀의 EgoDex900M 표기는 원 데이터 약90M과 불일치한다. [EgoDex 원출처](https://github.com/apple-aiml-research/ml-egodex)를 기준으로 쓰고, HE의 전체 corpus와 Ψ₀ 사용31h도 구별한다.

[RL/data](../../synthesis/02_rl_il_offline.md#humanoid-data-2026), [VLA](../../synthesis/04_vla_generalist.md#psi0-2026), [whole-body](../../synthesis/06_locomotion_whole_body.md#psi0-controller-boundary)에 비교 경계를 연결했다. 후보 순위·NO-GO/HOLD·다음 LANGRET-P0 계약은 유지한다.

## 검토 범위와 남은 불확실성

전체 registry에 구조·식별자·중복·노트·링크 검사를 적용하고, 사실 교정은 위 논문과 인접 공개 자료에 한정했다. **전체1,206편의 모든 문장·수치를 인터넷 원문과 전수 대조한 것은 아니다.** 자동 artifact scanner가 통과해도 AMO 같은 의미상 OCR 오독을 모두 검출한다는 뜻은 아니다. Ψ₀의 RSS 최종본문 전체와 arXiv v1의 차이, EgoDex/HE 전체 평가, 공개 release의 실제 runtime은 별도 확인 대상이다.

## Snapshot와 검증

전체1,206편/표준 노트6,030개, CORE50/NEXT405/REFERENCE509/ARCHIVE242, active455/history47. Source evidence FULL_TEXT_CHECKED968/ABSTRACT_CHECKED238. 사용자 READ5편과 모든 기존 읽기 입력을 보존한다.

<!-- VALIDATION:START -->
등록 dry-run/apply, tier 생성기 compile/rebuild, priority-only reconcile, catalog/resource/index/stats 재생성을 완료했다. 최종 reconcile 추가 변경0건. 읽기 이력6개·문서 유지보수8개 검사 통과. `git diff --check`(working/staged) 통과. 전체 audit는 **오류0/경고0**이며 Markdown6,257개·내부 링크13,499개·registry1,206행·표준 노트6,030개를 확인했다. Artifact scanner6,030노트의 검출0건은 의미상 정확성 전수 검증을 뜻하지 않는다. 검사 중 checkpoint status enum3건을 올바른 `reported`로 고친 뒤 재검사를 통과했다.

기존1,203편 중 AMO/SONIC2편만 canonical record를 수정했다. 기존 tier1,203건·사용자 입력499건·실험/재현 자료236파일을 보존했다. 신규 읽기3건은 UNREAD. 기존 표준 노트6,015개 중8개만 교정/보완하고6,007개를 그대로 유지했다. 이번 작업의 기존 파일 삭제0개·신규 파일19개(노트15·등록 입력·원장·이 보고서·.gitattributes). Git staging 전 기존 staged patch도 byte-identical임을 확인했다. Resource658개·curated relation50개이며 자동 resource 연결은 cue_only다.
GitHub 게시를 위해 기존 미추적 파일까지 staging한 뒤 발견한 비실행 문서8개의 마지막 빈 줄을 정리했다. 보존된 patch의 diff context와 재현 자료3개의 마지막 빈 줄은 원 bytes를 유지하고 `.gitattributes`에 해당4경로만 좁은 whitespace 예외를 두었다. 전체 staged diff 검사를 통과했으며 실행 자료236개는 그대로다.
<!-- VALIDATION:END -->

## GitHub 반영

사용자 요청에 따라 누적 registry·문헌·실행 준비 자료를 포함한 [내용 commit `f04a8579`](https://github.com/Kim-Yoo-Hyun/PaperReview/commit/f04a8579c7a2569e9fa57112265d8f453f805abc)을 **origin/main에 게시했다**. `git ls-remote`와 별도 새 GitHub clone의 HEAD 일치를 확인했다. 원격 clone에서도 전체 audit 오류0/경고0이며 재현 자료236개가 작업 전 원본과 byte-identical이다. 이는 현재 Mac의 문서/파일 감사이며 다른 NVIDIA 컴퓨터의 Docker/image/native 실험 검증이 아니다.

게시 확인 인계를 별도 후속 커밋으로 남긴다. 기존 날짜별 실행/업로드 미확인 기록은 당시 사실로 보존하고, 현재 TODO와 주제 index에서 게시 상태를 갱신했다. 이번 작업은 실험·Docker 실행·host dependency 설치·PDF/weights 다운로드를 수행하지 않았다.
