import pytest
import requests

BASE_URL = "http://localhost:5002/predict"

def test_vgg_predict_valid_file():
    # Path to a valid audio file
    audio_file = {'file': open('tests/test_audio.wav', 'rb')}
    
    response = requests.post(BASE_URL, files=audio_file)
    
    assert response.status_code == 200
    result = response.json()
    assert 'predicted_genre' in result
    assert result['predicted_genre'] in ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

def test_vgg_predict_no_file():
    response = requests.post(BASE_URL)
    assert response.status_code == 400
    result = response.json()
    assert 'error' in result
    assert result['error'] == 'No file part in the request'

def test_vgg_predict_invalid_file():
    # Testing with an empty file
    audio_file = {'file': open('tests/empty_file.wav', 'rb')}
    response = requests.post(BASE_URL, files=audio_file)
    assert response.status_code == 400
    result = response.json()
    assert 'error' in result
    assert result['error'] == 'No selected file'
