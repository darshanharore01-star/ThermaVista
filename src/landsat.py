from src.earth_engine import ee


def get_landsat_image(lat, lon, year, layer):

    point = ee.Geometry.Point([lon, lat])

    image = (
        ee.ImageCollection("LANDSAT/LC08/C02/T1_L2")
        .filterBounds(point)
        .filterDate(f"{year}-01-01", f"{year}-12-31")
        .sort("CLOUD_COVER")
        .first()
    )

    # True Color
    if layer == "True Color":
        vis_params = {
            "bands": ["SR_B4", "SR_B3", "SR_B2"],
            "min": 7000,
            "max": 15000,
        }

    # NDVI
    elif layer == "NDVI":
        image = image.normalizedDifference(["SR_B5", "SR_B4"]).rename("NDVI")

        vis_params = {
            "min": 0,
            "max": 1,
            "palette": ["brown", "yellow", "green"],
        }

    # Land Surface Temperature
    elif layer == "Land Surface Temperature":
        image = image.select("ST_B10").multiply(0.00341802).add(149.0)

        vis_params = {
            "min": 290,
            "max": 320,
            "palette": ["blue", "orange", "red"],
        }

    map_id = image.getMapId(vis_params)

    return map_id["tile_fetcher"].url_format
    