from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
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

@router.get("/{shortcode}")
def redirect_to_url(shortcode: str):
	if shortcode not in database:
		raise HTTPException(status_code=404, detail="Shortcode not found")

	entry = database[shortcode]
	expiry = datetime.fromisoformat(entry["validity"])

	# check expiry
	if datetime.now() > expiry:
		raise HTTPException(status_code=410, detail="Short URL expired")

	# increment code_hit
	entry["code_hit"] += 1
	save_db()

	return RedirectResponse(url=entry["url"])