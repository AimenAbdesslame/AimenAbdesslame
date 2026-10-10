<div align="center">
  <img src="assets/banner.svg" alt="Abdesselam Aimen: AI & Deep Learning Researcher · Computer Vision Engineer · Medical Imaging · Graph Neural Networks" width="100%">
</div>

<p align="center">
  <img src="https://img.shields.io/badge/ESI--SBA-IASD_AI_%26_Data_Science-3b8ae6?style=for-the-badge" alt="ESI-SBA IASD">
  <img src="https://img.shields.io/badge/Degree-Master's_M2_Candidate-34d399?style=for-the-badge" alt="Master's Candidate">
  <img src="https://img.shields.io/badge/Languages-EN_·_FR_·_AR-fbbf24?style=for-the-badge" alt="Languages">
  <img src="https://img.shields.io/badge/Seeking-6--Month_Research_PFE-a78bfa?style=for-the-badge" alt="Seeking Research PFE">
</p>

<p align="center"><i>I develop multi-task deep learning architectures, 2D medical vision pipelines, and decentralized graph neural networks.<br>
Final-year Master's student at ESI-SBA (Algeria 🇩🇿), actively interviewing for a 6-month AI Research PFE starting Feb/Mar 2027.</i></p>

<img src="assets/stats.svg" alt="0.726 BraTS20 Dice · 0.962 Tumor ROC-AUC · -41% Latency drop · 5.3ms Per-slice inference · 7.77M Shared params" width="100%">

<br><br>

<img src="assets/h-01.svg" alt="01 Showreel" width="100%">

<div align="center">
  <img src="assets/showreel.svg" alt="Showreel: BraTS20 Medical AI, GNN Drone Swarm, CINEMATCH RecSys, E-VENTI" width="100%">
</div>

<p align="center">
  <a href="https://multimodal-brain-tumor-diagnostics.vercel.app/"><img src="https://img.shields.io/badge/BraTS20_Clinical_App-open_app-34d399?style=flat-square&logo=vercel&logoColor=white" alt="BraTS20 Clinical App"></a>
  <a href="https://drive.google.com/file/d/1BGBiM9NWthjeNTqe7vRC0PhU4XXtyTR6/view?usp=sharing"><img src="https://img.shields.io/badge/Research_Paper-read_pdf-a78bfa?style=flat-square&logo=googledocs&logoColor=white" alt="Research Paper"></a>
  <a href="https://github.com/AimenAbdesslame/CINEMATCH_movie-recommender-system"><img src="https://img.shields.io/badge/CINEMATCH_RecSys-open_app-fbbf24?style=flat-square&logo=streamlit&logoColor=white" alt="CINEMATCH RecSys"></a>
  <a href="https://github.com/AimenAbdesslame/E-VENTI_Front-End"><img src="https://img.shields.io/badge/E--VENTI_Platform-open_repo-3b8ae6?style=flat-square&logo=react&logoColor=white" alt="E-VENTI Platform"></a>
</p>

<br>

<img src="assets/h-02.svg" alt="02 Projects" width="100%">

<img src="assets/sub-research.svg" alt="Research and systems" width="100%">

<a href="https://github.com/AimenAbdesslame/multimodal-brain-tumor-diagnostics"><img src="assets/c-brats.svg" alt="Multi-Task Brain Tumor Diagnosis on BraTS20" width="100%"></a>

<details>
<summary><b>How the research pipeline fits together</b> (architecture)</summary>
<br>

```mermaid
flowchart LR
    M["🧠 4-Modality 2D MRI<br/>"] --> E
    E["⚡ Shared U-Net Encoder<br/>7.77M parameters"] --> S["🎯 Decoder Head A<br/>Dice segmentation"]
    E --> C["📊 Decoder Head B<br/>BCE tumor grade"]
    S & C --> K{{"⚖️ Kendall Uncertainty<br/>+ PCGrad Surgery"}}
    K --> F["🚀 FastAPI (5.3ms)<br/>Docker Container"]
    F --> R["💻 React Clinical UI<br/>Vercel (Live)"]
```

</details>

<a href="https://github.com/AimenAbdesslame/gnn_drone_project"><img src="assets/c-drone.svg" alt="GNN Drone Swarm Optimization" width="100%"></a>
<p align="center">
  <a href="https://github.com/AimenAbdesslame/gnn_drone_project"><img src="https://img.shields.io/badge/Technical_Report_&_Docs-181717?style=for-the-badge&logo=github&logoColor=white" alt="Technical Report & Docs"></a>
</p>

