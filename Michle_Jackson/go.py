import sys, os
import image2txt
import time

def getTxt(imagePath, txtPath):
	img_count = 1
	while img_count <= len(os.listdir(imagePath)):
		imageFile = imagePath + str(img_count) + '.png'
		txtFile = txtPath + str(img_count) + '.txt'
		image2txt.image2txt(imageFile, txtFile)
		print('MJ舞蹈加载中： ' + str(img_count) + '%')
		img_count += 1

def play(txtPath):
	txt_count = 1
	while txt_count <= len(os.listdir(txtPath)):
		os.system('type ' + txtPath + str(txt_count) + '.txt')
		txt_count += 1
		os.system('cls')

if __name__ == '__main__':
	txt_dir_path = r'D:\MJ\mjtxt' + '\\'
	img_dir_path = r'D:\MJ\mjimages' + '\\'
	getTxt(img_dir_path, txt_dir_path)
	play(txt_dir_path)
