pipeline {
    agent any

    environment {
        IMAGE = "selfheal-app"
        CONTAINER = "selfheal-container"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ganeshmalleshe17/self-healing-jenkins.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t $IMAGE app/'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    try {
                        sh '''
                        docker rm -f $CONTAINER || true
                        docker run -d --name $CONTAINER -p 5000:5000 $IMAGE
                        '''
                    } catch (e) {
                        error "Deployment Failed"
                    }
                }
            }
        }
    }

    post {
        failure {
            echo "Pipeline failed → Running self-healing logic"
            sh 'python3 scripts/analyze_failure.py'
        }
    }
}
