# Pyodide Test Wheels

This repository hosts WebAssembly (WASM) wheels for the [ifcopenshell](https://github.com/IfcOpenShell/IfcOpenShell) library, optimized for use with [Pyodide](https://pyodide.org/).

## Purpose

The purpose of this repository is to provide a centralized, publicly accessible source for ifcopenshell wheels, allowing users to install them via URL without needing to host the files themselves.

## Available Wheels

The repository contains several versions of ifcopenshell wheels compiled for Emscripten/WASM. An auto-generated index of available wheels is available at: [https://andrej730.github.io/pyodide-test/](https://andrej730.github.io/pyodide-test/)

## Installation in Pyodide

To install a wheel in Pyodide:

```python
import micropip
await micropip.install("https://andrej730.github.io/pyodide-test/ifcopenshell-0.8.3+34a1bc6-cp313-cp313-emscripten_4_0_9_wasm32.whl")
```

Replace the URL with the desired wheel filename from the index.

## Alternatives Considered

Other hosting options were considered:
- Raw files from GitHub repository commits: Do not serve proper CORS headers.
- Files in GitHub Releases: Do not serve proper CORS headers.

GitHub Pages was chosen as it automatically includes Access-Control-Allow-Origin: * headers, enabling cross-origin requests required for Pyodide installations.