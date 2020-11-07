## 证明题

* 仿射变换(`Affine Transformation`)中平行线变换后仍然是平行线

  设`AB∥CD，A′，B′，C′，D′`分别是`A,B，C,D`经过某个仿射变换后的像。假设`A′B′`与`C′D'`不平行，则由于它们在同一个平面上，因此它们有公共点`P′`，所以点`P′`的原像`P`既在直线`AB`上，又在直线`CD`上。这与`AB∥CD`的前提矛盾，因此`A′B′∥C′D′`。
---

## 编程题

* 通过实验对比正向变换(`Forward warping`)与反向变换（`inverse warping`）对图像变形/扭曲(`Image warps`)结果的不同，且总结正向变换的缺点可能有哪些

  在当前目录下运行`image_warping.py`即可得到正向变换与反射变换的结果。结果保存为当前目录下的`forward_warp_vs_inverse_warp.png`。程序使用`matplotlib`画出的1,2,3,4四个子图分别为原图，正向变换的结果，原图，反向变换的结果。

  如下图所示，可以明显的看出正向变换的结果产生了大量空洞，并且在实现过程中会有像素的重叠，使`image warping`的结果不理想，而反向变换的图像则不会产生这种问题。

<div style="text-align: center;">
<img src="https://raw.githubusercontent.com/vitalemonate/Image-Warping/main/results/forward_warp_vs_inverse_warp.png"/>
</div>

---
## 两张图片看懂Forward Warping和Inverse Warping

### Forward Warping
![Forward Warping Image](https://raw.githubusercontent.com/vitalemonate/Image-Warping/main/pictures/forward_warping_implement.png)

`Forward Warping`的原理：遍历`source image`中的每个点`p_source`，乘以从`source image`到`destination image`的`affine transform matrix`，将其投影到`destination image`中得到`p_destination`，如果`p_destination`的坐标不是整数，则进行四舍五入取整，这必然会产生问题：`destination image`中有的位置没有从`source image`中投影过来的点，有的位置有多个从`source image`中投影过来的点，所以会产生很多空洞，产生类似波纹的效果

### Inverse Warping
![Inverse Warping Image](https://raw.githubusercontent.com/vitalemonate/Image-Warping/main/pictures/inverse_warping_implement.png)

`Inverse Warping`的原理：遍历`destination image`中的每个点`p_destination`，乘以`destination image`到`source image`的`affine transform matrix`，得这个点在`source image`中的对应点`p_source`，令`p_destination`的像素值等于`p_source`的值，如果`p_source`的坐标不是整数，则采用**插值逼近**的方法进行近似，因此不会产生上文提到的`Forward Warping`的问题

## OpenCV中的`warpAffine`函数

* 由下图中列出的公式可知，OpenCV中的`warpAffine`的实现是基于`Inverse Warping`的

![OpenCV warpAffine](https://raw.githubusercontent.com/vitalemonate/Image-Warping/main/pictures/opencv-doc-warpAffine.png)

说明：
* 当`WARP_INVERSE_MAP`被指定时，函数的输入参数`M`表示从`destination image`到`source image`的**2×3**的`transform matrix`,可以直接遍历`destination image`中的每个像素点，代入上图中的公式进行`affine transform`


* 当`WARP_INVERSE_MAP`没有被指定时，`M`表示从`source image`到`destination image`的`affine transform matrix`，在函数内部首先会调用另一个函数`invertAffineTransform`求出`M`的逆，仍然是**2×3**的`affine transform matrix`,然后再代入上图中的公式进行`affine transform`

* `flages`表示**插值方式**与`WARP_INVERSE_MAP`的组合，默认为 `flags=cv2.INTER_LINEAR`，表示线性插值，此外还有：`cv2.INTER_NEAREST`（最近邻插值）,`cv2.INTER_AREA`（区域插值）,`cv2.INTER_CUBIC`（三次样条插值）和`cv2.INTER_LANCZOS4`（Lanczos插值）

![OpenCV warpAffine](https://raw.githubusercontent.com/vitalemonate/Image-Warping/main/pictures/WARP_INVERSE_MAP.png)


* `borderValue`表示边界填充值，默认值为0，因此可能出现“黑边”现象


* 一般情况下`cv2.warpAffine(img,M,(rows,cols))`即可完成基本的`affine transform `
---
## 参考资料
* [OpenCV-doc getAffineTransform函数](https://docs.opencv.org/3.4.1/da/d54/group__imgproc__transform.html#ga8f6d378f9f8eebb5cb55cd3ae295a999)

* [OpenCV-doc warpAffine函数](https://docs.opencv.org/3.4.1/da/d54/group__imgproc__transform.html#ga0203d9ee5fcd28d40dbc4a1ea4451983)

* [Princeton University CS426 lectures, FALL 2000](https://www.cs.princeton.edu/courses/archive/fall00/cs426/lectures/warp/warp.pdf)

* [北京邮电大学2020秋季学期图像处理与图像识别课程lecture07](https://github.com/vitalemonate/Image-Warping/blob/main/lectures/L07-2D%20transformation.pdf)
