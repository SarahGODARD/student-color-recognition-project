// Team project 01.cpp

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>
#include<stdio.h> 

using namespace cv;
using namespace std;

int main(int ac, char **av)
{
	Mat image;

	string filename = "C:/input/ImageProImage.png";
	image = imread(filename);
	Vec3b intensity;
	int spottedRegion = -1;
	int currentRegion = 0;
	int maxColorCounted = 0;
	int colorCounter = 0;
	
	if (image.empty()) {
		//cout << "Could not open or find the image" << endl;
		cout << "-1" << endl;
		return (-1);
	}

	// Index des couleurs à comparer
	int mainColor = 2;
	int otherColor1 = 1;
	int otherColor2 = 0;

	if (ac > 1) {
		const char* str = av[1];
		if (sscanf_s(str, "%d", &mainColor) == EOF) {
			cout << "-1" << endl;
			return -1;
		}
			
		switch (mainColor) {
		case 0:
			otherColor1 = 1;
			otherColor2 = 2;
			break;
		case 1:
			otherColor1 = 0;
			otherColor2 = 2;
			break;
		case 2:
			otherColor1 = 0;
			otherColor2 = 1;
			break;
		}
	}


	int windowSizeHeight = image.rows / 3;
	int windowSizeWidth = image.cols / 3;
	bool isOutside = false;

	for (int y = 0; y < image.rows; y += windowSizeHeight) {
		for (int x = 0; x < image.cols; x += windowSizeWidth) {

			colorCounter = 0;
			isOutside = false;

			for (int windowY = 0; windowY < windowSizeHeight && isOutside == false; windowY++) {
				for (int windowX = 0; windowX < windowSizeWidth; windowX++) {
					if (y + windowY < image.rows && x + windowX < image.cols) {
						intensity = image.at<Vec3b>(windowY + y, windowX + x);

						if (intensity.val[mainColor] > 175 && intensity.val[otherColor1] < 70 && intensity.val[otherColor2] < 70)
							colorCounter++;
					}
					else {
						isOutside = true;
						break;
					}
				}
			}

			if (isOutside == false) {
				if (colorCounter > maxColorCounted) {
					maxColorCounted = colorCounter;
					spottedRegion = currentRegion;
				}
				currentRegion++;
			}

		}
	}

	if (spottedRegion == -1)
		cout << "-1" << endl;
	else
		cout << spottedRegion << endl;

	waitKey(0);
	return (0);
}