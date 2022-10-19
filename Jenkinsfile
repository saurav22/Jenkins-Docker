pipeline {
    agent any    
    stages {
        stage('Cloning Git') {
            steps {
                // make link via Pipeline Syntax
                checkout([$class: 'GitSCM', branches: [[name: '*/*']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Pankajsingh63/Jenkins-Docker.git']]])       
            }
        }
    
    // Building Docker images
    stage('Building image') {
      steps{
        script {
            sh 'docker build -t devops-repo/python-app-1.0 .'
        }
      }
    }
    
     // Uploading Docker images into Docker Hub
    stage('Upload Image') {
     steps{    
         script {
            withCredentials([string(credentialsId: 'pankajsingh63', variable: 'dockerhubpwd')]) {
            sh 'docker login -u  pankajsingh63 -p ${dockerhubpwd} docker.io '  
            
            sh 'docker push pankajsingh63/devops-repo:latest'
            sh 'docker push devops-repo/python-app-1.0:latest'
    // some block
}
        }
      }
    }
    
    
    }
  }
