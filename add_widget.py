import os, glob

html_files = glob.glob('*.html')
widget_html = """
<a href="https://buymemomo.com/vabin" class="momo-widget">
  <img src="https://buymemomo.com/logo.png" alt="Buy me a momo" title="Buy me a momo">
  <span class="momo-text">Buy me a momo</span>
</a>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'momo-widget' not in content:
        content = content.replace('</body>', f'{widget_html}</body>')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
