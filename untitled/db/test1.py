import pymysql


def db_connect():
    connection = pymysql.connect(host='localhost', user='root', passwd='1234', db='db_sea', port=3306, charset='utf8')
    return connection


class Test1:
    def test_data(self,need_data):
        cur = db_connect().cursor()  # 游标(指针)cursor的方式操作数据
        sql = f"select {need_data} from env"  # sql语句
        cur.execute(sql)  # execute(query, args):执行单条sql语句
        test_data = cur.fetchall()
        cur.close()
        db_connect().close()
        return test_data


if __name__ == '__main__':
    all = Test1()
    print(all.test_data("*"))
    # content = all.test_data("*")