<table>
<tr>
<td width="50%" align="center">
  <a href="https://github.com/AimenAbdesslame/CINEMATCH_movie-recommender-system"><img src="assets/c-cinematch.svg" alt="CINEMATCH RecSys" width="100%"></a><br>
  <a href="https://github.com/AimenAbdesslame/CINEMATCH_movie-recommender-system"><img src="https://img.shields.io/badge/Live_App_Demo-3b8ae6?style=for-the-badge&logo=streamlit&logoColor=white" alt="Live App Demo"></a>
</td>
<td width="50%" align="center">
  <a href="https://github.com/AimenAbdesslame/breast-cancer-unsupervised-app"><img src="assets/c-breast.svg" alt="Breast Cancer Clustering" width="100%"></a><br>
  <a href="https://github.com/AimenAbdesslame/breast-cancer-unsupervised-app"><img src="https://img.shields.io/badge/Case_Study-a78bfa?style=for-the-badge&logo=jupyter&logoColor=white" alt="Case Study"></a>
</td>
</tr>
<tr>
<td align="center">
  <a href="https://github.com/AimenAbdesslame/Linear_Regression_from_Scratch__No_ML_Libraries"><img src="assets/c-linreg.svg" alt="Linear Regression From Scratch" width="100%"></a><br>
  <a href="https://github.com/AimenAbdesslame/Linear_Regression_from_Scratch__No_ML_Libraries"><img src="https://img.shields.io/badge/NumPy_First_Principles-fbbf24?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy First Principles"></a>
</td>
<td align="center">
  <a href="https://github.com/AimenAbdesslame/Logistic_Regression_from_Scratch__No_ML_Libraries"><img src="assets/c-logreg.svg" alt="Logistic Regression From Scratch" width="100%"></a><br>
  <a href="https://github.com/AimenAbdesslame/Logistic_Regression_from_Scratch__No_ML_Libraries"><img src="https://img.shields.io/badge/NumPy_First_Principles-fbbf24?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy First Principles"></a>
</td>
</tr>
</table>

<br>

<img src="assets/sub-academic.svg" alt="Academic Projects (Big Data, ML, Base de Données)" width="100%">

<table>
<tr>
<td width="50%" align="center">
  <a href="https://github.com/AimenAbdesslame/IASD-university-projects-Labs-S1"><img src="assets/c-academic-s1.svg" alt="IASD Master's S1 Academic Labs: Big Data, ML & Databases" width="100%"></a><br>
  <a href="https://github.com/AimenAbdesslame/IASD-university-projects-Labs-S1"><img src="https://img.shields.io/badge/See_Academic_Projects_S1-Big_Data_·_ML_·_Bases_de_Données-a78bfa?style=for-the-badge&logo=github&logoColor=white" alt="See Academic Projects S1"></a>
</td>
<td width="50%" align="center">
  <a href="https://github.com/AimenAbdesslame/IASD-university-projects-Labs-S2"><img src="assets/c-academic-s2.svg" alt="IASD Master's S2 Academic Labs: Deep Learning & Computer Vision" width="100%"></a><br>
  <a href="https://github.com/AimenAbdesslame/IASD-university-projects-Labs-S2"><img src="https://img.shields.io/badge/See_Academic_Projects_S2-Deep_Learning_·_Vision_·_Optimization-38bdf8?style=for-the-badge&logo=github&logoColor=white" alt="See Academic Projects S2"></a>
</td>
</tr>
</table>

<br>

<img src="assets/sub-web.svg" alt="Also shipped: web and product" width="100%">

<table>
<tr>
<td width="50%" align="center">
  <a href="https://github.com/AimenAbdesslame/E-VENTI_Front-End"><img src="assets/c-eventi.svg" alt="E-VENTI Front-End" width="100%"></a><br>
  <a href="https://github.com/AimenAbdesslame/E-VENTI_Front-End"><img src="https://img.shields.io/badge/Frontend_Architecture-3b8ae6?style=for-the-badge&logo=react&logoColor=white" alt="Frontend Architecture"></a>
</td>
<td width="50%" align="center">
  <a href="https://github.com/AimenAbdesslame/social_media_react"><img src="assets/c-social.svg" alt="Social Media React" width="100%"></a><br>
  <a href="https://github.com/AimenAbdesslame/social_media_react"><img src="https://img.shields.io/badge/MUI_5_Interface-181717?style=for-the-badge&logo=mui&logoColor=white" alt="MUI 5 Interface"></a>
