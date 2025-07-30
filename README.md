# Land-Surface-Temperature
This repository contains a Google Earth Engine (GEE) script to extract  Land Surface Temperature (LST) Day and Night averages for Nepal using MODIS Terra MOD11A1 V061 (Daily 1km LST) data. 
# MODIS MOD11A1 V061 - Land Surface Temperature (LST) Extraction for Nepal Districts (FY2023_24)

This Google Earth Engine (GEE) script computes **district-wise daily average Land Surface Temperature (LST) Day and Night** using **MOD11A1 V061** data for the **Fiscal Year 2023/24 (July 16, 2023 - July 15, 2024)**.

---

## 📂 Dataset Used:
- **MODIS/Terra MOD11A1 V061** - Daily Land Surface Temperature (LST) & Emissivity 1 km SIN Grid.
  - [Dataset Link](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD11A1)

## 📍 Region of Interest:
- **Nepal District Boundaries (77 districts)**.
  - Load your shapefile as a GEE **FeatureCollection**.

---

## 🚀 Script Overview:
1. Load Nepal District shapefile.
2. Filter MOD11A1 ImageCollection for the fiscal year.
3. Compute average **Daytime and Nighttime LST** (Kelvin to Celsius).
4. Reduce LST values to **district-wise means**.
5. Export as CSV to **Google Drive**.

---

## 📝 Instructions:
1. Upload your **Nepal District shapefile** to your GEE Assets.
2. Update the **FeatureCollection path** in line 4.
3. Copy-paste the script in [Google Earth Engine Code Editor](https://code.earthengine.google.com/).
4. Run the script.
5. Download the CSV from **Google Drive**.

---

## 📊 Output:
- Two CSV files:
  - `FY2023_24_District_LST_Day.csv`
  - `FY2023_24_District_LST_Night.csv`

Each file contains:
| District Name | Mean LST (°C) | Fiscal Year |

---

## 🔧 Author:
- **Nabin Bist**

---

## 🔗 License:
- For academic/public research usage.
