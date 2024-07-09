import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .emails_to_invite_repository import EmailsToInviteRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_register_email():
  conn = db_connection_handler.get_connection()
  email_to_invite_repository = EmailsToInviteRepository(conn)

  emails_trips_infos = {
    "id": str(uuid.uuid4()),
    "trip_id": trip_id,
    "email": "email.olaMundo@email.com"
  }

  email_to_invite_repository.register_email(emails_trips_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_find_email_from_trip():
  conn = db_connection_handler.get_connection()
  email_to_invite_repository = EmailsToInviteRepository(conn)

  emails = email_to_invite_repository.find_email_from_trip(trip_id)
  print()
  print(emails)
