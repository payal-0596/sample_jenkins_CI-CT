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
        dir('.') {
            bat 'pip install pytest pytest-xdist'
            bat 'python -m pytest --junitxml=test-report.xml'
        }
    }
}
        stage('Report') {
            steps {
                junit 'test-report.xml'  // Tell Jenkins where to find the reports
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
