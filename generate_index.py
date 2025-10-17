#!/usr/bin/env python3

import os
import glob

# Generate index.html in root listing all .whl files

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

# Find all .whl files in the repo, sorted descending
whl_files = sorted(glob.glob('**/*.whl', recursive=True), reverse=True)

for whl_file in whl_files:
    filename = os.path.basename(whl_file)
    # Since index.html is in root, link to filename
    html_content += f'        <li><a href="{filename}">{filename}</a></li>\n'

html_content += '''    </ul>
</body>
</html>
'''

with open('index.html', 'w') as f:
    f.write(html_content)