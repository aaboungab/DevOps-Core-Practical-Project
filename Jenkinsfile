pipeline{
        agent any
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