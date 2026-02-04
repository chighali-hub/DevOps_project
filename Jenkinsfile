pipeline {
    agent any

    environment {
        IMAGE_NAME = "django-crud-app"
        CONTAINER_NAME = "django-app-prod"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('Build & Tests') {
            agent {
                docker { 
                    image 'python:3.9-slim' 
                    // Mount current dir to keep files
                    args '-u 0:0' 
                }
            }
            steps {
                dir('django-crud-app') {
                    echo 'Installing Dependencies and Running Tests...'
                    sh 'pip install -r requirements.txt'
                    sh 'python manage.py test'
                }
            }
        }

        stage('SAST (SonarQube)') {
            agent {
                docker {
                    image 'sonarsource/sonar-scanner-cli:latest'
                    args '--network devops_project_devops-net' // Connect to SonarQube network
                }
            }
            steps {
                dir('django-crud-app') {
                    echo 'Running SonarQube Analysis...'
                    withSonarQubeEnv('SonarQube') {
                         // On force l'injection du token via 'sonar.login' pour être sûr
                         withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
                            sh 'sonar-scanner -Dsonar.login=${SONAR_TOKEN}'
                         }
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Docker Build') {
            steps {
                dir('django-crud-app') {
                    echo 'Building Docker Image...'
                    sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
                    sh "docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest"
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Application...'
                sh """
                docker stop ${CONTAINER_NAME} || true
                docker rm ${CONTAINER_NAME} || true
                """
                
                sh """
                docker run -d --name ${CONTAINER_NAME} \
                --network devops_project_devops-net \
                -p 8000:8000 \
                ${IMAGE_NAME}:latest
                """
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
