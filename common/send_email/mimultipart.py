# 发送附件  pytest+jenkins 下载工具就行  json文件
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
# 发送附件
from email.mime.multipart import MIMEMultipart
# 发送正文
from email.mime.text import MIMEText
# 头部
from email.utils import formataddr, parseaddr

from common.zip_file import Compress


def server_pre(msg):
    """邮件服务器基础设置"""
    con = smtplib.SMTP_SSL('smtp.qq.com', 465)
    con.login('961429475@qq.com', 'gqqzbwyedhjpbeef')
    con.send_message(msg)
    con.quit()


def send_listing(sender, receiver, _title, body):
    """
    发送邮件
    :param sender: 发件人账号
    :param receiver: 收件人账号
    :param _title: 邮件title
    :param body: 邮件正文
    :return:
    :
    """
    global message
    message = MIMEMultipart()
    message['From'] = formataddr(parseaddr('明月清风<wuggfox@foxmail.com>'))
    message['To'] = receiver
    message['Subject'] = _title
    message.attach(MIMEText(body))
    with open("zipfile/report.zip", 'rb') as f:
        # 这里附件的MIME和文件名，这里是xls类型
        mime = MIMEBase('zip', 'zip')
        # 加上必要的头信息
        mime.add_header('Content-Disposition', 'attachment', filename=('gb2312', '', '测试报告.zip'))
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来
        mime.set_payload(f.read())
        # 用Base64编码
        encoders.encode_base64(mime)
        message.attach(mime)
    server_pre(message)
    print(">>>发送邮件成功！")


if __name__ == '__main__':
    dirpath = os.path.dirname(os.path.dirname(__file__)) + '/allure_report'
    print(dirpath)
    outFullName = os.path.dirname(os.path.dirname(__file__)) + '/send_email/zipfile/report.zip'
    print(outFullName)
    Compress.zip_dirs(dirpath, file_o=outFullName)
    print('>>>压缩文件成功！')
    title = '-------测试报告---------'
    messages = '你好，今天是个好日子'
    send_listing('wuggfox@foxmail.com', 'wuggfox@foxmail.com', title, messages)
    # os.remove(outFullName)
    # shutil.rmtree(r'../zipfile/')
    # print('>>>删除文件成功！')
