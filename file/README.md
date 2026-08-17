# `file/` — publication metadata for the source CEG

This directory contains the literature metadata used to build the Cognitive Evidence Graph (CEG) that the BFGA framework walks.

The original content is **two Microsoft Excel 97-2003 (.xls) workbooks**:

- `PHM case metadata_part1.xls` — first half of the 70-test-case publication metadata.
- `PHM case metadata_part2.xls` — second half of the 70-test-case publication metadata.

Each row corresponds to one source publication and contains the same fields present in `papers[]` of `data/CEG data/CEG data for 2027cases.json` (paper title, year, source, cite count, algorithm hyperparameters, training config, performance metrics, `case_id`).

The `.xls` files are **not** in this repository because the underlying source publications are closed-source and embedding the metadata here would create an IP issue. The 70-case metadata is already released in JSON form under `data/BFGA test data under <scenario>/70case_*_description.json`, which is what the BFGA inference code consumes.

## What to do if you need the original spreadsheets

If you are the author or have explicit permission from the rightsholders, place the two `.xls` files in this directory and they will be tracked by Git. The BFGA inference code does not read them — they are provenance records only.
