pipeline {
    agent any
    environment {
         GIT_REPO = 'https://github.com/salsabilmoussa/MusicGenre.git'
        GIT_CREDENTIALS_ID = 'github_token'
        DOCKER_IMAGE_SVM = "svm-microservice-1"
        DOCKER_IMAGE_VGG = "vgg-microservice-1"
        DOCKER_IMAGE_FRONTEND = "frontend-1"
    }
    stages {
             stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: "${GIT_CREDENTIALS_ID}", url: "${GIT_REPO}"
            }
        }
        
        stage('Build Docker Images') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE_SVM, '../SVM-microservice/Dockerfile')
                    docker.build(DOCKER_IMAGE_VGG, '../VGG-microservice/Dockerfile')
                    docker.build(DOCKER_IMAGE_FRONTEND, '../frontend/Dockerfile')
                }
            }
        }
        stage('Run Docker Compose') {
            steps {
                script {
                    sh 'docker-compose -f ../docker-compose.yaml up -d'
                }
            }
        }
        stage('Run Tests') {
        steps {
            script {
                sh 'docker-compose exec svm-microservice pytest /SVM-microservice/test_app1.py'
                sh 'docker-compose exec vgg-microservice pytest /VGG-microservice/test_app2.py'
            }
        }
}

        stage('Stop Services') {
            steps {
                script {
                    // Stop all containers after tests
                    sh 'docker-compose down'
                }
            }
        }
    }
    post {
        success {
            echo 'Build and tests successful!'
        }
        failure {
            echo 'Build or tests failed!'
        }
    }
}