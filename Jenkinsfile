pipeline{
        agent any
        environment {
            app_version = 'v1'
            rollback = 'false'
        }
        stages{
            stage('Install Docker using ansible'){
                steps{
                sh " ./scripts/ansible.sh"
                	}
            }
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
            stage('Pushing Images'){
                steps{
                    sh "./scripts/push.sh"
                }
            }
            stage('Deploying App'){
                steps{
                    sh "./scripts/deploy.sh"
                }
            }
        }
    
}