</td>
</tr>
<tr>
<td align="center">
  <a href="https://github.com/AimenAbdesslame/Fitness_Supplements_app"><img src="assets/c-fitness.svg" alt="Fitness Supplements App" width="100%"></a><br>
  <a href="https://github.com/AimenAbdesslame/Fitness_Supplements_app"><img src="https://img.shields.io/badge/Web_Application-34d399?style=for-the-badge&logo=javascript&logoColor=white" alt="Web Application"></a>
</td>
<td align="center">
  <a href="https://github.com/AimenAbdesslame/numpy-100-exercises-solutions"><img src="assets/c-numpy.svg" alt="NumPy 100 & TCP" width="100%"></a><br>
  <a href="https://github.com/AimenAbdesslame/Socket-TCP_networking"><img src="https://img.shields.io/badge/TCP_Networking-3b8ae6?style=for-the-badge&logo=typescript&logoColor=white" alt="TCP Networking"></a>
</td>
</tr>
</table>

<details>
<summary><b>More experiments</b> · university labs, data pipelines & notebooks</summary>
<br>

- [`IASD-university-projects-Labs-S1`](https://github.com/AimenAbdesslame/IASD-university-projects-Labs-S1): S1 university curriculum labs, algorithmic foundations, probabilistic models
- [`IASD-university-projects-Labs-S2`](https://github.com/AimenAbdesslame/IASD-university-projects-Labs-S2): S2 university labs in computer vision, deep learning pipelines, optimization
- [`paris-2024-olympics-dashboard`](https://github.com/AimenAbdesslame/paris-2024-olympics-dashboard): Olympic games data analysis, metric exploration, interactive visualization
- [`Socket-TCP_networking`](https://github.com/AimenAbdesslame/Socket-TCP_networking): Asynchronous client/server network transport layer in TypeScript
- [`numpy-100-exercises-solutions`](https://github.com/AimenAbdesslame/numpy-100-exercises-solutions): Comprehensive 100-problem benchmark suite covering advanced vectorized operations

</details>

<br>

<img src="assets/h-03.svg" alt="03 Journey" width="100%">

```text
$ traceroute --story aimen

 hop  where                                     what happened
 ───  ────────────────────────────────────────  ──────────────────────────────────────────────
  1   ESI-SBA · 2021 → now                      Integrated Preparatory Cycle & Engineering Degree
  2   IASD Master's Track · 2025 → 2027         Specialization: Artificial Intelligence & Data Science
  3   Foundations · 2024–25                     NumPy from-scratch ML, TCP sockets, 100 numerical labs
  4   Full-Stack Systems · 2023                 Shipped E-VENTI, Social Media React, Fitness web apps
  5   EnoGeo internship  (Sonatrach subsidiary)· 2024                Data analysis, pipeline & discovery of departements rely them with ai
  6   Team R&D · 2026                           GNN Drone Swarm Optimization: multi-agent spatial coordination
  7   Solo Research Lead · 2026                 BraTS20 Dual-Head U-Net: Kendall uncertainty + PCGrad surgery
  8   → I am here                            seeking 6-month Master's PFE in AI / Deep Learning (Feb/Mar 2027)

 trace complete. destination reachable.
```

<br>

<img src="assets/h-04.svg" alt="04 Stack" width="100%">

<div align="center">
  <img src="assets/skills-marquee.svg" alt="Skills: AI Engineering, Deep Learning, PyTorch, Transformers, LLMs, Reinforcement Learning, FastAPI, Docker, Power BI, Scikit-learn, and more" width="100%">
</div>

<br>

<table>
<tr>
<td width="170"><b>Languages</b></td>
<td><img src="https://skillicons.dev/icons?i=py,cpp,c,ts,js,html,css&theme=dark" alt="Python, C++, C, TypeScript, JavaScript, HTML, CSS"><br><sub><code>Python (Scientific Computing)</code> <code>Modern C++</code> <code>C</code> <code>TypeScript</code> <code>SQL</code></sub></td>
</tr>
<tr>
<td><b>ML &amp; Deep Learning</b></td>
<td><img src="assets/stack-mldl.svg" alt="PyTorch, Scikit-learn, OpenCV, NumPy, Pandas, Reinforcement Learning" height="48"><br><sub><code>PyTorch Geometric</code> <code>CNNs &amp; U-Net</code> <code>Graph Neural Networks</code> <code>Multi-Task Learning</code> <code>Reinforcement Learning (RL)</code> <code>Medical Vision</code></sub></td>
</tr>
<tr>
<td><b>Transformers &amp; LLMs</b></td>
<td><img src="assets/stack-transformers.svg" alt="Hugging Face, Transformers, LLMs, LangChain, LlamaIndex" height="48"><br><sub><code>Hugging Face Transformers</code> <code>LLM Fine-Tuning (LoRA / QLoRA)</code> <code>RAG Systems</code> <code>Prompt Engineering</code> <code>Vector Embeddings</code> <code>LangChain &amp; LlamaIndex</code></sub></td>
</tr>
<tr>
<td><b>AI Engineering &amp; MLOps</b></td>
<td><img src="assets/stack-aieng.svg" alt="FastAPI, Docker, Weights & Biases, MLflow, ONNX, Streamlit" height="48"><br><sub><code>FastAPI Microservices (5.3ms)</code> <code>Docker Deployment</code> <code>Weights &amp; Biases (W&amp;B)</code> <code>MLflow Tracking</code> <code>ONNX Runtime</code> <code>Vector Databases (Chroma / Pinecone)</code></sub></td>
</tr>
<tr>
<td><b>Data Analytics &amp; BI</b></td>
<td><img src="assets/stack-data.svg" alt="Power BI, Pandas, NumPy, Jupyter, SQL" height="48"><br><sub><code>Data Cleaning &amp; Imputation</code> <code>Power BI Dashboards</code> <code>Exploratory Data Analysis (EDA)</code> <code>Feature Engineering</code> <code>Statistical Modeling</code></sub></td>
</tr>
<tr>
<td><b>Web &amp; Backend</b></td>
<td><img src="https://skillicons.dev/icons?i=fastapi,react,tailwind,nodejs,express&theme=dark" alt="FastAPI, React, Tailwind, Node.js, Express"><br><sub><code>RESTful APIs</code> <code>React / Next.js</code> <code>Interactive Clinical Dashboards</code> <code>TypeScript</code></sub></td>
</tr>
<tr>
<td><b>Tools &amp; DevOps</b></td>
<td><img src="https://skillicons.dev/icons?i=docker,linux,git,github,vscode,bash&theme=dark" alt="Docker, Linux, Git, GitHub, VS Code, Bash"><br><sub><code>Linux Environments</code> <code>Git &amp; GitHub Workflows</code> <code>CI/CD Pipelines</code> <code>Bash Scripting</code></sub></td>
</tr>
<tr>
<td><b>Core Math &amp; Theory</b></td>
<td><code>Machine Learning (ML)</code> <code>Deep Learning</code> <code>Reinforcement Learning</code> <code>Data Cleaning &amp; Preprocessing</code> <code>Data Visualization (Power BI)</code> <code>Multi-Task Learning</code> <code>Graph Neural Networks</code> <code>Medical Image Segmentation</code> <code>Homoscedastic Uncertainty</code> <code>Gradient Surgery</code></td>
</tr>
<tr>
<td><b>Soft Skills</b></td>
<td>Research synthesis · technical writing · experimental rigor · cross-functional collaboration · agile delivery</td>
</tr>
</table>

<br>

<img src="assets/h-05.svg" alt="05 Field notes" width="100%">

- 🧠 **BraTS 2020 Multi-Task Research Lead**: Dual-Head U-Net on 2D MRI, 0.726 Dice, 0.962 ROC-AUC, -41% latency (5.3ms/slice)
- 🚁 **GNN Swarm Optimization Co-Author**: Decentralized multi-agent spatial coordination using PyTorch Geometric & MARL
- 🎓 **ESI-SBA IASD Track**: M.Sc. in AI & Data Science, specialized in deep learning, medical computer vision & graph learning
- 🔬 **First-Principles ML**: Vectorized gradient descent & classification engines written purely from scratch in NumPy
- 🌍 **PFE Availability**: Actively seeking a 6-month Master's PFE (End-of-Studies Internship) in European R&D labs starting Feb/Mar 2027

<br>

<img src="assets/h-06.svg" alt="06 Connect" width="100%">

<p align="center">
  <a href="https://www.linkedin.com/in/aimen-abdesselam-bab937223/"><img src="https://img.shields.io/badge/LinkedIn-Aimen_Abdesselam-3b8ae6?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://multimodal-brain-tumor-diagnostics.vercel.app/"><img src="https://img.shields.io/badge/Live_Portfolio_Demo-34d399?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio App"></a>
  <a href="mailto:aimen.abdesselam@outlook.com"><img src="https://img.shields.io/badge/Email-Say_hello-a78bfa?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
</p>

<img src="assets/footer.svg" alt="Thanks for scrolling. Let's build something that connects." width="100%">
