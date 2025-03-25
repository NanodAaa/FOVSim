# 最小放大倍率计算工具

## 简介

该工具用于计算 CMS 系统的最小放大倍率, 在参数界面中输入 CMS 系统的各项参数后点击运行即可输出计算的结果以及各图表.

## 工具界面

### 主界面 - 显示 Monitor → World 坐标的计算结果

![image.png](./README/image%206.png)

**各标签定义**

Monitor, Sensor 默认以左上角为原点.

- MP_A, MP_B: Monitor 中点 A, B 的像素坐标.
- SP_C, SP_D: Sensor 中点 C, D 的像素坐标, (mm) 为 相对原点的毫米单位的坐标.
- SP_C_Conv, SP_D_Conv: 将点 C, D 的坐标原点转换为 Sensor 中心点后的坐标, (mm) 为 相对原点的毫米单位的坐标.
- WP_E, F: 转换后的世界坐标, E, F 两点的 Y 坐标将作为计算最小放大倍率的输入范围值 (E, F).

### 参数设置界面

![image.png](./README/image%207.png)

**各标签定义**

- MP_A, MP_B: Monitor 中点 A, B 的像素坐标.
- Pose: 相机的姿态 (Pitch, Yaw, Roll).
- FitCoe: 真实相高 (Real Height) vs. 入射角 (Angle) 的 5 阶多项式拟合函数的参数 x^5 → x^0.
- FitCoeR: 入射角 (Angle) vs. 真实相高 (Real Height) 的 5 阶多项式拟合函数的参数 x^5 → x^0.
- SenPrms: Sensor 的各项参数 (Width, Height, Pixel Size).
- MonPrms: Monitor 的各项参数 (Width, Height, Pixel Size).

### 最小放大倍率计算结果表格

![image.png](./README/image%208.png)

此界面展示 WP_E, WP_F 范围内均匀分布的 20 个点经 World → Monitor 变换后各阶段的值.

### 最小放大倍率计算结果图表

![image.png](./README/image%209.png)

**各图表定义**

- **Points distance from MP_A**: 显示 (WP_F, WP_E) 范围内 20 个点 Y 坐标距 WP_F 的 Y 坐标的距离 (mm).
    - Point distance from WP_F: 该点转换前的 Y 坐标距 WP_F 的 Y 坐标的距离 (mm).
    - Point distance from MP_A: 该点转换后的 X 坐标距 MP_A 的 X 坐标的距离 (pixel).
- **Magnification Factors of Points**: 显示 (WP_F, WP_E) 范围内 20 个点的经镜头后的放大倍率. 此图中的最小值即为 CMS 的最小放大倍率.
    - Point distance from WP_F: 该点转换前的 Y 坐标距 WP_F 的 Y 坐标的距离 (mm).
    - Magnification Factor: 放大倍率.
- **Points position on monitor**: (WP_F, WP_E) 范围内 20 个点变换后在 Monitor 上的位置.
    - Width: X 坐标.
    - Height: Y 坐标.