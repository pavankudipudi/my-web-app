pipeline {
    agent {
        docker {
            image 'python:3.9'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python manage.py test'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-web-page .'
            }
        }
        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                    sh 'docker push my-web-page'
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG_FILE')]) {
                    sh 'kubectl apply -f deployment.yaml'
                    sh 'kubectl apply -f pod.yaml'
                    sh 'kubectl apply -f service.yaml'
                }
            }
        }
    }
}
