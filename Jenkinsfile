pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // This stage might be optional for a Python project
            }
        }
        stage('Unit Tests') {
            steps {
                echo 'Running unit tests...'
                sh 'python -m unittest discover' // Run unit tests
            }
        }
        stage('Code Analysis') {
            steps {
                echo 'Analyzing code...'
                sh 'flake8 hello.py' // Run code analysis
            }
        }
        stage('Security Scan') {
            steps {
                echo 'Scanning for security issues...'
                sh 'bandit -r .' // Run security scan
            }
        }
        stage('Deploy to Staging') {
            steps {
                echo 'Deploying to staging...'
                // Example command to deploy to staging
                // sh 'scp -r * user@staging-server:/path/to/deploy'
            }
        }
        stage('Integration Tests on Staging') {
            steps {
                echo 'Running integration tests on staging...'
                // Example command to run integration tests
                // sh 'pytest'
            }
        }
        stage('Deploy to Production') {
            steps {
                echo 'Deploying to production...'
                // Example command to deploy to production
                // sh 'scp -r * user@production-server:/path/to/deploy'
            }
        }
    }
    post {
        success {
            emailext(
                to: 'felixkent360@example.com',
                subject: 'Pipeline Success',
                body: 'The pipeline was successful!',
                attachmentsPattern: '**/*.log'
            )
        }
        failure {
            emailext(
                to: 'felixkent360@example.com',
                subject: 'Pipeline Failure',
                body: 'The pipeline failed.',
                attachmentsPattern: '**/*.log'
            )
        }
    }
}
