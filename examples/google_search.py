# (c) 2022-2023 Yoga Pranata a.k.a zYxDevs
# Google search example code.

from wibuapi import WibuAPI


client = WibuAPI()


print(client.google("game of thrones"))
"""
{
  "result": [
    {
      "title": "...",
      "link": "...",
      "snippet": "...",
    }
  ],
  "success": ...,
  "creator": "Yoga Pranata"
}
"""
