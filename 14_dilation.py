#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np



def special_dilation(im):
    im_new = 1 * im
    for i in range(len(im)):
        for j in range(len(im[i]) - 1):
            for k in range(im.shape[2]):
                im_new[i, j, k] = max(im[i, j, k], im[i, j + 1, k])
    return im_new


im = np.array([[[0.6, 0.5, 0.7], [0.0, 0.3, 0.2], [0.7, 0.5, 0.1]],
               [[0.4, 0.8, 0.7], [0.5, 0.3, 0.2], [0.6, 0.5, 0.3]],
               [[0.7, 0.7, 0.6], [0.8, 0.4, 0.3], [0.4, 0.8, 0.3]]])

im_new = special_dilation(im)
print(im_new)
print(np.sum(im_new))