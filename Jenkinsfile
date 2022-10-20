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
            sh 'docker build -t pankajsingh63/docker-app .'
        }
      }
    }
    
     // Uploading Docker images into Docker Hub
    stage('Upload Image') {
     steps{    
         script {
            withCredentials([string(credentialsId: 'pankajsingh63', variable: 'dockerhubpwd')]) {
            // Login   Docker hub and push the image           
              sh "docker login -u  pankajsingh63 -p ${dockerhubpwd} docker.io " 
            sh 'docker push pankajsingh63/docker-app'
			  sh 'docker run -p 80:5000 -d pankajsingh63/docker-app '
  }			
        }
      }
    }

    
    }
  }
