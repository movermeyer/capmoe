# -*- coding: utf-8 -*-
"""
    :synopsis: 最もナイーブな画像検索

・leaning setのSIFTとる
・クエリ画像のSIFTとる(N個)
・クエリ画像のi個目(i = 1 ~ N)の特徴ベクトルに、最も近い特徴ベクトルを各learning set要素からとる。
  全要素の内、最も近いものにvoteする。
・全vote数N個のうち、もっとも大きいvoteを集めた画像が答え
"""


# python 2.x support
from __future__ import division, print_function, absolute_import, unicode_literals

# standard modules
import time
from os.path import basename
import sys

# 3rd party modules
import cv2
import numpy as np

# original modules
import capmoe.util.logger


FEATURE_DIR = '/home/nakatani/git/capmoe/test/images/features'
IMGS        = [
    '/home/nakatani/git/capmoe/test/images/%s' % (img)
    for img in (
        '1a-crop.jpg',
        '2b-crop.jpg',
        '3a-crop.jpg',
        '4a-crop.jpg',
        '5a-crop.jpg',
    )
]
logger = capmoe.util.logger.factory(__file__)


def get_features(im):
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    detector = cv2.SURF(400, 5, 5)
    t0 = time.time()
    kps, descs = detector.detectAndCompute(im, None)
    logger.debug('feature detection: %f sec' % (time.time() - t0))
    return (kps, descs)


def save_descriptors(imgpath, descriptors):
    np.save('%s.npy' % (imgpath), descriptors)


def create_features():
    for impath in IMGS:
        im = cv2.imread(impath)
        kps, descs = get_features(im)
        save_descriptors(impath, descs)


def dist(desc1, desc2):
    return np.power(desc1 - desc2, 2).sum()


def nearest_dist(desc, descs):
    min_d = float('inf')
    for desc2 in descs:
        d = dist(desc, desc2)
        if d < min_d:
            min_d = d
    return min_d


def search(query_imgpath):
    im = cv2.imread(query_imgpath)
    kps, descs = get_features(im)

    vote = {basename(img): 0 for img in IMGS}
    for j, desc in enumerate(descs):
        logger.info('start vote#%d/%d' % (j, len(descs)))

        min_dist = {'d': float('inf'), 'img': None}
        for i, target_descs in enumerate((np.load('%s.npy' % (imgpath)) for imgpath in IMGS)):
            # t0 = time.time()
            d = nearest_dist(desc, target_descs)
            # logger.debug('calc min distance: %f sec' % (time.time() - t0))

            if d < min_dist['d']:
                min_dist['img'] = basename(IMGS[i])
                min_dist['d']   = d
        # vote for most similar image
        vote[min_dist['img']] += 1
        logger.info('voted to %s' % (min_dist['img']))

    # logger.info('Most possible image: %s' % (min_dist['img']))
    logger.info('vote: %s' % (vote))


if __name__ == '__main__':
    logger.setLevel('DEBUG')

    if len(sys.argv) == 1:
        logger.info('[create feature mode]')
        create_features()
    elif len(sys.argv) == 2:
        logger.info('[search mode]')
        search(sys.argv[1])
    else:
        assert(False)
