# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:35:25 2019

@author: Kasbah
"""

#%% AGISOFT PhotoScan 1.5.5 (API Python 3.7)

import PhotoScan
import os

	#Set variables
path_project = r'C:/Users/Kasbah/OneDrive - Universitat de Barcelona/Intercanvi/3_WORKFLOW_TESTS/Dades_treball_test_4/agisoft_files/'
name_project = r'Filter_tests3.psx'

doc = PhotoScan.app.document
doc.read_only = False
doc.save(path_project+name_project)
doc.read_only = False
doc.clear()
chunk_original = doc.addChunk()


#%%STEP0 -> Load images in camera groups

#path_master2 = PhotoScan.app.getExistingDirectory("Main folder:")
path_master = "C:/Users/Kasbah/OneDrive - Universitat de Barcelona/Intercanvi/3_WORKFLOW_TESTS/Dades_treball_test_4/Imatges"

sub_folders = os.listdir(path_master)
for folder in sub_folders:
	folder = os.path.join(path_master, folder)
	if not os.path.isdir(folder):
		continue

	image_list = os.listdir(folder)
	photo_list = list()
	new_group = chunk_original.addCameraGroup()
	new_group.label = os.path.basename(folder)
	for photo in image_list:
		if photo.rsplit(".",1)[1].lower() in  ["jpg", "jpeg", "tif", "tiff"]:
			photo_list.append(os.path.join(folder, photo))
	chunk_original.addPhotos(photo_list)
	for camera in chunk_original.cameras:
		if not camera.group:
			camera.group = new_group

print("Imatges carregades correctament")
#%% STEP 1 -> Calibration Camera Groups
            
for camera in chunk_original.cameras:   
    if camera.label[0:6] == "HRCam1":      
        sensor1 = chunk_original.addSensor()
        sensor1.label = camera.label
        sensor1.type = camera.sensor.type
        sensor1.calibration = camera.sensor.calibration
        sensor1.width = camera.sensor.width
        sensor1.height = camera.sensor.height
        sensor1.focal_length = camera.sensor.focal_length
        sensor1.pixel_height = camera.sensor.pixel_height
        sensor1.pixel_width = camera.sensor.pixel_width
        camera.sensor = sensor1
    
    elif camera.label[0:6] == "HRCam2":
        sensor2 = chunk_original.addSensor()
        sensor2.label = camera.label
        sensor2.type = camera.sensor.type
        sensor2.calibration = camera.sensor.calibration
        sensor2.width = camera.sensor.width
        sensor2.height = camera.sensor.height
        sensor2.focal_length = camera.sensor.focal_length
        sensor2.pixel_height = camera.sensor.pixel_height
        sensor2.pixel_width = camera.sensor.pixel_width
        camera.sensor = sensor2
        
    elif camera.label[0:6] == "HRCam3": 
        sensor3 = chunk_original.addSensor()
        sensor3.label = camera.label
        sensor3.type = camera.sensor.type
        sensor3.calibration = camera.sensor.calibration
        sensor3.width = camera.sensor.width
        sensor3.height = camera.sensor.height
        sensor3.focal_length = camera.sensor.focal_length
        sensor3.pixel_height = camera.sensor.pixel_height
        sensor3.pixel_width = camera.sensor.pixel_width
        camera.sensor = sensor3
        
    elif camera.label[0:6] == "HRCam4": 
        sensor4 = chunk_original.addSensor()
        sensor4.label = camera.label
        sensor4.type = camera.sensor.type
        sensor4.calibration = camera.sensor.calibration
        sensor4.width = camera.sensor.width
        sensor4.height = camera.sensor.height
        sensor4.focal_length = camera.sensor.focal_length
        sensor4.pixel_height = camera.sensor.pixel_height
        sensor4.pixel_width = camera.sensor.pixel_width
        camera.sensor = sensor4
        
    elif camera.label[0:6] == "HRCam5": 
        sensor5 = chunk_original.addSensor()
        sensor5.label = camera.label
        sensor5.type = camera.sensor.type
        sensor5.calibration = camera.sensor.calibration
        sensor5.width = camera.sensor.width
        sensor5.height = camera.sensor.height
        sensor5.focal_length = camera.sensor.focal_length
        sensor5.pixel_height = camera.sensor.pixel_height
        sensor5.pixel_width = camera.sensor.pixel_width
        camera.sensor = sensor5

for camera in chunk_original.cameras:   
    if camera.label[0:6] == "HRCam1":
        camera.sensor = sensor1
    if camera.label[0:6] == "HRCam2":
        camera.sensor = sensor2
    if camera.label[0:6] == "HRCam3":
        camera.sensor = sensor3
    if camera.label[0:6] == "HRCam4":
        camera.sensor = sensor4
    if camera.label[0:6] == "HRCam5":
        camera.sensor = sensor5

print("Grups de calibració realitzats correctament")

#%% STEP 2 -> Create and load masks
            
exec(open(r"C:/Users/Kasbah/OneDrive - Universitat de Barcelona/Intercanvi/3_WORKFLOW_TESTS/Dades_treball_test_4/scripts/Masking_files.py").read())

pathToMasks = 'C:/Users/Kasbah/OneDrive - Universitat de Barcelona/Intercanvi/3_WORKFLOW_TESTS/Dades_treball_test_4/masks/{filename}.JPG'            
for f in chunk_original.frames:
    f.importMasks(path=pathToMasks, source=PhotoScan.MaskSource.MaskSourceFile)

print("Imatges enmascarades correctament")

#%% STEP 3 -> Add markers (import markers    

marker1=chunk_original.addMarker()
marker2=chunk_original.addMarker()
marker3=chunk_original.addMarker()
marker4=chunk_original.addMarker()
marker5=chunk_original.addMarker()

for marker in chunk_original.markers:
    marker.reference.accuracy = [0.01,  0.01,   0.01]

marker1.reference.location = [-20.588,  114.760,    16.76]
marker2.reference.location = [-5.339,   114.879,    25.358]
marker3.reference.location = [7.042,    109.692,    22.037]
marker4.reference.location = [-34.656,  118.285,    23.403]
marker5.reference.location = [1.544,    110.234,    12.932]

for camera in chunk_original.cameras:
    if camera.label[0:6] == "HRCam1":
        marker1.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([4261.83, 1860.48]), True)            
        marker2.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([4905.41, 1287.13]), True)            
        marker3.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([5727.24, 1392.13]), True)            
        #marker4.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([3230.67, 1496.05]), True)   
        #marker5.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([5585.46, 1969.99]), False)     
    
    elif camera.label[0:6] == "HRCam2":
        marker1.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([2204.05, 1488.69]), True)            
        marker2.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([3046.72, 968.805]), True)            
        marker3.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([3788.14, 1062.98]), True)            
        marker4.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([1448.99, 1187.02]), True)   
        marker5.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([3488.89, 1618.48]), True)     
    
    elif camera.label[0:6] == "HRCam3":
        marker1.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([3473.14, 1533.4]), True)            
        marker2.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([4097.07, 1069.04]), True)            
        marker3.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([4819.92, 1176.99]), True)            
        #marker4.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([3230.67, 1496.05]), False)   
        #marker5.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([5585.46, 1969.99]), False)   
    
    elif camera.label[0:6] == "HRCam4":
        marker1.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([2326.38, 2277.07]), True)            
        marker2.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([3353.64, 1635.95]), True)            
        marker3.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([4186.16, 1722.91]), True)            
        marker4.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([1501.82, 1936.99]), True)   
        marker5.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([3811.02, 2410.58]), True)    
    
    elif camera.label[0:6] == "HRCam5":
        marker1.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([4347.78, 2234.95]), True)            
        marker2.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([5363.14, 1788.16]), True)            
        marker3.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([6235.99, 2018.9]), True)            
        marker4.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([3493.18, 1771.91]), True)   
        marker5.projections[camera] = PhotoScan.Marker.Projection(PhotoScan.Vector([5825.04, 2591.94]), True)   
        
print("Punts de control afegits correctament")
    
#%% STEP 4 -> Align and optimization Cameras       
            
chunk_original.matchPhotos(accuracy = PhotoScan.HighestAccuracy, generic_preselection=False, reference_preselection=False, filter_mask = True, keypoint_limit = 0, tiepoint_limit = 0) 

print("Punts homòlegs detectats correctament")

chunk_original.alignCameras()

print("Alineació de càmeres realitzada correctament")

#Optimize Cameras

chunk_original.optimizeCameras(fit_f=True,fit_cx=True,fit_cy=True,fit_b1=True,fit_b2=True,fit_k1=True,fit_k2=True,fit_k3=True,fit_k4=True,fit_p1=True,fit_p2=True,fit_p3=True,fit_p4=True,adaptive_fitting=False,tiepoint_covariance=False)

#Update Transform
chunk_original.updateTransform()

print("Optimització de càmeres realitzada")

#%% STEP 5 -> Point filtering

threshold_array=[10,1,0.7,0.5,0.4,0.3,0.2,0.1,0.05]
     
for i in range(0,9):
    
    for camera in chunk_original.cameras:
        camera.enabled = True

    threshold = threshold_array[i]
    print('Iteració amb threshold = ' + str(threshold))
    threshold_name = '_f_' + str(threshold)
    f = PhotoScan.PointCloud.Filter()
    f.init(chunk_original, criterion = PhotoScan.PointCloud.Filter.ReprojectionError)
    f.selectPoints(threshold)
    f.removePoints(threshold)

    #Optimize Cameras (again after treshold)
    
    chunk_original.optimizeCameras(fit_f=True,fit_cx=True,fit_cy=True,fit_b1=True,fit_b2=True,fit_k1=True,fit_k2=True,fit_k3=True,fit_k4=False,fit_p1=True,fit_p2=True,fit_p3=False,fit_p4=False,adaptive_fitting=False,tiepoint_covariance=False)
    
    #Update Transform
    chunk_original.updateTransform()
    
    print("Optimització de càmeres realitzada")
    
    f = PhotoScan.PointCloud.Filter()
    f.init(chunk_original, criterion = PhotoScan.PointCloud.Filter.ReprojectionError)
    f.removePoints(threshold)
    
    print("Filtratge realitzat correctament")
    
    #%% STEP 6 -> Duplicate Chunk and dissable cameras    

    chunk_original.resetRegion()
    
    chunk_copy = chunk_original.copy()
    
    for i in range(3,28,6):
        
        camera = chunk_original.cameras[i]
        camera.enabled = False
        camera = chunk_original.cameras[i+1]
        camera.enabled = False
        camera = chunk_original.cameras[i+2]
        camera.enabled = False
        label_lastday = camera.label[7:15] + threshold_name
    
    for i in range(0,25,6):
        
        camera = chunk_copy.cameras[i]
        camera.enabled = False
        camera = chunk_copy.cameras[i+1]
        camera.enabled = False
        camera = chunk_copy.cameras[i+2]
        camera.enabled = False
        label_firstday = camera.label[7:15] + threshold_name         
    
    chunk_original.label = label_firstday
    chunk_copy.label = label_lastday
    
    #%% STEP 7 -> Dense Cloud Computation
      
    for chunk in doc.chunks:
        chunk.resetRegion()
        chunk.buildDepthMaps(quality=PhotoScan.UltraQuality, filter=PhotoScan.MildFiltering)
        chunk.buildDenseCloud(point_colors=True,keep_depth=True)
    
    #%% STEP 8 -> Dense Clouds color filtering
        
    #for chunk in doc.chunks:       
        #chunk.image_brightness = 150
        #chunk.image_contrast = 1200
        #dense_cloud = chunk.dense_cloud
        #dense_cloud.selectPointsByColor(color=[0,0,0], tolerance=100, channels='RGBHSV')
        #dense_cloud.removeSelectedPoints()
        
    #%% STEP 9 -> Export Dense Clouds
        
    path_save = 'C:/Users/Kasbah/OneDrive - Universitat de Barcelona/Intercanvi/3_WORKFLOW_TESTS/Dades_treball_test_4/resultats/{chunklabel}_nocolor.xyz'  
    
    for chunk in doc.chunks:  
        chunk.exportPoints(path_save, source = PhotoScan.DenseCloudData, binary=True, precision=3, normals=True, colors=True, colors_rgb_8bit=True, format=PhotoScan.PointsFormatXYZ)
    # doc.save()      
    doc.remove(chunk_copy)

print("Codi finalitzat")