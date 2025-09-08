from fastapi import APIRouter, HTTPException
from db.db import database

router = APIRouter()

@router.get("/shorturls/{shortcode}")
def get_short_url(shortcode: str):
	if shortcode not in database:
		raise HTTPException(status_code=404, detail="Shortcode not found")
	return database[shortcode]
