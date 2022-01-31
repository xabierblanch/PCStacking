# Point Cloud Stacking: A Workflow to Enhance 3D Monitoring Capabilities Using Time-Lapse Cameras
Author: Xabier Blanch<br/>
Contact: xabierblanch@gmail.com<br/>
Publication: https://www.mdpi.com/2072-4292/12/8/1240

Code developed in MATLAB to perform the PCStacking algorithm on point clouds. The basic principle of the PCstacking algorithm is straightforward: it computes the median of the Z coordinates of each point for multiple photogrammetric models to give a resulting point cloud with a greater precision than any of the individual point cloud.

* More information is detailed in the [article](https://www.mdpi.com/2072-4292/12/8/1240) 

Codes developed as part of a doctoral research at Universtiy of Barcelona (PhD). All these codes are developed for a particular case, some modifications will be necessary. If you use these codes or if they inspire you in your work, please share it with me :D (And cite it correctly).

How to cite:
-----

Blanch, X.; Abellan, A.; Guinau, M. Point Cloud Stacking: A Workflow to Enhance 3D Monitoring Capabilities Using Time-Lapse Cameras. Remote Sens. 2020, 12, 1240. https://doi.org/10.3390/rs12081240

Graphical Abstract:
-----

![image](https://user-images.githubusercontent.com/37353398/151721717-f6eade1e-17ab-4fe3-827c-fcb7ada27309.png)

Usage
-----

* [NP_Promig_3D_function.m](NP_Promig_3D_function.m) -> MATLAB code that performs the PCStacking process.

* [NP_Sintetic_function.m](https://github.com/xabierblanch/PCStacking/blob/main/NP_Sintetic_function.m) -> MATLAB code that randomly generates 3D point clouds (from a mathematical function)

* [Script_control_test.m](https://github.com/xabierblanch/PCStacking/blob/main/Script_control_test.m) -> MATLAB code that automatically performs the comparison of point clouds. Run the following .bat code: [Script_Comparacio_DEFORMATION_2.bat](https://github.com/xabierblanch/PCStacking/blob/main/Script_Comparacio_DEFORMATION_2.bat) 

Contribute
-----

Contributions are always welcome!
Feel free to contact me: xabierblanch@gmail.com

License
-----

Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)<br/><br/>
[![CC0](https://licensebuttons.net/i/cc-gift-guide/by-sa.png)](https://creativecommons.org/licenses/by-sa/4.0/)
