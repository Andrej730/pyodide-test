#!/bin/bash

# Generate index.html in docs/ listing all .whl files

mkdir -p docs

cat > docs/index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pyodide Test Wheels</title>
</head>
<body>
    <h1>Available Wheels</h1>
    <ul>
EOF

find . -name "*.whl" -type f | while read -r file; do
    filename=$(basename "$file")
    echo "        <li><a href=\"../$filename\">$filename</a></li>" >> docs/index.html
done

cat >> docs/index.html << 'EOF'
    </ul>
</body>
</html>
EOF