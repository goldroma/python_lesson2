pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('test') {
            steps {
            echo 'my test'
            workspace = env.WORKSPACE
            echo "Current workspace is $WORKSPACE"  
            }
        }    
    }
}
