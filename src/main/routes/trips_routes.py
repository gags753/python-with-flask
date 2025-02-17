from flask import jsonify, Blueprint, request
from pydantic import ValidationError

# Importação de controllers
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer

from src.controllers.participants_finder import ParticipantFinder
from src.controllers.participant_creator import ParticipantCreator
from src.controllers.participant_confirmer import ParticipantConfirmer

from src.controllers.activity_creator import ActivityCreator
from src.controllers.activity_finder import ActivityFinder

from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder

# Importando requests
from src.main.requests.create_trip_request import CreateTripRequest

# Imortação de repositórios
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.repositories.activities_repository import ActivitiesRepository

# Importando o gerente de conexões
from src.models.settings.db_connection_handler import db_connection_handler
 
trips_routes_bp = Blueprint("trip_routes", __name__)

@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)
  emails_repository = EmailsToInviteRepository(conn)
  controller = TripCreator(trips_repository, emails_repository)

  try:
    data = CreateTripRequest(**request.json).model_dump()
    response = controller.create(data)

    return jsonify(response["body"]), response["status_code"]
  except ValidationError as err:
    return jsonify(err.errors()), 400

@trips_routes_bp.route("/trips/<tripId>", methods=["GET"])
def find_trip_by_id(tripId: str):
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)
  controller = TripFinder(trips_repository)

  response = controller.find_trip_details(tripId)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/confirm", methods=["GET"])
def confirm_trip(tripId: str):
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)
  controller = TripConfirmer(trips_repository)

  response = controller.confirm(tripId)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/links", methods=["POST"])
def create_trip_link(tripId: str):
  conn = db_connection_handler.get_connection()
  link_repository = LinksRepository(conn)
  controller = LinkCreator(link_repository)

  response = controller.create(request.json, tripId)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/links", methods=["GET"])
def find_trip_link(tripId: str):
  conn = db_connection_handler.get_connection()
  link_repository = LinksRepository(conn)
  controller = LinkFinder(link_repository)

  response = controller.find(tripId)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/invites", methods=["POST"])
def inviteToTrip(tripId: str):
  conn = db_connection_handler.get_connection()
  participant_repository = ParticipantsRepository(conn)
  emails_repository = EmailsToInviteRepository(conn)

  controller = ParticipantCreator(participant_repository, emails_repository)

  response = controller.create(request.json, tripId)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/activities", methods=["POST"])
def create_activity(tripId: str):
  conn = db_connection_handler.get_connection()
  activities_repository = ActivitiesRepository(conn)
  controller = ActivityCreator(activities_repository)

  response = controller.create(request.json, tripId)

  return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/participants", methods=["GET"])
def get_trip_participants(tripId: str):
  conn = db_connection_handler.get_connection()
  participant_repository = ParticipantsRepository(conn)
  controller = ParticipantFinder(participant_repository)

  response = controller.find_participants_from_trip(tripId)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/activities", methods=["GET"])
def get_trip_activities(tripId: str):
  conn = db_connection_handler.get_connection()
  activities_repository = ActivitiesRepository(conn)
  controller = ActivityFinder(activities_repository)

  response = controller.find_from_trip(tripId)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/participants/<participantId>/confirm", methods=["PATCH"])
def confirm_participant(participantId: str):
  conn = db_connection_handler.get_connection()
  participants_repository = ParticipantsRepository(conn)
  controller = ParticipantConfirmer(participants_repository)

  response = controller.confirm(participantId)

  return jsonify(response["body"]), response["status_code"]
