<div align="center">
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:020c1b,50:0a192f,100:020c1b&height=200&section=header&text=&fontSize=1"/>
</div>

<div align="center">

```
// hello, world. i'm
```

# Aimen Abdesselam.

**AI Research Engineer · Medical Imaging · Computer Vision · GNNs**

`⚡ PFE opportunities`&nbsp;&nbsp;&nbsp;&nbsp;`🇫🇷 France · EU · Remote`

<br/>

![IASD](https://img.shields.io/badge/IASD-M.Sc._AI_%26_CV-64ffda?style=flat-square&labelColor=0a192f)&nbsp;
![PyTorch](https://img.shields.io/badge/PyTorch-Production_AI-EE4C2C?style=flat-square&labelColor=0a192f&logo=pytorch&logoColor=white)&nbsp;
![Medical](https://img.shields.io/badge/Medical_Imaging-BraTS20-ccd6f6?style=flat-square&labelColor=0a192f)&nbsp;
![GNN](https://img.shields.io/badge/GNN-Graph_ML-8892b0?style=flat-square&labelColor=0a192f)&nbsp;
![Status](https://img.shields.io/badge/SEEKING_PFE-FEB_2027-64ffda?style=flat-square&labelColor=0a192f)

<br/>

> I research multi-task medical imaging systems, graph neural networks for autonomous swarms,<br/>and ship production AI — from 3D MRI tensors to live clinical web apps.

`M.Sc. completion: June 2027` · `6-month internship availability: Feb / Mar 2027`

</div>

---

<br/>

## ✦ PROJECTS

<br/>

<!-- ════════════════════════════════════════════════════════ -->

<table><tr><td>

<br/>

`MEDICAL AI · SOLO LEAD · RESEARCH`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`LIVE`

### [🧠 Multi-Task Brain Tumor Diagnosis — BraTS20](https://github.com/AimenAbdesslame/multimodal-brain-tumor-diagnostics)

A dual-head U-Net for joint **3D MRI tumor segmentation + grade classification** on BraTS 2020 (T1 · T1ce · T2 · FLAIR). Implements **Kendall uncertainty weighting** for adaptive multi-task loss balancing and **PCGrad gradient surgery** to resolve cross-task gradient conflicts. Deployed as a full-stack clinical web app with FastAPI backend, React frontend, Docker containers, and W&B experiment tracking.

| Dice | ROC-AUC | Latency | Param ↓ |
|:----:|:-------:|:-------:|:-------:|
| **0.726** | **0.962** | **5.3 ms/slice** | **50% (7.77M)** |

<br/>

![PyTorch](https://img.shields.io/badge/PyTorch-0a192f?style=flat-square&logo=pytorch&logoColor=EE4C2C)&nbsp;![U-Net](https://img.shields.io/badge/Dual--Head_U--Net-0a192f?style=flat-square)&nbsp;![PCGrad](https://img.shields.io/badge/PCGrad-0a192f?style=flat-square)&nbsp;![Kendall](https://img.shields.io/badge/Kendall_Uncertainty-0a192f?style=flat-square)&nbsp;![FastAPI](https://img.shields.io/badge/FastAPI-0a192f?style=flat-square&logo=fastapi&logoColor=009688)&nbsp;![React](https://img.shields.io/badge/React-0a192f?style=flat-square&logo=react&logoColor=61DAFB)&nbsp;![Docker](https://img.shields.io/badge/Docker-0a192f?style=flat-square&logo=docker&logoColor=2496ED)&nbsp;![W&B](https://img.shields.io/badge/W%26B-0a192f?style=flat-square&logo=weightsandbiases&logoColor=FFBE00)

<br/>

<details>
<summary><b>▸ How the research pipeline fits together (architecture)</b></summary>
<br/>

```
BraTS20 NIfTI volumes (T1·T1ce·T2·FLAIR)
    │
    ▼
3D Tensor Fusion Pipeline (NiBabel · NumPy)
    │
    ▼
Shared U-Net Encoder (7.77M params)
    ├── Decoder Head A → Segmentation (Dice Loss)
    └── Decoder Head B → Classification (BCE Loss)
    │
    ▼
Kendall Uncertainty Weighting (learned σ per task)
    +
PCGrad Gradient Surgery (conflict-free backprop)
    │
    ▼
FastAPI Inference Server (5.3 ms/slice) → Docker → Render
    │
    ▼
React + Tailwind Frontend → Vercel (LIVE)
```

</details>

<br/>

[![VIEW REPOSITORY](https://img.shields.io/badge/VIEW_REPOSITORY-64ffda?style=for-the-badge&logoColor=020c1b)](https://github.com/AimenAbdesslame/multimodal-brain-tumor-diagnostics)&nbsp;&nbsp;[![LIVE DEMO](https://img.shields.io/badge/▲_LIVE_DEMO-64ffda?style=for-the-badge&logoColor=020c1b)](https://multimodal-brain-tumor-diagnostics.vercel.app)&nbsp;&nbsp;[![READ PAPER](https://img.shields.io/badge/READ_PAPER-64ffda?style=for-the-badge&logoColor=020c1b)](https://drive.google.com/file/d/1BGBiM9NWthjeNTqe7vRC0PhU4XXtyTR6/view?usp=sharing)

<br/>

</td></tr></table>

<br/>

<!-- ════════════════════════════════════════════════════════ -->

<table><tr><td>

<br/>

`GRAPH AI · CO-AUTHOR · TEAM R&D`

### [🚁 GNN Drone Swarm Optimization](https://github.com/AimenAbdesslame/gnn_drone_project)

A graph neural network framework for **multi-agent drone swarm coordination**: each drone modeled as a graph node with spatial features (position · velocity · heading), inter-drone radio links as edges. GNN message-passing protocols learn decentralized collective trajectory policies via multi-agent RL — no central coordinator. C++ firmware bridge for real-time telemetry.

<br/>

![PyG](https://img.shields.io/badge/PyTorch_Geometric-0a192f?style=flat-square&logo=pytorch&logoColor=EE4C2C)&nbsp;![GNN](https://img.shields.io/badge/Graph_Neural_Nets-0a192f?style=flat-square)&nbsp;![RL](https://img.shields.io/badge/Multi--Agent_RL-0a192f?style=flat-square)&nbsp;![C++](https://img.shields.io/badge/C++-0a192f?style=flat-square&logo=cplusplus&logoColor=00599C)&nbsp;![Spatial](https://img.shields.io/badge/Spatial_Encoding-0a192f?style=flat-square)

<br/>

[![VIEW REPOSITORY](https://img.shields.io/badge/VIEW_REPOSITORY-64ffda?style=for-the-badge&logoColor=020c1b)](https://github.com/AimenAbdesslame/gnn_drone_project)

<br/>

</td></tr></table>

<br/>

<!-- ════════════════════════════════════════════════════════ -->

<table><tr><td width="50%">

<br/>

**🎗️ Breast Cancer Clustering**

Unsupervised ML on breast-cancer patient data — K-Means, hierarchical clustering, PCA dimensionality reduction for latent diagnostic pattern discovery.

![sklearn](https://img.shields.io/badge/scikit--learn-0a192f?style=flat-square&logo=scikitlearn&logoColor=F7931E)&nbsp;![Python](https://img.shields.io/badge/Python-0a192f?style=flat-square&logo=python&logoColor=3776AB)

[![REPO](https://img.shields.io/badge/REPO-233554?style=flat-square&logo=github&logoColor=ccd6f6)](https://github.com/AimenAbdesslame/breast-cancer-unsupervised-app)

<br/>

</td><td width="50%">

<br/>

**🎬 CINEMATCH — Hybrid RecSys**

Movie recommender combining content-based, collaborative filtering, and matrix factorization — Streamlit dashboard with Netflix-style UI.

![Python](https://img.shields.io/badge/Python-0a192f?style=flat-square&logo=python&logoColor=3776AB)&nbsp;![Streamlit](https://img.shields.io/badge/Streamlit-0a192f?style=flat-square&logo=streamlit&logoColor=FF4B4B)

[![REPO](https://img.shields.io/badge/REPO-233554?style=flat-square&logo=github&logoColor=ccd6f6)](https://github.com/AimenAbdesslame/CINEMATCH_movie-recommender-system)

<br/>

</td></tr></table>

<table><tr><td width="50%">

<br/>

**📉 Linear Regression — From Scratch**

Gradient descent, MSE, vectorized NumPy — zero sklearn. First-principles numerical ML. ⭐ 2

[![REPO](https://img.shields.io/badge/REPO-233554?style=flat-square&logo=github&logoColor=ccd6f6)](https://github.com/AimenAbdesslame/Linear_Regression_from_Scratch__No_ML_Libraries)

<br/>

</td><td width="50%">

<br/>

**📊 Logistic Regression — From Scratch**

Binary classifier, sigmoid, cross-entropy — pure NumPy. First-principles ML depth. ⭐ 2

[![REPO](https://img.shields.io/badge/REPO-233554?style=flat-square&logo=github&logoColor=ccd6f6)](https://github.com/AimenAbdesslame/Logistic_Regression_from_Scratch__No_ML_Libraries)

<br/>

</td></tr></table>

<br/>

**`▸ ALSO SHIPPED: WEB & TOOLS`**

<table><tr><td width="50%">

<br/>

**E-VENTI**

Event management platform — full frontend architecture.

![TypeScript](https://img.shields.io/badge/TypeScript-0a192f?style=flat-square&logo=typescript&logoColor=3178C6)&nbsp;![React](https://img.shields.io/badge/React-0a192f?style=flat-square&logo=react&logoColor=61DAFB)

[![REPO](https://img.shields.io/badge/REPO-233554?style=flat-square&logo=github&logoColor=ccd6f6)](https://github.com/AimenAbdesslame/E-VENTI_Front-End)

<br/>

</td><td width="50%">

<br/>

**Social Media React**

Social feed UI with real-time components.

![React](https://img.shields.io/badge/React-0a192f?style=flat-square&logo=react&logoColor=61DAFB)&nbsp;![MUI](https://img.shields.io/badge/MUI_5-0a192f?style=flat-square&logo=mui&logoColor=007FFF)

[![REPO](https://img.shields.io/badge/REPO-233554?style=flat-square&logo=github&logoColor=ccd6f6)](https://github.com/AimenAbdesslame/social_media_react)

<br/>

</td></tr>
<tr><td width="50%">

<br/>

**Fitness Supplements App**

Gym exercise & supplement tracker.

![JavaScript](https://img.shields.io/badge/JavaScript-0a192f?style=flat-square&logo=javascript&logoColor=F7DF1E)

[![REPO](https://img.shields.io/badge/REPO-233554?style=flat-square&logo=github&logoColor=ccd6f6)](https://github.com/AimenAbdesslame/Fitness_Supplements_app)

<br/>

</td><td width="50%">

<br/>

**NumPy 100 + TCP Networking**

100 numerical computing exercises · TCP socket system.

![NumPy](https://img.shields.io/badge/NumPy-0a192f?style=flat-square&logo=numpy&logoColor=013243)&nbsp;![TS](https://img.shields.io/badge/TypeScript-0a192f?style=flat-square&logo=typescript&logoColor=3178C6)

[![NumPy](https://img.shields.io/badge/REPO-233554?style=flat-square&logo=github&logoColor=ccd6f6)](https://github.com/AimenAbdesslame/numpy-100-exercises-solutions)&nbsp;[![TCP](https://img.shields.io/badge/REPO-233554?style=flat-square&logo=github&logoColor=ccd6f6)](https://github.com/AimenAbdesslame/Socket-TCP_networking)

<br/>

</td></tr></table>

---

<br/>

## ✦ JOURNEY

| when | where | what happened |
|------|-------|---------------|
| 2025 → 2027 | **IASD — M.Sc. AI & CV** | Deep learning · CV · probabilistic models · optimization |
| 2026 | Solo Research | BraTS20 multi-task brain tumor project → shipped live |
| 2026 | Team R&D | GNN drone swarm optimization — co-author |
| 2025 | Self-Study / Labs | 100 NumPy exercises · from-scratch ML · TCP · IASD labs S1 & S2 |
| 2023 | Full-Stack Dev | E-VENTI · Social Media · Fitness App — React / TS / JS |

*`Target: completion & distribution. Manifesto.`*

---

<br/>

## ✦ STACK

<br/>

**Languages**

![Python](https://img.shields.io/badge/Python-0a192f?style=flat-square&logo=python&logoColor=3776AB)&nbsp;![C++](https://img.shields.io/badge/C++-0a192f?style=flat-square&logo=cplusplus&logoColor=00599C)&nbsp;![TypeScript](https://img.shields.io/badge/TypeScript-0a192f?style=flat-square&logo=typescript&logoColor=3178C6)&nbsp;![JavaScript](https://img.shields.io/badge/JavaScript-0a192f?style=flat-square&logo=javascript&logoColor=F7DF1E)&nbsp;![SQL](https://img.shields.io/badge/SQL-0a192f?style=flat-square&logo=mysql&logoColor=4479A1)

**AI & data science**

![PyTorch](https://img.shields.io/badge/PyTorch-0a192f?style=flat-square&logo=pytorch&logoColor=EE4C2C)&nbsp;![PyG](https://img.shields.io/badge/PyG-0a192f?style=flat-square&logo=pytorch&logoColor=EE4C2C)&nbsp;![sklearn](https://img.shields.io/badge/sklearn-0a192f?style=flat-square&logo=scikitlearn&logoColor=F7931E)&nbsp;![NumPy](https://img.shields.io/badge/NumPy-0a192f?style=flat-square&logo=numpy&logoColor=013243)&nbsp;![Pandas](https://img.shields.io/badge/Pandas-0a192f?style=flat-square&logo=pandas&logoColor=150458)&nbsp;![OpenCV](https://img.shields.io/badge/OpenCV-0a192f?style=flat-square&logo=opencv&logoColor=5C3EE8)

**Web & backend**

![FastAPI](https://img.shields.io/badge/FastAPI-0a192f?style=flat-square&logo=fastapi&logoColor=009688)&nbsp;![React](https://img.shields.io/badge/React-0a192f?style=flat-square&logo=react&logoColor=61DAFB)&nbsp;![Tailwind](https://img.shields.io/badge/Tailwind-0a192f?style=flat-square&logo=tailwindcss&logoColor=06B6D4)&nbsp;![Streamlit](https://img.shields.io/badge/Streamlit-0a192f?style=flat-square&logo=streamlit&logoColor=FF4B4B)

**Tools & infra**

![Docker](https://img.shields.io/badge/Docker-0a192f?style=flat-square&logo=docker&logoColor=2496ED)&nbsp;![W&B](https://img.shields.io/badge/W%26B-0a192f?style=flat-square&logo=weightsandbiases&logoColor=FFBE00)&nbsp;![Vercel](https://img.shields.io/badge/Vercel-0a192f?style=flat-square&logo=vercel&logoColor=white)&nbsp;![Render](https://img.shields.io/badge/Render-0a192f?style=flat-square&logo=render&logoColor=46E3B7)&nbsp;![Git](https://img.shields.io/badge/Git-0a192f?style=flat-square&logo=git&logoColor=F05032)

---

<br/>

## ✦ ANALYTICS

<div align="center">

<img height="170" src="https://github-readme-stats.vercel.app/api?username=AimenAbdesslame&show_icons=true&hide_border=true&bg_color=020c1b&title_color=64ffda&icon_color=64ffda&text_color=8892b0&include_all_commits=true&count_private=true"/>
<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=AimenAbdesslame&layout=compact&langs_count=7&hide_border=true&bg_color=020c1b&title_color=64ffda&text_color=8892b0"/>

<br/>

<img width="55%" src="https://github-readme-streak-stats.herokuapp.com/?user=AimenAbdesslame&hide_border=true&background=020c1b&ring=64ffda&fire=ff7b72&currStreakLabel=64ffda&stroke=233554&sideLabels=8892b0&dates=8892b0"/>

</div>

---

<br/>

## ✦ CONNECT

<div align="center">

### `>> Available · Feb / Mar 2027 · 6-Month PFE · Europe or Remote`

<br/>

[![LINKEDIN](https://img.shields.io/badge/LINKEDIN-64ffda?style=for-the-badge&logoColor=020c1b)](https://www.linkedin.com/in/aimen-abdesselam-bab937223/)&nbsp;&nbsp;[![GITHUB](https://img.shields.io/badge/ALL_REPOS-64ffda?style=for-the-badge&logoColor=020c1b)](https://github.com/AimenAbdesslame?tab=repositories)&nbsp;&nbsp;[![LIVE DEMO](https://img.shields.io/badge/▲_LIVE_DEMO-64ffda?style=for-the-badge&logoColor=020c1b)](https://multimodal-brain-tumor-diagnostics.vercel.app)&nbsp;&nbsp;[![PAPER](https://img.shields.io/badge/RESEARCH_PAPER-64ffda?style=for-the-badge&logoColor=020c1b)](https://drive.google.com/file/d/1BGBiM9NWthjeNTqe7vRC0PhU4XXtyTR6/view?usp=sharing)

<br/>

*Thanks for scrolling.*<br/>
*Let's build something that counts.*

<br/>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:020c1b,50:0a192f,100:020c1b&height=80&section=footer"/>

</div>
