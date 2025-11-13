// Updated and enhanced Jenkinsfile
pipeline {
    agent any // Use 'any' agent available to run the pipeline

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out code from SCM...'
                // Explicitly defining the SCM checkout using the 'git' step
                // This replaces the default implicit checkout, ensuring correct branch handling.
                git branch: 'main', url:'https://github.com/1ms24mc111/machine.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                
                // Use 'python3' and 'pip3' for modern systems to avoid 'python: not found' errors
                sh 'python3 -m pip install --upgrade pip' // Ensure pip is updated

                // Install libraries listed in requirements.txt
                sh 'pip3 install -r requirements.txt' 
            }
        }

        stage('Run Model Tests') {
            steps {
                echo 'Executing machine learning tests with pytest...'
                
                // Assuming 'pytest' is installed globally or in the path accessible by Jenkins
                // If pytest is not found, you might need 'sh "$HOME/.local/bin/pytest ..."' or 'sh "$(pip3 show pytest | grep Location | cut -d' ' -f2)/pytest ..."'
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
