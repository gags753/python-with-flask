import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .links_repository import LinksRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
link_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_register_link():
  conn = db_connection_handler.get_connection()
  links_repository = LinksRepository(conn)

  links_infos = {
    "id": link_id,
    "trip_id": trip_id,
    "link": "https://www.google.com/",
    "title": "airbnb"
  }

  links_repository.register_link(links_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_find_email_from_trip():
  conn = db_connection_handler.get_connection()
  links_repository = LinksRepository(conn)

  links = links_repository.find_links_of_trip(trip_id)

  assert isinstance(links, list)
  assert isinstance(links[0], tuple)
  print()
  print(links)
