import os

# 1. sub-academic.svg
sub_academic_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="34" viewBox="0 0 1000 34" role="img" aria-label="ACADEMIC PROJECTS (BIG DATA · ML · BASES DE DONNÉES)">
<circle cx="8" cy="17" r="4" fill="#a78bfa"><animate attributeName="opacity" values="1;.25;1" dur="2s" repeatCount="indefinite"/></circle>
<text x="24" y="22" font-family="'SF Mono','Fira Code',Consolas,'Liberation Mono',monospace" font-size="13" letter-spacing="3" fill="#a78bfa">ACADEMIC PROJECTS (BIG DATA · ML · BASES DE DONNÉES)</text>
<path d="M510 17 H996" stroke="#223a61" stroke-width="1.5" stroke-dasharray="2 6" stroke-linecap="round"/>
</svg>'''

with open('assets/sub-academic.svg', 'w', encoding='utf-8') as f:
    f.write(sub_academic_svg)

# 2. c-academic-s1.svg (490x200)
c_academic_s1 = '''<svg xmlns="http://www.w3.org/2000/svg" width="490" height="200" viewBox="0 0 490 200" role="img" aria-label="IASD University Labs S1 - Big Data, ML, Base de Données">
<defs>
<linearGradient id="bg1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#141a33"/><stop offset="1" stop-color="#0a1024"/></linearGradient>
<radialGradient id="gl1" cx="0" cy="0" r="1"><stop offset="0" stop-color="#a78bfa" stop-opacity=".32"/><stop offset="1" stop-color="#a78bfa" stop-opacity="0"/></radialGradient>
<linearGradient id="sw1" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".08"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<pattern id="dots1" width="16" height="16" patternUnits="userSpaceOnUse"><circle cx="1.5" cy="1.5" r="1" fill="#202a4a"/></pattern>
<clipPath id="cl1"><rect width="490" height="200" rx="16"/></clipPath>
</defs>
<g clip-path="url(#cl1)">
<rect width="490" height="200" fill="url(#bg1)"/>
<rect width="490" height="200" fill="url(#dots1)" opacity=".7"/>
<ellipse cx="450" cy="200" rx="230" ry="130" fill="url(#gl1)"><animate attributeName="rx" values="200;270;200" dur="7s" repeatCount="indefinite"/></ellipse>
<rect x="0" y="0" width="490" height="3" fill="#a78bfa" opacity=".9"/>
<rect x="-200" y="0" width="200" height="200" fill="url(#sw1)" transform="skewX(-20)"><animate attributeName="x" values="-200;790" dur="8s" begin="0.5s" repeatCount="indefinite"/></rect>
</g>
<rect x=".75" y=".75" width="488.5" height="198.5" rx="15.5" fill="none" stroke="#a78bfa" stroke-opacity=".35" stroke-width="1.5"/>
<text x="34" y="40" font-family="'SF Mono','Fira Code',Consolas,'Liberation Mono',monospace" font-size="11.5" letter-spacing="2" fill="#a78bfa">ACADEMIC LABS · S1</text>
<text x="34" y="72" font-family="'Segoe UI',-apple-system,Helvetica,Arial,sans-serif" font-size="22" font-weight="800" fill="#eaf1fb">Curriculum Labs S1</text>
<rect x="385" y="16" width="81" height="22" rx="11" fill="#a78bfa" fill-opacity=".15" stroke="#a78bfa" stroke-opacity=".6"/>
<circle cx="399" cy="27" r="3.6" fill="#a78bfa"><animate attributeName="opacity" values="1;.2;1" dur="1.6s" repeatCount="indefinite"/></circle>
<text x="408" y="31" font-family="'SF Mono','Fira Code',Consolas,'Liberation Mono',monospace" font-size="10.5" letter-spacing="1.2" fill="#a78bfa">S1 REPO</text>
<text x="34" y="100" font-family="'Segoe UI',-apple-system,Helvetica,Arial,sans-serif" font-size="14" fill="#8aa0bd">Comprehensive university research labs across Big Data,</text>
<text x="34" y="121" font-family="'Segoe UI',-apple-system,Helvetica,Arial,sans-serif" font-size="14" fill="#8aa0bd">Machine Learning algorithms, and Bases de Données</text>
<text x="34" y="142" font-family="'Segoe UI',-apple-system,Helvetica,Arial,sans-serif" font-size="14" fill="#8aa0bd">(SQL/NoSQL relational &amp; distributed storage engines).</text>
<rect x="34" y="154" width="80" height="24" rx="12" fill="#a78bfa" fill-opacity=".12" stroke="#a78bfa" stroke-opacity=".5"/>
<text x="74" y="170" text-anchor="middle" font-family="'SF Mono','Fira Code',Consolas,'Liberation Mono',monospace" font-size="11" fill="#eaf1fb">Big Data</text>
<rect x="122" y="154" width="130" height="24" rx="12" fill="#a78bfa" fill-opacity=".12" stroke="#a78bfa" stroke-opacity=".5"/>
<text x="187" y="170" text-anchor="middle" font-family="'SF Mono','Fira Code',Consolas,'Liberation Mono',monospace" font-size="11" fill="#eaf1fb">Machine Learning</text>
<rect x="260" y="154" width="135" height="24" rx="12" fill="#a78bfa" fill-opacity=".12" stroke="#a78bfa" stroke-opacity=".5"/>
<text x="327" y="170" text-anchor="middle" font-family="'SF Mono','Fira Code',Consolas,'Liberation Mono',monospace" font-size="11" fill="#eaf1fb">Bases de Données</text>
</svg>'''

with open('assets/c-academic-s1.svg', 'w', encoding='utf-8') as f:
    f.write(c_academic_s1)

# 3. c-academic-s2.svg (490x200)
c_academic_s2 = '''<svg xmlns="http://www.w3.org/2000/svg" width="490" height="200" viewBox="0 0 490 200" role="img" aria-label="IASD University Labs S2 - Deep Learning, Computer Vision">
<defs>
<linearGradient id="bg2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#10203a"/><stop offset="1" stop-color="#091326"/></linearGradient>
<radialGradient id="gl2" cx="0" cy="0" r="1"><stop offset="0" stop-color="#38bdf8" stop-opacity=".32"/><stop offset="1" stop-color="#38bdf8" stop-opacity="0"/></radialGradient>
<linearGradient id="sw2" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".08"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<pattern id="dots2" width="16" height="16" patternUnits="userSpaceOnUse"><circle cx="1.5" cy="1.5" r="1" fill="#1b2e50"/></pattern>
<clipPath id="cl2"><rect width="490" height="200" rx="16"/></clipPath>
</defs>
<g clip-path="url(#cl2)">
<rect width="490" height="200" fill="url(#bg2)"/>
<rect width="490" height="200" fill="url(#dots2)" opacity=".7"/>
<ellipse cx="450" cy="200" rx="230" ry="130" fill="url(#gl2)"><animate attributeName="rx" values="200;270;200" dur="7s" repeatCount="indefinite"/></ellipse>
<rect x="0" y="0" width="490" height="3" fill="#38bdf8" opacity=".9"/>
<rect x="-200" y="0" width="200" height="200" fill="url(#sw2)" transform="skewX(-20)"><animate attributeName="x" values="-200;790" dur="8s" begin="1.8s" repeatCount="indefinite"/></rect>
</g>
<rect x=".75" y=".75" width="488.5" height="198.5" rx="15.5" fill="none" stroke="#38bdf8" stroke-opacity=".35" stroke-width="1.5"/>
<text x="34" y="40" font-family="'SF Mono','Fira Code',Consolas,'Liberation Mono',monospace" font-size="11.5" letter-spacing="2" fill="#38bdf8">ACADEMIC LABS · S2</text>
<text x="34" y="72" font-family="'Segoe UI',-apple-system,Helvetica,Arial,sans-serif" font-size="22" font-weight="800" fill="#eaf1fb">Curriculum Labs S2</text>
<rect x="385" y="16" width="81" height="22" rx="11" fill="#38bdf8" fill-opacity=".15" stroke="#38bdf8" stroke-opacity=".6"/>
<circle cx="399" cy="27" r="3.6" fill="#38bdf8"><animate attributeName="opacity" values="1;.2;1" dur="1.6s" repeatCount="indefinite"/></circle>
<text x="408" y="31" font-family="'SF Mono','Fira Code',Consolas,'Liberation Mono',monospace" font-size="10.5" letter-spacing="1.2" fill="#38bdf8">S2 REPO</text>
<text x="34" y="100" font-family="'Segoe UI',-apple-system,Helvetica,Arial,sans-serif" font-size="14" fill="#8aa0bd">Advanced M.Sc. laboratory benchmarks in Deep Learning,</text>
<text x="34" y="121" font-family="'Segoe UI',-apple-system,Helvetica,Arial,sans-serif" font-size="14" fill="#8aa0bd">Computer Vision pipelines, neural architectures,</text>
<text x="34" y="142" font-family="'Segoe UI',-apple-system,Helvetica,Arial,sans-serif" font-size="14" fill="#8aa0bd">and convex &amp; gradient-based numerical optimization.</text>
<rect x="34" y="154" width="110" height="24" rx="12" fill="#38bdf8" fill-opacity=".12" stroke="#38bdf8" stroke-opacity=".5"/>
<text x="89" y="170" text-anchor="middle" font-family="'SF Mono','Fira Code',Consolas,'Liberation Mono',monospace" font-size="11" fill="#eaf1fb">Deep Learning</text>
<rect x="152" y="154" width="125" height="24" rx="12" fill="#38bdf8" fill-opacity=".12" stroke="#38bdf8" stroke-opacity=".5"/>
<text x="214" y="170" text-anchor="middle" font-family="'SF Mono','Fira Code',Consolas,'Liberation Mono',monospace" font-size="11" fill="#eaf1fb">Computer Vision</text>
<rect x="285" y="154" width="105" height="24" rx="12" fill="#38bdf8" fill-opacity=".12" stroke="#38bdf8" stroke-opacity=".5"/>
<text x="337" y="170" text-anchor="middle" font-family="'SF Mono','Fira Code',Consolas,'Liberation Mono',monospace" font-size="11" fill="#eaf1fb">Optimization</text>
</svg>'''

with open('assets/c-academic-s2.svg', 'w', encoding='utf-8') as f:
    f.write(c_academic_s2)

print("Created academic project SVGs successfully!")
