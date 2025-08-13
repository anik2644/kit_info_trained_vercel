from mangum import Mangum
from app.main import app

# Lambda adapter for Vercel
handler = Mangum(app)
