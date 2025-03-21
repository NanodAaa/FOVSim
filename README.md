# 最小放大倍率-工作笔记

Date: February 27, 2025
Last edited time: March 17, 2025 3:30 PM

# 基础信息:

### 平均放大倍率:

![image.png](/images/WorkNotes/image.png)

---

# 最小放大倍率测试:

## 测试方法:

![image.png](/images/WorkNotes/image%201.png)

## 测试信息记录:

左边缘(原图): 左2

右边缘: 右

相机距离图像: 75mm

中点线像素 x 坐标: 图像左→右

显示器像素尺寸: 0.1521 mm

显示器像素坐标:
19 40 63 86 111 137 165 192 222 251 283 314 347 379 411 444 476 507 538 568 597 625 651 678 702

---

# 最小放大倍率计算:

## 计算方法:

![image.png](/images/WorkNotes/image%202.png)

![最小放大倍率.png](/images/WorkNotes/%E6%9C%80%E5%B0%8F%E6%94%BE%E5%A4%A7%E5%80%8D%E7%8E%87.png)

1. 显示屏幕边缘的两个点AB，映射到Sensor平面点CD
2. Sensor平面两个点映射到墙面点EF
3. EF之间平均分布插入20个点
4. 将20个点重新投影到屏幕平面
5. 通过这20个点计算最小放大倍数

## 1. Monitor 点 A,B → Sensor 平面点 C,D:

[屏幕点 A,B → Sensor 平面点 C,D 草稿](https://www.notion.so/A-B-Sensor-C-D-1a79e6730e5f8024bde8f19d7d1dc0ee?pvs=21)

通过映射算法将 A, B 点像素坐标映射为 C, D 点像素坐标.

Sensor 平面坐标原点为左上角

### **参数:**

- Sensor 分辨率: 1920 * 1536
- 显示器分辨率: 720 * 540
- A 点像素坐标: (702, 270)
- B 点像素 X 坐标: (19, 270)

### **映射算法:**

![image.png](/images/WorkNotes/image%203.png)

![image.png](/images/WorkNotes/image%204.png)

### 计算结果:

- C 点像素坐标: (1872, 768)
- D 点像素坐标: (51, 768)

## 2. Sensor 平面点 C,D → 墙面点 E,F :

### 像素坐标→世界坐标, 其中:

- Sensor 平面 与 E,F 所在平面 的距离:
- 显示器像素尺寸: 0.1521 mm
- Sensor像素尺寸: 0.003 mm
- Angle vs Real Height 拟合函数的各阶参数: ?
- C 点像素 X 坐标: 1872
- D 点像素 X 坐标: 51
- C→F, D→E

详情见: [世界坐标与Sensor坐标互换](https://www.notion.so/Sensor-1a79e6730e5f8033afa4dfbe98c4ae14?pvs=21) 

<aside>
💡

使用 图像坐标 → 相机坐标工具, **注意: 此工具反转计算时, 输入的Sensor坐标以Sensor中心为原点! 使用时需进行坐标变换.**

</aside>

$$
x'=x−960
$$

![image.png](/images/WorkNotes/image%205.png)

- 坐标变换后 C 点像素 X 坐标为 (912, 0), 图像 X 坐标为 (2.736, 0)
- 坐标变换后 D 点像素 X 坐标为 (-909, 0), 图像 X 坐标为 (-2.727, 0)

### 计算结果:

- F 坐标 (0, 2181.7, 2000)
- E 坐标 (0, -2168.79, 2000)

## 3. EF之间平均分布插入20个点:

- 输入: 范围 [E, F]
- 输出: [E, F] 范围内 20 个点的坐标

## 4. 将20个点重新投影到屏幕平面:

1. 输入: [E, F] 范围内 20 个点的坐标
2. 对 20 个点分别应用:
    1. 世界坐标 (mm) → Sensor 坐标 (像素).
    2. Sensor 坐标进行线性变换, 使原点位置从 Sensor 中心变为 Sensor 左上角.
    3. Sensor 坐标 (像素) → 显示器坐标 (mm).

## 5. 计算最小放大倍率