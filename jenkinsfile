pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
              git url: 'https://github.com/lakkawardhananjay/sample_jenkins_CI-CT.git', branch: 'main'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest discover' // Example Python unit tests
            }
        }
        stage('Report') {  // Optional, but good practice
            steps {
                junit 'test-reports/*.xml'  // If your tests generate JUnit-style reports
            }
        }
    }

    post {
        always {
            echo "Build finished!"
        }
        success {
            echo "Build succeeded!"
        }
        failure {
            echo "Build failed!"
        }
    }
}
