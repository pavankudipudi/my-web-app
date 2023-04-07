pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t my-web-app .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run --rm -p 5000:5000 my-web-app python3 -m unittest'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker push my-web-app'
            }
        }
    }
}

