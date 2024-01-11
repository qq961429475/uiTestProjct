import smtplib
# 发送头部
from email.header import Header
# 发送邮件正文
from email.mime.text import MIMEText
# 美化”地址中的姓名部分
from email.utils import parseaddr, formataddr


def send_email(sender_account, receiver_account, txt):
    # 创建邮箱服务器  邮局  SMTP_SSL(邮箱链接地址，端口号)
    # 邮箱链接地址：smtp.xx.com  端口号:自己去查
    # 163邮箱  网易邮箱  qq邮箱
    con = smtplib.SMTP_SSL('smtp.qq.com', 465)
    # 163邮箱  qq邮箱 设置一下 用户名是邮箱名  密码：授权密码  qq邮箱--设置--账号--POP3/SMTP服务开启
    con.login('wuggfox@foxmail.com', 'gqqzbwyedhjpbeef')
    message = MIMEText(_text=txt, _charset='utf-8')
    # 设置头部 设置标题
    message['Subject'] = Header('测试报告')
    # 发件人
    message['from'] = formataddr(parseaddr('明月清风<wuggfox@foxmail.com>'))
    # 接受人 的信息
    message['To'] = Header('接受者<961429475@qq.com>')
    try:
        # 发送邮件  由谁发送  邮局发送 con  发送邮件失败
        con.sendmail(sender_account, receiver_account, message.as_string())
        print('发送邮件成功')
    except Exception:
        print('无法发送邮件')
    # 关闭服务器连接
    con.quit()


if __name__ == '__main__':
    txt = '本文章向大家介绍Python的os的文件复制，主要包括Python的os的文件复制使用实例、应用技巧、基本知识点总结和需要注意事项，具有一定的参考价值，需要的朋友可以参考一下。'
    send_email('wuggfox@foxmail.com', 'wuggfox@foxmail.com', txt)
