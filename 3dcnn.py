'''notes on import'''
import argparse
import os

import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
import numpy as np
from keras.datasets import cifar10
from keras.layers import (Activation, Conv3D, Dense, Dropout, Flatten,
                          MaxPooling3D)
from keras.layers.advanced_activations import LeakyReLU
from keras.losses import categorical_crossentropy
from keras.models import Sequential
from keras.optimizers import Adam
from keras.utils import np_utils
from keras.utils.vis_utils import plot_model
from sklearn.model_selection import train_test_split

import videoto3d
from tqdm import tqdm

def main():
	'''define the argument when execute'''
	parser = argparse.ArgumentPaerser(
		description = 'ureca project 3D CNN for action recognition')
	#batch: use how many samples to train at a time
	parser.add_argument('--batch', type =int, default =128)
	#epoch: how many times tarin forward and backward
	parser.add_argument('--epoch', type =int, default =100)
	parser.add_argument('--dataset', type =str, default ='UCF101')
	parser.add_argument('--nclass', type =int, default =10)
	parser.add_argument('--output', type =str, default =True)
	parser.add_argument('--color', type =bool, default =False)
	parser.add_argument('--skip', type =bool, default =True)
	parser.add_argument('--depth', type =int, default = 10)
	#parse_args():
	args = parser.parse_args()

	'''initilize training sample and transfer dataset'''
	img_rows, img_cols, frames = 32, 32, args.depth
	#rgb chaannel or else
	channel = 3 if args.color else 1
	fname_npz = 'dataset_{}_{}_{}.npz'.format(args.nclass, args.depth, args.skip)

	vid3d = videoto3d.Videoto3D(img_rows, img_cols, frames)
	nb_class = args.nclass







if __name__ == '__main__':
	main()