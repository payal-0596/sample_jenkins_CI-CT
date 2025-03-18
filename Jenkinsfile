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
                // Ensure unittest-xml-reporting is installed
                sh 'pip install unittest-xml-reporting'

                // Run the tests and generate JUnit XML report
                sh 'python -m unittest discover -s . -p "test_*.py"'
            }
        }
        stage('Report') {
            steps {
                junit '**/TEST-*.xml' //Adjust the directory, based on the discover report name
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
