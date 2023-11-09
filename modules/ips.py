import IP2Location, os
import modules.database_manager as database_manager
import asyncio

async def get_ip_info(ip: str):
  database = await database_manager.get_database()
  rec = await asyncio.to_thread(database.get_all, ip)
  
  return rec

# print("Country Code          : " + rec.country_short)
# print("Country Name          : " + rec.country_long)
# print("Region Name           : " + rec.region)
# print("City Name             : " + rec.city)
# print("ISP Name              : " + rec.isp)
# print("Latitude              : " + rec.latitude)
# print("Longitude             : " + rec.longitude)
# print("Domain Name           : " + rec.domain)
# print("ZIP Code              : " + rec.zipcode)
# print("Time Zone             : " + rec.timezone)
# print("Net Speed             : " + rec.netspeed)
# print("Area Code             : " + rec.idd_code)
# print("IDD Code              : " + rec.area_code)
# print("Weather Station Code  : " + rec.weather_code)
# print("Weather Station Name  : " + rec.weather_name)
# print("MCC                   : " + rec.mcc)
# print("MNC                   : " + rec.mnc)
# print("Mobile Carrier        : " + rec.mobile_brand)
# print("Elevation             : " + rec.elevation)
# print("Usage Type            : " + rec.usage_type)
# print("Address Type          : " + rec.address_type)
# print("Category              : " + rec.category)
# print("District              : " + rec.district)
# print("ASN                   : " + rec.asn)
# print("AS                    : " + rec.as_name)