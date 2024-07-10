from sqlite3 import Connection
from typing import Dict, List, Tuple

class LinksRepository:
  def __init__(self, conn: Connection) -> None:
    self.__conn = conn

  def create_link_to_trip(self, link_info: Dict) -> None:
    cursor = self.__conn.cursor()
    cursor.execute(
      '''
        INSERT INTO links
          (id, trip_id, link)
        VALUES
          (?, ?, ?)
      ''', (
        link_info["id"],
        link_info["trip_id"],
        link_info["link"],
      )
    )
    self.__conn.commit()

  def find_links_of_trip(self, trip_id: str) -> list[Tuple]:
    cursor = self.__conn.cursor()
    cursor.execute(
      '''
        SELECT * FROM links WHERE trip_id = ?
      ''', (trip_id,)
    )
    links = cursor.fetchmany()
    return links