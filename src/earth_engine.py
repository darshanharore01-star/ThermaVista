import ee

PROJECT_ID = "nth-mantra-501009-e8"

try:
    ee.Initialize(project=PROJECT_ID)
except Exception:
    ee.Authenticate()
    ee.Initialize(project=PROJECT_ID)
    
    