# import uvicorn
# from core.app import app
# from config.serverConfig import HOST, PORT

# if __name__ == "__main__":
#     uvicorn.run("core.app:app", host=HOST, port=PORT, reload=True)


import uvicorn
from core.app import app
from config.serverConfig import HOST, PORT
    
if __name__ == "__main__":
    # Thay vì dùng HOST/PORT từ config, bạn có thể ghi đè trực tiếp 0.0.0.0 
    # để các thiết bị khác (Emulator/Mobile) có thể kết nối.
    uvicorn.run("core.app:app", host="0.0.0.0", port=8080, reload=True)