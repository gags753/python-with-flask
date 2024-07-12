from typing import Dict, Tuple, List
from sqlite3 import Connection

class ActivitiesRepository:
  def __init__(self, conn: Connection) -> None:
    self.__conn = conn

  def register_activitie(self, activity_infos: Dict) -> None:
    cursor = self.__conn.cursor()
    cursor.execute(
      '''
        INSERT INTO activities
          (id, trip_id, title, accurs_at)
        VALUES 
          (?, ?, ?, ?)
      ''', (
        activity_infos["id"],
        activity_infos["trip_id"],
        activity_infos["title"],
        activity_infos["accurs_at"],
      )
    )
    self.__conn.commit()

  def find_activities_from_trip(self, trip_id: str) -> List[Tuple]:
    cursor = self.__conn.cursor()
    cursor.execute(
      '''
        SELECT * FROM activities WHERE trip_id = ?
      ''', (trip_id,)
    )
    activities = cursor.fetchmany()
    return activities
  
  # def update_trip_status(self, trip_id: str) -> None:
  #   cursor = self.__conn.cursor()
  #   cursor.execute(
  #     '''
  #       UPDATE trips
  #         SET status = 1
  #       WHERE
  #         id = ?
  #     ''', (trip_id,)
  #   )
  #   self.__conn.commit()
