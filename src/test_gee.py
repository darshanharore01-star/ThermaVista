import ee

PROJECT_ID = "nth-mantra-501009-e8"

try:
    # Force Python authentication
    ee.Authenticate()

    # Initialize using your project
    ee.Initialize(project=PROJECT_ID)

    print("✅ Google Earth Engine Connected Successfully!")

    collection = ee.ImageCollection("LANDSAT/LC08/C02/T1_L2")
    print("Total Images:", collection.size().getInfo())

except Exception as e:
    print("❌ Error:")
    print(e)