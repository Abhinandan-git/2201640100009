from fastapi import APIRouter
from datetime import datetime, timedelta

from db.db import database, save_db

router = APIRouter()

@router.post("/shorturls")
def generate_short_url(url: str, shortcode: str = "", validity: int = 30):
    expiry_date = datetime.now() + timedelta(minutes=validity)

    # auto-generate shortcode if empty
    if shortcode == "":
        shortcode = str(int(datetime.now().timestamp()))[-6:]

    if shortcode not in database:
        database[shortcode] = {
            "validity": expiry_date.isoformat(),
            "url": url,
            "code_hit": 0,
            "creation_date": datetime.now().isoformat()
        }
        save_db()

    return {
        "shortLink": f"/{shortcode}",
        "expiry": expiry_date
    }
