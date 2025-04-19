from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash
from models import User

def setup_api_routes(app):
    """Simple API endpoint for users"""
    @app.route('/api/users', methods=['POST'])
    def api_users():
        """Return all users in a simple format"""
        users = User.query.all()
        user_list = []
        for user in users:
            if not user.email or not user.password_hash:
                return jsonify({"success": False}), 400
            if user and check_password_hash(user.password_hash, password):
                user_list.append({
                'id': user.id,
                'name': user.full_name,
                'email': user.email,
                'password_hash': user.password_hash})
                return jsonify({"success": True})
            else:
                return jsonify({"success": False})
        return jsonify(user_list) 