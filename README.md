# 证明题：仿射变换(Affine Transformation)中平行线变换后仍然是平行线

设`AB∥CD，A′，B′，C′，D′`分别是`A,B，C,D`经过某个仿射变换后的像。假设`A′B′`与`C′D'`不平行，则由于它们在同一个平面上，因此它们有公共点`P′`，所以点`P′`的原像`P`既在直线`AB`上，又在直线`CD`上。这与`AB∥CD`的前提矛盾，因此`A′B′∥C′D′`。

# 编程题：通过实验对比正向变换(Forward warping)与反向变换（inverse warping）对图像变形/扭曲(Image warps)结果的不同，且总结正向变换的缺点可能有哪些

在当前目录下运行`image_warping.py`即可得到正向变换与反射变换的结果。结果保存为当前目录下的`forward_warp_vs_inverse_warp.png`。程序使用`matplotlib`画出的1,2,3,4四个子图分别为原图，正向变换的结果，原图，反向变换的结果。

打开`forward_warp_vs_inverse_warp.png`，可以明显的看出正向变换的结果产生了大量空洞，并且在实现过程中会有像素的重叠，使`image warping`的结果不理想，而反向变换的图像则不会产生这种问题。

![contrast](https://raw.githubusercontent.com/vitalemonate/Image-Warping/main/forward_warp_vs_inverse_warp.png)

# 参考资料
* [OpenCV-doc getAffineTransform函数](https://docs.opencv.org/3.4.1/da/d54/group__imgproc__transform.html#ga8f6d378f9f8eebb5cb55cd3ae295a999)

* [OpenCV-doc warpAffine函数](https://docs.opencv.org/3.4.1/da/d54/group__imgproc__transform.html#ga0203d9ee5fcd28d40dbc4a1ea4451983)

* [Princeton University CS426 lectures, FALL 2000](https://www.cs.princeton.edu/courses/archive/fall00/cs426/lectures/warp/warp.pdf)

* [北京邮电大学2020秋季学期图像处理与图像识别课程lecture07](https://github.com/vitalemonate/Image-Warping/blob/main/L07-2D%20transformation.pdf)
