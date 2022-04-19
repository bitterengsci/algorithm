
# Image Processing

图像平滑算子、边缘检测算子
图像去噪滤波算法（高斯、均值、双边、Guide filter）
三个度量patch相似度的方法（SSD、SAD、NCC）
二进制描述子
计算描述子距离函数
描述一下SIFT或者SURF特征检测、匹配
SIFT的4个不变性
特征点、描述子ORB、SIFT、SURF、BRIEF等等 。geometric invariance：平移，旋转，尺度……; photometric invariance：亮度，曝光……
Mat实现、Mat类指针引用复制函数
颜色直方图统计，手撕代码
形态学操作，手撕代码
积分图，手撕代码
连通区域算法，给二值图，求出最大联通区域（用深度优先和广度优先算法，手撕代码）
Mser、Swt检测
图像分割（Grabcut）
目标跟踪（相关滤波KCF）

Feature: SIFT、SURF、ASIFT、ORB、HOG

Edge Detector: Robert prewit sobel 拉普拉斯 canddy

Mosaic

LBP特征。原理，如何计算相似性（汉明距离），汉明距离怎么计算
相机的3A参数（自动对焦（AF）、自动曝光（AE）及自动白平衡（AWB））

# Visual Inertial Odometry

# SLAM
landmark参数化方式、对比，逆深度参数化；点线面因子图优化
滤波+回环（Trifo-VIO）
outlier+鲁棒核、RANSAC
EKF更新方程
AR系统如何实现
介绍下VO
Gridmap（网格标0、1）给定起点和终点，求最优路径（A*或其他路径规划算法）
相似变换、仿射变换、射影变换的区别
E和F的区别，自由度计算
单应矩阵H的求取
PNP算法、ICP算法（二维码、手眼标定）
闭环检测常用方法（orb、lsd、深度学习）
单目的初始化（拓展：双目，RGBD，VIO的初始化及传感器标定），其他：https://github.com/frobelbest/GSLAM
简述一下Bundle Adjustment的过程
SVO、LSD中深度滤波器原理
说一说某个SLAM框架的工作原理（svo、orb、lsd）及其优缺点，如何改进？
RANSAC的框架
位姿不同表示间的相互转化、旋转矩阵特征值和特征向量物理意义
真实世界到相机照片的变换可看成射影变换
直接法与特征点法的优缺点对比
常见滤波方法的对比（KF、EKF、IEKF、UKF、PF）
双目测距范围Z=fb/d。问题： 640*480，fov＝90°，zmax＝10m，最小视差为2，求使zmax稳定的最小基线长度（6.25cm）
特征点法与直接法误差模型、Jacobian推导
光流的假设、仿射变换、4种方法，svo采取的方法，优势何在
MSCKF与ROVIO、MSCKF与预积分（structureless factor）
边缘化方式原理
grid_map

# 3D Geometry
进行立体匹配
MVS、SFM、SCM分别代表什么
已知左相机R1、T1和右相机R2、T2怎么算基线
ICP迭代算法

知道深度图和相机内参数A。外参数R、T，怎么获取三维点云
立体匹配算法有哪些，具体的思想是什么？
点云拼接和融合有什么异同

视差匹配原理
推深度相机模型公式，推双目相机成像公式

基本矩阵，本征矩阵，旋转矩阵特性，
相机标定

极线矫正原理，矫正完后内参怎么变换？极线矫正除了bougent方法外，还有其他哪些方法？
极线校正的本质是什么，是怎么做的
极线校正前后的不变量

双目恢复的三维点云会有空洞，怎么解决

怎么判断空间点云在相机成像面上

对于n个实例的k维数据，建立kd tree的时间复杂度
三维空间最近邻搜索的常用数据结构（八叉树、kd tree）

绝对二次曲线，绝对二次曲线和相机内参有什么关系

单目相机如何初始化和三角化 (单目初始化和2种方法)

BA问题, 相机投影模型的Jacobian
鲁棒核函数

边缘化过程&可能存在的问题


如何求解Ax=b (非迭代Cholesky分解、QR分解，迭代)
最小二乘封闭解与迭代解的取舍
梯度下降法、牛顿法、GN、LM，推导、优缺点
如何判断点在多边形内


《Keyframe-based monocular SLAM: design, survey, and future directions》
《Past, Present, and Future of Simultaneous Localization And Mapping: Towards the Robust-Perception Age》
《Visual Place Recognition: A Survey》
《Simultaneous Localization and Mapping: A Survey of Current Trends in Autonomous Driving》
《Visual SLAM and Structure from Motion in Dynamic Environments: A Survey》
《A Benchmark Comparison of Monocular Visual-Inertial Odometry Algorithms for Flying Robots》
《GSLAM: A General SLAM Framework and Benchmark》
《Survey on Computer Vision for UAVs: Current Developments and Trends》
《Semantic mapping for mobile robotics tasks: A survey》
《A Review on Deep Learning Techniques Applied to Semantic Segmentation》
《Deep Learning for Generic Object Detection: A Survey》

特征匹配
- 距离度量 (欧氏距离, 马氏距离, 汉明距离)
- 匹配策略 (最近邻搜索, 最近邻距离比)

多视角立体技术
- 基于体素
- 基于空间patch扩散
- 基于深度图融合 (优点)
    - 全局视角和局部视角的选择? 区域生长法扩张? 非线性深度优化流程?

稠密重建:
稠密点云获取方式
极线搜索
两个假设 (光度一致性, 可视性约束)


Pinhole camera model


OpenMVG 的BA怎么做的?


Egomotion: 3D motion of a camera within an environment. 
- estimate a camera's motion relative to a rigid scene.
- photometric loss + geometric loss
- depth estimation + ego motion (trajectory) estimation



camera calibration (哪些parameters involved? 具体怎么做的)

planar-based calibration

vanishing point

vanishing plane


fundamental matrix (in geometry sense?? )

epipolar line in geometry sense?


homogeneous coordinate system point at infinity [x, y, z, 0]

monocular depth estimation


trust-region based optimization