#!/usr/bin/env python3

import os
import glob

# Generate index.html in docs/ listing all .whl files

os.makedirs('docs', exist_ok=True)

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pyodide Test Wheels</title>
</head>
<body>
    <h1>Available Wheels</h1>
    <ul>
'''

# Find all .whl files in the repo
whl_files = glob.glob('**/*.whl', recursive=True)

for whl_file in whl_files:
    filename = os.path.basename(whl_file)
    # Since index.html is in docs/, link to ../filename
    html_content += f'        <li><a href="../{filename}">{filename}</a></li>\n'

html_content += '''    </ul>
</body>
</html>
'''

with open('docs/index.html', 'w') as f:
    f.write(html_content)