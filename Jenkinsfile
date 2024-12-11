pipeline {
    agent any
    environment {
        DOCKER_IMAGE_SVM = "svm-microservice"
        DOCKER_IMAGE_VGG = "vgg-microservice"
        DOCKER_IMAGE_FRONTEND = "frontend"
    }
    stages {
            stage('Clone') {
            steps {
                git branch: 'master'
                url: 'https://github.com/salsabilmoussa/MusicGenre.git'
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
                    sh 'docker-compose exec svm-service pytest /tests/test_svm.py'
                    sh 'docker-compose exec vgg-service pytest /tests/test_vgg.py'
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