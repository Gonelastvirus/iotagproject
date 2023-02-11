from channels.generic.websocket import AsyncJsonWebsocketConsumer
from iotapp.models import SensorData,DailySensorData
import json
from django.db.models import Avg 
from pytz import timezone, UTC
import datetime
from channels.db import database_sync_to_async
class DashConsumer(AsyncJsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.time_zone = timezone('Asia/Kathmandu')
        self.last_date = None  # added here
    async def connect(self):
        if self.scope["user"].is_anonymous or self.scope["user"].is_superuser:
            await self.close()
        else:
            device_username=str(self.scope['user'])
            self.room_name=f"personal_dash_{device_username}"
            await self.channel_layer.group_add(
                self.room_name,
                self.channel_name,
            )
            print(f'[{self.room_name}]-You are connected')
            await self.accept()
        
    async def disconnect(self,code_close):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name,
        )
        #await self.disconnect()
        pass
    async def receive(self, text_data):
        datapoint = json.loads(text_data)
        val =datapoint['value']
        node=datapoint['node']
        temp=datapoint['temp']
        timestamp = datetime.datetime.now(self.time_zone)
        #timestamp = self.time_zone.localize(datetime.datetime.now())
        date = timestamp.date()  #get date before converting it into string
        # get the date from the timestamp
         # get the user from the scope
        user = self.scope['user']
        print(user)
        # check if the user is anonymous
        if user.is_anonymous:
            # handle anonymous user
            pass
        else:
            print(timestamp)
            time=(timestamp.strftime("%H:%M:%S"))
            # create a new SensorData model instance and save it to the database
            sensor_data = SensorData(user=user, sensor_value=val, timestamp=timestamp)
            await database_sync_to_async(sensor_data.save)()
            if date!= self.last_date:
                await self.save_daily_average(user,date)
                # flush the SensorData table for the user
                await database_sync_to_async(SensorData.objects.filter(user=user).delete)()
            self.last_date=date
      # send the sensor data to the group
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type':'deprocessing',
                'value':val,
                'node':node,
                'temp':temp,
                'time':time,
                
            }
        )
        print(f"{node}"+ " "+f"{val}"+" "+"Receive")
    async def deprocessing(self,event):
        valOther=event['value']
        node=event['node']
        temp=event['temp']
        time=event['time']
        await self.send(text_data=json.dumps({'value':valOther,'node':node,'temp':temp,'time':time}))
    async def save_daily_average(self, user, date):
        # get the daily sensor data for the user and date
        daily_sensor_data = SensorData.objects.filter(user=user, timestamp__date=date)

        # calculate the average sensor value for the day
        average_sensor_value = (await database_sync_to_async(daily_sensor_data.aggregate)(Avg('sensor_value'))).get('sensor_value__avg')

        # create a new DailySensorData model instance and save it to the database
        daily_data = DailySensorData(user=user, date=date, average_sensor_value=average_sensor_value)
        await database_sync_to_async(daily_data.save)()
