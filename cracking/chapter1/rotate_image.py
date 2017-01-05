
def rotate_image(image):
    for i in range(0, len(image)):
        for j in range(i+1, len(image[i])):
            image[i][j], image[j][i] = image[j][i], image[i][j]


if __name__ == "__main__":
    image = [[1,2,3],[4,5,6],[7,8,9]]
    rotate_image(image)
    print image
