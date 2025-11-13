// Jenkinsfile
pipeline {
    agent any // Specifies where the pipeline will run

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out code from SCM...'
                 git branch: 'main', url:'https://github.com/1ms24mc111/machine.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'python -m pip install --upgrade pip' // Ensure pip is updated
                // Install libraries listed in requirements.txt
                sh 'pip install -r requirements.txt' 
            }
        }

        stage('Run Model Tests') {
            steps {
                echo 'Executing machine learning tests with pytest...'
                // The --junitxml option generates a report file for Jenkins to read
                sh 'pytest test.py --junitxml=test-results.xml' 
            }
        }
        
        stage('Publish Test Results') {
            steps {
                echo 'Publishing test results for display in Jenkins UI...'
                // Use the JUnit plugin to archive and display the results
                junit 'test-results.xml'
                // Optional: Archive the generated model file as an artifact
                archiveArtifacts artifacts: 'model.pkl', onlyIfSuccessful: true
            }
        }
    }
}
