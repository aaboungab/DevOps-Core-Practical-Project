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
                    script{
                        if (env.rollback == 'false'){
                            image = docker.build("aaboungab/service1")
                            image = docker.build("aaboungab/service2")
                            image = docker.build("aaboungab/service3")
                            image = docker.build("aaboungab/service4")
                        }
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
}