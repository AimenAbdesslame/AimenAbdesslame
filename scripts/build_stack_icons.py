import re
import os

# Helper to read file
def read_f(fn):
    with open(fn, 'r', encoding='utf-8') as f:
        return f.read()

# Helper to extract the inner content of skillicons (which are 256x256)
def extract_skillicon_inner(fn):
    content = read_f(fn)
    # skillicons format:
    # <svg ... viewBox="0 0 256 256" ...><rect ... rx="60" fill="#242938"/> ... </svg>
    # We want everything between <svg ...> and </svg>
    m = re.search(r'<svg[^>]*>(.*)</svg>', content, re.DOTALL)
    if m:
        return m.group(1).strip()
    return ""

# Helper to extract path d from simple-icons (viewBox="0 0 24 24")
def extract_si_path(fn):
    content = read_f(fn)
    # find all path d
    matches = re.findall(r'<path[^>]*d="([^"]+)"', content)
    return matches

# Colors for simple-icons
COLORS = {
    'numpy': '#4DABCF',
    'pandas': '#FFFFFF', # pandas white on dark squircle
    'huggingface': '#FFD21E',
    'langchain': '#22C55E',
    'wandb': '#FFBE00',
    'mlflow': '#0194E2',
    'streamlit': '#FF4B4B',
    'jupyter': '#F37626',
    'postgresql': '#4169E1'
}

def make_simpleicon_box(x, paths, fill_color, rx=11, width=48, height=48):
    path_tags = ""
    for d in paths:
        path_tags += f'<path fill="{fill_color}" d="{d}"/>'
    return f'''
    <g transform="translate({x}, 0)">
      <rect width="{width}" height="{height}" rx="{rx}" fill="#242938"/>
      <g transform="translate(10, 10) scale(1.16667)">
        {path_tags}
      </g>
    </g>'''

def make_skillicon_box(x, inner_svg, rx=11, width=48, height=48):
    # inner_svg is in 256x256 coordinate system
    # scale factor = 48 / 256 = 0.1875
    return f'''
    <g transform="translate({x}, 0)">
      <svg width="{width}" height="{height}" viewBox="0 0 256 256">
        {inner_svg}
      </svg>
    </g>'''

def make_rl_box(x, rx=11, width=48, height=48):
    return f'''
    <g transform="translate({x}, 0)">
      <rect width="{width}" height="{height}" rx="{rx}" fill="#242938"/>
      <!-- Agent node -->
      <circle cx="24" cy="24" r="8" fill="#34d399" fill-opacity="0.18" stroke="#34d399" stroke-width="1.6"/>
      <text x="24" y="27.5" font-family="'SF Mono','Fira Code',Consolas,monospace" font-size="8.5" font-weight="900" fill="#34d399" text-anchor="middle">RL</text>
      <!-- Action top loop (Agent -> Env) -->
      <path d="M 17 14 C 20 10, 28 10, 31 14" fill="none" stroke="#38bdf8" stroke-width="1.8" stroke-linecap="round"/>
      <polygon points="33,14 30,12 30,16" fill="#38bdf8"/>
      <!-- Reward bottom loop (Env -> Agent) -->
      <path d="M 31 34 C 28 38, 20 38, 17 34" fill="none" stroke="#34d399" stroke-width="1.8" stroke-linecap="round"/>
      <polygon points="15,34 18,36 18,32" fill="#34d399"/>
    </g>'''

def make_powerbi_box(x, rx=11, width=48, height=48):
    return f'''
    <g transform="translate({x}, 0)">
      <rect width="{width}" height="{height}" rx="{rx}" fill="#242938"/>
      <!-- Power BI 3-bar chart -->
      <rect x="13" y="26" width="5.5" height="12" rx="2" fill="#f2c811" fill-opacity="0.85"/>
      <rect x="21.25" y="19" width="5.5" height="19" rx="2" fill="#f2c811"/>
      <rect x="29.5" y="10" width="5.5" height="28" rx="2" fill="#f2c811"/>
      <!-- Gloss overlay -->
      <rect x="13" y="26" width="5.5" height="4" rx="1.5" fill="#fff" fill-opacity="0.3"/>
      <rect x="21.25" y="19" width="5.5" height="4" rx="1.5" fill="#fff" fill-opacity="0.3"/>
      <rect x="29.5" y="10" width="5.5" height="4" rx="1.5" fill="#fff" fill-opacity="0.3"/>
    </g>'''

