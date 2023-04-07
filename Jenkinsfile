pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t sample-web-app .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run --rm -p 5000:5000 sample-web-app pytest'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker push your-docker-hub-username/sample-web-app:latest'
                sh 'kubectl apply -f kubernetes-deployment.yml'
            }
        }
    }

    post {
        always {
            sh 'docker stop sample-web-app'
        }
    }
}

