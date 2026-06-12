# Building Disaggregation Pipeline — CoEnergy × Scalian

Prediction of individual building characteristics from aggregated block data and a precise address, for German cities (Düsseldorf, Gelsenkirchen).

## Project Overview

This pipeline predicts 10 building variables from minimal input (address + floor area):
- **Building type** (EFH, MFH, GMH, RH, HH, GHD, Industrie, Öffentlich)
- **Type of use** (Wohngebäude, Gewerbegebäude, Industriegebäude, Öffentliche Hand)
- **Construction year class** (11 periods from 1860 to 2023)
- **Initial heating system** (Gaskessel, Ölkessel, Fernwärme, el. WP, etc.)
- **Renovation state** (not_renovated, partially_renovated, renovated)
- **Heated space** (m²)
- **Initial heat demand** (kWh/year)
- **Number of apartments** (min/max)
- **Construction year**

## Architecture

The pipeline uses a **cascade ML approach** with XGBoost models:

```
Address → Geocoding → Block identification → Feature engineering
    ↓
Level 1: building_type, type_of_use, construction_year_class
    ↓
Level 2: initial_heating_system, renovation_state, NOA
    ↓
Level 3: heated_space
    ↓
Level 4: initial_heat_demand, construction_year
```

Optional LLM integration (Mistral local/cloud) for IHD prediction on residential buildings.

## Data Requirements

The following data files are required but NOT included in this repository (too large):

```
data/
└── raw/
    ├── Düsseldorf/
    │   ├── Düsseldorf_digital_twin_buildings.csv      # Individual buildings (~94K)
    │   ├── Düsseldorf_digital_twin_geo_area_aggregated.csv  # Aggregated blocks
    │   └── height/                                     # TIF height files (240 tiles)
    │       ├── ndom50_32344_5674_1_nw_2023.tif
    │       └── ...
    └── Gelsenkirchen/
        ├── Gelsenkirchen_digital_twin_buildings.csv    # Individual buildings (~44K)
        ├── Gelsenkirchen_digital_twin_geo_area_aggregated.csv
        └── height/                                     # TIF height files
            └── ...
```

Additionally required:
- `TABULA.xlsx` — IWU/TABULA reference specific heat demands

## Installation

```bash
# Clone the repository
git clone https://github.com/AlexBatisse/Use_Case_5_SCALIAN_x_COENERGY.git
# Create virtual environment
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# For local LLM (optional)
# Install Ollama: https://ollama.ai
# ollama pull mistral
```

## Configuration

1. Copy `.env.example` to `.env` and fill in your API keys (if using cloud LLMs)
2. Update `DATA_ROOT` path in the notebook to point to your data directory
3. Place the required data files in the correct directory structure

## Notebooks

- `ML_and_LLM_Pipeline.ipynb` — Main ML + LLM pipeline (XGBoost cascade, feature engineering, benchmarks)
- `LLM_Pipeline.ipynb.ipynb` — LLM pipeline (profiling, few-shot prompting, LLM benchmarks)

## Key Features

- **Automatic city detection** — `initialize_city()` auto-detects the city and loads appropriate datasets
- **TIF height extraction** — Indexed tile lookup for fast height extraction from LiDAR data
- **TABULA integration** — Professional reference consumption values with proxy mapping for non-residential types
- **Block TABULA proxy** — Weighted average consumption feature from aggregated block distributions
- **Cascade ML** — Hierarchical prediction with encoded predictions as features for downstream models
- **Production mode** — Features strictly limited to what's available without the measured dataset
- **SHAP analysis** — Feature importance analysis for each prediction variable

## Performance (Gelsenkirchen — Production mode)

| Variable | Accuracy/MAPE |
|---|---|
| building_type | 81.3% |
| type_of_use | 94.1% |
| construction_year_class | 67.7% |
| initial_heating_system | 72.6% |
| renovation_state | 52.6% |
| heated_space | MAPE 16.3% |
| initial_heat_demand | MAPE 30.0% |
| NOA | MAPE ~28% |

## GDPR Compliance

- Training uses aggregated block data + open-data features only
- No individual building data is stored or transmitted
- Local LLM option available for sensitive datasets

## 📁 Datasets

To run this project, you need to manually add the following datasets to the repository structure:

### **Folder**
- Replace the following folder with the google drive datas and it should work:
  - `data/Raw/Gelsenkirchen/`
  - `data/Raw/Düsseldorf/`

### **TABULA.xlsx**
- Place the `TABULA.xlsx` file in:
  - `data/Raw/`