def make_transformers_box(x, rx=11, width=48, height=48):
    return f'''
    <g transform="translate({x}, 0)">
      <rect width="{width}" height="{height}" rx="{rx}" fill="#242938"/>
      <!-- Attention lattice / Transformer architecture -->
      <!-- Input layer -->
      <circle cx="15" cy="14" r="3" fill="#818cf8"/>
      <circle cx="15" cy="24" r="3" fill="#818cf8"/>
      <circle cx="15" cy="34" r="3" fill="#818cf8"/>
      <!-- Output layer -->
      <circle cx="33" cy="14" r="3" fill="#38bdf8"/>
      <circle cx="33" cy="24" r="3" fill="#38bdf8"/>
      <circle cx="33" cy="34" r="3" fill="#38bdf8"/>
      <!-- Attention weight links -->
      <line x1="15" y1="14" x2="33" y2="14" stroke="#a855f7" stroke-width="1.2" stroke-opacity="0.8"/>
      <line x1="15" y1="14" x2="33" y2="24" stroke="#a855f7" stroke-width="0.8" stroke-opacity="0.5"/>
      <line x1="15" y1="24" x2="33" y2="24" stroke="#c084fc" stroke-width="1.6" stroke-opacity="0.9"/>
      <line x1="15" y1="24" x2="33" y2="34" stroke="#a855f7" stroke-width="0.8" stroke-opacity="0.5"/>
      <line x1="15" y1="34" x2="33" y2="34" stroke="#a855f7" stroke-width="1.2" stroke-opacity="0.8"/>
      <line x1="15" y1="34" x2="33" y2="14" stroke="#a855f7" stroke-width="0.7" stroke-opacity="0.4"/>
    </g>'''

def make_llm_box(x, rx=11, width=48, height=48):
    return f'''
    <g transform="translate({x}, 0)">
      <rect width="{width}" height="{height}" rx="{rx}" fill="#242938"/>
      <!-- Generative Spark / Neural LLM -->
      <path d="M 24 10 C 24 18, 25 19, 32 21 C 25 23, 24 24, 24 32 C 24 24, 23 23, 16 21 C 23 19, 24 18, 24 10 Z" fill="#c084fc"/>
      <path d="M 33 27 C 33 30, 33.5 30.5, 36.5 31.5 C 33.5 32.5, 33 33, 33 36 C 33 33, 32.5 32.5, 29.5 31.5 C 32.5 30.5, 33 30, 33 27 Z" fill="#38bdf8"/>
    </g>'''

def make_llamaindex_box(x, rx=11, width=48, height=48):
    return f'''
    <g transform="translate({x}, 0)">
      <rect width="{width}" height="{height}" rx="{rx}" fill="#242938"/>
      <!-- LlamaIndex / Graph Index nodes -->
      <circle cx="24" cy="15" r="4.5" fill="#ec4899"/>
      <circle cx="16" cy="31" r="3.8" fill="#be185d"/>
      <circle cx="32" cy="31" r="3.8" fill="#db2777"/>
      <line x1="24" y1="15" x2="16" y2="31" stroke="#f472b6" stroke-width="1.8"/>
      <line x1="24" y1="15" x2="32" y2="31" stroke="#f472b6" stroke-width="1.8"/>
      <line x1="16" y1="31" x2="32" y2="31" stroke="#f472b6" stroke-width="1.2" stroke-dasharray="2,2"/>
    </g>'''

def make_onnx_box(x, rx=11, width=48, height=48):
    return f'''
    <g transform="translate({x}, 0)">
      <rect width="{width}" height="{height}" rx="{rx}" fill="#242938"/>
      <!-- ONNX Runtime interconnected blocks -->
      <rect x="13" y="13" width="9" height="9" rx="2" fill="#005ced"/>
      <rect x="26" y="13" width="9" height="9" rx="2" fill="#005ced" fill-opacity="0.75"/>
      <rect x="13" y="26" width="9" height="9" rx="2" fill="#005ced" fill-opacity="0.75"/>
      <rect x="26" y="26" width="9" height="9" rx="2" fill="#38bdf8"/>
      <line x1="17.5" y1="22" x2="17.5" y2="26" stroke="#fff" stroke-width="1.5"/>
      <line x1="22" y1="17.5" x2="26" y2="17.5" stroke="#fff" stroke-width="1.5"/>
      <line x1="26" y1="26" x2="22" y2="22" stroke="#fff" stroke-width="1.5"/>
    </g>'''

