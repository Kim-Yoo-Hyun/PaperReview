# Method

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_SceneVerse-Scaling-3D-Vision-Language-Learning-for-Grounde/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Results and Analyses We present the results of zero-shot transfer experiments in Tab.
- We introduce the first million-scale 3D-VL dataset, SceneVerse, encompassing 68K indoor scenes and comprising 2.5M vision-language pairs collected from both human annotations and our scalable scene-graph-based generation approach.
- Specifically, for the zero-shot text setting, we use the generated texts in SceneVerse as fine-tuning sources for the zero-shot model.

## 원리적 동기
- In this work, we aim to address these major challenges in 3D-VL by examining the potential of systematically upscaling 3D-VL learning in indoor scenes.
- In comparison to recent advancements in the 2D domain, grounding language in 3D scenes faces two significant challenges: (i) the scarcity of paired 3D-VL data to support grounded ...
- Results and Analyses We present the results of zero-shot transfer experiments in Tab.

## 핵심 방법론
- Results and Analyses We present the results of zero-shot transfer experiments in Tab.
- Specifically, for the zero-shot text setting, we use the generated texts in SceneVerse as fine-tuning sources for the zero-shot model.
- We mainly compare our model against a recent pre-training-based model 3D-VisTA.
- Moreover, the dataset-specific fine-tuned model, i.e., Ours (fine-tuned ), consistently outperforms existing baselines with only a simple projection MLP added on top of the pretrained model, jointly optimized ...
- This indicates the effectiveness of contrastive alignment over traditional classification objectives, aligning with the advancements seen in 2D-VL models for open-vocabulary grounding and transfer capabilities ‚ SceneVerse dataset ...
