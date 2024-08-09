from flask import Blueprint, jsonify, request
from app import db
from app.models import User, Track, Playlist

# Создаем blueprint для маршрутов
bp = Blueprint('main', __name__)

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201

@bp.route('/tracks', methods=['GET'])
def get_tracks():
    tracks = Track.query.all()
    return jsonify([{'title': track.title, 'duration': track.duration} for track in tracks])

@bp.route('/playlists', methods=['POST'])
def create_playlist():
    data = request.json
    user = User.query.get(data['user_id'])
    if not user:
        return jsonify({"message": "User not found"}), 404
    playlist = Playlist(title=data['title'], user_id=user.id)
    db.session.add(playlist)
    db.session.commit()
    return jsonify({"message": "Playlist created"}), 201