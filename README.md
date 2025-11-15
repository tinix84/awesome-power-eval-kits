# Awesome Power Eval Kits

A curated collection of power electronics evaluation kits, student projects, and academic paper reproductions—with simulations, measurements, and digital twin models.

## 📋 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Three Content Types](#three-content-types)
- [Getting Started](#getting-started)
- [Workflow for Students](#workflow-for-students)
- [Kit Catalog](#kit-catalog)
- [Contributing](#contributing)

## Overview

This repository is a **learning museum** for power electronics:
- **Kits**: Reverse-engineering of real evaluation boards (hardware-based)
- **Projects**: Original student designs and proposals (concept/simulation-based)
- **Articles**: Reproduction of published IEEE/journal papers

**Educational Goals:**
- Build digital twin models in PLECS/LTspice/MATLAB
- Quantify currents, voltages, losses, and component stresses
- Compare simulation results with vendor data or published results
- Perform spectral analysis, efficiency measurements, and margin checks
- Propose evidence-based design improvements

## Repository Structure

```
awesome-power-eval-kits/
├─ README.md                        # This file
├─ kits/                            # Real eval boards (vendor hardware)
│  ├─ ti_ucc28740evm_525/
│     ├─ README.md                  # Board specs, datasheet links
│     ├─  docs/                    # Additional documentation (optional)
│     │  ├─ schematic.pdf              # (optional, if distributable)
│     │  ├─ bom.csv                    # Bill of materials
│     │  ├─ efficiency_curve.png       # Vendor plots
│     └─ 20250115_group_alpha/      # Student analysis (YYYYMMDD_name)
│        ├─ README.md
│        ├─ sim/
│        ├─ meas/
│        ├─ analysis/
│        └─ report/
├─ projects/                        # Student original designs/proposals
│  ├─ 20250120_bidirectional_dcdc_sic/  # YYYYMMDD_project_name
│  │  ├─ README.md                  # Project summary
│  │  ├─ sim/                       # Simulation files
│  │  ├─ analysis/                  # Scripts, Jupyter notebooks
│  │  └─ report/                    # Final PDF/Markdown report
│  └─ 20250210_llc_resonant_charger/
│     └─ README.md
├─ articles/                        # IEEE/journal paper reproductions
│  ├─ 20250115_smith2023_gan_totem_pfc/  # YYYYMMDD_author_year_topic
│  │  ├─ README.md                  # Paper metadata, reproduction scope
│  │  ├─ paper.pdf                  # (if allowed) or link
│  │  ├─ sim/                       # Replicated model
│  │  ├─ plots/                     # Reproduced figures
│  │  └─ report/                    # Comparison & analysis
│  └─ 20250201_lee2022_totem_pfc/
│     └─ README.md
├─ templates/                       # Starter templates
│  ├─ STUDENT_CHECKLIST.md          # Analysis checklist (for kits)
│  ├─ KIT_README_TEMPLATE.md        # Template for kits/
│  ├─ PROJECT_README_TEMPLATE.md    # Template for projects/
│  ├─ ARTICLE_README_TEMPLATE.md    # Template for articles/
│  └─ REPORT_TEMPLATE.md            # General report structure
└─ .github/
   └─ PULL_REQUEST_TEMPLATE.md
```

## Three Content Types

### 1. `kits/` – Real Evaluation Boards

**What:** Reverse-engineering of **existing vendor hardware** (TI, ST, Infineon, etc.).

**Structure:** Each kit folder uses the same template as the board itself:
- `README.md` with specs, datasheet links, component list
- Optionally: schematics, BOM, efficiency plots (stored locally or linked)
- Student analysis folders **inside the kit folder** with naming: `YYYYMMDD_groupname/`
  - Example: `kits/ti_ucc28740evm_525/20250115_group_alpha/`

**Template:** [`templates/KIT_README_TEMPLATE.md`](templates/KIT_README_TEMPLATE.md)

### 2. `projects/` – Student Original Designs

**What:** **Student-proposed converters** not tied to a specific eval board. These are original designs, thesis projects, or hypothetical topologies.

**Naming Convention:** `YYYYMMDD_project_description/`
- Example: `projects/20250120_bidirectional_dcdc_sic/`
- Example: `projects/20250315_llc_resonant_ev_charger/`

**Examples:**
- Bidirectional DC/DC with SiC for energy storage
- Custom LLC resonant charger for EVs
- Multi-phase buck for server VRM

**Template:** [`templates/PROJECT_README_TEMPLATE.md`](templates/PROJECT_README_TEMPLATE.md)

### 3. `articles/` – Academic Paper Reproductions

**What:** **Reproduction of published work** from IEEE, APEC, ECCE, journals, etc. Goal: replicate simulations, validate claims, understand techniques.

**Naming Convention:** `YYYYMMDD_firstauthor_year_topic/`
- Example: `articles/20250115_smith_2023_gan_totem_pfc/`
- Example: `articles/20250201_lee_2022_llc_zerocurrent/`

**Template:** [`templates/ARTICLE_README_TEMPLATE.md`](templates/ARTICLE_README_TEMPLATE.md)

---

## Getting Started

### For Instructors

**Adding content:**
1. **Kits:** Create folder in `kits/` using [`KIT_README_TEMPLATE.md`](templates/KIT_README_TEMPLATE.md)
2. **Projects:** Direct students to `projects/YYYY/` with appropriate template
3. **Articles:** Use [`ARTICLE_README_TEMPLATE.md`](templates/ARTICLE_README_TEMPLATE.md) for paper reproductions

**Managing submissions:** Review PRs, check completeness via checklist, merge to main, apply labels.

### For Students

Pick your activity type and follow the corresponding workflow below.

## Workflow for Students

We use a **fork-based workflow**. All work happens in your fork; submit a PR when complete.

### Common Steps (All Types)

1. **Fork** this repository (click Fork button on GitHub)
2. **Clone** your fork:
   ```bash
   git clone https://github.com/YOUR-USERNAME/awesome-power-eval-kits.git
   cd awesome-power-eval-kits
   ```

### Type A: Analyzing a Real Eval Board (`kits/`)

3. Navigate to the kit folder (e.g., `kits/ti_ucc28740evm_525/`)
4. Read the kit `README.md` and linked datasheets
5. Create your analysis folder **inside the kit folder** using `YYYYMMDD_groupname`:
   ```bash
   cd kits/ti_ucc28740evm_525
   mkdir 20250115_group_alpha
   cd 20250115_group_alpha
   ```
6. Copy templates:
   ```bash
   cp ../../../templates/PROJECT_README_TEMPLATE.md README.md
   ```
7. Build your simulation model, follow [`STUDENT_CHECKLIST.md`](templates/STUDENT_CHECKLIST.md)
8. Structure your work:
   ```
   20250115_group_alpha/
   ├─ README.md
   ├─ sim/          # PLECS, LTspice
   ├─ meas/         # CSV, scope data
   ├─ analysis/     # Scripts
   └─ report/       # Final PDF/Markdown
   ```

### Type B: Original Student Project (`projects/`)

3. Create a project folder with `YYYYMMDD_description` naming:
   ```bash
   cd projects
   mkdir 20250120_bidirectional_dcdc_sic
   cd 20250120_bidirectional_dcdc_sic
   ```
4. Copy template:
   ```bash
   cp ../../templates/PROJECT_README_TEMPLATE.md README.md
   ```
5. Develop your design, simulation, and analysis

### Type C: Paper Reproduction (`articles/`)

3. Create article folder using `YYYYMMDD_author_year_topic` naming:
   ```bash
   cd articles
   mkdir 20250115_smith_2023_gan_totem_pfc
   cd 20250115_smith_2023_gan_totem_pfc
   ```
4. Copy template:
   ```bash
   cp ../../templates/ARTICLE_README_TEMPLATE.md README.md
   ```
5. Reproduce simulations/measurements from the paper
6. Document discrepancies and lessons learned

### Final Steps (All Types)

9. **Commit and push:**
   ```bash
   git add .
   git commit -m "Add [kit/project/article]: YYYYMMDD_description"
   git push origin main
   ```

10. **Open Pull Request:**
    - Go to your fork on GitHub
    - Click **Pull Request** → **New Pull Request**
    - Base: `tinix84/awesome-power-eval-kits` (main)
    - Head: `YOUR-USERNAME/awesome-power-eval-kits` (main)
    - Fill PR template, add labels: `kit-xxx` / `project` / `article-reproduction`

**Important:**
- No large binaries (>10 MB). Use compressed images (PNG/JPG).
- Export scope data as CSV.
- Follow the appropriate checklist/template.

---

## Kit Catalog

Browse available evaluation boards in `kits/`. See [kits/kits_catalog.md](kits/kits_catalog.md) for the complete table.

### Easy (Entry-Level)

Non-isolated DC/DC and low-power offline boards.

- **TPS62932EVM** · buck synchronous, 3.8-30 V → 3.3 / 5 V @ ~2 A, ~10 W
- **TPS563212EVM** · buck synchronous, 4.2-18 V → 3.3 V @ 3 A, ~10 W
- **TPS6213xEVM** · buck synchronous, 3-17 V → 3.3 / 5 V @ 3-4 A, ~15 W
- **STEVAL-VP12201F** · flyback, 85-265 VAC → 12 V @ 5 W, 5 W
- **STEVAL-ISA201V1** · buck (l5987), up to 24-25 V → 5 V @ 3 A, ~15 W
- **NCP1060FLBKGEVB** · flyback, 85-265 VAC → 12 V @ 0.6 A, ~7 W
- **NCP1076FLBKGEVB** · flyback, 85-265 VAC → 12 V @ 1.2 A, ~18 W
- **BD7F100EFJ-EVK-001** · flyback, 24 V DC → 5 V @ 0.8 A, 4 W
- **2190** · buck-boost, 3-12 V → 5 V USB, 2.5-5 W
- **EVAL_5BR2280BZ_700MA1** · high-voltage buck (non-isolated), 85-264 VAC input (for internals) -> DC bus high voltage? (Refer doc) → 15 V @ 0.7 A (~10.5 W) typical, ~10 W
- **DC2781A (LT8316 non-isolated buck demo)** · non-isolated buck (quasi-resonant boundary mode), 19-600 V DC input range → 12 V @ up to 200 mA, ~2.4 W
- **BM2P141X-EVK-001 (non-isolation buck converter)** · non-isolated buck (pwm current mode), 12-15 V (drain max 650 V but EVK is low power) → 14 V (10 W output), ~10 W

### Medium

Intermediate power, more complex control or wide-VIN.

- **[TPS23753AEVM-004](kits/ti_tps23753aevm_004/)** · poe flyback, 37-57 V (PoE) → 3.3 / 5 / 12 V (configurable), ~10 W
- **UCC28740EVM-525** · flyback dcm, 85-265 VAC → 5 V @ 2.1 A, 10 W
- **LM5118EVAL** · buck-boost, 5-75 V → 12 V @ 3 A, ~36 W
- **LM5176EVM-HP** · buck-boost synchronous, 6-36 V → 12 V @ 12 A, ~144 W
- **LM5576EVAL** · buck, 6-75 V → 5 V @ 3 A, ~15 W
- **EVLSTACF01-65WU** · active-clamp flyback (acf), 90-264 VAC → 5-20 V (USB-PD), 65 W
- **STEVAL-QUADV01** · multi-output buck + ldo, 3.5-38 / 60 V → multiple rails (A, B, C, LDO), ~10-20 W
- **EVAL_5BR2280BZ_700MA1** · high-voltage buck, 85-264 VAC → 15 V @ 0.7 A, 10.5 W
- **Si34061-KIT** · poe flyback, PoE 37-57 V → 12 V, ~25-30 W
- **EVQ3369-R-01A** · boost led driver, 4.5-36 V → LED strings (multi-channel), ~10-20 W
- **LM5146-Q1-EVM12V** · synchronous buck, 15-85 V → 12 V (adjustable 8-15 V), ~12 V x up to ~8 A = ~96 W
- **TPS55287-Q1EVM-085** · buck-boost synchronous, 3-36 V → 0.8-22 V (programmable), Up to 2 A output current (~ up to ~44 W at 22 V)

### Advanced / High Power

kW-class boards with complex topologies (LLC, PSFB, bidirectional, PFC+LLC).

- **STEVAL-DPSLLCK1** · llc full-bridge, DC bus 350-400 V → 3 kW @ low-V, 3000 W
- **EVAL_3KW_50V_PSU** · pfc + llc, 178-275 VAC → 50 V DC, 3000 W
- **REF-1KW-PSU-5G-SIC** · totem-pole pfc + hb-llc, mains AC → 48-54 V, 1000 W
- **EVAL_1K6W_PSU_CFD7_QD** · pfc + llc, mains AC → 12 / 48 V, 1600 W
- **EVAL_3K3W_BIDI_PSFB** · bidirectional psfb, HV bus <-> 54 V → Bidirectional, 3300 W
- **LMG1210EVM-012** · half-bridge gan stage, up to 300 V DC bus → configurable, 10-100+ W (by design)

> **Note:** Not all kits have folders yet. Contributions welcome! Use [`KIT_README_TEMPLATE.md`](templates/KIT_README_TEMPLATE.md) to add one.


---

## Contributing

### Content Types

1. **Kits (`kits/`)** – Add new eval boards with docs and specs
2. **Projects (`projects/`)** – Submit original student designs
3. **Articles (`articles/`)** – Reproduce published papers

### Submission Guidelines

**Before submitting a PR:**
- [ ] Use the appropriate template (`KIT_README_TEMPLATE.md`, `PROJECT_README_TEMPLATE.md`, or `ARTICLE_README_TEMPLATE.md`)
- [ ] Complete all required sections (no placeholder `<text>` left)
- [ ] Follow checklist: [`STUDENT_CHECKLIST.md`](templates/STUDENT_CHECKLIST.md) for kits
- [ ] Simulation model included and functional
- [ ] No large binaries (>10 MB); use links or compressed files
- [ ] Analysis/report section complete with conclusions

**PR Process:**
1. Fork → create branch → commit changes
2. Open PR to `tinix84/awesome-power-eval-kits:main`
3. Fill out PR template
4. Add labels:
   - Type: `kit`, `project`, `article-reproduction`
   - Kit (if applicable): `kit-ti-ucc28740`, `kit-st-evlstacf01`
   - Topic: `topic-efficiency`, `topic-magnetics`, `topic-emi`

**Rejection Criteria:**

PRs lacking the following will be politely rejected:
- Working simulation model
- Basic loss breakdown or efficiency analysis
- Written conclusions (even if brief)

### Improving Templates

Found a better way to structure reports? Submit a PR to `templates/` with explanation.

---

## License

This repository is for **educational purposes**. 

- Student submissions: work of respective authors
- Vendor documentation: property of manufacturers (linked for reference)
- Reproduced papers: cite original authors and DOI

---

**Maintainer:** [tinix84](https://github.com/tinix84)  
**Questions?** Open an issue or contact the course instructor.
