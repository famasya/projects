import csv
import bisect
import geoip2.database

# collection of ranges, each range is a tupple of (starting ip, ending ip, country)
ranges = []
# array of starting ip for searching
keys = []

# read from database to collect ip ranges
with open('GeoIPCountryWhois.csv', 'rb') as f:
  reader = csv.reader(f)
  for row in reader:
      ip_start = int(row[2])
      ip_end = int(row[3])
      ranges.append((ip_start, ip_end, row[5], row[0], row[1]))
      keys.append(ip_start)
      
ip_list = geoip2.database.Reader("GeoLite2-City.mmdb")

def ip_to_country(ip):
  # convert IP to integer
  if(":" in ip):
      return "Unknown"
  (o1, o2, o3, o4) = ip.split('.')
  i_ip = 16777216 * int(o1) + 65536 * int(o2) + 256 * int(o3) + int(o4)

  result = None

  # I dont have to sort the ranges because those ranges are already sorted in the
  # Mindmax database

  # using bisect to find the position i that every key goes before i will smaller
  # or equal to i_ip
  index = bisect.bisect(keys, i_ip)

  # if the position is greater than 0, the one before that position is the greatest
  # which is smaller or equal to i_ip
  if index > 0:

      # get that range
      found_range = ranges[index - 1]

      # if ending ip is greater or equal to i_ip, return the country name
      if found_range[1] >= i_ip:
          result = found_range[2]

      # otherwise, the IP doesn't belong to any ranges
      else:
          result = "Unknown"
  # if the position is 0, the IP doesn't belong to any ranges
  else:
      result = "Unknown"

  return result

def ip_to_city(ip, loc=False):
    try:
        response = ip_list.city(ip)
        if(loc):
            return response.location.latitude,response.location.longitude
        else:
            return response.city.name
    except:
        return "Unknown"
print ip_to_city("10.252.108.90")