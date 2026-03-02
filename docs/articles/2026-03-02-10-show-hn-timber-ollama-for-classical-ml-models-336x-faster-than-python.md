# Show HN: Timber – Ollama for classical ML models, 336x faster than Python

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 160
- **Published (UTC):** 2026-03-02 00:57
- **Original:** https://github.com/kossisoroyce/timber

## Summary

Ollama for classical ML models. Timber compiles trained tree-based models (XGBoost, LightGBM, scikit-learn, CatBoost, ONNX) into optimized native C and serves them over a local HTTP API. - No Python runtime in the inference hot path - Native latency (microseconds) - One command to load, one command to serve 📚 Docs: https://kossisoroyce.github.io/timber/ Timber is built for teams that need fast, predictable, portable inference: - Fraud/risk teams running classical models in low-latency transaction paths - Edge/IoT teams deploying models to gateways and embedded devices - Regulated industries (finance, healthcare, automotive) needing deterministic artifacts and audit trails - Platform/infra teams replacing Python model-serving overhead with native binaries pip install timber-compiler # Load any supported model (auto-detected) timber load model.json --name fraud-detector # Serve it (Ollama-style workflow) timber serve fraud-detector curl http://localhost:11434/api/predict \ -d '{"model": "fraud-detector", "inputs": [[1.0, 2.0, 3.0, ...]]}' | Format | Framework | File Types | |---|---|---| | XGBoost JSON | XGBoost | .json | | LightGBM text | LightGBM | .txt , .model , .lgb | | scikit-learn pickle | scikit-learn | .pkl , .pickle | | ONNX ML opset (TreeEnsemble) | ONNX | .onnx | | CatBoost JSON | CatBoost | .json | The 336× claim is measured against Python XGBoost single-sample inference.

## Key Takeaways

- - Hardware: Apple M2 Pro, 16 GB RAM, macOS (recorded by script) - Model: XGBoost binary classifier, 50 trees, max depth 4, 30 features - Dataset: breast_cancer (sklearn) - Warmup: 1,000 iterations - Timed: 10,000 single-sample predictions - Metric: in-process latency (not HTTP/network round-trip) - Baseline: Python XGBoost ( booster.predict ) See benchmarks/ for: run_benchmarks.py (Timber vs Python XGBoost + optional ONNX Runtime/Treelite/lleaves)system_info.py (hardware/software metadata)render_table.py (markdown table output) Run: python benchmarks/run_benchmarks.py --output benchmarks/results.json python benchmarks/render_table.py --input benchmarks/results.json | Runtime | Runtime deps | Typical artifact size | Latency profile | Notes | |---|---|---|---|---| | Timber | None (generated C99) | ~48 KB (example model) | ~2 µs native call | Strong fit for edge/embedded and deterministic deployments | | Python (xgboost/sklearn serving) | Python + framework stack | 50–200+ MB process footprint | 100s of µs to ms | Easy dev loop, high runtime overhead | | ONNX Runtime | ONNX Runtime libs | MBs to 10s of MBs | usually low 100s of µs | Broad model ecosystem, larger runtime | | Treelite Runtime | Treelite runtime + compiled artifact | MB-scale runtime + model lib | low-latency when compiled | Great for GBDTs; separate compile/runtime flow | | lleaves | Python package + LightGBM text model | Python runtime + compiled code | lower than pure Python | LightGBM-focused | - ONNX support is currently focused on TreeEnsembleClassifier/Regressor operators.
- - CatBoost support expects JSON exports (not native binary formats).
- - scikit-learn parser supports major tree estimators and pipelines; uncommon/custom estimator wrappers may fail.

---
_Auto-generated daily digest entry._
