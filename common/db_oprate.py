import configparser

import pymysql


class OperateDB:
    def __init__(self, config_path, db):
        # 实例config工具
        config = configparser.ConfigParser()
        # 从配置文件里读取数据库服务器IP  账号 密码.....
        config.read(config_path)
        host = config[db]['host']
        port = int(config[db]['port'])
        user = config[db]['user']
        passwd = config[db]['passwd']
        db_name = config[db]['database']
        charset = config[db]['charset']
        try:
            self.con = pymysql.connect(host=host, port=port, user=user,
                                       password=passwd, database=db_name, charset=charset)
        except Exception as e:
            print('初始化数据库连接失败：%s' % e)
        self.cur = self.con.cursor()

    # 增删改查
    def select_query(self, sql):
        try:
            # 执行sql语句
            self.cur.execute(sql)
            # 显示结果
            result = self.cur.fetchall()
            return result
        except Exception as e:
            print('查询失败%s' % e)

    def insert_query(self, sql):
        try:
            # 执行sql语句
            self.cur.execute(sql)
            self.cur.execute('commit')
            return True
        except Exception as e:
            self.cur.execute('rollback')
            print('语句增删改失败%s' % e)


if __name__ == '__main__':
    operate = OperateDB('../config/db.ini', 'TEST_DB')
    sql = 'select host,user from mysql.user f where user="root"'
    result = operate.select_query(sql)
    sql1 = 'SELECT f.first_name,f.last_name,g.department_name from hrdb.employees f ,hrdb.departments g WHERE f.department_id=g.department_id;'
    r1 = operate.select_query(sql1)
    print(r1)
