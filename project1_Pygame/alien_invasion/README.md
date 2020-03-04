# 外星人入侵: 使用 Python 开发游戏
	在项目 “ 外星人入侵 ” 中,将使用 Pygame 包来开发一款 2D 游戏,
	它在玩家每消灭一群向下移动的外星人后,都将玩家提高一个等级;
	而等级越高,游戏的节奏越快,难度越大。
	完成这个项目后,将获得自己动手使用 Pygame 开发 2D 游戏所需的技能。

# 项目分析：
	1、武装飞船：
		1）安装Pygame：
			使用pip安装包
		2）创建项目：
			窗口、用户输入、背景色、创建设置类
		3）开始添加飞船图像：
			创建ship类、显示飞船
		4）重构：
			模块game_function
		5）驾驶飞船（控制）：
			响应按键、不断左右移动、速度调整、限制范围、重构check_events
		6）射击：
			添加子弹设置、创建Bullet类、将子弹存储到编组中、开关控制、删除已消失的子弹、限制子弹数量、
			创建函数update_bullets()、fire_bullets()

	2、外星人：
		1）创建外星人：
			Alien类、显示、确认行容量、行数、群、加行
		2）外星人群移动：
			创建移动方向的设置、边界检测、下移变化
		3）击杀外星人：
			检测子弹与外星人碰撞、创建大量子弹测试、生成新外星人群、提高子弹的速度
		4）结束游戏：
			检测有外星人与飞船碰撞、响应碰撞结果、检测有外星人到达屏幕底线、game over

	3、记分系统：
		1）添加 Play 按钮
		2）提高等级
		3）记分