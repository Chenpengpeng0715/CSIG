Data set lib
Version: v1.0.1
依赖环境
1.opencv-python(≥3.0)
2.numpy
3.scipy
4.random
5.shutil
6.pypinyin
git
python2: 
python3:
本工具函数库是有感于在实际工作中数据集从原始图片或者视频，到变成可以被输入到sdk进行测试的数据集，需要经过多道处理，而每个同学在这个过程中需要自己编写或使用脚本，同时，每个人手中有着实现类似功能但不同的脚本，造成了一定的不方便和浪费。因此，本着方便同学们使用和简化操作的目的，封装了在数据集准备过程中经常使用到的功能。欢迎各位同学在使用过程中提出宝贵的意见和一起改进扩展功能。
Lib 一共包含4个文件：
1.unit 基础模块
	1.读取图片
	imread(image_path)
	输入为图片的绝对路径，例如：/data/youtu/0001.jpg
	输出为经过编码的图片数据
	
	2.保存图片
	save_image(image,dirpath)
	输入编码图片数据，目标路径（具体到文件名.jpg，路径不存在会自动创建，文件名后缀必须为小写）,可在这里使用不同的后缀来更改保存的图片格式（支持jpg,png,bmp）。
	
	3.创建路径
	mkdir(path)
	输入要添加的路径，路径中没有的文件夹会创建。
	
	4.生成文件列表（可附带标签）
	makeFileLists(path, fileName='list.txt', withLabel=False, ext=['jpg', 'bmp', 'png'])
	功能，可用于包含多目录的文件列表创建。
	输入 文件夹路径（父目录），保存的文件名（路径），标签选项（否，不加；是，将文件所在文件夹名作为标签保存到最后的list.txt中），检索的文件类型。
	输出 存放list的文件
	
	5.视频抽帧
	video_extract(video_path, interval, target_path)
	功能，将视频文件按设定帧间隔提取为图片保存
	输入 存放视频文件的文件夹路径（同时对文件夹中所有视频文件抽帧），抽取帧间隔（如interval=10，则每10帧抽1张），保存的目标路径
	输出 提取的图片文件保存到目录路径下，保存格式，创建同名文件夹，在文件夹内按照“视频名_图片序号.jpg”格式保存。
	例如，视频为video_man.mp4 则图片名为 video_man_1.jpg

2.datapre 数据集准备
	1.替换文件名中的中文
	replace_Chinese(image_path, dictpath)
	输入为图片的绝对路径，替换字典的路径。 
	文件格式：
	中文 English

	rename_pinyin(testset_dir)
	输入图片所在文件夹路径，替换文件名中所以中文为拼音
	
	2.压缩
	compress(image_path, threshold, quality, dirpath)
	输入图片路径，阈值（大于阈值的文件才会被压缩，以字节为单位），质量(0-100)越低，压缩程度越大,存入路径（eg. C:/test/1.jpg）。
	Ps: png格式的文件压缩程度有限，如压缩后不满足需要，可以用save_image()转为jpg再压缩。
	
	3.裁剪提取人脸
	crop(image, rect)
	输入编码图片数据，人脸框信息list[left，top，width，height]。
	输出处理后编码图片数据。

	crop_all(image, rect)
	输入编码图片数据，人脸框信息list[left，top，width，height]。
	输出处理后编码图片数据。

	4.人脸摆正
	face_rotate(image, five_point)
	输入编码图片数据，人脸5点信息list[ ]。
	eg. List[0] = x_left_eye y_left_eye 中间空格分隔
	输出处理后编码图片数据。

	5.绘制特征点
	draw_points(image, point_list, r=3, color=(0,255,0))
	输入编码图片数据，特征的坐标list[ ]，绘制点的半径，绘制点的颜色(0,255,0) BGR。
	输出处理后编码图片数据。
	输出的数据image可以结合cv2.imshow("show",image) cv2.waitkey()看到展示。

	6.绘制框（可用于显示人脸框）
	draw_rect(image,rect,r=5,color=(0,255,0))
	输入编码图片数据，框信息list[left，top，width，height]，绘制框的半径，颜色(B,G,R)。
	输出处理后编码图片数据。
	输出的数据image可以结合cv2.imshow("show",image) cv2.waitkey()看到展示。

	7.抽取文件
	extract_image(path, rate, target_path,mode=1)
	输入要抽取的图片所在目录，抽取比例，目标目录，抽取模式。mode=1时，按顺序等间隔抽取，rate取值为正整数，如rate=3时，每3张抽取一张图片；mode=2时，随机抽取，rate取值为(0-1)，如有1000张图片，rate=0.3 ，则会随机抽取300张。
	8．给图片添加文字（可中文）
	image_add_text(img_path, text, rects, text_color=(255, 0, 0), text_size=100)
	参数依次为图片路径，文字，框，字体颜色，字体大小
3.operation 图像变换
	1.平移
	translate(image, x, y)
	输入编码图片数据，x轴平移距离，y轴平移距离。
	可搭配crop_black(image)搭配使用去除移动后黑边。
	输出处理后编码图片数据。

	2.旋转
	rotate(image, angle, mode=1, scale=1.0)
	输入编码图片数据，旋转角度（顺时针），mode=1 旋转后不改变尺寸（缺省），mode=2 旋转后完整显示（一般会变大），sacle为缩放系数。
	输出处理后编码图片数据。

	3.缩放
	3.1按照长宽缩放
	resize(image, width=None, height=None, inter=cv2.INTER_AREA)
	输入编码图片数据，缩放到的宽度，高度（只传入一项时，自动保持宽高比缩放），缩放方法：采用插值法,下采样时建议inter=cv2.INTER_AREA 上采样时建议cv2.INTER_LINEAR。
	输出处理后编码图片数据。
	
	3.2按照比例缩放
	Resize(image, x, mode=1)
	输入编码图片数据，缩放比例，mode=1放大图片，mode=2缩小图片
	输出处理后编码图片数据
	
	4.裁剪（可用于去除图片两侧出现公司logo的情况）
	cut_image(image, X_rate, Y_rate)
	输入编码图片数据，X轴裁剪比例，Y轴裁剪比例。
	输出处理后编码图片数据。

	5.去除黑边
	crop_black(image)
	输入编码图片数据。
	输出处理后编码图片数据。

4.perturbance 生成带扰动的图片
	1.模拟噪点
	gaussian_noise(image, degree=None)
	输入编码图片数据，噪点扰动程度degree,推荐值：10-50 高分辨率需要调高degree。degree越大，扰动程度越大。
	输出处理后编码图片数据。

	2.模拟对焦模糊（失焦）
	duijiao_blur(image, degree=5)
	输入编码图片数据，模糊程度degree为正奇数，degree越大，扰动程度越大。
	输出处理后编码图片数据。

	3.模拟运动模糊
	motion_blur(image, degree=20, angle=45)
	输入编码图片数据，模糊程度degree（建议不超过20），相对运动角度（顺时针0-360）degree越大，扰动程度越大。
	输出处理后编码图片数据。

	4.模拟光照问题（可用于修正光线问题）
	light_image(image, degree=1)
	输入编码图片数据，degree: 0-1范围内向过曝调整（越小越亮），1-n范围向欠曝（过暗）调整（越大越暗），低分辨率图片建议1.5-3，高分辨率图片可根据需要继续调整。
	输出处理后编码图片数据。

	5.创建遮挡
	occlusion(image,point,mask_size)
	输入编码图片数据，创建遮挡区域的左上角坐标，遮挡区域尺寸
	eg. occlusion(imagepath,(260,524),(90,60))
	输出处理后编码图片数据。

