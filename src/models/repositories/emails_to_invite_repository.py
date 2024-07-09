from typing import Dict, Tuple, List
from sqlite3 import Connection

class EmailsToInviteRepository:
  def __init__(self, conn: Connection) -> None:
    self.__conn = conn

  def register_email(self, email_infos: Dict) -> None:
    cursor = self.__conn.cursor()
    cursor.execute(
      '''
        INSERT INTO emails_to_invite
          (id, trip_id, email)
        VALUES 
          (?, ?, ?)
      ''', (
        email_infos["id"],
        email_infos["trip_id"],
        email_infos["email"],
      )
    )
    self.__conn.commit()

  def find_email_from_trip(self, trip_id: str) -> List[Tuple]:
    cursor = self.__conn.cursor()
    cursor.execute(
      '''
        SELECT * FROM emails_to_invite WHERE trip_id = ?
      ''', (trip_id,)
    )
    email_to_invite = cursor.fetchmany()
    return email_to_invite
  
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
