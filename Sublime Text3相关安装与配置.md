# Sublime Text3安装与基础配置(Ubuntu)

##  Ubuntu下安装Sublime Text3
### 三步安装法
1. 添加sublime text 3的仓库：

		$:sudo add-apt-repository ppa:webupd8team/sublime-text-3
这地方需要我们确认是否添加这个仓库，按`enter`键继续，按`crtl+c`取消。
回车，建立信任数据库。

2. 更新软件库

		$:sudo apt update
3. 安装Sublime Text3

		$:sudo apt install sublime-text-installer

到这就完成啦，这里附带Sublime Text2的安装方法：

> 		$:sudo add-apt-repository ppa:webupd8team/sublime-text-2
> 		$:sudo apt update
> 		$:sudo apt install sublime-text-dev

## 安装Package Control
官方介绍：

> [A full-featured package manager](https://packagecontrol.io/packages/Package%20Control)

简而言之，Package Control是一款优秀的包管理工具。
安装方式的话，网上有很多，但是其中很多都”过期“了，这里也是提供[Package Control官方的方法](https://packagecontrol.io/installation#Simple)
最简单的安装方法是通过Sublime Text控制台。可通过快捷方式`` ctrl+` ``或`View > Show Console` 菜单访问控制台。打开后，将适用于您的Sublime Text版本的Python代码粘贴到控制台中。
具体代码见上面链接官方方法。官方也有警告：

> WARNING: Please do not redistribute the install code via another website. It will change with every release. Instead, please link to this page.
> 警告： 请不要通过其他网站重新分发安装代码。它会随着每个版本而改变。相反，请链接到此页面。

此外，如果通过代码形式行不通，那也可以通过手动建立文件的方式进行，具体见以上链接的官方方法

##  配置中文
配置中文我采用的是[Chinese​Localizations](https://packagecontrol.io/packages/ChineseLocalizations)插件，当然，你也可以使用别的。
不知道是不是GFW墙了的原因，导致常用的用Package Contol安装的方法下载不下来，所以这里提供了两种方法：

1. 用Package Control安装
在菜单栏中找到我们刚刚安装的Package Control，
`Preferences>Package Control`，然后输入`Install Package`，或者直接在下面选择，
然后输入`Chinese​Localizations`，
当然，这些命令都不用输完，下面会有提示，选择对应的就行。然后选择`Chinese​Localizations`就行。
当然，这之后你可能会报错
`Package Control:Unable to download Chinese​Localizations.Please view the console for more details.`
那么就参见下一种方法。

2. 使用git手动安装
注意.git后面是一个空格，然后接sublime text3包路径
		$:git clone -b st3 https://github.com/rexdf/ChineseLocalization.git ~/.config/sublime-text-3/Packages/ChineseLocalization

## 配置代码补全
Emmet是一款编辑器插件，支持多种编辑器支持。在前端开发中，Emmet 使用缩写语法快速编写 HTML、CSS 以及实现其他的功能，极大的提高前端开发效率。
## 一些有趣的插件
[参考](https://www.cnblogs.com/guanshuai/p/6511585.html)