'''課後作業3：用命令行參數完成測試環境切換，這裡主要獲取不同環境的url，username，password'''


def test_env(getenv):
    print("測試環境驗證")
    env, datas = getenv
    print(f"環境：{env}，數據：{datas}")
    username = datas['env']['username']
    password = datas['env']['password']
    print(f"用戶名：{username},密碼：{password}")
