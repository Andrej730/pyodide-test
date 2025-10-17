# Pyodide Test Wheels

This repository hosts WebAssembly (WASM) wheels for the [ifcopenshell](https://github.com/IfcOpenShell/IfcOpenShell) library, optimized for use with [Pyodide](https://pyodide.org/).

## Purpose

The wheels enable installing and using ifcopenshell in Pyodide-based environments, such as web browsers, for processing Industry Foundation Classes (IFC) files without server-side computation.

## Available Wheels

The repository contains several versions of ifcopenshell wheels compiled for Emscripten/WASM. An auto-generated index of available wheels is available at: [https://andrej730.github.io/pyodide-test/](https://andrej730.github.io/pyodide-test/)

## Installation in Pyodide

To install a wheel in Pyodide:

```python
import micropip
await micropip.install("https://andrej730.github.io/pyodide-test/ifcopenshell-0.8.3+34a1bc6-cp313-cp313-emscripten_4_0_9_wasm32.whl")
```

Replace the URL with the desired wheel filename from the index.

## Source

Wheels are sourced from the [IfcOpenShell/wasm-wheels](https://github.com/IfcOpenShell/wasm-wheels) repository.

## GitHub Pages

This repository uses GitHub Pages to serve the wheels with proper CORS headers, ensuring compatibility with browser-based installations.