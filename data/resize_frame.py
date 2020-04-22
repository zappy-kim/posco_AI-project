from PIL import Image

count = 0

while count < 2959:

    image = Image.open('/home/pirl/test/project1/1202_night_frame/frame%d.png' %count)

    # print(image.size)

    resize_image = image.resize((512,512))

    resize_image.save('/home/pirl/test/project1/new_night_frame(512)/frame%d.png' %count)

    print('Saved frame%d.png' % count)

    count += 1
