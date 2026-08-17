# BFGA-PHM-Recommendation

Reference implementation of the **Belief-Feedback Graph Agent (BFGA)** framework for PHM algorithm recommendation. Companion open-source release for the SCI paper by Xuanyuan Su.

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](requirements.txt)

---

## What is here

- `code/` — Python source code for the BFGA reasoning loop and the CEG construction pipeline.
- `data/` — Released dataset and result tables (see [docs/data_description.md](docs/data_description.md)).
- `file/` — Publication metadata for the source CEG (see [file/README.md](file/README.md)).
- `docs/` — Documentation.
- `UPLOAD_TO_GITHUB.md` — How to publish this repository to GitHub.

This repository is a **reference release**. It is not packaged as a runnable end-to-end CLI; the BFGA inference modules are intended to be imported and driven from your own code. See [docs/installation.md](docs/installation.md) for installation and the module hierarchy.

---

## Repository layout

```
BFGA-PHM-Recommendation/
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── requirements.txt
├── CITATION.cff
├── UPLOAD_TO_GITHUB.md
├── code/
│   ├── 01-cognitive evidence graph modeling/
│   │   ├── 01_CEG schema/
│   │   │   ├── edge schema for llm/
│   │   │   └── node schema for llm/      # 5 MDs: 00 … 15-20 (canonical English terminology)
│   │   └── 02_CEG modeling guided by three topologies/
│   │       ├── 021_node extraction_disambiguation_indcution/
│   │       ├── 022_edge extraction_disambiguation_indcution/
│   │       └── 023_graph aggregation/
│   └── 02-BFGA-driven PHM algorithm recommendation/
│       └── BFGA_main_code/
│           ├── v7_modules/                # m00_config … m09_recommend
│           ├── Shared_module_BFGA_for_algorithm_level_task.py
│           └── Shared_module_BFGA_for_paradigm_level_task.py
├── data/
│   ├── CEG data/
│   ├── BFGA test data under Normal test/
│   ├── BFGA test data under Missing 1 test/
│   ├── BFGA test data under Missing 3 test/
│   ├── BFGA test data under Missing 5 test/
│   └── Recommendation consistency results under 4 tests/
├── file/
│   └── README.md                          # closed-source publication metadata
└── docs/
    ├── data_description.md
    ├── ceg_schema.md
    ├── installation.md
    └── SECURITY.md
```

---

## License

Apache License 2.0 — see [LICENSE](LICENSE).
