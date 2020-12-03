pipeline{
        agent any
        environment {
            app_version = 'v1'
            rollback = 'false'
        }
        stages{
            
            stage('Testing'){
                steps{
                    sh "./scripts/test.sh"
                }
            }
            stage('Building Images'){
                steps{
                    sh "./scripts/build.sh"
                }
            }
            stage('Deploying App'){
                steps{
                    sh "./scripts/deploy.sh"
                }
            }
        }
    
}