from fastapi.responses import RedirectResponse
from app.schemas import UserOut, UserAuth
from replit import db
from app.utils import get_hashed_password
from uuid import uuid4