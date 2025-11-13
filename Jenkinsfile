// Updated Jenkinsfile to use a virtual environment (Recommended)
pipeline {
    agent any

    environment {
        // Define the path for the virtual environment
        VENV_DIR = '.venv' 
    }

    stages {
        // ... (Checkout Code stage remains the same) ...
        stage('Checkout Code') {
            steps {
                echo 'Checking out code from SCM...'
                git branch: 'main', url:'https://github.com/1ms24mc111/machine.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Setting up virtual environment and installing dependencies...'
                
                // 1. Create the virtual environment using python3
                sh 'python3 -m venv $VENV_DIR'
                
                // 2. Activate the venv and upgrade pip (commands change slightly when in a venv)
                sh '. $VENV_DIR/bin/activate && pip install --upgrade pip'
                
                // 3. Install requirements using the venv's pip
                sh '. $VENV_DIR/bin/activate && pip install -r requirements.txt' 
            }
        }

        stage('Run Model Tests') {
            steps {
                echo 'Executing machine learning tests with pytest using the virtual environment...'
                // Run pytest using the executable within the virtual environment
                sh '. $VENV_DIR/bin/activate && pytest test.py --junitxml=test-results.xml' 
            }
        }
        
        stage('Publish Test Results') {
            steps {
                echo 'Publishing test results for display in Jenkins UI...'
                junit 'test-results.xml'
                archiveArtifacts artifacts: 'model.pkl', onlyIfSuccessful: true
            }
        }
    }
}
