// MOD11A1 V061 - Daily LST Day/Night for Nepal Districts (FY2023_24)
// Author: Nabin Bist

// 1. Load Nepal District Boundary (77 Districts)
var districts = ee.FeatureCollection('users/nabinbist2052/local_unit'); // <-- Update this path if needed

// 2. Define Fiscal Year 2023/24 (eg. July 16, 2023 to July 15, 2024)
var fiscalYear = {
  name: 'year',
  start: 'Enter start date',
  end: 'Enter end date'
};

// 3. Load MODIS Terra Daily LST Data (MOD11A1 V061)
var modis = ee.ImageCollection('MODIS/061/MOD11A1')
              .filterDate(fiscalYear.start, fiscalYear.end)
              .filterBounds(districts);

// 4. Convert LST from Kelvin to Celsius
var lstDay = modis.select('LST_Day_1km')
                  .mean()
                  .multiply(0.02)
                  .subtract(273.15)
                  .rename('LST_Day_Celsius');

var lstNight = modis.select('LST_Night_1km')
                    .mean()
                    .multiply(0.02)
                    .subtract(273.15)
                    .rename('LST_Night_Celsius');

// 5. Reduce to District Level
var dayStats = lstDay.reduceRegions({
  collection: districts,
  reducer: ee.Reducer.mean(),
  scale: 1000
}).map(function(feature) {
  return feature.set('Fiscal_Year', fiscalYear.name);
});

var nightStats = lstNight.reduceRegions({
  collection: districts,
  reducer: ee.Reducer.mean(),
  scale: 1000
}).map(function(feature) {
  return feature.set('Fiscal_Year', fiscalYear.name);
});

// 6. Export to Google Drive
Export.table.toDrive({
  collection: dayStats,
  description: fiscalYear.name + '_LST_Day',
  fileFormat: 'CSV'
});

Export.table.toDrive({
  collection: nightStats,
  description: fiscalYear.name + '_LST_Night',
  fileFormat: 'CSV'
});

// 7. Print Preview
print('Sample Day LST :', dayStats.limit(10));
print('Sample Night LST :', nightStats.limit(10));
