import cv2
import os
import torch
import pandas as pd
import numpy as np
from scipy import spatial

import posenet

class Webcam_processing():
    
    def __init__(self,path,filename, output_filename):
        self.cam = cv2.VideoCapture(0)
        self.filename = filename
        self.output_filename = output_filename
        self.path = path
        self.df = pd.read_csv("poses_final_sample_v1.csv")
    
    
    def take_picture(self):
        """
        This function take a picture from the webcam and compute its pose
        """
        self.flag = False
        s, img = self.cam.read()
        
        if s:
            cv2.imwrite(self.path+self.filename,img)
            _, raw_pose = self.compute_pose()
            self.pose = raw_pose[0][0]
            self.flag = True
            return self.path+self.filename
        else:
            raise Exception("Webcam was unable to take the picture")
    
    
    def compute_pose(self):
        """
        This function compute the pose of the picture taken
        """
        scale_factor = 1.0
        
        pose_scores_acc = []
        keypoint_scores_acc = []
        keypoint_coords_acc = []
        
        model = posenet.load_model(101)
        output_stride = model.output_stride
        
        input_image, draw_image, output_scale = posenet.read_imgfile(
            self.path+self.filename, scale_factor=scale_factor, output_stride=output_stride)

        with torch.no_grad():
            input_image = torch.Tensor(input_image)

            heatmaps_result, offsets_result, displacement_fwd_result, displacement_bwd_result = model(input_image)

            pose_scores, keypoint_scores, keypoint_coords = posenet.decode_multiple_poses(
                heatmaps_result.squeeze(0),
                offsets_result.squeeze(0),
                displacement_fwd_result.squeeze(0),
                displacement_bwd_result.squeeze(0),
                output_stride=output_stride,
                max_pose_detections=10,
                min_pose_score=0.25)

        keypoint_coords *= output_scale
        
        pose_scores_acc.append(pose_scores)
        keypoint_scores_acc.append(keypoint_scores)
        keypoint_coords_acc.append(keypoint_coords)

        draw_image = posenet.draw_skel_and_kp(
                draw_image, pose_scores, keypoint_scores, keypoint_coords,
                min_pose_score=0.25, min_part_score=0.25)

        cv2.imwrite(self.path + self.output_filename, draw_image)
        
        return self.path + self.output_filename, keypoint_coords_acc
    
    
    def get_pose(self):
        """
        This function return the pose as an array
        """
        if self.flag:
            return self.pose
        else:
            raise Exception("Last photo failed or no photo taken")
    
    
    def get_output(self):
        """
        This function return the path to the image with the skeleton detected on it.
        """
        if self.flag:
            return self.path + self.output_filename
        else:
            raise Exception("Last photo failed or no photo taken")

            
    def closest_match(self):
        """
        This function get the closest image identifier to the pose taken
        """
        pose = self.normalize_posenet_vector(self.get_pose())
        
        self.df["distance"] =\
        self.df.norm_poses.apply(
            lambda poses : min([self.cosine_similarity(p, self.get_pose()) for p in eval(poses)]))
        
        best_index = self.df["distance"].idxmin()
        
        if np.isnan(best_index):
            return -1
        else:
            return self.df.iloc[best_index]["image_identifier"]
    
    
    def normalize_posenet_vector(self,vecteur):
        """
        This function normalize a posenet vector so that it stay exactly in a 1x1 square, without deformation.
        """

        x_components, y_components = zip(*vecteur)

        x_components, y_components = np.array(x_components), np.array(y_components)


        max_amplitude = max(max(x_components)-min(x_components),max(y_components)-min(y_components))

        amplification_factor = 1/max_amplitude

        x_components = amplification_factor*x_components
        y_components = amplification_factor*y_components

        def mean_extrema(array):
            return np.mean((max(array),min(array)))

        x_components, y_components =\
        x_components-mean_extrema(x_components) + 1/2, y_components-mean_extrema(y_components) + 1/2

        return list(zip(x_components, y_components))
    
    
    def cosine_similarity(self,pose1, pose2):
        """
        Classic pose similarity.
        """
        return spatial.distance.cosine(np.array(pose1).flatten(),np.array(pose2).flatten())
    
if __name__ == "__main__":
    wb = Webcam_processing("webcam_images/","image_webcam.png","skeleton_webcam.png")
    wb.take_picture()
    print(wb.closest_match())