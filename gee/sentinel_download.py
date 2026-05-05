import ee

ee.Initialize()

ROI = ee.Geometry.Rectangle([78.5, 10.8, 78.8, 11.1])  # Example ROI

def get_sentinel(start, end):
    collection = (
        ee.ImageCollection("COPERNICUS/S2_SR")
        .filterBounds(ROI)
        .filterDate(start, end)
        .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 10))
        .median()
        .clip(ROI)
    )
    return collection

image_T1 = get_sentinel("2019-01-01", "2019-03-31")
image_T2 = get_sentinel("2023-01-01", "2023-03-31")

task1 = ee.batch.Export.image.toDrive(
    image=image_T1,
    description="Sentinel_T1",
    scale=10,
    region=ROI
)

task2 = ee.batch.Export.image.toDrive(
    image=image_T2,
    description="Sentinel_T2",
    scale=10,
    region=ROI
)

task1.start()
task2.start()
