pipeline {
    agent any
    environment {
        EMAIL_RECIPIENT = 'felixkent360@gmail.com'
    }
    stages {
        stage('Build') {
            steps {
                script {
                    echo 'Building the application...'
                    // Example build command for a Python project
                    sh 'echo Building the application...'
                }
            }
        }
        stage('Unit and Integration Tests') {
            steps {
                script {
                    echo 'Running unit and integration tests...'
                    // Running unit tests using pytest
                    sh 'pytest'
                }
            }
        }
        stage('Code Analysis') {
            steps {
                script {
                    echo 'Analyzing code with pylint...'
                    // Performing code analysis with pylint
                    sh 'pylint app.py test_app.py'
                }
            }
        }
        stage('Security Scan') {
            steps {
                script {
                    echo 'Performing security scan with bandit...'
                    // Performing security scan with bandit
                    sh 'bandit -r app.py'
                }
            }
        }
        stage('Deploy to Staging') {
            steps {
                script {
                    echo 'Deploying to staging environment...'
                    // Example deployment to staging server
                    sh 'scp -r * user@staging-server:/path/to/staging'
                }
            }
        }
        stage('Integration Tests on Staging') {
            steps {
                script {
                    echo 'Running integration tests on staging...'
                    // Running integration tests in the staging environment
                    sh 'pytest --staging'
                }
            }
        }
        stage('Deploy to Production') {
            steps {
                script {
                    echo 'Deploying to production environment...'
                    // Example deployment to production server
                    sh 'scp -r * user@production-server:/path/to/production'
                }
            }
        }
    }
    post {
        always {
            emailext to: "${EMAIL_RECIPIENT}",
                     subject: "Jenkins Pipeline Status",
                     body: """\
The Jenkins pipeline has finished executing. 
Here are the details:
- Build Status: ${currentBuild.result}
- Logs: See the attached logs.
                     """,
                     attachmentsPattern: '**/*.log',
                     compress: true
        }
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
            emailext to: "${EMAIL_RECIPIENT}",
                     subject: "Jenkins Pipeline Failed",
                     body: """\
The Jenkins pipeline has failed. 
Here are the details:
- Build Status: ${currentBuild.result}
- Logs: See the attached logs.
                     """,
                     attachmentsPattern: '**/*.log',
                     compress: true
        }
    }
}
