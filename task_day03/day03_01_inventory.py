from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

device_list = [
    {'name': 'R1', 'type': 'router', 'version': 'IOS XE 17.14', 'location': 'Beijing-IDC-A'},
    {'name': 'R2', 'type': 'router', 'version': 'IOS XE 17.14', 'location': 'Shanghai-IDC-B'},
    {'name': 'SW1', 'type': 'switch', 'version': 'IOS 15.2', 'location': 'Beijing-IDC-A'},
    {'name': 'SW2', 'type': 'switch', 'version': 'IOS 15.2', 'location': 'Shanghai-IDC-B'},
    {'name': 'FW1', 'type': 'firewall', 'version': 'ASA 9.16', 'location': 'Beijing-IDC-A'},
    {'name': 'FW2', 'type': 'firewall', 'version': 'FTD 7.2', 'location': 'Shenzhen-IDC-C'},
]

Base = declarative_base()

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), index=True)
    type = Column(String(50))
    version = Column(String(50))
    location = Column(String(100))
    create_time = Column(DateTime, default=datetime.now)
        
engine = create_engine("sqlite:///device_inventory.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

if session.query(Device).count() == 0:
    for item in device_list:
        device = Device( 
            name = item["name"],
            type = item["type"],
            version = item["version"],
            location = item["location"]
            )
        session.add(device)

session.commit()

while True:
    option = input("""请选择查询方式：
    输入 1:查询所有设备
    输入 2:根据设备名称查询
    输入 3:根据设备类型查询
    输入 4:根据机房位置查询
    输入 0:退出
    """)
    if option == "1":
        devices = session.query(Device).all()
    elif option == "2":
        device_name = input("请输入设备名称: ")
        devices = session.query(Device).filter_by(name=device_name).all()
    elif option == "3":
        device_type = input("请输入设备类型(router/switch/firewall)：")
        devices = session.query(Device).filter_by(type=device_type).all()
    elif option == "4":
        device_location = input("请输入机房位置关键词：")
        devices = session.query(Device).filter(Device.location.like(f"%{device_location}%")).all()
    elif option == "0":
        break
    for device in devices:
        print(f"Device(设备名称: {device.name} | 类型: {device.type} | 版本: {device.version} | 位置: {device.location} | 入库时间: {device.create_time}")