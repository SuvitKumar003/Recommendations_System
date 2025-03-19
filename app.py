from flask import Flask, render_template, request, jsonify
from recommender import RecommendationSystem
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# Initialize the recommendation system
recommender = RecommendationSystem()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        item_id = request.form.get('item_id')
        if not item_id:
            return jsonify({'error': 'Item ID is required'}), 400
        
        recommendations = recommender.get_recommendations(item_id)
        return jsonify({'recommendations': recommendations})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/load_data', methods=['POST'])
def load_data():
    try:
        file_path = request.form.get('file_path')
        if not file_path or not os.path.exists(file_path):
            return jsonify({'error': 'Invalid file path'}), 400
        
        success = recommender.load_data(file_path)
        if success:
            recommender.preprocess_data()
            return jsonify({'message': 'Data loaded successfully'})
        else:
            return jsonify({'error': 'Failed to load data'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 