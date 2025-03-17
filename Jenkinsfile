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
                dir('.'){
                powershell 'python -m unittest discover'
                }// Example Python unit tests
            }
        }
        stage('Report') {  // Optional, but good practice
            steps {
                junit '**/reports/*.xml' // If your tests generate JUnit-style reports
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
