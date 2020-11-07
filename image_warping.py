from matplotlib import pyplot as plt
import cv2
import numpy as np

img = cv2.imread('pictures/lena.jpg')
rows, cols, depth = img.shape

pts1 = np.float32([[50, 50],[200, 50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

# transform matrix
M = cv2.getAffineTransform(pts1, pts2)
M = np.asmatrix(M)

# forward_warp_pic是forward warped的结果, inverse_warp_pic是inverse warped的结果
forward_warp_pic = np.zeros_like(img)
inverse_warp_pic = np.zeros_like(img)

# 1.forward warping
# 遍历原图img，将img上所有的点transform到forward_warp_pic上
for d in range(depth):
    for v in range(rows):
        for u in range(cols):
            x = int(round(M[0,0]*u + M[0,1]*v + M[0,2]))
            y = int(round(M[1,0]*u + M[1,1]*v + M[1,2]))
            if x < 0 or x >= cols or y < 0 or y >= rows:
                continue
            forward_warp_pic[y,x,d] = img[v,u,d]

# 2.inverse warping
inverse_warp_pic = cv2.warpAffine(img, M, (rows, cols))

# 3.对比两种warp的结果
# 1，2，3,4四个子图分别为原图img，forward warped的结果forward_warp_pic,原图img以及inverse warped的结果inverse_warp_pic
plt.subplot(2, 2, 1)
plt.imshow(img)
plt.plot(pts1[:, 0], pts1[:, 1], "ro")
plt.title('original picture')

plt.subplot(2, 2, 2)
plt.imshow(forward_warp_pic)
plt.plot(pts2[:, 0], pts2[:, 1], "bo")
plt.title('forward warped picture')

plt.subplot(2, 2, 3)
plt.imshow(img)
plt.plot(pts1[:, 0], pts1[:, 1], "ro")
plt.title('original picture')

plt.subplot(2, 2, 4)
plt.imshow(inverse_warp_pic)
plt.plot(pts2[:, 0], pts2[:, 1], "bo")
plt.title('inverse warped picture')

plt.tight_layout()
plt.savefig(fname="results/forward_warp_vs_inverse_warp.png",dpi=100)
plt.show() 