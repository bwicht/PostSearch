

let video;
let poseNet;
let pose;
let skeleton;
let button;
let json = {};

// Resultat photo
// let photo;

// Creation d'une Canva Principal avec retour video
// Chargement de poseNet
function setup() {
  createCanvas(640, 480);
  video = createCapture(VIDEO);
  video.hide();
  poseNet = ml5.poseNet(video);
  poseNet.on('pose', gotPoses);
  // Bouton pour capture, à changer en fonction des besoins
  button = createButton('Store Position !');
  button.position(320, 500);
  button.mousePressed(getUserPose);
}

function gotPoses(poses) {
  // Si élém détecté, créé pose et skeleton
  if (poses.length > 0) {
    pose = poses[0].pose;
    skeleton = poses[0].skeleton;
  }
}


function draw() {
  // retour video dans canva sur lequel se dessine le squelette
  image(video, 0, 0);

  // Dessiner skeleton, barres, points
  // Retour User pour faire une pose utilisable 
  if (pose) {
    let eyeR = pose.rightEye;
    let eyeL = pose.leftEye;
    let d = dist(eyeR.x, eyeR.y, eyeL.x, eyeL.y);
    fill(255, 0, 0);
    fill(0, 0, 255);


    for (let i = 0; i < pose.keypoints.length; i++) {
      let x = pose.keypoints[i].position.x;
      let y = pose.keypoints[i].position.y;
      fill(0, 255, 0);
      ellipse(x, y, 16, 16);
    }

    for (let i = 0; i < skeleton.length; i++) {
      let a = skeleton[i][0];
      let b = skeleton[i][1];
      strokeWeight(2);
      stroke(255);
      line(a.position.x, a.position.y, b.position.x, b.position.y);
    }
  }
}

// TODO : Only send if full skel or pose depending of cedric needs
// No need to feedback image
// Maybe ask to stay in position for 5 sec and take pic automatically
function getUserPose() {
  // image(video,0,0)
  console.log(skeleton);
  console.log(pose);

  // button click send Json with position / skelleton for python matching
  json = pose
  saveJSON(json, 'user.json')
}


