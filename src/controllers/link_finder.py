from src.models.repositories.links_repository import LinksRepository

class LinkFinder:
  def __init__(self, link_repository: LinksRepository) -> None:
    self.__link_repository = link_repository

  def find(self, tripId: str):
    try:
      links = self.__link_repository.find_links_of_trip(tripId)

      formated_links = []
      for link in links:
        formated_links.append({
          "id": link[0],
          "url": link[2],
          "title": link[3]
        })

      return {
        "body": { "links": formated_links },
        "status_code": 200
      }
    except Exception as exception:
      return {
        "body": { "error": "Bad Request", "message": str(exception) },
        "status_code": 400
      }