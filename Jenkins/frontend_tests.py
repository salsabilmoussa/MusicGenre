import pytest
from flask import Flask, jsonify
from unittest.mock import patch

# Mock Flask's HTTP client for testing the frontend
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def mock_predict():
    return jsonify({"predicted_genre": "rock"})

def test_frontend_svm_predict():
    with app.test_client() as client:
        with patch('requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = {"predicted_genre": "rock"}

            response = client.post('/predict', data={'file': 'test_audio.wav'})
            assert response.status_code == 200
            assert 'predicted_genre' in response.json
            assert response.json['predicted_genre'] == 'rock'

def test_frontend_vgg_predict():
    with app.test_client() as client:
        with patch('requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = {"predicted_genre": "jazz"}

            response = client.post('/predict', data={'file': 'test_audio.wav'})
            assert response.status_code == 200
            assert 'predicted_genre' in response.json
            assert response.json['predicted_genre'] == 'jazz'

def test_frontend_file_selection():
    with app.test_client() as client:
        # Simulating a scenario where no file is selected
        response = client.post('/predict', data={})
        assert response.status_code == 400
        assert 'error' in response.json
        assert response.json['error'] == 'No file part in the request'
