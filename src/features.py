from src.earth_engine import ee


def get_features(lat, lon, year):

    point = ee.Geometry.Point([lon, lat])

    image = (
        ee.ImageCollection("LANDSAT/LC08/C02/T1_L2")
        .filterBounds(point)
        .filterDate(f"{year}-01-01", f"{year}-12-31")
        .sort("CLOUD_COVER")
        .first()
    )

    # NDVI
    ndvi = image.normalizedDifference(
        ["SR_B5", "SR_B4"]
    )

    # Land Surface Temperature
    lst = image.select("ST_B10") \
        .multiply(0.00341802) \
        .add(149.0)

    region = point.buffer(500).bounds()

    ndvi_value = ndvi.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=region,
        scale=30
    ).get("nd")

    lst_value = lst.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=region,
        scale=30
    ).get("ST_B10")

    return {
        "ndvi": ndvi_value.getInfo(),
        "lst": lst_value.getInfo()
    }