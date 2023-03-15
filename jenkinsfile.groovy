pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'pip install selenium'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest pesan.py -m "pesan_tiket"'
            }
        }
    }
}
