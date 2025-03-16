
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Mock AI profile data
ai_profiles = [
    {
        'id': 1,
        'name': 'Wingman 1',
        'aggressiveness': 5,
        'evasion': 5,
        'engagement_range': 50,
        'conserve_fuel': True,
        'conserve_weapons': False
    },
    {
        'id': 2,
        'name': 'Wingman 2',
        'aggressiveness': 8,
        'evasion': 3,
        'engagement_range': 40,
        'conserve_fuel': False,
        'conserve_weapons': True
    }
]

@app.route('/')
def home():
    return render_template('ai_editor.html')

@app.route('/api/ai_profiles', methods=['GET'])
def get_ai_profiles():
    return jsonify(ai_profiles)

@app.route('/api/ai_profiles/<int:profile_id>', methods=['PUT'])
def update_ai_profile(profile_id):
    data = request.json
    for profile in ai_profiles:
        if profile['id'] == profile_id:
            profile.update(data)
            return jsonify({'message': 'Profile updated!'})
    return jsonify({'message': 'Profile not found!'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