def build_strip(boxes, width, height=48):
    content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none">
    {''.join(boxes)}
</svg>'''
    return content

print("Helper functions ready.")

# GAP between icons = 8px, ICON_WIDTH = 48px -> step = 56px
GAP = 8
W = 48
H = 48

# 1. ML & Deep Learning: PyTorch, Scikit-learn, OpenCV, NumPy, Pandas, Reinforcement Learning (NO TensorFlow!)
mldl_boxes = [
    make_skillicon_box(0 * (W + GAP), extract_skillicon_inner('pytorch_si.svg')),
    make_skillicon_box(1 * (W + GAP), extract_skillicon_inner('sklearn_si.svg')),
    make_skillicon_box(2 * (W + GAP), extract_skillicon_inner('opencv_si.svg')),
    make_simpleicon_box(3 * (W + GAP), extract_si_path('numpy_si.svg'), COLORS['numpy']),
    make_simpleicon_box(4 * (W + GAP), extract_si_path('pandas_si.svg'), COLORS['pandas']),
    make_rl_box(5 * (W + GAP))
]
total_w_mldl = 6 * W + 5 * GAP
with open('assets/stack-mldl.svg', 'w', encoding='utf-8') as f:
    f.write(build_strip(mldl_boxes, total_w_mldl, H))
print("Created assets/stack-mldl.svg, width:", total_w_mldl)

# 2. Transformers & LLMs: Hugging Face, Transformers, LLMs, LangChain, LlamaIndex
trans_boxes = [
    make_simpleicon_box(0 * (W + GAP), extract_si_path('huggingface_si.svg'), COLORS['huggingface']),
    make_transformers_box(1 * (W + GAP)),
    make_llm_box(2 * (W + GAP)),
    make_simpleicon_box(3 * (W + GAP), extract_si_path('langchain_si.svg'), COLORS['langchain']),
    make_llamaindex_box(4 * (W + GAP))
]
total_w_trans = 5 * W + 4 * GAP
with open('assets/stack-transformers.svg', 'w', encoding='utf-8') as f:
    f.write(build_strip(trans_boxes, total_w_trans, H))
print("Created assets/stack-transformers.svg, width:", total_w_trans)

# 3. AI Engineering & MLOps: FastAPI, Docker, Weights & Biases, MLflow, ONNX, Streamlit
aieng_boxes = [
    make_skillicon_box(0 * (W + GAP), extract_skillicon_inner('fastapi_si.svg')),
    make_skillicon_box(1 * (W + GAP), extract_skillicon_inner('docker_si.svg')),
    make_simpleicon_box(2 * (W + GAP), extract_si_path('wandb_si.svg'), COLORS['wandb']),
    make_simpleicon_box(3 * (W + GAP), extract_si_path('mlflow_si.svg'), COLORS['mlflow']),
    make_onnx_box(4 * (W + GAP)),
    make_simpleicon_box(5 * (W + GAP), extract_si_path('streamlit_si.svg'), COLORS['streamlit'])
]
total_w_aieng = 6 * W + 5 * GAP
with open('assets/stack-aieng.svg', 'w', encoding='utf-8') as f:
    f.write(build_strip(aieng_boxes, total_w_aieng, H))
print("Created assets/stack-aieng.svg, width:", total_w_aieng)

# 4. Data Analytics & BI: Power BI, Pandas, NumPy, Jupyter, PostgreSQL/SQL
data_boxes = [
    make_powerbi_box(0 * (W + GAP)),
    make_simpleicon_box(1 * (W + GAP), extract_si_path('pandas_si.svg'), COLORS['pandas']),
    make_simpleicon_box(2 * (W + GAP), extract_si_path('numpy_si.svg'), COLORS['numpy']),
    make_simpleicon_box(3 * (W + GAP), extract_si_path('jupyter_si.svg'), COLORS['jupyter']),
    make_simpleicon_box(4 * (W + GAP), extract_si_path('postgresql_si.svg'), COLORS['postgresql'])
]
total_w_data = 5 * W + 4 * GAP
with open('assets/stack-data.svg', 'w', encoding='utf-8') as f:
    f.write(build_strip(data_boxes, total_w_data, H))
print("Created assets/stack-data.svg, width:", total_w_data)

