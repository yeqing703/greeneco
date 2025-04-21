import psycopg2

conn = psycopg2.connect("postgresql://postgres:n3NNuQt0Z7pKTmbk@db.lprctmqyclfvyveblbin.supabase.co:5432/postgres")
print("✅ 数据库连接成功！")
conn.close()

