pipeline {
    agent any

    environment {
        STUDENT_NAME = 'Dilnur'
        STUDENT_SURNAME = 'Satibaldiyev'
        STUDENT_GROUP = 'IT2-2304'
        STUDENT_ID = '38036'
        IMAGE_NAME = 'satibaldiyev-dilnur-devops'
        CONTAINER_NAME = 'satibaldiyev-dilnur-container'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'python3 --version'
                sh 'python3 -m py_compile app.py test_app.py'
                sh 'echo "Student: $STUDENT_NAME $STUDENT_SURNAME"'
                sh 'echo "Group: $STUDENT_GROUP"'
                sh 'echo "Student ID: $STUDENT_ID"'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m unittest -v'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t "$IMAGE_NAME" .'
            }
        }
        stage('Docker Run') {
            steps {
                sh 'docker rm -f "$CONTAINER_NAME" || true'
                sh 'docker run --name "$CONTAINER_NAME" -e STUDENT_NAME="$STUDENT_NAME" -e STUDENT_SURNAME="$STUDENT_SURNAME" -e STUDENT_GROUP="$STUDENT_GROUP" -e STUDENT_ID="$STUDENT_ID" "$IMAGE_NAME"'
                sh 'docker rm "$CONTAINER_NAME"'
            }
        }
    }
    post {
        always {
            echo 'Pipeline execution finished. Check the stage results above.'
        }
    }
}
