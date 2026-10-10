import os

# Pill items for Track 1 (Cyan/Blue #3b8ae6 theme)
track1_items = [
    "Python", "PyTorch", "C++", "C", "TypeScript", "JavaScript",
    "Deep Learning", "Transformers", "LLMs", "Multi-Task Learning",
    "LangChain", "LlamaIndex", "FastAPI", "Docker", "React",
    "Node.js", "Express", "SQL", "PostgreSQL", "Linux", "Git"
]

# Pill items for Track 2 (Emerald/Teal #34d399 theme)
track2_items = [
    "Machine Learning", "Reinforcement Learning", "Graph Neural Networks",
    "Computer Vision", "Medical Imaging", "Hugging Face", "Weights & Biases",
    "MLflow", "ONNX Runtime", "Vector Databases", "RAG Systems", "Prompt Engineering",
    "scikit-learn", "OpenCV", "NumPy", "Pandas", "Power BI", "Data Cleaning",
    "Fine-Tuning (LoRA)", "Streamlit"
]

def render_track(items, y, color, speed, reverse=False):
    pills = []
    curr_x = 0
    gap = 12
    for item in items:
        text_len = len(item)
        width = max(55, text_len * 9 + 26)
        pills.append((curr_x, width, item))
        curr_x += width + gap
    
    total_w = curr_x
    
    def make_loop(offset_x):
        res = []
        for x, w, text in pills:
            px = x + offset_x
            escaped_text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            res.append(f'<rect x="{px}" y="{y}" width="{w}" height="34" rx="17" fill="{color}" fill-opacity=".12" stroke="{color}" stroke-opacity=".55"/>')
            res.append(f'<text x="{px + w/2}" y="{y + 22}" text-anchor="middle" font-family="\'SF Mono\',\'Fira Code\',Consolas,\'Liberation Mono\',monospace" font-size="13.5" fill="#eaf1fb">{escaped_text}</text>')
        return "".join(res)
    
    inner_g = make_loop(0) + f'<g transform="translate({total_w},0)">{make_loop(0)}</g>' + f'<g transform="translate({total_w*2},0)">{make_loop(0)}</g>'
    
    if reverse:
        anim = f'<animateTransform attributeName="transform" type="translate" from="-{total_w} 0" to="0 0" dur="{speed}s" repeatCount="indefinite"/>'
    else:
        anim = f'<animateTransform attributeName="transform" type="translate" from="0 0" to="-{total_w} 0" dur="{speed}s" repeatCount="indefinite"/>'
        
    return f'<g>{anim}{inner_g}</g>'

track1_svg = render_track(track1_items, 16, "#3b8ae6", 55, reverse=False)
track2_svg = render_track(track2_items, 66, "#34d399", 70, reverse=True)

# Build bulletproof SVG with clipPath (100% supported everywhere) and edge fade gradient overlays
svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1000" height="130" viewBox="0 0 1000 130" role="img" aria-label="Skills marquee: AI, Deep Learning, Transformers, LLMs, AI Engineering, ML, Data Analytics and MLOps tools">
<defs>
<clipPath id="cpm">
<rect width="1000" height="130" rx="18"/>
</clipPath>
<linearGradient id="fade-l" x1="0" y1="0" x2="1" y2="0">
<stop offset="0" stop-color="#0e1a31" stop-opacity="1"/>
<stop offset="1" stop-color="#0e1a31" stop-opacity="0"/>
</linearGradient>
<linearGradient id="fade-r" x1="0" y1="0" x2="1" y2="0">
<stop offset="0" stop-color="#0e1a31" stop-opacity="0"/>
<stop offset="1" stop-color="#0e1a31" stop-opacity="1"/>
</linearGradient>
</defs>
<rect width="1000" height="130" rx="18" fill="#0e1a31"/>
<g clip-path="url(#cpm)">
{track1_svg}
{track2_svg}
<!-- Smooth edge fades -->
<rect x="0" y="0" width="80" height="130" fill="url(#fade-l)"/>
<rect x="920" y="0" width="80" height="130" fill="url(#fade-r)"/>
</g>
<rect x=".75" y=".75" width="998.5" height="128.5" rx="17.5" fill="none" stroke="#223a61" stroke-width="1.5"/>
</svg>'''

# Save to both marquee.svg and skills-marquee.svg
for out_path in ['assets/skills-marquee.svg', 'assets/marquee.svg']:
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Generated {out_path} successfully!")
