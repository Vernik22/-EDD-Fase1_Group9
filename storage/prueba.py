from storage import principal as j

print(j.createDatabase('db1','avl','ascii'))      # 0
print(j.createDatabase('db1','avl','ascii'))      # 2
print(j.createDatabase('db4','b','ascii'))      # 0
print(j.createDatabase('db5','bplus','ascii'))      # 0
print(j.createDatabase('db1','bplus','ascii'))      # 0
print(j.createDatabase('db1','avl','ascii'))      # 0
print(j.createDatabase('db5','isam','ascii'))      # 0
print(j.createDatabase('db1','hash','ascii'))      # 0
print(j.createDatabase('db1','dict','ascii'))      # 0