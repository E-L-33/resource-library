#Git
##一、Git
>Git is s free and open source distributed version control sysytem

##二、创建版本库
* 安装完成后，需要在你的机器上初始化一下,不加的会在clone时报错，具体见**·问题·**栏

		~$:git config --global user.name "Your Name"
        ~$:git config --global user.email "Your Email"

	>git config命令的--global参数，用了这个参数，表示你这台机器上所有的Git仓库都会使		用这个配置，当然也可以对某个仓库指定不同的用户名和Email地址

* 在需要创建版本库的地方执行

		~$:git init
        ~$:#创建版本库或初始化一个已存在的版本库

* 修改文件完成后可使用

		~$:git add [file or directory]
    	~$:#将文件或者目录提交到暂存区

* 提交到仓库，`message`为提交的版本说明

		~$:git commit -m "message"

##三、版本控制
###1、状态查询
* 查询当前工作区的状态

    	~$:git status

* 查看文件的被修改的内容

		~$:git diff [file or directory]

* 显示文件的提交日志，加上`--pretty=oneline`参数可以精简输出信息

		~$:git log [--pretty=oneline]

	* 在`git log`显示的信息中最前面一列一大串字母和数字的组合就是后面用到的`commit id`，如`"1094a..."`

###2、版本回退
* 在Git中，用`HEAD`表示当前版本，上一版本为`HEAD^`，上上一版本为`HEAD^^`，上100个版本为`HEAD~100`
* 使用`git reset`命令回退版本

		~$:git reset --hard HEAD^
        ~$:#回退到上一个版本
    或者
    	~$:git reset --hard 1094a
    其中`1094a`为某个要回退版本的commit id的前几位，不用写全，系统会自动识别
    >Git回退版本的速度非常快，因为Git在内部有个指向当前版本的`HEAD指针`，当你回退版本时	 Git仅仅把HEAD改变指向，然后顺便把工作区的文件更新了
* 当回退了版本以后，找不到“未来”版本的`commit id`时，可以使用`git reflog`来查看你的每一次操作
		~$:git reflog

###3、撤销修改
* 撤销修改命令

		~$:git checkout -- [file or directory]

	* 当工作区文件修改后未添加到暂存区，撤销修改后文件回到和当前版本库一模一样的状态
	* 当工作区文件已经添加到暂存区，又做了修改，那此时撤销修改就会回到暂存区目前的状态
	* ————即回到最近一次`git commit`或者`git add`时的状态

>`git checkout`没有`--`参数会变成分支管理命令

* 当需要撤销暂存区的修改，回退到工作区时

		~$:git reset HEAD [filr or directory]
        ~$:# 需要继续撤销工作区的修改可继续使用
        ~$:git checkout -- [file or directory]

>`git reset`既可以回退版本，也可以把暂存区的修改回退到工作区。当我们用`HEAD`时表示最新版本

###4、删除文件

	~$:git rm [file or directory]
    ~$:git commit -m 'message'

**`git rm`和`rm`有什么区别？？！**

##四、远程仓库
###1、连接远程仓库
####建立SSH Key
* 在用户主目录下有`.ssh`文件，该目录下有`id_rsa`和`id_rsa.pub`文件，**其中`id_rsa`是私钥，`id_rsa.pub`是公钥**。登录github——“Add SSH Key”，在key文本框中粘贴公钥的内容就可以建立连接了
* 当找不到时，最好的办法就是创建一个啦：

		~$:ssh-keygen -t rsa -C "youremail@example.com"
	这里`ssh-keygen`是一个命令，中间没有间隔
    **Git初始化？？！**
    执行之后可看到屏幕提示：
	>Your identification has been saved in /root/.ssh/id_rsa.
	>Your public key has been saved in /root/.ssh/id_rsa.pub.

    再执行第一步操作即可

###2、添加远程库
在本地仓库下运行

	~$:git remote add origin git@github.com:yourgithubname/repositoryname

`yourgithubname/repositoryname`是你自己的github项目地址，添加完成后，`origin`就是远程库的名字了

###3、推送本地内容至远程库
将当前的master分支推送到远程

	~$:git push -u origin master


* `-u`参数，Git会把本地的master分支和远程master分支关联起来，在之后的推送或者拉取取时就可以简化命令为`git push origin master`

###4、从远程库克隆

	~$:git clone git@github.com:yourgithubname/repositoryname

git还支持https等协议，但默认的git使用SSH，速度最快

**************
##后续是分支及标签管理还有初次使用时的问题整理