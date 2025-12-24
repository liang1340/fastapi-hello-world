from fastapi import FastAPI
# 创建 FastAPI应用
app = FastAPI(
    title="我的API",
    description="简单的计算API",
    version="1.0.0",
    docs_url="/docs",  # 确保文档路径存在
    redoc_url="/redoc"  # 确保ReDoc路径存在
)

@app.get("/")
def read_root():
    return {"message":"HELLO WORLD! FastAPI 正在运行！ ","location":"D盘"}

@app.get("/calculate/{number}")
def calculat_square(number: int):
    """
    计算一个数字的平方
    """
    square = number * number
    return {
        "number":number,
        "square":square,
        "massage":f"{number}的平方是{square}"
    }
@app.get("/hea;th")
def health_check():
    return {"status":"OK","service":"FastAPI"}
#如果要直接运行这个文件
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0",port=8000)





