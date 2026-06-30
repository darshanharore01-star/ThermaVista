import ee

PROJECT_ID = "nth-mantra-501009-e8"

ee.Initialize(project=PROJECT_ID)


def get_landsat_image():

    image = (
        ee.ImageCollection("LANDSAT/LC08/C02/T1_L2")
        .filterDate("2024-01-01", "2024-12-31")
        .filterBounds(ee.Geometry.Point([73.8567, 18.5204]))  # Pune
        .sort("CLOUD_COVER")
        .first()
    )

    return image