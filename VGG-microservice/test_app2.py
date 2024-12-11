from app2 import app

def test_vgg_valid_audio():
    # Initialisation du client Flask pour tester l'application
    client = app.test_client()

    # Charger un fichier audio valide
    with open("test_audio.wav", "rb") as audio_file:
        response = client.post("/predict", content_type="multipart/form-data", data={
            "file": (audio_file, "test_audio.wav")
        })

    # Vérifier la réponse
    assert response.status_code == 200
    data = response.get_json()
    assert "predicted_genre" in data

def test_vgg_no_audio():
    client = app.test_client()

    # Envoyer une requête sans fichier
    response = client.post("/predict", content_type="multipart/form-data", data={})

    # Vérifier la réponse
    assert response.status_code == 400  # Une erreur doit être renvoyée
    data = response.get_json()
    assert data["error"] == "No file part in the request"  # Vérifier le message d'erreur
