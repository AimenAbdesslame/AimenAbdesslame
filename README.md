<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,40:0f2744,100:0d1117&height=220&section=header&text=Aimen%20Abdesselam&fontSize=58&fontColor=ffffff&fontAlignY=40&desc=AI%20Research%20Engineer%20%E2%80%94%20Medical%20Imaging%20%C2%B7%20Computer%20Vision%20%C2%B7%20Graph%20Neural%20Networks&descSize=15&descAlignY=62&descColor=58a6ff&animation=fadeIn" />

</div>

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&pause=1000&color=58A6FF&center=true&vCenter=true&width=600&lines=M.Sc.+AI+%26+Computer+Vision+%E2%80%94+IASD;Multi-Task+Medical+Imaging+Researcher;Production+AI+%7C+MLOps+%7C+Full-Stack+Engineer;Open+to+European+PFE+%E2%80%94+Feb%2FMar+2027)](https://github.com/AimenAbdesslame)

</div>

---

<div align="center">

### `>> ACTIVELY SEEKING PFE INTERNSHIP — 6 MONTHS — FEB / MAR 2027`

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aimen-abdesselam-bab937223/)&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-AimenAbdesslame-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AimenAbdesslame)&nbsp;
[![Live App](https://img.shields.io/badge/Live%20Demo-%F0%9F%A7%A0%20Brain%20Tumor%20AI-00d4aa?style=flat-square)](https://multimodal-brain-tumor-diagnostics.vercel.app)&nbsp;
[![Research Paper](https://img.shields.io/badge/Research%20Paper-PDF-FF4B4B?style=flat-square&logo=googledrive&logoColor=white)](https://drive.google.com/file/d/1BGBiM9NWthjeNTqe7vRC0PhU4XXtyTR6/view?usp=sharing)

</div>

---

## 01 · IDENTITY

```python
profile = {
  "name"        :  "Aimen Abdesselam",
  "degree"      :  "M.Sc. Artificial Intelligence & Computer Vision  (IASD)",
  "graduation"  :  "June 2027",
  "languages"   :  ["French 🇫🇷", "English 🇬🇧", "Arabic 🇩🇿"],
  "location"    :  "France  ·  Open to Europe & Remote",
  "seeking"     :  "PFE / Stage de fin d'études  —  6 months  —  Feb–Mar 2027",
  "targets"     :  ["Owkin", "INRIA", "Siemens Healthineers", "Philips Healthcare",
                    "European AI R&D Labs", "AI Scaleups"],
  "core_skills" :  ["Medical Imaging AI", "Multi-Task Deep Learning",
                    "Graph Neural Networks", "MLOps", "Full-Stack AI Systems"],
}
```

---

## 02 · AI RESEARCH PROJECTS

<br/>

### `[SOLO LEAD]` 🧠 Multi-Task Brain Tumor Diagnosis on BraTS20

> **The full-spectrum research project: from 3D MRI tensor engineering to a live production clinical app.**

<table>
  <tr>
    <td valign="top" width="55%">

**Architecture:** Dual-Head U-Net — shared encoder, two specialized decoder heads

**Research Innovations:**
- 🔬 **Kendall Uncertainty Weighting** — learned, adaptive multi-task loss scaling
- ⚗️ **PCGrad Gradient Surgery** — resolves cross-task gradient conflicts
- 🧩 Joint **segmentation + classification** from a single 7.77M-param model

**Production Stack:**
- Backend: `FastAPI` · `Docker` · `Render`
- Frontend: `React` · `Tailwind CSS` · `Vercel`
- Tracking: `Weights & Biases`

    </td>
    <td valign="top" width="45%">

| KPI | Score |
|-----|-------|
| 🎯 Dice Score | **0.726** |
| 📈 ROC-AUC | **0.962** |
| ⚡ Inference | **5.3 ms / slice** |
| 📉 Latency ↓ | **−41 %** |
| 🗜️ Parameters | **7.77 M** (−50 %) |
| 🧩 Tasks | Seg. + Classif. |
| 📦 Dataset | BraTS 2020 |
| 🔬 Modalities | T1 · T1ce · T2 · FLAIR |

  </td>
  </tr>
</table>

[![Repo](https://img.shields.io/badge/⚗%20Code-multimodal--brain--tumor--diagnostics-1f6feb?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AimenAbdesslame/multimodal-brain-tumor-diagnostics)&nbsp;
[![Live](https://img.shields.io/badge/🌐%20Live%20App-vercel.app-00C7B7?style=for-the-badge&logo=vercel&logoColor=black)](https://multimodal-brain-tumor-diagnostics.vercel.app)&nbsp;
[![Paper](https://img.shields.io/badge/📄%20Research%20Paper-Read%20PDF-FF4B4B?style=for-the-badge&logo=googledrive&logoColor=white)](https://drive.google.com/file/d/1BGBiM9NWthjeNTqe7vRC0PhU4XXtyTR6/view?usp=sharing)

```
PyTorch · Dual-Head U-Net · Kendall Uncertainty · PCGrad · FastAPI
React · Tailwind CSS · Docker · Weights & Biases · Render · Vercel
```

<br/>

---

### `[CO-AUTHOR]` 🚁 GNN Drone Swarm Optimization

> **Graph-structured multi-agent coordination at the intersection of geometric deep learning and autonomous systems.**

<table>
  <tr>
    <td valign="top" width="55%">

**Research Focus:**
- 🕸️ Graph Neural Network message-passing for swarm topology modeling
- 🤖 Multi-agent Reinforcement Learning for decentralized trajectory planning
- 📐 Spatial node features: position · velocity · heading vectors
- ⚙️ C++ firmware integration layer for real-time drone telemetry

**Problem:** Each drone = graph node. Inter-drone radio links = graph edges. GNN learns optimal collective behavior through localized message exchange — no central coordinator.

    </td>
    <td valign="top" width="45%">

| Layer | Technology |
|-------|-----------|
| Graph Learning | PyTorch Geometric |
| Agent Policy | Multi-Agent RL |
| Node Features | Spatial Encoding |
| Communication | Graph Message Passing |
| Systems Bridge | C++ |
| Environment | Custom Swarm Sim |

  </td>
  </tr>
</table>

[![Repo](https://img.shields.io/badge/⚗%20Code-gnn--drone--project-1f6feb?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AimenAbdesslame/gnn_drone_project)

```
PyTorch Geometric · Graph Neural Networks · Multi-Agent RL · C++
```

<br/>

---

## 03 · FULL PROJECT PORTFOLIO

<br/>

**🔬 Medical & Oncology AI**

| Project | Role | Key Result | Stack |
|---------|------|-----------|-------|
| [multimodal-brain-tumor-diagnostics](https://github.com/AimenAbdesslame/multimodal-brain-tumor-diagnostics) | Solo Lead | 0.726 Dice · 0.962 AUC · 5.3ms | PyTorch · FastAPI · React |
| [breast-cancer-unsupervised-app](https://github.com/AimenAbdesslame/breast-cancer-unsupervised-app) | Solo | Cluster-based pattern discovery | Scikit-learn · Python |

<br/>

**🤖 Autonomous Systems & Graph AI**

| Project | Role | Focus | Stack |
|---------|------|-------|-------|
| [gnn_drone_project](https://github.com/AimenAbdesslame/gnn_drone_project) | Co-Author | Swarm coordination via GNN | PyTorch Geometric · RL · C++ |

<br/>

**🎯 Applied ML & RecSys**

| Project | Description | Stack |
|---------|-------------|-------|
| [CINEMATCH_movie-recommender-system](https://github.com/AimenAbdesslame/CINEMATCH_movie-recommender-system) | Hybrid recommender: content + collab filtering + matrix factorization | Python · Streamlit |
| [paris-2024-olympics-dashboard](https://github.com/AimenAbdesslame/paris-2024-olympics-dashboard) | Sports analytics & data visualization | Data Viz |

<br/>

**🛠️ ML Foundations — Numerical Engineering from Scratch**

| Project | What It Proves | Stars |
|---------|---------------|-------|
| [Linear_Regression_from_Scratch](https://github.com/AimenAbdesslame/Linear_Regression_from_Scratch__No_ML_Libraries) | Gradient descent, cost function, pure NumPy — no sklearn | ⭐ 2 |
| [Logistic_Regression_from_Scratch](https://github.com/AimenAbdesslame/Logistic_Regression_from_Scratch__No_ML_Libraries) | Binary classifier from first principles | ⭐ 2 |
| [numpy-100-exercises-solutions](https://github.com/AimenAbdesslame/numpy-100-exercises-solutions) | 100 NumPy challenges — beginner to advanced, all solved independently | ⭐ 2 |
| [Socket-TCP_networking](https://github.com/AimenAbdesslame/Socket-TCP_networking) | Real-time TCP client-server communication | ⭐ 2 |

<br/>

**🎓 University Research Labs — M.Sc. IASD**

| Repo | Semester | Scope |
|------|----------|-------|
| [IASD-Labs-S1](https://github.com/AimenAbdesslame/IASD-university-projects-Labs-S1) | Sem. 1 | Supervised/unsupervised ML · Optimization · Statistical Learning |
| [IASD-Labs-S2](https://github.com/AimenAbdesslame/IASD-university-projects-Labs-S2) | Sem. 2 | Deep Learning · Computer Vision · Probabilistic Models |

<br/>

**💻 Full-Stack Engineering**

| Project | Stack |
|---------|-------|
| [E-VENTI_Front-End](https://github.com/AimenAbdesslame/E-VENTI_Front-End) | TypeScript · React — event management platform |
| [social_media_react](https://github.com/AimenAbdesslame/social_media_react) | React · MUI 5 — social feed UI |
| [Fitness_Supplements_app](https://github.com/AimenAbdesslame/Fitness_Supplements_app) | JavaScript — gym exercise & supplement tracker |

---

## 04 · STACK

<br/>

**AI · Deep Learning · Computer Vision**

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)&nbsp;
![PyG](https://img.shields.io/badge/PyTorch_Geometric-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)&nbsp;
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)&nbsp;
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)&nbsp;
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)&nbsp;
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)&nbsp;
![MONAI](https://img.shields.io/badge/MONAI-Medical_AI-0088CC?style=flat-square)&nbsp;
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square)&nbsp;

**MLOps · Deployment · Infrastructure**

![W&B](https://img.shields.io/badge/Weights_%26_Biases-FFBE00?style=flat-square&logo=weightsandbiases&logoColor=black)&nbsp;
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)&nbsp;
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)&nbsp;
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white)&nbsp;
![Render](https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=black)&nbsp;
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)&nbsp;

**Languages**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)&nbsp;
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)&nbsp;
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)&nbsp;
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)&nbsp;
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)&nbsp;

**Frontend**

![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)&nbsp;
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)&nbsp;
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)&nbsp;

---

## 05 · GITHUB ANALYTICS

<div align="center">

<br/>

<img height="175em" src="https://github-readme-stats.vercel.app/api?username=AimenAbdesslame&show_icons=true&theme=github_dark&include_all_commits=true&count_private=true&hide_border=true&bg_color=0d1117&title_color=58a6ff&icon_color=1f6feb&text_color=8b949e&ring_color=58a6ff" />
<img height="175em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=AimenAbdesslame&layout=compact&langs_count=8&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=58a6ff&text_color=8b949e" />

<br/>

<img width="60%" src="https://github-readme-streak-stats.herokuapp.com/?user=AimenAbdesslame&theme=github-dark-blue&hide_border=true&background=0d1117&stroke=1f6feb&ring=58a6ff&fire=ff7b72&currStreakLabel=58a6ff&sideLabels=8b949e&dates=8b949e" />

<br/>

</div>

---

## 06 · RESEARCH DEPTH

| Concept | Implementation Evidence |
|---------|------------------------|
| Multi-task loss balancing | Kendall homoscedastic uncertainty weighting — learned σ per task |
| Gradient conflict resolution | PCGrad surgery applied across segmentation + classification heads |
| 3D volumetric data pipeline | BraTS20 T1/T1ce/T2/FLAIR tensor fusion, NIfTI preprocessing |
| Graph message passing | PyTorch Geometric node/edge feature encoding for drone swarm |
| Production AI serving | FastAPI async inference · Docker container · 5.3 ms/slice live SLA |
| Model compression | 50 % parameter reduction (7.77M vs 15.5M) with zero accuracy loss |
| Numerical ML foundations | Linear & Logistic Regression from scratch — pure NumPy, no sklearn |
| Unsupervised learning | K-means / hierarchical clustering on real oncology patient data |

---

## 07 · CONNECT

<div align="center">

<br/>

### Available · Feb / Mar 2027 · 6-Month PFE · Europe or Remote

<br/>

| I'm looking for | Locations | Start |
|:---:|:---:|:---:|
| PFE / Stage de fin d'études | 🇫🇷 France · 🇩🇪 Germany · 🇳🇱 Netherlands · 🇬🇧 UK | Feb 2027 |
| AI Research Engineer Internship | Europe · Remote | Feb 2027 |
| Computer Vision / Medical AI | Any European AI Hub | Feb 2027 |

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn%20—%20Let's%20Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aimen-abdesselam-bab937223/)&nbsp;
[![GitHub](https://img.shields.io/badge/All%20Repositories-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AimenAbdesslame?tab=repositories)&nbsp;
[![Demo](https://img.shields.io/badge/Live%20AI%20Demo-00d4aa?style=for-the-badge&logo=vercel&logoColor=black)](https://multimodal-brain-tumor-diagnostics.vercel.app)&nbsp;
[![Paper](https://img.shields.io/badge/Research%20Paper%20PDF-FF4B4B?style=for-the-badge&logo=googledrive&logoColor=white)](https://drive.google.com/file/d/1BGBiM9NWthjeNTqe7vRC0PhU4XXtyTR6/view?usp=sharing)

<br/>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,60:0f2744,100:0d1117&height=100&section=footer" />

</div>
